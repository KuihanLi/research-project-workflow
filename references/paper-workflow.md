# Paper and Submission Workflow

Load for manuscript structure/drafting/revision, claim audit, venue selection, recent literature delta, or submission work. Do not rerun audits every turn unless scope, evidence or publishing landscape changed.

## 1. Choose venue family before locking a manuscript frame

Unless venue-neutral drafting is explicitly requested, first summarize the real surviving problem, **selected IDEA/claim version and its lineage**, algorithm/system/measurement emphasis, independent evidence level, resource/coverage/robustness limits, and evidence gaps. Search current official scope/instructions and recent related work; shortlist roughly 2–4 plausible venues by contribution-type fit, experimental burden, related published work, official constraints and practical submission conditions. Choose primary and fallback; keep scientific facts invariant across narratives. If no candidate fits, narrow the claim or collect evidence rather than forcing a publication frame.

## 2. Literature at manuscript stage is a delta audit

A new or materially changed branch claim should already have passed a proportional pre-experiment novelty and practical strong-baseline check. Update for publication changes, closest-prior overlap, changed mechanism/domain, and claim drift; never invent “first” novelty after the fact. For surviving branches distinguish an integrated contribution from a bundle of unrelated modules.

## 3. Protocol-honest comparisons

**Strict-protocol** baselines match inputs, split, supervision, resource and evaluation semantics; **method-native literature** comparisons can be relevant but are not numerically equivalent. Prefer official code with traceable adaptations. Retain stronger simple baselines and scope-limiting negative results. If baseline viability was not validated before the campaign, mark the debt rather than hiding it.

For merged IDEA branches, distinguish effects of each component, combined A+B and a strong simpler alternative using controlled contrasts. Never treat a post-hoc best slice per branch as a preplanned universal result.

## 4. Claim-to-evidence closure across branch revisions

Map each material final claim to: `idea_id`, `claim_version`, differentiating technical action, relevant prior-art delta, provenance/run IDs, data split and evidence class, prespecified metrics, target deployment domain/coverage, worst important subgroup risks, resource cost and known contradictions.

Classify:

- **supported**: directly by appropriate independent frozen/final evidence for that exact claim version and target domain;
- **qualified**: validation, diagnostic, observational or selected post-hoc exploration only;
- **unsupported/contradicted**: don't claim.

Final-test driven pivots produce new exploratory claim versions; the old final observations cannot become independent confirmation for the new idea. Claims of causal mechanism require appropriately distinguishing evidence; statistical correlation does not suffice. Conditional average gain does not mean every subject or unseen condition improves.

## 5. Write from the actual surviving contribution

Use a venue-appropriate structure; for empirical work Introduction, Related Work, Method, Experiments, Discussion/Limitations and Conclusion are a neutral starting point. Trace numbers and tables to run/report IDs where practical; align abstract, conclusions, figures and terminology. Existing data gaps must be labeled, never filled by invented measurements or citations. Figures should resolve a scientific question (mechanism, stability, robustness, conditional coverage/risk, ablation or cost), not decorate the text.

Describe branch pivots honestly when their selection history changes the strength of evidence. A narrower but realistic conditional-domain contribution can be useful, but its coverage and risks must be visible. Preserve negative results that materially qualify the paper.

## 6. Submission only when requested

Prepare the needed subset of source, figures, title page, highlights, cover letter, data/code availability, funding/COI/CRediT, AI-use declaration, checklists and archive. Check current official instructions when submission details matter. Journal-specific prose/figure-style guide extraction remains outside this core unless separately validated and reopened.
