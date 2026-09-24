# TODO

## Community-maintained journal and discipline guidance

This roadmap is intentionally non-binding. Do not make these items part of the core Skill until the extraction and validation workflow has been tested on real manuscripts.

- Add a GitHub-first discovery step for journal-specific writing guides and discipline-specific figure-preference guides.
  - Search the repository / configured GitHub source for an existing guide before extracting a new one.
  - Reuse a guide only when its journal identity, source provenance, and freshness are adequate for the current task.
- If no suitable guide exists, extract a candidate from:
  - current official scope and author instructions;
  - recent close papers, normally emphasizing roughly the last 24--36 months;
  - representative influential/high-impact papers where useful for stable stylistic patterns.
- Keep newly extracted guides outside the core Skill until they are tested on real drafting tasks.
- Encourage users who validate a useful guide to contribute it back by PR so later users do not repeat the same extraction work.
- Later define, but do not yet lock:
  - journal aliases and naming conventions (for example ITJ vs IoT-J);
  - filename/directory conventions;
  - extraction date and source/provenance manifest;
  - guide versioning;
  - minimum evidence/sample requirements;
  - review and deprecation criteria.

## Discipline-level scientific figure preferences

- Explore evidence-backed plotting and figure preferences by discipline/subfield.
- Separate scientific-question fit from visual convention: do not hard-code assumptions such as “machine learning always needs a confusion matrix.”
- Prefer guides that explain when a figure type is evidentially useful (ablation, robustness, uncertainty, error structure, trade-off, etc.), not merely visually common.
- Keep this guidance lazy-loaded and outside the session-resident core.
