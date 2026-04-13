#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import subprocess
from concurrent.futures import ThreadPoolExecutor, as_completed
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from fill_affiliations import get_pdf_first_page_text, html_source_text
from patch import extract_note, project_page_scan, scan_arxiv_page, validate_github


def project_root() -> Path:
    for parent in Path(__file__).resolve().parents:
        if (parent / "README.md").exists():
            return parent
    return Path.cwd()


PROXY_FILE = project_root() / ".PROXY"
ARXIV_ID_RE = re.compile(r"^\d{4}\.\d{5}$")
PDF_STOP_LINE_RE = re.compile(
    r"^(abstract|introduction|1[\s.]*introduction|keywords?|index terms?)\b",
    re.I,
)


@dataclass(frozen=True)
class DiffEntry:
    arxiv_id: str
    title: str


@dataclass(frozen=True)
class DownloadEntry:
    arxiv_id: str
    affiliation_text: str
    affiliation_source: str
    note: str
    code_url: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Download affiliation candidates and note/code metadata for new papers."
    )
    parser.add_argument(
        "--input",
        type=Path,
        default=Path("tmp/diff.json"),
        help="Diff JSON path (default: tmp/diff.json).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        default=Path("tmp/download.json"),
        help="Output JSON path (default: tmp/download.json).",
    )
    parser.add_argument(
        "--workers",
        type=int,
        default=4,
        help="Concurrent worker count (default: 4).",
    )
    parser.add_argument(
        "--cache-dir",
        type=Path,
        default=Path("tmp/affiliation_cache"),
        help="Cache directory for HTML/PDF downloads (default: tmp/affiliation_cache).",
    )
    args = parser.parse_args()
    if args.workers <= 0:
        parser.error("--workers must be a positive integer.")
    return args


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def load_diff_entries(path: Path) -> list[DiffEntry]:
    payload = json.loads(path.read_text())
    if not isinstance(payload, dict):
        raise ValueError("Diff payload must be a JSON object.")
    raw_items = payload.get("new")
    if not isinstance(raw_items, list):
        raise ValueError("Diff payload must contain a list field: new")

    entries: list[DiffEntry] = []
    for item in raw_items:
        if not isinstance(item, dict):
            continue
        arxiv_id = str(item.get("arxiv_id", "")).strip()
        title = str(item.get("title", "")).strip()
        if not ARXIV_ID_RE.fullmatch(arxiv_id):
            continue
        entries.append(DiffEntry(arxiv_id=arxiv_id, title=title))
    return entries


def normalize_space(text: str) -> str:
    return " ".join(text.replace("\x0c", " ").replace("\xa0", " ").split())


def trim_pdf_affiliation_text(raw_text: str) -> str:
    lines: list[str] = []
    for raw_line in raw_text.splitlines():
        line = normalize_space(raw_line)
        if not line:
            if lines and lines[-1] != "":
                lines.append("")
            continue
        if PDF_STOP_LINE_RE.match(line):
            break
        if re.fullmatch(r"\d+", line):
            continue
        lines.append(line)

    while lines and lines[-1] == "":
        lines.pop()
    text = "\n".join(lines).strip()
    if len(text) > 5000:
        return text[:5000].rstrip()
    return text


def html_affiliation_text(arxiv_id: str, cache_dir: Path) -> tuple[str, str]:
    try:
        source, text = html_source_text(arxiv_id, cache_dir)
    except Exception:
        return "none", ""
    if source and text:
        return str(source), str(text).strip()
    return "none", ""


def pdf_affiliation_text(arxiv_id: str, cache_dir: Path) -> str:
    try:
        raw = get_pdf_first_page_text(arxiv_id, cache_dir)
    except (FileNotFoundError, RuntimeError, OSError, subprocess.CalledProcessError):
        return ""
    return trim_pdf_affiliation_text(raw)


def process_entry(entry: DiffEntry, cache_dir: Path, github_cache: dict[str, bool]) -> DownloadEntry:
    note = ""
    code_url = ""
    try:
        scan_result = scan_arxiv_page(entry.arxiv_id, entry.title, github_cache)
    except Exception:
        scan_result = {}
    if isinstance(scan_result, dict):
        note = str(scan_result.get("note", "")).strip()
        code_url = str(scan_result.get("code_url", "")).strip()
        if not note:
            note = extract_note(str(scan_result.get("comments", "")))
        if not code_url:
            external_urls = scan_result.get("external_urls")
            if isinstance(external_urls, list):
                for external_url in external_urls[:3]:
                    if not isinstance(external_url, str) or not external_url.startswith("http"):
                        continue
                    project_note, github_urls = project_page_scan(external_url, entry.title)
                    if project_note and not note:
                        note = project_note
                    for github_url in github_urls:
                        if validate_github(github_url, github_cache):
                            code_url = github_url
                            break
                    if code_url:
                        break

    source, affiliation_text = html_affiliation_text(entry.arxiv_id, cache_dir)
    if not affiliation_text:
        pdf_text = pdf_affiliation_text(entry.arxiv_id, cache_dir)
        if pdf_text:
            source = "pdf"
            affiliation_text = pdf_text
        else:
            source = "none"

    return DownloadEntry(
        arxiv_id=entry.arxiv_id,
        affiliation_text=affiliation_text,
        affiliation_source=source,
        note=note,
        code_url=code_url,
    )


def build_payload(input_path: Path, entries: list[DownloadEntry]) -> dict[str, Any]:
    return {
        "downloaded_at": utc_now_iso(),
        "input": str(input_path),
        "count": len(entries),
        "results": [asdict(item) for item in entries],
    }


def write_output(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def run_download(diff_entries: list[DiffEntry], workers: int, cache_dir: Path) -> list[DownloadEntry]:
    if not diff_entries:
        return []
    cache_dir.mkdir(parents=True, exist_ok=True)
    github_cache: dict[str, bool] = {}
    completed: dict[str, DownloadEntry] = {}
    with ThreadPoolExecutor(max_workers=workers) as executor:
        futures = {
            executor.submit(process_entry, entry, cache_dir, github_cache): entry.arxiv_id
            for entry in diff_entries
        }
        for future in as_completed(futures):
            arxiv_id = futures[future]
            try:
                completed[arxiv_id] = future.result()
            except Exception:
                completed[arxiv_id] = DownloadEntry(
                    arxiv_id=arxiv_id,
                    affiliation_text="",
                    affiliation_source="none",
                    note="",
                    code_url="",
                )
    return [completed[entry.arxiv_id] for entry in diff_entries]


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


def main() -> None:
    _install_proxy()
    args = parse_args()
    diff_entries = load_diff_entries(args.input)
    results = run_download(diff_entries=diff_entries, workers=args.workers, cache_dir=args.cache_dir)
    payload = build_payload(input_path=args.input, entries=results)
    write_output(args.output, payload)
    print(f"✓ {len(results)} papers downloaded")
    print(f"→ {args.output}")


if __name__ == "__main__":
    main()
