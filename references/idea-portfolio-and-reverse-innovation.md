# Parallel IDEA Portfolio, Reverse Innovation, and Claim Evolution

Load only for multi-IDEA research, reinterpreting old results to develop new innovations, anomaly mechanism inference, conditional-domain claims, or branch arbitration/merging. This procedure integrates the user-provided reverse-innovation methodology with the existing evidence-protected workflow. It does **not** require every project to maintain all possible artifacts.

## 1. Use a portfolio, not a compulsory IDEA chain

Think in **branches plus shared evidence**:

```text
Shared task / raw data / protocol / strong baselines / evidence ledger
    |-- F: forward IDEA -> minimal mechanism -> controlled result
    |-- A: result re-mining -> conditional effects -> candidate method
    |-- B: anomaly fingerprint -> competing causes -> discriminating tests
    `-- C: deployable applicability domain -> coverage / risk / cost
               \      |       /  (optional evidence-based merge)
          claim revisions -> frozen independent confirmation -> paper
```

F/A/B/C are **modes, not required sequential stages or fixed folders**. One branch can use multiple modes; A, B and C can advance simultaneously, and none automatically receives priority because it was first. Distinguish branches that compete for the same answer from those probing orthogonal mechanisms or serving as robust negative controls.

For each materially active IDEA, keep only enough state to decide the next test:

| Field | Meaning |
| --- | --- |
| `idea_id`, `parent_id`, `claim_version` | Stable lineage; revisions never silently overwrite a frozen claim |
| `question`, `technical_action`, `predicted_difference` | Problem, executable mechanism, how it differs from alternatives |
| `status`, `priority`, `dependencies`, `next_decision` | Candidate / active / paused / merged / rejected / confirmed; dependencies |
| `evidence_ids`, `evidence_class`, `split_exposure` | What is known and whether test evidence was used for discovery |
| `baseline`, `fairness_budget`, `falsifier` | Strong/simple alternatives, equal inputs/splits/resources, stop rule |
| `deployment_domain`, `risks`, `novelty_delta` | Boundaries, worst groups, real prior-art gap |

A small project can use a short section in `PROJECT_STATE.md`; a many-branch project can use a small project-local `IDEA_REGISTER.md` with the fields above. Do not require a new registry for a single routine answer.

## 2. Mine old results without rewriting history (track A)

1. Preserve the old IDEA's protocol, both positive and negative runs, identifiers, model/feature variants, metric definitions and true independent evaluation units. Identify any run invalidated by leakage/protocol/implementation errors and keep it separate from valid negatives.
2. Compute **paired effects on comparable units** at the right unit of independence. Explore task × group/source × condition × feature × model capacity × resources × train/validation/test × error type. Do not call overlapping windows or several settings on the same people independent samples.
3. Look for six structural patterns: stable complementarity; task-condition reversal; fit vs deployment reversal; complex method losing to simple method; local gain with critical local harm; conflicting objectives (e.g., NLL vs accuracy or mean vs worst group).
4. Promote a pattern to an innovation candidate only with: **(i)** concrete preexisting gap, **(ii)** executable technical intervention, **(iii)** distinctive prediction over strong simple baselines, **(iv)** failure/stop criterion. Prefer minimal transparent changes.
5. Before launching costly new campaigns, audit closest relevant literature and run at least one representative viable strong baseline when practical. Do not assert first-ever novelty based on a pattern alone.

A finding like “extra features help fitting but hurt unseen sources” allows conditional-value and robustness hypotheses, **not** a test-result oracle selector. Newly proposed decisions must use features and side information actually available before or during deployment.

## 3. Infer mechanisms from anomaly fingerprints (track B)

First triage validity: labels, identity and source groups, duplicate observations, leakage, normalization time, missingness semantics, code/config/metric/checkpoint mismatch, training budget, aggregation. Invalid runs do not count as scientific refutations.

Describe an **error fingerprint**, not only an average: who/what/where/when is affected; train/validation/held-out direction; information block responsible; ranking vs probability/threshold effect; repeated records from the same unit; severity and identifiable conditions.

For a material anomaly, name at least **two competing, distinguishable explanations**, e.g. source scaling, shortcut correlations, capacity/regularization burden, task-specific feature value, or fully confounded labels/deployment conditions. For each, write a unique observable prediction and cheapest discriminating test. **No unique causal mechanism follows from the shape alone.**

Use the smallest feasible intervention ladder:

1. Observational correlation (association only).
2. Within-task/source/person pairing or meaningful stratification (reduces some confounding).
3. Negative controls (matched-dimensional noise, unrelated labels, controlled shuffling; choose a valid one).
4. Component ablation or matched replacement (mechanism evidence, not automatically causal).
5. Controlled intervention/natural experiment where identifiability and assumptions permit (potentially stronger causal inference).

Ask **necessity**, **sufficiency**, and **actionability at deployment**. When a suspected factor remains completely confounded with the label, existing data cannot isolate its cause by repeated analysis. Keep counterexamples. Investigate deeper only if anomaly threatens the principal claim, poses serious deployment risk, distinguishes mechanisms, or admits an actionable method; otherwise archive as a known limitation.

## 4. Define a conditional deployment-level claim (track C)

A narrower but **operationally identifiable** target population is a legitimate research target. Define before independent confirmation:

\[
\mathcal C=\{(X,Z):\text{task, device, environment, population and resource criteria known at deployment hold}\}.
\]

Classify the boundary's origin:

- **Ex ante reality constraint** (hardware/protocol/business): legitimate a priori scope.
- **Training-side defined recognizable rule**: eligible after its selection is frozen and checked on unused confirmation data.
- **Post-hoc favorable slice** of test results: discovery only, **not independent proof** on those same observations.

A valid gate must not require true test labels, future errors, or per-example oracle access. For loss (smaller is better), define:

\[
\Delta_{\mathcal C}=\mathbb E[\ell(Y,f_{\rm base}(X))\mid(X,Z)\in\mathcal C]-\mathbb E[\ell(Y,f_{\rm new}(X))\mid(X,Z)\in\mathcal C].
\]

Report together: **domain recognition rule and coverage**, pre-specified paired primary gain and uncertainty, failure-sensitive and worst observed relevant subgroup outcomes, resource/latency/maintenance cost, important non-target/untested sources and a fallback/abstention policy when applicable. Domain-average improvement is not pointwise or out-of-domain guarantee. Worst observed groups are not guaranteed future lower bounds.

Reject post-hoc **source picking, metric picking, task picking** presented as confirmation. The proposed constrained-domain claim becomes a new version, requiring untouched source/site/batch/data for independent confirmation when available; if not available, label exploratory and show the complete selection history.

## 5. Cross-branch experiments and fair scheduling

Parallelize cheap independent tests and shared preprocessing/controls; sequence real prerequisites (data validity, matched baseline, frozen final contract). Favor small, high-information contrasts over firing every idea into a full multi-seed campaign.

For each planned contrast declare:

- linked `idea_id`/`claim_version` and evidence class (exploratory / mechanism / independent final);
- question, competing predictions and what result would eliminate an alternative;
- same subjects/splits/available inputs/capacity/compute when required; variance/seed independent units;
- strong simple and closest public baseline, negative controls where appropriate;
- run ID, code/config/data version, status, bounded retry and results location;
- ahead-of-time pass/fail/stop rule and next decision.

**Cross-branch evidence quarantine:** experiment results can be shared as observations but not counted as fresh confirmations for every branch. If a final holdout was inspected to **select** branch, metric, model, threshold or domain, it is exploratory for the selected new claim. Refreezing the method does not rehabilitate it. A new independent confirmation source, not a new branch/seed label, is required for that selected claim.

Avoid duplicated runs when multiple branches use an identical configuration; reference the same run ID and mark dependency. If resources are constrained, retain a viable simple baseline and a reserved confirmation budget before adding complex branches.

## 6. Branch decisions, pivots, and merges

At a decision checkpoint, compare **evidence strength**, not only the best observed score. Consider research value, known novelty overlap, discriminating power, cost, deployment coverage/risk, and practical feasibility. Do not invent a precise weighted ranking if values are qualitative.

- **Advance:** fair decisive evidence supports a distinctive effect and next experiment improves confidence.
- **Narrow:** credible benefit is confined to a recognizable, useful domain; log new claim version and confirmation status.
- **Pivot:** a mechanism is contradicted or old evidence exposes a new problem; retain parent negatives and start a child branch with new falsifiers.
- **Merge:** two mechanisms are jointly needed and combined contribution predicts more than either alone; compare A, B, A+B and strong simple alternative fairly. Shared evidence remains shared, not independent.
- **Pause:** insufficient budget/identifiability/inputs; record missing prerequisite, do not repeatedly rediscover.
- **Reject / close:** a required prediction fails, a simple baseline explains the gain, risk is unacceptable or further tests do not alter decisions. A valid negative is not an operational failure.

A changed **technical action, principal metric, application domain or primary claim** increments the claim version. Record the reason, evidence that inspired it, potential test exposure, novelty/baseline update, new controls and validation plan. A wording-only clarification with unchanged evidential meaning need not restart experiments.

## 7. Source-derived, bounded deliverables

For a substantive revision, return a compact portfolio summary containing each active branch's **supported fact -> competing explanation -> smallest deciding test -> continuation decision**. A paper's chosen contribution must be traceable to its originating IDEA(s), strong baseline, independent evidence class and constraints; related branches and negative results remain available for limitations or future work.

If several branches must be maintained, keep a small project-local register based on Section 1. A single exploratory discovery card can use the source methodology's five blocks: verified facts, competing explanations, deployable constraints, discriminating experiment, honest claim/status. Avoid forcing full paperwork on small tasks.

**Stop** when the cheapest meaningful test cannot change the decision, when independent confirmation is unavailable and a qualified exploratory conclusion suffices, or when current user-requested work is complete.
