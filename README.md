# Research Project Workflow

> English | [简体中文](README.zh-CN.md)

A lightweight, completion-first ChatGPT Skill for **parallel research IDEA exploration, evolving claims, controlled experiments, evidence interpretation, manuscript work, and recoverable project handoff**. It extends the original single-IDEA workflow into a branch-aware research portfolio without turning workflow maintenance into a blocker.

## What's new (working update)

- **Parallel IDEA portfolio:** competing, complementary, diagnostic, baseline and deployment-focused branches can coexist; advancement is determined by evidence and experiment dependencies, not by which IDEA arrived first.
- **Reverse innovation discovery:** mine existing experiment results through (A) effect heterogeneity, (B) anomaly fingerprint and competing mechanism tests, and (C) explicitly recognizable conditional deployment domains.
- **Versioned scientific claims:** `idea_id`, `parent_id`, `claim_version`, shared evidence IDs, stop/falsification rules, and honest branch decisions: advance, narrow, pivot, merge, pause or reject.
- **Project-wide evidence quarantine:** final-test inspection used for branch, metric, method or domain selection cannot serve as independent confirmation of the resulting new claim. Fresh data/sources are needed for that purpose, not new labels or code versions.
- **Conditional utility:** report deployable boundary, coverage, paired mean benefit/uncertainty, worst key-group risks, costs, and out-of-domain limits rather than post-hoc cherry-picked success.
- **Resource-aware experiments:** share strong controls and source identities; favor cheap discriminating tests, preserve independent confirmation budgets and negative evidence.
- **Continuity:** save only the live IDEA map and evidence boundaries at meaningful handoffs, not every historical run.

The previous **completion-first**, **pre-experiment novelty and baseline viability**, **validation vs. locked final testing**, **paper/venue selection**, and **minimal recoverable handoff** requirements remain active.

## Core research paths

```text
shared question/data/protocol/strong baselines
    +-- forward: IDEA -> mechanism -> matched experiment
    +-- reverse A: condition-specific gain / loss
    +-- reverse B: anomaly -> rival mechanisms -> discriminating intervention
    +-- reverse C: recognizable deployment boundary -> utility / risk
    \-- optional evidence-based merges and pivots
                    |
        versioned frozen claim -> independent confirmation -> paper
```

A, B and C are possible concurrent discovery modes, not mandatory stages or guaranteed innovations. A narrower valid contribution still needs clear technical distinction and honest verification.

## Reference routing

| Task | Load when needed |
| --- | --- |
| Parallel IDEA portfolio, reverse discovery, anomaly mechanism, pivots and domain claims | `references/idea-portfolio-and-reverse-innovation.md` |
| New/revised claim, baseline check, experiment contract | `references/idea-to-plan.md` |
| Code, batches, runs, diagnostics, results | `references/code-experiment-loop.md` |
| Manuscript/venue/claim-evidence audit | `references/paper-workflow.md` |
| New-session recovery, material state conflicts | `references/context-management.md` |
| Explicit handoff, major checkpoint or confirmed context pressure | `references/handoff-workspace.md` |

`SKILL.md` is the session-resident core, read once. Load at most one primary reference by default and reuse instructions already present in the session. Project-specific state belongs in the project workspace; an optional compact IDEA register can be kept there only when several active branches make it useful.

## Prompt examples

```text
Use Research Project Workflow to compare IDEA-A and IDEA-B and plan the cheapest tests that distinguish them, while preserving the independent final holdout.
```

```text
Mine last week's positive and negative experiments for conditional effects, competing anomaly mechanisms and a deployable conditional domain. Propose evidence-labeled child IDEAs, not post-hoc final claims.
```

```text
Evolve the current innovation claim based on the anomalous results, retain negative evidence, check the closest stronger baselines and specify how we can independently confirm the revised claim.
```

```text
Reconcile the manuscript contributions with the surviving IDEA branches, domain coverage and locked confirmation evidence.
```

## Repository layout

```text
SKILL.md
references/{idea-portfolio-and-reverse-innovation,idea-to-plan,code-experiment-loop,paper-workflow,context-management,handoff-workspace}.md
scripts/package_handoff.py
agents/openai.yaml
assets/icon.svg
```

## Installation / maintenance

Keep the directory structure intact when importing the Skill. If applying this source bundle to an existing Git clone, use a feature branch, review the changed files and commit after validation. The source bundle itself does not include the Git commit history. The original published citation version stays unchanged until a new release is actually made.

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

MIT License. See [LICENSE](LICENSE). Citation metadata: [CITATION.cff](CITATION.cff).
