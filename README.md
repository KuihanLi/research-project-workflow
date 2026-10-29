# Research Project Workflow

> English | [简体中文](README.zh-CN.md)

A lightweight, completion-first workflow Skill for long-running research projects. It helps ChatGPT move from research idea and method design through implementation, controlled experiments, evidence interpretation, manuscript writing, handoff, and submission without turning the workflow itself into a bottleneck.

## Why this exists

Long research conversations often become slower over time because the assistant repeatedly reloads workflow instructions, re-routes the task, performs redundant audits, or treats bookkeeping as a gate before useful work. Research Project Workflow separates stable session rules from task-specific procedures:

- **Session-resident core:** load once, then reuse during the session.
- **Lazy procedure loading:** read only the reference needed for the current task.
- **Completion first:** finish answerable work instead of blocking on noncritical process steps.
- **Evidence discipline:** protect validation/test boundaries and avoid tuning on final-test evidence.
- **Early novelty/baseline gate:** verify the claim landscape and strongest practical baselines before freezing the main experiment contract.
- **Venue-first manuscript framing:** shortlist target venues from the actual evidence and recent publication landscape before locking the manuscript frame.
- **Recoverable checkpoints:** package a minimal resumable workspace after major revisions/phase closures, explicit handoff requests, or reliably signaled context pressure.
- **Compact output:** default to a three-part response focused on conclusion, evidence/deliverable, and next action.

## What it supports

- Research question and hypothesis framing
- Method and algorithm revision
- Pre-experiment novelty search and baseline viability validation
- Baseline and control design
- Experiment implementation and debugging
- Multi-seed and ablation planning
- Validation/test evidence separation
- Failure diagnosis and result aggregation
- Manuscript drafting and revision
- Novelty and claim-evidence audits
- Evidence-based venue shortlisting before manuscript framing
- Venue and submission preparation
- Long-project handoff and continuity
- Minimal recoverable workspace packaging with `HANDOFF.md` and SHA-256 manifest verification

## Repository structure

```text
research-project-workflow/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── icon.svg
├── scripts/
│   └── package_handoff.py
└── references/
    ├── idea-to-plan.md
    ├── code-experiment-loop.md
    ├── paper-workflow.md
    ├── context-management.md
    └── handoff-workspace.md
```

## Loading model

`SKILL.md` contains the always-on rules for the active session. The files under `references/` are procedures and should be loaded only when required.

| Task | Reference |
| --- | --- |
| New/vague research idea, major redesign, controls | `references/idea-to-plan.md` |
| Experiment code, runs, failures, aggregation, returned results | `references/code-experiment-loop.md` |
| Manuscript, claims, novelty, venue, submission | `references/paper-workflow.md` |
| New-session recovery or confirmed context-pressure continuity | `references/context-management.md` |
| Explicit handoff, major-revision/phase checkpoint, resumable workspace export | `references/handoff-workspace.md` |

The workflow explicitly avoids rereading references that are already available in the same session unless context was lost or the file changed.

## Core behavior

1. Complete all compatible user-requested work that can be done now.
2. Before the main experiment contract is frozen, run a proportional novelty scan and validate the strongest practical strict-protocol baseline path.
3. Block only when proceeding would contaminate final evidence, fabricate evidence, violate safety/authorization constraints, or require a missing fact that cannot be safely inferred.
4. Use validation evidence for tuning and reserve final-test evidence for frozen evaluation.
5. Keep development evidence, mechanism evidence, and final evidence distinct.
6. Before locking manuscript framing, shortlist target venues from official scope, recent close work, and the evidence actually available.
7. After a major revision/meaningful phase close, create a minimal recoverable checkpoint when the workspace has a new authoritative state; also checkpoint on explicit request or reliable context-pressure signals.
8. Put handoff download links in the normal second response section rather than adding a fourth section.
9. Load at most one primary procedure reference by default.
10. Stop when the current deliverable is sufficient for the decision.

## Example prompts

```text
Use Research Project Workflow to turn this idea into a minimal experiment plan with baselines and success criteria.
```

```text
Use Research Project Workflow to diagnose these five-seed results and decide whether the method should be frozen or revised.
```

```text
Use Research Project Workflow to audit the claims in this manuscript against the evidence we actually have.
```

```text
Use Research Project Workflow to recover the current project state and continue from the latest valid experiment.
```

## Installation / migration

For source-based use, clone or download this repository and keep the directory structure intact. If your ChatGPT environment supports custom Skill import, package the repository contents as a Skill archive using the supported Skill packaging workflow, then import that archive.

Do not flatten `references/`, `agents/`, or `assets/`; `SKILL.md` references these paths directly.

## Design goals

- Small always-on instruction surface
- No per-turn phase scan
- No reply-count bookkeeping
- No recursive Skill invocation
- No workflow-only blocking turns except evidence/safety boundaries and confirmed continuity-risk checkpoints
- Lazy reference loading
- Strong experimental evidence boundaries
- Compact user-facing output

## Development and maintenance contract

Keep this Skill lightweight as it evolves. Every maintenance change should follow these rules:

1. **Audit before editing.** Start from a concrete user-observed failure or validated need. Inspect the current core, relevant reference, and existing scripts before changing anything; identify the root cause and check whether an existing rule already covers it.
2. **Classify the change.** Put stable, cross-project rules that must remain active in `SKILL.md`; put detailed task procedures in a lazily loaded `references/` file; keep project paths, results, thresholds, and temporary decisions in the project workspace or handoff. Do not promote project-specific facts into the reusable Skill.
3. **Make the smallest sufficient patch.** Prefer updating the nearest existing file over adding another Skill, reference, checklist, or script. Add a new component only when it represents a distinct reusable capability. Preserve verified behavior and avoid speculative features, duplicate gates, and parallel mechanisms.
4. **Protect execution efficiency.** Do not add per-turn phase scans, repeated reference reads, recursive Skill calls, turn counters, mandatory bookkeeping, or status-only steps. Reuse already available context. Complete the task first; process checks must not become a new source of blocking.
5. **Validate the affected behavior.** Run the Skill validator and relevant self-tests; add targeted regression tests for the changed path, including a representative real case when practical. Test the exact packaged artifact and documented import/extraction path. Check archive contents and hashes when identity matters. Never describe a ZIP as persistently installed, or a remote update as complete, until that state is actually verified.
6. **Release with traceable evidence.** Keep source, README, and changelog consistent; preserve upstream attribution and license boundaries. For repository changes, use a focused branch/PR, inspect the final diff, and merge only after relevant checks pass. Avoid unrelated refactors in the same release.
7. **Checkpoint major work.** After a major revision or meaningful phase closure, create a minimal recoverable workspace ZIP with `HANDOFF.md`. Trigger early for context pressure only when there is a reliable runtime signal or demonstrable compaction/loss. Include the download link in the second part of the normal three-part response; create a separate experiment evidence-chain file only when explicitly requested.
8. **Stop low-value branches.** Keep experimental features outside the core until real tasks demonstrate meaningful benefit. The journal-style and discipline-level figure-preference guide experiment is stopped; do not resume it without an explicit request.

### Definition of done

A change is complete when its user-visible problem is addressed, the relevant regression checks pass, the package/repository state is accurately verified, and the handoff contains enough information to resume any unfinished work. Do not add extra review loops once these conditions are met.

## License

MIT. See [LICENSE](LICENSE).

## Citation

If this workflow materially supports an academic project, you can cite the repository using the metadata in [`CITATION.cff`](CITATION.cff).
