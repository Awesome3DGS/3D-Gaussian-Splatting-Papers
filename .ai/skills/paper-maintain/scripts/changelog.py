#!/usr/bin/env python

import subprocess
import re
from collections import defaultdict
from datetime import datetime


def parse_git_log(git_log):
    commits = git_log.split("commit ")[1:]
    changelog_entries = defaultdict(list)

    for commit in commits:
        date_raw = re.search(r"Date:\s+(.+)", commit).group(1).strip()
        date = datetime.strptime(date_raw, "%a %b %d %H:%M:%S %Y %z")
        date_formatted = date.strftime("%Y/%m/%d")
        if 'Add "' in commit:
            papers = re.findall(r'Add "(.+?)"', commit)
            for paper in papers:
                changelog_entries[date_formatted].append(f'Add "{paper}"')

    return changelog_entries


def write_changelog(changelog_entries, filename="Changelog.md"):
    with open(filename, "w") as file:
        file.write("# Changelog\n\n")
        for date in sorted(changelog_entries.keys(), reverse=True):
            file.write(f"### {date}\n\n")
            for entry in changelog_entries[date]:
                file.write(entry + "\n\n")


def main():
    try:
        kwargs = dict(check=True, text=True, capture_output=True)
        process = subprocess.run(["git", "log"], **kwargs)
        write_changelog(parse_git_log(process.stdout))
        print("Changelog generated successfully.")
    except subprocess.CalledProcessError as e:
        print(f"Error executing git log: {e}")


if __name__ == "__main__":
    main()
