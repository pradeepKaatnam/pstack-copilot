# Recipes and pitfalls

> Copilot adaptation: request skills by name in natural language. Examples below
> are requests, not universal slash commands. Tools, model selection, session
> history, and delegation depend on the host; unavailable checks are BLOCKED,
> never silently simulated. This chapter preserves upstream engineering guidance.

Prompts worth copying, then the mistakes everyone makes once. Swap in your own paths and finish conditions. The recipes are deliberately informal. That's how they get typed in practice, and the skills read intent fine.

![She tastes a finished dish while robots cook from a recipe box, with pinned cards bearing original Cursor skill and loop labels above the counter.](./images/recipes.jpg)

## Understand an unfamiliar subsystem

```text
use the how skill first to understand how this initialization works. then use the why skill to figure out why it broke recently.
```

Mechanics first, history second. Require each report to identify the authorized sources it actually searched and the sources it could not access.

## Restate a noisy report before touching code

```text
Use the poteto-mode skill: read this thread. restate the underlying issue in your own words, in plain english. don't change any code yet.
```

A misreading shows up in the restatement, where it costs one message to correct. Keep your own theory to yourself until the agent has stated its own.

## Prototype before you pick

```text
Use the poteto-mode skill: prototype a few options for the settings layout. put them behind a switcher and send me screenshots of each.
```

You pick from things that run, not from descriptions. The agent answers its own layout and timing questions along the way.

## Turn a settled design into a plan

```text
Use the poteto-mode skill: turn this design into a plan. small verifiable PRs, each with its own proof.
```

Ask only after the design settles. The plan is the deliverable, and it names the playbook that will execute it.

## Get a second opinion on a design

```text
ask the arena skill for a second opinion on this thread and our approach
```

Your current design becomes one candidate among several, and the synthesis tells you whether the panel found something better or confirmed what you had. Cheap insurance before a costly commitment.

## Check independent slices in parallel

```text
Use the swarm skill: check every package under packages/ against its check.sh. one worker per package. one report.
```

If the host exposes delegation, each worker owns one package and the parent accounts for every slice. Otherwise check the packages serially. Return PASS, ISSUES, or BLOCKED, including missing coverage, rather than pretending workers ran.

## Review a branch skeptically

```text
Use the interrogate skill: the whole branch, but skeptically. don't change anything yet. no nitpicks unless it's an actual bug or regression in behavior.
```

The qualifiers do real work. "don't change anything yet" keeps it read-only, and the nitpick rule pre-filters the noise so `Act on` findings are worth your time.

## Fix a bug through a failing test

```text
Use the poteto-mode skill: repro the duplicate write first. if there's a cheap test path, the tdd skill it. then fix and rerun.
```

"if there's a cheap test path" matters. Forcing a test through brittle mocks proves less than running the real command, and the playbook is allowed to say so.

## Repro and fix a report with proof

```text
Use the poteto-mode skill: repro this with the verify-<app> skill. if it repros on main, fix it and show me a video as proof.
```

"if it repros on main" lets the run stop early when the bug is already gone. The video lets you check the fix before you read the diff.

## Vet a number before you post it

```text
Use the benchmark-checklist skill: vet this 40% speedup before it goes in the pr description
```

You get faster, slower, no measurable difference, or inconclusive, with the run count, the range, and what limits the number.

## Stop correcting the same mistake

```text
Use the correct skill: agents keep adding new config flags without registering them in the schema
```

The fix lands in the repo as architecture, a type, a lint, or a test, so the next agent can't make the mistake.

## Ask how without starting the work

```text
Use the poteto-help skill: how do i explicitly reuse poteto-mode in this host?
```

You get an answer, a prompt to send, and a link to the source. Nothing runs until you send that prompt.

## Keep a run honest while you're away

```text
Within this authorized session, work until every fixture passes or a genuine permission or environment blocker prevents progress. Keep an evidence-linked decision log. Do not merge or deploy.
```

This is a request for bounded work within the current authorized session, not a scheduler or guarantee of unattended execution. Define stop conditions, credentials, and permitted writes explicitly. The [original overnight page](https://github.com/cursor/plugins/blob/e5136d82418d2db3165ea1050d17577cd618cc05/pstack/docs/guide/07-overnight.md) depends on Cursor loops and Projects and remains inactive reference material.

## Redirect a drifting run

Steering prompts are one line:

```text
i said the goal is to repro. i did not ask for a fix yet.
```

```text
apply prove it works. show me the real output, not the build log.
```

```text
Use the unslop skill: that, no emdashes
```

You rarely need more words. You need the right name, and [the principles page](./08-principles.md) is the vocabulary.

## Get the reply in plain words

```text
Use the bro skill:
```

That's the whole prompt. [`bro`](../../skills/bro/SKILL.md) restates the last message like one human talking to another, no jargon, shorter. Use it when a reply is technically thorough and you still don't know what it said.

## The pitfalls

- **Enumerating skills in the prompt.** "use the how skill then the architect skill then the arena skill" reorders steps the playbook already sequences. State the goal and constraints. Name a skill only to override a default.
- **A vague finish condition.** "make it better" gives `loop` nothing to check. Give a command or artifact that can pass or fail.
- **Leading with your theory of the cause.** The agent searches wherever you pointed. Ask it to restate the problem first, then share your hunch.
- **Taking the first design.** One attempt locks in the first shape the model thought of. Ask for prototypes or `architect` and pick from evidence.
- **Polishing an abstract plan.** Adversarial review of a plan with no code behind it invents risks that will never happen. Settle the open questions with prototypes, then review what got built.
- **Parallel agents in one worktree.** They overwrite each other and the diff becomes archaeology. Run them as cloud agents, or say "own worktree per attempt".
- **Looping before you trust the loop.** A loop that can't verify its own work only makes unchecked work faster. Get the verification skill working first.
- **Trusting an unvetted number.** A warm cache or a skipped code path can fake a speedup. Run `benchmark-checklist` before the number goes anywhere.
- **Correcting the same mistake by hand.** A correction in chat helps one run. `correct` fixes the repo so no later run repeats it.
- **Using `arena` for coverage.** `arena` repeats one design or code brief, then picks a base and grafts the best parts. `swarm` partitions slices or declared race arms and aggregates one report.
- **Accepting every review comment.** Bots and humans both file real catches and noise in one list. `interrogate` sorts findings into act-on and dismissed buckets with reasons, and you can override either way.
- **Assuming a portable model router.** This pack does not translate Cursor model-role rules into guaranteed Copilot routing. Use only the actual host model picker or documented configuration; never invent model slugs.
- **Reporting success off a green build.** A build proves it compiles. Ask for the real command, flow, stored value, or profile, and expect the evidence in the reply.
- **Skipping skill validation.** Follow the [authoring playbook](../../skills/poteto-mode/playbooks/authoring-a-skill.md), check frontmatter, relative links, and host compatibility, and review the actual output. No Cursor create-skill built-in is assumed.

That's the adapted guide. If you skipped ahead, go back to the [guide index](./README.md) and run one small real task using the host installation instructions. The habits stick from use, not from reading.

Back to the [guide index](./README.md).
