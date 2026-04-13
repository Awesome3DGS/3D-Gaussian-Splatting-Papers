#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import os
import re
import sys
import time
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode, urlparse
from urllib.request import Request, urlopen
from xml.etree import ElementTree


ARXIV_API_ENDPOINT = "https://arxiv.org/api/query"
ARXIV_SCHEMA_NS = "http://arxiv.org/schemas/atom"
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom", "arxiv": ARXIV_SCHEMA_NS}
HEADERS = {"User-Agent": "3dgs-archive-acceptance-check/1.0"}


def project_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "README.md").exists():
            return parent
    return Path.cwd()


PROXY_FILE = project_root() / ".PROXY"

ENTRY_SPLIT_RE = re.compile(r"(?m)^#### \[(\d+)\] ")
LINK_LINE_RE = re.compile(r"^- \*\*🔗 链接\*\*[:：]\s*(.*)$", re.M)
NOTE_LINE_RE = re.compile(r"^- \*\*📝 说明\*\*[:：]\s*(.*)$", re.M)
ARXIV_LINK_RE = re.compile(r"\[\[arXiv:(\d{4}\.\d{5})(?:v\d+)?\]")
ARXIV_ID_FROM_URL_RE = re.compile(r"(\d{4}\.\d{5})(?:v\d+)?$")
CODE_LINK_RE = re.compile(r"\[\[Code\]\((https?://[^)\s]+)\)\]")
CODE_LINK_FALLBACK_RE = re.compile(r"\[Code\]\((https?://[^)\s]+)\)")
GITHUB_URL_RE = re.compile(r"https?://(?:www\.)?github\.com/[^\s<>\]\"')]+", re.IGNORECASE)
ARXIV_HTML_GITHUB_HREF_RE = re.compile(r'href="(https?://github\.com/[^"]+)"', re.IGNORECASE)

README_REFS = ("HEAD", "main", "master")
ACCEPTANCE_KEYWORDS = (
    "accepted",
    "cvpr",
    "eccv",
    "iccv",
    "neurips",
    "siggraph",
    "iclr",
    "aaai",
    "acm mm",
    "miccai",
    "icml",
    "3dv",
    "wacv",
    "icra",
    "iros",
    "published in",
    "journal ref",
)

EXCLUDED_ARXIV_HTML_GITHUB_OWNERS = {"arxiv", "brucemiller", "html_feedback"}
DISCOVERY_SOURCE_CONFIDENCE = {
    "arxiv_comment": 3,
    "arxiv_html": 2,
    "github_search": 1,
}
DISCOVERY_SOURCE_ORDER = {
    "arxiv_comment": 0,
    "arxiv_html": 1,
    "github_search": 2,
}
TRAILING_URL_PUNCTUATION = ".,;:!?)]}>'\""


@dataclass(frozen=True)
class PaperEntry:
    source: str
    source_file: str
    entry_index: int
    title: str
    arxiv_id: str
    code_url: str


@dataclass(frozen=True)
class ArxivEntry:
    arxiv_id: str
    title: str
    journal_ref: str
    comment: str
    github_urls_in_comment: list[str]
    has_journal_ref: bool
    keyword_hits: list[str]
    found: bool


@dataclass(frozen=True)
class RepoReadmeCheck:
    repo: str
    ok: bool
    ref: str
    readme_url: str
    status_code: int
    keyword_hits: list[str]
    snippets: list[str]
    error: str


@dataclass(frozen=True)
class CodeDiscoveryHit:
    source: str
    url: str
    repo: str
    confidence: int
    extra: dict[str, object]


def _install_proxy() -> None:
    if not PROXY_FILE.exists():
        return
    proxy = PROXY_FILE.read_text(encoding="utf-8").strip()
    if not proxy:
        return
    import urllib.request

    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({"http": proxy, "https": proxy})
    )
    urllib.request.install_opener(opener)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Check acceptance signals for archive/README papers via arXiv metadata, "
            "GitHub README keyword matching, and code-link discovery."
        )
    )
    parser.add_argument(
        "--archive-glob",
        default="archive/*.md",
        help="Glob pattern for archive markdown files (default: archive/*.md).",
    )
    parser.add_argument(
        "--readme",
        type=Path,
        default=Path("README.md"),
        help="README markdown path (default: README.md).",
    )
    parser.add_argument(
        "--output-dir",
        type=Path,
        default=Path("tmp"),
        help="Output directory for report/json (default: tmp).",
    )
    parser.add_argument(
        "--batch-size",
        type=int,
        default=100,
        help="arXiv id_list batch size, must be in [1,100] (default: 100).",
    )
    parser.add_argument(
        "--batch-sleep",
        type=float,
        default=3.0,
        help="Seconds to sleep between arXiv API batches (default: 3.0).",
    )
    parser.add_argument(
        "--timeout",
        type=float,
        default=None,
        help=(
            "Set both arXiv and GitHub HTTP timeouts. "
            "If omitted, --arxiv-timeout/--github-timeout are used."
        ),
    )
    parser.add_argument(
        "--arxiv-timeout",
        type=float,
        default=30.0,
        help="arXiv HTTP timeout seconds (default: 30).",
    )
    parser.add_argument(
        "--github-timeout",
        type=float,
        default=8.0,
        help="GitHub README/search HTTP timeout seconds (default: 8).",
    )
    parser.add_argument(
        "--arxiv-retries",
        type=int,
        default=2,
        help="Retry count for each arXiv batch on fetch/parse failure (default: 2).",
    )
    parser.add_argument(
        "--arxiv-retry-sleep",
        type=float,
        default=2.0,
        help="Sleep seconds between arXiv batch retries (default: 2.0).",
    )
    parser.add_argument(
        "--github-token",
        default="",
        help="GitHub token for search API (fallback: env GITHUB_TOKEN).",
    )
    parser.add_argument(
        "--skip-github-search",
        action="store_true",
        help="Skip GitHub Search API fallback for code discovery.",
    )
    args = parser.parse_args()
    if args.batch_size <= 0 or args.batch_size > 100:
        parser.error("--batch-size must be between 1 and 100.")
    if args.batch_sleep < 0:
        parser.error("--batch-sleep must be >= 0.")
    if args.timeout is not None and args.timeout <= 0:
        parser.error("--timeout must be > 0.")
    if args.arxiv_timeout <= 0:
        parser.error("--arxiv-timeout must be > 0.")
    if args.github_timeout <= 0:
        parser.error("--github-timeout must be > 0.")
    if args.arxiv_retries < 0:
        parser.error("--arxiv-retries must be >= 0.")
    if args.arxiv_retry_sleep < 0:
        parser.error("--arxiv-retry-sleep must be >= 0.")
    if args.timeout is not None:
        args.arxiv_timeout = args.timeout
        args.github_timeout = args.timeout
    return args


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def file_timestamp_now() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")


def clean_text(value: str | None) -> str:
    return " ".join((value or "").replace("\xa0", " ").split())


def ordered_unique(items: Iterable[str]) -> list[str]:
    seen: set[str] = set()
    ordered: list[str] = []
    for item in items:
        if item in seen:
            continue
        seen.add(item)
        ordered.append(item)
    return ordered


def chunked(items: list[str], size: int) -> Iterable[list[str]]:
    for start in range(0, len(items), size):
        yield items[start : start + size]


def parse_arxiv_id_from_entry_id(raw_id: str) -> str:
    candidate = raw_id.rsplit("/", 1)[-1].strip()
    match = ARXIV_ID_FROM_URL_RE.search(candidate)
    if not match:
        return ""
    return match.group(1)


def extract_arxiv_id(text: str) -> str:
    match = ARXIV_LINK_RE.search(text)
    if not match:
        return ""
    return match.group(1)


def extract_code_url(text: str) -> str:
    match = CODE_LINK_RE.search(text)
    if match:
        return match.group(1).strip()
    fallback = CODE_LINK_FALLBACK_RE.search(text)
    if fallback:
        return fallback.group(1).strip()
    return ""


def extract_github_repo(code_url: str) -> str:
    if not code_url:
        return ""
    try:
        parsed = urlparse(code_url)
    except ValueError:
        return ""
    host = (parsed.netloc or "").lower()
    path_parts = [part for part in parsed.path.split("/") if part]
    if host in {"github.com", "www.github.com"}:
        if len(path_parts) < 2:
            return ""
        owner, repo = path_parts[0], path_parts[1]
        if repo.endswith(".git"):
            repo = repo[:-4]
        if owner and repo:
            return f"{owner}/{repo}"
        return ""
    if host == "raw.githubusercontent.com":
        if len(path_parts) < 2:
            return ""
        owner, repo = path_parts[0], path_parts[1]
        if owner and repo:
            return f"{owner}/{repo}"
    return ""


def normalize_github_url(raw_url: str) -> tuple[str, str, str]:
    candidate = raw_url.strip().strip("<>").rstrip(TRAILING_URL_PUNCTUATION)
    if not candidate:
        return "", "", ""
    try:
        parsed = urlparse(candidate)
    except ValueError:
        return "", "", ""

    host = (parsed.netloc or "").lower()
    if host not in {"github.com", "www.github.com"}:
        return "", "", ""

    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        return "", "", ""

    owner = parts[0]
    repo = parts[1]
    if repo.endswith(".git"):
        repo = repo[:-4]
    if not owner or not repo:
        return "", "", ""

    normalized_repo = f"{owner}/{repo}"
    normalized_url = f"https://github.com/{normalized_repo}"
    return normalized_url, normalized_repo, owner.lower()


def extract_github_urls_from_text(
    text: str,
    excluded_owners: set[str] | None = None,
) -> list[str]:
    excluded = {owner.lower() for owner in (excluded_owners or set())}
    urls: list[str] = []
    seen: set[str] = set()

    for match in GITHUB_URL_RE.finditer(text):
        normalized_url, _repo, owner_lower = normalize_github_url(match.group(0))
        if not normalized_url:
            continue
        if owner_lower and owner_lower in excluded:
            continue
        if normalized_url in seen:
            continue
        seen.add(normalized_url)
        urls.append(normalized_url)

    return urls


def parse_markdown_entries(
    path: Path,
    source: str,
    require_empty_note: bool,
) -> tuple[list[PaperEntry], list[str]]:
    entries: list[PaperEntry] = []
    parse_errors: list[str] = []
    text = path.read_text(encoding="utf-8")
    parts = ENTRY_SPLIT_RE.split(text)

    for i in range(1, len(parts), 2):
        index_text = parts[i]
        block = parts[i + 1]
        try:
            entry_index = int(index_text)
        except ValueError:
            parse_errors.append(f"{path.as_posix()}: invalid entry index {index_text!r}; skipped")
            continue

        if "\n" not in block:
            parse_errors.append(
                f"{path.as_posix()}#{entry_index}: malformed block without newline; skipped"
            )
            continue

        title, body = block.split("\n", 1)

        if require_empty_note:
            note_match = NOTE_LINE_RE.search(body)
            if not note_match:
                parse_errors.append(
                    f"{path.as_posix()}#{entry_index}: missing note line; skipped"
                )
                continue
            note_value = clean_text(note_match.group(1))
            if note_value and note_value != "---":
                continue

        link_match = LINK_LINE_RE.search(body)
        link_text = link_match.group(1) if link_match else body
        arxiv_id = extract_arxiv_id(link_text)
        if not arxiv_id:
            arxiv_id = extract_arxiv_id(body)
        if not arxiv_id:
            parse_errors.append(
                f"{path.as_posix()}#{entry_index}: missing arXiv id in link block; skipped"
            )
            continue

        code_url = extract_code_url(link_text)
        entries.append(
            PaperEntry(
                source=source,
                source_file=path.as_posix(),
                entry_index=entry_index,
                title=clean_text(title),
                arxiv_id=arxiv_id,
                code_url=code_url,
            )
        )

    return entries, parse_errors


def find_archive_entries(paths: list[Path]) -> tuple[list[PaperEntry], list[str]]:
    all_entries: list[PaperEntry] = []
    all_errors: list[str] = []
    for path in paths:
        entries, parse_errors = parse_markdown_entries(
            path=path,
            source="archive",
            require_empty_note=False,
        )
        all_entries.extend(entries)
        all_errors.extend(parse_errors)
    return all_entries, all_errors


def find_readme_entries(path: Path) -> tuple[list[PaperEntry], list[str]]:
    return parse_markdown_entries(path=path, source="readme", require_empty_note=True)


def keyword_hits(text: str) -> list[str]:
    lowered = text.lower()
    return [keyword for keyword in ACCEPTANCE_KEYWORDS if keyword in lowered]


def extract_keyword_snippets(
    text: str,
    keywords: list[str],
    context_chars: int = 60,
    max_snippets: int = 30,
) -> list[str]:
    lowered = text.lower()
    snippets: list[str] = []
    seen: set[str] = set()

    for keyword in keywords:
        start = 0
        while True:
            index = lowered.find(keyword, start)
            if index == -1:
                break
            left = max(0, index - context_chars)
            right = min(len(text), index + len(keyword) + context_chars)
            excerpt = clean_text(text[left:right]).replace("|", "/")
            if left > 0:
                excerpt = "…" + excerpt
            if right < len(text):
                excerpt = excerpt + "…"
            snippet = f"{keyword}: {excerpt}"
            if snippet not in seen:
                seen.add(snippet)
                snippets.append(snippet)
                if len(snippets) >= max_snippets:
                    return snippets
            start = index + len(keyword)

    return snippets


def request_bytes(
    url: str,
    timeout: float,
    extra_headers: dict[str, str] | None = None,
) -> tuple[bytes, int]:
    request_headers = dict(HEADERS)
    if extra_headers:
        request_headers.update(extra_headers)
    request = Request(url, headers=request_headers)
    with urlopen(request, timeout=timeout) as response:
        status = int(getattr(response, "status", 200))
        return response.read(), status


def decode_bytes(data: bytes) -> str:
    return data.decode("utf-8", errors="replace")


def build_arxiv_batch_url(arxiv_ids: list[str]) -> str:
    query = urlencode({"id_list": ",".join(arxiv_ids), "max_results": str(len(arxiv_ids))})
    return f"{ARXIV_API_ENDPOINT}?{query}"


def fetch_arxiv_batch(arxiv_ids: list[str], timeout: float) -> dict[str, ArxivEntry]:
    url = build_arxiv_batch_url(arxiv_ids)
    data, _status = request_bytes(url, timeout=timeout)
    feed = ElementTree.fromstring(data)
    records: dict[str, ArxivEntry] = {}
    for entry in feed.findall("atom:entry", ATOM_NS):
        arxiv_id = parse_arxiv_id_from_entry_id(
            entry.findtext("atom:id", default="", namespaces=ATOM_NS)
        )
        if not arxiv_id:
            continue
        title = clean_text(entry.findtext("atom:title", default="", namespaces=ATOM_NS))
        journal_ref = clean_text(entry.findtext("arxiv:journal_ref", default="", namespaces=ATOM_NS))
        comment = clean_text(entry.findtext("arxiv:comment", default="", namespaces=ATOM_NS))
        hits = keyword_hits(" ".join([journal_ref, comment]))
        github_urls_in_comment = extract_github_urls_from_text(comment)
        records[arxiv_id] = ArxivEntry(
            arxiv_id=arxiv_id,
            title=title,
            journal_ref=journal_ref,
            comment=comment,
            github_urls_in_comment=github_urls_in_comment,
            has_journal_ref=bool(journal_ref),
            keyword_hits=hits,
            found=True,
        )
    return records


def fetch_arxiv_records(
    arxiv_ids: list[str],
    batch_size: int,
    batch_sleep: float,
    timeout: float,
    retries: int,
    retry_sleep: float,
) -> tuple[dict[str, ArxivEntry], list[str]]:
    all_records: dict[str, ArxivEntry] = {}
    errors: list[str] = []
    batches = list(chunked(arxiv_ids, batch_size))
    for index, batch in enumerate(batches, start=1):
        print(
            f"[arXiv] batch {index}/{len(batches)} ids={len(batch)} ({batch[0]}..{batch[-1]})",
            file=sys.stderr,
        )
        for attempt in range(retries + 1):
            try:
                all_records.update(fetch_arxiv_batch(batch, timeout=timeout))
                break
            except (HTTPError, URLError, TimeoutError, OSError, ElementTree.ParseError) as exc:
                if attempt < retries:
                    print(
                        f"[arXiv] retry {attempt + 1}/{retries} for batch {index}/{len(batches)}: {exc}",
                        file=sys.stderr,
                    )
                    if retry_sleep > 0:
                        time.sleep(retry_sleep)
                else:
                    errors.append(
                        f"batch {index}/{len(batches)} ids {batch[0]}..{batch[-1]} failed: {exc}"
                    )
        if index < len(batches) and batch_sleep > 0:
            time.sleep(batch_sleep)
    return all_records, errors


def merge_code_discovery_hits(hits: list[CodeDiscoveryHit]) -> list[CodeDiscoveryHit]:
    by_key: dict[str, CodeDiscoveryHit] = {}
    for hit in hits:
        key = hit.repo or hit.url
        existing = by_key.get(key)
        if existing is None or hit.confidence > existing.confidence:
            by_key[key] = hit

    merged = list(by_key.values())
    merged.sort(
        key=lambda item: (
            -item.confidence,
            DISCOVERY_SOURCE_ORDER.get(item.source, 99),
            item.repo,
            item.url,
        )
    )
    return merged


def fetch_arxiv_html_code_hits(
    arxiv_ids: list[str],
    timeout: float,
) -> tuple[dict[str, list[CodeDiscoveryHit]], list[str]]:
    hits_by_id: dict[str, list[CodeDiscoveryHit]] = {}
    errors: list[str] = []

    for index, arxiv_id in enumerate(arxiv_ids, start=1):
        if index == 1 or index % 100 == 0 or index == len(arxiv_ids):
            print(f"[arXiv HTML] {index}/{len(arxiv_ids)}: {arxiv_id}", file=sys.stderr)

        abs_url = f"https://arxiv.org/abs/{arxiv_id}"
        try:
            data, _status = request_bytes(abs_url, timeout=timeout)
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            errors.append(f"{arxiv_id}: {exc}")
            continue

        html = decode_bytes(data)
        raw_urls = ARXIV_HTML_GITHUB_HREF_RE.findall(html)
        entry_hits: list[CodeDiscoveryHit] = []
        for raw_url in raw_urls:
            normalized_url, repo, owner_lower = normalize_github_url(raw_url)
            if not normalized_url or not repo:
                continue
            if owner_lower in EXCLUDED_ARXIV_HTML_GITHUB_OWNERS:
                continue
            entry_hits.append(
                CodeDiscoveryHit(
                    source="arxiv_html",
                    url=normalized_url,
                    repo=repo,
                    confidence=DISCOVERY_SOURCE_CONFIDENCE["arxiv_html"],
                    extra={"abs_url": abs_url},
                )
            )

        hits_by_id[arxiv_id] = merge_code_discovery_hits(entry_hits)

    return hits_by_id, errors


def build_github_search_url(arxiv_id: str) -> str:
    query = urlencode(
        {
            "q": arxiv_id,
            "sort": "stars",
            "order": "desc",
            "per_page": "3",
        }
    )
    return f"https://api.github.com/search/repositories?{query}"


def fetch_github_search_code_hits(
    arxiv_ids: list[str],
    timeout: float,
    github_token: str,
    sleep_seconds: float,
) -> tuple[dict[str, list[CodeDiscoveryHit]], list[str]]:
    hits_by_id: dict[str, list[CodeDiscoveryHit]] = {}
    errors: list[str] = []

    extra_headers: dict[str, str] = {"Accept": "application/vnd.github+json"}
    token = github_token.strip()
    if token:
        extra_headers["Authorization"] = f"Bearer {token}"

    for index, arxiv_id in enumerate(arxiv_ids, start=1):
        if index == 1 or index % 25 == 0 or index == len(arxiv_ids):
            print(f"[GitHub Search] {index}/{len(arxiv_ids)}: {arxiv_id}", file=sys.stderr)

        url = build_github_search_url(arxiv_id)
        try:
            data, status = request_bytes(url, timeout=timeout, extra_headers=extra_headers)
            payload = json.loads(decode_bytes(data))
        except HTTPError as exc:
            errors.append(f"{arxiv_id}: HTTP {exc.code}")
            payload = {}
            status = int(exc.code)
        except (URLError, TimeoutError, OSError, json.JSONDecodeError) as exc:
            errors.append(f"{arxiv_id}: {exc}")
            payload = {}
            status = 0

        items_obj = payload.get("items", []) if isinstance(payload, dict) else []
        if not isinstance(items_obj, list):
            errors.append(f"{arxiv_id}: malformed GitHub response")
            items_obj = []

        entry_hits: list[CodeDiscoveryHit] = []
        for item in items_obj[:3]:
            if not isinstance(item, dict):
                continue
            full_name = clean_text(str(item.get("full_name", "")))
            html_url = clean_text(str(item.get("html_url", "")))
            stars_obj = item.get("stargazers_count", 0)
            try:
                stars = int(stars_obj)
            except (TypeError, ValueError):
                stars = 0
            description = clean_text(str(item.get("description") or ""))

            normalized_url = ""
            repo = ""
            if html_url:
                normalized_url, repo, _owner_lower = normalize_github_url(html_url)
            if not repo and full_name and "/" in full_name:
                repo = full_name
            if not repo:
                continue
            if not normalized_url:
                normalized_url = f"https://github.com/{repo}"

            entry_hits.append(
                CodeDiscoveryHit(
                    source="github_search",
                    url=normalized_url,
                    repo=repo,
                    confidence=DISCOVERY_SOURCE_CONFIDENCE["github_search"],
                    extra={
                        "stars": stars,
                        "description": description,
                        "status_code": status,
                    },
                )
            )

        hits_by_id[arxiv_id] = merge_code_discovery_hits(entry_hits)

        if index < len(arxiv_ids) and sleep_seconds > 0:
            time.sleep(sleep_seconds)

    return hits_by_id, errors


def discover_code_links(
    ids_without_code_url: list[str],
    arxiv_records: dict[str, ArxivEntry],
    timeout: float,
    github_token: str,
    skip_github_search: bool,
) -> tuple[dict[str, list[CodeDiscoveryHit]], list[str], list[str], list[str]]:
    discovery_by_id: dict[str, list[CodeDiscoveryHit]] = {}

    for arxiv_id in ids_without_code_url:
        hits: list[CodeDiscoveryHit] = []
        arxiv = arxiv_records.get(arxiv_id)
        if arxiv:
            for url in arxiv.github_urls_in_comment:
                normalized_url, repo, _owner_lower = normalize_github_url(url)
                if not normalized_url or not repo:
                    continue
                hits.append(
                    CodeDiscoveryHit(
                        source="arxiv_comment",
                        url=normalized_url,
                        repo=repo,
                        confidence=DISCOVERY_SOURCE_CONFIDENCE["arxiv_comment"],
                        extra={},
                    )
                )
        discovery_by_id[arxiv_id] = merge_code_discovery_hits(hits)

    html_hits_by_id, arxiv_html_errors = fetch_arxiv_html_code_hits(
        arxiv_ids=ids_without_code_url,
        timeout=timeout,
    )
    for arxiv_id, hits in html_hits_by_id.items():
        merged = merge_code_discovery_hits(discovery_by_id.get(arxiv_id, []) + hits)
        discovery_by_id[arxiv_id] = merged

    github_search_targets = [
        arxiv_id for arxiv_id in ids_without_code_url if not discovery_by_id.get(arxiv_id)
    ]
    github_search_errors: list[str] = []

    if github_search_targets and not skip_github_search:
        sleep_seconds = 2.0 if github_token.strip() else 6.0
        search_hits_by_id, github_search_errors = fetch_github_search_code_hits(
            arxiv_ids=github_search_targets,
            timeout=timeout,
            github_token=github_token,
            sleep_seconds=sleep_seconds,
        )
        for arxiv_id, hits in search_hits_by_id.items():
            merged = merge_code_discovery_hits(discovery_by_id.get(arxiv_id, []) + hits)
            discovery_by_id[arxiv_id] = merged

    return discovery_by_id, arxiv_html_errors, github_search_errors, github_search_targets


def fetch_repo_readme(repo: str, timeout: float) -> RepoReadmeCheck:
    owner, name = repo.split("/", 1)
    errors: list[str] = []
    for ref in README_REFS:
        readme_url = f"https://raw.githubusercontent.com/{owner}/{name}/{ref}/README.md"
        try:
            data, status = request_bytes(readme_url, timeout=timeout)
            content = decode_bytes(data)
            hits = keyword_hits(content)
            snippets = extract_keyword_snippets(content, hits)
            return RepoReadmeCheck(
                repo=repo,
                ok=True,
                ref=ref,
                readme_url=readme_url,
                status_code=status,
                keyword_hits=hits,
                snippets=snippets,
                error="",
            )
        except HTTPError as exc:
            errors.append(f"{ref}:{exc.code}")
            if exc.code == 404:
                continue
            return RepoReadmeCheck(
                repo=repo,
                ok=False,
                ref=ref,
                readme_url=readme_url,
                status_code=int(exc.code),
                keyword_hits=[],
                snippets=[],
                error="; ".join(errors),
            )
        except (URLError, TimeoutError, OSError) as exc:
            errors.append(f"{ref}:{exc}")
            return RepoReadmeCheck(
                repo=repo,
                ok=False,
                ref=ref,
                readme_url=readme_url,
                status_code=0,
                keyword_hits=[],
                snippets=[],
                error="; ".join(errors),
            )
    return RepoReadmeCheck(
        repo=repo,
        ok=False,
        ref="",
        readme_url="",
        status_code=0,
        keyword_hits=[],
        snippets=[],
        error="; ".join(errors) if errors else "readme not found",
    )


def check_repos(repos: list[str], timeout: float) -> tuple[dict[str, RepoReadmeCheck], list[str]]:
    checks: dict[str, RepoReadmeCheck] = {}
    errors: list[str] = []
    for index, repo in enumerate(repos, start=1):
        if index == 1 or index % 25 == 0 or index == len(repos):
            print(f"[GitHub README] repo {index}/{len(repos)}: {repo}", file=sys.stderr)
        check = fetch_repo_readme(repo, timeout=timeout)
        checks[repo] = check
        if not check.ok:
            errors.append(f"{repo}: {check.error}")
    return checks, errors


def shorten(text: str, limit: int = 120) -> str:
    normalized = clean_text(text).replace("|", "/")
    if len(normalized) <= limit:
        return normalized
    return normalized[: limit - 1].rstrip() + "…"


def select_primary_github_evidence(
    checks: list[RepoReadmeCheck],
) -> dict[str, object]:
    if not checks:
        return {
            "url": "",
            "ref": "",
            "keyword_hits": [],
            "snippets": [],
        }

    matched = [check for check in checks if check.ok and check.keyword_hits]
    if matched:
        matched.sort(key=lambda item: (-len(item.keyword_hits), item.repo))
        best = matched[0]
        return {
            "url": best.readme_url,
            "ref": best.ref,
            "keyword_hits": best.keyword_hits,
            "snippets": best.snippets,
        }

    successful = [check for check in checks if check.ok]
    if successful:
        best = successful[0]
        return {
            "url": best.readme_url,
            "ref": best.ref,
            "keyword_hits": [],
            "snippets": [],
        }

    return {
        "url": "",
        "ref": "",
        "keyword_hits": [],
        "snippets": [],
    }


def build_results(
    entries: list[PaperEntry],
    arxiv_records: dict[str, ArxivEntry],
    repo_checks: dict[str, RepoReadmeCheck],
    code_discovery_by_id: dict[str, list[CodeDiscoveryHit]],
) -> list[dict[str, object]]:
    grouped: dict[str, dict[str, object]] = {}
    for entry in entries:
        item = grouped.get(entry.arxiv_id)
        if item is None:
            item = {
                "arxiv_id": entry.arxiv_id,
                "titles": [],
                "entries": [],
                "sources": [],
                "code_urls": [],
                "github_repos": [],
                "non_github_code_urls": [],
            }
            grouped[entry.arxiv_id] = item

        titles: list[str] = item["titles"]  # type: ignore[assignment]
        source_entries: list[dict[str, object]] = item["entries"]  # type: ignore[assignment]
        sources: list[str] = item["sources"]  # type: ignore[assignment]
        code_urls: list[str] = item["code_urls"]  # type: ignore[assignment]
        github_repos: list[str] = item["github_repos"]  # type: ignore[assignment]
        non_github_code_urls: list[str] = item["non_github_code_urls"]  # type: ignore[assignment]

        if entry.title and entry.title not in titles:
            titles.append(entry.title)
        source_entries.append(asdict(entry))
        if entry.source not in sources:
            sources.append(entry.source)

        if entry.code_url and entry.code_url not in code_urls:
            code_urls.append(entry.code_url)
            repo = extract_github_repo(entry.code_url)
            if repo:
                if repo not in github_repos:
                    github_repos.append(repo)
            elif entry.code_url not in non_github_code_urls:
                non_github_code_urls.append(entry.code_url)

    ordered_ids = sorted(grouped.keys(), reverse=True)
    results: list[dict[str, object]] = []
    for arxiv_id in ordered_ids:
        item = grouped[arxiv_id]
        titles = ordered_unique(item["titles"])  # type: ignore[arg-type]
        source_entries = item["entries"]  # type: ignore[assignment]
        sources = ordered_unique(item["sources"])  # type: ignore[arg-type]
        code_urls = ordered_unique(item["code_urls"])  # type: ignore[arg-type]
        github_repos = ordered_unique(item["github_repos"])  # type: ignore[arg-type]
        non_github_code_urls = ordered_unique(item["non_github_code_urls"])  # type: ignore[arg-type]

        arxiv = arxiv_records.get(arxiv_id)
        if arxiv is None:
            arxiv = ArxivEntry(
                arxiv_id=arxiv_id,
                title="",
                journal_ref="",
                comment="",
                github_urls_in_comment=[],
                has_journal_ref=False,
                keyword_hits=[],
                found=False,
            )

        checks_for_id: list[RepoReadmeCheck] = []
        fetch_results: list[dict[str, object]] = []
        matched_repos: list[dict[str, object]] = []
        combined_github_hits: list[str] = []

        for repo in github_repos:
            check = repo_checks.get(repo)
            if check is None:
                continue
            checks_for_id.append(check)
            fetch_results.append(asdict(check))
            if check.ok and check.keyword_hits:
                matched_repos.append(
                    {
                        "repo": check.repo,
                        "ref": check.ref,
                        "readme_url": check.readme_url,
                        "keyword_hits": check.keyword_hits,
                        "snippets": check.snippets,
                    }
                )
                for hit in check.keyword_hits:
                    if hit not in combined_github_hits:
                        combined_github_hits.append(hit)

        primary_readme_evidence = select_primary_github_evidence(checks_for_id)

        code_discovery_hits = code_discovery_by_id.get(arxiv_id, [])
        code_discovery_payload = [asdict(hit) for hit in code_discovery_hits]

        arxiv_signal = arxiv.has_journal_ref or bool(arxiv.keyword_hits)
        github_signal = bool(combined_github_hits)
        if arxiv_signal and github_signal:
            signal_source = "both"
        elif arxiv_signal:
            signal_source = "arxiv_only"
        elif github_signal:
            signal_source = "github_only"
        else:
            signal_source = "none"

        primary_title = ""
        if titles:
            primary_title = titles[0]
        elif arxiv.title:
            primary_title = arxiv.title

        source_label = sources[0] if len(sources) == 1 else "mixed"

        results.append(
            {
                "arxiv_id": arxiv_id,
                "title": primary_title,
                "titles": titles,
                "source": source_label,
                "sources": sources,
                "entries": source_entries,
                "signals": {
                    "arxiv": arxiv_signal,
                    "github": github_signal,
                    "source": signal_source,
                },
                "arxiv": asdict(arxiv),
                "github": {
                    "checked": bool(github_repos),
                    "code_urls": code_urls,
                    "github_repos": github_repos,
                    "non_github_code_urls": non_github_code_urls,
                    "keyword_hits": combined_github_hits,
                    "matched_repos": matched_repos,
                    "fetch_results": fetch_results,
                },
                "evidence": {
                    "arxiv": {
                        "journal_ref": arxiv.journal_ref,
                        "comment": arxiv.comment,
                        "github_urls_in_comment": arxiv.github_urls_in_comment,
                    },
                    "github_readme": primary_readme_evidence,
                    "code_discovery": code_discovery_payload,
                },
            }
        )
    return results


def build_stats(
    results: list[dict[str, object]],
    entries: list[PaperEntry],
    archive_paths: list[Path],
    readme_path: Path,
    github_search_candidates: int,
    github_search_executed: int,
) -> dict[str, int]:
    signal_counts = {"both": 0, "arxiv_only": 0, "github_only": 0, "none": 0}
    ids_with_code_url = 0
    ids_with_github_repo = 0
    arxiv_found = 0
    github_checked = 0
    ids_with_code_discovery = 0
    ids_from_archive = 0
    ids_from_readme = 0

    for result in results:
        signals = result["signals"]  # type: ignore[assignment]
        source = str(signals["source"])
        signal_counts[source] += 1

        github_info = result["github"]  # type: ignore[assignment]
        arxiv_info = result["arxiv"]  # type: ignore[assignment]
        evidence = result["evidence"]  # type: ignore[assignment]
        sources = result["sources"]  # type: ignore[assignment]

        if github_info["code_urls"]:  # type: ignore[index]
            ids_with_code_url += 1
        if github_info["github_repos"]:  # type: ignore[index]
            ids_with_github_repo += 1
        if github_info["checked"]:  # type: ignore[index]
            github_checked += 1
        if arxiv_info["found"]:  # type: ignore[index]
            arxiv_found += 1
        if evidence["code_discovery"]:  # type: ignore[index]
            ids_with_code_discovery += 1

        if "archive" in sources:
            ids_from_archive += 1
        if "readme" in sources:
            ids_from_readme += 1

    archive_entries = [entry for entry in entries if entry.source == "archive"]
    readme_entries = [entry for entry in entries if entry.source == "readme"]

    unique_code_urls = len({entry.code_url for entry in entries if entry.code_url})
    unique_repos = len(
        {
            repo
            for entry in entries
            if entry.code_url
            for repo in [extract_github_repo(entry.code_url)]
            if repo
        }
    )

    return {
        "archive_files": len(archive_paths),
        "readme_files": 1 if readme_path.exists() else 0,
        "archive_entries_with_arxiv": len(archive_entries),
        "readme_entries_with_arxiv": len(readme_entries),
        "unique_arxiv_ids": len(results),
        "unique_code_urls": unique_code_urls,
        "unique_github_repos": unique_repos,
        "ids_from_archive": ids_from_archive,
        "ids_from_readme": ids_from_readme,
        "ids_with_code_url": ids_with_code_url,
        "ids_with_github_repo": ids_with_github_repo,
        "arxiv_records_found": arxiv_found,
        "github_checked_ids": github_checked,
        "ids_with_code_discovery": ids_with_code_discovery,
        "github_search_candidates": github_search_candidates,
        "github_search_executed": github_search_executed,
        "signal_both": signal_counts["both"],
        "signal_arxiv_only": signal_counts["arxiv_only"],
        "signal_github_only": signal_counts["github_only"],
        "signal_none": signal_counts["none"],
    }


def format_arxiv_evidence(result: dict[str, object]) -> str:
    evidence = result["evidence"]  # type: ignore[assignment]
    arxiv_evidence = evidence["arxiv"]  # type: ignore[index]
    arxiv_info = result["arxiv"]  # type: ignore[assignment]

    journal_ref = str(arxiv_evidence["journal_ref"])
    comment = str(arxiv_evidence["comment"])
    comment_urls = arxiv_evidence["github_urls_in_comment"]  # type: ignore[index]
    keyword_list = arxiv_info["keyword_hits"]  # type: ignore[index]

    pieces: list[str] = []
    if journal_ref:
        pieces.append(f"journal_ref={shorten(journal_ref, 90)}")
    if keyword_list:
        pieces.append("keywords=" + ", ".join(keyword_list))
    if comment_urls:
        display_urls = [extract_github_repo(url) or url for url in comment_urls[:3]]
        suffix = f", +{len(comment_urls) - 3} more" if len(comment_urls) > 3 else ""
        pieces.append("comment_github=" + ", ".join(display_urls) + suffix)
    if not pieces and comment:
        pieces.append("comment=" + shorten(comment, 90))
    if not pieces and not arxiv_info["found"]:  # type: ignore[index]
        pieces.append("not found in arXiv response")
    return "; ".join(pieces) if pieces else "-"


def format_github_evidence(result: dict[str, object]) -> str:
    evidence = result["evidence"]  # type: ignore[assignment]
    readme_evidence = evidence["github_readme"]  # type: ignore[index]
    github_info = result["github"]  # type: ignore[assignment]

    readme_url = str(readme_evidence["url"])
    ref = str(readme_evidence["ref"])
    keyword_list = readme_evidence["keyword_hits"]  # type: ignore[index]
    snippets = readme_evidence["snippets"]  # type: ignore[index]

    if not readme_url:
        if github_info["checked"]:  # type: ignore[index]
            return "checked, no keyword hit"
        return "-"

    repo = extract_github_repo(readme_url)
    repo_text = f"{repo}@{ref}" if repo else readme_url
    if keyword_list:
        return (
            f"{repo_text}; keywords={', '.join(keyword_list)}; "
            f"snippets={len(snippets)}"
        )
    return f"{repo_text}; no keyword hit"


def format_code_discovery_evidence(result: dict[str, object]) -> str:
    evidence = result["evidence"]  # type: ignore[assignment]
    hits = evidence["code_discovery"]  # type: ignore[index]
    if not hits:
        return "-"

    parts: list[str] = []
    for hit in hits[:3]:
        source = str(hit["source"])
        repo = str(hit["repo"])
        parts.append(f"{source}:{repo}")
    if len(hits) > 3:
        parts.append(f"+{len(hits) - 3} more")
    return "; ".join(parts)


def render_markdown_report(
    generated_at: str,
    stats: dict[str, int],
    results: list[dict[str, object]],
    parse_errors: list[str],
    arxiv_errors: list[str],
    arxiv_html_errors: list[str],
    github_readme_errors: list[str],
    github_search_errors: list[str],
) -> str:
    lines = [
        "# Archive Acceptance Check",
        "",
        f"- Generated at (UTC): {generated_at}",
        "",
        "## Summary",
        f"- archive files scanned: {stats['archive_files']}",
        f"- README files scanned: {stats['readme_files']}",
        f"- archive entries with arXiv id: {stats['archive_entries_with_arxiv']}",
        f"- README entries (empty note) with arXiv id: {stats['readme_entries_with_arxiv']}",
        f"- unique arXiv ids: {stats['unique_arxiv_ids']}",
        f"- ids from archive: {stats['ids_from_archive']}",
        f"- ids from README: {stats['ids_from_readme']}",
        f"- ids with code url: {stats['ids_with_code_url']}",
        f"- ids with github repo: {stats['ids_with_github_repo']}",
        f"- arXiv records found: {stats['arxiv_records_found']}",
        f"- ids with code discovery hits: {stats['ids_with_code_discovery']}",
        f"- GitHub search candidates: {stats['github_search_candidates']}",
        f"- GitHub search executed: {stats['github_search_executed']}",
        f"- signal both: {stats['signal_both']}",
        f"- signal arXiv only: {stats['signal_arxiv_only']}",
        f"- signal GitHub only: {stats['signal_github_only']}",
        f"- signal none: {stats['signal_none']}",
    ]

    sections = [
        ("both", "Both"),
        ("arxiv_only", "arXiv Only"),
        ("github_only", "GitHub Only"),
    ]
    for source_key, title in sections:
        lines.extend(["", f"## {title}"])
        subset = [result for result in results if result["signals"]["source"] == source_key]
        lines.append(f"- count: {len(subset)}")
        if not subset:
            lines.append("")
            lines.append("(none)")
            continue
        lines.extend(
            [
                "",
                "| Source | arXiv ID | Title | arXiv Evidence | GitHub README Evidence | Code Discovery |",
                "| --- | --- | --- | --- | --- | --- |",
            ]
        )
        for result in subset:
            source_text = ",".join(result["sources"])
            arxiv_id = str(result["arxiv_id"])
            title_text = shorten(str(result["title"]), 100)
            arxiv_text = shorten(format_arxiv_evidence(result), 140)
            github_text = shorten(format_github_evidence(result), 140)
            code_text = shorten(format_code_discovery_evidence(result), 140)
            lines.append(
                f"| {source_text} | {arxiv_id} | {title_text} | {arxiv_text} | {github_text} | {code_text} |"
            )

    lines.extend(["", "## Errors"])
    lines.append(f"- parse warnings: {len(parse_errors)}")
    lines.append(f"- arXiv fetch errors: {len(arxiv_errors)}")
    lines.append(f"- arXiv abs HTML fetch errors: {len(arxiv_html_errors)}")
    lines.append(f"- GitHub README fetch errors: {len(github_readme_errors)}")
    lines.append(f"- GitHub search errors: {len(github_search_errors)}")

    if parse_errors:
        lines.extend(["", "### Parse Warnings (first 20)"])
        for message in parse_errors[:20]:
            lines.append(f"- {message}")

    if arxiv_errors:
        lines.extend(["", "### arXiv Fetch Errors (first 20)"])
        for message in arxiv_errors[:20]:
            lines.append(f"- {message}")

    if arxiv_html_errors:
        lines.extend(["", "### arXiv Abs HTML Fetch Errors (first 20)"])
        for message in arxiv_html_errors[:20]:
            lines.append(f"- {message}")

    if github_readme_errors:
        lines.extend(["", "### GitHub README Fetch Errors (first 20)"])
        for message in github_readme_errors[:20]:
            lines.append(f"- {message}")

    if github_search_errors:
        lines.extend(["", "### GitHub Search Errors (first 20)"])
        for message in github_search_errors[:20]:
            lines.append(f"- {message}")

    return "\n".join(lines) + "\n"


def write_outputs(
    output_dir: Path,
    generated_at: str,
    archive_paths: list[Path],
    readme_path: Path,
    stats: dict[str, int],
    results: list[dict[str, object]],
    parse_errors: list[str],
    arxiv_errors: list[str],
    arxiv_html_errors: list[str],
    github_readme_errors: list[str],
    github_search_errors: list[str],
) -> tuple[Path, Path]:
    output_dir.mkdir(parents=True, exist_ok=True)
    timestamp = file_timestamp_now()
    md_path = output_dir / f"archive-acceptance-{timestamp}.md"
    json_path = output_dir / f"archive-acceptance-{timestamp}.json"

    payload = {
        "generated_at": generated_at,
        "archive_files": [path.as_posix() for path in archive_paths],
        "readme_file": readme_path.as_posix(),
        "keywords": list(ACCEPTANCE_KEYWORDS),
        "stats": stats,
        "errors": {
            "parse": parse_errors,
            "arxiv_fetch": arxiv_errors,
            "arxiv_html_fetch": arxiv_html_errors,
            "github_readme_fetch": github_readme_errors,
            "github_search_fetch": github_search_errors,
        },
        "results": results,
    }
    md_text = render_markdown_report(
        generated_at=generated_at,
        stats=stats,
        results=results,
        parse_errors=parse_errors,
        arxiv_errors=arxiv_errors,
        arxiv_html_errors=arxiv_html_errors,
        github_readme_errors=github_readme_errors,
        github_search_errors=github_search_errors,
    )
    json_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    md_path.write_text(md_text, encoding="utf-8")
    return md_path, json_path


def main() -> None:
    _install_proxy()
    args = parse_args()

    archive_paths = sorted(Path(".").glob(args.archive_glob))
    if not archive_paths:
        raise SystemExit(f"No archive files matched: {args.archive_glob}")

    readme_path = Path(args.readme)
    if not readme_path.exists():
        raise SystemExit(f"README not found: {readme_path.as_posix()}")

    archive_entries, archive_parse_errors = find_archive_entries(archive_paths)
    readme_entries, readme_parse_errors = find_readme_entries(readme_path)
    entries = archive_entries + readme_entries
    parse_errors = archive_parse_errors + readme_parse_errors

    unique_arxiv_ids = sorted({entry.arxiv_id for entry in entries}, reverse=True)
    arxiv_records, arxiv_errors = fetch_arxiv_records(
        unique_arxiv_ids,
        batch_size=args.batch_size,
        batch_sleep=args.batch_sleep,
        timeout=args.arxiv_timeout,
        retries=args.arxiv_retries,
        retry_sleep=args.arxiv_retry_sleep,
    )

    repos = sorted(
        {
            extract_github_repo(entry.code_url)
            for entry in entries
            if entry.code_url and extract_github_repo(entry.code_url)
        }
    )
    repo_checks, github_readme_errors = check_repos(repos, timeout=args.github_timeout)

    has_code_url_by_id: dict[str, bool] = {}
    for entry in entries:
        if entry.code_url:
            has_code_url_by_id[entry.arxiv_id] = True

    ids_without_code_url = [
        arxiv_id for arxiv_id in unique_arxiv_ids if not has_code_url_by_id.get(arxiv_id, False)
    ]

    github_token = args.github_token.strip() or os.getenv("GITHUB_TOKEN", "").strip()
    code_discovery_by_id, arxiv_html_errors, github_search_errors, github_search_targets = (
        discover_code_links(
            ids_without_code_url=ids_without_code_url,
            arxiv_records=arxiv_records,
            timeout=args.github_timeout,
            github_token=github_token,
            skip_github_search=args.skip_github_search,
        )
    )

    results = build_results(
        entries=entries,
        arxiv_records=arxiv_records,
        repo_checks=repo_checks,
        code_discovery_by_id=code_discovery_by_id,
    )
    stats = build_stats(
        results=results,
        entries=entries,
        archive_paths=archive_paths,
        readme_path=readme_path,
        github_search_candidates=len(github_search_targets),
        github_search_executed=0 if args.skip_github_search else len(github_search_targets),
    )

    generated_at = utc_now_iso()
    md_path, json_path = write_outputs(
        output_dir=args.output_dir,
        generated_at=generated_at,
        archive_paths=archive_paths,
        readme_path=readme_path,
        stats=stats,
        results=results,
        parse_errors=parse_errors,
        arxiv_errors=arxiv_errors,
        arxiv_html_errors=arxiv_html_errors,
        github_readme_errors=github_readme_errors,
        github_search_errors=github_search_errors,
    )

    print(f"Wrote markdown report: {md_path.as_posix()}")
    print(f"Wrote json report: {json_path.as_posix()}")
    print(
        "Summary:"
        f" unique_arxiv_ids={stats['unique_arxiv_ids']}"
        f" both={stats['signal_both']}"
        f" arxiv_only={stats['signal_arxiv_only']}"
        f" github_only={stats['signal_github_only']}"
        f" none={stats['signal_none']}"
        f" code_discovery={stats['ids_with_code_discovery']}"
    )


if __name__ == "__main__":
    main()
