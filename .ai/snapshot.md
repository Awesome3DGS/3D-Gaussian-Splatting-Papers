# Project Snapshot

Last updated: 2026-04-08

## Overview

A curated bilingual repository of 3D Gaussian Splatting research papers organized by venue and year. The project maintains:
- **README.md**: Master list with **538 entries** (as of 2026-04-08), organized by conference/journal, with acceptance classification counts and archive timeline
- **Year/venue documents** (`2024/`, `2025/`, `2026/` directories): 38 classification docs across 3 years
- **Abstract archive** (`abs/` directory): **2,501 bilingual** (English/Chinese) summaries, keyed by arXiv ID
- **Historical snapshots** (`archive/` directory): 5 time-indexed snapshots (202407 / 202410 / 202501 / 202504 / 202507); not active classification storage
- **Scripts** (`scripts/` directory): Automation for syncing acceptance classifications, auditing evidence, and extracting affiliations
- **Temporary workspace** (`tmp/` directory): Intermediate audit artifacts and evidence indices (gitignored)

Maintenance is Agent-assisted via the dotai workflow. AGENTS.md was restructured 2026-04-08 into a lean dispatch layer; full execution rules live in `.ai/roles/paper-maintainer.md`.

## Paper Curation Workflow

**Three mandatory, ordered steps** for accepting papers:
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
- **Current README top entry**: `arXiv:2603.09718` (GSStream — streamed after the large sync via incremental additions)
- **Coverage**: Papers from `2601.*` through `2603.09718` confirmed in README; older entries preserved
- **Queries used**: `3DGS`, `"3D Gaussian"`, `"Gaussian Splatting"` — all three needed; none is a superset
- **Methods**: arXiv HTML author blocks (primary) → PDF first-page parsing (fallback) → LaTeX source bundles (special cases)
- **Affiliations**: Filled for the batch; 3 papers left blank due to unavailable source data
- **Abstract translations**: All new entries have bilingual summaries; Chinese derived from English, LaTeX symbols rewritten as plain text

## Sync Pipeline (2026-04-08)

Five-stage scripted pipeline for incremental paper sync:

```
fetch → diff → curate → sync → validate
```

| Stage | Script / Role | Input | Output |
|-------|--------------|-------|--------|
| `fetch` | `scripts/fetch.py --since <id>` | arXiv Atom API | `tmp/fetch.json` |
| `diff` | `scripts/diff.py` | fetch.json + README + abs/ | `tmp/diff.json` |
| `curate` | AI Worker (paper-maintainer) | diff.json | README entries + abs/*.md |
| `sync` | `scripts/sync.py` | README | year/venue docs + README index |
| `validate` | `scripts/validate.py` | full repo | PASS/FAIL report |

Scripts are stdlib-only (no external deps). `validate` exits non-zero on any ERROR — hard gate before commit.

## Maintenance Documentation

**AGENTS.md restructure (2026-04-08)**:
- Split into lean dispatch layer (38 lines) + full execution rules in `.ai/roles/paper-maintainer.md`
- AGENTS.md now contains: repo overview, file structure table, role registry, Orchestrator constraints, git workflow
- `paper-maintainer` is the only defined role; covers all paper entry tasks

**Git workflow**:
- Daily work on `dev` branch; dev branch not pushed to remote
- Merges to `main` use squash commits containing only paper content changes
- `.ai/plan/` committed on dev during agent work; plan files never reach remote due to squash-only merge
- `dotai snapshot` run before closing a dev cycle to absorb plan knowledge into memory
- Commit title format: "Update {filename}.md" for paper changes, "chore: ..." for infrastructure
- Orchestrator handles commits; user pushes

## Historical Record Pruning (2026-03-23)

Cleaned up `.ai/plan/` after consolidating repetitive batch logs:
- Removed one-off execution logs (per-paper fix records, batch-level evidence rollups, classification hotfixes)
- Consolidated 84 batch files into 4 rollup files (older-accepted, older-pending, recent-pending, formal-evidence)
- Retained only long-term policy/reference docs: baseline sync, evidence policy, acceptance-note policy, project overview, plan rollups
- Post-pruning file count: 46 files (down from 84)
- Future paper history remains in target year/venue docs, not in plan logs

## Supported Venues (as of 2026-04-08)

| Year | Venues (paper counts) |
|------|----------------------|
| 2024 | ICLR(2), CVPR(67), ECCV(86), ACM MM(10), MICCAI(8), SIGGRAPH(27), NeurIPS(70), ICML(4), BMVC(8), CoRL(6), IROS(9), others(27) |
| 2025 | 3DV(21), WACV(16), AAAI(28), ICLR(42), ICASSP(5), ICRA(23), CVPR(157), ICCV(109), ACM MM(22), MICCAI(7), SIGGRAPH(35), ICML(7), IROS(18), ICME(8), ICIP(4), BMVC(3), NeurIPS(35), others(99) |
| 2026 | 3DV(5), WACV(4), AAAI(22), ICLR(26), ICASSP(2), ICRA(5), CVPR(23), others(11) |

- **Archive snapshots**: 202407(176), 202410(99), 202501(196), 202504(203), 202507(216)
- **Survey Papers**: 12
- **Special venue alias**: `IEEE Transactions on Instrumentation and Measurement` → `TIM 2026`
