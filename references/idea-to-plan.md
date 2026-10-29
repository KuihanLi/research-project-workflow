# IDEA -> Implementable Research Plan (branch-aware)

Load for new/vague ideas, materially revised hypotheses, implementation contracts, novelty/baseline scans or experiment freeze. Do not assume the IDEA must be the only active research line. Use `idea-portfolio-and-reverse-innovation.md` for branch competition, reverse mining and claim lineage; load both only if those procedures are needed.

## 1. Define the branch research contract

Capture only fields needed for the next decision:

- stable `idea_id`, `claim_version`, parent/originating evidence (if a pivot), and what actually changed;
- task, target output, technical intervention and falsifiable prediction;
- input semantics, shape/order/units/missingness/normalization, and deployment-time information;
- controlled resource/data budget, true independent evaluation unit, randomness (split/training/view/domain/etc.);
- primary metric, failure-sensitive metrics, eligible deployment domain and rule for recognizing it;
- other active branches sharing or competing for the same evidence, including shared controls.

Do not request a full portfolio table for a lone idea. Noncritical unknowns can be marked as assumptions.

## 2. Novelty-and-baseline gate before expensive claim freeze

For a new or materially changed contribution, search current literature around task, mechanism/architecture, claimed advantage, strongest simple alternatives, closest works in roughly the last 3–5 years and relevant seminal work. The initial cheap proof-of-feasibility may precede this check; not the costly main confirmation campaign.

For decisive prior work record: contribution, exact overlap, **surviving** technical distinction, evidence needed and official runnable code/data/protocol when available. If novelty collapses, revise the claim now rather than recycling an obsolete “first” claim. A child branch can reuse the parent novelty review only where truly unchanged; run a delta search on the new mechanism/target.

Separate:

- **strict-protocol baselines**, comparable numerically with same split, inputs, supervision, resource and metric semantics;
- **method-native literature comparisons**, relevant but not directly protocol-equivalent.

Make a representative strongest practical baseline executable when feasible. Record official-versus-adapted provenance, plausibility and resource/input mismatches; if unreproducible, explain specifically and narrow numerical comparison claims.

## 3. Hypothesis, alternatives and minimal discriminating controls

For the branch record:

- precise candidate mechanism and competing alternative(s);
- minimal intervention and explicit prediction that alternatives would *not* equally explain;
- controlled confounders, matched strong/simple baselines, negative controls where valid;
- expected signature by task, source, feature, capacity or domain if relevant;
- development pass/fail thresholds, principal confirmation rule, falsifier, cost and risk boundaries.

Choose a meaningful causal contrast where experiment design permits; observations alone are not causal identification. A post-hoc positive slice from earlier tests is a discovery lead only, requiring fresh evaluation before a confirmatory scope claim.

## 4. Freeze one claim version, not the whole portfolio

Before first *reserved independent final-test* access, freeze a **selected candidate claim version** with method/code/config, input scope, data/split/seed definitions, checkpoint selection, primary and risk metrics, baseline comparison, target domain, reporting/aggregation plan and planned multiplicity treatment. Other branches may continue exploring on development data; do not let their results select a different winner on the same final holdout.

Final evidence is not a model-selection budget. A new idea inspired by final tests starts a new exploratory `claim_version`; independent confirmation requires genuinely untouched data/sources. Never relabel a refrozen old holdout as unseen evidence.

## 5. Implementation boundary and next action

Prioritize a minimal mechanism test, viable strong baseline, instrumentation, reproducibility controls, and then justified complexity. Identify which resource-sharing with sibling branches avoids duplicate experiments. Mark core, auxiliary or optional only when useful.

Deliver runnable experiments and analysis whenever the user requests them; avoid turning the registry, literature check or branch stages into needless blockers. Stop or pivot if a simple baseline already explains the observed gain or falsifying evidence makes the proposed claim unsupportable.
