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

| Role | 文件 | 负责 |
|------|------|------|
| `paper-maintainer` | `.ai/roles/paper-maintainer.md` | 论文条目增删改、摘要页维护、归类核证、计数同步 |

Worker 执行前读角色文件获取完整操作规范。

## Orchestrator 核心约束

规划任务时须知：

- **归类与核证顺序不可互换**：先全量归类（`sync.py`），再逐条核查证据，证据不足才回退
- **补漏口径**：差集优先（README arXiv ID + abs 文件名 vs arXiv 查询），不要只看 README 顶部
- **archive 去重**：论文进入正式分类文档后，须从 archive 去重并修正 README 归档计数
- **计划文件**：每轮大批量同步后写 `.ai/plan/YYYY-MM-DD-{slug}.md` 记录目标、边界和结论

## Git 工作流

- 日常开发在 `dev` 分支，合并到 `main` 前需压缩（squash）成一个提交
- **提交只在用户明确要求时执行**
- 提交标题格式：`Update README.md`（论文内容变更）或 `chore: ...` / `feat: ...`（基础设施变更）
- 正文逐条列出新增论文：`Add "论文标题"`
- 论文提交无 `Co-Authored-By`；基础设施提交可加
- 论文提交前运行 `python scripts/changelog.py`，将 `Changelog.md` 一并 amend 进提交
- 归档（`python scripts/sync.py`）只在用户明确要求时执行，单独提交，不与论文入库提交混合
- Orchestrator 负责 commit，不做 push；用户自行 push
- `.ai/plan/` 在 dev 上正常提交，但 dev 不推远程；squash 到 main 时只含论文内容变更，plan 文件实际上永远不会到达远程；关闭 dev 周期前运行 `dotai snapshot` 将 plan 知识吸收进 memory

## 参考

- 历史同步与政策记录见 `.ai/plan/`
- 操作细则见 `.ai/roles/paper-maintainer.md`
