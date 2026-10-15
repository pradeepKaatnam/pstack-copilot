---
name: reflect
description: Run judgment, tooling, and divergent review passes over the active conversation, surface learnings, and route each to a concrete edit on an existing skill. Use when the user says reflect.
disable-model-invocation: true
---

# Reflect

Mine the current conversation for durable learnings, then route them into skill edits.

Invoke when the user says "reflect" or "/reflect". Skip when the conversation is trivial, off-topic, or already covered by an existing skill the parent followed correctly. One-offs are not learnings.

## 1. Scope the active conversation

Use the active conversation context or an export explicitly supplied for this task. If no export is available, build a tight digest from the visible conversation, preserving evidence and unknowns. Do not inspect Cursor history, caches, private workspace storage, or unrelated conversations.

Cursor transcript discovery, Task/model rules, and built-in authoring assumptions are removed; exact originals are archived at `../../../upstream/pstack/skills/reflect/SKILL.md`. This port runs roles sequentially. Optional delegation needs a real host-exposed tool and its actual schema, with no assumed models, reasoning, background execution, or MCP inheritance. Missing MCP access stops the affected lookup and is reported unavailable.

## 2. Run three reviewer passes

Run judgment, tooling, then divergent passes, read-only, using `references/judgment-reviewer.md`, `references/tooling-reviewer.md`, and `references/divergent-reviewer.md`. Fill in the supplied export path or digest where marked. Record findings separately; later passes must look for new evidence, not just endorse earlier prose. Do not describe these as independent models.

## 3. Synthesize

Run a synthesis pass using `references/synthesizer.md`, with each reviewer's full output inlined where marked. Spot-verify citations only through available, authorized tools. It returns an Accepted / Rejected / Backlog list. Same-model agreement does not establish independent consensus.

## 4. Structural enforcement check

Move any Accepted item that a lint rule, script, metadata flag, or runtime check would enforce more reliably to Backlog. See the **encode-lessons-in-structure** principle skill.

## 5. Apply

Present the synthesizer's full Accepted / Rejected / Backlog output and wait for explicit approval before applying any Accepted edit. The user picks the subset and may redirect routings. Skill changes affect every future agent in the org. Do not auto-apply.

Prepare Backlog items for the team's chosen tracker. Post externally only when the user has authorized that action and the integration is actually available; otherwise return the proposed items and the access limitation.

Follow each approved row's Routing exactly:

- Trivial existing-skill edit (a one-line bullet, a tightened sentence, a stale fact corrected): the parent does it directly.
- Substantive existing-skill edit (a new section, a new pattern table, more than ~10 lines): draft, test against representative tasks, and iterate using the existing skill's structure.
- `tune description: <skill path>` (the skill exists but didn't trigger when it should have): test the description against intended and unintended trigger examples, then revise it.
- `new skill via create-skill: <kebab-name>`: this routing label means author a native `.github/skills/<kebab-name>/SKILL.md` with matching lowercase kebab-case `name` and a specific `description`, plus any referenced resources. It does not call a presumed built-in tool. Draft, test, and iterate before presenting it.

If your environment ships a SKILL.md validator, run it on every touched skill before declaring done.

## 6. Summarize for the user

Short list, no preamble:

- Edits applied: `<skill path>`. What changed, one line each.
- New skills created: `<skill path>`. One line each (rare).
- Backlog filed to the devex tracker: `<issue title>` (`<tags>`). One line each.
- Dropped: one line per rejected finding + reason from the synthesizer.
