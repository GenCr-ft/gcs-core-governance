---
docId: GOV-PROTO-OR-001
title: Operations Runbook — Agent CLI Reference
version: 1.0.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: protocol
  intended-audience: [ai-agents]
  security-classification: l2_confidential
  source_version: "1.0.0"
  last_verified: "2026-06-27"
---
# Operations Runbook — Agent CLI Reference

Copy-pasteable commands for AI agents operating in gcs-core-governance. All `gh` calls **must** authenticate via the studio bot token: source `gcs-plt-gemop/hooks/github-app-token.sh` to populate `GH_TOKEN` before every command. Never run `unset GH_TOKEN` — keychain auth is unavailable in CI and automated agent pipelines.

## WI Operations

### Create an issue

```bash
source gcs-plt-gemop/hooks/github-app-token.sh
gh issue create --repo GenCr-ft/gcs-core-governance \
  --title "[GOV] Short description" \
  --body-file /tmp/issue-body.md
```

### Create a branch

```bash
git checkout main && git pull
git checkout -b feat/issue-{N}-{slug}
```

### Commit format (enforced by commitlint)

```
type(scope): WI-N.M — description
```

Types: `feat`, `fix`, `refactor`, `test`, `docs`, `chore`, `ci`  
`Co-Authored-By` trailer: **strictly prohibited**

### Create a PR

```bash
source gcs-plt-gemop/hooks/github-app-token.sh
gh pr create --repo GenCr-ft/gcs-core-governance \
  --title "type(scope): WI-N — description" \
  --body-file /tmp/pr-body.md \
  --base main \
  --head feat/issue-{N}-{slug}
```

### Merge a PR (squash)

```bash
source gcs-plt-gemop/hooks/github-app-token.sh
gh pr merge {PR_NUMBER} --repo GenCr-ft/gcs-core-governance --squash --delete-branch
```

### Close an issue with comment

```bash
source gcs-plt-gemop/hooks/github-app-token.sh
gh issue close {N} --repo GenCr-ft/gcs-core-governance --comment "Merged in PR #{PR}."
```

## Lifecycle Stamp

### Pre-condition: verify gcs-plt-gemop is co-located

`gcs-plt-gemop` must be cloned as a sibling directory to `gcs-core-governance` at the workspace collection root (e.g., `~/hxgn/dev/claude/exp/gcs-plt-gemop/`). Run this check before issuing any stamp command:

```bash
test -f $(git -C . rev-parse --show-toplevel)/../gcs-plt-gemop/hooks/lifecycle_stamp.py \
  || echo "ERROR: gcs-plt-gemop not found at sibling path — clone it before continuing"
```

### Write a stamp (REFINE gate)

```bash
python3 $(git -C . rev-parse --show-toplevel)/../gcs-plt-gemop/hooks/lifecycle_stamp.py write \
  gcs-core-governance \
  feat/issue-{N}-{slug} \
  {N} \
  refine
```

Stamp written to: `/tmp/lifecycle/gcs-core-governance-feat-issue-{N}-{slug}.json`

### Verify a stamp exists

The `/tmp` stamp is volatile and may be lost on agent restart or container flush. Use the following two-step procedure:

**Step 1 — check /tmp (fast path):**

```bash
cat /tmp/lifecycle/gcs-core-governance-feat-issue-{N}-{slug}.json
```

**Step 2 — fallback: query GitHub issue comments (durable source of truth):**

If Step 1 returns file-not-found, run:

```bash
unset GH_TOKEN
gh issue view {N} --repo GenCr-ft/gcs-core-governance --comments \
  | grep -E '✅ LIFECYCLE:(REFINE|IMPLEMENT):PASS'
```

A matching line confirms the gate was passed in a prior session. Absence of both the `/tmp` stamp **and** a matching GitHub comment means the gate was never passed and must be executed.

## LIFECYCLE Comment Strings

Post these exact strings as GitHub issue comments (no surrounding text required):

| Gate | Comment string |
|------|---------------|
| CREATE pass | `✅ LIFECYCLE:CREATE:PASS` |
| REFINE pass | `✅ LIFECYCLE:REFINE:PASS` |
| REFINE fail | `❌ LIFECYCLE:REFINE:FAIL — <gap list>` |
| DESIGN ready | `✅ LIFECYCLE:DESIGN:READY — ready for human review and status:approved label` |
| IMPLEMENT pass | `✅ LIFECYCLE:IMPLEMENT:PASS` |
| CLOSE pass | `✅ LIFECYCLE:CLOSE:PASS` |
| Close blocked | `LIFECYCLE:CLOSE:BLOCKED — sub-issue #<M> is open and undeferred` |

Post via:

```bash
source gcs-plt-gemop/hooks/github-app-token.sh
# Gate 1 — CREATE
gh issue comment {N} --repo GenCr-ft/gcs-core-governance --body "✅ LIFECYCLE:CREATE:PASS"
# Gate 2 — REFINE
gh issue comment {N} --repo GenCr-ft/gcs-core-governance --body "✅ LIFECYCLE:REFINE:PASS"
```

## Error Handling

| HTTP status | Cause | Action |
|-------------|-------|--------|
| 404 | Issue / branch not found | Verify issue number; check `gh issue list --repo GenCr-ft/gcs-core-governance` |
| 403 | Auth / scope missing | Re-source `gcs-plt-gemop/hooks/github-app-token.sh` to refresh `GH_TOKEN`; verify with `gh auth status` |
| 422 | Branch already exists | Use `git branch -d feat/issue-{N}-{slug}` then recreate |
| 429 | Rate limit hit | Wait 60s; avoid parallel `gh` calls |
| 5xx | GitHub API unavailable | Retry after 30s; check https://githubstatus.com |
| self-approval | Label setter = current login | A different human must set `status:approved` |

## Parity Check

Verify agent-context/ routing table matches storage-rules.yml:

```bash
python3 scripts/verify_agent_context_parity.py
```

Exit 0 = PASS. Exit 1 = FAIL (rule IDs listed).

## Template Registry

Templates referenced in `collaboration-algorithms.md`:

| Template | Status | Location |
|----------|--------|----------|
| `disagreement-formalization-template.md` | Not yet authored | File issue in gcs-core-governance |
| `decision-template.md` | Not yet authored | File issue in gcs-core-governance |
| `escalation-template.md` | Not yet authored | File issue in gcs-core-governance |

When a template is needed and does not exist: create a minimal inline version in the issue body and file a follow-up to formalize it.
