---
name: paper-maintain
description: 维护 3D Gaussian Splatting Papers 仓库的论文条目、摘要页、录用归类、计数同步与一致性校验。
metadata:
  short-description: 论文维护统一工作流
---

# paper-maintain

统一入口：`uv run .ai/skills/paper-maintain/scripts/paper.py`

```bash
alias paper='uv run .ai/skills/paper-maintain/scripts/paper.py'
```

以下命令均使用 `paper` 简写。

## When to Use

在以下场景使用本技能：

- 收录新论文（抓取、差集、下载元数据、生成 README/abs、校验）
- 补充现有条目（说明文案、Code 链接、机构信息）
- 录用核查与归档（check -> patch -> archive -> sync）
- 大批量同步后的一致性检查与修复（validate / sync）

## Workflow 1: 收录新论文

标准步骤：`fetch -> diff -> download -> curate -> validate`

1) 抓取新论文到 `tmp/fetch.json`

```bash
paper fetch --since <arxiv_id> --output tmp/fetch.json
```

2) 计算差集（README + abs 去重）

```bash
paper diff tmp/fetch.json --output tmp/diff.json
```

3) 下载补充信息（机构候选、note、code）

```bash
paper download --input tmp/diff.json --output tmp/download.json
```

4) 生成并写入 README + `abs/*.md`

```bash
paper curate --diff tmp/diff.json --download tmp/download.json
```

5) 结束前校验

```bash
paper validate
```

6) 提交（commit）后运行 changelog（**此步骤必须在 commit 之后执行**）

```bash
paper changelog
```

一键批处理（等价于 fetch->diff->download->curate->validate）：

```bash
paper run [--since <arxiv_id>] [--batch 20] [--skip-fetch]
```

## Workflow 2: 补充与归档

标准步骤：`patch -> check -> archive -> sync -> validate`

1) 先补元信息（可 dry-run，不落库）

```bash
paper patch [--limit N] [--write]
```

2) 录用信号核查，必要时直接 patch

```bash
paper check [--patch] [--yes]
```

3) 将已录用条目归入正式 venue 文档

```bash
paper archive [--dry-run]
```

4) 同步 README 计数索引与分类文档

```bash
paper sync
```

5) 收尾校验

```bash
paper validate
```

## Commands Reference

- `paper fetch --since <id> [--max 500] [--output <path>]`
  - 输入：arXiv API
  - 输出：`tmp/fetch.json`
- `paper diff [fetch_json|-] [--readme README.md] [--abs-dir abs] [--output <path>]`
  - 输入：`fetch.json` + 仓库现有条目
  - 输出：`tmp/diff.json`
- `paper download [--input tmp/diff.json] [--output tmp/download.json] [--workers 4] [--cache-dir tmp/affiliation_cache]`
  - 输入：`diff.json`
  - 输出：`download.json`
- `paper curate [--diff tmp/diff.json] [--download tmp/download.json] [--readme README.md] [--abs-dir abs] [--cache tmp/curate_cache.json] [--dry-run]`
  - 输入：`diff.json` + `download.json`
  - 输出：README + `abs/*.md` + `tmp/curate_report.json`
- `paper patch [--base-rev <rev>] [--baseline-rev <rev>] [--readme README.md] [--report /tmp/recent_sync_metadata_report.json] [--limit N] [--write]`
  - 输入：README + arXiv 页面
  - 输出：report；`--write` 时回写 README
- `paper check [checker args...] [--patch] [--yes] [--no-code] [--no-acceptance] [--patch-dry-run]`
  - 输入：`archive/*.md` + README + 网络信号
  - 输出：`tmp/archive-acceptance-*.{md,json}`；`--patch` 时调用 `acceptance_patch.py` 回写
- `paper archive [--dry-run]`
  - 输入：README + `archive/*.md`
  - 输出：按年份/会场归档文档，更新 README 归档计数
- `paper sync`
  - 输入：README formal note
  - 输出：`<year>/` 分类文档 + README 会议索引计数
- `paper validate [--readme README.md] [--abs-dir abs] [--fix] [--json]`
  - 输入：README + abs + 分类/归档文档
  - 输出：文本或 JSON 校验报告
- `paper changelog`
  - 输入：git log（提交历史中的 `Add "..."` 记录）
  - 输出：重建 `Changelog.md`
- `paper run [--since <id>] [--batch 20] [--skip-fetch] [--readme README.md] [--abs-dir abs]`
  - 输入：同 Workflow 1
  - 输出：同 Workflow 1

辅助命令（透传内部脚本）：

- `paper fill-affiliations ...` — 批量从 arXiv 页面抓取并回填 README 单位字段
- `paper clean-latex ...` — 将 abs/ 和 README 标题中的 LaTeX 标记转为 Unicode 纯文本（`--dry-run` 预览）
- `paper export-acceptance-audit ...` — 导出录用审计表（CSV/JSON），用于批量核查录用状态
- `paper add-abs ...` — 为 README 中缺少 `[[中英摘要]...]` 链接的条目补充链接
- `paper reverse ...` — 反转 venue 文档中的论文条目顺序
- `paper format ...` — 修正 venue 文档中不连续的条目编号

## Rules

### 1) 维护 SOP（顺序不可互换）

1. 先确认条目是否已存在：至少查 `README.md` + `abs/*.md` + 对应年份文档 + `archive/*.md`
2. 新增条目时，先补 `abs/{arxiv_id}.md`，再补 README 或对应分类文档
3. 若为 formal note（`🏆 Accepted to ...`），先 `paper sync` 做归类
4. 归类后再做证据核查；证据不足回退为待确认状态并重新同步
5. 若从 `archive` 提升到正式分类文档：必须 archive 去重并修正 README 归档计数
6. 每轮结束执行校验清单

### 2) README 维护规则

- 条目按时间倒序（通常按 arXiv ID 倒序）维护
- 新论文插入正确位置，不能只追加顶部或底部
- 插入后顺延编号，保持连续
- 一篇论文只能出现一次，前后都检查 arXiv ID 重复
- 字段格式遵循：标题 / `🏫 单位` / `🔗 链接`

### 3) abs 页面规则

- 每新增一条 README 条目，必须生成 `abs/{arxiv_id}.md`
- 至少包含：标题、英文摘要、中文摘要
- 中文摘要直接翻译英文摘要
- LaTeX 符号优先改写为普通文本，不机械保留公式

### 4) 单位字段规则

- 优先从 PDF 首页作者区提取；arXiv HTML 作者区干净时可直接取
- 按出现顺序保留并去重（去掉国家/城市/邮箱/脚注噪声）
- 缩写和别名人工核对（如 `HKUST(GZ)`、`CUHK`、`ETH Zürich`）
- 难提取时先留空，不阻塞整批流程

### 5) 补漏口径与优先级

- 补漏不要只看 README，必须联查 `abs/*.md`
- 主要查询口径：`3DGS`、`"3D Gaussian"`、`"Gaussian Splatting"`
- 优先做差集：`README arXiv ID + abs 文件名` vs arXiv 查询结果
- 不默认 README 顶部就是完整最新列表
- 优先级：论文条目 > abs 摘要页 > 单位 + Code 链接

### 6) 录用归类与核证（强制两步）

1. **先归类**：先把 formal note 条目归入对应年份文档（`paper sync`）
2. **再核查**：逐条核证；缺证据条目回退并再次同步

文案规范：

- 统一 `🏆 Accepted to <Venue Year>`
- 期刊也用 `Accepted to` 风格，不用 `Published in`
- `IEEE Transactions on Instrumentation and Measurement` 统一缩写为 `TIM`
- 证据索引 `note` 必须与分类文档 `📝 说明` 文案一致

### 7) 校验清单

每轮改动后至少检查：

- README 会议计数 vs 各分类文档实际条目数
- README 归档计数 vs `archive/*.md` 实际条目数
- 新增论文是否都生成对应 `abs/*.md`
- arXiv ID 唯一性
- 空白单位条数（知悉即可，不强制填满）
- 证据索引 `note` 与分类文档文案一致性

边界论文同步时额外检查：

- 边界论文是否已存在
- 所有比它新的论文是否已纳入
- 边界以下旧列表是否保持原状

### 8) 提交说明规范

见 `AGENTS.md` — Git 工作流 · 三种提交类型。要点强调：

- 新增论文（type 2）的 `Add` 行**必须按 README 顺序排列**（arXiv ID 降序，最新条目在最上），多次抓取 squash 后同样降序合并
- `Changelog.md` 由 commit message 的 `Add` 行顺序逐条生成（`paper changelog` → `.ai/skills/paper-maintain/scripts/changelog.py`），message 顺序若被 amend 调整，必须重新跑 `paper changelog` 再 amend

### 9) 工作习惯

- 不轻易删除历史内容，除非确认空白模板/重复条目/错误导入
- 回答”是否补完”先给判定口径，再给结论，避免混淆
