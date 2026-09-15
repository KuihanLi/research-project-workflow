# Idea -> Implementable Research Plan

Load this reference only for a new/vague idea, material method redesign, hypothesis framing, or experiment-contract planning. Do not reload it after the research contract is stable unless scope changes.

## 1. Define the research contract

Capture only fields needed to make the next implementation/evaluation decision:

- task and target output;
- exact input semantics, shape/order/units/missingness/normalization;
- inference/deployment information actually available;
- controlled resource/data budget;
- randomness axes: split, training, view/subset, augmentation, hardware/domain as applicable;
- primary metric plus failure-sensitive metrics.

Resolve only ambiguities that materially change the method or evaluation. Noncritical unknowns may be stated as assumptions.

## 2. Frame one testable gap

Prefer a causal question such as: under the same relevant data/backbone/resource budget, what changes when mechanism X changes?

Classify the main gap only as needed: representation, optimization, sampling/data, efficiency, domain/generalization, or evaluation. Do not combine unrelated gaps merely to make the contribution appear larger.

## 3. Register the hypothesis

For each core hypothesis record:

- hypothesis/mechanism;
- minimal intervention;
- controlled factors;
- development validation criterion;
- final claim criterion;
- falsifying outcome;
- claim boundary.

Use this register to prevent post-hoc storytelling, not as a mandatory visible table.

## 4. Choose controls before complexity

Use simple causal controls and compatible strong public/official baselines when they bear on the claim. Keep relevant backbone/data/resource conditions controlled when testing a mechanism. If a simple baseline wins, interpret what it reveals before adding complexity.

Run a literature novelty/baseline audit only when novelty/comparison positioning is actually in scope. The session router will load the paper procedure when needed; do not chain-load it from this reference.

## 5. Bound implementation

Prioritize: minimal mechanism test, diagnostic instrumentation, reproducibility controls, then optional refinements. Mark components as core, auxiliary, or future work only when that distinction affects implementation or claims.
