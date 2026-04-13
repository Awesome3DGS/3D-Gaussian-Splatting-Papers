#!/usr/bin/env python3

from __future__ import annotations

import argparse
import json
import re
from collections import Counter
from dataclasses import asdict, dataclass
from datetime import datetime, timezone
from pathlib import Path

from sync import count_entries


ARXIV_RE = re.compile(r"\[arXiv:([0-9]{4}\.[0-9]{5})\]")
ENTRY_HEADING_RE = re.compile(r"(?m)^#### \[(\d+)\] ")
CONFERENCE_BLOCK_RE = re.compile(
    r"(?s)#### \*\*📚 会议期刊\*\*\n\n(?P<body>.*?)\n#### \*\*📂 归档论文\*\*"
)
INDEX_LINK_COUNT_RE = re.compile(
    r"\[\[(?P<label>[^\]]+)\]\(\./(?P<path>[^)]+\.md)\)\]\s*\((?P<count>\d+)\s*篇\)"
)


@dataclass(frozen=True)
class Issue:
    level: str
    check: str
    message: str


@dataclass(frozen=True)
class CheckResult:
    name: str
    status: str
    message: str


@dataclass(frozen=True)
class CountTarget:
    label: str
    path: Path
    expected_count: int


def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Validate repository consistency for paper pipeline.")
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
        "--fix",
        action="store_true",
        help="Fix README entry numbering only (renumber #### [N] headings).",
    )
    parser.add_argument(
        "--json",
        action="store_true",
        help="Emit machine-readable JSON output.",
    )
    return parser.parse_args()


def utc_now_iso() -> str:
    return datetime.now(timezone.utc).replace(microsecond=0).isoformat().replace("+00:00", "Z")


def renumber_readme_entries(text: str) -> str:
    counter = 1

    def repl(match: re.Match[str]) -> str:
        nonlocal counter
        replacement = f"#### [{counter}] "
        counter += 1
        return replacement

    return ENTRY_HEADING_RE.sub(repl, text)


def evaluate_arxiv_uniqueness(readme_text: str) -> tuple[CheckResult, list[Issue]]:
    ids = ARXIV_RE.findall(readme_text)
    counts = Counter(ids)
    duplicate_ids = sorted(arxiv_id for arxiv_id, value in counts.items() if value > 1)
    if duplicate_ids:
        issues = [
            Issue(
                level="ERROR",
                check="README arXiv uniqueness",
                message=f"Duplicate arXiv ID: {arxiv_id} (count={counts[arxiv_id]}).",
            )
            for arxiv_id in duplicate_ids
        ]
        return (
            CheckResult(
                name="README arXiv uniqueness",
                status="ERROR",
                message=f"{len(duplicate_ids)} duplicate IDs found among {len(ids)} entries.",
            ),
            issues,
        )
    return (
        CheckResult(
            name="README arXiv uniqueness",
            status="PASS",
            message=f"{len(ids)} IDs found, all unique.",
        ),
        [],
    )


def evaluate_abs_coverage(readme_text: str, abs_dir: Path) -> tuple[CheckResult, list[Issue]]:
    readme_ids = sorted(set(ARXIV_RE.findall(readme_text)))
    missing = [arxiv_id for arxiv_id in readme_ids if not (abs_dir / f"{arxiv_id}.md").exists()]
    if missing:
        issues = [
            Issue(
                level="ERROR",
                check="abs coverage",
                message=f"Missing abs file: {abs_dir / f'{arxiv_id}.md'}",
            )
            for arxiv_id in missing
        ]
        return (
            CheckResult(
                name="abs coverage",
                status="ERROR",
                message=f"{len(missing)} missing abs files for {len(readme_ids)} README IDs.",
            ),
            issues,
        )
    return (
        CheckResult(
            name="abs coverage",
            status="PASS",
            message=f"{len(readme_ids)}/{len(readme_ids)} README IDs have abs files.",
        ),
        [],
    )


def evaluate_readme_numbering(
    readme_path: Path, readme_text: str, fix: bool
) -> tuple[CheckResult, list[Issue], str, bool]:
    numbers = [int(match.group(1)) for match in ENTRY_HEADING_RE.finditer(readme_text)]
    expected = list(range(1, len(numbers) + 1))
    mismatches = [
        (index, current)
        for index, current in enumerate(numbers, start=1)
        if current != expected[index - 1]
    ]
    if not mismatches:
        return (
            CheckResult(
                name="README numbering continuity",
                status="PASS",
                message=f"{len(numbers)} entries numbered continuously from 1.",
            ),
            [],
            readme_text,
            False,
        )

    if fix:
        fixed_text = renumber_readme_entries(readme_text)
        if fixed_text != readme_text:
            readme_path.write_text(fixed_text)
        post_numbers = [int(match.group(1)) for match in ENTRY_HEADING_RE.finditer(fixed_text)]
        post_mismatches = [
            (index, current)
            for index, current in enumerate(post_numbers, start=1)
            if current != index
        ]
        if not post_mismatches:
            return (
                CheckResult(
                    name="README numbering continuity",
                    status="PASS",
                    message=f"Renumbered {len(post_numbers)} entries to be continuous.",
                ),
                [
                    Issue(
                        level="WARNING",
                        check="README numbering continuity",
                        message="README entry numbers were fixed in-place (--fix).",
                    )
                ],
                fixed_text,
                True,
            )
        return (
            CheckResult(
                name="README numbering continuity",
                status="ERROR",
                message="Renumbering attempted but numbering is still inconsistent.",
            ),
            [
                Issue(
                    level="ERROR",
                    check="README numbering continuity",
                    message="Failed to repair numbering with --fix.",
                )
            ],
            fixed_text,
            fixed_text != readme_text,
        )

    first_index, first_value = mismatches[0]
    return (
        CheckResult(
            name="README numbering continuity",
            status="ERROR",
            message=f"Found {len(mismatches)} numbering mismatches.",
        ),
        [
            Issue(
                level="ERROR",
                check="README numbering continuity",
                message=(
                    f"Entry position {first_index} is numbered [{first_value}], "
                    f"expected [{first_index}]."
                ),
            )
        ],
        readme_text,
        False,
    )


def parse_count_targets(section_text: str, prefix: str) -> list[CountTarget]:
    targets: list[CountTarget] = []
    for match in INDEX_LINK_COUNT_RE.finditer(section_text):
        rel_path = match.group("path")
        if not rel_path.startswith(prefix):
            continue
        targets.append(
            CountTarget(
                label=match.group("label"),
                path=Path(rel_path),
                expected_count=int(match.group("count")),
            )
        )
    return targets


def evaluate_count_targets(
    check_name: str, targets: list[CountTarget]
) -> tuple[CheckResult, list[Issue]]:
    if not targets:
        return (
            CheckResult(name=check_name, status="ERROR", message="No count targets found in README."),
            [
                Issue(
                    level="ERROR",
                    check=check_name,
                    message="README index does not contain any matching counted links.",
                )
            ],
        )

    issues: list[Issue] = []
    for target in targets:
        if not target.path.exists():
            issues.append(
                Issue(
                    level="ERROR",
                    check=check_name,
                    message=f"Missing referenced file: {target.path}",
                )
            )
            continue
        actual_count = count_entries(target.path)
        if actual_count != target.expected_count:
            issues.append(
                Issue(
                    level="ERROR",
                    check=check_name,
                    message=(
                        f"Count mismatch for {target.path}: "
                        f"README={target.expected_count}, actual={actual_count}."
                    ),
                )
            )

    if issues:
        return (
            CheckResult(
                name=check_name,
                status="ERROR",
                message=f"{len(issues)} count issues found across {len(targets)} targets.",
            ),
            issues,
        )
    return (
        CheckResult(
            name=check_name,
            status="PASS",
            message=f"All {len(targets)} targets match README counts.",
        ),
        [],
    )


def evaluate_conference_counts(readme_text: str) -> tuple[CheckResult, list[Issue]]:
    match = CONFERENCE_BLOCK_RE.search(readme_text)
    if match is None:
        return (
            CheckResult(
                name="README conference counts",
                status="ERROR",
                message="Could not locate conference index block in README.",
            ),
            [
                Issue(
                    level="ERROR",
                    check="README conference counts",
                    message="Missing README section between conference and archive headings.",
                )
            ],
        )
    targets = parse_count_targets(match.group("body"), prefix="20")
    return evaluate_count_targets("README conference counts", targets)


def evaluate_archive_counts(readme_text: str) -> tuple[CheckResult, list[Issue]]:
    targets = parse_count_targets(readme_text, prefix="archive/")
    return evaluate_count_targets("README archive counts", targets)


def render_text_report(
    computed_at: str,
    readme_path: Path,
    abs_dir: Path,
    fix_applied: bool,
    checks: list[CheckResult],
    issues: list[Issue],
) -> str:
    lines = [
        "Validation Report",
        f"- computed_at: {computed_at}",
        f"- readme: {readme_path}",
        f"- abs_dir: {abs_dir}",
        f"- fix_applied: {'yes' if fix_applied else 'no'}",
        "",
        "Checks",
    ]
    for check in checks:
        lines.append(f"- [{check.status}] {check.name}: {check.message}")

    errors = [issue for issue in issues if issue.level == "ERROR"]
    warnings = [issue for issue in issues if issue.level == "WARNING"]
    if not issues:
        lines.extend(["", "Result", "- All checks passed."])
        return "\n".join(lines) + "\n"

    if errors:
        lines.extend(["", "Errors"])
        for issue in errors:
            lines.append(f"- {issue.check}: {issue.message}")

    if warnings:
        lines.extend(["", "Warnings"])
        for issue in warnings:
            lines.append(f"- {issue.check}: {issue.message}")

    return "\n".join(lines) + "\n"


def main() -> None:
    args = parse_args()
    readme_path: Path = args.readme
    abs_dir: Path = args.abs_dir
    fix: bool = args.fix

    if not readme_path.exists():
        raise SystemExit(f"README not found: {readme_path}")

    readme_text = readme_path.read_text()
    checks: list[CheckResult] = []
    issues: list[Issue] = []

    numbering_check, numbering_issues, readme_text, fix_applied = evaluate_readme_numbering(
        readme_path=readme_path,
        readme_text=readme_text,
        fix=fix,
    )
    checks.append(numbering_check)
    issues.extend(numbering_issues)

    uniqueness_check, uniqueness_issues = evaluate_arxiv_uniqueness(readme_text)
    checks.append(uniqueness_check)
    issues.extend(uniqueness_issues)

    coverage_check, coverage_issues = evaluate_abs_coverage(readme_text, abs_dir=abs_dir)
    checks.append(coverage_check)
    issues.extend(coverage_issues)

    conference_check, conference_issues = evaluate_conference_counts(readme_text)
    checks.append(conference_check)
    issues.extend(conference_issues)

    archive_check, archive_issues = evaluate_archive_counts(readme_text)
    checks.append(archive_check)
    issues.extend(archive_issues)

    computed_at = utc_now_iso()
    payload = {
        "computed_at": computed_at,
        "readme": str(readme_path),
        "abs_dir": str(abs_dir),
        "fix_applied": fix_applied,
        "checks": [asdict(check) for check in checks],
        "issues": [asdict(issue) for issue in issues],
        "error_count": sum(1 for issue in issues if issue.level == "ERROR"),
        "warning_count": sum(1 for issue in issues if issue.level == "WARNING"),
    }

    if args.json:
        print(json.dumps(payload, ensure_ascii=False, indent=2))
    else:
        print(
            render_text_report(
                computed_at=computed_at,
                readme_path=readme_path,
                abs_dir=abs_dir,
                fix_applied=fix_applied,
                checks=checks,
                issues=issues,
            ),
            end="",
        )

    has_error = any(issue.level == "ERROR" for issue in issues)
    raise SystemExit(1 if has_error else 0)


if __name__ == "__main__":
    main()
