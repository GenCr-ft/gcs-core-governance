---
docId: GOV-PROTO-OR-001
title: Operations Runbook — Agent CLI Reference
version: 1.0.1
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: protocol
  intended-audience: [ai-agents]
  security-classification: l2_confidential
  source_version: "1.0.0"
  last_verified: "2026-06-28"
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
git checkout develop && git pull
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
  --base develop \
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
bash scripts/lifecycle-stamp.sh write \
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

### Issue comments (Gate 1–3 phase markers)

Post these exact strings as GitHub **issue** comments (no surrounding text required):

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

### PR comments (Gate 4 close-review markers)

Post these exact strings as GitHub **PR** comments before the close gate (GOV-PROT-003 Gate 4):

| Review type | Comment string |
|-------------|---------------|
| Code review clean | `LIFECYCLE:CODE-REVIEW:PASS` |
| Code review findings accepted | `LIFECYCLE:CODE-REVIEW:FINDINGS` |
| Security review clean | `LIFECYCLE:SECURITY-REVIEW:PASS` |
| Security review findings accepted | `LIFECYCLE:SECURITY-REVIEW:FINDINGS` |
| No data risk | `LIFECYCLE:DATA-RISK:NONE` |
| Data risk mitigated | `LIFECYCLE:DATA-RISK:MITIGATED` |
| Data risk accepted | `LIFECYCLE:DATA-RISK:ACCEPTED` |
| Human-authored bypass | `LIFECYCLE:BYPASS — gate: <name> — reason: <justification>` |

Post via:

```bash
source gcs-plt-gemop/hooks/github-app-token.sh
gh pr comment {PR_NUMBER} --repo GenCr-ft/gcs-core-governance --body "LIFECYCLE:CODE-REVIEW:PASS"
```

## Adversary Review

Triggered automatically by `wi-lifecycle` when `adversary_review: true` is set in `wi-lifecycle-gates.yml` (DESIGN phase line 49, IMPLEMENT phase line 77). Can also be invoked directly.

### Invocation syntax

```
wi-lifecycle-adversary <review-type> <artifact-ref>
```

| `review-type` | When to use | `artifact-ref` |
|--------------|-------------|----------------|
| `design-review` | After `[DESIGN]` sub-issue is authored, before posting `LIFECYCLE:DESIGN:READY` | `[DESIGN]` sub-issue number (e.g. `#212`) |
| `impl-review` | After `[IMPL]` sub-issue is authored, before posting `LIFECYCLE:IMPLEMENT:PASS` | `[IMPL]` sub-issue number |
| `pr-review` | After PR is open, before posting `LIFECYCLE:CLOSE:PASS` | PR number (e.g. `PR#45`) |

Examples:

```
wi-lifecycle-adversary design-review #212
wi-lifecycle-adversary impl-review #213
wi-lifecycle-adversary pr-review PR#45
```

### Severity tier schema

An adversary finding must be classified as one of the following tiers. The gate blocker `critical_or_high_adversary_finding_unresolved` in `wi-lifecycle-gates.yml` lines 54 and 86 is satisfied (i.e. the gate is BLOCKED) when any CRITICAL or HIGH finding is unresolved.

| Tier | Definition | Gate behaviour |
|------|-----------|----------------|
| CRITICAL | A gap that makes the artifact un-implementable or structurally unsound — missing schema, contradictory interface, untestable AC. | Block gate. Post `LIFECYCLE:ADVERSARY-REVIEW:<PHASE>:FINDINGS`. Stop. Implementer must fix and re-trigger adversary. |
| HIGH | A significant gap that can be remediated without a full redesign — missing section, ambiguous field type, incomplete rollback path. | Block gate. Post `LIFECYCLE:ADVERSARY-REVIEW:<PHASE>:FINDINGS`. Stop. Implementer posts `ADVERSARY-REVIEW:DISPOSITION` comment; gate re-runs and posts `LIFECYCLE:ADVERSARY-REVIEW:<PHASE>:FINDINGS-DISPOSITIONED`. |
| LOW | A minor improvement — wording, optional field, style. | Do not block gate. Post `LIFECYCLE:ADVERSARY-REVIEW:<PHASE>:PASS` with findings in body. |

`<PHASE>` ∈ {`DESIGN`, `IMPL`, `PR`}.

### Adversary comment tokens

| Outcome | Comment token |
|---------|---------------|
| DESIGN: no blocking findings | `LIFECYCLE:ADVERSARY-REVIEW:DESIGN:PASS` |
| DESIGN: CRITICAL or HIGH finding | `LIFECYCLE:ADVERSARY-REVIEW:DESIGN:FINDINGS` |
| DESIGN: HIGH finding dispositioned | `LIFECYCLE:ADVERSARY-REVIEW:DESIGN:FINDINGS-DISPOSITIONED` |
| IMPL: no blocking findings | `LIFECYCLE:ADVERSARY-REVIEW:IMPL:PASS` |
| IMPL: CRITICAL or HIGH finding | `LIFECYCLE:ADVERSARY-REVIEW:IMPL:FINDINGS` |
| IMPL: HIGH finding dispositioned | `LIFECYCLE:ADVERSARY-REVIEW:IMPL:FINDINGS-DISPOSITIONED` |
| PR: no blocking findings | `LIFECYCLE:ADVERSARY-REVIEW:PR:PASS` |
| PR: CRITICAL or HIGH finding | `LIFECYCLE:ADVERSARY-REVIEW:PR:FINDINGS` |
| PR: HIGH finding dispositioned | `LIFECYCLE:ADVERSARY-REVIEW:PR:FINDINGS-DISPOSITIONED` |

Post via:

```bash
unset GH_TOKEN
gh issue comment {N} --repo GenCr-ft/gcs-core-governance --body "LIFECYCLE:ADVERSARY-REVIEW:DESIGN:PASS"
```

Full skill specification (dispatch prompt format, challenge dimensions, accepted-findings registry): `gcs-plt-gemop/skills/wi-lifecycle-adversary/SKILL.md`.

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

Templates used by agent collaboration protocols:

| Template | Referenced In | Status | Location |
|----------|---------------|--------|----------|
| `disagreement-formalization-template.md` | collaboration-algorithms.md line 31 (Algorithm 2) | Not yet authored | `agent-context/protocols/templates/disagreement-formalization-template.md` |
| `decision-template.md` | collaboration-algorithms.md line 43 (Algorithm 3) | Not yet authored | `agent-context/protocols/templates/decision-template.md` |
| `incident-report-template.md` | collaboration-algorithms.md line 63 (Algorithm 5) | Not yet authored | `agent-context/protocols/templates/incident-report-template.md` |
| `protocol-change-proposal-template.md` | collaboration-algorithms.md line 70 (Algorithm 6) | Not yet authored | `agent-context/protocols/templates/protocol-change-proposal-template.md` |
| `escalation-template.md` | Algorithm 2 escalation flow | Not yet authored | `agent-context/protocols/templates/escalation-template.md` |

When a template is needed and does not exist: create a minimal inline version in the issue body and file a follow-up to formalize it.
