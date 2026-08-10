---
docId: GOV-PLAN-319
title: "[CODE] agent-context-parity.yml is YAML-invalid — unquoted run: value contains \": \""
version: 1.0.0
authors: [loig-allain]
status: in-progress
issue-id: GenCr-ft/gcs-core-governance#319
metadata:
  scope: workspace-ops
  domain: governance
  doc-type: plan
  lifecycle-stage: approved
  security-classification: l2_confidential
---

## Objective

Make `.github/workflows/agent-context-parity.yml` load, **and** make its parity job able to run — so
the check it implements executes for the first time.

## Why it matters

The file has never parsed, so GitHub has never loaded it and the agent-context parity check has
**never executed**. A governance check that has never run is indistinguishable from one that passes,
and this repo is the canonical DevOps/tooling SSoT.

## Two defects, both in scope

Scope is wider than "make it parse", and that follows from the issue's own **AC-3** — *"the
routing-table verification step executes and reports a real verdict"* — which the YAML fix alone
cannot satisfy.

### 1. YAML-fatal unquoted `run:` value (45:69)

In a plain YAML scalar `": "` is a key/value separator. The inner double quotes belong to the shell;
YAML never sees a quoted string, so it read `FAIL` as a key. Fixed with a block scalar, which avoids
reasoning about nested quoting entirely.

### 2. `path: ../gcs-plt-gemop` escapes `$GITHUB_WORKSPACE`

`actions/checkout` refuses a path outside the workspace, so the job would die at checkout even once
the file parsed. Evidence that `../` is wrong is **fleet convention**, not inference about checkout
internals — every other cross-repo checkout uses a workspace-relative path:

| Repo / workflow | `path:` |
| --- | --- |
| `gcp-aethel-client` `ci.yml` | `gcd-ops-scripts` |
| `gencraft-iac` `generate-catalog.yml` | `'gcs-core-governance'`, `'gcd-ops-scripts'` |
| `gcs-security-core` `credential-matrix-validate.yml` | `gemop` |
| `gcs-plt-gemop` `agent-schema.yml` | `gcs-plt-gembp` |
| **this file** | **`../gcs-plt-gemop`** — sole outlier |

## `path:` and `WORKSPACE_ROOT` are a coupled pair

The `../` was **not** careless. `scripts/verify_agent_context_parity.py:46` defaults
`WORKSPACE_ROOT` to `REPO_ROOT.parent`, which is exactly where `../gcs-plt-gemop` lands. The author
was consistent with the script and defeated by checkout's containment rule.

So moving the checkout without moving the lookup trades a checkout failure for a **resolution**
failure, and `check_gem_ids_in_gems_index` then hard-fails blaming the checkout that just succeeded.
Both move together, with a comment recording why. `WORKSPACE_ROOT` is scoped to the single step that
reads it — that script is the only one in `scripts/` referencing it (grep-verified).

## Steps

- [x] Worktree `../wi-319-gcs-core-governance`, branch `fix/issue-319-parity-yaml-quoting`, from `origin/main` at `aa8a2aa`
- [x] Post `LIFECYCLE:REFINE-LIGHTWEIGHT:PASS`, correcting the issue's own prediction
- [x] Block scalar for the assert step; `path:` inside the workspace; `WORKSPACE_ROOT` on the parity step
- [x] Must-fire ×2 + CI-layout simulation (below)
- [x] `./test.sh` exit 0 — all three parity checks PASS
- [ ] PR; adversary review (§4.1); human merge

## Verification

```
[PASS] MUST-FIRE: original does NOT parse — 45:69: mapping values are not allowed here
[PASS] fixed file parses
[PASS] checkout path is workspace-relative (fleet convention) — 'gcs-plt-gemop'
[PASS] assert step no longer references ../
[PASS] assert echo text survived YAML as shell text
[PASS] parity step sets WORKSPACE_ROOT (coupled with the path move)
[PASS] parity script resolves gems/index.yaml via WORKSPACE_ROOT (CI layout simulated)
[PASS] MUST-FIRE: parity script fails when gems/index.yaml is unreachable
```

The CI layout was **reproduced rather than reasoned about**: gemop symlinked inside a temporary
workspace, `WORKSPACE_ROOT` pointed at it, the script executed. Its must-fire twin points
`WORKSPACE_ROOT` at an empty directory and confirms a non-zero exit, so the passing case is not
vacuous.

## Correction to the issue

The issue's impact note predicted *"expect genuine findings on first execution."* **Wrong.** All
three parity scripts pass against `origin/main`. The invariants do currently hold, so the exposure
was **loss of the signal**, not accumulated drift behind it.

## Unverifiable here, stated rather than assumed

`CROSS_REPO_PAT` (line 43). This repo has **zero** repository-level secrets (`actions/secrets` →
`total_count: 0`) and organisation secrets return `HTTP 403` for my identity. The one comparable
workflow in the fleet, `gcs-security-core/credential-matrix-validate.yml`, marks its gemop checkout
`continue-on-error: true` — the fleet already treats this token as possibly absent.

Deliberately **not** papered over with `continue-on-error`: that would recreate precisely what this
issue is about, a governance check that cannot be distinguished from a passing one. If the token is
missing, the PR makes it a clearly-diagnosable finding to file.

## Trigger note

`paths:` does not list this workflow itself, so the job will not run on a PR that only edits it. The
primary AC is still directly observable: **startup failures ignore path filters**, so no path-named
0-job run appearing on the branch push is proof the file now loads.
