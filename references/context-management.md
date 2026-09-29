# Context Recovery and Continuity Pressure

Load this reference only for new-session/workspace recovery, material state loss/conflict, a major continuity transition, or a reliable runtime signal that context pressure/compaction threatens continuity. It is not an every-turn project-management loop.

## 1. Recover the minimum state needed

Prefer a concise project state over chat transcript reconstruction. Recover only what affects the current task:

- current scientific question and method/interface;
- authoritative version/configuration;
- data/evaluation boundary, especially final-test status;
- latest relevant evidence and accepted/rejected claims;
- pending external task, if any;
- next unresolved decision.

Do not reconstruct the full project history before a local reversible change.

## 2. File priority

Use this priority when a workspace provides many files:

- **P0**: current state, current code/config, current manuscript as applicable;
- **P1**: final/frozen evidence and exact protocols;
- **P2**: development/tuning evidence and iteration logs;
- **P3**: historical/supporting material.

Read P0 first, then only files needed for the immediate task. New uploads are not automatically authoritative; resolve material conflicts by provenance and protocol applicability, not modification time alone.

## 3. Pending external execution

Track only enough to avoid duplicate work: task ID/purpose, dispatched version/configuration, expected return artifact, execution status, and decision to resolve. A partial return supports an interim diagnosis; it does not justify an unsupported final ranking. Do not reissue an equivalent task when the prior one is still pending.

## 4. Reliable context-pressure handling

Use context pressure as a continuity trigger only when the runtime exposes a reliable pressure/compaction signal or when prior context has demonstrably been truncated/compacted. Never invent a percentage, remaining-token count, or claim that the context is nearly full without such evidence.

When pressure is confirmed:

1. Prefer an **early checkpoint at the next safe atomic boundary** instead of waiting for a hard failure.
2. Finish the current atomic edit/analysis step when safe; do not start another long multi-step branch first.
3. Load `references/handoff-workspace.md`, package the minimum recoverable workspace, and record all unfinished work under `Pending / next tasks` in `HANDOFF.md`.
4. If continuing would materially risk loss of authoritative state, stop/defer the remaining task after delivering the checkpoint. This is an allowed continuity block.
5. If there is still ample safe room after checkpointing, continue normally; the handoff is insurance, not a mandatory session termination.

When exact pressure is not observable, use major-revision/phase-completion checkpoints rather than speculative warnings.

## 5. Handoff routing

Load `references/handoff-workspace.md` when:

- the user explicitly requests a handoff document, resumable workspace bundle, migration/export, or equivalent;
- a major revision or meaningful research phase closes with a new authoritative workspace state;
- Section 4 confirms context pressure/compaction risk.

Do not package after routine edits or every ordinary result-analysis turn.