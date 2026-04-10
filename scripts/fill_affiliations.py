#!/usr/bin/env python3

import argparse
import concurrent.futures
import re
import subprocess
import sys
import urllib.error
import urllib.request
from pathlib import Path

from bs4 import BeautifulSoup


README_PATH = Path("README.md")
CACHE_DIR = Path("/tmp/arxiv_affiliation_cache")
ENTRY_RE = re.compile(r"(?ms)^#### \[(?P<num>\d+)\] (?P<title>.+?)\n(?P<body>.*?)(?=^#### \[\d+\] .+$|\Z)")
ARXIV_RE = re.compile(r"arXiv:(\d+\.\d+)")
UNIT_LINE_RE = re.compile(r"^- \*\*🏫 单位\*\*：(.*)$", re.M)

KNOWN_COMPANIES = {
    "A*STAR",
    "Adobe",
    "Adobe Research",
    "Alibaba",
    "Amazon",
    "Apple",
    "BAAI",
    "Baidu",
    "Bosch",
    "ByteDance",
    "DeepMind",
    "ETH Zurich",
    "EPFL",
    "Google",
    "Google Research",
    "GigaAI",
    "Hugging Face",
    "Huawei",
    "KAIST",
    "Meta",
    "Microsoft",
    "Microsoft Research",
    "NVIDIA",
    "NTU",
    "OpenAI",
    "SenseTime",
    "Shanghai AI Laboratory",
    "Siemens",
    "Siemens Digital Industries Software",
    "Tencent",
    "Tencent AI Lab",
    "THU",
    "UNIST",
    "Valeo Vision Systems",
    "VisualAIs",
    "Xiaomi",
    "Zenseact",
}

ORG_ALIASES = {
    "CUHK": "The Chinese University of Hong Kong",
    "ETH Zürich": "ETH Zurich",
    "GMU": "George Mason University",
    "HKUST": "The Hong Kong University of Science and Technology",
    "HKUST(GZ)": "The Hong Kong University of Science and Technology (Guangzhou)",
    "HUST": "Huazhong University of Science and Technology",
    "NUS": "National University of Singapore",
}

KEEP_SUBUNITS = {
    "A*STAR",
    "Google Research",
    "Microsoft Research",
    "Adobe Research",
    "Shanghai AI Laboratory",
    "Tencent AI Lab",
}

LOCATION_WORDS = {
    "beijing",
    "berkeley",
    "boston",
    "california",
    "canada",
    "china",
    "england",
    "france",
    "germany",
    "guangzhou",
    "hong kong",
    "hong kong sar",
    "india",
    "japan",
    "korea",
    "kowloon",
    "london",
    "paris",
    "singapore",
    "shanghai",
    "shenzhen",
    "tokyo",
    "toronto",
    "uk",
    "united kingdom",
    "united states",
    "usa",
    "wuhan",
}

ORG_WORDS = (
    "academy",
    "center",
    "centre",
    "college",
    "corporation",
    "hospital",
    "institute",
    "laboratory",
    "laboratories",
    "lab",
    "labs",
    "research",
    "school",
    "software",
    "systems",
    "technology",
    "technologies",
    "university",
)

SKIP_PREFIXES = (
    "college of ",
    "department of ",
    "school of ",
    "faculty of ",
    "center for ",
    "centre for ",
    "state key ",
    "key laboratory",
    "key lab",
    "national key ",
    "institute of ",
    "laboratory of ",
)

HEADER_MARKERS = (
    "abstract",
    "introduction",
    "keywords",
    "index terms",
)

ORG_PATTERNS = (
    re.compile(
        r"\b((?:The )?[A-Z][\w&.\-']*(?: [A-Z][\w&.\-']*)* "
        r"(?:University|College|Institute|Academy|Hospital|Center|Centre|Laboratory|Laboratories|Research|Technology|Technologies|Software|Systems))\b"
    ),
    re.compile(
        r"\b((?:The )?(?:University|College|Institute|Academy|Hospital|Center|Centre|Laboratory|Laboratories|Research) "
        r"of [A-Z][\w&.\-']*(?: [A-Z][\w&.\-']*)*(?: [A-Z][\w&.\-']*)*)\b"
    ),
    re.compile(r"\b(ETH Zurich|EPFL|KAIST|UNIST|BAAI|THU|BUAA|NJU|ZJU|NTU|BNU|NVIDIA|Google|Microsoft|Meta|Adobe)\b"),
)


def parse_args():
    parser = argparse.ArgumentParser()
    parser.add_argument("--readme", default=str(README_PATH))
    parser.add_argument("--limit", type=int, default=135)
    parser.add_argument("--workers", type=int, default=4)
    parser.add_argument("--force", action="store_true")
    parser.add_argument("--write", action="store_true")
    return parser.parse_args()


def fetch_text(url: str, path: Path) -> str:
    if path.exists():
        return path.read_text(encoding="utf-8", errors="ignore")
    request = urllib.request.Request(url, headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=60) as response:
        data = response.read()
    path.write_bytes(data)
    return data.decode("utf-8", errors="ignore")


def fetch_pdf(aid: str, path: Path) -> Path:
    if path.exists() and path.stat().st_size > 1024:
        return path
    request = urllib.request.Request(f"https://arxiv.org/pdf/{aid}.pdf", headers={"User-Agent": "Mozilla/5.0"})
    with urllib.request.urlopen(request, timeout=180) as response:
        with path.open("wb") as file:
            while True:
                chunk = response.read(1024 * 1024)
                if not chunk:
                    break
                file.write(chunk)
    return path


def get_pdf_first_page_text(aid: str, cache_dir: Path) -> str:
    pdf_path = cache_dir / f"{aid}.pdf"
    for attempt in range(2):
        fetch_pdf(aid, pdf_path)
        try:
            result = subprocess.run(
                ["pdftotext", "-f", "1", "-l", "1", "-layout", str(pdf_path), "-"],
                check=True,
                capture_output=True,
                text=True,
            )
            return result.stdout
        except subprocess.CalledProcessError:
            if attempt == 0 and pdf_path.exists():
                pdf_path.unlink()
                continue
            raise
    raise RuntimeError(f"Failed to parse PDF for {aid}")


def normalize_spaces(text: str) -> str:
    return " ".join(text.replace("\xa0", " ").split())


def extract_entries(text: str, limit: int):
    entries = []
    for match in ENTRY_RE.finditer(text):
        body = match.group("body")
        arxiv_match = ARXIV_RE.search(body)
        if not arxiv_match:
            continue
        unit_match = UNIT_LINE_RE.search(match.group(0))
        entries.append(
            {
                "match": match,
                "num": int(match.group("num")),
                "title": match.group("title"),
                "body": body,
                "arxiv_id": arxiv_match.group(1),
                "unit": unit_match.group(1).strip() if unit_match else "",
            }
        )
        if len(entries) >= limit:
            break
    return entries


def collect_known_orgs(text: str):
    orgs = []
    seen = set()
    for match in re.finditer(r"\*\*🏫 单位\*\*：(.*)", text):
        value = match.group(1).strip()
        if not value:
            continue
        for part in value.split("⟐"):
            org = normalize_org(part)
            if not org:
                continue
            key = org.lower()
            if key in seen:
                continue
            seen.add(key)
            orgs.append(org)
    orgs.extend(sorted(KNOWN_COMPANIES))
    merged = []
    seen = set()
    for org in sorted(orgs, key=len, reverse=True):
        key = org.lower()
        if key in seen:
            continue
        seen.add(key)
        merged.append(org)
    return merged


def html_source_text(aid: str, cache_dir: Path):
    html_path = cache_dir / f"{aid}.html"
    try:
        html = fetch_text(f"https://arxiv.org/html/{aid}", html_path)
    except (urllib.error.HTTPError, urllib.error.URLError):
        return None, None
    soup = BeautifulSoup(html, "html.parser")
    notes = soup.select_one(".ltx_author_notes")
    if notes:
        notes_text = normalize_spaces(notes.get_text(" ", strip=True))
        if contains_org_signal(notes_text):
            return "html_notes", notes_text
    authors = soup.select_one(".ltx_authors")
    if authors:
        author_text = "\n".join(line.strip() for line in authors.get_text("\n", strip=True).splitlines() if line.strip())
        if contains_org_signal(author_text):
            return "html_authors", author_text
    article = soup.select_one("article")
    abstract = soup.select_one(".ltx_abstract")
    if article and abstract:
        chunks = []
        for child in article.children:
            if child == abstract:
                break
            if getattr(child, "name", None) in {"h1", "div", "p", "span"}:
                text = normalize_spaces(child.get_text(" ", strip=True))
                if text:
                    chunks.append(text)
        header_text = " ".join(chunks)
        if contains_org_signal(header_text):
            return "html_header", header_text
    return None, None


def contains_org_signal(text: str) -> bool:
    lowered = text.lower()
    return any(word in lowered for word in ORG_WORDS) or any(org.lower() in lowered for org in KNOWN_COMPANIES)


def clauses_from_text(text: str):
    clauses = []
    cleaned = normalize_spaces(text)
    for match in re.finditer(r"([^.]*(?:\b(?:is|are|was|were)\s+(?:with|at|from)\b)[^.]*)(?=\.|$)", cleaned, re.I):
        clause = match.group(1).strip(" ;,)")
        if clause:
            clauses.append(clause)
    if clauses:
        return clauses
    return [line.strip() for line in re.split(r"[\n.;]+", text) if line.strip()]


def normalize_org(text: str) -> str:
    text = normalize_spaces(text)
    text = re.sub(r"^[\d*\-†‡§¶\[\]\(\)]+", "", text).strip()
    text = re.sub(r"\s*\([^)]*email[^)]*\)", "", text, flags=re.I)
    text = re.sub(r"\s*\([^)]*corresponding[^)]*\)", "", text, flags=re.I)
    text = re.sub(r"\s+", " ", text).strip(" ,;.")
    return text


def looks_like_location(piece: str) -> bool:
    stripped = piece.strip(" ,;.")
    lowered = stripped.lower()
    if not stripped:
        return True
    if re.fullmatch(r"[\d\- ]+", stripped):
        return True
    if lowered in LOCATION_WORDS:
        return True
    if lowered.endswith(" china") or lowered.endswith(" usa") or lowered.endswith(" uk"):
        return True
    return False


def is_org_piece(piece: str) -> bool:
    lowered = piece.lower()
    if "@" in piece or looks_like_location(piece):
        return False
    if lowered.startswith(SKIP_PREFIXES) and not any(word in lowered for word in ("university", "academy", "institute", "college london")):
        return False
    if any(word in lowered for word in ORG_WORDS):
        return True
    if piece in KNOWN_COMPANIES:
        return True
    if re.fullmatch(r"[A-Z][A-Z0-9&\-]{1,9}", piece):
        return True
    if piece in {"ETH Zurich", "EPFL"}:
        return True
    return False


def dedupe_in_order(items):
    out = []
    seen = set()
    for item in items:
        key = item.lower()
        if key in seen:
            continue
        seen.add(key)
        out.append(item)
    return out


def canonicalize_org(org: str) -> str:
    return ORG_ALIASES.get(org, org)


def is_noise_org(org: str) -> bool:
    lowered = org.lower()
    if any(token in lowered for token in ("their ", "our ", "this ", "that ", "these ", "those ", "scalability", "dataset", "benchmark", "approach", "framework")):
        return True
    if "@" in org or "http" in lowered:
        return True
    if not any(word in lowered for word in ORG_WORDS) and org not in KNOWN_COMPANIES and org not in ORG_ALIASES.values():
        if re.fullmatch(r"[A-Z][A-Z0-9&\-]{1,9}", org):
            return True
        if any(ch.islower() for ch in org):
            return True
    return False


def prune_subunits(orgs):
    canonical = [canonicalize_org(org) for org in orgs]
    canonical = [org for org in canonical if not is_noise_org(org)]
    has_high_level = any(
        any(word in org.lower() for word in ("university", "institute", "academy", "hospital", "college", "technology"))
        or org in KNOWN_COMPANIES
        for org in canonical
    )
    if not has_high_level:
        return dedupe_in_order(canonical)
    pruned = []
    for org in canonical:
        lowered = org.lower()
        if org not in KEEP_SUBUNITS and any(word in lowered for word in (" lab", "laboratory", "center", "centre", "school")):
            continue
        pruned.append(org)
    return dedupe_in_order(pruned)


def find_known_orgs(text: str, known_orgs):
    matches = []
    for org in known_orgs:
        pattern = re.compile(rf"(?<!\w){re.escape(org)}(?!\w)", re.I)
        for match in pattern.finditer(text):
            matches.append((match.start(), match.end(), org))
    matches.sort(key=lambda item: (item[0], -(item[1] - item[0])))
    selected = []
    last_end = -1
    for start, end, org in matches:
        if start < last_end:
            continue
        selected.append((start, end, org))
        last_end = end
    return dedupe_in_order([org for _, _, org in sorted(selected)])


def heuristic_orgs(text: str):
    pieces = []
    for part in re.split(r"[;\n]", text):
        for piece in re.split(r",(?![^(]*\))", part):
            for sub_piece in re.split(r"\s+\band\b\s+", piece):
                cleaned = normalize_org(sub_piece)
                if cleaned:
                    pieces.append(cleaned)
    orgs = []
    for piece in pieces:
        if is_org_piece(piece):
            orgs.append(piece)
    if not orgs:
        for pattern in ORG_PATTERNS:
            for match in pattern.finditer(text):
                org = normalize_org(match.group(1))
                if org and not looks_like_location(org):
                    orgs.append(org)
    return dedupe_in_order(orgs)


def extract_affiliations(raw_text: str, known_orgs):
    affiliations = []
    for clause in clauses_from_text(raw_text):
        clause = re.sub(r"https?://\S+", "", clause)
        clause = re.sub(r"\S+@\S+", "", clause)
        clause = re.sub(r"^.*?\b(?:is|are|was|were)\s+(?:with|at|from)\s+", "", clause, flags=re.I)
        clause = re.sub(r"Email:.*$", "", clause, flags=re.I)
        clause = normalize_spaces(clause)
        if not clause or "supported" in clause.lower():
            continue
        hits = find_known_orgs(clause, known_orgs)
        if hits:
            affiliations.extend(hits)
            continue
        affiliations.extend(heuristic_orgs(clause))
    if affiliations:
        normalized = [normalize_org(item) for item in affiliations if normalize_org(item)]
        return prune_subunits(normalized)
    return []


def extract_pdf_affiliations(aid: str, known_orgs, cache_dir: Path):
    text = get_pdf_first_page_text(aid, cache_dir)
    header = []
    for line in text.splitlines():
        cleaned = normalize_spaces(line)
        if not cleaned:
            continue
        lowered = cleaned.lower()
        if any(marker in lowered for marker in HEADER_MARKERS):
            break
        if "arxiv:" in lowered:
            continue
        header.append(cleaned)
    header_text = " ".join(header)
    return extract_affiliations(header_text, known_orgs)


def replace_unit_line(block_text: str, value: str) -> str:
    replacement = f"- **🏫 单位**：{value}"
    return UNIT_LINE_RE.sub(replacement, block_text, count=1)


def apply_updates(text: str, entries, updates, force: bool):
    parts = []
    last = 0
    for entry in entries:
        match = entry["match"]
        parts.append(text[last:match.start()])
        block_text = match.group(0)
        current = entry["unit"]
        new_value = updates.get(entry["arxiv_id"], "")
        if new_value and (force or not current):
            block_text = replace_unit_line(block_text, new_value)
        parts.append(block_text)
        last = match.end()
    parts.append(text[last:])
    return "".join(parts)


def resolve_entry(index: int, entry, known_orgs, cache_dir: Path):
    aid = entry["arxiv_id"]
    try:
        source, raw_text = html_source_text(aid, cache_dir)
        affiliations = extract_affiliations(raw_text, known_orgs) if raw_text else []
        if not affiliations:
            affiliations = extract_pdf_affiliations(aid, known_orgs, cache_dir)
            source = "pdf"
    except Exception as exc:
        source = f"miss:{type(exc).__name__}"
        affiliations = []
    return index, aid, source or "none", affiliations


def main():
    args = parse_args()
    readme_path = Path(args.readme)
    text = readme_path.read_text(encoding="utf-8")
    entries = extract_entries(text, args.limit)
    known_orgs = collect_known_orgs(text)
    CACHE_DIR.mkdir(parents=True, exist_ok=True)
    updates = {}
    resolved = 0
    known_snapshot = tuple(known_orgs)
    results = {}

    with concurrent.futures.ThreadPoolExecutor(max_workers=max(1, args.workers)) as executor:
        futures = [
            executor.submit(resolve_entry, index, entry, known_snapshot, CACHE_DIR)
            for index, entry in enumerate(entries, start=1)
        ]
        for future in concurrent.futures.as_completed(futures):
            index, aid, source, affiliations = future.result()
            value = " ⟐ ".join(affiliations)
            updates[aid] = value
            results[index] = (aid, source, value)
            if value:
                resolved += 1
            print(f"[{index}/{len(entries)}] {aid} source={source} unit={value or '<blank>'}", flush=True)

    new_text = apply_updates(text, entries, updates, args.force)
    if args.write:
        readme_path.write_text(new_text, encoding="utf-8")
    print(f"Resolved {resolved}/{len(entries)} entries", flush=True)


if __name__ == "__main__":
    sys.exit(main())
