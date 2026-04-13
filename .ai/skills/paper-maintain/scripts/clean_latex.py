#!/usr/bin/env python3
r"""Clean LaTeX markup from abs/ files and README.md titles.

Converts common LaTeX patterns to plain Unicode text:
  $N\times$  → N×    \textit{x} → x    $^\circ$ → °
  $^2$       → ²     \textbf{x} → x    \mathbb{R} → ℝ
  $\sim$     → ~     \emph{x}   → x    \mathcal{L} → ℒ

Usage:
    python3 .ai/skills/paper-maintain/scripts/paper.py clean-latex [--dry-run] [--readme README] [--abs-dir ABS]
"""

from __future__ import annotations

import argparse
import re
from pathlib import Path


# ── Symbol tables ─────────────────────────────────────────────────────────────

COMMAND_SYMBOLS: dict[str, str] = {
    r"\times":        "×",
    r"\circ":         "°",
    r"\sim":          "~",
    r"\approx":       "≈",
    r"\in":           "∈",
    r"\log":          "log",
    r"\pi":           "π",
    r"\alpha":        "α",
    r"\beta":         "β",
    r"\gamma":        "γ",
    r"\delta":        "δ",
    r"\epsilon":      "ε",
    r"\lambda":       "λ",
    r"\mu":           "μ",
    r"\sigma":        "σ",
    r"\tau":          "τ",
    r"\phi":          "φ",
    r"\psi":          "ψ",
    r"\omega":        "ω",
    r"\textasciicircum": "^",
    r"\and":          ", ",
}

MATHBB: dict[str, str] = {
    "R": "ℝ", "Z": "ℤ", "N": "ℕ", "C": "ℂ", "Q": "ℚ",
}

MATHCAL: dict[str, str] = {
    "L": "ℒ", "O": "𝒪", "F": "ℱ", "H": "ℋ", "N": "𝒩",
}

SUPERSCRIPT: dict[str, str] = {
    "0": "⁰", "1": "¹", "2": "²", "3": "³", "4": "⁴",
    "5": "⁵", "6": "⁶", "7": "⁷", "8": "⁸", "9": "⁹",
    "+": "⁺", "-": "⁻", "n": "ⁿ", "i": "ⁱ",
}


# ── Core cleaner ──────────────────────────────────────────────────────────────

def _strip_braced(cmd: str, text: str) -> str:
    r"""Replace \cmd{content} with content."""
    return re.sub(r"\\%s\{([^}]*)\}" % re.escape(cmd), r"\1", text)


def _superscript(match: re.Match) -> str:
    content = match.group(1)
    result = "".join(SUPERSCRIPT.get(c, c) for c in content)
    return result


def clean_latex(text: str) -> str:
    # \keywords{...} — remove entirely
    text = re.sub(r"\\keywords\{[^}]*\}", "", text)

    # \mathbb{X} → ℝ etc.
    def replace_mathbb(m: re.Match) -> str:
        return MATHBB.get(m.group(1), m.group(1))
    text = re.sub(r"\\mathbb\{([^}])\}", replace_mathbb, text)

    # \mathcal{X} → 𝒪 etc.
    def replace_mathcal(m: re.Match) -> str:
        return MATHCAL.get(m.group(1), m.group(1))
    text = re.sub(r"\\mathcal\{([^}])\}", replace_mathcal, text)

    # \mathrm{...} / \mathit{...} / \boldsymbol{...} → content
    for cmd in ("mathrm", "mathit", "mathbf", "boldsymbol", "mbox", "emph"):
        text = _strip_braced(cmd, text)

    # \textit{...} / \textbf{...} → content
    for cmd in ("textit", "textbf", "textrm", "textsf", "texttt"):
        text = _strip_braced(cmd, text)

    # ^\circ → ° (must be before generic \circ → °)
    text = re.sub(r"\^\\circ|\^{\\circ}", "°", text)

    # Named command symbols
    for latex, uni in COMMAND_SYMBOLS.items():
        text = text.replace(latex, uni)

    # ^° leftover (e.g. after $^\circ$ → ^°) → °
    text = text.replace("^°", "°")

    # $^{...}$ or $^X$ — superscripts inside math
    text = re.sub(r"\^\{([^}]+)\}", _superscript, text)
    text = re.sub(r"\^([0-9nij+\-])", lambda m: SUPERSCRIPT.get(m.group(1), m.group(1)), text)

    # $...\%...$ — percent in math → just %
    text = re.sub(r"\\%", "%", text)

    # Strip paired $...$ inline math delimiters (not lone $ like currency)
    text = re.sub(r"\$([^$\n]*)\$", r"\1", text)

    # Clean up leftover \cmd (unknown commands without braces)
    text = re.sub(r"\\[a-zA-Z]+\b", "", text)

    # Collapse multiple spaces (but preserve leading/trailing newlines)
    text = re.sub(r"  +", " ", text)

    return text


# ── File processors ───────────────────────────────────────────────────────────

def process_abs_file(path: Path, dry_run: bool) -> bool:
    original = path.read_text()
    cleaned = clean_latex(original)
    if cleaned == original:
        return False
    if not dry_run:
        path.write_text(cleaned)
    return True


def process_readme(path: Path, dry_run: bool) -> int:
    text = path.read_text()

    def clean_title_line(m: re.Match) -> str:
        prefix = m.group(1)   # "#### [N] "
        title = m.group(2)
        return prefix + clean_latex(title)

    cleaned = re.sub(r"(#### \[\d+\] )(.+)", clean_title_line, text)
    count = sum(1 for a, b in zip(text.splitlines(), cleaned.splitlines()) if a != b)
    if cleaned != text and not dry_run:
        path.write_text(cleaned)
    return count


# ── CLI ───────────────────────────────────────────────────────────────────────

def parse_args() -> argparse.Namespace:
    parser = argparse.ArgumentParser(description="Clean LaTeX from abs files and README titles.")
    parser.add_argument("--readme", type=Path, default=Path("README.md"))
    parser.add_argument("--abs-dir", type=Path, default=Path("abs"))
    parser.add_argument("--commit", help="Only process abs files added/modified in this commit (e.g. HEAD or a hash).")
    parser.add_argument("--dry-run", action="store_true", help="Report changes without writing.")
    return parser.parse_args()


def _files_in_commit(commit: str) -> list[Path]:
    import subprocess
    result = subprocess.run(
        ["git", "diff-tree", "--no-commit-id", "-r", "--name-only", commit],
        capture_output=True, text=True, check=True,
    )
    return [Path(p) for p in result.stdout.splitlines() if p.startswith("abs/") and p.endswith(".md")]


def main() -> None:
    args = parse_args()

    if args.commit:
        abs_files = sorted(_files_in_commit(args.commit))
    else:
        abs_files = sorted(args.abs_dir.glob("*.md"))

    abs_changed = 0
    for p in abs_files:
        if not p.exists():
            continue
        if process_abs_file(p, args.dry_run):
            abs_changed += 1
            print(f"  abs/{p.name}")

    readme_changed = process_readme(args.readme, args.dry_run)

    suffix = " (dry-run)" if args.dry_run else ""
    print(f"\n✓ abs files updated: {abs_changed}{suffix}")
    print(f"✓ README title lines updated: {readme_changed}{suffix}")


if __name__ == "__main__":
    main()
