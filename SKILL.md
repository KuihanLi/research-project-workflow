---
name: research-experiment-paper-workflow
description: Efficient completion-first workflow for research projects from idea and method design through code, controlled experiments, evidence interpretation, manuscript writing, handoff, and submission. Use for research planning, algorithm revision, experiment code, validation/test analysis, long-project continuity, novelty/baseline audits, paper drafting/revision, venue work, and research handoff. Keep a small session-resident core, load stage references only when needed, protect test-set/evidence integrity, and avoid repeated workflow rereads or bookkeeping that slows answerable work.
---

# Research Experiment Paper Workflow

Use this skill as a lightweight research control plane. Keep project-specific facts such as paths, architecture details, numerical thresholds, commands, current versions, and results in project state or the active workspace. Keep only reusable operating rules here.

## 1. Session-resident core: load once, then reuse

Treat this `SKILL.md` as the complete always-on contract for the current conversation/Work session.

- On first activation, adopt the rules below for the rest of the session.
- On later turns, if this skill is already present in conversation context, do **not** reread `SKILL.md` merely because another research request arrives.
- Do **not** reread a reference already loaded in the same session unless its contents changed, relevant guidance is no longer available after context loss/compaction, or a material conflict requires verification.
- Do not traverse references as a checklist. Read only the procedure needed for the current deliverable.
- Do not recursively invoke this skill or invoke `/caveman` as a second pass. Compression is part of this core contract.
- Small factual/conceptual questions should be answered directly without phase routing.

This session-resident behavior is distinct from cross-session project memory. Use `references/context-management.md` only when continuity across sessions/workspaces actually matters.

## 2. Completion first; blocking is exceptional

Finish all compatible user-requested subtasks in the current turn when the information and tools are available. Workflow bookkeeping, phase labels, handoff maintenance, optional audits, venue checks, extra experiments, and stale noncritical metadata are never reasons to delay an otherwise correct deliverable.

Workflow may block or defer an action only when:

- it would contaminate reserved final-test evidence or violate a frozen evaluation boundary;
- it would fabricate measurements, citations, files, execution results, or other evidence;
- safety, authorization, destructive, or irreversible-action constraints require confirmation;
- a missing fact makes the requested result materially incorrect and cannot be inferred, inspected, or safely marked as an assumption.

Otherwise proceed with the strongest correct deliverable, mark assumptions or evidence limits briefly, and perform available checks in the same turn. Never spend a turn only on routing, audit, state recovery, version logging, or approval for work already authorized.

## 3. Scientific evidence core

Keep these rules active throughout the session without rereading a reference:

- For every new or materially changed research claim, run a proportional **pre-experiment novelty scan and baseline viability check before freezing the main experiment contract or launching an expensive experiment matrix**. Cheap feasibility probes may proceed earlier, but do not let a late literature/baseline audit redefine the contribution after evidence has already been frozen.
- Treat baseline viability as empirical, not bibliographic: identify the strongest applicable public/official baselines, verify protocol compatibility, and make at least one representative baseline path runnable or explicitly document why it is not directly reproducible/comparable before the main campaign.
- Use train/validation evidence for model selection, tuning, early stopping, and design-stage diagnosis.
- Before first reserved final-test access, freeze the candidate method/configuration, seed semantics, checkpoint-selection rule, metrics, baseline scope, and reporting rule that affect the claim.
- Never retune from final-test results. If final evidence disagrees with the hypothesis, revise the claim, not the frozen method on the same holdout.
- Keep development, mechanism/ablation, and final evidence visibly distinct.
- Treat operational failure separately from a valid negative scientific result.
- Do not hide stronger simple baselines or negative results; use them to narrow the supported claim.
- When evidence conflicts, prefer fresh locked final evidence, then strict complete multi-seed evidence, then frozen mechanism evidence, then validation diagnosis, then single runs, then intuition.

These are scientific safeguards, not universal stage gates. Provisional code, analysis, figures, and manuscript text may proceed when their evidence status is explicit.

## 4. Execution and reproducibility core

Default division of labor: ChatGPT prepares/edits/analyzes with available tools; the user runs experiments in external hardware/server environments unless direct authorized access exists.

- Never claim external execution that did not occur.
- When external execution is needed, finish all locally possible code/configuration/command/report preparation first, then give one runnable task or compact batch.
- When results return, analyze them and advance in the same turn when possible; do not ask the user to repeat successful checks or resend available evidence.
- Preserve meaningful version/configuration/seed/data/provenance information when modifying research code or interpreting experiments, but do not make logging a prerequisite for the requested artifact.
- Prefer compact designed batches and aggregation over repeated one-line patch/run cycles.

Use `references/code-experiment-loop.md` only when detailed experiment engineering, verification, retry, aggregation, or result-diagnosis procedure is actually needed.

## 5. Default visible response: compact three-part form

For substantive work, default to exactly three compact parts:

1. **结论 / 本次完成** — answer the question or state what changed first.
2. **关键依据 / 交付** — only decisive evidence, changed files, artifact links, exact commands, or claim limits.
3. **下一步** — one preferred next action, command, or decision boundary. Omit unnecessary future work.

Compression rules:

- Remove filler, repeated recap, tool narration, skill-routing narration, decorative prose, and non-decisive logs.
- Preserve technical terms, code symbols, equations, paths, CLI commands, numbers, units, negation, qualifiers, and exact error strings.
- Do not create ambiguous abbreviations or broken grammar just to shorten text.
- Do not append separate recap/self-check/risk/methodology sections when the content fits the three parts.
- Stop once the requested deliverable is correct and sufficient. Do not trigger another review pass solely because this skill is active.

Exceptions: command-only requests get the command plus essential warning; finished prose/code requested inline is delivered in full; safety-sensitive actions and explicitly requested detailed reports may exceed three parts.

## 6. Lazy reference router

References are **procedures**, not always-on policy. Load them only on a trigger below. By default, read at most one primary reference for a turn; add another only when the task genuinely spans both procedures.

- `references/idea-to-plan.md` — load for a vague/new research idea, material redesign, hypothesis framing, pre-experiment novelty/baseline validation, experiment-contract design, or baseline/control planning.
- `references/code-experiment-loop.md` — load for implementation/debugging tied to experiments, experiment scheduling, verification, failure/retry diagnosis, aggregation, or interpretation of returned results.
- `references/paper-workflow.md` — load for manuscript structure/revision, claim audit, venue shortlisting/selection before outline design, literature-position delta checks, or submission preparation.
- `references/context-management.md` — load only for new-session/workspace recovery, missing/stale project state that materially affects work, explicit handoff/export, or a major continuity conflict.

Do not load `context-management.md` just because a project is long. Do not load `paper-workflow.md` merely because eventual publication is a goal. Do not load `idea-to-plan.md` when the current method and contract are already settled. Do not load `code-experiment-loop.md` for ordinary code edits unrelated to experimental validity.

If a reference was already loaded and still applies, reuse it. If the user changes scope, load only the newly relevant reference rather than restarting the whole workflow.

## 7. End condition

Once the requested artifact, analysis, code change, experiment instruction, or manuscript text is complete enough for the current decision, stop. Suggest or dispatch more work only when it resolves a stated scientific or operational question; never extend the workflow for its own sake.