# Idea -> Implementable Research Plan

Load this reference only for a new/vague idea, material method redesign, hypothesis framing, pre-experiment novelty/baseline validation, or experiment-contract planning. Do not reload it after the research contract is stable unless scope or the central claim changes.

## 1. Define the research contract

Capture only fields needed to make the next implementation/evaluation decision:

- task and target output;
- exact input semantics, shape/order/units/missingness/normalization;
- inference/deployment information actually available;
- controlled resource/data budget;
- randomness axes: split, training, view/subset, augmentation, hardware/domain as applicable;
- primary metric plus failure-sensitive metrics.

Resolve only ambiguities that materially change the method or evaluation. Noncritical unknowns may be stated as assumptions.

## 2. Run the novelty-and-baseline gate before the main experiment contract is frozen

For every new or materially changed claim, search before committing to the expensive experiment matrix. A cheap implementation smoke/proof-of-concept may run earlier, but the main experimental contract should not be frozen until this gate is complete.

Use current literature and search around:

- the exact task and evaluation setting;
- the closest mechanism/architecture, not only papers using the same application vocabulary;
- the claimed advantage (accuracy, robustness, generalization, efficiency, interpretability, deployment, etc.);
- strong simple methods that could explain the gain without the proposed mechanism;
- recent work from roughly the last 3--5 years plus seminal work that still defines the comparison.

For the decisive prior work, capture only what changes the research decision:

- closest prior contribution and evidence;
- overlap with the proposed claim;
- differentiator that still survives;
- experiment/evidence required to establish that differentiator;
- whether official runnable code/data/protocol exists.

If the scan weakens or removes the intended novelty, revise the claim/hypothesis now rather than after final experiments.

## 3. Validate baseline viability, not just baseline names

Separate candidate baselines into:

- **strict-protocol baselines**: compatible input/split/supervision/resource/evaluation semantics and suitable for numerical main-table comparison;
- **method-native literature comparisons**: scientifically relevant but not directly equivalent because the protocol or information set differs.

Before the main experiment matrix, make the strongest practical strict-protocol baseline path runnable on at least one representative condition when code/data access allows. Check that:

- the implementation is official or the adaptation is traceable;
- the evaluation protocol matches the planned claim;
- the result is numerically plausible relative to the source paper or known behavior;
- resource and information advantages are not silently mismatched.

If a decisive baseline cannot be reproduced, record the concrete limitation and adapt the claim/comparison plan before the experiment campaign rather than discovering the gap at manuscript freeze.

## 4. Frame one testable gap and register the hypothesis

Prefer a causal question such as: under the same relevant data/backbone/resource budget, what changes when mechanism X changes?

Classify the main gap only as needed: representation, optimization, sampling/data, efficiency, domain/generalization, or evaluation. Do not combine unrelated gaps merely to make the contribution appear larger.

For each core hypothesis record:

- hypothesis/mechanism;
- minimal intervention;
- controlled factors;
- development validation criterion;
- final claim criterion;
- falsifying outcome;
- claim boundary;
- closest surviving prior and strongest required baseline from Sections 2--3.

Use this register to prevent post-hoc storytelling, not as a mandatory visible table.

## 5. Choose controls before complexity

Use simple causal controls and compatible strong public/official baselines when they bear on the claim. Keep relevant backbone/data/resource conditions controlled when testing a mechanism. If a simple baseline wins, interpret what it reveals before adding complexity.

Do not postpone the first meaningful novelty/baseline audit to the paper-writing stage. Later manuscript-stage searches should normally be delta updates for newly published work or claim drift.

## 6. Bound implementation

Prioritize: minimal mechanism test, validated baseline path, diagnostic instrumentation, reproducibility controls, then optional refinements. Mark components as core, auxiliary, or future work only when that distinction affects implementation or claims.
