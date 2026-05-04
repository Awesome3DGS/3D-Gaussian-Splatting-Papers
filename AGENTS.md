# 3D Gaussian Splatting Papers — AI Workflow

## 仓库定位

论文整理仓库，不是算法实现仓库。维护对象是 README 论文列表及 `abs/` 下每篇论文的摘要页。

## 项目文件结构

| 路径 | 用途 |
|------|------|
| `README.md` | 主列表（会议/期刊分类计数索引 + 归档时间计数索引 + 当前条目池） |
| `2024/*.md` `2025/*.md` `2026/*.md` | 按年份+会场的正式分类文档（归类结果主落点） |
| `abs/{arxiv_id}.md` | 论文摘要库（中英摘要，按 arXiv ID 唯一命名） |
| `archive/*.md` | 历史时间切片快照；不是当前主分类池，已进入正式分类的条目不应在此重复 |
| `tmp/` | 审计中间产物与证据索引工作区 |
| `scripts/` | 同步与审计脚本 |

## Roles

> ⚠️ `.ai/roles/paper-maintainer.md` 已删除。操作规范统一由 `.ai/skills/paper-maintain/SKILL.md` 承载。Worker 执行前读该 SKILL.md 获取完整操作规范。

## Orchestrator 核心约束

规划任务时须知：

- **归类与核证顺序不可互换**：先全量归类（`sync.py`），再逐条核查证据，证据不足才回退
- **补漏口径**：差集优先（README arXiv ID + abs 文件名 vs arXiv 查询），不要只看 README 顶部
- **archive 去重**：论文进入正式分类文档后，须从 archive 去重并修正 README 归档计数
- **计划文件**：每轮大批量同步后写 `.ai/plan/YYYY-MM-DD-{slug}.md` 记录目标、边界和结论

## Git 工作流

### 分支策略

- 所有操作在 `dev` 分支进行，dev 上可多次提交修复，不要求一步到位
- 合并到 `main` 前需整理提交历史（rebase/squash），梳理成下述三种规范提交
- **提交只在用户明确要求时执行**；Orchestrator 负责 commit，不做 push，用户自行 push
- `.ai/plan/` 在 dev 上正常提交，但 dev 不推远程；squash 到 main 时只含论文内容变更

### 三种提交类型

**1. 基础设施 / 工作流变更**

- 标题：`feat: ...` 或 `chore: ...`
- 必须单独提交，不与论文相关变更混合
- 可加 `Co-Authored-By`

**2. 新增论文**

- 标题：`Update README.md`
- 正文每行一条：`Add "论文标题"`，**顺序与 README 列表一致（即 arXiv ID 降序，最新条目在最上）**；多次抓取 squash 时同样按降序合并，不分批
- 提交后运行 `paper changelog`（即 `.ai/skills/paper-maintain/scripts/changelog.py`），将 `Changelog.md` 一并 amend 进提交（Changelog 由 commit message 的 Add 行顺序生成，因此 message 顺序变更后必须重生）
- 无 `Co-Authored-By`

**3. 补充信息并重新归档**

- 标题：`Update README.md`
- 正文每行一条：`Archive papers accepted to {VenueYear}`
- **所有被修改的 venue 文件都要有对应一行**，包括从 `Accepted` 兜底池重新归类到具体 venue 的情况
- 不更新 `Changelog.md`；无 `Co-Authored-By`

## 参考

- 历史同步与政策记录见 `.ai/plan/`
- 操作细则见 `.ai/skills/paper-maintain/SKILL.md`
