### Worktree and simulator cleanup

The Cursor transcript/cache discovery and inferred-safe deletion passages are inactive. Source-repository provenance is `upstream/pstack/skills/poteto-mode/playbooks/worktree-cleanup.md`, not an installed resource. The audit remains a standalone read-only classifier, not permission to delete.

1. Snapshot and audit. Record `df -h /`, then run `scripts/worktree-audit.sh [-b <pr-base-ref>] [repo-path]` from the skill directory. Without `-b`, it checks `origin/HEAD`, then `origin/main` or `origin/master`; use the actual PR base. It reads paths from `git worktree list` and records size, age, tracked/untracked work, remote and PR state. Its best-effort fetch may update remote refs. It no longer scans application caches or private transcripts. Activity is unknown, and a merged candidate is `verify-activity`, not safe.
2. Treat every bucket as advice. Obtain the active worktree and process set from explicit operator information or authorized project-local evidence. A pinned or active session wins over stale PR state. Missing evidence is a hold, never proof of inactivity.
3. Verify each candidate. Read only supplied run records and project-local process evidence. Sequential analysis is the default. Worktrees used by a simulator, development server, experiment, or delegated run remain in use even if not visible in a sidebar. No host-specific model or background controls are assumed.
4. Pause on loss. Tracked edits, untracked files, ignored build artifacts, and simulator state can all matter. Show the affected paths and get explicit deletion approval. A `scratch` classification is not permission. Do not infer authorization from a clean or merged branch.
5. Prune only the confirmed authorized set. Use normal `git worktree remove <path>` first. If it refuses, report why rather than adding `--force` or recursively deleting the directory. Any separately authorized removal of ignored artifacts needs the same exact-path and activity checks. Preserve branch refs, then re-list and record `df -h /`.
6. Simulators and caches. Inspect only when the installed platform tools support it and the operator requested it. Propose exact stale simulator/runtime identifiers for approval, not delete-all commands. Do not scan or clear Cursor, IDE, package-manager, or unrelated application caches to reclaim space automatically.

This playbook deletes user state with no code review to catch a slip. Approval and exact-path evidence are the review.

**Reply:** disk before and after, paths removed with approval, each held candidate and reason, and any unavailable platform tools or activity evidence.
