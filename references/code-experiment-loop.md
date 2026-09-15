# Code -> Experiment Loop

Load this reference for experiment-facing implementation, experiment planning, returned-result interpretation, retry/failure diagnosis, or aggregation. Reuse it once loaded; do not reload per run or per turn.

## 1. Implement by risk

Check the layer touched by the change; do not audit unrelated layers every time.

### Data/semantics
- shape, ordering, units, mask/missingness semantics;
- leakage-free split and normalization;
- deterministic subset/view construction when required;
- inference matches the declared deployment contract.

### Model/interface
- preserve existing APIs unless a change is necessary;
- expose repeated experimental choices as configuration rather than hard-coded branches;
- keep the mechanism minimal until evidence justifies complexity.

### Experiment infrastructure
For nontrivial sweeps, ensure the needed subset of: seed control, config snapshot, checkpoint resume, best/last distinction, structured JSON/CSV results, run completeness, failure classification, and scheduler/retry support.

### Reporting
Aggregate the metrics required by the claim: valid run count, mean/std, paired differences or confidence intervals where meaningful, worst case, resource cost when claimed, and exact provenance.

## 2. Verification ladder

Use the cheapest check that addresses the risk introduced by the change:

1. unit/shape check;
2. synthetic/dry run;
3. tiny real-data development smoke run;
4. one full development run;
5. small multi-seed batch;
6. full sweep or frozen final confirmation.

This is risk guidance, not a turn-by-turn gate. Skip irrelevant levels when prior evidence already covers them. Never use the reserved final test as a smoke/debug surface.

## 3. Experiment classes

- **Development/tuning**: choose settings from train/validation evidence only.
- **Mechanism/ablation**: test explanatory components; after freeze, do not use these results to silently retune the frozen candidate.
- **Final confirmation**: evaluate a prespecified frozen candidate; do not redesign from the result on the same holdout.

Prefer planned compact searches over serial ad-hoc edits. Declare the primary selection statistic before interpreting a tuning batch.

## 4. Dispatch external execution

When the user must run the experiment, provide only information needed to execute and return evidence:

- task purpose and experiment class;
- code/config/data/seed identity that matters;
- exact command(s) for the real environment;
- required run count and bounded retry/stop conditions when relevant;
- output location and one preferred return bundle;
- decision the evidence will resolve.

Do not invent executable script names. Do not imply background monitoring. If a prerequisite can be checked with available tools now, check it instead of adding a user round trip.

## 5. Receive and interpret results

First classify the return:

- operational failure;
- valid result below criterion;
- valid result meeting criterion;
- incomplete or validity unresolved.

Do not retry valid negative results until they pass. A method-caused OOM/instability may itself be reliability evidence.

For surprising results, check only relevant causes in this order: protocol/semantics mismatch, leakage/normalization/order, incomplete or unpaired runs, checkpoint/metric mismatch, strong simple-baseline explanation, then model redesign.

Use the strongest valid conclusion supported by current evidence and state its scope. Never present an incomplete matrix as complete final evidence.

## 6. Retry and identity

For confirmatory comparisons, preserve pairing keys, intended repeat counts, acceptance criteria, and bounded operational retry rules. A repair that changes method/data/metric semantics creates a new condition rather than replacing the old result.

Use stable run/config/data identity or fingerprints when version labels are insufficient. Temporary paths, ports, or process IDs are not scientific identity.

## 7. Version continuity

For meaningful code/experiment iterations, retain the minimum useful record: version, changed behavior/reason, relevant config/CLI, seed/data semantics, tests performed, result/decision, and compatibility note if needed. Update project state in the same pass when practical, but never withhold a clear code fix merely because bookkeeping is stale.
