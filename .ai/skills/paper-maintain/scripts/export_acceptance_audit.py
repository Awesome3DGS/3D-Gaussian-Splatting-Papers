#!/usr/bin/env python3

from __future__ import annotations

import csv
import json
from dataclasses import asdict, dataclass
from datetime import date
from pathlib import Path

from sync import README_PATH, classify_note


def default_audit_dir() -> Path:
    return Path(f"tmp/acceptance-audit-{date.today()}")


@dataclass(frozen=True)
class AuditEntry:
    readme_index: int
    arxiv_id: str
    arxiv_month: str
    title: str
    note_category: str
    current_note: str
    suggested_audit_bucket: str
    likely_venues: list[str]
    abs_path: str
    has_code_url: bool
    code_url: str


def parse_readme_blocks(text: str) -> list[dict[str, str | int]]:
    blocks: list[dict[str, str | int]] = []
    parts = text.split("#### [")
    for chunk in parts[1:]:
        number_text, rest = chunk.split("] ", 1)
        readme_index = int(number_text)
        title, body = rest.split("\n", 1)
        info = {
            "readme_index": readme_index,
            "title": title.strip(),
            "body": body.rstrip(),
        }
        for line in body.splitlines():
            if line.startswith("- **🔗 链接**"):
                info["link_line"] = line
            elif line.startswith("- **📝 说明**"):
                info["note"] = line.split(":", 1)[1].strip()
        blocks.append(info)
    return blocks


def parse_arxiv_id(link_line: str) -> str:
    marker = "[[arXiv:"
    start = link_line.find(marker)
    if start == -1:
        return ""
    start += len(marker)
    end = link_line.find("]", start)
    return link_line[start:end]


def parse_abs_path(link_line: str) -> str:
    marker = "[[中英摘要]("
    start = link_line.find(marker)
    if start == -1:
        return ""
    start += len(marker)
    end = link_line.find(")", start)
    return link_line[start:end]


def parse_code_url(link_line: str) -> str:
    marker = "[[Code]("
    start = link_line.find(marker)
    if start == -1:
        return ""
    start += len(marker)
    end = link_line.find(")", start)
    return link_line[start:end]


def arxiv_month(arxiv_id: str) -> str:
    prefix = arxiv_id.split(".")[0]
    if len(prefix) != 4 or not prefix.isdigit():
        return ""
    return f"20{prefix[:2]}-{prefix[2:]}"


def note_category(note: str) -> str:
    stripped = note.strip()
    if not stripped or stripped == "---":
        return "pending"
    if classify_note(stripped) is not None:
        return "formal"
    lowered = stripped.lower()
    if "withdrawn" in lowered:
        return "withdrawn"
    if any(
        token in stripped
        for token in (
            "Extended version of",
            "Preliminary work",
            "First Rank of",
        )
    ):
        return "context_only"
    return "nonformal_other"


def likely_bucket(arxiv_id: str) -> tuple[str, list[str]]:
    prefix = arxiv_id.split(".")[0]
    if not prefix.isdigit() or len(prefix) != 4:
        return "older_or_misc", ["Manual audit"]
    yymm = int(prefix)
    if 2511 <= yymm <= 2603:
        return (
            "recent_2026_cycle",
            [
                "AAAI 2026",
                "WACV 2026",
                "3DV 2026",
                "ICLR 2026",
                "CVPR 2026",
                "ICRA 2026",
                "IROS 2026",
                "ICASSP 2026",
            ],
        )
    if 2507 <= yymm <= 2510:
        return (
            "late_2025_cycle",
            [
                "ICCV 2025",
                "ACM MM 2025",
                "NeurIPS 2025",
                "SIGGRAPH Asia 2025",
                "BMVC 2025",
                "IROS 2025",
                "MICCAI 2025",
                "ICIP 2025",
                "ICME 2025",
            ],
        )
    if 2501 <= yymm <= 2506:
        return (
            "mid_2025_cycle",
            [
                "CVPR 2025",
                "SIGGRAPH 2025",
                "ICML 2025",
                "ICRA 2025",
                "ACM MM 2025",
                "MICCAI 2025",
                "IROS 2025",
            ],
        )
    if 2411 <= yymm <= 2412:
        return (
            "early_2025_cycle",
            [
                "AAAI 2025",
                "3DV 2025",
                "WACV 2025",
                "ICLR 2025",
                "CVPR 2025",
            ],
        )
    return (
        "older_or_misc",
        [
            "2024 conferences / journals",
            "2025 journals",
            "Manual audit",
        ],
    )


def build_entries() -> list[AuditEntry]:
    entries: list[AuditEntry] = []
    readme_text = README_PATH.read_text()
    for block in parse_readme_blocks(readme_text):
        link_line = str(block.get("link_line", ""))
        arxiv_id = parse_arxiv_id(link_line)
        if not arxiv_id:
            continue
        note = str(block.get("note", ""))
        category = note_category(note)
        bucket, venues = likely_bucket(arxiv_id)
        entries.append(
            AuditEntry(
                readme_index=int(block["readme_index"]),
                arxiv_id=arxiv_id,
                arxiv_month=arxiv_month(arxiv_id),
                title=str(block["title"]),
                note_category=category,
                current_note=note,
                suggested_audit_bucket=bucket,
                likely_venues=venues,
                abs_path=parse_abs_path(link_line),
                has_code_url=bool(parse_code_url(link_line)),
                code_url=parse_code_url(link_line),
            )
        )
    return entries


def write_csv(path: Path, entries: list[AuditEntry]) -> None:
    with path.open("w", newline="", encoding="utf-8") as f:
        writer = csv.writer(f)
        writer.writerow(
            [
                "readme_index",
                "arxiv_id",
                "arxiv_month",
                "title",
                "note_category",
                "current_note",
                "suggested_audit_bucket",
                "likely_venues",
                "abs_path",
                "has_code_url",
                "code_url",
            ]
        )
        for entry in entries:
            writer.writerow(
                [
                    entry.readme_index,
                    entry.arxiv_id,
                    entry.arxiv_month,
                    entry.title,
                    entry.note_category,
                    entry.current_note,
                    entry.suggested_audit_bucket,
                    " | ".join(entry.likely_venues),
                    entry.abs_path,
                    "yes" if entry.has_code_url else "no",
                    entry.code_url,
                ]
            )


def write_json(path: Path, entries: list[AuditEntry]) -> None:
    with path.open("w", encoding="utf-8") as f:
        json.dump([asdict(entry) for entry in entries], f, ensure_ascii=False, indent=2)


def write_summary(path: Path, entries: list[AuditEntry]) -> None:
    categories = {}
    buckets = {}
    for entry in entries:
        categories[entry.note_category] = categories.get(entry.note_category, 0) + 1
        if entry.note_category in {"pending", "context_only", "nonformal_other"}:
            buckets[entry.suggested_audit_bucket] = buckets.get(entry.suggested_audit_bucket, 0) + 1

    pending_entries = [
        entry
        for entry in entries
        if entry.note_category in {"pending", "context_only", "nonformal_other"}
    ]
    pending_entries.sort(key=lambda item: (item.arxiv_id, item.readme_index), reverse=True)

    lines = [
        "# Acceptance Audit Export",
        "",
        f"- Total README entries with arXiv links: {len(entries)}",
        "",
        "## Category Counts",
    ]
    for key in sorted(categories):
        lines.append(f"- {key}: {categories[key]}")
    lines.extend(["", "## Pending Audit Buckets"])
    for key in sorted(buckets):
        lines.append(f"- {key}: {buckets[key]}")
    lines.extend(
        [
            "",
            "## Pending Candidates Preview",
            "",
            "| README | arXiv | Month | Bucket | Note | Title |",
            "| --- | --- | --- | --- | --- | --- |",
        ]
    )
    for entry in pending_entries[:50]:
        note = entry.current_note if entry.current_note else "(empty)"
        note = note.replace("|", "/")
        title = entry.title.replace("|", "/")
        lines.append(
            f"| {entry.readme_index} | {entry.arxiv_id} | {entry.arxiv_month} | {entry.suggested_audit_bucket} | {note} | {title} |"
        )
    path.write_text("\n".join(lines) + "\n")


def main() -> None:
    import argparse
    parser = argparse.ArgumentParser(description="Export acceptance audit tables.")
    parser.add_argument("--output-dir", type=Path, default=None, help="Output directory (default: tmp/acceptance-audit-YYYY-MM-DD).")
    args = parser.parse_args()
    AUDIT_DIR = args.output_dir or default_audit_dir()
    AUDIT_DIR.mkdir(parents=True, exist_ok=True)
    entries = build_entries()
    pending_entries = [
        entry
        for entry in entries
        if entry.note_category in {"pending", "context_only", "nonformal_other"}
    ]
    recent_with_code = [
        entry
        for entry in pending_entries
        if entry.suggested_audit_bucket == "recent_2026_cycle" and entry.has_code_url
    ]
    pending_entries.sort(key=lambda item: (item.arxiv_id, item.readme_index), reverse=True)
    recent_with_code.sort(key=lambda item: (item.arxiv_id, item.readme_index), reverse=True)

    write_csv(AUDIT_DIR / "all_entries.csv", entries)
    write_json(AUDIT_DIR / "all_entries.json", entries)
    write_csv(AUDIT_DIR / "pending_candidates.csv", pending_entries)
    write_json(AUDIT_DIR / "pending_candidates.json", pending_entries)
    write_csv(AUDIT_DIR / "priority_recent_2026_with_code.csv", recent_with_code)
    write_json(AUDIT_DIR / "priority_recent_2026_with_code.json", recent_with_code)
    write_summary(AUDIT_DIR / "README.md", entries)

    print(f"Exported acceptance audit files to {AUDIT_DIR}")
    print(
        f"all_entries={len(entries)} pending_candidates={len(pending_entries)} recent_2026_with_code={len(recent_with_code)}"
    )


if __name__ == "__main__":
    main()
