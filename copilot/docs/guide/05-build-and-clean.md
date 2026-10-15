# Build the change and clean the diff

> Copilot adaptation: request skills by name in natural language. Examples below
> are requests, not universal slash commands. Tools, model selection, session
> history, and delegation depend on the host; unavailable checks are BLOCKED,
> never silently simulated. This chapter preserves upstream engineering guidance.

The build playbooks share one discipline. Say what you observed, let the playbook demand the evidence. This page shows what to put in the prompt for each common build task, then the cleanup habit that keeps diffs reviewable.

## Prompt each build playbook with what you know

A bug prompt states the symptom and asks for a reproduction first:

```text
Use the poteto-mode skill: this command emits two records after a retry. repro first, then fix and verify.
```

A feature prompt states the behavior and what must not change:

```text
Use the poteto-mode skill: add a --json flag. text output stays byte-identical. verify both forms.
```

A refactoring prompt pins behavior before structure moves:

```text
Use the poteto-mode skill: move parsing into one module, zero behavior change. record the current output first and prove it's unchanged after.
```

A perf prompt states the measurement, not a vibe:

```text
Use the poteto-mode skill: startup takes 1.8s on this fixture. trace it, fix the measured cause, show me before and after.
```

Each of these routes to its playbook ([Bug fix](../../skills/poteto-mode/playbooks/bug-fix.md), [Feature](../../skills/poteto-mode/playbooks/feature.md), [Refactoring](../../skills/poteto-mode/playbooks/refactoring.md), [Perf issue](../../skills/poteto-mode/playbooks/perf-issue.md)), and the playbook supplies the steps you didn't type: reproduce before fixing, name the data shape before implementing, pin behavior before restructuring, profile before optimizing.

For sustained improvement of one number, there's the [Hillclimb playbook](../../skills/poteto-mode/playbooks/hillclimb.md). Give it the metric, a target, and a floor on attempts, and it loops one hypothesis at a time with a frozen measurement harness. It keeps wins and reverts everything else.

Both perf playbooks run [`benchmark-checklist`](../../skills/benchmark-checklist/SKILL.md) on their numbers. Perf issue vets its baseline and every number after it, and Hillclimb vets its harness before freezing it. [Verify and ship](./06-verify-and-ship.md#vet-a-measured-number-with-benchmark-checklist) shows when to type it yourself.

Sometimes you want the cause before any fix. For a live symptom, such as a leak, an idle CPU spin, or a visual glitch, the [Runtime forensics playbook](../../skills/poteto-mode/playbooks/runtime-forensics.md) instruments the running process. For a profile you already captured, the [Trace forensics playbook](../../skills/poteto-mode/playbooks/trace-forensics.md) reads the artifact and maps the hot frame to source. Both return a diagnosis, not a fix:

```text
Use the poteto-mode skill: here's a cpuprofile from the slow startup. tell me where the time goes and which source lines own it. no fix yet.
```

## Write the failing test first with `tdd`

When a bug has a cheap local test path, the whole prompt can be two words:

```text
Use the tdd skill: implement
```

In context, that's enough. [`tdd`](../../skills/tdd/SKILL.md) writes the smallest test that fails for the intended reason, then the fix, then reruns the test. If a test would need broad harness setup or brittle mocks, the skill says so and uses the closest executable check instead. Don't force a test where a real command is stronger evidence.

## Load the TypeScript rules by name

[`typescript-best-practices`](../../skills/typescript-best-practices/SKILL.md) turns the type-system principles into concrete rules: discriminated unions, `unknown` at boundaries, exhaustive variants, schema-derived types. Ask explicitly to use this skill when a task touches `.ts` or `.tsx` files; automatic skill selection varies by host.

## Clean before you commit

Before committing, review the diff and apply the [unslop skill](../../skills/unslop/SKILL.md) to PR and commit prose. Cursor's external deslop dependency is not bundled or required in this port. Ask for its engineering outcome directly: remove narrating comments, unsupported guards, dead compatibility paths, and unrelated edits. Keep necessary correctness checks and unrelated existing code intact.

For prose, `unslop` takes a target and any extra rules you have:

```text
Use the unslop skill: the readme changes, no emdashes
```

You'll develop your own shorthand. The skill reads intent fine from terse prompts like `unslop that, tighten it`.

## Strip the comments with `no-comments`

Comments need their own pass, and not from the agent that wrote them. An author defends its comments the way you'd defend yours. So before review, hand them to fresh eyes:

```text
Use the no-comments skill: the diff
```

[`no-comments`](../../skills/no-comments/SKILL.md) can use [Comment Sicko](../../agents/comment-sicko.agent.md), a read-only reviewer with a short keep list: license headers, doc comments on a public API, links that explain what code can't, behavior forced by an external dependency you can't reshape. Everything else goes. A surprise in your own code gets no such pass. The comment comes back as a refactor flag, and `no-comments` fixes the flags it accepts at the root cause. When a comment claims a constraint, "do not remove", the skill offers to encode the claim as a type, test, or lint. Either way, the comment comes out. These are the reviewer's recommendations: accepted deletions and root-cause changes belong to the caller, not the read-only reviewer, and remain subject to permission gates.

Keep the division of labor clear: review code for unnecessary complexity, use unslop for prose, and have a fresh read-only reviewer inspect comments when available. If delegation is unavailable, do a separate review pass and state that limitation.

**Pitfall:** cleanup is not optional polish. A diff with narrating comments and defensive dead weight reads as unfinished to reviewers, and the extra code is where the next bug hides. If the diff feels padded, say `deslop it` before you commit, not after review calls it out.

Next: [Verify and ship](./06-verify-and-ship.md).
