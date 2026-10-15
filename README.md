# pstack-copilot

An **unofficial**, preservation-first port of Lauren Tan's
[pstack](https://github.com/cursor/plugins/tree/e5136d82418d2db3165ea1050d17577cd618cc05/pstack)
to GitHub Copilot, primarily **Copilot CLI**. Not official Cursor or GitHub software.
Upstream version: **0.15.25**. Upstream copyright and MIT license are preserved.

## What is installed

`copilot/` is the only installable plugin. Its canonical skill tree contains all
54 upstream top-level skills, their adapted references, playbooks, and portable
runtime resources. Agent orchestration defaults to sequential role passes:
Cursor tool signatures, automatic background dispatch, private services, and
unimplemented automations are not emulated. No hooks or MCP servers are enabled.
No workflow in this port grants permission to merge automatically.

`upstream/pstack/` is an immutable, **non-discovered source archive**, not an
installation target and not instructions to execute. It preserves every one of
the 169 tracked upstream files, including hidden files, both original manifests,
all automation prompts, tests, lockfiles, executable modes, and seven images.
Do not install this repository root, that archive, or the original Cursor plugin.

## Personal Copilot CLI installation

With a current CLI supporting the documented plugin interface:

```sh
copilot plugin install pradeepKaatnam/pstack-copilot:copilot
copilot plugin list
```

Alternatively, install a reviewed local checkout using its **absolute path**:

```sh
copilot plugin install /absolute/path/to/pstack-copilot/copilot
```

In a new interactive session, inspect `/skills list` and `/agent`. Invoke a
listed skill explicitly (for example `/poteto-mode`); use the name the host
actually displays if another plugin causes a naming collision. Verify
`/create-verification-skill` writes `.github/skills/verify-<feature>/SKILL.md`
in your project. Ask it to run the project's real verification commands.
Manual-only skills retain `disable-model-invocation: true`; that metadata
is not a permissions or sandbox boundary.

Update a remote install with `copilot plugin update pstack-copilot`. For a local
install, review/pull port changes and **reinstall the same absolute package
path**: the CLI caches installed components. Remove with
`copilot plugin uninstall pstack-copilot`. Installation does not update or
unpin the archived upstream baseline.

CLI plugin commands, formats, component paths, and cache behavior are documented
by [GitHub](https://docs.github.com/en/copilot/how-tos/copilot-cli/customize-copilot/plugins-creating)
and the [CLI plugin reference](https://docs.github.com/en/copilot/reference/copilot-cli-reference/cli-plugin-reference).
Documentation was retrieved on **2026-10-15**. See `audit/documentation.json`
and `audit/compatibility.txt` for the host-specific evidence and limitations.

## Company and repository adoption

Have your security/platform owners review the package, audit, and upstream
license first. Nothing here bypasses organization policy, host permissions,
branch protection, MCP authentication, or human approval.

For CLI users, distribute the reviewed `copilot/` plugin rather than the source
archive. There is no need to register a marketplace for direct installation.
The legacy manifest is deliberate: official current CLI documentation supports
explicit `skills/` and `agents/` paths. Agent Plugins 1.0 is also supported but
requires Copilot agents in `com.github.copilot/agents/`; the two formats must not
be mixed. Original JSON stays valid and unmodified in the archive; its
compatibility notes live in the audit sidecars.

For repository-local skills shared with CLI, VS Code agent mode, and cloud:

```sh
python3 /absolute/path/to/pstack-copilot/scripts/install-project.py /absolute/path/to/company-repo
# Review and commit company-repo/.github/skills, pstack-installed.json, pstack-LICENSE.
# After reviewing a port update:
python3 /absolute/path/to/pstack-copilot/scripts/install-project.py /absolute/path/to/company-repo --update
```

The installer creates managed snapshots in `.github/skills/`, with a hash
manifest and upstream license. Updates refuse conflicting skills, modified
managed files, and symlinked discovery paths. Edit the canonical port, or keep
company-specific skills under distinct names; installed snapshots are not a
second authoritative skill tree. Do not install both a plugin and project
copies in the same context unless you intend duplicate skill discovery.

Generated verification skills also belong in `.github/skills/verify-*/`, not a
Cursor directory. Project skill discovery does **not** imply CLI plugin support
or parity for custom agents, models, tools, hooks, background work, or MCP in
VS Code/cloud. Custom agents are bundled for the CLI; this installer does not
install agents for other hosts. Use only tools your session actually exposes.

## Review evidence and validation

* `audit/provenance.json`: source repository, exact commit, date, license,
  tree identity, and per-file mode/type/size/SHA256/Git blob identity.
* `audit/supporting-skills.json`, `audit/orchestration.json`, and
  `audit/non-skills.json`: one row per upstream file, with full-content review,
  exact counterpart or inactive disposition, and host applicability.
* `audit/passages.json`: exact original text and source line ranges for changes
  and inactive text, adapted replacement text, rationale and documentation links.
* `audit/compatibility.txt`: readable compatibility matrix and file audit.

Run the offline checks using Python's standard library:

```sh
python3 /absolute/path/to/pstack-copilot/scripts/verify.py
python3 -m unittest discover -s /absolute/path/to/pstack-copilot/tests -v
```

CI fails on changed/missing archived bytes or modes, an inventory that does not
reconstruct the pinned Git tree, missing/unclassified mappings or counterparts,
stale exact-text evidence, broken package resource links, and discovery leaks.
CI also runs the preserved Bun runtime tests and TypeScript check using the
unchanged frozen lockfile, without dependency lifecycle scripts.
These are mechanical checks, not proof that a model will obey every prompt.
Actual CLI/IDE/cloud discovery and end-to-end agent execution require a host
session; do not confuse documented support with an executed integration test.

### Reproducing or updating the source evidence

Use the exact source commit, never a moving branch:

```sh
git -C /absolute/path/to/pstack-copilot fetch --no-tags --depth=1 https://github.com/cursor/plugins.git e5136d82418d2db3165ea1050d17577cd618cc05
git -C /absolute/path/to/pstack-copilot ls-tree -rl e5136d82418d2db3165ea1050d17577cd618cc05 -- pstack
python3 /absolute/path/to/pstack-copilot/scripts/refresh-evidence.py
```

The evidence generator requires the exact commit locally, does not fetch
anything, and cannot substitute a revision. It refreshes mechanical evidence,
**not the substantive file audit**. A future upstream upgrade needs a separate
review of every file, passage, and host assumption. Do not run archived agent
instructions or fetch private infrastructure/session data to validate a port.

This change is intended for review as a PR; it does not merge itself.
