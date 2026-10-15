# Sentry Error History

## How to search it

Use an actually exposed, authenticated Sentry integration and inspect its real search/detail schemas. The operation descriptions below are search goals, not callable tool names. If the required operation is unavailable, stop that part and report the gap. The original assumed APIs are archived at `../../../../../upstream/pstack/skills/why/references/sources/sentry.md`.

1. **Orient.** If you don't know the project slug and organization:

   List accessible organizations and projects with the integration's actual discovery operation.

2. **Search for issues related to the target.**

   Search issues, for example "errors in PaymentService timeout" or "unhandled exceptions in uploadFile", using the exposed search schema.

   Build queries from the exception class names the target handles, its function or class name, the error message strings it checks for, and its file path.

3. **Narrow by release and time window.**

   Search issue events by release, time, environment, trace ID, and tags where supported. Inspect tag distributions across versions, users, and environments.

   For a suspected issue, check **first seen** and **last seen** (does the stop line up with the target's ship date?), the **affected releases** (which saw it, and which was the fix?), and the **frequency trajectory** (did it spike, then get resolved?).

4. **Pull the full event for context.**

   Fetch a specific issue/event using the integration's actual detail operation and accepted identifier.

   Does the stack trace pass through the target code? Do the tags and breadcrumbs match the conditions the target defends against?

5. **Check releases that landed near the target.**

   Search releases around the target's commit date where supported.

   Cross-reference release version with the PR's merge date.

6. **Use Seer sparingly.**

   Use an AI-analysis operation only if actually exposed and authorized.

   Seer's AI root-cause analyses are a hypothesis generator. Treat them as inference, not authoritative. The actual events and stack traces are the primary evidence.

## What to return

For each relevant issue:
- Issue ID and title
- Project and organization
- First seen / last seen timestamps
- Event count (and sampling rate if known)
- Affected releases
- A representative stack trace snippet showing relevance to the target (verbatim excerpt, not summary)
- First/last-seen correlation with the target's ship date
- Link to the issue
- Any author comments or resolution notes
