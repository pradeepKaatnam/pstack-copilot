---
name: swarm
description: "Cover N scoped slices or candidate attempts and return one report. Use for /swarm, 'swarm this', coverage, gauntlets, and exploration."
disable-model-invocation: true
---

# Swarm

Run N sequential worker-role passes. They may cover separate slices, attempt the same brief, or mix both. Collect results and return one report. Sequential attempts are not a concurrent speed race.

Cursor cloud-worker APIs, model rules, and background assumptions are removed; the exact original is archived at `../../../upstream/pstack/skills/swarm/SKILL.md`. Optional delegation is permitted only when a real tool is exposed by the current host. Use its actual schema; never assume remote machines, cloud branch selection, model selection, reasoning controls, or background execution.

## Start

Open a todolist with one entry per phase before launching anything.

1. Frame
2. Fan out
3. Aggregate
4. Report

## Phase A: Frame

1. State the done predicate and the artifact or report the swarm must return.
2. Choose the shape. Partition into slices, race N workers on identical briefs, or mix both. For a race or mixed shape, declare `first pass`, `rank all`, or `best-of` before running the passes.
3. Set N from the user or derive it from the shape. N is total workers, not the cloud concurrency limit.
4. Assign each pass a slice or distinct candidate direction. If the user requires independent models or a concurrent race and the host does not expose those capabilities, report that requirement unavailable rather than pretending sequential passes satisfy it.
5. Give each worker its own writable output when it writes. When workers verify or measure commits, each brief names the exact SHAs. A measurement brief also names the method (sample count, what one sample is, order). The worker records both in its result.

## Phase B: Fan out

Execute N worker-role passes sequentially. Verify the required checkout and branch before each pass, without silently changing shared state. Store each terminal result before moving on.

Every brief stands alone. Include the goal, scope, exact slice or race arm, how to verify, and what to report. Reports use `PASS`, `ISSUES`, or `BLOCKED` with evidence. A worker that can prove a defect reports `ISSUES` and lists every issue it can prove, not only the first.

If a worker drops out, proceed with N-1 and note it.

## Phase C: Aggregate

Read the terminal results. Drop a result that does not record the SHAs and method its brief names, and rerun that role pass once. After a second miss, record a gap. A gap does not count as a pass. For coverage, every required slice needs a result. For a race, apply the selection rule declared up front. Use first pass, rank all, or best-of. Do not paste raw worker dumps.

Keep a compact result table, one-line evidenced issues, and explicit gaps or dropouts.

## Phase D: Report

Return one consolidated in-chat report with the table, issue one-liners, gaps or dropouts, and the race rule when used.
