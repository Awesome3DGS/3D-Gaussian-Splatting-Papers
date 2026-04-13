#!/usr/bin/env python3

from __future__ import annotations

import argparse
import re
from collections import Counter, defaultdict
from dataclasses import dataclass
from pathlib import Path


README_PATH = Path("README.md")
ARCHIVE_SOURCES = [
    Path("archive/202407.md"),
    Path("archive/202410.md"),
    Path("archive/202501.md"),
    Path("archive/202504.md"),
    Path("archive/202507.md"),
]
SOURCE_PATHS = [README_PATH, *ARCHIVE_SOURCES]

ENTRY_SPLIT_RE = re.compile(r"(?m)^#### \[(\d+)\] ")
NOTE_RE = re.compile(r"^- \*\*📝 说明\*\*[:：]\s*(.*)$", re.M)
ARXIV_RE = re.compile(r"arXiv:(\d{4}\.\d{5}(?:v\d+)?)")
YEAR_RE = re.compile(r"(20\d{2})")


@dataclass(frozen=True)
class PaperEntry:
    title: str
    body: str
    note: str
    arxiv_id: str


@dataclass(frozen=True)
class SourceDoc:
    path: Path
    prefix: str
    entries: list[PaperEntry]
    original_text: str


@dataclass(frozen=True)
class AcceptedInfo:
    venue: str
    year: str
    workshop: str


@dataclass(frozen=True)
class MovePlan:
    source_path: Path
    source_index: int
    entry: PaperEntry
    venue: str
    year: str
    workshop: str
    target_path: Path


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Move accepted paper entries from README/archive time slices to archive/{year} files."
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print planned moves only, without modifying files.",
    )
    return parser.parse_args()


def normalize_spaces(text: str) -> str:
    return " ".join(text.strip().split())


def sanitize_filename(stem: str) -> str:
    cleaned = stem.strip()
    for old, new in (("/", "-"), ("\\", "-"), (":", "-"), ("|", "-"), ("?", "-"), ("*", "-"), ('"', "-"), ("<", "-"), (">", "-")):
        cleaned = cleaned.replace(old, new)
    cleaned = normalize_spaces(cleaned)
    return cleaned or "Accepted"


def parse_entries(text: str) -> tuple[str, list[PaperEntry]]:
    parts = ENTRY_SPLIT_RE.split(text)
    if len(parts) <= 1:
        return text, []

    prefix = parts[0]
    entries: list[PaperEntry] = []
    for i in range(1, len(parts), 2):
        block = parts[i + 1]
        if "\n" in block:
            title, body = block.split("\n", 1)
            body = body.rstrip()
        else:
            title = block.rstrip()
            body = ""

        note_match = NOTE_RE.search(body)
        arxiv_match = ARXIV_RE.search(body)
        entries.append(
            PaperEntry(
                title=title.strip(),
                body=body,
                note=note_match.group(1).strip() if note_match else "",
                arxiv_id=arxiv_match.group(1) if arxiv_match else "",
            )
        )
    return prefix, entries


def render_entries(entries: list[PaperEntry]) -> str:
    chunks = []
    for idx, entry in enumerate(entries, start=1):
        chunks.append(f"#### [{idx}] {entry.title}\n{entry.body}".rstrip())
    return "\n\n".join(chunks)


def render_source_doc(prefix: str, entries: list[PaperEntry]) -> str:
    if not entries:
        return ""
    body = render_entries(entries)
    stripped_prefix = prefix.rstrip()
    if stripped_prefix:
        return f"{stripped_prefix}\n\n{body}\n"
    return f"{body}\n"


def read_source_docs() -> list[SourceDoc]:
    docs: list[SourceDoc] = []
    for path in SOURCE_PATHS:
        if not path.exists():
            raise FileNotFoundError(f"Missing source file: {path}")
        text = path.read_text()
        prefix, entries = parse_entries(text)
        docs.append(SourceDoc(path=path, prefix=prefix, entries=entries, original_text=text))
    return docs


def parse_acceptance(note: str) -> AcceptedInfo | None:
    clean_note = normalize_spaces(note)
    marker = "Accepted to"
    marker_index = clean_note.find(marker)
    if marker_index == -1:
        return None

    tail = clean_note[marker_index + len(marker) :].strip(" ：:-")
    year_match = YEAR_RE.search(tail)
    if year_match is None:
        return AcceptedInfo(venue="", year="", workshop="")

    venue = tail[: year_match.start()].strip(" ：:-")
    venue = re.sub(r"^(?:the)\s+", "", venue, flags=re.I).strip()
    if venue.lower() in {"the", "a", "an"}:
        venue = ""
    year = year_match.group(1)
    suffix = tail[year_match.end() :].strip(" ：:-")
    workshop = suffix if "workshop" in suffix.lower() else ""
    return AcceptedInfo(
        venue=normalize_spaces(venue),
        year=year,
        workshop=normalize_spaces(workshop),
    )


def arxiv_sort_key(arxiv_id: str) -> tuple[int, int, int]:
    match = re.fullmatch(r"(\d{4})\.(\d{5})(?:v(\d+))?", arxiv_id.strip())
    if match is None:
        return (9999, 99999, 9999)
    return (
        int(match.group(1)),
        int(match.group(2)),
        int(match.group(3) or 0),
    )


def key_to_target_path(year: str, venue: str, workshop: str, count: int) -> Path:
    if count > 5:
        stem = venue if not workshop else f"{venue} {workshop}"
        return Path(year) / f"{sanitize_filename(stem)}.md"
    return Path(year) / "Accepted.md"


def target_header(path: Path) -> str:
    year = path.parent.name
    if path.name == "Accepted.md":
        return f"# 3D Gaussian Splatting Papers Accepted in {year}"
    return f"# 3D Gaussian Splatting Papers Accepted to {path.stem} {year}"


def update_readme_archive_counts(readme_text: str, counts: dict[Path, int]) -> str:
    updated = readme_text
    for path, count in counts.items():
        path_text = path.as_posix()
        pattern = re.compile(
            rf"(\[\[[^\]]+\]\(\./{re.escape(path_text)}\)\]\s*\()(\d+)(\s*篇\))"
        )
        updated, replaced = pattern.subn(rf"\g<1>{count}\3", updated, count=1)
        if replaced != 1:
            print(f"WARNING: failed to update README archive count link for {path_text}")
    return updated


def build_move_plan(source_docs: list[SourceDoc]) -> tuple[list[MovePlan], list[str]]:
    warnings: list[str] = []
    provisional: list[tuple[Path, int, PaperEntry, str, str, str]] = []
    key_counter: Counter[tuple[str, str, str]] = Counter()

    for doc in source_docs:
        for idx, entry in enumerate(doc.entries):
            accepted = parse_acceptance(entry.note)
            if accepted is None:
                continue
            if not accepted.venue or not accepted.year:
                warnings.append(
                    "WARNING: malformed accepted entry skipped: "
                    f"{doc.path} | {entry.title} | note={entry.note!r}"
                )
                continue
            if not entry.arxiv_id:
                warnings.append(
                    "WARNING: missing arXiv ID, accepted entry skipped: "
                    f"{doc.path} | {entry.title}"
                )
                continue
            key = (accepted.year, accepted.venue, accepted.workshop)
            key_counter[key] += 1
            provisional.append(
                (
                    doc.path,
                    idx,
                    entry,
                    accepted.year,
                    accepted.venue,
                    accepted.workshop,
                )
            )

    plans: list[MovePlan] = []
    for source_path, source_index, entry, year, venue, workshop in provisional:
        key = (year, venue, workshop)
        target_path = key_to_target_path(
            year=year,
            venue=venue,
            workshop=workshop,
            count=key_counter[key],
        )
        plans.append(
            MovePlan(
                source_path=source_path,
                source_index=source_index,
                entry=entry,
                venue=venue,
                year=year,
                workshop=workshop,
                target_path=target_path,
            )
        )
    return plans, warnings


def load_target_entries(path: Path) -> tuple[str, list[PaperEntry]]:
    if not path.exists():
        return target_header(path), []
    text = path.read_text()
    prefix, entries = parse_entries(text)
    if entries:
        return prefix, entries
    existing_header = prefix.strip()
    return (existing_header if existing_header else target_header(path)), []


def apply_moves(source_docs: list[SourceDoc], plans: list[MovePlan], dry_run: bool) -> None:
    moves_by_source: dict[Path, set[int]] = defaultdict(set)
    moves_by_target: dict[Path, list[PaperEntry]] = defaultdict(list)

    for plan in plans:
        moves_by_source[plan.source_path].add(plan.source_index)
        moves_by_target[plan.target_path].append(plan.entry)

    remaining_by_source: dict[Path, list[PaperEntry]] = {}
    updated_counts: dict[Path, int] = {}
    source_lookup = {doc.path: doc for doc in source_docs}

    for path in SOURCE_PATHS:
        doc = source_lookup[path]
        removed_indexes = moves_by_source.get(path, set())
        remaining = [entry for idx, entry in enumerate(doc.entries) if idx not in removed_indexes]
        remaining_by_source[path] = remaining
        updated_counts[path] = len(remaining)

    archive_counts = {archive_path: updated_counts[archive_path] for archive_path in ARCHIVE_SOURCES}

    for path in SOURCE_PATHS:
        doc = source_lookup[path]
        remaining = remaining_by_source[path]
        rendered = render_source_doc(doc.prefix, remaining)
        if path == README_PATH and remaining:
            rendered = update_readme_archive_counts(rendered, archive_counts)
        if not dry_run and rendered != doc.original_text:
            path.write_text(rendered)

    for target_path, additions in moves_by_target.items():
        prefix, existing_entries = load_target_entries(target_path)

        merged_by_id: dict[str, PaperEntry] = {}
        without_id: list[PaperEntry] = []
        for entry in existing_entries:
            if entry.arxiv_id:
                merged_by_id[entry.arxiv_id] = entry
            else:
                without_id.append(entry)
        for entry in additions:
            merged_by_id[entry.arxiv_id] = entry

        merged = list(merged_by_id.values()) + without_id
        merged.sort(key=lambda item: arxiv_sort_key(item.arxiv_id))
        rendered = render_source_doc(prefix, merged)

        if not dry_run:
            target_path.parent.mkdir(parents=True, exist_ok=True)
            old_text = target_path.read_text() if target_path.exists() else ""
            if rendered != old_text:
                target_path.write_text(rendered)


def print_plan(plans: list[MovePlan], dry_run: bool) -> None:
    phase = "DRY-RUN" if dry_run else "APPLY"
    for plan in sorted(
        plans,
        key=lambda item: (
            item.target_path.as_posix(),
            arxiv_sort_key(item.entry.arxiv_id),
            item.source_path.as_posix(),
        ),
    ):
        print(
            f"{phase}: {plan.source_path} -> {plan.target_path} "
            f"| arXiv:{plan.entry.arxiv_id} | {plan.entry.title}"
        )

    grouped: Counter[str] = Counter(plan.target_path.as_posix() for plan in plans)
    print(f"{phase}: total entries: {len(plans)}")
    for target, count in sorted(grouped.items()):
        print(f"{phase}: {target} <= {count}")


def main() -> None:
    args = parse_args()
    dry_run: bool = args.dry_run

    source_docs = read_source_docs()
    plans, warnings = build_move_plan(source_docs)

    for warning in warnings:
        print(warning)

    if not plans:
        print("No accepted entries found to move.")
        return

    print_plan(plans, dry_run=dry_run)
    apply_moves(source_docs, plans, dry_run=dry_run)


if __name__ == "__main__":
    main()
