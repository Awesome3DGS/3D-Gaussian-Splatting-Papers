# 打开并逐行读取 README.md 文件
with open('README.md', 'r', encoding='utf-8') as file:
    lines = file.readlines()

# 处理每一行
modified_lines = []
for line in lines:
    if line.startswith("- **🔗 链接**："):
        # 找到 arXiv ID 并构造新的链接
        arxiv_id = line.split('arXiv:')[1].split(']')[0]
        new_link = f"[[中英摘要](./abs/{arxiv_id}.md)] "

        # 替换原链接
        line = line.replace('[[arXiv:', new_link + '[[arXiv:')

    modified_lines.append(line)

# 将修改后的内容写回 README.md
with open('README.md', 'w', encoding='utf-8') as file:
    file.writelines(modified_lines)

