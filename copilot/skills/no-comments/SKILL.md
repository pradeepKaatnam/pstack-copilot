---
name: no-comments
description: "Review comments through an explicitly available Comment Sicko specialist, fix accepted findings, and offer encodings for claimed constraints. Stop if that specialist is unavailable."
disable-model-invocation: true
---

# No comments

This workflow requires the actual Comment Sicko specialist and its complete rules. If the current host does not explicitly expose it, STOP and report `/no-comments` unavailable; do not invent its deletion rules or substitute blanket comment removal. The Cursor-specific invocation is removed; exact originals are archived at `../../../upstream/pstack/skills/no-comments/SKILL.md`.

When that specialist is genuinely available, run it through the host's actual supported interface and act on accepted findings. Do not assume a Task API, model selection, reasoning controls, or background execution.

Defer to Comment Sicko's fresh perspective.

## Scope

Use the caller's files or diff. Otherwise use the current diff against the base branch, default `main`, including the working tree.

## Steps

1. Confirm the specialist and its rules are actually available, then pass the scope through the real host-exposed interface. Otherwise stop without deleting comments. Do not restate or invent its rules.
2. Inspect its report and diff. Reject application-code edits, scope escapes, exception-protected deletions, misstated `MUST KILL` reasons, and flags that treat kept intentional code as guilty. Reshape flags on our-code surprises stay actionable. Do not restore those comments. A keep survives only with proof it is about something we cannot change. Audit missed scoped lint and TypeScript suppressions. Correctness or safety suppressions stay actionable `MUST KILL`s. Restore deletions only with exact exceptions and scoped proof. Before accepting thin `IMPORTANT` or `do not remove` kills or keeps, run `/how` or `/why` on their symbol. If a kill is ambiguous, do not restore. If a keep is refuted or still ambiguous, delete it. Revert and rerun one rejected report with the failure named. Reject a second, report it open, and fail `/no-comments`.
3. Fix trivial accepted flags directly by deleting a dead path, dropping a parameter, or using the real API. If any fix needs a shape, run `/architect` once for the accepted set and surrounding code. Stop at the sketch. Architect shapes. Step 4 implements.
4. Implement the smallest root-cause fix in scope. Remove every named workaround. If the root cause is out of scope, land the smallest in-scope fix and report the rest open. The **principle-fix-root-causes** and **principle-redesign-from-first-principles** skills guide intent only. Neither authorizes widening the fence nor fixing instances outside it. Never bolt on symptom guards.
5. Constraint comments say `do not remove`, `do not change wording`, or `talk to X before changing`. Leave keeps about things we cannot change. Offer the cheapest in-scope type, runtime, test, or CI lint. Wait for interactive approval. Unattended and eval require caller pre-approval. If approved, encode then delete. Otherwise retain the constraint comment, report it open, and sketch out-of-scope work; lack of approval does not authorize deleting a safety constraint.
6. Report the deletion count, restored comments, reruns, architect sketch, fixes, encoding offers, encodings, unenforced constraints, and other open work.
