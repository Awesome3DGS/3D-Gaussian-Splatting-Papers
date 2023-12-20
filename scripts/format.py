#!/usr/bin/env python

import re
import sys


def correct_markdown_numbering_simple(markdown_text):
    """
    A simpler version of the previous function. It corrects the numbering in a markdown file where each entry is
    preceded by a number in square brackets and starts with '####'.

    Parameters:
    markdown_text (str): The original markdown text with possibly incorrect numbering.

    Returns:
    str: The markdown text with corrected numbering.
    """
    lines = markdown_text.split("\n")
    counter = 0
    pattern = re.compile(r"####\s*\[\d*\]")
    for i in range(len(lines)):
        if pattern.match(lines[i]):
            lines[i] = pattern.sub(f"#### [{counter}]", lines[i])
            counter += 1
    return "\n".join(lines)


def main():
    if len(sys.argv) < 2:
        print("Usage: python script.py <input_filename> [output_filename]")
        sys.exit(1)

    input_filename = sys.argv[1]
    output_filename = sys.argv[2] if len(sys.argv) > 2 else None

    if not output_filename or output_filename == input_filename:
        confirm = input(f"Overwrite {input_filename}? (y/n): ")
        if confirm.lower() != "y":
            print("Operation cancelled.")
            sys.exit(1)
        output_filename = input_filename

    with open(input_filename, "r", encoding="utf-8") as file:
        content = file.read()

    corrected_content = correct_markdown_numbering_simple(content)

    with open(output_filename, "w", encoding="utf-8") as file:
        file.write(corrected_content)
    print(f"Corrected content written to {output_filename}")


if __name__ == "__main__":
    main()
