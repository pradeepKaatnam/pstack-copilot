### Autonomous run

**You own the exit condition. Define done, then drive to it without stopping.**

1. State a checkable exit predicate before the first iteration (tests green, repro fixed, all N PRs merge-ready, pixel-diff zero). Merging is reserved for the operator.
2. Run bounded foreground iterations with a stated time or iteration budget and durable checkpoints. The Cursor scheduler is inactive, not mapped to a Copilot wake API. For CI, the standalone watcher can poll with a finite timeout. If the host cannot keep running, report the checkpoint and exact next action instead of promising background work.
3. Each iteration makes the smallest change the evidence justifies, verifies it against the predicate, commits if it advanced, discards changes that didn't help. Belt-and-suspenders that "might help" gets reverted, not left to ride.
   Sequence the work via the **sequence-verifiable-units** principle skill, verifying each unit before the next instead of batching checks at the end.
4. Address related blockers within scope, but record unrelated discoveries as follow-ups. Do not expand an autonomy grant into external actions or approvals. Surface irreversible actions, genuine product choices, permission limits, or a dead end. Keep the predicate as the main drive.
5. Checkpoint every iteration via the **show-me-your-work** skill, a row for what changed and whether the predicate moved.
6. Stop when the predicate is met, the operator stops you, the budget expires, or a genuine gate blocks progress. Pivot past a plateau within the budget. Never relax the predicate or claim completion when blocked.

**Reply:** the exit condition, iterations run, what landed, what was discarded, final predicate state.
