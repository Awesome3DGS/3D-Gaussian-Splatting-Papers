#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
import sys
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path
from urllib.error import HTTPError, URLError
from urllib.parse import urlencode
from urllib.request import Request, urlopen
from xml.etree import ElementTree


API_ENDPOINT = "https://arxiv.org/api/query"
ARXIV_ID_RE = re.compile(r"^(\d{4}\.\d{5})$")
ARXIV_ID_WITH_VERSION_RE = re.compile(r"^(?P<base>\d{4}\.\d{5})(?:v\d+)?$")
ATOM_NS = {"atom": "http://www.w3.org/2005/Atom"}
HEADERS = {"User-Agent": "3dgs-papers-pipeline/1.0"}


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


@dataclass(frozen=True)
class QuerySpec:
    label: str
    search_query: str


@dataclass(frozen=True)
class ArxivPaper:
    arxiv_id: str
    title: str
    authors: list[str]
    abstract: str
    submitted: str
    updated: str


QUERY_SPECS = (
    QuerySpec(label="3DGS", search_query="all:3DGS"),
    QuerySpec(label='"3D Gaussian"', search_query='all:"3D Gaussian"'),
    QuerySpec(label='"Gaussian Splatting"', search_query='all:"Gaussian Splatting"'),
)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(
        description="Fetch recent 3DGS-related papers from arXiv Atom API."
    )
    parser.add_argument(
        "--since",
        required=True,
        help="Only keep papers with arXiv ID greater than this ID (YYMM.NNNNN).",
    )
    parser.add_argument(
        "--max",
        type=int,
        default=500,
        help="Maximum number of results per query (default: 500).",
    )
    parser.add_argument(
        "--output",
        type=Path,
        help="Output JSON file path. Defaults to stdout.",
    )
    args = parser.parse_args()
    if not ARXIV_ID_RE.fullmatch(args.since):
        parser.error("--since must match YYMM.NNNNN, e.g. 2603.09718")
    if args.max <= 0:
        parser.error("--max must be a positive integer.")
    return args


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def clean_text(value: str | None) -> str:
    return " ".join((value or "").split())


def parse_arxiv_id(raw_id: str) -> str:
    candidate = raw_id.rsplit("/", 1)[-1].strip()
    match = ARXIV_ID_WITH_VERSION_RE.fullmatch(candidate)
    if not match:
        return ""
    return match.group("base")


def build_query_url(search_query: str, max_results: int) -> str:
    query = urlencode(
        {
            "search_query": search_query,
            "max_results": str(max_results),
            "sortBy": "submittedDate",
            "sortOrder": "descending",
        }
    )
    return f"{API_ENDPOINT}?{query}"


def fetch_feed(url: str) -> ElementTree.Element:
    request = Request(url, headers=HEADERS)
    with urlopen(request, timeout=30) as response:
        data = response.read()
    return ElementTree.fromstring(data)


def parse_entries(feed: ElementTree.Element) -> list[ArxivPaper]:
    papers: list[ArxivPaper] = []
    for entry in feed.findall("atom:entry", ATOM_NS):
        arxiv_id = parse_arxiv_id(entry.findtext("atom:id", default="", namespaces=ATOM_NS))
        if not arxiv_id:
            continue
        title = clean_text(entry.findtext("atom:title", default="", namespaces=ATOM_NS))
        abstract = clean_text(entry.findtext("atom:summary", default="", namespaces=ATOM_NS))
        submitted = clean_text(entry.findtext("atom:published", default="", namespaces=ATOM_NS))
        updated = clean_text(entry.findtext("atom:updated", default="", namespaces=ATOM_NS))
        authors = []
        for author_node in entry.findall("atom:author", ATOM_NS):
            name = clean_text(author_node.findtext("atom:name", default="", namespaces=ATOM_NS))
            if name:
                authors.append(name)
        papers.append(
            ArxivPaper(
                arxiv_id=arxiv_id,
                title=title,
                authors=authors,
                abstract=abstract,
                submitted=submitted,
                updated=updated,
            )
        )
    return papers


def keep_newer_candidate(existing: ArxivPaper, candidate: ArxivPaper) -> ArxivPaper:
    if candidate.submitted > existing.submitted:
        return candidate
    if candidate.submitted == existing.submitted and candidate.updated > existing.updated:
        return candidate
    return existing


def collect_papers(since_id: str, max_results: int) -> list[ArxivPaper]:
    deduped: dict[str, ArxivPaper] = {}
    for query in QUERY_SPECS:
        feed = fetch_feed(build_query_url(query.search_query, max_results=max_results))
        for paper in parse_entries(feed):
            if paper.arxiv_id <= since_id:
                continue
            existing = deduped.get(paper.arxiv_id)
            if existing is None:
                deduped[paper.arxiv_id] = paper
            else:
                deduped[paper.arxiv_id] = keep_newer_candidate(existing, paper)
    return sorted(deduped.values(), key=lambda item: item.arxiv_id, reverse=True)


def render_payload(since_id: str, papers: list[ArxivPaper]) -> dict[str, object]:
    return {
        "fetched_at": utc_now_iso(),
        "since": since_id,
        "queries": [spec.label for spec in QUERY_SPECS],
        "results": [asdict(paper) for paper in papers],
    }


def write_json(payload: dict[str, object], output_path: Path | None) -> None:
    rendered = json.dumps(payload, ensure_ascii=False, indent=2)
    if output_path is None:
        sys.stdout.write(rendered + "\n")
        return
    output_path.parent.mkdir(parents=True, exist_ok=True)
    output_path.write_text(rendered + "\n")


def main() -> None:
    _install_proxy()
    args = parse_args()
    try:
        papers = collect_papers(since_id=args.since, max_results=args.max)
        payload = render_payload(since_id=args.since, papers=papers)
    except (HTTPError, URLError, TimeoutError, OSError, ElementTree.ParseError) as exc:
        print(f"Failed to fetch arXiv data: {exc}", file=sys.stderr)
        raise SystemExit(1) from exc
    write_json(payload, args.output)


if __name__ == "__main__":
    main()
