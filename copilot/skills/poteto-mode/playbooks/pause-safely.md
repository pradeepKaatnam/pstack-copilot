### Pause safely

**You own a clean stop. Leave a checkpoint a cold-start agent can resume from.** This is explicit only. On "keep going", "going to bed, keep going", or "don't stop", do not pause.

1. Stop at a safe boundary. Finish the current atomic step or back out of it. Start nothing new, and cancel any nested subagents.
2. Take no irreversible action to pause. No PR and no push unless you already had one out.
3. Make the work durable within the user's commit policy. If commits are allowed, use one clear `wip:` commit and disclose a broken tree. If commits are prohibited, preserve the working tree and report its paths instead.
4. Write a resume note only in an operator-authorized session location, not a temporary directory or discovered host cache. Capture intent, progress, verified state, next steps, key files, and gotchas. Point at an existing show-me-your-work trail rather than duplicating it.

**Reply:** where you are in the loop, what's on disk versus still in your head (paths, no diff dumps), the commits you made and whether the tree is clean, and the first action on resume. This is a pause, not a final report.
