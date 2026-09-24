# Changelog

## 1.1.0 - 2026-09-24

### Added
- Pre-experiment novelty scan before freezing the main experiment contract for new or materially changed claims.
- Baseline viability gate that distinguishes strict-protocol baselines from method-native literature comparisons and validates a representative runnable baseline path when practical.
- Evidence-based venue shortlisting before manuscript title/abstract/contribution and section framing.
- Repository TODO for future community-maintained journal/discipline guidance discovery and contribution.

### Changed
- Manuscript-stage literature search is now normally a delta audit rather than the first novelty discovery pass.
- Venue positioning now considers the paper's actual evidence, current official scope, recent close publications, contribution type, and experimental burden rather than prestige alone.
- Journal- and discipline-specific writing/figure preferences remain outside the core Skill until separately validated.

## 1.0.0 - 2026-09-15

### Added
- Session-resident research workflow core.
- Lazy loading for idea design, experiment execution, paper workflow, and context recovery.
- Completion-first execution policy with a narrow blocking whitelist.
- Scientific evidence hierarchy and validation/final-test separation.
- Compact three-part response contract.
- Long-project continuity and handoff procedure.

### Changed
- Reworked earlier gate-heavy workflow into nonblocking checkpoints and evidence safeguards.
- Removed repeated per-turn routing, response counters, and mandatory handoff checks.
- Removed recursive output-compression Skill calls; compression now lives in the core contract.
- Reduced instruction footprint and duplicate reference loading.
