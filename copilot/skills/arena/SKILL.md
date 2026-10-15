---
name: arena
description: "Produce distinct candidates at the same task, pick a base, graft the strongest parts of the losers into it. Use for /arena, 'arena this', 'throw it in the arena', or when one attempt at a non-trivial artifact would lock in the wrong shape."
disable-model-invocation: true
---

# Arena

Open a todolist with one entry per phase (Frame, Fan out, Cross-judge, Pick, Graft, Verify) before launching anything.

## Phase A: Frame

Every candidate gets the same prompt, so the prompt is the contract.

1. State the artifact each candidate is producing.
2. Derive the rubric, 3-6 concrete gradeable criteria for what success looks like on *this* task. It is the picker's tool in Phase D. Candidates only see the task.
3. Pick at least two structurally distinct candidate directions. Produce them as sequential role passes in Copilot CLI, keeping each candidate's artifact and rationale separate. Do not claim independent model diversity from repeated passes on one model.
4. Give each candidate its own output location (a git worktree where possible, otherwise `.arena/<slug>/candidate-<n>/` under the work directory), per the **separate-before-serializing-shared-state** principle skill.

Cursor Task, per-role model rules, and background assumptions are removed; the exact original is archived at `../../../upstream/pstack/skills/arena/SKILL.md`. Delegation is optional only if the current host exposes a real suitable tool; follow its schema and permissions without assuming cloud, background, model, or reasoning controls.

## Phase B: Fan out

Run all N candidate passes sequentially, each with the task, the path to the shared grounding, its own output path, and instructions to produce the artifact and a short rationale naming the alternatives it considered and what it rejected. Finish and record one before starting the next.

If a candidate produces no output, proceed with N-1 and note the dropout.

## Phase C: Cross-judge

After all Phase B candidates complete, run a read-only judge pass. It sees the rubric and the candidates by path label, scores each criterion, and recommends a base with rationale. Keep its scoring separate from Phase D's maintainer-oriented reading. Do not describe a same-model judge pass as independent cross-model review.

## Phase D: Pick a base

Read every candidate end to end before picking. Score each against the rubric criterion by criterion, not on holistic feel, and compare with the cross-judge. Agreement on the base confirms the pick. Disagreement means one of you is biased or the rubric was ambiguous. Read both rationales before deciding.

Pick the base a future maintainer can extend most easily without breaking invariants. When two feel tied, prefer the cleaner boundary or smaller API, per the Laziness Protocol.

## Phase E: Graft

Walk each losing candidate once more for what is worth porting into the base, usually one or two things per candidate, not most of it. Fold each graft in by hand, per the **redesign-from-first-principles** principle skill, so the result stays coherent under one mental model. Don't paste mechanically.

If the candidates converge on one shape, that is strong agreement. Note it and ship the consensus shape. No graft is needed. If they wildly diverge, Phase A was under-specified. Reframe and re-run rather than averaging the divergence.

## Phase F: Verify

Verify the synthesized artifact like any other output, per the **prove-it-works** principle skill. If verification finds a problem the arena missed, either Phase A was wrong (re-frame and re-run) or a candidate caught it and you missed the graft (go back to Phase E). Don't paper over it.

## Outputs

One synthesized artifact, with a short synthesis note alongside naming the base and why, the cross-judge's verdict, each graft with its source candidate, what was rejected and why, any convergence or dropouts, and the verification result.
