# Paper and Submission Workflow

Load this reference for manuscript drafting/revision, claim audit, venue selection, literature-position delta checks, or submission work. Reuse it after loading; do not rerun searches every turn unless evidence, claim scope, target venue, or the publication landscape materially changed.

## 1. Select the venue family before designing the manuscript frame

Unless the user explicitly requests a venue-neutral draft, do venue positioning **before** locking the title/abstract/contribution framing or section architecture. Do not choose by impact factor alone.

First summarize the paper as it actually exists:

- central problem and surviving contribution;
- evidence type and strength;
- algorithm/system/measurement/application emphasis;
- scale, datasets/testbeds, robustness/generalization axes, and reproducibility assets;
- major evidence gaps that cannot be hidden by writing.

Then search current official scope/instructions and recent related publications and shortlist roughly 2--4 plausible venues. Compare them on:

- scope and contribution-type fit;
- novelty/evidence burden;
- systems vs algorithm vs measurement emphasis;
- expected experimental breadth and baseline strength;
- whether the journal has recently published close work;
- practical constraints such as manuscript type/page policy and public data/code expectations when relevant.

Choose one primary target and one or more fallbacks. Record how the **narrative emphasis** would change across venues while keeping scientific facts fixed. If no candidate fits the evidence, revise the paper claim or collect missing evidence rather than forcing a venue.

## 2. Treat manuscript-stage literature review as a delta audit, not first discovery

A new/materially changed research claim should already have passed the pre-experiment novelty/baseline gate in `idea-to-plan.md`. At drafting time, search again only to:

- capture important work published since the earlier audit;
- check that the contribution wording has not drifted beyond what survived the original scan;
- update the closest-prior comparison for the selected venue;
- verify that no newly found work invalidates a central claim.

For each decisive paper capture: what is already known, what is similar but not identical, what evidence distinguishes the present work, and which wording must be narrowed. If a late discovery does collapse a claim, change the claim transparently; do not invent post-hoc novelty.

## 3. Keep baseline comparisons protocol-honest

Separate:

- **strict-protocol baselines**: compatible with the same input/split/evaluation semantics and suitable for numerical main tables;
- **method-native literature comparisons**: require incompatible inputs, preprocessing, supervision, resources, or datasets and should be discussed rather than misrepresented as equivalent reproductions.

Prefer official implementations when practical and record material adaptations. A stronger baseline stays visible and should narrow or sharpen the contribution. If the strongest baseline was not validated before the main experiment campaign, flag that as research debt and resolve it before final comparative claims whenever feasible.

## 4. Claim-to-evidence closure

Before final claims or new expensive confirmation, map each material claim to existing evidence, missing evidence, the cheapest valid experiment, and any impact on reserved final-test validity.

Maintain three statuses:

- **supported**: directly supported by appropriate frozen/final evidence;
- **qualified**: supported only on validation, limited datasets/axes, or descriptive analysis;
- **unsupported/contradicted**: do not claim.

If final test was already accessed, do not redesign the method from that holdout and rerun as if it were still untouched.

## 5. Draft from available evidence and the selected venue emphasis

Deliver writable text when requested; missing results do not justify invented numbers or citations. Mark pending evidence and constrain wording instead.

For empirical/algorithmic work, a useful neutral order is: Introduction, Related Work, Method, Experiments, Discussion/Limitations, Conclusion. Adapt section architecture to the selected venue and paper type rather than forcing the template.

Trace quantitative claims/tables to run or report IDs when practical. Keep terminology, equations/interfaces, figure/table references, abstract, contributions, and conclusion consistent with the current evidence state.

Figures/tables should answer a scientific question rather than decorate the paper: mechanism, consistency, trade-off, ablation, robustness, generalization, uncertainty, or resource cost as relevant. Journal- or discipline-specific figure/style preferences are not part of this core until separately validated.

## 6. Submission work only when requested

Prepare the needed subset of manuscript/source, figures, title page, highlights, cover letter, data/code availability, funding/COI/CRediT, AI-use declaration, checklist, and source archive. Verify current official author instructions when submission requirements matter.
