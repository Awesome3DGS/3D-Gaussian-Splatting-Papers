#!/usr/bin/env python3
from __future__ import annotations
import argparse
import json
import re
import sys
from collections import defaultdict
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any, Callable
VENUE_GROUPS = {
    "CVPR": ("computer vision and pattern recognition", "cvpr"),
    "ECCV": ("european conference on computer vision", "eccv"),
    "Eurographics": ("eurographics", "eurographics symposium"),
    "ICCV": ("international conference on computer vision", "iccv"),
    "NeurIPS": ("neural information processing systems", "neurips", "nips"),
    "SIGGRAPH": ("special interest group on computer graphics", "siggraph"),
    "ICLR": ("international conference on learning representations", "iclr"),
    "AAAI": ("aaai conference on artificial intelligence", "aaai"),
    "ACM MM": ("acm international conference on multimedia", "acm mm", "acm multimedia"),
    "MICCAI": ("medical image computing and computer-assisted intervention", "miccai"),
    "ICML": ("international conference on machine learning", "icml"),
    "3DV": ("international conference on 3d vision", "3dv"),
    "WACV": ("winter conference on applications of computer vision", "wacv"),
    "ICRA": ("international conference on robotics and automation", "icra"),
    "IROS": ("intelligent robots and systems", "iros"),
    "IEEE VR": ("ieee vr", "ieee virtual reality", "ieee conference on virtual reality"),
}
VENUE_MAP: dict[str, str] = {key: abbr for abbr, keys in VENUE_GROUPS.items() for key in keys}
DISCOVERY_SOURCE_ORDER = {"arxiv_comment": 0, "arxiv_html": 1, "github_search": 2}
ENTRY_HEADING_RE = re.compile(r"^#### \[(\d+)\] ")
LINK_LINE_RE = re.compile(r"^(\s*- \*\*\U0001f517 \u94fe\u63a5\*\*[:\uff1a][ \t\u00a0]*)(.*?)(\r?\n?)$")
NOTE_LINE_RE = re.compile(r"^(\s*- \*\*\U0001f4dd \u8bf4\u660e\*\*[:\uff1a][ \t\u00a0]*)(.*?)(\r?\n?)$")
PLAIN_CODE_RE = re.compile(r"(?<!\[)\[Code\](?!\()")
CODE_URL_RE = re.compile(r"\[\[Code\]\((https?://[^)\s]+)\)\]|\[Code\]\((https?://[^)\s]+)\)")
YEAR_RE = re.compile(r"(\d{4})")
COMMENT_ACCEPTED_RE = re.compile(r"accepted(?:\s+for\s+publication)?\s*(?:to|at|in|@|by)\s+(.+?)\s*(\d{4})", re.IGNORECASE)
COMMENT_VENUE_YEAR_RE = re.compile(r"(.+?)\s+(\d{4})(?:\s+(?:workshop|poster|oral))?", re.IGNORECASE)
ACCEPTANCE_HINT_RE = re.compile(r"(accepted|to appear|published)", re.IGNORECASE)
COMMENT_SKIP_ACCEPTANCE_RE = re.compile(
    r"\bsubmit(?:ted)?\b|\bunder\s+review(?:ed)?\b|for\s+possible\s+publication|extended\s+version\s+of|journal\s+extension\s+of",
    re.IGNORECASE,
)
WORKSHOP_WORD_RE = re.compile(r"\bworkshop\b", re.IGNORECASE)
WORKSHOP_NAME_AFTER_RE = re.compile(r"\bworkshop\b(?:\s+on|\s+for|\s*:)?\s*[\"']?([^\"'.,;()]+)", re.IGNORECASE)
WORKSHOP_NAME_BEFORE_RE = re.compile(r"([A-Za-z0-9][A-Za-z0-9/&:+\- ]{1,80}?)\s+workshop\b", re.IGNORECASE)
PARENS_ABBR_RE = re.compile(r"\(([A-Za-z][A-Za-z0-9]{1,15})\)")
@dataclass
class AcceptanceDecision:
    source: str
    evidence_text: str
    venue_raw: str
    venue_abbr: str
    year: str
    note: str
    suspicious: bool
    reasons: list[str]
@dataclass
class EntryContext:
    arxiv_id: str
    title: str
    source_file: str
    entry_index: int
class MarkdownEditor:
    def __init__(self, path: Path) -> None:
        self.path = path
        self.lines = path.read_text(encoding="utf-8").splitlines(keepends=True)
        self.entry_ranges = self._index_entries()
        self.changed = False
    def _index_entries(self) -> dict[int, tuple[int, int]]:
        starts = [(int(m.group(1)), i) for i, line in enumerate(self.lines) if (m := ENTRY_HEADING_RE.match(line))]
        ranges: dict[int, tuple[int, int]] = {}
        for i, (entry_index, start) in enumerate(starts):
            end = starts[i + 1][1] if i + 1 < len(starts) else len(self.lines)
            ranges.setdefault(entry_index, (start, end))
        return ranges
    def _find_field_line(self, entry_index: int, pattern: re.Pattern[str]) -> int | None:
        span = self.entry_ranges.get(entry_index)
        if span is None:
            return None
        start, end = span
        return next((i for i in range(start + 1, end) if pattern.match(self.lines[i])), None)
    def get_note(self, entry_index: int) -> tuple[int | None, str]:
        i = self._find_field_line(entry_index, NOTE_LINE_RE)
        if i is None:
            return None, ""
        m = NOTE_LINE_RE.match(self.lines[i])
        assert m is not None
        return i, m.group(2).strip()
    def set_note(self, line_index: int, value: str) -> None:
        m = NOTE_LINE_RE.match(self.lines[line_index])
        assert m is not None
        prefix = m.group(1)
        joiner = " " if value and not prefix.endswith((" ", "\t", "\u00a0")) else ""
        self.lines[line_index] = f"{prefix}{joiner}{value}{m.group(3)}"
        self.changed = True
    def get_link(self, entry_index: int) -> tuple[int | None, str]:
        i = self._find_field_line(entry_index, LINK_LINE_RE)
        if i is None:
            return None, ""
        m = LINK_LINE_RE.match(self.lines[i])
        assert m is not None
        return i, m.group(2)
    def set_link(self, line_index: int, value: str) -> None:
        m = LINK_LINE_RE.match(self.lines[line_index])
        assert m is not None
        self.lines[line_index] = f"{m.group(1)}{value}{m.group(3)}"
        self.changed = True
    def save(self) -> None:
        if self.changed:
            self.path.write_text("".join(self.lines), encoding="utf-8")
def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")
def file_timestamp_now() -> str:
    return datetime.now().strftime("%Y%m%d-%H%M%S")
def clean_text(value: str | None) -> str:
    return " ".join((value or "").replace("\xa0", " ").split())
def to_int(value: Any, default: int = 0) -> int:
    try:
        return int(value)
    except (TypeError, ValueError):
        return default
def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description=(
            "Patch archive/README entries from acceptance_check JSON: "
            "write acceptance note and/or code URL back to markdown entries."
        )
    )
    parser.add_argument("--input", type=Path, required=True, help="JSON report produced by paper check (acceptance_check.py).")
    parser.add_argument("--dry-run", action="store_true", help="Print intended changes without writing markdown or evidence JSON.")
    parser.add_argument("--yes", action="store_true", help="Auto-accept all suspicious items without interactive confirmation.")
    parser.add_argument("--no-code", action="store_true", help="Disable code URL patching.")
    parser.add_argument("--no-acceptance", action="store_true", help="Disable acceptance note patching.")
    args = parser.parse_args()
    if args.no_code and args.no_acceptance:
        parser.error("At least one of --no-code/--no-acceptance must be disabled.")
    return args
def map_venue(text: str) -> tuple[str, str]:
    lowered = text.lower()
    best_key = ""
    best_abbr = ""
    for key, abbr in VENUE_MAP.items():
        if re.search(rf"\b{re.escape(key)}\b", lowered) and len(key) > len(best_key):
            best_key = key
            best_abbr = abbr
    return best_abbr, best_key
def extract_year(text: str) -> str:
    m = YEAR_RE.search(text)
    return "" if m is None else m.group(1)
def looks_like_acceptance(text: str) -> bool:
    if ACCEPTANCE_HINT_RE.search(text.lower()):
        return True
    venue_abbr, _ = map_venue(text)
    return bool(venue_abbr and extract_year(text))
def fallback_venue_abbr(text: str) -> str:
    raw = clean_text(text)
    if not raw:
        return ""
    m = PARENS_ABBR_RE.search(raw)
    if m:
        return m.group(1).upper()
    upper_tokens = re.findall(r"\b[A-Z][A-Z0-9]{1,15}\b", raw)
    if upper_tokens:
        return upper_tokens[0]
    words = re.findall(r"[A-Za-z0-9]+", raw)
    if not words:
        return ""
    return words[0].upper() if len(words) == 1 else "".join(word[0] for word in words[:8]).upper()
def normalize_workshop_name(workshop_name: str, venue_abbr: str) -> str:
    name = clean_text(workshop_name.strip(" \"'()[]{}:;,-"))
    if not name:
        return ""
    name = re.sub(
        r"^(?:accepted(?:\s+for\s+publication)?\s*(?:to|at|in|@|by)|to\s+appear(?:\s+in)?|published(?:\s+in)?)\s+",
        "",
        name,
        flags=re.IGNORECASE,
    )
    name = re.sub(r"\bworkshops?\b.*$", "", name, flags=re.IGNORECASE).strip()
    if venue_abbr:
        name = re.sub(rf"^{re.escape(venue_abbr)}\s+", "", name, flags=re.IGNORECASE)
    name = re.sub(r"^\d{4}\s+", "", name)
    name = re.sub(r"\s+\d{4}$", "", name)
    return clean_text(name.strip(" \"'()[]{}:;,-"))
def extract_workshop_name(text: str, venue_abbr: str) -> str:
    cleaned = clean_text(text)
    if not cleaned or not WORKSHOP_WORD_RE.search(cleaned):
        return ""
    after = WORKSHOP_NAME_AFTER_RE.search(cleaned)
    if after:
        candidate = normalize_workshop_name(after.group(1), venue_abbr)
        if candidate:
            return candidate
    for match in reversed(list(WORKSHOP_NAME_BEFORE_RE.finditer(cleaned))):
        candidate = normalize_workshop_name(match.group(1), venue_abbr)
        if candidate:
            return candidate
    return ""
def format_note(venue_abbr: str, year: str, workshop_name: str = "") -> str:
    if workshop_name:
        return f"\U0001f3c6 Accepted to {venue_abbr} {year} {workshop_name} Workshop"
    return f"\U0001f3c6 Accepted to {venue_abbr} {year}"
def build_decision(source: str, evidence_text: str, venue_raw: str, venue_abbr: str, year: str, workshop_name: str = "") -> AcceptanceDecision:
    reasons: list[str] = []
    if not venue_abbr:
        reasons.append("venue_unmapped")
    if not year:
        reasons.append("year_missing")
    note_venue = venue_abbr
    if not note_venue:
        note_venue = fallback_venue_abbr(venue_raw)
        if note_venue:
            reasons.append("venue_fallback")
    note = format_note(note_venue, year, workshop_name) if note_venue and year else ""
    return AcceptanceDecision(source, evidence_text, venue_raw, venue_abbr, year, note, bool(reasons), reasons)
def parse_comment_acceptance(comment: str) -> AcceptanceDecision | None:
    text = clean_text(comment)
    if not text:
        return None
    if COMMENT_SKIP_ACCEPTANCE_RE.search(text):
        return None
    if not looks_like_acceptance(text):
        return None
    has_workshop = bool(WORKSHOP_WORD_RE.search(text))
    candidates: list[tuple[str, str]] = []
    accepted_match = COMMENT_ACCEPTED_RE.search(text)
    if accepted_match:
        candidates.append((clean_text(accepted_match.group(1)), accepted_match.group(2)))
    for match in COMMENT_VENUE_YEAR_RE.finditer(text):
        venue_raw = clean_text(match.group(1))
        if venue_raw:
            candidates.append((venue_raw, match.group(2)))
        if len(candidates) >= 5:
            break
    for venue_raw, year in candidates:
        venue_abbr, _ = map_venue(venue_raw)
        if venue_abbr and year:
            workshop_name = ""
            if has_workshop:
                workshop_name = extract_workshop_name(venue_raw, venue_abbr) or extract_workshop_name(text, venue_abbr)
            return build_decision("comment", text, venue_raw, venue_abbr, year, workshop_name)
    if candidates:
        venue_raw, year = candidates[0]
        venue_abbr, _ = map_venue(venue_raw)
        workshop_name = ""
        if has_workshop:
            workshop_name = extract_workshop_name(venue_raw, venue_abbr) or extract_workshop_name(text, venue_abbr)
        return build_decision("comment", text, venue_raw, venue_abbr, year, workshop_name)
    venue_abbr, _ = map_venue(text)
    workshop_name = extract_workshop_name(text, venue_abbr) if has_workshop else ""
    return build_decision("comment", text, text, venue_abbr, extract_year(text), workshop_name)
def parse_journal_ref_acceptance(journal_ref: str) -> AcceptanceDecision | None:
    text = clean_text(journal_ref)
    if not text:
        return None
    venue_abbr, _ = map_venue(text)
    if not venue_abbr and not looks_like_acceptance(text):
        return None
    workshop_name = extract_workshop_name(text, venue_abbr) if WORKSHOP_WORD_RE.search(text) else ""
    return build_decision("journal_ref", text, text, venue_abbr, extract_year(text), workshop_name)
def parse_acceptance_decision(evidence_arxiv: dict[str, Any]) -> AcceptanceDecision | None:
    comment = clean_text(str(evidence_arxiv.get("comment", "")))
    journal_ref = clean_text(str(evidence_arxiv.get("journal_ref", "")))
    decision: AcceptanceDecision | None = None
    if comment:
        decision = parse_comment_acceptance(comment)
    if decision is None and journal_ref:
        decision = parse_journal_ref_acceptance(journal_ref)
    return decision
def extract_existing_code_url(link_value: str) -> str:
    m = CODE_URL_RE.search(link_value)
    return "" if m is None else (m.group(1) or m.group(2) or "").strip()
def normalize_code_hit(hit: dict[str, Any]) -> dict[str, Any]:
    return {
        "url": clean_text(str(hit.get("url", ""))),
        "source": clean_text(str(hit.get("source", ""))),
        "confidence": to_int(hit.get("confidence", 0), 0),
        "repo": clean_text(str(hit.get("repo", ""))),
    }
def select_best_code_hit(code_hits: list[dict[str, Any]]) -> dict[str, Any] | None:
    candidates = [item for item in (normalize_code_hit(hit) for hit in code_hits) if item["url"]]
    if not candidates:
        return None
    candidates.sort(key=lambda item: (-item["confidence"], DISCOVERY_SOURCE_ORDER.get(str(item["source"]), 99), str(item["url"])))
    return candidates[0]
def make_patch_spec(
    field: str,
    line_index: int | None,
    old_value: str,
    already_filled: bool,
    new_value: str,
    set_value: Callable[[int, str], None],
    evidence_source: str,
    confidence: int | None,
    suspicious: bool,
    reasons: list[str],
    evidence_text: str,
    proposal: str,
    print_old: str,
    print_new: str,
    write_old: str,
    write_new: str,
    skip_old: str,
    skip_new: str,
) -> dict[str, Any]:
    return {
        "field": field,
        "line_index": line_index,
        "old_value": old_value,
        "already_filled": already_filled,
        "new_value": new_value,
        "set_value": set_value,
        "evidence_source": evidence_source,
        "confidence": confidence,
        "suspicious": suspicious,
        "reasons": reasons,
        "evidence_text": evidence_text,
        "proposal": proposal,
        "print_old": print_old,
        "print_new": print_new,
        "write_old": write_old,
        "write_new": write_new,
        "skip_old": skip_old,
        "skip_new": skip_new,
    }
def ask_confirmation(ctx: EntryContext, spec: dict[str, Any]) -> str:
    print("")
    print(f"[suspicious][{spec['field']}] {ctx.title}")
    print(f"- arXiv: {ctx.arxiv_id}")
    print(f"- target: {ctx.source_file}#{ctx.entry_index}")
    reasons = spec["reasons"]
    print(f"- reasons: {', '.join(reasons) if reasons else 'n/a'}")
    evidence_text = spec["evidence_text"]
    print(f"- evidence: {evidence_text or '(empty)'}")
    proposal = spec["proposal"]
    print(f"- parsed: {proposal or '(unable to parse a writable value)'}")
    while True:
        try:
            answer = input("Apply this change? [y/s/q] ").strip().lower()
        except EOFError:
            return "q"
        if answer in {"y", "s", "q"}:
            return answer
        if answer == "":
            return "s"
        print("Please input y / s / q.")
def append_record(records: list[dict[str, Any]], ctx: EntryContext, spec: dict[str, Any], old_value: str, new_value: str, action: str) -> None:
    records.append(
        {
            "arxiv_id": ctx.arxiv_id,
            "file": ctx.source_file,
            "entry_index": ctx.entry_index,
            "field": spec["field"],
            "old_value": old_value,
            "new_value": new_value,
            "evidence_source": spec["evidence_source"],
            "confidence": spec["confidence"],
            "action": action,
            "timestamp": utc_now_iso(),
        }
    )
def add_event(summary: dict[str, dict[str, int]], records: list[dict[str, Any]], ctx: EntryContext, spec: dict[str, Any], action: str, old_value: str, new_value: str) -> None:
    summary[spec["field"]][action] += 1
    append_record(records, ctx, spec, old_value, new_value, action)
def decide_write(args: argparse.Namespace, interactive_quit: bool, ctx: EntryContext, spec: dict[str, Any]) -> tuple[bool, str, bool]:
    if not spec["suspicious"]:
        return True, "auto_written", interactive_quit
    if args.yes:
        return True, "auto_written", interactive_quit
    if interactive_quit:
        return False, "skipped", interactive_quit
    answer = ask_confirmation(ctx, spec)
    if answer == "y":
        return True, "confirmed_written", interactive_quit
    if answer == "q":
        return False, "skipped", True
    return False, "skipped", interactive_quit
def print_change(args: argparse.Namespace, ctx: EntryContext, spec: dict[str, Any], action: str) -> None:
    prefix = "[DRY-RUN] " if args.dry_run else ""
    print(f"{prefix}{spec['field']}:{action} {ctx.source_file}#{ctx.entry_index} old={spec['print_old']!r} new={spec['print_new']!r}")
def _apply_patch(args: argparse.Namespace, ctx: EntryContext, spec: dict[str, Any], summary: dict[str, dict[str, int]], records: list[dict[str, Any]], interactive_quit: bool) -> bool:
    if spec["line_index"] is None:
        add_event(summary, records, ctx, spec, "skipped", spec["skip_old"], spec["skip_new"])
        return interactive_quit
    if spec["already_filled"]:
        old = spec["old_value"]
        add_event(summary, records, ctx, spec, "already_filled", old, old)
        return interactive_quit
    should_write, action, interactive_quit = decide_write(args, interactive_quit, ctx, spec)
    if should_write and not spec["new_value"]:
        should_write = False
        action = "skipped"
    if not should_write:
        add_event(summary, records, ctx, spec, "skipped", spec["skip_old"], spec["skip_new"])
        return interactive_quit
    spec["set_value"](spec["line_index"], spec["new_value"])
    print_change(args, ctx, spec, action)
    add_event(summary, records, ctx, spec, action, spec["write_old"], spec["write_new"])
    return interactive_quit
def load_editor(editors: dict[Path, MarkdownEditor], source_file: str) -> MarkdownEditor:
    path = Path(source_file)
    resolved = path if path.is_absolute() else Path.cwd() / path
    if resolved in editors:
        return editors[resolved]
    if not resolved.exists():
        raise FileNotFoundError(f"File not found for source_file={source_file!r}")
    editors[resolved] = MarkdownEditor(resolved)
    return editors[resolved]
def build_entry_context(result: dict[str, Any], entry: dict[str, Any]) -> EntryContext | None:
    source_file = clean_text(str(entry.get("source_file", "")))
    if not source_file:
        return None
    entry_index = to_int(entry.get("entry_index"), -1)
    if entry_index < 0:
        return None
    title = clean_text(str(entry.get("title", ""))) or clean_text(str(result.get("title", "")))
    arxiv_id = clean_text(str(result.get("arxiv_id", "")))
    return EntryContext(arxiv_id=arxiv_id, title=title, source_file=source_file, entry_index=entry_index)
def process_acceptance(args: argparse.Namespace, ctx: EntryContext, editor: MarkdownEditor, decision: AcceptanceDecision | None, summary: dict[str, dict[str, int]], records: list[dict[str, Any]], interactive_quit: bool) -> bool:
    if decision is None:
        return interactive_quit
    line_index, old_note = editor.get_note(ctx.entry_index)
    spec = make_patch_spec(
        "acceptance", line_index, old_note, bool(old_note and old_note != "---"), decision.note, editor.set_note,
        decision.source, None, decision.suspicious, decision.reasons, decision.evidence_text, decision.note,
        old_note, decision.note, old_note, decision.note, old_note if line_index is not None else "", old_note if line_index is not None else "",
    )
    return _apply_patch(args, ctx, spec, summary, records, interactive_quit)
def build_code_patch_spec(ctx: EntryContext, editor: MarkdownEditor, best_hit: dict[str, Any]) -> dict[str, Any]:
    source = str(best_hit.get("source", ""))
    confidence = to_int(best_hit.get("confidence", 0), 0)
    line_index, link_value = editor.get_link(ctx.entry_index)
    if line_index is None:
        return make_patch_spec("code", None, "", False, "", editor.set_link, source, confidence, False, [], "", "", "", "", "", "", "", "")
    old_code_url = extract_existing_code_url(link_value)
    new_url = clean_text(str(best_hit.get("url", "")))
    new_link_value, replace_count = PLAIN_CODE_RE.subn(f"[[Code]({new_url})]", link_value, count=1)
    new_value = new_link_value if replace_count else ""
    skip_value = "" if replace_count else link_value.strip()
    suspicious = confidence == 1
    reasons = ["confidence=1(github_search_only)"] if suspicious else []
    return make_patch_spec(
        "code", line_index, old_code_url, bool(old_code_url), new_value, editor.set_link,
        source, confidence, suspicious, reasons, f"{best_hit.get('source', '')}: {new_url}", f"[[Code]({new_url})]",
        "[Code]", new_url, "", new_url, skip_value, skip_value,
    )
def process_code(args: argparse.Namespace, ctx: EntryContext, editor: MarkdownEditor, best_hit: dict[str, Any] | None, summary: dict[str, dict[str, int]], records: list[dict[str, Any]], interactive_quit: bool) -> bool:
    if best_hit is None:
        return interactive_quit
    spec = build_code_patch_spec(ctx, editor, best_hit)
    return _apply_patch(args, ctx, spec, summary, records, interactive_quit)
def extract_result_inputs(args: argparse.Namespace, result: dict[str, Any]) -> tuple[AcceptanceDecision | None, dict[str, Any] | None, list[dict[str, Any]]]:
    evidence = result.get("evidence", {})
    evidence = evidence if isinstance(evidence, dict) else {}
    evidence_arxiv = evidence.get("arxiv", {})
    evidence_arxiv = evidence_arxiv if isinstance(evidence_arxiv, dict) else {}
    acceptance = None if args.no_acceptance else parse_acceptance_decision(evidence_arxiv)
    code_hits = evidence.get("code_discovery", [])
    code_hits = code_hits if isinstance(code_hits, list) else []
    best_code_hit = None if args.no_code else select_best_code_hit(code_hits)
    entries = result.get("entries", [])
    entries = entries if isinstance(entries, list) else []
    return acceptance, best_code_hit, [entry for entry in entries if isinstance(entry, dict)]
def process_entry(args: argparse.Namespace, ctx: EntryContext, editor: MarkdownEditor, acceptance: AcceptanceDecision | None, best_code_hit: dict[str, Any] | None, summary: dict[str, dict[str, int]], records: list[dict[str, Any]], interactive_quit: bool) -> bool:
    if not args.no_acceptance:
        interactive_quit = process_acceptance(args, ctx, editor, acceptance, summary, records, interactive_quit)
    if not args.no_code:
        interactive_quit = process_code(args, ctx, editor, best_code_hit, summary, records, interactive_quit)
    return interactive_quit
def process_results(args: argparse.Namespace, results: list[dict[str, Any]]) -> tuple[dict[Path, MarkdownEditor], list[dict[str, Any]], dict[str, dict[str, int]]]:
    editors: dict[Path, MarkdownEditor] = {}
    records: list[dict[str, Any]] = []
    summary: dict[str, dict[str, int]] = {"acceptance": defaultdict(int), "code": defaultdict(int)}
    interactive_quit = False
    for result in results:
        acceptance, best_code_hit, entries = extract_result_inputs(args, result)
        contexts = [ctx for ctx in (build_entry_context(result, entry) for entry in entries) if ctx is not None]
        for ctx in contexts:
            editor = load_editor(editors, ctx.source_file)
            interactive_quit = process_entry(args, ctx, editor, acceptance, best_code_hit, summary, records, interactive_quit)
    return editors, records, summary
def print_summary(summary: dict[str, dict[str, int]]) -> None:
    actions = ("auto_written", "confirmed_written", "skipped", "already_filled")
    print("\nSummary:")
    for field in ("acceptance", "code"):
        counts = summary[field]
        joined = " / ".join(f"{action}={counts.get(action, 0)}" for action in actions)
        print(f"- {field}: {joined}")
def finalize(args: argparse.Namespace, editors: dict[Path, MarkdownEditor], records: list[dict[str, Any]], summary: dict[str, dict[str, int]]) -> int:
    if args.dry_run:
        print("\nDry run complete: no markdown files modified, no evidence JSON written.")
        print_summary(summary)
        return 0
    for editor in editors.values():
        editor.save()
    evidence_path = Path("tmp") / f"patch-evidence-{file_timestamp_now()}.json"
    evidence_path.parent.mkdir(parents=True, exist_ok=True)
    payload = {"generated_at": utc_now_iso(), "input": args.input.as_posix(), "records": records}
    evidence_path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n", encoding="utf-8")
    print(f"\nEvidence written: {evidence_path.as_posix()}")
    print_summary(summary)
    return 0
def main() -> int:
    args = parse_args()
    payload = json.loads(args.input.read_text(encoding="utf-8"))
    results = payload.get("results")
    if not isinstance(results, list):
        raise SystemExit("Invalid input JSON: missing top-level list field 'results'.")
    typed_results = [result for result in results if isinstance(result, dict)]
    editors, records, summary = process_results(args, typed_results)
    return finalize(args, editors, records, summary)
if __name__ == "__main__":
    try:
        raise SystemExit(main())
    except FileNotFoundError as exc:
        print(f"Error: {exc}", file=sys.stderr)
        raise SystemExit(1)
