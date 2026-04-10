#!/usr/bin/env python

import re
import sys
import os


def reverse_paper_entries(input_file, output_file=None):
    if not os.path.isfile(input_file):
        print(f"❌ 找不到文件：{input_file}")
        return

    with open(input_file, "r", encoding="utf-8") as f:
        content = f.read()

    # 保留开头非论文部分（从文件开头到第一个条目前）
    split_match = re.search(r"(#### \[\d+\])", content)
    if not split_match:
        print("⚠️ 没有找到任何论文条目（#### [数字]）。")
        return

    prefix = content[: split_match.start()].rstrip()  # 文件开头的非论文部分
    paper_section = content[split_match.start() :]

    # 提取所有论文条目（#### [数字] 开头，直到下一个或结束）
    pattern = r"(#### \[\d+\][\s\S]*?)(?=#### \[\d+\]|$)"
    entries = re.findall(pattern, paper_section)

    cleaned_entries = [entry.strip() for entry in entries]
    reversed_entries = cleaned_entries[::-1]

    # 用单个空行拼接论文条目
    papers_text = "\n\n".join(reversed_entries)

    # 构建最终内容（头部 + 正文）
    if prefix:
        new_content = prefix + "\n\n" + papers_text
    else:
        new_content = papers_text

    # 如果没有指定输出文件，询问是否覆盖原文件
    if output_file is None:
        confirm = (
            input(
                f"⚠️ 你没有指定输出文件。是否要覆盖原文件 '{input_file}'？(y/N): "
            )
            .strip()
            .lower()
        )
        if confirm != "y":
            print("操作已取消。未写入任何文件。")
            return
        output_file = input_file

    with open(output_file, "w", encoding="utf-8") as f:
        f.write(new_content)

    print(f"✅ 论文顺序已反转并保存到：{output_file}")


if __name__ == "__main__":
    if len(sys.argv) < 2:
        print("用法：python reverse_md.py 输入文件 [输出文件]")
        sys.exit(1)

    input_file = sys.argv[1]
    output_file = sys.argv[2] if len(sys.argv) >= 3 else None

    reverse_paper_entries(input_file, output_file)
