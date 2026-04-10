# Role: Paper Maintainer

Handles paper entry maintenance for the 3D Gaussian Splatting Papers repository.
Tasks: add/update entries in README, create abs pages, classify accepted papers, verify evidence, sync counts.

---

## 维护 SOP

执行顺序固定，不要互换：

1. 确认条目是否已存在：至少查 `README.md` + `abs/*.md` + 对应年份分类文档 + `archive/*.md`
2. 新增条目：先补 `abs/{arxiv_id}.md`，再补 `README.md` 或对应分类文档
3. 如果是 formal note（`🏆 Accepted to ...`）：先执行 `python scripts/sync.py` 做归类
4. 归类后做证据核查；证据不足回退到待确认状态并重新同步
5. 若从 `archive` 提升到正式分类文档：从 `archive` 去重 + 修正 `README` 归档计数
6. 收尾校验（见下方"校验清单"）

---

## README 维护规则

- 列表按时间倒序（通常按 arXiv ID 倒序）维护
- 新论文插入正确位置，不能只追加顶部或底部
- 插入后重新顺延所有编号，保证连续
- 一篇论文只允许出现一次；操作前后都要检查 arXiv ID 是否重复
- 常用字段格式：
  - 标题
  - `🏫 单位`
  - `🔗 链接`

## abs 页面维护规则

- 每新增一条 README 条目，同步创建 `abs/{arxiv_id}.md`
- 至少包含：论文标题、英文摘要、中文摘要
- 中文摘要直接翻译英文摘要
- 摘要中的 LaTeX 符号优先改写为普通文本，不要机械保留公式写法

## 单位字段规则

- 优先从论文 PDF 首页标题/作者区提取；arXiv HTML 作者区足够干净时也可直接取
- 按论文中出现顺序保留，去重（保留机构，不保留重复国家/城市/邮箱/脚注标记）
- 缩写和别名需人工核对，例如 `HKUST(GZ)`、`CUHK`、`ETH Zürich`
- 单位提取困难或多次失败时，先留空，不要卡住整批进度

## 补漏口径

- 不只看 `README.md`，同时看 `abs/*.md`；`abs` 已存在说明该论文可能已在别处纳入
- 当前仓库使用的 arXiv 查询主要有三组：`3DGS`、`"3D Gaussian"`、`"Gaussian Splatting"`
- 补漏时优先做差集：当前 README 中的 arXiv ID + `abs/*.md` 文件名 vs arXiv 查询结果
- 不要默认 README 顶部是完整最新列表；历史上出现过空白模板条目、顺序漂移和中途漏插

## 补漏优先级

1. 论文条目本身
2. abs 摘要页
3. 单位 + Code 链接

对于单位难提取的论文，先导入条目和摘要，不要因单位卡住整批进度。

---

## 录用归类与核证流程（强制两步）

1. **先归类**：把 `README` 中带 formal 录用说明的条目归类到对应年份文档，运行 `python scripts/sync.py`
2. **再核查**：逐条核查证据；缺少可复核证据的条目回退到待确认状态并重新同步

不要等"全量核查完成"才归类，应先完成整批归类，再做核证与回退。

录用说明文案规范：
- 统一使用 `🏆 Accepted to <Venue Year>`
- 期刊也用 `Accepted to` 风格，不用 `Published in`
- `IEEE Transactions on Instrumentation and Measurement` 统一写作 `TIM 2026`

证据索引（`tmp/current-classified-evidence-index-*.{md,json}`）的 `note` 字段必须与分类文档中说明文案保持一致。

---

## 校验清单

每轮改动后至少检查：

- [ ] `README` 会议计数 vs 各分类文档实际条目数
- [ ] `README` 归档计数 vs `archive/*.md` 实际条目数
- [ ] 新增论文是否都生成了对应 `abs/*.md`
- [ ] arXiv ID 唯一性（无重复）
- [ ] 空白单位条数（知悉即可，不必强制填满）
- [ ] 证据索引 `note` 与分类文档 `📝 说明` 文案一致性

如果是按某篇边界论文做同步，额外确认：
- [ ] 边界论文本身是否已存在
- [ ] 所有比它新的论文是否已纳入
- [ ] 边界以下旧列表是否保持原状

---

## 提交说明格式

**提交只在用户明确要求时执行。**

标题：`Update README.md`

正文按 README 当前顺序列出新增论文：
```
Add "论文标题"
```

无 `Co-Authored-By` 行。

提交前运行 `python scripts/changelog.py` 更新 `Changelog.md`，然后 `git add Changelog.md && git commit --amend --no-edit` 合并进提交。

如果用户要求"比某篇边界论文更新的所有文章"，以该论文为分界重新生成，不要用 `HEAD` 差集偷换口径。

---

## 工作习惯

- 大批量同步、补漏、修编号后，及时把过程和结论写入 `.ai/plan/*.md`
- 不要轻易删除历史内容，除非确认是空白模板、重复条目或错误导入
- 遇到"是不是已经补完"类问题，先给口径，再给结论；不要混淆"当前策略下补完"和"绝对无遗漏"

---

## 脚本参考

### 同步流水线（`fetch → diff → curate → sync → validate`）

| 阶段 | 脚本 / 执行者 | 用途 |
|------|--------------|------|
| `fetch` | `scripts/fetch.py --since <id>` | arXiv API 拉取新论文原始数据 → `tmp/fetch.json` |
| `diff` | `scripts/diff.py` | 计算差集，排除已有条目 → `tmp/diff.json` |
| `curate` | AI Worker（本角色） | 读 diff.json，写 README 条目 + abs/*.md（含中文翻译） |
| `sync` | `scripts/sync.py` | README formal note → 年份分类文档 + README 计数索引同步 |
| `validate` | `scripts/validate.py` | 收尾一致性校验，全部 PASS 才可提交 |

### 辅助工具

| 脚本 | 用途 |
|------|------|
| `scripts/export_acceptance_audit.py` | 导出接受状态审计视图 |
| `scripts/fill_affiliations.py` | 单位提取辅助（不能盲信输出） |
