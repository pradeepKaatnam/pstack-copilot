---
name: poteto-help
description: Guides users through pstack setup, /poteto-mode, and picking the skill, playbook, or principle for a task. Type /poteto-help with a question.
disable-model-invocation: true
---

# Poteto help

Answer the user's question about pstack, hand them a prompt they can send, and link the file the answer came from. For a help question, don't start the work. The user asked how, and a pstack run spends real tokens, so let them send the prompt.

A message that asks for work, such as "use pstack to fix this bug", is not a help question. Read [`poteto-mode`](../poteto-mode/SKILL.md) and do the work under it. Do not claim a Cursor Custom Mode is available in Copilot.

This file maps questions to the skills and guide pages that hold the answers. Those files own the details. Read the file you route to before you quote it, and trust it when it disagrees with this map. Link the local adapted file, not an upstream Cursor page presented as Copilot guidance.

Cursor installation, model-rule, Custom Mode, Task, and loop instructions are not portable. Their exact originals are archived at `../../../upstream/pstack/skills/poteto-help/SKILL.md`. This port targets Copilot CLI, uses sequential role passes by default, and does not assume VS Code or cloud hosts expose the same tools. Missing required MCPs, credentials, or specialist tools stop the affected workflow and must be reported unavailable. No automatic merge or auto-merge is authorized by a prompt recipe or unattended run.

## Find out what they need

Infer the need from the message and the conversation. A named situation, such as "which skill reviews a PR?", goes straight to its section. If the need is still unclear, ask one multiple-choice question with these options, then answer only the section they pick:

- Get set up
- Start a task with `/poteto-mode`
- Pick a skill for a situation
- Fix a run that went wrong
- Make pstack my own

Check the state that changes the answer, and mention it only when it does:

- No `.github/skills/verify-*/SKILL.md` or other app harness in the project means agents may have no scripted way to drive the app. Mention `/create-verification-skill` when the question is about proving a change works.
- A missing integration is an explicit gap, not permission to fabricate results. Model, reasoning, concurrency, and background options depend entirely on actual host capabilities, not Cursor rule files.

## Get set up

1. Install the adapted skill directories into the repository's `.github/skills/`, retaining each directory, `SKILL.md`, and its resources. Follow this port's installation documentation for any host-specific alternative.
2. Read [`setup-pstack`](../setup-pstack/SKILL.md) for the port's capability checks. Do not create Cursor model rules or infer Copilot controls from Cursor configuration.
3. Start a real task with `/poteto-mode`, a goal, and a check that can pass or fail.

These skills retain `disable-model-invocation: true` for explicit selection on supporting hosts. Skill discovery and invocation syntax are host-specific; if slash selection is absent, ask the assistant to read and follow the named installed `SKILL.md`. The adapted [setup skill](../setup-pstack/SKILL.md) and public [port README](https://github.com/pradeepKaatnam/pstack-copilot/blob/main/README.md) have the details. The pinned upstream [original setup chapter](https://github.com/cursor/plugins/blob/e5136d82418d2db3165ea1050d17577cd618cc05/pstack/docs/guide/01-setup.md) is historical Cursor reference only, not executable Copilot guidance. Offer to word their first prompt with them, per [`references/prompting.md`](references/prompting.md).

If cost is the worry, say where the tokens go and how to spend fewer: scoped reading, candidate passes, and review passes. Choose a smaller task scope or fewer optional candidate passes without dropping required verification. Model selection belongs to controls actually documented and exposed by the user's host. Save `/poteto-mode` for work that needs rigor.

The upstream was built for Cursor. This adaptation preserves the engineering guidance but replaces Cursor orchestration syntax with safe sequential role passes and inherited host settings. Native Copilot CLI does support delegation, model controls, and background tasks; these are optional capabilities, not APIs bundled or configured by this port. Use their actual exposed interfaces and ensure delegated roles receive the required repository instructions. Cloud plugin support is documented too, but this port does not claim integration-tested cloud execution. `make-bot-ui` is inactive because its private routine infrastructure is absent; `no-comments` stops unless its actual specialist and rules are exposed.

## Start a task with `/poteto-mode`

`/poteto-mode` matches the task to a playbook, copies the playbook's steps into the todo list, and runs the other skills as the steps need them. A step it skips stays in the list as `skip: <reason>`. A good prompt states the goal and how to tell it's done. It doesn't list skills, because a hand-written sequence tends to drop or reorder steps the playbook would keep. Read [`references/prompting.md`](references/prompting.md) before you help word one. The [prompt recipes](references/recipes.md) and adapted public [guide page 2](https://github.com/pradeepKaatnam/pstack-copilot/blob/main/copilot/docs/guide/02-poteto-mode.md) have examples.

Explicitly select `/poteto-mode` for each new task where the host supports slash skill selection, or ask to read and follow its installed `SKILL.md`. Do not promise persistent Custom Mode behavior. Mid-chat, "new task" makes the workflow match a fresh playbook. Run its role passes sequentially; delegation is optional only through tools the current host really exposes, with no assumed agent type, model, background, or cloud controls.

## Pick a skill

The default answer is `/poteto-mode`, which runs most of the others when its steps need them. Name a skill directly when the user wants more or less of something than the playbook gives. Read the skill before you recommend it, and give one example prompt.

| The user wants to | Skill |
|---|---|
| Do any non-trivial task with rigor | [`/poteto-mode`](../poteto-mode/SKILL.md) |
| Check that the agent understood their goal and the problem before it starts | [`/in-your-own-words`](../in-your-own-words/SKILL.md) |
| Aim a task higher before starting: more expert, more outcome-focused, not overspecified | [`/sharpen`](../sharpen/SKILL.md) |
| Know how code works now, or where new code should live | [`/how`](../how/SKILL.md) |
| Know why code is shaped this way, or where a number came from | [`/why`](../why/SKILL.md) |
| Understand a change or subsystem, explained plainly | [`/teach`](../teach/SKILL.md) |
| Catch up on their own recent work on a topic | [`/recall`](../recall/SKILL.md) |
| Catch up on what changed in this chat since their last message, in a few plain sentences and small visuals, with enough context to decide each action item | [`/ketchup`](../ketchup/SKILL.md) |
| Know what a small diff could break outside itself | [`/blast-radius`](../blast-radius/SKILL.md) |
| Settle types and module shape before code that crosses a function boundary | [`/architect`](../architect/SKILL.md) |
| Get several attempts at one brief, merged into the best one | [`/arena`](../arena/SKILL.md) |
| Cover scoped slices or candidate attempts and return one report | [`/swarm`](../swarm/SKILL.md) |
| Review a diff through adversarial role passes | [`/interrogate`](../interrogate/SKILL.md) |
| Fix a bug test-first when a cheap local test exists | [`/tdd`](../tdd/SKILL.md) |
| Apply TypeScript rules to `.ts` or `.tsx` work | [`/typescript-best-practices`](../typescript-best-practices/SKILL.md) |
| Audit comments when the actual Comment Sicko specialist is available, otherwise report unavailable | [`/no-comments`](../no-comments/SKILL.md) |
| Clean AI tells out of prose | [`/unslop`](../unslop/SKILL.md) |
| Write docs, an RFC, a README, a PR description, or a commit message to a standard | [`/technical-writing`](../technical-writing/SKILL.md) |
| Hear the last reply again in plain words | [`/bro`](../bro/SKILL.md) |
| Give agents a scripted way to drive the app and prove behavior | [`/create-verification-skill`](../create-verification-skill/SKILL.md) |
| Bring a verification skill and its feature map back in line with the app | [`/maintain-verification-skill`](../maintain-verification-skill/SKILL.md) |
| Vet a performance number before reporting or acting on it | [`/benchmark-checklist`](../benchmark-checklist/SKILL.md) |
| Run a large or cross-cutting change, or one to review after stepping away | [`/figure-it-out`](../figure-it-out/SKILL.md) |
| Keep a decision log during a run, and review it afterward | [`/show-me-your-work`](../show-me-your-work/SKILL.md) |
| Check host capabilities and port setup | [`/setup-pstack`](../setup-pstack/SKILL.md) |
| Turn their own working habits into a personal mode skill | [`/automate-me`](../automate-me/SKILL.md) |
| Turn what a finished task taught into skill edits | [`/reflect`](../reflect/SKILL.md) |
| Stop agents from repeating the same mistakes in this repo | [`/correct`](../correct/SKILL.md) |
| Learn why the upstream Grok Bot UI integration is unavailable in this port | [`/make-bot-ui`](../make-bot-ui/SKILL.md) |
| Find their way around pstack | `/poteto-help` |

If a skill directory next to this one is missing from the table, read its frontmatter and route by its description. The `principle-*` directories are covered under principles below.

Close calls:

- `/how` explains what the code does. `/why` explains the reasons. `/teach` runs one or both and explains the result plainly.
- `/arena` gives every worker the same brief and merges the best parts. `/swarm` splits work into slices or a race and returns one report.
- `/architect` implements right after it settles the design. Add "with checkpoint" to review the design before it writes code.
- `/interrogate` reviews the diff. `/blast-radius` looks for breakage outside the diff and proves the one fact that makes the change safe.
- `/recall` rebuilds context across recent chats. `/ketchup` covers only this chat since the user's last message. Resuming one specific chat or branch is the Session pickup playbook.
- `/figure-it-out` designs one rigorous run. The Orchestrate playbook runs a program that spans days and many PRs. The Autonomous run playbook drives one task to a finish condition.

Not in pstack:

- Upstream `cursor-team-kit` helpers are not bundled here. Use only an actual repository harness or exposed integration.
- Cursor `/loop` and `/create-skill` are not Copilot APIs. Use bounded sequential iterations and native skill authoring instead.
- pstack has no `/orchestrate` skill. Orchestrate is a `/poteto-mode` playbook. If the slash menu shows `/orchestrate`, another plugin provides it.

## Playbooks and principles

Playbooks are step lists inside `/poteto-mode`, not skills, so they have no slash command. Inside `/poteto-mode`, describing the task picks one, and these phrases name one directly:

- "babysit this pr" or "check on pr 123" runs Babysit. It drives the PR to merge-ready and stops there. It doesn't merge unless the user asks to merge, land, or ship.
- "land the stack" runs Shipping.
- "take over this branch" runs Session pickup.
- "pause safely" runs Pause safely.
- "full autopilot on this queue" runs Autopilot-full. "stack them, don't ship" runs Autopilot-stack.
- "run the eval playbook" runs Eval.

Without explicit skill selection, a phrase such as "babysit this pr" may not select the intended workflow. The Playbooks section of [`poteto-mode`](../poteto-mode/SKILL.md) lists every playbook and when it applies. The [opening a PR](../poteto-mode/playbooks/opening-a-pr.md), [babysitting](../poteto-mode/playbooks/babysit.md), and [shipping](../poteto-mode/playbooks/shipping.md) playbooks and adapted public [guide page 6](https://github.com/pradeepKaatnam/pstack-copilot/blob/main/copilot/docs/guide/06-verify-and-ship.md) cover these workflows. Shipping still requires explicit user merge authorization.

pstack has no standalone planning skill. Use only planning controls actually exposed by the current Copilot host. For work that spans phases or stacked PRs, asking `/poteto-mode` for a plan runs the [Multi-phase plan playbook](../poteto-mode/playbooks/multi-phase-plan.md), which writes the plan and doesn't implement it. For a design question, the Prototype playbook or `/architect` settles it in code first.

Principles are one-rule skills that `/poteto-mode` reads and cites in its replies. The user rarely invokes one. They steer with the names instead, as in "apply prove it works. show me the real output." Typing `/principle-<name>` still loads one on demand. Read the adjacent `principle-*/SKILL.md` files for the full rules; start with [Prove It Works](../principle-prove-it-works/SKILL.md), [Fix Root Causes](../principle-fix-root-causes/SKILL.md), and [Foundational Thinking](../principle-foundational-thinking/SKILL.md) as the task requires. The adapted public [guide page 8](https://github.com/pradeepKaatnam/pstack-copilot/blob/main/copilot/docs/guide/08-principles.md) lists the principles.

## Fix a run that went wrong

| Symptom | Fix |
|---|---|
| The workflow stopped applying after a few turns | Explicitly select the skill for the new task or ask to read and follow its installed `SKILL.md`. No persistent mode is promised. |
| A question got treated as the next step of the last task | Say "new task", or say the turn doesn't need the mode. |
| A requested per-role model choice had no effect | The host may not expose per-role model selection; do not expect Cursor rules to configure Copilot. |
| Runs cost more than expected | See the cost paragraph under Get set up. |
| A skill didn't load on its own | Explicitly select it; these skills retain manual-invocation metadata. Confirm the host discovers the installed skill directory. |
| Writers overwrote each other | Run sequentially by default. Optional real delegates need isolated ownership or worktrees; never assume a cloud machine. |
| An unattended run moved but finished nothing | Use bounded iterations and a check that can pass or fail, not a duration. See [Autonomous run playbook](../poteto-mode/playbooks/autonomous-run.md). The pinned upstream [original overnight chapter](https://github.com/cursor/plugins/blob/e5136d82418d2db3165ea1050d17577cd618cc05/pstack/docs/guide/07-overnight.md) is historical Cursor reference only, not runnable Copilot instructions. |
| The reply claims success from a green build | Ask for the real command, flow, stored value, or profile. That's the prove-it-works principle. |

For a run that drifts, [`references/prompting.md`](references/prompting.md) has one-line steers. The adjacent [prompt recipes](references/recipes.md) and adapted public [guide page 10](https://github.com/pradeepKaatnam/pstack-copilot/blob/main/copilot/docs/guide/10-recipes-and-pitfalls.md) have examples worth copying.

## Make pstack my own

- [`/automate-me`](../automate-me/SKILL.md) drafts a personal mode skill from the user's own history, to use alongside `/poteto-mode`.
- [`/reflect`](../reflect/SKILL.md) after a session turns its lessons into skill edits the user approves.
- `/poteto-mode write a skill for <workflow>` runs the authoring playbook. The eval playbook tests a skill change blind.
- Fix a misbehaving skill in its own PR, not inside the feature work where it went wrong.

The adapted [automate-me](../automate-me/SKILL.md), [reflect](../reflect/SKILL.md), and [skill-authoring playbook](../poteto-mode/playbooks/authoring-a-skill.md) cover these workflows. The pinned upstream [original customization chapter](https://github.com/cursor/plugins/blob/e5136d82418d2db3165ea1050d17577cd618cc05/pstack/docs/guide/09-make-it-yours.md) is historical Cursor reference only, not executable Copilot guidance.

## Reply

Lead with the answer. Give at most one example prompt in a code block, adapted from [`references/recipes.md`](references/recipes.md) when one fits, then the link to that file. Keep it short unless the user asked for the whole map.
