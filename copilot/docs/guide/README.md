# The pstack guide for Copilot

Describe the goal and a checkable finish condition. Let the workflow demand
evidence, rather than prescribing every implementation step.

This is a selective, full-chapter adaptation, not a claim that Cursor's runtime
has been ported. Read the repository's root README for host installation.
Request a skill by name in natural language, for example:

```text
Use the poteto-mode skill: the export writes duplicate rows after a retry.
Reproduce first, then fix and verify. Show the failing and passing row counts.
```

Skill discovery, model selection, session history, delegation, and execution
permissions differ between Copilot CLI, VS Code, and the cloud agent. An
unavailable capability is a blocker or an explicitly disclosed serial fallback,
not permission to invent a tool call. A skill never grants permission to merge,
deploy, bypass review, or write to an external integration.

## Adapted chapters

1. [Route work through poteto-mode](./02-poteto-mode.md): goal, done check, proof,
   known facts, constraints, follow-ups, task switching, and isolated worktrees.
2. [Understand the code](./03-understand.md): read-only investigation, runtime
   tracing, evidence-backed history, teaching, context recovery, and safe pickup.
3. [Design the change](./04-design.md): caller-first APIs, independent attempts,
   coverage versus synthesis, adversarial diff review, prototypes, and plans.
4. [Build and clean](./05-build-and-clean.md): reproduction, behavior-preserving
   refactoring, measured performance, TDD, TypeScript, prose, and comment review.
5. [Verify and ship](./06-verify-and-ship.md): real-artifact proof, seven benchmark
   checks, project verification infrastructure, PR checks, and authorized landing.
6. [Steer with principles](./08-principles.md): all 24 engineering principles,
   with concrete examples and links to their complete rules.
7. [Recipes and pitfalls](./10-recipes-and-pitfalls.md): realistic prompts and
   failure modes, with host-specific limitations made explicit.

These chapters retain the upstream explanations, diagrams, examples, and
engineering checklists, with incompatible mechanics replaced or constrained.
The six original guide illustrations are preserved byte-for-byte in `images/`;
illustration labels may depict the original Cursor command vocabulary.

## Inactive original chapters

The following remain complete in the immutable archive, for historical reference
only. Do not follow their installation paths or treat their prompts as Copilot
instructions:

- [Original setup](https://github.com/cursor/plugins/blob/e5136d82418d2db3165ea1050d17577cd618cc05/pstack/docs/guide/01-setup.md): Cursor
  marketplace installation, model-role rules, and persistent Custom Modes.
- [Original overnight runs](https://github.com/cursor/plugins/blob/e5136d82418d2db3165ea1050d17577cd618cc05/pstack/docs/guide/07-overnight.md):
  Cursor loop wakeups, Projects, cloud-subagent fleets, and Benny automation setup.
- [Original customization](https://github.com/cursor/plugins/blob/e5136d82418d2db3165ea1050d17577cd618cc05/pstack/docs/guide/09-make-it-yours.md):
  Cursor transcript mining, create-skill orchestration, and Grok Bot webhooks.

The useful engineering ideas in these originals remain available for reading:
bounded completion contracts, evidence-linked decision logs, structural
enforcement of recurring lessons, and controlled workflow evaluation. Their
product-specific machinery is not installed or silently replaced by a summary.

See [compatibility.txt](../compatibility.txt) and
[the per-file audit](https://github.com/pradeepKaatnam/pstack-copilot/blob/main/audit/non-skills.json) for exact dispositions.
