#!/usr/bin/env python3
"""Add [[中英摘要](...)] links to README.md entries that are missing them."""

from __future__ import annotations

import argparse
import re
from pathlib import Path


def add_abs_links(readme_path: Path) -> int:
    lines = readme_path.read_text(encoding="utf-8").splitlines(keepends=True)
    modified = []
    count = 0
    for line in lines:
        if line.startswith("- **🔗 链接**：") and "[[中英摘要]" not in line:
            arxiv_id = line.split("arXiv:")[1].split("]")[0]
            new_link = f"[[中英摘要](./abs/{arxiv_id}.md)] "
            line = line.replace("[[arXiv:", new_link + "[[arXiv:", 1)
            count += 1
        modified.append(line)
    readme_path.write_text("".join(modified), encoding="utf-8")
    return count


def main() -> None:
    parser = argparse.ArgumentParser(description=__doc__)
    parser.add_argument("--readme", type=Path, default=Path("README.md"), help="README path.")
    args = parser.parse_args()
    count = add_abs_links(args.readme)
    print(f"Added {count} 中英摘要 links to {args.readme}")


if __name__ == "__main__":
    main()
