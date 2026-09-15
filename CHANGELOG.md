# Changelog

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
