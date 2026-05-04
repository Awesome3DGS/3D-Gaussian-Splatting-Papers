#!/usr/bin/env python3

from __future__ import annotations

import argparse
import subprocess
import sys
from pathlib import Path


SCRIPT_DIR = Path(__file__).resolve().parent


def run_script(script_name: str, script_args: list[str]) -> None:
    script_path = SCRIPT_DIR / script_name
    cmd = [sys.executable, str(script_path), *script_args]
    result = subprocess.run(cmd)
    if result.returncode != 0:
        raise SystemExit(result.returncode)


def find_latest_acceptance_report(output_dir: Path) -> Path:
    reports = list(output_dir.glob("archive-acceptance-*.json"))
    if not reports:
        raise SystemExit(
            f"No acceptance report found in {output_dir}. Run `paper check` first."
        )
    return max(reports, key=lambda item: item.stat().st_mtime)


def cmd_fetch(args: argparse.Namespace) -> None:
    script_args = ["--since", args.since, "--max", str(args.max)]
    if args.output is not None:
        script_args.extend(["--output", str(args.output)])
    run_script("fetch.py", script_args)


def cmd_diff(args: argparse.Namespace) -> None:
    script_args = [args.fetch_json, "--readme", str(args.readme), "--abs-dir", str(args.abs_dir)]
    if args.output is not None:
        script_args.extend(["--output", str(args.output)])
    run_script("diff.py", script_args)


def cmd_download(args: argparse.Namespace) -> None:
    script_args = [
        "--input",
        str(args.input),
        "--output",
        str(args.output),
        "--workers",
        str(args.workers),
        "--cache-dir",
        str(args.cache_dir),
    ]
    run_script("download.py", script_args)


def cmd_curate(args: argparse.Namespace) -> None:
    script_args = [
        "--diff",
        str(args.diff),
        "--download",
        str(args.download),
        "--readme",
        str(args.readme),
        "--abs-dir",
        str(args.abs_dir),
        "--cache",
        str(args.cache),
    ]
    if args.dry_run:
        script_args.append("--dry-run")
    run_script("curate.py", script_args)


def cmd_patch(args: argparse.Namespace) -> None:
    script_args = [
        "--base-rev",
        args.base_rev,
        "--baseline-rev",
        args.baseline_rev,
        "--readme",
        str(args.readme),
        "--report",
        str(args.report),
        "--limit",
        str(args.limit),
    ]
    if args.write:
        script_args.append("--write")
    run_script("patch.py", script_args)


def cmd_check(args: argparse.Namespace) -> None:
    check_args = [
        "--archive-glob",
        args.archive_glob,
        "--readme",
        str(args.readme),
        "--output-dir",
        str(args.output_dir),
        "--batch-size",
        str(args.batch_size),
        "--batch-sleep",
        str(args.batch_sleep),
        "--arxiv-timeout",
        str(args.arxiv_timeout),
        "--github-timeout",
        str(args.github_timeout),
        "--arxiv-retries",
        str(args.arxiv_retries),
        "--arxiv-retry-sleep",
        str(args.arxiv_retry_sleep),
        "--github-token",
        args.github_token,
    ]
    if args.timeout is not None:
        check_args.extend(["--timeout", str(args.timeout)])
    if args.skip_github_search:
        check_args.append("--skip-github-search")

    run_script("acceptance_check.py", check_args)

    if not args.patch:
        return

    latest_report = find_latest_acceptance_report(args.output_dir)
    patch_args = ["--input", str(latest_report)]
    if args.yes:
        patch_args.append("--yes")
    if args.no_code:
        patch_args.append("--no-code")
    if args.no_acceptance:
        patch_args.append("--no-acceptance")
    if args.patch_dry_run:
        patch_args.append("--dry-run")
    run_script("acceptance_patch.py", patch_args)


def cmd_archive(args: argparse.Namespace) -> None:
    script_args: list[str] = []
    if args.dry_run:
        script_args.append("--dry-run")
    run_script("archive.py", script_args)


def cmd_sync(_: argparse.Namespace) -> None:
    run_script("sync.py", [])


def cmd_changelog(_: argparse.Namespace) -> None:
    run_script("changelog.py", [])


def cmd_validate(args: argparse.Namespace) -> None:
    script_args = ["--readme", str(args.readme), "--abs-dir", str(args.abs_dir)]
    if args.fix:
        script_args.append("--fix")
    if args.json:
        script_args.append("--json")
    run_script("validate.py", script_args)


def cmd_run(args: argparse.Namespace) -> None:
    script_args = ["--batch", str(args.batch), "--readme", str(args.readme), "--abs-dir", str(args.abs_dir)]
    if args.since is not None:
        script_args.extend(["--since", args.since])
    if args.skip_fetch:
        script_args.append("--skip-fetch")
    run_script("pipeline.py", script_args)


def cmd_passthrough(args: argparse.Namespace) -> None:
    run_script(args.script, args.script_args)


def build_parser() -> argparse.ArgumentParser:
    parser = argparse.ArgumentParser(
        description="Unified CLI for paper-maintain workflow scripts."
    )
    subparsers = parser.add_subparsers(dest="command", required=True)

    fetch = subparsers.add_parser("fetch", help="Fetch recent arXiv papers.")
    fetch.add_argument("--since", required=True, help="Only keep papers newer than this arXiv ID.")
    fetch.add_argument("--max", type=int, default=500, help="Max results per query (default: 500).")
    fetch.add_argument("--output", type=Path, help="Output JSON path.")
    fetch.set_defaults(func=cmd_fetch)

    diff = subparsers.add_parser("diff", help="Compute fetched-vs-existing paper diff.")
    diff.add_argument("fetch_json", nargs="?", default="-", help="Fetch JSON path (default: stdin).")
    diff.add_argument("--readme", type=Path, default=Path("README.md"), help="README path.")
    diff.add_argument("--abs-dir", type=Path, default=Path("abs"), help="abs directory path.")
    diff.add_argument("--output", type=Path, help="Output JSON path.")
    diff.set_defaults(func=cmd_diff)

    download = subparsers.add_parser("download", help="Download affiliation and note/code metadata.")
    download.add_argument("--input", type=Path, default=Path("tmp/diff.json"), help="Diff JSON path.")
    download.add_argument("--output", type=Path, default=Path("tmp/download.json"), help="Output JSON path.")
    download.add_argument("--workers", type=int, default=4, help="Concurrent workers.")
    download.add_argument(
        "--cache-dir",
        type=Path,
        default=Path("tmp/affiliation_cache"),
        help="Cache directory for HTML/PDF downloads.",
    )
    download.set_defaults(func=cmd_download)

    curate = subparsers.add_parser("curate", help="Generate README and abs entries from diff/download payloads.")
    curate.add_argument("--diff", type=Path, default=Path("tmp/diff.json"), help="Diff JSON path.")
    curate.add_argument("--download", type=Path, default=Path("tmp/download.json"), help="Download JSON path.")
    curate.add_argument("--readme", type=Path, default=Path("README.md"), help="README path.")
    curate.add_argument("--abs-dir", type=Path, default=Path("abs"), help="abs directory path.")
    curate.add_argument("--cache", type=Path, default=Path("tmp/curate_cache.json"), help="Curate cache path.")
    curate.add_argument("--dry-run", action="store_true", help="Do not write README/abs/cache/report files.")
    curate.set_defaults(func=cmd_curate)

    patch = subparsers.add_parser("patch", help="Patch README notes/code links from arXiv metadata.")
    patch.add_argument("--base-rev", required=True, help="Git rev marking the start of the patch window (papers added after this commit will be patched).")
    patch.add_argument("--baseline-rev", default="HEAD")
    patch.add_argument("--readme", type=Path, default=Path("README.md"))
    patch.add_argument("--report", type=Path, default=Path("/tmp/recent_sync_metadata_report.json"))
    patch.add_argument("--limit", type=int, default=0)
    patch.add_argument("--write", action="store_true")
    patch.set_defaults(func=cmd_patch)

    check = subparsers.add_parser("check", help="Check acceptance signals and optionally patch markdown.")
    check.add_argument("--archive-glob", default="archive/*.md")
    check.add_argument("--readme", type=Path, default=Path("README.md"))
    check.add_argument("--output-dir", type=Path, default=Path("tmp"))
    check.add_argument("--batch-size", type=int, default=100)
    check.add_argument("--batch-sleep", type=float, default=3.0)
    check.add_argument("--timeout", type=float, default=None)
    check.add_argument("--arxiv-timeout", type=float, default=30.0)
    check.add_argument("--github-timeout", type=float, default=8.0)
    check.add_argument("--arxiv-retries", type=int, default=2)
    check.add_argument("--arxiv-retry-sleep", type=float, default=2.0)
    check.add_argument("--github-token", default="")
    check.add_argument("--skip-github-search", action="store_true")
    check.add_argument("--patch", action="store_true", help="Run acceptance_patch.py on the newest generated JSON report.")
    check.add_argument("--yes", action="store_true", help="Auto-accept suspicious items when patching.")
    check.add_argument("--no-code", action="store_true", help="Disable code URL patching when --patch is used.")
    check.add_argument("--no-acceptance", action="store_true", help="Disable acceptance note patching when --patch is used.")
    check.add_argument("--patch-dry-run", action="store_true", help="Print patch changes without writing markdown.")
    check.set_defaults(func=cmd_check)

    archive = subparsers.add_parser("archive", help="Move accepted papers from README/archive into venue files.")
    archive.add_argument("--dry-run", action="store_true")
    archive.set_defaults(func=cmd_archive)

    sync = subparsers.add_parser("sync", help="Sync accepted-paper docs and README conference index.")
    sync.set_defaults(func=cmd_sync)

    changelog = subparsers.add_parser("changelog", help="Regenerate Changelog.md from git log.")
    changelog.set_defaults(func=cmd_changelog)

    validate = subparsers.add_parser("validate", help="Validate repository consistency.")
    validate.add_argument("--readme", type=Path, default=Path("README.md"), help="README path.")
    validate.add_argument("--abs-dir", type=Path, default=Path("abs"), help="abs directory path.")
    validate.add_argument("--fix", action="store_true", help="Fix README numbering in-place.")
    validate.add_argument("--json", action="store_true", help="Emit machine-readable JSON output.")
    validate.set_defaults(func=cmd_validate)

    run = subparsers.add_parser("run", help="Run one ingest batch (fetch -> diff -> download -> curate -> validate).")
    run.add_argument("--since", help="Only process papers newer than this arXiv ID.")
    run.add_argument("--batch", type=int, default=20, help="Number of papers in this run.")
    run.add_argument("--skip-fetch", action="store_true", help="Reuse existing tmp/fetch.json and tmp/diff.json.")
    run.add_argument("--readme", default="README.md", help="README path.")
    run.add_argument("--abs-dir", default="abs", help="abs directory.")
    run.set_defaults(func=cmd_run)

    passthrough_commands = [
        ("fill-affiliations", "fill_affiliations.py", "Run fill_affiliations.py with passthrough args."),
        ("clean-latex", "clean_latex.py", "Run clean_latex.py with passthrough args."),
        ("export-acceptance-audit", "export_acceptance_audit.py", "Run export_acceptance_audit.py."),
        ("add-abs", "add_abs.py", "Run add_abs.py."),
        ("reverse", "reverse.py", "Run reverse.py with passthrough args."),
        ("format", "format.py", "Run format.py with passthrough args."),
    ]
    for name, script, help_text in passthrough_commands:
        sub = subparsers.add_parser(name, help=help_text)
        sub.add_argument("script_args", nargs=argparse.REMAINDER, help="Arguments passed to the internal script.")
        sub.set_defaults(func=cmd_passthrough, script=script)

    return parser


def main() -> None:
    parser = build_parser()
    args = parser.parse_args()
    args.func(args)


if __name__ == "__main__":
    main()
