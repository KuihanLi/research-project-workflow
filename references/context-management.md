# Context Recovery and Handoff

Load this reference only for new-session/workspace recovery, material state loss/conflict, explicit handoff/export, or a major continuity transition. It is not an every-turn project-management loop.

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

- **P0**: current state/handoff, current code/config, current manuscript as applicable;
- **P1**: final/frozen evidence and exact protocols;
- **P2**: development/tuning evidence and iteration logs;
- **P3**: historical/supporting material.

Read P0 first, then only files needed for the immediate task. New uploads are not automatically authoritative; resolve material conflicts by provenance and protocol applicability, not modification time alone.

## 3. Pending external execution

Track only enough to avoid duplicate work: task ID/purpose, dispatched version/configuration, expected return artifact, execution status, and decision to resolve. A partial return supports an interim diagnosis; it does not justify an unsupported final ranking. Do not reissue an equivalent task when the prior one is still pending.

## 4. Event-driven handoff

Create or refresh a handoff when the user requests it or when continuity risk is real, such as:

- major phase/method/evaluation boundary changes;
- frozen final plan or completed final evidence;
- large result matrix closure;
- imminent new session/context reset;
- material contradictions or state loss.

Do not count replies or tokens to trigger handoff work. Do not interrupt active work solely to refresh state.

## 5. Handoff contents

A compact handoff should contain only what another session needs to continue safely:

1. objective and current conclusion;
2. current method/interface and authoritative version;
3. data/evaluation/final-test boundary;
4. evidence summary with development vs final distinction;
5. key decisions, rejected paths, and claim limits;
6. workspace inventory with P0-P3 priority;
7. pending external tasks;
8. next allowed/actionable step;
9. short starter prompt.

Include actual available artifacts when portability is requested. Never claim local-only or unreturned external outputs were exported. Exclude credentials and unnecessary raw data.
