### Multi-phase or multi-PR plan

**Copilot adaptation.** Run planning and verification roles sequentially by default. Cursor Task parameters, fixed model/effort defaults, cloud VM placement, and the hourly scheduler are inactive. Source-repository provenance is `upstream/pstack/skills/poteto-mode/playbooks/multi-phase-plan.md`, not an installed resource. Use actual host controls only; never merge or arm auto-merge.

**You own the plan, not the code. The plan is a checklist an owner runs box by box and the operator audits from the evidence.** The plan is the deliverable. Do not implement.

1. When the change is one or two files with an obvious approach, skip the plan. Say so and stop.
2. Settle open questions by prototype before you write. Run `playbooks/prototype.md` for each. Keep the branch, the SHA, and the screenshots for Appendix A. Ask the operator only about a product or preference call that no run can settle. Give options (the **never-block-on-the-human** principle skill).
3. Explore in scoped sequential role passes under `../SKILL.md` (**guard-the-context-window**). Return file pointers, conventions, test commands, and entry points, not bulk dumps. If independent host-supported invocations are used, disclose their actual model and isolation rather than assuming them.
4. Copy the skeleton into the explicitly requested plan path or an authorized session plan artifact, never a discovered agent store. Fill every placeholder and retain heading order. One section per PR with its own evidence (**sequence-verifiable-units**). Name the execution playbook in **How to read this**. Pick independent work in `autopilot-full.md`, dependent stacks in `autopilot-stack.md`, or a standing program in `orchestrate.md`.
5. Apply the bundled **technical-writing** skill in full, then **unslop**, using natural-language requests or actual supported host discovery rather than assumed custom slash commands. The body is one Diátaxis mode, how-to. Appendices hold explanation and reference. Each heading states the task or the finding. No long dashes. No mid-sentence colons.
6. Run `node <resolved-poteto-mode-directory>/scripts/check-plan.mjs <plan.md>` and fix every line it prints (**encode-lessons-in-structure**). Resolve the directory from the loaded skill, not a source checkout assumption. The checker requires a sequential audit checkpoint rather than the inactive scheduler command.
7. Hand back. Post the plan path and the script's output, then stop. Execution starts on the operator's explicit go, under the execution playbook the plan names.

**Verification.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked (**prove-it-works**). Every verification block opens with that rule. Preserve ten live coverage lanes, each with a scenario, saved screenshot, and pass predicate. Execute sequentially by default using the actual host model, not a configured worker slug. One lane compares the same load-bearing scenario on trunk and head. If trunk lacks the feature, record that fact and gate the added behavior and user-visible end state instead of inventing a comparison. Both sides must produce the perf metric; for unlike scenarios, isolate diff-added work and use absolute budgets, never an invalid ratio. Name the interleaved probe, measured trunk baseline, and failure threshold. Interaction changes wait for operator review with screenshots and video. Non-interaction PRs write `**Review gate.** None. <PR id> is not review-gated.` without boxes. Neither case authorizes agent merging.

**Control surface.** Use an existing authorized browser, terminal, or simulator driver appropriate to the surface. The original external control plugin is not assumed installed. Cover both surfaces when a PR touches two. Missing drivers are risks in Appendix C and block the relevant live lanes.

````markdown
# <Program> plan

<Under ten lines. What changes, for whom, the rule the program enforces, and the PR ids in order.>

## How to read this

One box is one unit of work. Every box names the evidence that checks it. A nested box is a sub-step of the box above it. Check a box only when its evidence exists, a file, a log line, a screenshot, a test run, or a SHA. The body is a how-to. The appendices explain and record.

The program runs `<installed-skill-root>/poteto-mode/playbooks/<execution playbook>.md`. Fill the actual installed root, such as project `.github/skills/`, before use. The operator lands every PR; all agent work stops at verified merge-ready.

Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

## Program checklist

### Arm the program

- [ ] State the protocol and this plan to the operator, then stop. Start execution only on the operator's explicit go.
- [ ] Read these from trunk at program start. Re-read them at every tick.
  - [ ] `git show origin/main:<tracked-skill-root>/poteto-mode/playbooks/<execution playbook>.md`
  - [ ] `git show origin/main:<tracked-skill-root>/swarm/SKILL.md`
  - [ ] `git show origin/main:<control skill path>`
  - [ ] `git show origin/main:<tracked-skill-root>/poteto-mode/playbooks/opening-a-pr.md`
  - [ ] `git show origin/main:<tracked-skill-root>/<each other leaf skill the program uses>`
  - [ ] Fill the real base ref and tracked skill root. For an untracked plugin install, read the actual loaded files and record that Git snapshots are unavailable rather than inventing tracked paths.
- [ ] On the operator's go, run a sequential audit checkpoint at each phase boundary using the prompt below. Record the next checkpoint; no background scheduler is assumed.
- [ ] Use this checkpoint prompt. "Re-read the execution playbook from the actual base. Audit recorded heads, lane receipts, blockers, and scope against it. Judge progress by artifacts rather than prose. Re-scope stuck work within the authorized budget and permissions. Post a short status message only for newly observed changes, naming each changed PR, head, verdict, blocker, or operator decision. Record the checkpoint row even if nothing changed. Do not merge, arm automatic merging, or assume a scheduler, remote-agent status API, or independent reviewer."
- [ ] On hold or stand-down, stop all role writes. If real delegates exist, use only their documented stop interface and record any unconfirmed stop.

### Spawn owners

- [ ] Assign one owner role per PR with the lifecycle the execution playbook names. Run roles sequentially unless real supported delegation is explicitly selected.
- [ ] Follow this dependency graph. Start dependent work only after its parent merges, or base it on the parent branch when the execution playbook stacks.
  - [ ] <PR id> and <PR id> are independent and first. Both branch from `main`.
  - [ ] <PR id> after <PR id>.
- [ ] Hold the file boundaries. <PR id or class> touches only `<glob>`.
- [ ] Hold the review gate. <PR ids> change an interaction. They wait for the operator's review in chat with screenshots and a video before merge.

### PR mechanics, for every PR

- [ ] Resolve the forge once. Default to `gh`; if `command -v origin` succeeds and Origin can resolve the repository, use `origin pr` for every PR operation. Record any fallback to `gh`. Never require `gt`.
- [ ] Open the PR ready, never draft, per **Opening a PR**. Use the run's built-in PR tool when it has one, else `origin pr create --status open --base <base-branch>` or `gh pr create --base <base-branch>` according to the resolved forge. A stack child targets its parent branch.
- [ ] Run the repo's lint and typecheck once before the PR-facing push. Push with hooks on.
- [ ] Clean unnecessary abstractions and duplicated logic before each authorized commit and run the bundled **no-comments** skill before review. The original external cleanup plugin is not assumed installed.
- [ ] Triage every Bugbot and security-reviewer comment per `../references/bugbot-triage.md`.
- [ ] Rebase onto current trunk before the code-ready report and babysit. Keep that merge base in fix rounds. Rebase again only at merge prep, on a `git merge-tree` conflict with trunk, or on a CI failure that comes from a change on trunk.

### Verdict and merge, for every PR

- [ ] Run the full coverage matrix at the code-ready head per the installed sibling `swarm/SKILL.md`, sequentially by default. Repeat for new behavior, redesign, or a large diff; smaller changes receive targeted re-verification. Include gates, ten live scenarios, perf, and at least two focused diff/receipt audit perspectives. The root checks receipts before its verdict. Disclose when the independent-review gate cannot be satisfied.
- [ ] Clean only when every lane is `PASS`. Findings go back to the owner, including a defect that a lane filed as a note. A new head gets a fresh verdict, except for results that stay valid under the patch-id rule in `playbooks/shipping.md`.
- [ ] <The verified operator-handoff rule from the execution playbook, with the patch-id rule from `shipping.md`. Never merge or arm auto-merge.>

### Boot recipe, for every live lane

Each live lane runs at the exact PR head in an available environment. Use an existing authorized runtime driver. Cloud VMs and external Cursor control plugins are not assumed available. Missing drivers block live verification rather than silently passing it.

- [ ] `git fetch origin <head-branch> && git checkout <head SHA>`.
- [ ] <Start the backend and the surface. Wait for ready.>
- [ ] <Deliver input only through the control skill's commands. Name the read-only diagnostics.>
- [ ] Save screenshots to an authorized project-local artifact directory and return exact paths with the report.

## <Task as a verb phrase> (<PR id>)

**Depends on.** <PR id, or None.>

**Files.**

- [ ] Edit `<path>`.
- [ ] Create `<path>`.
- [ ] Delete `<path>`.

**Build.**

- [ ] <One change. Name the symbol and the file.>

**You see.**

- [ ] <One observable result, with the exact log line or screen state.>

**Verify, unit.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] <Test file and the case it gains.> Run `<command>`.

**Verify, live.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked. Ten lanes on `<actual host model>` at the PR head, sequentially by default per the boot recipe. Fill the observed host model, not an inferred role setting.

- [ ] Lane 1. Regression lane against trunk. Run <the same load-bearing scenario> at trunk and head. If trunk lacks the feature, record that and gate <the behavior the diff adds plus the end state the user waits for>. Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 2. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 3. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 4. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 5. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 6. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 7. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 8. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 9. <Scenario.> Save `<slug>.png`. Pass when <predicate>.
- [ ] Lane 10. <Scenario.> Save `<slug>.png`. Pass when <predicate>.

**Verify, perf.** Tests alone are not sufficient verification. A PR is verified only when its unit, live, and perf boxes are all checked.

- [ ] Metric. <What is measured at both trunk and head. If trunk lacks the feature, also name the diff-added work and the end-to-end state the user waits for.>
- [ ] Probe. <The command or procedure, run at trunk and at the head, interleaved. Both sides must produce the metric.>
- [ ] Baseline. Record the trunk <value> first.
- [ ] Rule. <Head against trunk, with the number that fails. If the scenarios differ, add absolute budgets for the diff-added work and the user-visible end state instead of an invalid ratio.>

**Review gate.** The operator reviews before merge.

- [ ] Copy lane <n> screenshots into `<media path>/<pr-id>-review-<slug>.png`.
- [ ] Record a 30 to 60 second video of the change on a lane VM. Save it as `<media path>/<pr-id>-review.mp4`.
- [ ] Post the screenshots and the video in chat. Stop at merge-ready. Wait for the operator's click.

**Merge.**

- [ ] Root's clean verdict at the exact head SHA.
- [ ] Bugbot triage done.
- [ ] Rebased onto current trunk after the verdict, patch-id unchanged.
- [ ] Hand the verified PR or base-chained stack to the operator for bottom-up landing. No merge command or automatic merge arming is performed.

## Close the program

- [ ] Every box above is checked with its evidence.
- [ ] Reply to the operator with the report the execution playbook names.

## Appendix A. Prototype evidence

<Each open question a prototype answered, with the branch, the SHA, and the artifact links. Each question that stays unproven.>

## Appendix B. Alternatives rejected

<Each approach weighed and why it lost.>

## Appendix C. Risks

<Each risk with the PR it lands in and what the owner watches.>

## Appendix D. Links and reading list

<Docs to read before editing. Which PRs use the installed sibling `how/SKILL.md` and `interrogate/SKILL.md`. The trail per the sibling `show-me-your-work/SKILL.md`. Resolve all paths from the loaded skill root.>
````

**Reply:** the plan path, the PR ids with their dependencies and the review-gated set, what the prototypes proved and what stays unproven, and the check script's output.
