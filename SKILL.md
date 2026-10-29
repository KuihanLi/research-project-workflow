---
name: research-experiment-paper-workflow
description: Completion-first, evidence-protected research workflow supporting parallel IDEA branches, evolving or reverse-mined innovations, competitive mechanism hypotheses, conditional deployment claims, code/experiment loops, paper drafting, and recoverable handoffs. Use when planning, testing, pivoting, comparing, merging or stopping research ideas, interpreting anomalies and negative results, designing controlled experiments, validating novelty/baselines, or maintaining long-running projects.
---

# Research Experiment Paper Workflow

This skill is a **lightweight research control plane**, not a mandatory linear pipeline. Research may proceed forward from an IDEA, backward from results, and concurrently across several hypotheses. Project-specific paths, measurements, thresholds, run IDs, and current branch statuses live in the project workspace, **not** in this skill.

## 1. Load once; completion first

- Treat this file as the session-resident core. Do not reread it or an already available reference on every turn; load only a procedure relevant to the active task.
- Finish compatible requested work in this turn. Do not stall on phase routing, updating registries, optional literature searches, or producing a handoff.
- Block only to protect reserved-test evidence, prevent fabricated evidence, respect safety/authorization/destructive-action boundaries, or resolve a genuinely indispensable missing fact.
- Answer simple questions directly. Do not recursively invoke this skill or external compression workflows.
- When a reliably signaled compaction/context issue threatens continuity, finish the atomic operation and checkpoint per `references/context-management.md`; never invent a context percentage.

## 2. Parallel IDEA and evolving innovation contract

- **No single IDEA is automatically the project's sole main line.** Maintain a lightweight portfolio of compatible, competing, auxiliary, diagnostic, or conditional-deployment IDEA branches as needed. Run independent low-cost tests in parallel when resource and evidence boundaries permit; sequence only actual dependencies.
- Accept three equally legitimate discovery directions from existing experiments: **A. conditional effect / result re-mining**, **B. anomaly fingerprint -> competing mechanism explanations**, and **C. explicit, operationally identifiable deployment domains**. They can generate new branches even if the original IDEA fails or succeeds.
- Each material IDEA or claim revision gets a stable `idea_id`, a `claim_version`, its parent/evidence origin, distinctive technical action, competing explanations or alternatives, fair strong baseline, falsifying criterion, and current evidence class. A research hypothesis is provisional, not a conclusion.
- **Revise, do not erase:** retain failed or superseded ideas and negative evidence. A new mechanism, primary metric, target task/domain, or condition chosen after examining results becomes a new claim version with exploratory provenance, not an invisible rewrite of the old frozen hypothesis.
- Share reusable datasets, components, controls, and evidence across branches with source identifiers; do not duplicate runs or equate shared observations with independent replications. Choose a primary paper story only when evidence and venue positioning justify it; branches may later merge, narrow, pause, or close.
- Prefer the **cheapest decisive discriminating test** over endless separate tuning campaigns. A finding becomes a method innovation only if it entails a concrete technical difference and survives fair simple/strong baselines and relevant controls.

Load `references/idea-portfolio-and-reverse-innovation.md` when a user requests multiple IDEA lines, new innovations mined from old results, anomaly-to-mechanism inference, branch arbitration/merging, claim revision, or conditional deployment claims. Use `references/idea-to-plan.md` for a new idea's implementation/experiment contract. Do not load both unless the task actually needs both.

## 3. Evidence and final-test protection across *all* branches

- Classify observations as **development/tuning**, **diagnostic/mechanism**, or **locked independent final confirmation**, with provenance and genuinely independent unit (subject/source/session/site/etc.). Keep operational failures separate from valid scientific negatives.
- The same held-out evaluation can be contaminated **project-wide**: looking at it to select a branch, metric, subgroup, applicability boundary, architecture, or failure rescue makes later claims built from that choice exploratory on that holdout. Creating a new branch name or code commit does **not** reset its independence.
- Use training/validation for exploration, branch selection, tuning, and exploratory anomaly analysis. Before a reserved final confirmation, freeze the selected claim version, method/config, data/split/seed semantics, checkpoint rule, primary and failure metrics, eligible domain and baseline/reporting plan. No retuning or post-hoc domain picking on that final set.
- If final results inspire a new IDEA, preserve the old result as discovery evidence; require a genuinely independent confirmation source for the revised claim or explicitly label the finding exploratory. Cross-branch multiple comparisons, non-independent windows/records, and repeated peeking must not be reported as independent proof.
- A claim about conditional overall benefit specifies a **pre-recognizable, deployable domain** (never test labels, per-sample test losses, or an oracle selector), coverage, paired average effect and uncertainty, important worst-subgroup failures, resource cost, and untested out-of-domain limits. Domain-average improvement does **not** imply every individual or condition improves.
- For a new or materially changed claim, perform a proportional novelty scan and **practical baseline-viability check** before locking an expensive main campaign. Cheap feasibility probes may precede this gate. An established formula or unusual error pattern alone is not a novelty or causality claim.
- Prefer fresh locked independent evidence > strict complete multi-seed evidence > controlled mechanism evidence > validation diagnosis > single-run impressions. Preserve contradictory cases and stronger simple baselines.

## 4. Execution, branch scheduling and paper consistency

- Prepare/edit/analyze with available tools; do not claim to have executed external server/GPU/hardware runs without access. Supply compact runnable commands and collection instructions for external tasks, avoiding duplicate launches for still-pending identical runs.
- Track experiment identity at least by `idea_id`, `claim_version`, purpose, code/config/data/split/seed, result location, status, and evaluation class when this affects interpretation. Changing the method or metric creates a new condition, not a silent replacement.
- Prioritize parallel work by decision value, cost and dependency: cheaply kill weak ideas, protect strong controls, and allocate independent confirmations deliberately. Do not require an oversized experiment matrix just because multiple branches exist.
- Manuscript contributions must be tied to surviving claim versions, their actual tests, target domains, limitations, and strongest comparisons. Never combine the best post-hoc slice of each branch as one pre-confirmed universal method.
- Handoff/checkpoints only on explicit request, meaningful major revision/phase closure, or reliably confirmed continuity pressure. Where several branches materially matter, preserve their statuses and evidence boundaries in the minimal handoff; do not archive all raw runs by default.

## 5. User-facing delivery

For substantive tasks, default to three compact sections: **结论 / 本次完成**, **关键依据 / 交付**, **下一步**. A portfolio comparison can use one compact table when requested or decision-relevant. Deliver finished code/docs/plans in full even if longer. Avoid verbose workflow narration or separate audit summaries. Put actual handoff links in section two.

## 6. Lazy reference router

- `references/idea-portfolio-and-reverse-innovation.md` — parallel IDEA management; old-results re-mining; anomaly mechanisms; conditional domains; claim pivots/merges/arbitration.
- `references/idea-to-plan.md` — a new/materially revised branch's claim, novelty and baseline viability, design and freezing of a main experiment contract.
- `references/code-experiment-loop.md` — experiment code, controls, launch/return, aggregation, abnormal results, retry and shared run identity.
- `references/paper-workflow.md` — manuscript, venue, claim/evidence and submission work.
- `references/context-management.md` — new-session state recovery, material conflict, or reliably observed continuity pressure.
- `references/handoff-workspace.md` — explicit handoff/export, authoritative major phase/revision checkpoint, or verified continuity pressure.

Read at most one primary reference by default. Load another only when its procedure is actually needed; previously loaded applicable guidance should be reused. Never start a linear phase scan just because a request mentions a research topic.

## 7. Stop condition

Stop once the requested artifact or scientific decision is supported sufficiently. A branch can **advance**, **narrow**, **merge**, **pause**, **be contradicted**, or **close**. Do not manufacture more IDEA work to keep the workflow busy.
