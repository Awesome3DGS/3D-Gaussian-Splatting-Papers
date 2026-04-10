#!/usr/bin/env python3

from __future__ import annotations

import re
from dataclasses import dataclass
from pathlib import Path


README_PATH = Path("README.md")

YEAR_INDEX = {
    2024: [
        ("ICLR", Path("2024/ICLR.md")),
        ("CVPR", Path("2024/CVPR.md")),
        ("ECCV", Path("2024/ECCV.md")),
        ("ACM MM", Path("2024/ACMMM.md")),
        ("MICCAI", Path("2024/MICCAI.md")),
        ("SIGGRAPH", Path("2024/SIGGRAPH.md")),
        ("NeurIPS", Path("2024/NeurIPS.md")),
        ("ICML", Path("2024/ICML.md")),
        ("BMVC", Path("2024/BMVC.md")),
        ("CoRL", Path("2024/CoRL.md")),
        ("IROS", Path("2024/IROS.md")),
        ("others", Path("2024/Accepted.md")),
    ],
    2025: [
        ("3DV", Path("2025/3DV.md")),
        ("WACV", Path("2025/WACV.md")),
        ("AAAI", Path("2025/AAAI.md")),
        ("ICLR", Path("2025/ICLR.md")),
        ("ICASSP", Path("2025/ICASSP.md")),
        ("ICRA", Path("2025/ICRA.md")),
        ("CVPR", Path("2025/CVPR.md")),
        ("ICCV", Path("2025/ICCV.md")),
        ("ACM MM", Path("2025/ACMMM.md")),
        ("MICCAI", Path("2025/MICCAI.md")),
        ("SIGGRAPH", Path("2025/SIGGRAPH.md")),
        ("ICML", Path("2025/ICML.md")),
        ("IROS", Path("2025/IROS.md")),
        ("ICME", Path("2025/ICME.md")),
        ("ICIP", Path("2025/ICIP.md")),
        ("BMVC", Path("2025/BMVC.md")),
        ("NeurIPS", Path("2025/NeurIPS.md")),
        ("others", Path("2025/Accepted.md")),
    ],
    2026: [
        ("3DV", Path("2026/3DV.md")),
        ("WACV", Path("2026/WACV.md")),
        ("AAAI", Path("2026/AAAI.md")),
        ("ICLR", Path("2026/ICLR.md")),
        ("ICASSP", Path("2026/ICASSP.md")),
        ("ICRA", Path("2026/ICRA.md")),
        ("CVPR", Path("2026/CVPR.md")),
        ("IROS", Path("2026/IROS.md")),
        ("others", Path("2026/Accepted.md")),
    ],
}

DOC_HEADER_NAMES = {
    "3DV.md": "3DV",
    "AAAI.md": "AAAI",
    "ACMMM.md": "ACMMM",
    "BMVC.md": "BMVC",
    "CoRL.md": "CoRL",
    "CVPR.md": "CVPR",
    "ECCV.md": "ECCV",
    "ICASSP.md": "ICASSP",
    "ICCV.md": "ICCV",
    "ICIP.md": "ICIP",
    "ICML.md": "ICML",
    "ICLR.md": "ICLR",
    "ICME.md": "ICME",
    "ICRA.md": "ICRA",
    "IROS.md": "IROS",
    "MICCAI.md": "MICCAI",
    "NeurIPS.md": "NeurIPS",
    "SIGGRAPH.md": "SIGGRAPH",
    "WACV.md": "WACV",
}

MAIN_VENUES = {
    2025: {
        "3DV": Path("2025/3DV.md"),
        "WACV": Path("2025/WACV.md"),
        "AAAI": Path("2025/AAAI.md"),
        "ICLR": Path("2025/ICLR.md"),
        "ICASSP": Path("2025/ICASSP.md"),
        "ICRA": Path("2025/ICRA.md"),
        "CVPR": Path("2025/CVPR.md"),
        "ICCV": Path("2025/ICCV.md"),
        "ACM MM": Path("2025/ACMMM.md"),
        "MICCAI": Path("2025/MICCAI.md"),
        "SIGGRAPH": Path("2025/SIGGRAPH.md"),
        "ICML": Path("2025/ICML.md"),
        "IROS": Path("2025/IROS.md"),
        "ICME": Path("2025/ICME.md"),
        "ICIP": Path("2025/ICIP.md"),
        "BMVC": Path("2025/BMVC.md"),
        "NeurIPS": Path("2025/NeurIPS.md"),
    },
    2026: {
        "3DV": Path("2026/3DV.md"),
        "WACV": Path("2026/WACV.md"),
        "AAAI": Path("2026/AAAI.md"),
        "ICLR": Path("2026/ICLR.md"),
        "ICASSP": Path("2026/ICASSP.md"),
        "ICRA": Path("2026/ICRA.md"),
        "CVPR": Path("2026/CVPR.md"),
        "IROS": Path("2026/IROS.md"),
    },
}

OTHER_VENUES = {
    2025: (
        "CHI 2025",
        "CoRL 2025",
        "Computational Visual Media 2025",
        "IEEE RA-L 2025",
        "IEEE VIS 2025",
        "IMVIP 2025",
        "ISPRS 2025",
        "Pacific Graphics 2025",
        "STAG 2025",
        "VCIP 2025",
    ),
    2026: (
        "ACCV 2026",
        "CVM 2026",
        "DCC 2026",
        "Eurographics 2026",
        "HPCA 2026",
        "ICACT 2026",
        "I3D 2026",
        "TIM 2026",
        "IEEE Transactions on Instrumentation and Measurement 2026",
        "TVCG 2026",
    ),
}

NON_FORMAL_NOTE_MARKERS = (
    "This paper has been withdrawn",
    "Extended version of",
    "Preliminary work",
    "First Rank of",
    "---",
)

ENTRY_SPLIT_RE = re.compile(r"(?m)^#### \[(\d+)\] ")
NOTE_RE = re.compile(r"^- \*\*📝 说明\*\*[:：]\s*(.*)$", re.M)
ARXIV_RE = re.compile(r"\[\[arXiv:([^\]]+)\]")


@dataclass(frozen=True)
class ManagedEntry:
    arxiv_id: str
    title: str
    body: str
    note: str
    target_path: Path

    def to_doc_entry(self) -> "DocEntry":
        return DocEntry(
            arxiv_id=self.arxiv_id,
            title=self.title,
            body=self.body.replace("](./abs/", "](../abs/"),
        )


@dataclass(frozen=True)
class DocEntry:
    arxiv_id: str
    title: str
    body: str

    def render(self, number: int) -> str:
        body = self.body
        return f"#### [{number}] {self.title}\n{body}".rstrip()


def parse_readme_entries(text: str) -> list[ManagedEntry]:
    parts = ENTRY_SPLIT_RE.split(text)
    entries: list[ManagedEntry] = []
    for i in range(1, len(parts), 2):
        block = parts[i + 1]
        title, body = block.split("\n", 1)
        note_match = NOTE_RE.search(body)
        arxiv_match = ARXIV_RE.search(body)
        if note_match is None or arxiv_match is None:
            continue
        note = note_match.group(1).strip()
        target_path = classify_note(note)
        if target_path is None:
            continue
        entries.append(
            ManagedEntry(
                arxiv_id=arxiv_match.group(1),
                title=title.strip(),
                body=body.rstrip(),
                note=note,
                target_path=target_path,
            )
        )
    return entries


def parse_doc_entries(path: Path) -> list[DocEntry]:
    if not path.exists():
        return []
    parts = ENTRY_SPLIT_RE.split(path.read_text())
    entries: list[DocEntry] = []
    for i in range(1, len(parts), 2):
        block = parts[i + 1]
        title, body = block.split("\n", 1)
        arxiv_match = ARXIV_RE.search(body)
        if arxiv_match is None:
            continue
        entries.append(
            DocEntry(
                arxiv_id=arxiv_match.group(1),
                title=title.strip(),
                body=body.rstrip(),
            )
        )
    return entries


def classify_note(note: str) -> Path | None:
    clean_note = note.strip()
    if not clean_note:
        return None
    if any(marker in clean_note for marker in NON_FORMAL_NOTE_MARKERS):
        return None
    for year in (2024, 2025):
        if f"SIGGRAPH Asia {year}" in clean_note:
            return Path(f"{year}/SIGGRAPH.md")
    if "To appear at" in clean_note and "HPCA 2026" in clean_note:
        return Path("2026/Accepted.md")
    if "🏆 Accepted to ACM MM 2025" in clean_note:
        return Path("2025/ACMMM.md")
    if "🏆 Accepted to CHI 2025" in clean_note:
        return Path("2025/Accepted.md")
    if "🏆 Accepted to Computational Visual Media 2025" in clean_note:
        return Path("2025/Accepted.md")
    if "Eurographics 2026" in clean_note:
        return Path("2026/Accepted.md")
    for venue in OTHER_VENUES[2025]:
        if venue in clean_note:
            return Path("2025/Accepted.md")
    for venue in OTHER_VENUES[2026]:
        if venue in clean_note:
            return Path("2026/Accepted.md")
    if "CVPR Finding 2026" in clean_note or "CVPR 2026 Findings Track" in clean_note:
        return Path("2026/CVPR.md")
    for year, venues in MAIN_VENUES.items():
        for venue, target_path in venues.items():
            if f"{venue} {year}" in clean_note:
                return target_path
    if clean_note.startswith("🏆 Accepted to ICASSP"):
        return Path("2026/ICASSP.md")
    return None


def read_doc_arxiv_ids(path: Path) -> set[str]:
    if not path.exists():
        return set()
    return set(ARXIV_RE.findall(path.read_text()))


def doc_header(path: Path) -> str:
    year = path.parent.name
    if path.name == "Accepted.md":
        return f"# 3D Gaussian Splatting Papers Accepted in {year}"
    return f"# 3D Gaussian Splatting Papers Accepted to {DOC_HEADER_NAMES[path.name]}{year}"


def renumber_entries(text: str) -> str:
    counter = 1

    def repl(match: re.Match[str]) -> str:
        nonlocal counter
        replacement = f"#### [{counter}] "
        counter += 1
        return replacement

    return ENTRY_SPLIT_RE.sub(repl, text)


def sync_doc(path: Path, new_entries: list[ManagedEntry], managed_arxiv_ids: set[str]) -> bool:
    if not new_entries and not path.exists():
        return False

    path.parent.mkdir(parents=True, exist_ok=True)
    header = doc_header(path)
    preserved_entries = [
        entry for entry in parse_doc_entries(path) if entry.arxiv_id not in managed_arxiv_ids
    ]
    merged_entries = preserved_entries + [entry.to_doc_entry() for entry in new_entries]
    rendered = [
        entry.render(idx)
        for idx, entry in enumerate(sorted(merged_entries, key=lambda item: item.arxiv_id), start=1)
    ]
    body = "\n\n".join(rendered)
    new_text = f"{header}\n\n{body}\n" if body else f"{header}\n"
    existing_text = path.read_text() if path.exists() else ""
    if existing_text != new_text:
        path.write_text(new_text)
        return True
    return False


def count_entries(path: Path) -> int:
    if not path.exists():
        return 0
    return len(re.findall(r"(?m)^#### \[\d+\] ", path.read_text()))


def render_year_section(year: int, rows: list[list[tuple[str, Path]]]) -> str:
    lines = [f"- **{year}**", ""]
    for row in rows:
        row_lines = []
        for index, (label, path) in enumerate(row):
            n = count_entries(path)
            if n == 0:
                continue
            prefix = "  - " if not row_lines else "    "
            row_lines.append(f"{prefix}[[{label}](./{path.as_posix()})] ({n} 篇)")
        lines.extend(row_lines)
    return "\n".join(lines)


def update_readme_index() -> bool:
    readme_text = README_PATH.read_text()
    sections = [
        render_year_section(
            2024,
            [
                YEAR_INDEX[2024][:6],
                YEAR_INDEX[2024][6:],
            ],
        ),
        render_year_section(
            2025,
            [
                YEAR_INDEX[2025][:6],
                YEAR_INDEX[2025][6:11],
                YEAR_INDEX[2025][11:16],
                YEAR_INDEX[2025][16:],
            ],
        ),
        render_year_section(
            2026,
            [
                YEAR_INDEX[2026][:6],
                YEAR_INDEX[2026][6:],
            ],
        ),
    ]
    new_block = "#### **📚 会议期刊**\n\n" + "\n\n".join(sections) + "\n\n#### **📂 归档论文**"
    new_text, count = re.subn(
        r"(?s)#### \*\*📚 会议期刊\*\*\n\n.*?\n#### \*\*📂 归档论文\*\*",
        new_block,
        readme_text,
        count=1,
    )
    if count != 1:
        raise RuntimeError("Failed to update README conference index block.")
    if new_text != readme_text:
        README_PATH.write_text(new_text)
        return True
    return False


def main() -> None:
    entries = parse_readme_entries(README_PATH.read_text())
    grouped: dict[Path, list[ManagedEntry]] = {}
    for entry in entries:
        grouped.setdefault(entry.target_path, []).append(entry)
    managed_arxiv_ids = {entry.arxiv_id for entry in entries}

    managed_paths = {
        path
        for year_paths in YEAR_INDEX.values()
        for _, path in year_paths
    }

    changed = False
    for path in sorted(managed_paths | set(grouped.keys()), key=lambda item: item.as_posix()):
        changed = sync_doc(path, grouped.get(path, []), managed_arxiv_ids) or changed
    changed = update_readme_index() or changed

    if not changed:
        print("No accepted-paper docs needed updates.")
        return
    print("Synced accepted-paper docs and README index.")


if __name__ == "__main__":
    main()
