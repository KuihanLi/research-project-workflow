# IDEA -> Implementable Research Plan (branch-aware)

Load for new/vague ideas, **creating candidate IDEAs from papers or constraints**, materially revised hypotheses, implementation contracts, novelty/baseline scans or experiment freeze. Do not assume an IDEA must be the only active research line. Use `idea-portfolio-and-reverse-innovation.md` for branch competition, reverse mining and claim lineage; load both only if both procedures are needed.

## 0. Discover IDEAs from literature or existing technology (only when needed)

If the user already has a testable IDEA, go directly to Section 1. If they have a research direction, papers, technical constraints or a literature collection but **no concrete mechanism**, use this lightweight discovery procedure; it is not a mandatory paper-count or venue scan.

1. **Read and decompose relevant work.** Select a small set of closest and useful adjacent-domain papers, prioritizing actual methods/evidence over a prestigious journal or a catchy title. For each, distinguish **topic/task, scenario/application, method/representation, extra constraints/assumptions/resources**; identify the *actual technical action*, its claimed advantage, protocol, limitations and whether that claim was supported. Cite individual sources, and mark abstract-only or unverified claims. A journal's acceptance does not prove technical soundness or originality.
2. **Extract a reusable change pattern, not just a list of ingredients.** Candidate operators include cross-domain mechanism transfer; a defensible new physical/data/resource constraint; a changed objective/metric; removing a costly intermediate step; fixed-to-adaptive decisions; adapting an existing method to different input or algebraic structure; and questioning overlooked protocol, representation, or physical assumptions. An A+B+C recombination is only a *search prompt* until it yields a real problem, specific adaptation and discriminating gain.
3. **Generate several distinct candidates if useful.** For each, state `source decomposition -> transferable operator -> target setting -> failure of closest method -> executable technical delta -> predicted observable difference`. Ask what assumption breaks on transfer, what data/hardware/runtime information is actually available, and what simpler solution might erase the contribution. Do not invent deployment needs or assert an unexplored combination is first-ever new.
4. **Filter before committing a main campaign.** Compare against closest same-task, same-mechanism and adjacent-field prior work; assess problem reality, technical necessity, feasibility, likely research depth and minimal differentiating test. Keep only a few nonredundant candidates with provisional novelty status; do not turn a combination matrix into compulsory experiments. If the literature is inconclusive, say what remains unknown instead of certifying novelty.

**Compact forward IDEA output (when requested):** source paper(s) + four-part decomposition; change operator and technical delta; precise question and falsifiable claim; closest alternatives; smallest fair test; feasibility/novelty uncertainty. Keep references to the original sources, including negative evidence. Record origin under the shared fields in `idea-portfolio-and-reverse-innovation.md` only when comparing or maintaining multiple branches.

## 1. Define the branch research contract

Capture only fields needed for the next decision:

- stable `idea_id`, `claim_version`, parent/originating evidence **or cited literature/technology source**, source-specific decomposition and change operator when relevant, and what actually changed;
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
