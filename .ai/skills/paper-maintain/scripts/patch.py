#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import subprocess
import time
from collections import OrderedDict
from pathlib import Path
from typing import Iterable
from urllib.error import HTTPError, URLError
from urllib.parse import urlparse
from urllib.request import Request, urlopen

from bs4 import BeautifulSoup


HEADERS = {"User-Agent": "Mozilla/5.0"}


def project_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "README.md").exists():
            return parent
    return Path.cwd()


PROXY_FILE = project_root() / ".PROXY"


def _install_proxy() -> None:
    if not PROXY_FILE.exists():
        return
    proxy = PROXY_FILE.read_text().strip()
    if not proxy:
        return
    import urllib.request
    opener = urllib.request.build_opener(
        urllib.request.ProxyHandler({"http": proxy, "https": proxy})
    )
    urllib.request.install_opener(opener)
ARXIV_ID_RE = re.compile(r"\[arXiv:(\d{4}\.\d{5})\]")
RAW_URL_RE = re.compile(r"https?://[^\s<>'\"\]\)]+")
VENUE_RE = re.compile(
    r"\b("
    r"cvpr|iccv|eccv|neurips|iclr|aaai|wacv|3dv|siggraph(?: asia)?|"
    r"miccai|icra|icml|iros|bmvc|acm mm|acmmm|tpami|tvcg|tog|cag|"
    r"medical image analysis|isprs|ijcv|stag|hpca|icassp|icip|icme"
    r")\b",
    re.I,
)
NEGATIVE_NOTE_RE = re.compile(
    r"\b("
    r"under review|submitted to|submission to|anonymous submission|"
    r"workshop version|supplementary material|preliminary version|"
    r"withdrawn"
    r")\b",
    re.I,
)
ACCEPTANCE_CUES_RE = re.compile(
    r"\b(accepted|to appear|published|camera-ready|oral|poster)\b", re.I
)
NOTE_PATTERNS = (
    re.compile(r"(Accepted as an [^.]{0,140}?\))", re.I),
    re.compile(r"(Accepted (?:to|at|by|for|in) [^.]{0,140}?(?:\d{4}\)|\d{4}))", re.I),
    re.compile(r"(To appear (?:at|in) [^.]{0,140}?(?:\d{4}\)|\d{4}))", re.I),
    re.compile(r"(Published (?:at|in) [^.]{0,140}?(?:\d{4}\)|\d{4}))", re.I),
)
NOTE_PREFIXES = (
    "accepted to ",
    "accepted at ",
    "accepted by ",
    "accepted for ",
    "accepted in ",
    "to appear in ",
    "published at ",
    "published in ",
)
GITHUB_RESERVED = {
    "about",
    "account",
    "apps",
    "collections",
    "contact",
    "customers",
    "enterprise",
    "events",
    "explore",
    "features",
    "login",
    "marketplace",
    "new",
    "notifications",
    "orgs",
    "pricing",
    "pulls",
    "search",
    "security",
    "settings",
    "site",
    "sponsors",
    "team",
    "teams",
    "topics",
}
TITLE_STOPWORDS = {
    "3d",
    "4d",
    "a",
    "an",
    "and",
    "aware",
    "based",
    "dynamic",
    "efficient",
    "explicit",
    "feed",
    "forward",
    "for",
    "from",
    "gaussian",
    "gaussians",
    "geometry",
    "gs",
    "human",
    "in",
    "learning",
    "monocular",
    "novel",
    "of",
    "on",
    "optimization",
    "reconstruction",
    "rendering",
    "representation",
    "scene",
    "semantic",
    "splatting",
    "synthesis",
    "the",
    "towards",
    "unified",
    "using",
    "via",
    "view",
    "with",
    "zero",
}


def run_git_show(spec: str) -> str:
    return subprocess.check_output(["git", "show", spec], text=True)


def load_target_ids(base_rev: str, readme_path: Path) -> list[str]:
    base_ids = set(ARXIV_ID_RE.findall(run_git_show(f"{base_rev}:README.md")))
    current_ids = set(ARXIV_ID_RE.findall(readme_path.read_text()))
    return sorted(current_ids - base_ids, reverse=True)


def load_readme_entries(readme_path: Path) -> tuple[list[str], dict[str, dict[str, int | str]]]:
    return load_readme_entries_from_text(readme_path.read_text())


def load_readme_entries_from_text(text: str) -> tuple[list[str], dict[str, dict[str, int | str]]]:
    lines = text.splitlines(keepends=True)
    entries: dict[str, dict[str, int | str]] = {}
    current_title = ""
    current_number = ""
    for idx, line in enumerate(lines):
        heading = re.match(r"^#### \[(\d+)\] (.+)$", line.rstrip("\n"))
        if heading:
            current_number = heading.group(1)
            current_title = heading.group(2)
            continue
        if line.startswith("- **🔗 链接**："):
            match = ARXIV_ID_RE.search(line)
            if not match:
                continue
            aid = match.group(1)
            code_match = re.search(r"\[\[Code\]\((https://github\.com/[^)]+)\)\]", line)
            note_text = ""
            if idx + 1 < len(lines) and lines[idx + 1].startswith("- **📝 说明**:"):
                note_text = lines[idx + 1].split(":", 1)[1].strip()
            entries[aid] = {
                "number": current_number,
                "title": current_title,
                "link_idx": idx,
                "note_idx": idx + 1,
                "note_text": note_text,
                "code_url": code_match.group(1) if code_match else "",
            }
    return lines, entries


def fetch_url(url: str, timeout: int = 20, retries: int = 1) -> dict[str, object]:
    last_error = ""
    for attempt in range(retries + 1):
        try:
            req = Request(url, headers=HEADERS)
            with urlopen(req, timeout=timeout) as response:
                body = response.read()
                charset = response.headers.get_content_charset() or "utf-8"
                return {
                    "ok": True,
                    "url": response.geturl(),
                    "status": getattr(response, "status", None) or response.code,
                    "content_type": response.headers.get_content_type(),
                    "text": body.decode(charset, "ignore"),
                }
        except (HTTPError, URLError, TimeoutError, OSError) as exc:
            last_error = str(exc)
            if attempt < retries:
                time.sleep(1.0 * (attempt + 1))
    return {"ok": False, "url": url, "status": None, "content_type": "", "text": "", "error": last_error}


def dedupe(items: Iterable[str]) -> list[str]:
    return list(OrderedDict.fromkeys(item for item in items if item))


def canonical_github(url: str) -> str | None:
    parsed = urlparse(url)
    if parsed.scheme not in {"http", "https"}:
        return None
    host = parsed.netloc.lower()
    if host not in {"github.com", "www.github.com"}:
        return None
    parts = [part for part in parsed.path.split("/") if part]
    if len(parts) < 2:
        return None
    if parts[0].lower() in GITHUB_RESERVED:
        return None
    return f"https://github.com/{parts[0]}/{parts[1].removesuffix('.git')}"


def title_tokens(title: str) -> set[str]:
    tokens = set(re.findall(r"[a-z0-9]+", title.lower()))
    return {token for token in tokens if len(token) >= 4 and token not in TITLE_STOPWORDS}


def repo_matches_title(url: str, title: str) -> bool:
    canonical = canonical_github(url)
    if not canonical:
        return False
    slug = canonical.rsplit("/", 1)[-1].lower()
    slug_tokens = set(re.findall(r"[a-z0-9]+", slug))
    paper_tokens = title_tokens(title)
    if not paper_tokens:
        return False
    return any(token in slug or slug in token or token in slug_tokens for token in paper_tokens)


def validate_github(url: str, cache: dict[str, bool]) -> bool:
    canonical = canonical_github(url)
    if not canonical:
        return False
    if canonical in cache:
        return cache[canonical]
    result = fetch_url(canonical, timeout=15, retries=1)
    if not result["ok"]:
        cache[canonical] = False
        return False
    text = str(result["text"]).lower()
    valid = "page not found" not in text and "repository unavailable due to dmca takedown" not in text
    cache[canonical] = valid
    return valid


def clean_note_fragment(text: str) -> str:
    text = re.sub(r"https?://\S+", "", text)
    text = re.split(r"(?i)\b(project page|project website|project|code|website)\b", text)[0]
    text = text.strip(" .;,:")
    while text.endswith("("):
        text = text[:-1].rstrip(" .;,:")
    return text


def normalize_note(note: str) -> str:
    note = clean_note_fragment(note)
    if note.lower().startswith("published in ") or note.lower().startswith("published at "):
        return note[0].upper() + note[1:]
    if note.lower().startswith("to appear in "):
        note = "To appear in " + note[len("To appear in ") :]
    elif note.lower().startswith("accepted by "):
        note = "Accepted to " + note[len("Accepted by ") :]
    elif note.lower().startswith("accepted"):
        note = note[0].upper() + note[1:]
    return f"🏆 {note}"


def extract_note(text: str) -> str:
    flat = re.sub(r"\s+", " ", text).strip(" .;")
    if not flat:
        return ""
    if NEGATIVE_NOTE_RE.search(flat):
        return ""
    if not VENUE_RE.search(flat):
        return ""
    if not ACCEPTANCE_CUES_RE.search(flat):
        return ""
    for pattern in NOTE_PATTERNS:
        match = pattern.search(flat)
        if match:
            note = normalize_note(match.group(1))
            return note if len(note) <= 180 else ""
    cleaned = clean_note_fragment(flat)
    if len(cleaned) > 180:
        return ""
    if any(cleaned.lower().startswith(prefix) for prefix in NOTE_PREFIXES):
        return normalize_note(cleaned)
    return ""


def collect_external_urls(nodes: Iterable[BeautifulSoup | None], text_blobs: Iterable[str]) -> list[str]:
    urls = []
    for node in nodes:
        if node is None:
            continue
        for anchor in node.select("a[href]"):
            href = anchor.get("href", "")
            if href.startswith("http"):
                urls.append(href)
    for blob in text_blobs:
        urls.extend(RAW_URL_RE.findall(blob))
    cleaned = []
    for url in dedupe(urls):
        host = urlparse(url).netloc.lower()
        if any(token in host for token in ("arxiv.org", "doi.org", "paperswithcode.com")):
            continue
        cleaned.append(url.rstrip(".,;"))
    return cleaned


def project_page_scan(url: str, title: str) -> tuple[str, list[str]]:
    result = fetch_url(url, timeout=12, retries=0)
    if not result["ok"] or result["content_type"] != "text/html":
        return "", []
    html = str(result["text"])
    soup = BeautifulSoup(html, "html.parser")
    note = extract_note(soup.get_text(" ", strip=True))
    urls = []
    for anchor in soup.select("a[href]"):
        href = anchor.get("href", "")
        if not href.startswith("http"):
            continue
        label = " ".join(
            value
            for value in (
                anchor.get_text(" ", strip=True),
                anchor.get("title", ""),
                anchor.get("aria-label", ""),
                " ".join(anchor.get("class", [])),
            )
            if value
        ).lower()
        canonical = canonical_github(href)
        if not canonical:
            continue
        if any(keyword in label for keyword in ("code", "github", "source", "repo", "repository")) or repo_matches_title(canonical, title):
            urls.append(canonical)
    github_urls = dedupe(urls)
    return note, github_urls


def scan_arxiv_page(aid: str, title: str, github_cache: dict[str, bool]) -> dict[str, object]:
    result = fetch_url(f"https://arxiv.org/abs/{aid}", timeout=20, retries=2)
    if not result["ok"]:
        return {
            "id": aid,
            "ok": False,
            "error": result.get("error", ""),
            "note": "",
            "code_url": "",
            "external_urls": [],
        }
    soup = BeautifulSoup(str(result["text"]), "html.parser")
    comments_cell = soup.find("td", class_="tablecell comments mathjax")
    abstract_block = soup.find("blockquote", class_="abstract mathjax")
    comments_text = comments_cell.get_text(" ", strip=True) if comments_cell else ""
    abstract_text = abstract_block.get_text(" ", strip=True) if abstract_block else ""
    note = extract_note(comments_text)
    external_urls = collect_external_urls([comments_cell, abstract_block], [comments_text, abstract_text])

    direct_github = []
    project_urls = []
    for url in external_urls:
        canonical = canonical_github(url)
        if canonical:
            direct_github.append(canonical)
        else:
            project_urls.append(url)

    code_url = ""
    for candidate in dedupe(direct_github):
        if validate_github(candidate, github_cache):
            code_url = candidate
            break

    project_notes = []
    project_github = []
    for url in project_urls[:3]:
        project_note, github_urls = project_page_scan(url, title)
        if project_note:
            project_notes.append(project_note)
        project_github.extend(github_urls)

    if not note:
        for project_note in project_notes:
            if project_note:
                note = project_note
                break

    if not code_url:
        for candidate in dedupe(project_github):
            if validate_github(candidate, github_cache):
                code_url = candidate
                break

    return {
        "id": aid,
        "ok": True,
        "comments": comments_text,
        "note": note,
        "code_url": code_url,
        "external_urls": external_urls,
    }


def update_readme(readme_path: Path, target_ids: set[str], results: dict[str, dict[str, object]], baseline_rev: str) -> dict[str, int]:
    lines, entries = load_readme_entries(readme_path)
    _, baseline_entries = load_readme_entries_from_text(run_git_show(f"{baseline_rev}:README.md"))
    updated_notes = 0
    updated_codes = 0
    for aid in target_ids:
        if aid not in entries or aid not in results:
            continue
        entry = entries[aid]
        result = results[aid]
        baseline_entry = baseline_entries.get(aid, {})
        link_idx = int(entry["link_idx"])
        note_idx = int(entry["note_idx"])
        line = lines[link_idx].rstrip("\n")
        code_url = str(baseline_entry.get("code_url", "")).strip() or str(result.get("code_url", "")).strip()
        if code_url:
            new_line = re.sub(r"\s+\[Code\]$", f" [[Code]({code_url})]", line)
            new_line = re.sub(r"\s+\[\[Code\]\([^)]+\)\]$", f" [[Code]({code_url})]", new_line)
        else:
            new_line = re.sub(r"\s+\[\[Code\]\([^)]+\)\]$", " [Code]", line)
        if new_line != line:
            lines[link_idx] = new_line + "\n"
            updated_codes += 1

        if note_idx < len(lines) and lines[note_idx].startswith("- **📝 说明**:"):
            baseline_note = str(baseline_entry.get("note_text", "")).strip()
            new_note = baseline_note or str(result.get("note", "")).strip()
            desired_line = f"- **📝 说明**: {new_note}\n" if new_note else "- **📝 说明**:\n"
            if lines[note_idx] != desired_line:
                lines[note_idx] = desired_line
                updated_notes += 1

    readme_path.write_text("".join(lines))
    return {"updated_notes": updated_notes, "updated_codes": updated_codes}


def main() -> None:
    _install_proxy()
    parser = argparse.ArgumentParser()
    parser.add_argument("--base-rev", required=True, help="Git rev marking the start of the patch window.")
    parser.add_argument("--baseline-rev", default="HEAD")
    parser.add_argument("--readme", default="README.md")
    parser.add_argument("--report", default="/tmp/recent_sync_metadata_report.json")
    parser.add_argument("--limit", type=int, default=0)
    parser.add_argument("--write", action="store_true")
    args = parser.parse_args()

    readme_path = Path(args.readme)
    target_ids = load_target_ids(args.base_rev, readme_path)
    if args.limit > 0:
        target_ids = target_ids[: args.limit]
    _, current_entries = load_readme_entries(readme_path)
    github_cache: dict[str, bool] = {}
    results: dict[str, dict[str, object]] = {}

    for index, aid in enumerate(target_ids, start=1):
        results[aid] = scan_arxiv_page(aid, str(current_entries[aid]["title"]), github_cache)
        print(f"[{index}/{len(target_ids)}] {aid} note={bool(results[aid].get('note'))} code={bool(results[aid].get('code_url'))}", flush=True)
        time.sleep(0.2)

    summary = {
        "target_count": len(target_ids),
        "note_count": sum(1 for item in results.values() if item.get("note")),
        "code_count": sum(1 for item in results.values() if item.get("code_url")),
        "errors": [item["id"] for item in results.values() if not item.get("ok")],
    }

    report = {"summary": summary, "results": results}
    Path(args.report).write_text(json.dumps(report, ensure_ascii=False, indent=2))

    if args.write:
        write_summary = update_readme(readme_path, set(target_ids), results, args.baseline_rev)
        summary.update(write_summary)

    print(json.dumps(summary, ensure_ascii=False, indent=2))


if __name__ == "__main__":
    main()
