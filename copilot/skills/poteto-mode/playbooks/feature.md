### Feature

**You own the design. Plan, review, verify.** Separate implementation and review roles, sequentially by default under `../SKILL.md`.

1. `how` over the affected subsystem.
2. `architect` for competing design exploration. Compare alternatives sequentially unless real supported delegation is available.
3. Write the throughput checkpoint as four todo items. A dimension that genuinely does not apply (single file, no fan-out) keeps its item with `n/a: <reason>` rather than being dropped:
   - **Blocking first steps.** Gates run before fan-out.
   - **Independent workstreams.** Disjoint files, services, or layers parallelize. Shared writes serialize.
   - **Shared mutable state.** Default to splitting the target (the **separate-before-serializing-shared-state** principle skill). Serialize only for real invariants.
   - **Smallest safe decomposition.** If one worker is best, name why.
4. Scope the implementation role with file paths, success criteria, and a named data shape per **principle-model-the-domain** before logic. Prefer state machines over scattered booleans, tables or registries over branching, and typed models over repeated assumptions. When multiple shapes are valid, use **arena** to compare alternatives and separate the selection review from implementation. Run roles sequentially by default. Optional delegation uses only real host controls, never an inert configured-model table. Own the diff directly when delegation is unavailable or forbidden and disclose review independence limits. Follow **Comments**, make surgical edits, re-ground upstream-derived files, port shared-primitive improvements to every consumer, and verify each.
5. Verify on the matching surface. "Inconclusive" or wrong-surface is not a pass. Flag it.
6. Rebase into small, ordered commits. Stack follow-ups.
   Use the **sequence-verifiable-units** principle skill, building, verifying, and committing each small unit before the next.
7. If the design is contested, `interrogate` before shipping.
8. Run **Opening a PR**.

Code-coupled work goes to a single owner with the checkpoint inline. Shared writes serialize. Independent artifacts can be partitioned if supported, but sequential roles remain the default. Rewrite the checkpoint at phase boundaries and carry consolidated instructions into every new invocation.

**Reply:** what you built, what you chose and why, the throughput checkpoint, open decisions. Tables for design alternatives.
