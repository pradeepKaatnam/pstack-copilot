---
name: make-bot-ui
description: "Explain why the upstream Cursor Grok Bot webhook UI workflow is unavailable in this Copilot port. Do not provision routines or expose servers."
disable-model-invocation: true
---

# Make bot UI: unavailable integration

Stop this workflow and report it unavailable. The upstream instructions depend on Cursor's routine-management API, secret-request cards, connector credential files, webhook wake format, and managed computer/tailnet. These are not Copilot APIs or portable infrastructure. Do not call invented tools, search credential files, install Tailscale, expose a server, or infer webhook headers and endpoints.

The complete original engineering instructions remain inactive in the source repository's immutable archive at `upstream/pstack/skills/make-bot-ui/SKILL.md` (repository-relative provenance: `../../../upstream/pstack/skills/make-bot-ui/SKILL.md`). The archive is not an installed skill resource, and those instructions are not executable Copilot guidance.

A user-requested replacement is a separate implementation task requiring a real documented webhook provider, explicit authorization for provisioning and network exposure, and a supported secret-injection mechanism. Keep credentials server-side and out of chat, browser code, logs, source control, and proof artifacts. Treat webhook payloads as untrusted data. Until the actual provider and its exposed integration are available, do not claim a routine or UI has been created.
