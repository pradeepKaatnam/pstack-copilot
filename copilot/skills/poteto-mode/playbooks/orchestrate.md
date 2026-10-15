### Orchestrate

**Copilot adaptation.** The Cursor background/cloud coordinator API is inactive. Run the roles below sequentially, with one writer at a time, and stop at verified merge-ready. The preserved standalone `orch` runtime is bookkeeping only, not an agent launcher or merge authority. Source-repository provenance is `upstream/pstack/skills/poteto-mode/playbooks/orchestrate.md`, not an installed resource.

**You own the program, never the code. Author briefs, drain the queue, keep the frontier green, decide.** For a whole project handed to one standing coordinator chat: multi-day, many stacked PRs, dozens to hundreds of subagents, the human checking in twice a day instead of every five minutes. One task driven to a predicate is Autonomous run. One ambitious run needing a bespoke workflow is figure-it-out. Route here when the work outlives any single agent. Work one agent could finish inside the session's budget is not a program.

Ceremony must scale with the program. On cheap near-identical units, collapse it as each section directs.

Three rules carry the rest.

- Completions are queue events, not interrupts.
- Every role handoff and new invocation carries the standing orders verbatim.
- The brief is the product. A vague brief fails quietly, because a worker cannot ask you a question.

#### Roles and placement

- **Coordinator (this chat).** Frames work, authors briefs, drains records, owns reports, and makes judgment calls. It can execute a scoped implementation role when separate agents are unavailable, then perform a separate review pass. It never merges PRs. State reads and writes use `../scripts/orch/orch.ts` at drain points. The CLI never spawns, waits, or wakes agents.
- **Track coordinator.** A planning role only when one board is too large. Consolidate scope and aggregate reports at wave boundaries. There is no assumed nesting depth, cloud environment field, or background worker window. Execute one scoped role at a time unless the current host independently documents safe delegation.
- **Worker / verifier.** Run in the current available environment by default. Local simulators, IDE state, authentication, and artifacts may not exist elsewhere. A supported remote invocation needs self-contained briefs or repository pointers. One writer per worktree or branch (**principle-separate-before-serializing-shared-state**). Seek a genuinely independent verifier for high-risk work and disclose when only a same-session review is available.

Depth stays at coordinator, track, worker. Author the track decomposition per project (build, landing, and verification are common cuts, not a required shape). Hard-coded swarm trees were tried and parked as too rigid.

#### Store layout

Choose an explicitly authorized project-local state directory. Do not infer a system-provided store path or scan application caches. Every file has exactly one writer. Owners publish facts, readers aggregate at read time. With Bun and advisory-reviewed dependencies already installed, use `bun <resolved-poteto-mode-directory>/scripts/orch/orch.ts --store <state-dir>` for bookkeeping, written below as `orch`. Resolve the actual loaded skill directory before execution. Plain TSV and JSON remain readable without it. Bootstrap does not install dependencies automatically.

- `preferences.md` is the standing-orders register: numbered lines, one constraint each (model policy, stack shape and count, verification bar, forbidden paths, escalation policy). Paste it verbatim into every spawn and every resume. Directives decay across resumes, and each dropped one costs a human turn. When you catch yourself restating an instruction, append the line before you act (principle-encode-lessons-in-structure).
- `overview.md` is the durable PR and issue DB. Append. Never rewrite wholesale per event.
- `units.tsv` has one row per unit: id, track, state, branch, PR, head SHA, brief path. Update rows in place.
- `frontier.json` is the computed merge frontier, per Stack safety.
- `ledger.tsv` is the verification ledger, per Verification.
- `inbox/` holds completion pointers. `gates.md` parks human gates (question, options, default on no answer).
- `decisions.tsv` is the trail via the show-me-your-work skill.
- `status.md` is derived from `units.tsv` and `ledger.tsv` at each drain, never hand-maintained. Regenerate it from the tables instead of narrating events into it.

#### The brief

Your prompts to agents are your only product, and a sloppy brief compounds into slop across the whole tree. Every spawn carries all of it. A field you cannot fill is a unit you have not scoped yet.

```
GOAL         one sentence, the outcome, executable by a stranger with no chat access
SCOPE        paths this unit may write; paths it may not; its exclusive worktree or branch
CONTEXT      pointers to files and PRs; upstream reports pasted in full when this unit
             depends on them, because workers cannot see siblings
ACCEPTANCE   checkable criteria, one per line
VERIFY       exact commands or the control-skill path, plus known gotchas
TIMEBOX      rough cap on runtime; on expiry, return partial findings and stop rather than run on
FORBIDDEN    no PR retargets or merges, no rebase, no force-push, no fixes outside scope,
             plus unit-specific bans
REPORT       status, branch, head SHA, PRs, verdict, what you actually ran, deviations,
             suggested follow-ups
STANDING     <preferences.md pasted verbatim>
```

Size the brief to the unit. A one-command unit gets the template collapsed to a paragraph that still names goal, scope, the verify command, and the report shape. A 4KB scaffold around a two-line edit costs more to write and obey than the edit. Local spawns may reference the standing-orders file by store path. Verbatim paste is for cloud spawns and every resume.

A track brief adds its boundary, unit list, time budget, drain protocol, and rollup format (per unit, name, status, PR, head SHA, verdict, plus track status and frontier delta). It does not imply a cloud or spawn API.

A dependency is a context relay, not just ordering. Undeclared upstream context makes the worker guess. Missing fields are a refuse-to-spawn condition. Audit one sampled worker brief per sub-coordinator per wave, concurrently with the wave it samples, never as a gate in front of it. A failing brief stops that track and fixes the sub-coordinator's instructions, not just the worker, because brief quality decays late in a run. Never resume-chain a brief. Respawn fresh with consolidated scope.

#### Steps

1. **Frame.** State a countable predicate, such as all 126 units verified and merge-ready. Quantify units, effort, stacks, and wall-clock budget. If one session can finish, do the work directly with inline verification and no program machinery. Reserve the end of the budget for checking receipts and preparing the handoff, never automatic landing. Name tracks and compare contested decompositions before the pilot.
2. **Install the runtime.** Run `orch init`. Open the trail via the show-me-your-work skill, write the standing orders before any spawn, and seed `frontier.json` from existing PRs with `orch frontier set --repo <repo-dir>`, adding `--forge origin` when the forge is Origin.
3. **Pilot.** Run one unit through brief, implementation, verification, stack entry, and ledger row to merge-ready. Falsify the brief template, verify recipe, and unit size before scaling. Cheap identical units can use inline checks with spot-checked receipts. Expensive or novel units need independent review; if unavailable, mark blocked rather than claiming it happened.
4. **Scale.** Work the dependency-ready queue sequentially. Recompute ready work after each drain and relay upstream reports into downstream briefs. Sample brief quality at wave boundaries. Optional supported delegation must preserve isolated writes and explicit scopes; no background API is assumed.
5. **Drain.** Run the queue discipline below at every drain point.
6. **Prepare landing.** Keep the frontier green and prepare verified units for operator review. Do not merge or arm auto-merge. Advance `frontier.json` only from observed forge state or reported head SHAs. Report each user-performed merge before continuing a dependent stack transition.
7. **Close.** Drain the final inbox, reconcile every spawned agent to a terminal row (done, abandoned, zombie-reconciled), confirm the predicate on the real artifact, confirm every landed PR has a verdict for its current head SHA, audit the trail per show-me-your-work including its cross-model review, encode recurring corrections into `preferences.md` or the brief template. Leave the store intact. It is the postmortem.

#### Queue and drain

- On a completion notification, run `orch inbox push <agent> <unit> <status> [--report PATH]` and return to what you were doing. Never deep-review inline. A completion that needs review becomes a verifier unit. Never review a diff inside a drain.
- Drain at the end of a critical section, a track rollup, a bounded foreground watcher result, and before a human report. Begin with `orch inbox drain`. No scheduler or wake hook is assumed.
- Critical sections you finish first: authoring a brief, a stack operation, a conflict decision, writing a gate, updating ledger or frontier.
- Each drain classifies every pointer (landed, needs-verify, failed, zombie, noise), writes the resulting rows through `orch unit add`, `orch unit set`, and `orch ledger record`, runs `orch status`, then spawns the next wave in one message.
- Account for every spawned child at its track's rollup: arrived, respawned, or its scope explicitly absorbed. Silently redoing a missing child's work hides both the wasted spend and the coverage gap its result existed to close.
- A drain turn ends with the three lines from `orch status`: counts against the states, what changed, gates open. Detail lives in `status.md`. The full reply contract applies at checkpoints and close.

#### Stack safety

- The frontier is a computed object, never narrative. Recompute `frontier.json` after every merge and stack mutation: ordered PR list, branch names, head SHAs, a generation number, the lowest unmerged PR. The command walks the PR base chain through the checkout's current branch, so chain order and PR states come from the forge. It uses `gh` by default. Pass `--forge origin` when the program resolved the forge to Origin. Head SHAs come from local branch refs, so resolve it from the stacker's clone. A branch with no PR errors rather than guessing.
- Exactly one authorized stacker role may mutate topology (chain rebases, branch pushes, base retargets), serialized within its stack. Record the holder. Respect permissions and explicit approval for destructive writes. Merges remain the operator's action; cloud execution is never assumed.
- Workers never rebase and never retarget or merge PRs. Babysitters follow `playbooks/babysit.md`, one per stack, scoped to one immutable frontier generation. They report conflicts to the stacker rather than rebasing.
- PR closes and retargets go through the stacker only. Closing a base PR orphans every chain above it. Merges and stack surgery are units with briefs like any other.
- One retro watcher follows merged PRs for reverts, post-merge CI breaks, and orphaned follow-ups.

#### Verification

Scale verification to the unit. When VERIFY is a single cheap command, the worker runs it and reports the output, and the coordinator spot-checks receipts. A dedicated verifier agent (on a different model family than the worker) is for units whose verification is expensive, judgment-laden, or high-blast-radius. A verifier agent whose entire product would be rerunning one command is ceremony, not verification.

Write ledger rows with `orch ledger record`. Check the current PR and head SHA with `orch ledger check`. `ledger.tsv`, one row per verdict, keyed by PR number plus head SHA: `live-ui-verified | unit-test-verified | type-check-only | verifier-blocked | verifier-failed`. CI green is an input to a verdict, not a verdict. Behavioral work needs better than `type-check-only`. `verifier-blocked` is not a pass. Respawn when the environment heals. `verifier-failed` gets a fix unit, not a re-verify. A worker may self-report. A verifier overrides it on the same key. A new head SHA voids the row, so re-verify after restack. The ledger answers "was this verified", not memory and not the transcript.

A unit is not done until its output is externalized the moment it lands, never batched to the end of the run. A worker pushes its branch, a verifier writes its ledger row, receipts land in the store. Work that exists only on one VM when that VM dies was never done.

#### Liveness and failure

- Inspect durable records, `gh`, and pushed branches for liveness. Use a host status interface only if actually available. Never invent a dashboard or resume an agent merely to check it. Transcript mtime is not liveness.
- A silent death gets a synthetic postmortem row in the inbox (unit, failure mode, last evidence, options). Replan on evidence as it arrives. Never wait for full quiescence.
- Retry by mode: cap-hit or oom, respawn with smaller scope. Network-drop, retry as-is. Tool-error, retry on a different model. Unknown, retry once. Two retries, then abandon the unit and replan around it.
- A zombie that returns hours late reconciles against the current frontier and ledger before anything is accepted. Salvage unique findings through a fresh unit, never a blind merge.
- When continued spawning would produce garbage tree-wide (bad upstream output, broken acceptance, dead infra), write a stop line at the top of the standing orders, let in-flight work finish, fix the cause, clear it.
- Bound your own infra retries the same way you bound a child's. After a few consecutive tool aborts, stop retrying. Write a terminal handoff to durable state (what is done, where it lives, the exact command to resume) and end the run.
- After a restart, do not assume any process survived. Re-read standing orders and `units.tsv`, recompute the frontier, and recover work from PRs, branches, and durable receipts. Resume sequential roles with consolidated scope. `orch` replaces a lock only when its holder pid is gone.

#### Escalation

Reaches the human, batched into the status page rather than per item: irreversible actions (force-push to shared branches, deploys, deletions, closing someone else's PR), genuine product or preference calls no experiment settles, a standing order that contradicts observed reality, a program-level dead end that survived a replan. Park each as a `gates.md` entry before asking, and route work around it.

Routine retries, CI triage, format fixes, and already-authorized reversible work need no repeated approval. Permission limits, merge authority, operator review, and destructive-action gates always reach the human. When uncertain, preserve the gate and continue only unrelated authorized work.

Mid-run discoveries fix only what blocks the frontier. Everything else parks in follow-ups. At this fan-out a small scope leak multiplies into PRs nobody asked for.

**Reply:** at checkpoints and close: the predicate and the count against it from `units.tsv` and `ledger.tsv`, tracks and what each landed, the frontier (PR list plus SHAs), verdicts summary, what was abandoned and why, gates awaiting the human (the only asks), the store path, and the trail path. Numbers from the tables, not narrative. Include PR links.
