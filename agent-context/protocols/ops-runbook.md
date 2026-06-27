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

Copy-pasteable commands for AI agents operating in gcs-core-governance. All `gh` calls require `unset GH_TOKEN` to use keychain auth.

## WI Operations

### Create an issue

```bash
unset GH_TOKEN
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
unset GH_TOKEN
gh pr create --repo GenCr-ft/gcs-core-governance \
  --title "type(scope): WI-N — description" \
  --body-file /tmp/pr-body.md \
  --base main \
  --head feat/issue-{N}-{slug}
```

### Merge a PR (squash)

```bash
unset GH_TOKEN
gh pr merge {PR_NUMBER} --repo GenCr-ft/gcs-core-governance --squash --delete-branch
```

### Close an issue with comment

```bash
unset GH_TOKEN
gh issue close {N} --repo GenCr-ft/gcs-core-governance --comment "Merged in PR #{PR}."
```

## Lifecycle Stamp

### Write a stamp (REFINE gate)

```bash
python3 gcs-plt-gemop/hooks/lifecycle_stamp.py write \
  gcs-core-governance \
  feat/issue-{N}-{slug} \
  {N} \
  refine
```

Stamp written to: `/tmp/lifecycle/gcs-core-governance-feat-issue-{N}-{slug}.json`

### Verify a stamp exists

```bash
cat /tmp/lifecycle/gcs-core-governance-feat-issue-{N}-{slug}.json
```

## LIFECYCLE Comment Strings

Post these exact strings as GitHub issue comments (no surrounding text required):

| Gate | Comment string |
|------|---------------|
| REFINE pass | `✅ LIFECYCLE:REFINE:PASS` |
| REFINE fail | `❌ LIFECYCLE:REFINE:FAIL — <gap list>` |
| DESIGN ready | `✅ LIFECYCLE:DESIGN:READY — ready for human review and status:approved label` |
| IMPLEMENT pass | `✅ LIFECYCLE:IMPLEMENT:PASS` |
| CLOSE pass | `✅ LIFECYCLE:CLOSE:PASS` |
| Close blocked | `LIFECYCLE:CLOSE:BLOCKED — sub-issue #<M> is open and undeferred` |

Post via:

```bash
unset GH_TOKEN
gh issue comment {N} --repo GenCr-ft/gcs-core-governance --body "✅ LIFECYCLE:REFINE:PASS"
```

## Error Handling

| HTTP status | Cause | Action |
|-------------|-------|--------|
| 404 | Issue / branch not found | Verify issue number; check `gh issue list --repo GenCr-ft/gcs-core-governance` |
| 403 | Auth / scope missing | Run `unset GH_TOKEN`; verify keychain via `gh auth status` |
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
