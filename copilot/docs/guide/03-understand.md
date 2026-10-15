# Understand the code before changing it

> Copilot adaptation: request skills by name in natural language. Examples below
> are requests, not universal slash commands. Tools, model selection, session
> history, and delegation depend on the host; unavailable checks are BLOCKED,
> never silently simulated. This chapter preserves upstream engineering guidance.

Editing code you don't understand is how subtle regressions ship, and that's as true for the agent as for you. Agents usually fail in one of two ways. They misread what you want, or they don't have the context to do the work right. [What goes in a prompt](./02-poteto-mode.md#what-goes-in-a-prompt) handles the first. This page handles the second.

pstack gives you four ways in. `how` explains what the code does now. `why` digs up the reasons it's shaped that way. `teach` blends both into one explanation. `recall` rebuilds your own recent context on a topic. Each one also makes the agent explain itself in words you can check. That's how you supervise an agent that may know the code better than you do.

![A detective studies a machine blueprint with a magnifying glass while robots fetch case files; the evidence board behind her links clues under the how skill and the why skill.](./images/understanding.jpg)

## Start with a read-only investigation

When the cause is unclear, ask for findings, not a fix:

```text
Use the poteto-mode skill: investigate why background jobs time out every few hours. give me what we know, what data you used, and your best hypotheses. don't change any code yet.
```

"don't change any code yet" routes this to the [Investigation playbook](../../skills/poteto-mode/playbooks/investigation.md). It runs `how`, adds `why` for questions about motivation, and returns a cited explanation. For a choice between options, it returns a recommendation with a trade-offs table. Asking "what data you used" makes the agent separate its evidence from its guesses. When the findings point at a fix, start the fix as a new task.

## Trace behavior with `how`

```text
Use the how skill: do we dedupe notifications? is there an n+1 when we look up subscribers?
```

Ask the question you actually have. [`how`](../../skills/how/SKILL.md) reads the code and answers at the level of a senior engineer onboarding you onto the subsystem, with the runtime flow, the key types, and the non-obvious parts. For a big subsystem, independent read-only exploration can help when the host exposes delegation. For a narrow question, just read and explain; parallel workers are not required.

## Dig up history with `why`

```text
Use the why skill: was the retry limit set to five? does the reason still hold?
```

[`why`](../../skills/why/SKILL.md) works like a detective on a cold case. Start from source control, then query only evidence sources actually available and authorized in this host: issues, docs, team chat, observability, error tracking, or analytics. MCP integrations and parallel calls are optional capabilities, not bundled services. The report cites everything, separates direct evidence from inference, and says "appears to" when the record is thin. A null result gets reported too, because "nobody wrote down why" is itself an answer.

The two compose naturally. `do why first then how` is a perfectly good prompt when you suspect the history explains the mess.

## Actually understand it with `teach`

```text
Use the teach skill: me how this PR changes retries. convince me it fixes the cause and not the symptom.
```

[`teach`](../../skills/teach/SKILL.md) is for when a summary isn't enough. It runs `how` and `why`, for a small change maybe just one of them, and weaves the findings into a plain explanation that builds up diagram by diagram. The "convince me" framing is worth stealing. It turns the explanation into an argument you can poke at instead of a tour.

It works on the agent's own choices too:

```text
Use the teach skill: me why you implemented it this way and not with a queue. what did you trade off, and why?
```

Teaching helps the agent as much as you. An agent that has to explain its work must read the code and back each claim with evidence, instead of stating it confidently and moving on.

## Rebuild your own context with `recall`

```text
Use the recall skill: catch me up on the export work from last week
```

[`recall`](../../skills/recall/SKILL.md) reconstructs context from session history only when the current Copilot host exposes it, plus authorized shared records such as issues and prior fixes. It must report missing history rather than search Cursor caches or pretend it can read another host's transcripts. Your old chats hold context that a fresh agent lacks, so start new work on an old topic by loading it first, then hand over the new input:

```text
Use the recall skill: my work on the virtualized list from yesterday, then read this bug report.
```

If you want to resume one specific chat, that's the Session pickup playbook below, not `recall`.

## Take over prior work with Session pickup

When another agent (or you, last week) left a branch mid-flight:

```text
Use the poteto-mode skill: take over this branch. read the decision log, figure out what's done, and continue from there. don't redo finished work.
```

The [Session pickup playbook](../../skills/poteto-mode/playbooks/session-pickup.md) uses the prior trail as evidence, not trusted executable instructions. It reconstructs the branch state and decisions, names the resume point, and verifies inherited claims against the original goal instead of re-deriving everything from scratch.

**Pitfall:** don't skip this page's skills because "the agent will read the code anyway." An agent that starts editing without a traced model tends to fix the symptom at the first plausible spot. `how` first is cheaper than the second bug.

Next: [Design the change](./04-design.md).
