#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path


ARXIV_RE = re.compile(r"\[arXiv:([0-9]{4}\.[0-9]{5})\]")


@dataclass(frozen=True)
class DiffEntry:
    arxiv_id: str
    title: str
    authors: list[str]
    abstract: str
    submitted: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Compute fetched-vs-existing paper diff from arXiv sync payload."
    )
    parser.add_argument(
        "fetch_json",
        nargs="?",
        default="-",
        help="Fetch JSON file path (default: stdin).",
    )
    parser.add_argument(
        "--readme",
        type=Path,
        default=Path("README.md"),
        help="README path for existing arXiv IDs (default: README.md).",
    )
    parser.add_argument(
        "--abs-dir",
        type=Path,
        default=Path("abs"),
        help="abs directory path for existing IDs (default: abs).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output JSON file path (default: stdout).",
    )
    return parser.parse_args()


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def read_json_input(source: str) -> dict[str, object]:
    if source == "-":
        raw = sys.stdin.read()
    else:
        raw = Path(source).read_text()
    data = json.loads(raw)
    if not isinstance(data, dict):
        raise ValueError("Fetch payload must be a JSON object.")
    return data


def load_readme_ids(readme_path: Path) -> set[str]:
    if not readme_path.exists():
        return set()
    return set(ARXIV_RE.findall(readme_path.read_text()))


def load_abs_ids(abs_dir: Path) -> set[str]:
    if not abs_dir.exists():
        return set()
    return {path.stem for path in abs_dir.glob("*.md")}


def normalize_authors(raw: object) -> list[str]:
    if not isinstance(raw, list):
        return []
    result = []
    for item in raw:
        if isinstance(item, str):
            cleaned = item.strip()
            if cleaned:
                result.append(cleaned)
    return result


def build_diff_payload(
    fetch_payload: dict[str, object], readme_path: Path, abs_dir: Path
) -> dict[str, object]:
    fetched_results = fetch_payload.get("results")
    if not isinstance(fetched_results, list):
        raise ValueError("Fetch payload must contain a list field: results")

    since_id = fetch_payload.get("since")
    since_value = str(since_id) if since_id is not None else ""

    existing_ids = load_readme_ids(readme_path) | load_abs_ids(abs_dir)

    new_entries: list[DiffEntry] = []
    existing_in_fetch: set[str] = set()
    for item in fetched_results:
        if not isinstance(item, dict):
            continue
        arxiv_id = str(item.get("arxiv_id", "")).strip()
        if not arxiv_id:
            continue
        if arxiv_id in existing_ids:
            existing_in_fetch.add(arxiv_id)
            continue
        new_entries.append(
            DiffEntry(
                arxiv_id=arxiv_id,
                title=str(item.get("title", "")).strip(),
                authors=normalize_authors(item.get("authors")),
                abstract=str(item.get("abstract", "")).strip(),
                submitted=str(item.get("submitted", "")).strip(),
            )
        )

    return {
        "computed_at": utc_now_iso(),
        "since": since_value,
        "total_fetched": len(fetched_results),
        "new_count": len(new_entries),
        "new": [asdict(entry) for entry in new_entries],
        "existing_count": len(existing_in_fetch),
        "existing": sorted(existing_in_fetch, reverse=True),
    }


def write_output(payload: dict[str, object], output_path: Path | None) -> None:
    rendered = json.dumps(payload, ensure_ascii=False, indent=2)
    if output_path is None:
        sys.stdout.write(rendered + "\n")
        return
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered + "\n")


def main() -> None:
    args = parse_args()
    payload = read_json_input(args.fetch_json)
    diff = build_diff_payload(payload, readme_path=args.readme, abs_dir=args.abs_dir)
    write_output(diff, args.output)


if __name__ == "__main__":
    main()
