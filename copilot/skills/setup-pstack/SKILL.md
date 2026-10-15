---
name: setup-pstack
description: Choose the actual Copilot CLI model and explicit per-invocation role preferences without creating an unused configuration file. Use for setup-pstack, configure pstack models, or changing model choices.
---

# Setup pstack

The original Cursor always-applied rule and model-slug rewriting workflow are inactive. Source-repository provenance is `upstream/pstack/skills/setup-pstack/SKILL.md`; the archive is not part of installed skills. Copilot does not consume that rule, so do not read or write it, rename it to a Copilot-looking file, or promise per-role model routing from it.

Copilot CLI does have real consumed configuration: `~/.copilot/settings.json` supports documented `subagents.agents.<id>.model` and `effortLevel` settings, and CLI agent metadata supports documented model policies and reasoning effort. Default to the simpler host `/model` control and explicit per-invocation choices; the optional registered-agent override below uses the actual native consumer, not another routing file. Do not write deprecated settings to internal `~/.copilot/config.json` or treat old keys as effective. See the official [CLI configuration-directory reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-config-dir-reference) and [CLI command reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-command-reference).

## Steps

### 1. Inspect the actual host

For Copilot CLI, read its current help. `/model` opens the documented model selector, including `auto`. Its documented `--repo` or `--local` controls set a repository default, and `plan` or `--plan` selects the plan-mode model. Use only options actually shown by the installed version. Do not infer availability from a Cursor cache, guessed API, or another host's model list.

For VS Code or cloud, use that host's documented model UI or configuration only if available. CLI slash commands are not portable host APIs. If model selection is unavailable, retain the host model and report the limitation.

### 2. Establish the real current state

Read the model shown by the host, not a pstack preferences file. Do not scan `~/.cursor/rules`, application state databases, plugin caches, or unrelated transcripts. No pstack model configuration file is created by this skill.

### 3. Discuss the tradeoff

Ask in ordinary language whether cost, speed, or strongest judgment matters most. The original budget ladder depended on Cursor-specific effort suffixes and is not translated into guessed Copilot model names. For unattended work, keep the current model rather than fabricating a choice.

Typical roles remain feature/refactoring, bug fix, performance, hillclimb, judgment/prose, hardest tasks, exploration, synthesis, experiment runner, and verifier. These are planning roles, not model-setting keys. Run them sequentially by default. Distinct-model review is useful only when real separate invocations support it.

### 4. Select and validate through the consumer

Have the operator select an offered model in `/model`, or use another documented control exposed by the installed CLI. Confirm the host shows the selected value. Never claim that writing a role table changed the model.

If the host exposes supported per-invocation model or effort controls, the operator may explicitly choose them for a particular invocation after inspecting that interface. Otherwise keep the current model. Do not fabricate slugs, append `max`, `xhigh`, or `fast`, or interpret `inherit-parent` as a portable API alias. `auto` is valid where the CLI model selector offers it, not a universal delegation parameter.

### 5. Optionally configure the registered native delegate

Do this only when the operator wants actual delegation to the installed custom agent. Use `/agent` to verify that its registered ID is `poteto-agent`; a filename or a planning role is not sufficient evidence. If it is absent, stop this optional step rather than creating an unregistered role key.

Inspect the installed CLI's actual settings interface for per-agent controls. `/model` selects the session model; do not claim it alone configures an agent override. Use a documented native settings UI if it exposes these controls, or a safe host-provided configuration editor that demonstrably preserves JSONC comments, unrelated keys, and existing overrides. If neither is available, explain the intended changes for the operator and leave the file untouched. Never parse-and-rewrite the entire settings file as plain JSON, strip comments, or overwrite it with a template.

With operator-selected values confirmed available, merge only `subagents.agents.poteto-agent.model` and, if requested and supported for that model, `subagents.agents.poteto-agent.effortLevel` in the real `~/.copilot/settings.json`. Preserve other agents, fields, comments, and formatting. To return to inherited behavior, remove only those selected override properties through the same safe editor; never manufacture an `inherit-parent` model value.

The consumer is an actual native task delegation that selects the verified registered `poteto-agent` ID using the host's current documented task interface. Do not invent a Cursor-style invocation or treat feature, bug-fix, or other planning roles as registered IDs. Inspect the resulting native configuration and, if the host exposes it, the actual delegate's selected model to verify the change. Configuration presence alone is not proof that a task ran.

Without such delegation, every sequential role pass inherits the current session model. A delegate override does not change those passes. Native CLI task/background support exists, but this port does not translate Cursor's background contracts onto it.

### 6. Confirm what actually changed

Report the host model or default the operator set, any safely edited native `poteto-agent` override, its observed scope, and remaining explicit per-invocation choices. Distinguish a verified configuration change from an observed delegate run. If nothing changed, say so. Do not claim settings apply to new sessions unless the actual host control says so.

### 7. Check the verification path

Look for an existing project-local verification skill at `.github/skills/verify-*/SKILL.md` relative to the target repository root, or an existing harness that drives the real artifact. If absent and the operator wants one, use the bundled `../create-verification-skill/SKILL.md` where available; its generated skills belong in that project-local directory. Validate actual paths and run existing checks. This optional work never changes model settings.
