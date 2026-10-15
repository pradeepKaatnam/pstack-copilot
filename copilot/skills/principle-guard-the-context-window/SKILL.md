---
name: principle-guard-the-context-window
description: "Apply when context is filling up: large outputs, long files, repeated reads, multi-pass planning. Read scoped chunks and keep concise findings, not repeated raw payloads."
disable-model-invocation: true
---

# Guard the Context Window

**Why:** Context overflow degrades reasoning quality, creates compression artifacts, and halts progress.

Use sequential scoped passes by default. Optional delegation requires a real tool exposed by the current host, not an assumed Task API. The original subagent routing is archived at `../../../upstream/pstack/skills/principle-guard-the-context-window/SKILL.md`.

**Pattern:**
- **Size phases and cap scope.** Limit files per phase, set turn budgets, account for mechanism costs.
