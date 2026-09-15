# Paper and Submission Workflow

Load this reference for manuscript drafting/revision, claim/novelty/baseline audit, venue selection, or submission work. Reuse it after loading; do not rerun literature/claim audits every turn unless evidence or positioning changed.

## 1. Position from evidence

For a venue-neutral draft, use a conventional research structure and proceed. When venue selection or a named venue is in scope, assess only relevant constraints: scope fit, novelty expectation, systems vs algorithm emphasis, baseline/evidence expectations, public data/code expectations, and current page/format/submission rules.

Rank venue fit against the actual evidence, not prestige alone.

## 2. Novelty audit only when the claim needs it

When contribution/novelty wording, venue positioning, or final submission is in scope, search recent work around the exact task, closest mechanism, methodological analogues, and any efficiency/generalization claims being made.

For each decisive paper capture:

- what is already known;
- what is similar but not identical;
- whether official runnable code exists when reproduction matters;
- which proposed claim it weakens or rules out;
- the narrower safe differentiator that remains.

Do not make this search a prerequisite for unrelated implementation, debugging, result interpretation, or provisional drafting.

## 3. Baseline audit when comparison claims depend on it

Separate:

- **strict-protocol baselines**: compatible with the same input/split/evaluation semantics and suitable for numerical main tables;
- **method-native literature comparisons**: require incompatible inputs, preprocessing, supervision, resources, or datasets and should be discussed rather than misrepresented as equivalent reproductions.

Prefer official implementations when practical and record material adaptations. A stronger baseline stays visible and should narrow or sharpen the contribution.

## 4. Claim-to-evidence closure

Before final claims or new expensive confirmation, map each material claim to existing evidence, missing evidence, the cheapest valid experiment, and any impact on reserved final-test validity.

Maintain three statuses:

- **supported**: directly supported by appropriate frozen/final evidence;
- **qualified**: supported only on validation, limited datasets/axes, or descriptive analysis;
- **unsupported/contradicted**: do not claim.

If final test was already accessed, do not redesign the method from that holdout and rerun as if it were still untouched.

## 5. Draft from available evidence

Deliver writable text when requested; missing results do not block a provisional manuscript. Mark pending evidence and constrain wording instead of inventing numbers or citations.

For empirical/algorithmic work, a useful default order is: Introduction, Related Work, Method, Experiments, Discussion/Limitations, Conclusion. Adapt to the paper type and venue rather than forcing the template.

Trace quantitative claims/tables to run or report IDs when practical. Keep terminology, equations/interfaces, figure/table references, abstract, contributions, and conclusion consistent with the current evidence state.

Figures/tables should answer a scientific question rather than decorate the paper: mechanism, consistency, trade-off, ablation, robustness, or resource cost as relevant.

## 6. Submission work only when requested

Prepare the needed subset of manuscript/source, figures, title page, highlights, cover letter, data/code availability, funding/COI/CRediT, AI-use declaration, checklist, and source archive. Verify current official author instructions when submission requirements matter.
