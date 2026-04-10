#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import os
import re
import shutil
import subprocess
import sys
import time
from dataclasses import dataclass
from datetime import datetime, timezone
from pathlib import Path
from typing import Any

from sync import ENTRY_SPLIT_RE, renumber_entries


ARXIV_ID_RE = re.compile(r"^\d{4}\.\d{5}$")
CODEX_TOKENS_RE = re.compile(r"tokens used\s*\n\s*([\d,]+)", re.I)
ARXIV_LINK_RE = re.compile(r"\[\[arXiv:([0-9]{4}\.[0-9]{5})\]")
THINK_RE = re.compile(r"<think>.*?</think>", re.I | re.S)
CODE_FENCE_RE = re.compile(r"```(?:json)?\s*([\s\S]*?)```", re.I)
REPORT_PATH = Path("tmp/curate_report.json")


PROMPT_TEMPLATE = """Given this academic paper:
Title: {title}
Abstract: {abstract}
Author/affiliation block: {affiliation_text}

Return JSON:
{{
  "noise_sentences": ["exact sentence to remove", ...],
  "abstract_zh": "中文摘要翻译",
  "affiliations": ["Institution A", "Institution B"]
}}

Rules:
- noise_sentences: list sentences from the abstract that are NOT scientific content, such as:
  "Code will be released.", "Our project page is at https://...", "Models are available at ...",
  "See our website at ...", or similar self-promotional/availability/meta sentences.
  Copy them VERBATIM from the abstract. Return [] if none found.
- abstract_zh: translate the abstract to Chinese, excluding the noise_sentences; rewrite LaTeX symbols as plain text
- affiliations: extract institution names in order of appearance, deduplicate;
  omit cities, countries, emails, department sub-units unless they are the top-level org;
  return [] if affiliation_text is empty or unparseable
"""


@dataclass(frozen=True)
class DiffEntry:
    arxiv_id: str
    title: str
    authors: list[str]
    abstract: str
    submitted: str


@dataclass(frozen=True)
class DownloadEntry:
    arxiv_id: str
    affiliation_text: str
    affiliation_source: str
    note: str
    code_url: str


@dataclass(frozen=True)
class AIResponse:
    ok: bool
    model: str
    noise_sentences: list[str]
    abstract_zh: str
    affiliations: list[str]
    error: str
    elapsed_s: float = 0.0
    tokens: int | None = None


@dataclass(frozen=True)
class CurateItem:
    arxiv_id: str
    title: str
    authors: list[str]
    abstract: str       # original (may contain noise)
    abstract_en: str    # noise-removed English abstract (verbatim except deleted sentences)
    abstract_zh: str
    affiliations: list[str]
    affiliation_source: str
    affiliation_status: str
    note: str
    code_url: str
    ai_model: str
    ai_error: str
    ai_elapsed_s: float
    ai_tokens: int | None


@dataclass(frozen=True)
class ReadmeEntry:
    arxiv_id: str
    raw: str


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Curate new papers with AI and write README + abs artifacts."
    )
    parser.add_argument(
        "--diff",
        type=Path,
        default=Path("tmp/diff.json"),
        help="Diff JSON path (default: tmp/diff.json).",
    )
    parser.add_argument(
        "--download",
        type=Path,
        default=Path("tmp/download.json"),
        help="Download JSON path (default: tmp/download.json).",
    )
    parser.add_argument(
        "--readme",
        type=Path,
        default=Path("README.md"),
        help="README path (default: README.md).",
    )
    parser.add_argument(
        "--abs-dir",
        type=Path,
        default=Path("abs"),
        help="abs directory path (default: abs).",
    )
    parser.add_argument(
        "--cache",
        type=Path,
        default=Path("tmp/curate_cache.json"),
        help="Curate cache path (default: tmp/curate_cache.json).",
    )
    parser.add_argument(
        "--dry-run",
        action="store_true",
        help="Print results only; do not write README/abs/cache/report files.",
    )
    return parser.parse_args()


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def normalize_text(value: object) -> str:
    if not isinstance(value, str):
        return ""
    return value.strip()


def normalize_authors(raw: object) -> list[str]:
    if not isinstance(raw, list):
        return []
    authors: list[str] = []
    for item in raw:
        if not isinstance(item, str):
            continue
        cleaned = item.strip()
        if cleaned:
            authors.append(cleaned)
    return authors


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
        arxiv_id = normalize_text(item.get("arxiv_id"))
        if not ARXIV_ID_RE.fullmatch(arxiv_id):
            continue
        entries.append(
            DiffEntry(
                arxiv_id=arxiv_id,
                title=normalize_text(item.get("title")),
                authors=normalize_authors(item.get("authors")),
                abstract=normalize_text(item.get("abstract")),
                submitted=normalize_text(item.get("submitted")),
            )
        )
    return entries


def default_download(arxiv_id: str) -> DownloadEntry:
    return DownloadEntry(
        arxiv_id=arxiv_id,
        affiliation_text="",
        affiliation_source="none",
        note="",
        code_url="",
    )


def load_download_entries(path: Path) -> dict[str, DownloadEntry]:
    payload = json.loads(path.read_text())
    if isinstance(payload, list):
        raw_items = payload
    elif isinstance(payload, dict):
        raw_items = payload.get("results")
    else:
        raise ValueError("Download payload must be a JSON object or list.")
    if not isinstance(raw_items, list):
        raise ValueError("Download payload must contain a list field: results")

    entries: dict[str, DownloadEntry] = {}
    for item in raw_items:
        if not isinstance(item, dict):
            continue
        arxiv_id = normalize_text(item.get("arxiv_id"))
        if not ARXIV_ID_RE.fullmatch(arxiv_id):
            continue
        entries[arxiv_id] = DownloadEntry(
            arxiv_id=arxiv_id,
            affiliation_text=normalize_text(item.get("affiliation_text")),
            affiliation_source=normalize_text(item.get("affiliation_source")) or "none",
            note=normalize_text(item.get("note")),
            code_url=normalize_text(item.get("code_url")),
        )
    return entries


def load_cache(path: Path) -> dict[str, dict[str, Any]]:
    if not path.exists():
        return {}
    try:
        payload = json.loads(path.read_text())
    except json.JSONDecodeError:
        return {}
    if not isinstance(payload, dict):
        return {}
    processed = payload.get("processed")
    if not isinstance(processed, dict):
        return {}
    normalized: dict[str, dict[str, Any]] = {}
    for arxiv_id, item in processed.items():
        if not isinstance(arxiv_id, str) or not ARXIV_ID_RE.fullmatch(arxiv_id):
            continue
        if isinstance(item, dict):
            normalized[arxiv_id] = item
        else:
            normalized[arxiv_id] = {}
    return normalized


def save_cache(path: Path, processed: dict[str, dict[str, Any]]) -> None:
    payload = {
        "updated_at": utc_now_iso(),
        "processed": processed,
    }
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def clean_ai_output(text: str) -> str:
    cleaned = THINK_RE.sub("", text or "")
    return "\n".join(line for line in cleaned.splitlines() if line.strip()).strip()


def iter_json_candidates(text: str) -> list[str]:
    candidates: list[str] = []
    seen: set[str] = set()

    def add(candidate: str) -> None:
        snippet = candidate.strip()
        if not snippet or snippet in seen:
            return
        seen.add(snippet)
        candidates.append(snippet)

    for block in CODE_FENCE_RE.findall(text):
        add(block)

    add(text)

    first = text.find("{")
    last = text.rfind("}")
    if first != -1 and last != -1 and first < last:
        add(text[first : last + 1])

    for start in (index for index, char in enumerate(text) if char == "{"):
        depth = 0
        in_string = False
        escaped = False
        for end in range(start, len(text)):
            char = text[end]
            if in_string:
                if escaped:
                    escaped = False
                elif char == "\\":
                    escaped = True
                elif char == '"':
                    in_string = False
                continue
            if char == '"':
                in_string = True
                continue
            if char == "{":
                depth += 1
            elif char == "}":
                depth -= 1
                if depth == 0:
                    add(text[start : end + 1])
                    break
            if depth < 0:
                break
    return candidates


def parse_ai_json(text: str) -> dict[str, Any] | None:
    for candidate in iter_json_candidates(text):
        try:
            parsed = json.loads(candidate)
        except json.JSONDecodeError:
            continue
        if isinstance(parsed, dict):
            return parsed
    return None


def normalize_affiliations(raw: object) -> list[str]:
    if not isinstance(raw, list):
        return []
    affiliations: list[str] = []
    seen: set[str] = set()
    for item in raw:
        if not isinstance(item, str):
            continue
        cleaned = " ".join(item.split()).strip(" ,;")
        if not cleaned:
            continue
        key = cleaned.lower()
        if key in seen:
            continue
        seen.add(key)
        affiliations.append(cleaned)
    return affiliations


def normalize_ai_payload(parsed: dict[str, Any]) -> tuple[list[str], str, list[str]]:
    noise_sentences = [
        s.strip()
        for s in parsed.get("noise_sentences", [])
        if isinstance(s, str) and s.strip()
    ]
    abstract_zh = normalize_text(parsed.get("abstract_zh"))
    affiliations = normalize_affiliations(parsed.get("affiliations"))
    return noise_sentences, abstract_zh, affiliations


def remove_noise(abstract: str, noise_sentences: list[str]) -> str:
    """Remove noise sentences verbatim from abstract, preserving all other content."""
    result = abstract
    for sentence in noise_sentences:
        result = result.replace(sentence, "")
    return re.sub(r"[ \t]{2,}", " ", result).strip()


def run_model(command: list[str], prompt: str, env_overrides: dict[str, str] | None = None, timeout: int | None = None) -> tuple[str, str]:
    env = None if env_overrides is None else {**os.environ, **env_overrides}
    process = subprocess.run(
        command,
        input=prompt,
        capture_output=True,
        text=True,
        check=False,
        env=env,
        timeout=timeout,
    )
    return process.stdout or "", process.stderr or ""


def run_ai(prompt: str) -> AIResponse:
    # Attempt order: aichat → codex → claude (haiku)
    # claude needs --tools "" to prevent AGENTS.md from hijacking the subprocess
    # via dotai preflight startup (which hangs in a non-TTY subprocess).
    attempts: list[tuple[str, list[str], dict[str, str] | None, int | None]] = []
    if shutil.which("aichat"):
        attempts.append(("aichat", ["aichat", "--no-stream"], None, None))
    if shutil.which("codex"):
        attempts.append(("codex", ["codex", "exec", "--full-auto", "-C", "/tmp", "--skip-git-repo-check"], None, None))
    if shutil.which("haiku") or shutil.which("claude"):
        attempts.append((
            "haiku",
            [
                "claude", "-p", "--model", "haiku",
                "--tools", "",
                "--no-session-persistence",
                "--dangerously-skip-permissions",
            ],
            None,
            None,
        ))

    if not attempts:
        return AIResponse(
            ok=False,
            model="",
            noise_sentences=[],
            abstract_zh="",
            affiliations=[],
            error="No available AI CLI found (aichat/codex/claude).",
        )

    errors: list[str] = []
    for model, command, env_overrides, timeout in attempts:
        t0 = time.perf_counter()
        try:
            stdout, stderr = run_model(command, prompt, env_overrides=env_overrides, timeout=timeout)
        except subprocess.TimeoutExpired:
            errors.append(f"{model}: timed out after {timeout}s")
            continue
        except OSError as exc:
            errors.append(f"{model}: {exc}")
            continue
        elapsed = time.perf_counter() - t0
        tokens: int | None = None
        m = CODEX_TOKENS_RE.search(stdout)
        if m:
            tokens = int(m.group(1).replace(",", ""))
        cleaned = clean_ai_output(stdout)
        if not cleaned:
            stderr_hint = stderr.strip().splitlines()[-1] if stderr.strip() else "empty output"
            errors.append(f"{model}: {stderr_hint}")
            continue
        parsed = parse_ai_json(cleaned)
        if parsed is None:
            errors.append(f"{model}: invalid JSON output")
            continue
        noise_sentences, abstract_zh, affiliations = normalize_ai_payload(parsed)
        if not abstract_zh:
            errors.append(f"{model}: missing abstract_zh")
            continue
        return AIResponse(
            ok=True,
            model=model,
            noise_sentences=noise_sentences,
            abstract_zh=abstract_zh,
            affiliations=affiliations,
            error="",
            elapsed_s=round(elapsed, 1),
            tokens=tokens,
        )

    return AIResponse(
        ok=False,
        model="",
        noise_sentences=[],
        abstract_zh="",
        affiliations=[],
        error="; ".join(errors) if errors else "AI call failed",
    )


def build_prompt(diff_entry: DiffEntry, download_entry: DownloadEntry) -> str:
    affiliation_text = download_entry.affiliation_text.strip()
    if len(affiliation_text) > 8000:
        affiliation_text = affiliation_text[:8000].rstrip()
    return PROMPT_TEMPLATE.format(
        title=diff_entry.title,
        abstract=diff_entry.abstract,
        affiliation_text=affiliation_text,
    )


def parse_readme_entries(text: str) -> tuple[str, list[ReadmeEntry]]:
    parts = ENTRY_SPLIT_RE.split(text)
    prefix = parts[0]
    entries: list[ReadmeEntry] = []
    for index in range(1, len(parts), 2):
        number = parts[index]
        block = parts[index + 1].rstrip()
        raw = f"#### [{number}] {block}".rstrip()
        match = ARXIV_LINK_RE.search(raw)
        arxiv_id = match.group(1) if match else ""
        entries.append(ReadmeEntry(arxiv_id=arxiv_id, raw=raw))
    return prefix, entries


def find_insert_index(entries: list[ReadmeEntry], arxiv_id: str) -> int:
    for index, entry in enumerate(entries):
        if not entry.arxiv_id:
            continue
        if arxiv_id > entry.arxiv_id:
            return index
    return len(entries)


def render_readme(prefix: str, entries: list[ReadmeEntry]) -> str:
    if not entries:
        return prefix.rstrip("\n") + "\n"
    rendered_entries = "\n\n".join(entry.raw.rstrip() for entry in entries).rstrip()
    combined = prefix.rstrip("\n") + "\n\n" + rendered_entries + "\n"
    return renumber_entries(combined)


def render_code_link(code_url: str) -> str:
    if not code_url:
        return "[Code]"
    return f"[[Code]({code_url})]"


def render_readme_entry(item: CurateItem) -> str:
    authors_text = ", ".join(item.authors)
    affiliations_text = " ⟐ ".join(item.affiliations)
    note_suffix = f" {item.note}" if item.note else ""
    return (
        f"#### [0] {item.title}\n"
        f"- **🧑‍🔬 作者**：{authors_text}\n"
        f"- **🏫 单位**：{affiliations_text}\n"
        f"- **🔗 链接**：[[中英摘要](./abs/{item.arxiv_id}.md)] "
        f"[[arXiv:{item.arxiv_id}](https://arxiv.org/abs/{item.arxiv_id})] "
        f"{render_code_link(item.code_url)}\n"
        f"- **📝 说明**:{note_suffix}"
    )


def render_abs_file(item: CurateItem) -> str:
    abstract_en = item.abstract_en or item.abstract
    return (
        f"### {item.title}\n\n"
        f"{abstract_en}\n\n"
        f"{item.abstract_zh}\n"
    )


def summarize_source(source: str) -> str:
    if source.startswith("html_"):
        return "html"
    return source or "none"


def determine_affiliation_status(affiliation_text: str, ai: AIResponse, affiliations: list[str]) -> str:
    if not affiliation_text.strip():
        return "empty_text"
    if not ai.ok:
        return "ai_failed"
    if not affiliations:
        return "ai_empty"
    return "ok"


def write_report(path: Path, payload: dict[str, Any]) -> None:
    path.parent.mkdir(parents=True, exist_ok=True)
    path.write_text(json.dumps(payload, ensure_ascii=False, indent=2) + "\n")


def main() -> None:
    args = parse_args()
    diff_entries = load_diff_entries(args.diff)
    download_entries = load_download_entries(args.download)
    cache_map = {} if args.dry_run else load_cache(args.cache)

    if not args.readme.exists():
        raise SystemExit(f"README not found: {args.readme}")
    readme_before = args.readme.read_text()
    readme_prefix, readme_entries = parse_readme_entries(readme_before)
    existing_readme_ids = {entry.arxiv_id for entry in readme_entries if entry.arxiv_id}

    total = len(diff_entries)
    curated_items: list[CurateItem] = []
    skipped_cached: list[str] = []
    for i, diff_entry in enumerate(diff_entries, 1):
        cache_hit = diff_entry.arxiv_id in cache_map
        abs_exists = (args.abs_dir / f"{diff_entry.arxiv_id}.md").exists()
        if cache_hit and diff_entry.arxiv_id in existing_readme_ids and abs_exists:
            skipped_cached.append(diff_entry.arxiv_id)
            continue

        print(f"[{i}/{total}] {diff_entry.arxiv_id}  {diff_entry.title[:55]}", flush=True)
        download_entry = download_entries.get(diff_entry.arxiv_id, default_download(diff_entry.arxiv_id))
        prompt = build_prompt(diff_entry, download_entry)
        ai_response = run_ai(prompt)
        affiliations = ai_response.affiliations if ai_response.ok else []
        abstract_en = remove_noise(diff_entry.abstract, ai_response.noise_sentences) if ai_response.ok else diff_entry.abstract
        abstract_zh = ai_response.abstract_zh if ai_response.ok else ""
        status = determine_affiliation_status(download_entry.affiliation_text, ai_response, affiliations)
        tokens_str = f"  tokens={ai_response.tokens}" if ai_response.tokens is not None else ""
        print(f"     → {ai_response.model or 'failed'}  affiliations={len(affiliations)}  noise={len(ai_response.noise_sentences)}  {ai_response.elapsed_s}s{tokens_str}", flush=True)

        curated_items.append(
            CurateItem(
                arxiv_id=diff_entry.arxiv_id,
                title=diff_entry.title,
                authors=diff_entry.authors,
                abstract=diff_entry.abstract,
                abstract_en=abstract_en,
                abstract_zh=abstract_zh,
                affiliations=affiliations,
                affiliation_source=download_entry.affiliation_source or "none",
                affiliation_status=status,
                note=download_entry.note,
                code_url=download_entry.code_url,
                ai_model=ai_response.model,
                ai_error=ai_response.error,
                ai_elapsed_s=ai_response.elapsed_s,
                ai_tokens=ai_response.tokens,
            )
        )

    inserted_ids: set[str] = set()
    for item in sorted(curated_items, key=lambda entry: entry.arxiv_id, reverse=True):
        if item.arxiv_id in existing_readme_ids:
            continue
        insert_index = find_insert_index(readme_entries, item.arxiv_id)
        readme_entries.insert(insert_index, ReadmeEntry(arxiv_id=item.arxiv_id, raw=render_readme_entry(item)))
        existing_readme_ids.add(item.arxiv_id)
        inserted_ids.add(item.arxiv_id)

    readme_after = render_readme(readme_prefix, readme_entries)
    readme_changed = readme_after != readme_before

    abs_updates: dict[str, str] = {
        item.arxiv_id: render_abs_file(item)
        for item in curated_items
    }

    if not args.dry_run:
        if readme_changed:
            args.readme.write_text(readme_after)
        args.abs_dir.mkdir(parents=True, exist_ok=True)
        for arxiv_id, content in abs_updates.items():
            (args.abs_dir / f"{arxiv_id}.md").write_text(content)

        for item in curated_items:
            cache_map[item.arxiv_id] = {
                "updated_at": utc_now_iso(),
                "affiliation_status": item.affiliation_status,
                "affiliation_source": item.affiliation_source,
                "ai_model": item.ai_model,
            }
        save_cache(args.cache, cache_map)

    manual_items = [item for item in curated_items if item.affiliation_status != "ok"]
    report_items = []
    for item in curated_items:
        report_items.append(
            {
                "arxiv_id": item.arxiv_id,
                "title": item.title,
                "affiliation_source": item.affiliation_source,
                "affiliation_status": item.affiliation_status,
                "ai_model": item.ai_model,
                "ai_error": item.ai_error,
                "ai_elapsed_s": item.ai_elapsed_s,
                "ai_tokens": item.ai_tokens,
                "readme_inserted": item.arxiv_id in inserted_ids,
                "abs_written": True,
            }
        )
    report_payload: dict[str, Any] = {
        "generated_at": utc_now_iso(),
        "diff": str(args.diff),
        "download": str(args.download),
        "dry_run": args.dry_run,
        "total_candidates": len(diff_entries),
        "processed": len(curated_items),
        "skipped_cached": len(skipped_cached),
        "manual_affiliation_count": len(manual_items),
        "items": report_items,
    }
    if not args.dry_run:
        write_report(REPORT_PATH, report_payload)

    print(f"\n✓ {len(curated_items)} papers curated")
    if skipped_cached:
        print(f"↷ {len(skipped_cached)} papers skipped from cache")
    if manual_items:
        print(f"⚠ {len(manual_items)} papers need manual affiliation:")
        for item in manual_items:
            source = summarize_source(item.affiliation_source)
            if item.affiliation_status == "empty_text" and source == "none":
                reason = "(HTML/PDF both failed)"
            else:
                reason = item.affiliation_status
            print(f"  - {item.arxiv_id}  source={source}    {reason}")

    if args.dry_run:
        print("→ dry-run: no files written")
    else:
        print(f"→ report: {REPORT_PATH}")


if __name__ == "__main__":
    try:
        main()
    except (json.JSONDecodeError, ValueError) as exc:
        print(f"Failed to curate papers: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
