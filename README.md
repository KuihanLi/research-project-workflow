# Research Project Workflow

> English | [简体中文](README.zh-CN.md)

A lightweight, completion-first workflow Skill for long-running research projects. It helps ChatGPT move from research idea and method design through implementation, controlled experiments, evidence interpretation, manuscript writing, handoff, and submission without turning the workflow itself into a bottleneck.

## Why this exists

Long research conversations often become slower over time because the assistant repeatedly reloads workflow instructions, re-routes the task, performs redundant audits, or treats bookkeeping as a gate before useful work. Research Project Workflow separates stable session rules from task-specific procedures:

- **Session-resident core:** load once, then reuse during the session.
- **Lazy procedure loading:** read only the reference needed for the current task.
- **Completion first:** finish answerable work instead of blocking on noncritical process steps.
- **Evidence discipline:** protect validation/test boundaries and avoid tuning on final-test evidence.
- **Compact output:** default to a three-part response focused on conclusion, evidence/deliverable, and next action.

## What it supports

- Research question and hypothesis framing
- Method and algorithm revision
- Baseline and control design
- Experiment implementation and debugging
- Multi-seed and ablation planning
- Validation/test evidence separation
- Failure diagnosis and result aggregation
- Manuscript drafting and revision
- Novelty and claim-evidence audits
- Venue and submission preparation
- Long-project handoff and continuity

## Repository structure

```text
research-project-workflow/
├── SKILL.md
├── agents/
│   └── openai.yaml
├── assets/
│   └── icon.svg
└── references/
    ├── idea-to-plan.md
    ├── code-experiment-loop.md
    ├── paper-workflow.md
    └── context-management.md
```

## Loading model

`SKILL.md` contains the always-on rules for the active session. The files under `references/` are procedures and should be loaded only when required.

| Task | Reference |
| --- | --- |
| New/vague research idea, major redesign, controls | `references/idea-to-plan.md` |
| Experiment code, runs, failures, aggregation, returned results | `references/code-experiment-loop.md` |
| Manuscript, claims, novelty, venue, submission | `references/paper-workflow.md` |
| New-session recovery, handoff, continuity conflicts | `references/context-management.md` |

The workflow explicitly avoids rereading references that are already available in the same session unless context was lost or the file changed.

## Core behavior

1. Complete all compatible user-requested work that can be done now.
2. Block only when proceeding would contaminate final evidence, fabricate evidence, violate safety/authorization constraints, or require a missing fact that cannot be safely inferred.
3. Use validation evidence for tuning and reserve final-test evidence for frozen evaluation.
4. Keep development evidence, mechanism evidence, and final evidence distinct.
5. Load at most one primary procedure reference by default.
6. Stop when the current deliverable is sufficient for the decision.

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
- No workflow-only blocking turns
- Lazy reference loading
- Strong experimental evidence boundaries
- Compact user-facing output

## License

MIT. See [LICENSE](LICENSE).

## Citation

If this workflow materially supports an academic project, you can cite the repository using the metadata in [`CITATION.cff`](CITATION.cff).
