#!/usr/bin/env python3
"""Run one batch of the 3DGS paper maintenance pipeline.

Steps: fetch → diff → slice → download → curate → validate

Usage:
    uv run .ai/skills/paper-maintain/scripts/paper.py run                  # auto-detect --since from README
    uv run .ai/skills/paper-maintain/scripts/paper.py run --since 2604.05908
    uv run .ai/skills/paper-maintain/scripts/paper.py run --batch 20       # papers per run (default: 20)
    uv run .ai/skills/paper-maintain/scripts/paper.py run --skip-fetch     # reuse existing tmp/fetch.json + tmp/diff.json
"""

from __future__ import annotations

import argparse
import json
import re
import subprocess
import sys
from pathlib import Path


ARXIV_RE = re.compile(r"\[arXiv:([0-9]{4}\.[0-9]{5})\]")
SCRIPTS = Path(__file__).parent


def run(cmd: list[str], **kwargs) -> subprocess.CompletedProcess:
    print(f"  $ {' '.join(cmd)}")
    result = subprocess.run(cmd, **kwargs)
    if result.returncode != 0:
        print(f"  ERROR: exit {result.returncode}", file=sys.stderr)
        sys.exit(result.returncode)
    return result


def detect_since(readme: Path) -> str:
    ids = ARXIV_RE.findall(readme.read_text())
    if not ids:
        raise SystemExit("Could not detect latest arXiv ID from README.md")
    return max(ids)


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Run one batch of the paper pipeline.")
    parser.add_argument(
        "--since",
        help="Start from papers newer than this arXiv ID. Auto-detected from README if omitted.",
    )
    parser.add_argument(
        "--batch",
        type=int,
        default=20,
        help="Number of papers to process in this run (default: 20).",
    )
    parser.add_argument(
        "--skip-fetch",
        action="store_true",
        help="Skip fetch+diff steps and reuse existing tmp/fetch.json / tmp/diff.json.",
    )
    parser.add_argument("--readme", default="README.md", help="README path.")
    parser.add_argument("--abs-dir", default="abs", help="abs directory.")
    return parser.parse_args()


def main() -> None:
    args = parse_args()
    readme = Path(args.readme)
    tmp = Path("tmp")
    tmp.mkdir(exist_ok=True)

    fetch_json = tmp / "fetch.json"
    diff_json = tmp / "diff.json"

    # ── Step 1-2: fetch + diff ──────────────────────────────────────────────
    if args.skip_fetch:
        print("[ skip ] fetch + diff (reusing existing files)")
        if not diff_json.exists():
            raise SystemExit("tmp/diff.json not found — run without --skip-fetch first.")
    else:
        since = args.since or detect_since(readme)
        print(f"\n[1/5] fetch  (since {since})")
        run(["uv", "run", str(SCRIPTS / "fetch.py"), "--since", since, "--output", str(fetch_json)])

        print("\n[2/5] diff")
        run(["uv", "run", str(SCRIPTS / "diff.py"), str(fetch_json), "--output", str(diff_json)])

    # ── Step 3: slice to batch ──────────────────────────────────────────────
    data = json.loads(diff_json.read_text())
    total_new = data["new_count"]

    if total_new == 0:
        print("\n✓ No new papers — repository is up to date.")
        return

    batch = min(args.batch, total_new)
    remaining = total_new - batch

    sliced = dict(data)
    sliced["new"] = data["new"][-batch:]  # oldest first (diff is sorted newest→oldest)
    sliced["new_count"] = batch
    diff_json.write_text(json.dumps(sliced, ensure_ascii=False, indent=2))

    print(f"\n[3/5] slice  → {batch} papers this batch ({remaining} remaining after this run)")
    for p in sliced["new"]:
        print(f"       {p['arxiv_id']}  {p['title'][:60]}")

    # ── Step 4: download ────────────────────────────────────────────────────
    print("\n[4/5] download")
    run(["uv", "run", str(SCRIPTS / "download.py")])

    # ── Step 5: curate ──────────────────────────────────────────────────────
    print("\n[5/5] curate")
    run(["uv", "run", str(SCRIPTS / "curate.py")])

    # ── Step 6: validate ────────────────────────────────────────────────────
    print("\n[6/6] validate")
    run(
        ["uv", "run", str(SCRIPTS / "validate.py")],
        check=False,
    )

    # ── Summary ─────────────────────────────────────────────────────────────
    report_path = tmp / "curate_report.json"
    if report_path.exists():
        report = json.loads(report_path.read_text())
        items = report.get("items", [])
        ok = sum(1 for r in items if r.get("affiliation_status") == "ok")
        warn = [r for r in items if r.get("affiliation_status") != "ok"]
        print(f"\n✓ {ok}/{batch} papers curated with affiliations")
        if warn:
            print(f"⚠ {len(warn)} papers need manual affiliation:")
            for r in warn:
                print(f"   {r['arxiv_id']}  status={r.get('affiliation_status')}  source={r.get('affiliation_source')}")

    if remaining > 0:
        next_since = sliced["new"][-1]["arxiv_id"]
        print(f"\n{remaining} papers remaining. Next run:")
        print(
            "  uv run .ai/skills/paper-maintain/scripts/paper.py run "
            f"--since {next_since} --skip-fetch"
        )
        print("  (or just say 「继续」)")
    else:
        print("\n✓ All new papers processed.")


if __name__ == "__main__":
    main()
