# Project Snapshot

Last updated: 2026-04-14

## Overview

A curated bilingual repository of 3D Gaussian Splatting research papers organized by venue and year. The project maintains:
- **README.md**: Master list with **538+ entries** (as of 2026-04-13), organized by conference/journal, with acceptance classification counts and archive timeline
- **Year/venue documents** (`2024/`, `2025/`, `2026/` directories): 38+ classification docs across 3 years, venue-grouped by paper count (separate files for > 5 papers per venue)
- **Abstract archive** (`abs/` directory): **2,501+ bilingual** (English/Chinese) summaries, keyed by arXiv ID
- **Historical snapshots** (`archive/YYYYMM.md` files): 5 time-indexed snapshots (202407 / 202410 / 202501 / 202504 / 202507); active workflow now organizes papers into year/venue structure
- **Skill-based entry point** (`.ai/skills/paper-maintain/`): Unified script dispatch with `paper.py` subcommands for all paper maintenance workflows
- **Tests** (`tests/` directory): Unit tests for archive_patch.py covering venue mapping, acceptance parsing, and edge cases
- **Temporary workspace** (`tmp/` directory): Intermediate audit artifacts and evidence indices (gitignored)

Maintenance is Agent-assisted via the dotai workflow. AGENTS.md was restructured 2026-04-08 into a lean dispatch layer; execution rules consolidated into `.ai/skills/paper-maintain/SKILL.md` (2026-04-14).

## Archive Acceptance Verification Pipeline (2026-04-12 onwards)

New three-script pipeline for finding, validating, and migrating accepted papers:

### archive_acceptance_check.py (1450 lines)

**Dual-signal acceptance detection** from arXiv API + GitHub README, plus code discovery:

1. **arXiv API queries** (batch API):
   - Fetches `journal_ref` (published venue) and `comment` (author note) for each paper ID
   - Extracts acceptance keywords from both fields (standardized keywords: accepted, cvpr, eccv, etc.)
   - Records Kubernetes markdown + JSON reports with full evidence text

2. **GitHub README scanning** (conditional):
   - For papers with `Code` links, fetches raw README from repo (tries `HEAD` → `main` → `master`)
   - Searches for acceptance keywords (case-insensitive, with snippet context)
   - Records matched text and source URL

3. **Code discovery** (three routes, confidence-ranked):
   - **Route 1 (arxiv_comment)**: Parse GitHub URLs from author's arXiv comment field
   - **Route 2 (arxiv_html)**: Scrape arXiv abs page for GitHub links in `href` attributes
   - **Route 3 (github_search)**: Call GitHub Search API `q={arxiv_id}` for top-3 repos (requires GitHub token for rate limit)
   - Merged by confidence, deduplicated, sorted by source quality

4. **CLI and output**:
   - Command: `uv run scripts/archive_acceptance_check.py [--archive] [--readme] [--github-token=TOKEN] [--skip-github-search]`
   - Reports to `tmp/archive-acceptance-*.md` (Markdown) and `.json` (structured evidence)
   - Report format: signal source (arXiv only / GitHub only / both), evidence text + snippets, code discovery results

### archive_patch.py (519 lines)

**Write-back script** for acceptance marks and code links, with venue normalization and interaction confirmation:

1. **Venue mapping**:
   - Maintains `VENUE_GROUPS` dict with 14+ venues (CVPR, ECCV, ICCV, NeurIPS, SIGGRAPH, ICLR, AAAI, ACM MM, MICCAI, ICML, 3DV, WACV, ICRA, IROS, Eurographics, IEEE VR)
   - Keyword matching: case-insensitive substring search, word boundary matching to avoid ICML/ICMLA collisions
   - Fallback handling: unmapped venues marked `suspicious=True` for interaction confirmation

2. **Acceptance decision parsing** (priority: comment > journal_ref):
   - Extracts from comment: `accepted (to|at|in|@|by) {VENUE} {YEAR}`
   - Extracts from journal_ref: venue name + 4-digit year
   - Detects and filters out: `submitted`, `under review`, `extended version of`, `journal extension of`, `for possible publication`
   - Workshop detection: formats as `🏆 Accepted to {VENUE} {YEAR} {WORKSHOP_NAME} Workshop`
   - Output format: `🏆 Accepted to {ABBR} {YEAR}`

3. **Code URL write-back**:
   - Confidence ≥ 2 (`arxiv_comment` / `arxiv_html`): auto-written to `[Code]` → `[[Code](url)]`
   - Confidence = 1 (`github_search` only): marked suspicious, requires interaction confirmation
   - Skips entries that already have Code links or acceptance marks

4. **Interaction confirmation**:
   - For suspicious entries: print title + evidence + current parse, prompt `[y/s/q]`
   - `--yes` flag: skip all interaction, auto-accept
   - `--dry-run`: print planned changes without writing

5. **Evidence logging**:
   - Records all operations to `tmp/patch-evidence-*.json` with arXiv ID, file, field, old/new values, confidence, action

6. **Bug fixes** (applied via version 2026-04-13-archive-patch-bugfix.md):
   - Early-exit filtering for submitted/under review/extended version in `parse_comment_acceptance`
   - Workshop detection and name extraction in both comment and journal_ref paths
   - Journal_ref fallback when comment is empty (previously blocked)
   - Word boundary matching for VENUE_MAP to separate ICML from ICMLA
   - Fallback venue abbr only used in `suspicious=True` path (auto write-back requires VENUE_MAP hit)

### venue_archive.py (370 lines)

**Paper reorganization** from time-sliced archives to year/venue organization:

1. **Grouping logic**:
   - Parses `🏆 Accepted to {VENUE} {YEAR}` marks from all papers
   - Counts papers per venue+year combination
   - Threshold-based file assignment:
     - ≥ 6 papers → `archive/{YEAR}/{VENUE}.md`
     - < 6 papers → `archive/{YEAR}/Accepted.md` (catchall)

2. **File operations**:
   - Reads README.md + all `archive/YYYYMM.md` time-sliced files
   - Removes matched entries from source files and renumbers
   - Writes entries to target files in arXiv ID order (oldest first)
   - Creates year/venue directories as needed

3. **Known groupings** (2026-04-13):
   - 2026: CVPR (78), ICRA (17), ICLR (36), AAAI (30), 3DV (11), others → Accepted.md (34)
   - 2025: CVPR (157), ICCV (109), NeurIPS (35), SIGGRAPH (35), ICRA (23), others → Accepted.md (89)
   - 2024: ECCV (86), NeurIPS (70), CVPR (67), SIGGRAPH (27), others → Accepted.md (28)

4. **CLI**:
   - `--dry-run` flag: print planned moves without modifying files

## Paper Curation Workflow

**Three mandatory, ordered steps** for accepting papers (unchanged since 2026-04-08):

1. **Classify**: Execute `scripts/sync.py` to route papers with formal acceptance notes from README into year/venue documents
2. **Verify**: Check evidence for each classified paper; if evidence is unavailable or stale, move paper back to pending status and resync
3. **Archive cleanup**: When papers are promoted from `archive/` into official year/venue docs, remove duplicates and correct README archive counts

**Acceptance evidence requirements** (formalized 2026-03-17):
- Per-paper evidence record required before assigning venue note
- Evidence fields: arxiv_id, title, claimed_note, evidence_type, evidence_url, checked_at, decision, comments
- Accepted notes must match exactly: `🏆 Accepted to <Venue Year>` (journals and conferences use same format, not "Published in")
- Special venues use short codes: e.g., `IEEE Transactions on Instrumentation and Measurement` → `TIM 2026`
- Evidence indices stored in `tmp/current-classified-evidence-index-*.{md,json}` with notes synchronized to actual classification docs

## Paper Entry Maintenance

Papers must be verified for existence before adding:
- Check: README.md + abs/*.md + year/venue docs + archive/*.md
- New entries require corresponding `abs/{arxiv_id}.md` with bilingual summary
- Affiliations extracted from arXiv HTML author blocks, PDF first pages, or LaTeX source bundles; left blank if unreliable
- All papers inserted in reverse-chronological order (by arXiv ID), then renumbered contiguously
- arXiv IDs verified for uniqueness across all storage locations

## ArXiv Synchronization

**Last sync completed: 2026-03-11**
- **Boundary at sync time**: `arXiv:2601.22990`
- **Current README top entry**: `arXiv:2604.08509` (as of 2026-04-13, incremental additions after large sync)
- **Coverage**: Papers from `2601.*` through `2604.08509` confirmed in README; older entries preserved
- **Queries used**: `3DGS`, `"3D Gaussian"`, `"Gaussian Splatting"` — all three needed; none is a superset
- **Methods**: arXiv HTML author blocks (primary) → PDF first-page parsing (fallback) → LaTeX source bundles (special cases)

## Sync Pipeline (2026-04-14)

Five-stage scripted pipeline for incremental paper sync via unified skill:

```
paper fetch → paper diff → paper curate → paper sync → paper validate
```

| Stage | Command | Input | Output |
|-------|---------|-------|--------|
| `fetch` | `paper fetch --since <id>` | arXiv Atom API | `tmp/fetch.json` |
| `diff` | `paper diff tmp/fetch.json` | fetch.json + README + abs/ | `tmp/diff.json` |
| `curate` | `paper curate` (AI Worker prompt) | diff.json + download.json | README entries + abs/*.md |
| `sync` | `paper sync` | README formal notes | year/venue docs + README index |
| `validate` | `paper validate` | full repo | PASS/FAIL report |

All scripts consolidated under `.ai/skills/paper-maintain/scripts/` as internal modules. Skill dispatcher (`paper.py`) handles argument parsing and subprocess dispatch. Scripts are stdlib-only (no external deps). `validate` exits non-zero on any ERROR — hard gate before commit.

## Maintenance Documentation

**Skill reorganization (2026-04-14)**:
- Consolidated `.ai/roles/paper-maintainer.md` and `scripts/` into unified skill `.ai/skills/paper-maintain/`
- Skill entry: `python3 .ai/skills/paper-maintain/scripts/paper.py` with subcommands
- Subcommands: `fetch`, `diff`, `download`, `curate`, `patch`, `check`, `archive`, `sync`, `validate`, `run`, `changelog`
- All execution rules (SOP, README, abs, affiliations, acceptance, validation) now live in `.ai/skills/paper-maintain/SKILL.md`
- `changelog` integration (2026-04-14): callable via `paper changelog` subcommand; Workflow 1 step 6 documents running after commit. (2026-05-04: 脚本由根 `scripts/changelog.py` 迁入 `.ai/skills/paper-maintain/scripts/changelog.py`，与其它子命令统一在 skill 内)

**AGENTS.md structure (2026-04-08)**:
- Lean dispatch layer (38 lines); full execution rules now in skill SKILL.md
- AGENTS.md contains: repo overview, file structure table, Orchestrator constraints, git workflow

**Git workflow**:
- Daily work on `dev` branch; dev branch not pushed to remote
- Merges to `main` use squash commits containing only paper content changes
- `.ai/plan/` committed on dev during agent work; plan files never reach remote due to squash-only merge
- `dotai snapshot` run before closing a dev cycle to absorb plan knowledge into memory
- Commit title format: "Update {filename}.md" for paper changes, "chore: ..." for infrastructure

## Historical Record Pruning (2026-03-23)

Cleaned up `.ai/plan/` after consolidating repetitive batch logs:
- Removed one-off execution logs (per-paper fix records, batch-level evidence rollups, classification hotfixes)
- Consolidated 84 batch files into 4 rollup files (older-accepted, older-pending, recent-pending, formal-evidence)
- Retained only long-term policy/reference docs: baseline sync, evidence policy, acceptance-note policy, project overview, plan rollups
- Post-pruning file count: 46 files (down from 84)
- Future paper history remains in target year/venue docs, not in plan logs

## Supported Venues (as of 2026-04-13)

| Year | Venues (paper counts) |
|------|----------------------|
| 2024 | ICLR(2), CVPR(67), ECCV(86), ACM MM(10), MICCAI(8), SIGGRAPH(27), NeurIPS(70), ICML(4), BMVC(8), CoRL(6), IROS(9), others(27) |
| 2025 | 3DV(21), WACV(16), AAAI(28), ICLR(42), ICASSP(5), ICRA(23), CVPR(157), ICCV(109), ACM MM(22), MICCAI(7), SIGGRAPH(35), ICML(7), IROS(18), ICME(8), ICIP(4), BMVC(3), NeurIPS(35), RAL(10), TPAMI(8), TVCG(5), others(99) |
| 2026 | 3DV(11), WACV(4), AAAI(30), ICLR(36), ICASSP(2), ICRA(17), CVPR(78), others(34) |

- **Archive snapshots**: 202407(174), 202410(98), 202501(186), 202504(196), 202507(204)
- **Survey Papers**: 12

