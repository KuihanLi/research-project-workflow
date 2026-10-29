# Handoff Workspace Packaging

Load only at a genuine continuity checkpoint: **(1)** explicit handoff/export/migration request; **(2)** major method, contract, manuscript or research-phase revision yielding a new authoritative state; or **(3)** confirmed runtime context/compaction risk. Do not package after routine edits or every experimental return.

## 1. Deliverables

When files are available, provide **both** `handoff_bundle.zip` and root-level `HANDOFF.md` in the same turn. The archive is a **minimum recoverable workspace**, not a full project dump; `HANDOFF.md` is included at its root and surfaced separately when practical. In three-part user responses include links under **关键依据 / 交付**, not a fourth section.

## 2. Select minimal recoverable files

Select by recoverability: current authoritative code/scripts/config, manuscript/source as needed, launch/status/aggregation scripts for pending experiments, compact evidence summaries, data/split/seed/locked evaluation protocols, and a project state file if genuinely authoritative.

For **materially multi-IDEA work**, include compact active branch portfolio or equivalent project-state excerpt that records IDs/parents/claim versions/status, shared evidence IDs, negative/paused paths, independent confirmation availability, and next decisions. Do **not** archive full evidence matrices or raw logs by default merely because branches exist.

Exclude raw datasets (if externally recoverable), large checkpoints unless essential/small, caches, virtual environments, build previews, superseded duplicate versions, long raw logs, credentials/tokens/private keys, secret-bearing environment files and unrelated project files.

If a required artifact cannot be included, give exact external path/identifier and recovery instructions in the handoff; never pretend it is packaged.

## 3. Required HANDOFF.md content

Keep concise but operationally sufficient:

1. **Project/objective** and immediate purpose.
2. **Task state**: completed, active, blocked, scientific negative or operational failure; for multi-IDEA projects include the *active branch map*, claim versions, parent relations, shared baselines and branch decisions.
3. **Authoritative versions** of code/config/model/manuscript and which path is primary.
4. **Evidence and claim state**: supported/qualified/rejected claims; development/mechanism/locked independent confirmation and per-branch or project-wide test exposure; negative results and identifiable constraints.
5. **Data/evaluation boundary**: data/source/split, true independent unit, protocol and locked/final-test status; no new claim obtains a fresh holdout by renaming its branch.
6. **Pending/next tasks**: ordered, actionable work; exact commands for external runs; if interrupted by context pressure, precise next atomic operation.
7. **Output preferences**: relevant user delivery, reporting, experiment resource and language constraints.
8. **Workspace inventory**: included files/purpose, P0/P1/P2 if useful.
9. **External dependencies/non-packaged artifacts**: paths/repos/hardware/missing large files.
10. **Do-not-repeat/rejected paths**: tested negative and superseded hypotheses, in-progress runs not to duplicate.
11. **Resume instructions**: shortest safe reading order and one starter prompt.

No full chat dump or speculative state. Mark uncertainty or staleness explicitly. If no meaningful portfolio exists, do not manufacture IDEA sections.

## 4. Major checkpoint or pressure procedure

At a material phase close: finish and validate the requested revision; write/update `HANDOFF.md` from the resulting authoritative state; package minimal recovery files; include links in response part two. Not for typos or routine plot updates.

At **confirmed** pressure: finish the current safe atomic edit, document unfinished work and experiment/branch statuses, package before starting another long operation, and warn briefly. If context pressure cannot be observed, do not guess.

## 5. Optional separate evidence-chain companion

Create `EXPERIMENT_EVIDENCE_CHAIN.md` **only on explicit user request** for a separate proof/evidence archive. Map claim version -> run ID -> protocol/code/config/seed -> evidence class -> result (including negatives) -> inference limits -> contradictory evidence -> missing valid test. A reused shared experiment retains one provenance, even if cited in several branches; annotate exploration triggered by final-test inspection. Keep this separate from project-state `HANDOFF.md` and include in ZIP only when requested.

## 6. Package and verify

When the runtime permits, use `scripts/package_handoff.py` rather than ad hoc zips:

```bash
python scripts/package_handoff.py \
  --workspace-root /path/to/workspace \
  --handoff /path/to/HANDOFF.md \
  --include docs/PROJECT_STATE.md \
  --include configs/experiment.json \
  --include outputs/aggregate.json \
  --output /mnt/data/handoff_bundle.zip
```

For a multi-IDEA project add `--include IDEA_REGISTER.md` **only if the file exists and is needed for recovery**. For the explicitly requested evidence companion add `--evidence-chain /path/to/EXPERIMENT_EVIDENCE_CHAIN.md`.

The tool generates `HANDOFF_MANIFEST.json` with SHA-256 hashes and refuses missing paths, duplicate archive entries, escapes outside workspace, and obvious secret-bearing filenames. Check ZIP CRC, root `HANDOFF.md`, file references, essential P0 coverage, no known secrets/unnecessary large artifacts, and named external dependencies.

## 7. End rule

Create real artifacts when the checkpoint triggers and inputs exist; a template alone is insufficient. Do not make checkpointing block a normal compatible user request.
