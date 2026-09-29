# Handoff Workspace Packaging

Load this reference at a real continuity checkpoint:

1. **Explicit request** — the user asks for a handoff, handoff document, resumable/minimal workspace package, workspace migration/export, or equivalent deliverable.
2. **Major revision / phase close** — a material revision or meaningful project phase has completed and produced a new authoritative state worth resuming from later.
3. **Confirmed context pressure** — the runtime reliably signals context/compaction risk, or prior context has demonstrably been truncated, and continuity needs protection.

Do not trigger after routine edits, small patches, every experiment return, or merely because a conversation is long.

## 1. Default deliverable

Produce both of the following in the same turn whenever the needed files are available:

1. `handoff_bundle.zip` — a **minimum recoverable workspace**, not a dump of the entire project;
2. `HANDOFF.md` — included at the archive root and also surfaced separately when practical.

The bundle must be sufficient for a new session to continue the next intended task without reconstructing the full chat history.

For an automatic major-revision/phase checkpoint, do not add a separate user-facing handoff section. In the normal three-part response, put the download link in **part 2: 关键依据 / 交付** alongside the main deliverable.

## 2. Select the minimum recoverable workspace

Choose files by recoverability, not recency or volume. Prefer the smallest set that preserves:

- authoritative current code/scripts/configuration needed for the next task;
- current manuscript/source when paper work is active;
- the exact run/launch/status/aggregation scripts needed to resume pending experiments;
- compact result summaries or machine-readable outputs that support the current conclusion;
- protocol/config files that define data, split, seed, frozen-test, hardware/topology, or evaluation semantics;
- any project master/state file that is actually authoritative.

Exclude by default:

- raw datasets that can be re-referenced by path;
- model checkpoints/weights unless they are uniquely required to resume and reasonably small;
- caches, virtual environments, build artifacts, rendered previews, temporary exports;
- duplicate historical versions already superseded by the authoritative one;
- large raw logs when a compact status/result file is sufficient;
- credentials, tokens, private keys, secrets, or environment files containing secrets;
- unrelated project files.

If a required artifact is too large, unavailable, or external, record its exact path/identifier and recovery command/source in `HANDOFF.md` rather than pretending it was packaged.

## 3. Required `HANDOFF.md` contents

Keep the handoff concise but operationally sufficient. Include these sections:

1. **Project / objective** — current research goal and immediate purpose of the handoff.
2. **Current task state** — what is completed, in progress, blocked, failed operationally, or scientifically negative.
3. **Authoritative versions** — current code/workspace/manuscript/model/config versions and which files are authoritative.
4. **Evidence and claim state** — current supported/qualified/rejected conclusions; distinguish development, mechanism/ablation, and frozen/final evidence when relevant.
5. **Data / evaluation boundary** — dataset/split/protocol and final-test access/freeze status when relevant.
6. **Pending / next tasks** — ordered, actionable work still to do; include exact command(s) when execution is external. **If handoff was triggered by context pressure before the requested task finished, record the interrupted task and exact next operation here.**
7. **Output preferences** — user-requested response style, packaging conventions, report/figure/document preferences, resource/scheduling constraints, and other reusable delivery expectations that materially affect continuation.
8. **Workspace inventory** — only files in the bundle, each with purpose and priority (`P0`/`P1`/`P2` when useful).
9. **External dependencies / non-packaged artifacts** — exact paths, repositories, server locations, hardware assumptions, or missing large files needed to continue.
10. **Do-not-repeat / rejected paths** — completed work that must not be redone, failed approaches that should remain frozen, and operational/scientific negatives worth preserving.
11. **Resume instructions** — shortest safe reading order and one starter prompt for the next session.

Do not include chat transcript dumps. Do not convert guesses into project facts. Mark stale or uncertain state explicitly.

## 4. Major-revision / phase-close checkpoint

Treat a checkpoint as automatic only when the just-completed work creates a materially new authoritative state, for example:

- major method/architecture revision;
- new experiment contract or frozen campaign definition;
- large result-matrix closure or final evidence milestone;
- major manuscript/workspace revision intended to become the continuation baseline;
- phase transition where later work should not reconstruct the prior phase from chat history.

Do not package for typo fixes, small code patches, minor prose edits, routine plot changes, or every intermediate result.

At checkpoint completion:

1. finish and validate the requested revision first;
2. write/update `HANDOFF.md` from the resulting authoritative state;
3. package the minimum recoverable workspace;
4. put the download link in response part 2 without duplicating the handoff narrative.

## 5. Context-pressure checkpoint

When context pressure is reliably confirmed, checkpoint **before** an avoidable hard stop:

- finish the current atomic operation if safe;
- capture the exact current state, including partial/incomplete work;
- write unfinished requested work into `Pending / next tasks`;
- package before starting another long branch;
- warn briefly that the checkpoint protects continuity.

If further work would materially risk losing authoritative state, stop after the checkpoint and make the next task explicit in `HANDOFF.md`. If the runtime does not expose a reliable pressure signal, do not guess; rely on major-revision/phase checkpoints.

## 6. Optional experiment evidence-chain companion — explicit request only

Create `EXPERIMENT_EVIDENCE_CHAIN.md` **only when the user explicitly asks for a separate experiment evidence chain, evidence bundle, or equivalent**. Do not create it automatically at a major revision or context checkpoint merely because experiments exist.

When requested, include:

- material claim / hypothesis;
- exact evidence artifact or run/report ID;
- protocol/configuration/seed semantics;
- evidence class: development, mechanism/ablation, locked/final, external baseline;
- observed result, including valid negative results;
- confounds/limitations and operational failures kept separate from scientific outcomes;
- what the evidence supports, qualifies, or contradicts;
- unresolved evidence gap and next cheapest valid test if one remains.

Keep the evidence-chain document separate from `HANDOFF.md` so project state and scientific proof do not become one oversized document. Surface it as a separate file; include it in `handoff_bundle.zip` only when explicitly requested.

## 7. Package and verify

After selecting the minimum file set and writing `HANDOFF.md`, use `scripts/package_handoff.py` rather than ad-hoc zip commands when the runtime permits.

Example:

```bash
python scripts/package_handoff.py \
  --workspace-root /path/to/workspace \
  --handoff /path/to/HANDOFF.md \
  --include docs/PROJECT_MASTER_OVERVIEW.md \
  --include scripts/run_campaign.sh \
  --include configs/campaign.json \
  --include outputs/aggregate.json \
  --output /mnt/data/handoff_bundle.zip
```

If the user explicitly requests the evidence-chain companion, add:

```bash
  --evidence-chain /path/to/EXPERIMENT_EVIDENCE_CHAIN.md
```

The script writes `HANDOFF_MANIFEST.json` with file sizes and SHA-256 hashes and fails on missing files, duplicate archive paths, paths outside the declared workspace, or obvious secret-bearing filenames.

Before delivery, verify:

- archive opens successfully;
- `HANDOFF.md` exists at archive root;
- every included file is referenced or understandable from the handoff inventory;
- no known required P0 file was omitted;
- no secret file or unnecessary large historical artifact was included;
- external/non-packaged requirements are named in `HANDOFF.md`.

## 8. Delivery rule

Create and return the artifacts directly when a checkpoint triggers. Do not respond only with a template or a future plan when the workspace is available. For normal three-part responses, surface the handoff download link in **part 2** and avoid a redundant extra handoff section.