---
name: interrogate
description: "Use for \"interrogate\", \"adversarial review\", \"challenge this\", \"stress test this code\", \"find blind spots\", or \"tear this apart\". Review passes challenge changes from distinct angles."
disable-model-invocation: true
---

# Interrogate

Run separate adversarial reviewer-role passes over code changes, followed by lead judgment. The deliverable is a synthesized verdict. Do NOT auto-apply changes.

This port defaults to sequential passes on the current model, not independent model reviewers. State that limitation in the verdict. Cursor Task/model configuration is removed; exact originals are archived at `../../../upstream/pstack/skills/interrogate/SKILL.md`. Optional delegation or model diversity is allowed only when actually exposed by the current host, using its real schema without assumed background or reasoning controls.

## Step 1, Scope

Identify what to review from context:

- If the user points at specific files or a diff, use that.
- If on a feature branch, run `git diff main...HEAD` (or the appropriate base branch) for the full changeset.
- If the user's message references recent work, gather the relevant files.

Package the diff or file contents with any surrounding context files the reviewers need to understand the code.

## Step 2, Intent

Before running reviewer passes, state the intent in one clear paragraph from the user's message, commit messages, the PR description if one exists, and the code. If you're unsure about the intent, ask the user before proceeding.

## Step 3, Reviewer Passes

Run Reviewer A and Reviewer B sequentially, read-only. Both apply the full rubric, with A starting from execution paths and failure cases and B starting from boundary contracts, maintainability, and missed simplifications. Record each result before the next pass; do not treat their agreement as independent model consensus.

Read `references/reviewer-prompt.md` and fill in the same template for every pass with the stated intent, the diff or file contents, the rubric from `references/rubric.md`, and the code-quality lens from `references/code-quality-review.md`.

## Step 4, Synthesize

Build a unified picture from every pass. Merge findings that describe the same issue differently and note which pass raised each one. Trace each claim against the code. Repeated same-model findings are not independent consensus. Note disagreements and resolve them with evidence, not a vote.

## Step 5, Lead Judgment

You are the lead reviewer, a pragmatic senior engineer, not a neutral aggregator. Read `references/lead-judgment.md` for the full framework. Put every finding in one of four buckets, with the pass(es) that raised it and a one-line rationale.

- **Act on**. Real issues affecting correctness, security, or maintainability given the actual goals. They would block a real PR.
- **Consider**. Legitimate, but you're not sure they outweigh the cost of addressing them now. Worth the user's attention.
- **Noted**. Technically valid but not actionable. Context-dependent, premature optimization, or low-impact at this stage.
- **Dismissed**. Wrong, nitpicky, or missing context, with a brief reason.

## Output Format

### Intent
> [The stated intent paragraph from Step 2]

### Reviewers
- Reviewer [label]: [role pass, actual model only if known], [N findings] (one bullet per reviewer; disclose sequential same-model review)

### Act On
[Each: description, which passes raised it, why it matters.]

### Consider
[Each: description, which passes raised it, the tradeoff.]

### Noted
[Brief list.]

### Dismissed
[Each with a brief rationale.]

### Agreement Map
[Where passes agreed and diverged, the evidence resolving disagreement, and any lack of independent model review.]
