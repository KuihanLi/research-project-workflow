# Code -> Experiment Loop (shared across IDEA branches)

Load for experiment-facing implementation, planned/returned experiments, retries, failure diagnosis, aggregation or controlled branch comparison. Reuse after loading.

## 1. Implement by touched risk

**Data/semantics:** verify shape/order/units, mask/missingness, leakage-free splits and normalization, source/subject/session identities, deterministic views, deployment-available inputs.

**Model/interface:** preserve current APIs unless necessary; put repeated choices in config; keep minimal controlled changes; isolate conflicting branch-specific modifications in reproducible commits/configs while keeping a known shared baseline.

**Infrastructure:** as applicable, record seeds, config snapshot, checkpoint identity, run completeness, structured result, bounded retries and failure classification.

**Reporting:** aggregate valid runs, mean/dispersion, paired effects or uncertainty on independent units, relevant worst subgroup, resource costs and source provenance. The same observation referenced by two branches is *not* two replications.

## 2. Verification ladder

Use the cheapest appropriate check: (1) unit/shape; (2) synthetic/dry-run; (3) tiny real development smoke; (4) one full development run; (5) small multi-seed batch; (6) full sweep or **frozen independent final**. Skip irrelevant levels covered by sound existing evidence; final holdout is never a debugging surface.

## 3. Evidence class and experiment identity

- **Development / tuning:** use training/validation to choose branch, method, metric-compatible settings or a conditional domain.
- **Mechanism / ablation:** discriminate explicit explanations, controlled alternatives and failure modes; don't silently tune a frozen candidate after observing final evidence.
- **Independent final confirmation:** execute the pre-specified locked claim-version contract, not a winner-selection competition over many unregistered branches.

Use stable identity containing relevant `idea_id`, `claim_version`, run purpose, code/config/data/split/seed, information and compute budget, expected output, status and evidence class. For shared baselines, register the run **once** with multiple consumers. If a code/data/metric semantic repair changes the condition, create a new run rather than overwriting the old negative.

Track test exposure across the project. Selecting a new feature, subgroup/domain or method after viewing final holdout results marks subsequent evidence on that holdout exploratory. Changing a branch ID does not restore holdout independence.

## 4. Design decisive, branch-comparable batches

Plan orthogonal low-cost contrasts together; keep inputs, source units, data splits, backbone/capacity, training budget, checkpoint and metric definitions matched when testing a targeted mechanism. Use negative controls (e.g. matched-dimensional noise or label shuffles) only when valid.

Measure conditional effects by task/source/feature and realistic independent unit, not a post-hoc best score. Anomaly fingerprints should have competing predictions and, when feasible, layered evidence: pairing -> negative controls -> ablation -> controlled intervention. Complexity that loses to a strong simple baseline must be acknowledged.

When several branches compete for one research claim, use **development evidence** to decide which merits a locked independent confirmation; protect its budget and plan for multiple-testing/selection where unavoidable. A+B combination requires controls A, B, A+B and simple baseline and a distinctive combined prediction; don't assume merging improves performance.

## 5. Dispatch external execution

For server/GPU/hardware work the user must run, first finish local code/config/scripts. Then provide purpose and evidence class, exact runnable command, identity/splits/seeds, bounded retries, expected result path, one preferred return bundle and the decision it resolves. For detached/background launch, provide status query and result-collection commands in the **same answer**, tied to the new run ID/path if known, without relaunching an existing equivalent job. Never invent executable script names or imply unattended access.

## 6. Receive and interpret

Classify: operational failure; valid negative; valid positive; incomplete/validity unknown. Treat a method-caused OOM or instability as possible reliability evidence, not always ignorable infrastructure failure. Never repeat a valid negative merely to obtain a passing result.

For surprises, check the relevant items in order: semantics/leakage/grouping, source/label confounding, unpaired or incomplete runs, checkpoint/metric mismatch, stronger simple baseline, then mechanism hypotheses. Preserve all counterexamples and actual uncertainty.

For each branch choose **advance / narrow / pivot / merge / pause / reject**; record the reason and claim-version transition only for material changes. A valid negative remains in the record. Do not infer universal or causal benefit from a post-hoc subset or observational correlation.

## 7. Continuity

For substantive iterations preserve the minimum useful version note: changed behavior, motivation, code/config/data/seed, affected branch claims, verified checks, result/provenance, next decision, and compatibility issues. Project bookkeeping is not a prerequisite for fixing code or delivering the requested result.
