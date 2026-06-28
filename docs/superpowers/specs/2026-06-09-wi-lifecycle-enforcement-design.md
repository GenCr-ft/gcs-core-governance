---
docId: GOV-SPEC-003-DESIGN
title: Work Item Lifecycle Quality Enforcement — Design Spec
version: 1.0.0
authors: [Studio Lead]
knowledgeGuardian:
- Orion (GCT-UTL-SLG-001)
creation_date: '2026-06-09'
last_updated_date: '2026-06-28'
language: en
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/docs/superpowers/specs/2026-06-09-wi-lifecycle-enforcement-design.md
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: specification
  intended-audience:
  - ai-agents
  - contributors
  - governance-team
  security-classification: l2_confidential
---

# Work Item Lifecycle Quality Enforcement — Design Spec

**Date**: 2026-06-09
**Status**: Approved
**Epic**: [gcs-pm#320](https://github.com/GenCr-ft/gcs-project-management/issues/320)
**Parent initiative**: [gcs-pm#300](https://github.com/GenCr-ft/gcs-project-management/issues/300)

---

## Problem

The GenCr@ft AI workflow relies on CLAUDE.md rules and skills to guide Claude through the Work
Item lifecycle. This is prompt-based adherence — the AI is told what to do but not mechanically
blocked from skipping gates.

Confirmed recurring failure modes (session analysis 2026-06-09):
- Missed AC checkboxes at PR merge
- Premature `Closes #X` references before evidence is posted
- Commits landing on `main` or the wrong branch
- Code written before `[DESIGN]` sub-issue or implementation plan exists
- Plans saved to local files instead of GitHub issue comments

These are predictable failure modes of prompt-only enforcement at specific lifecycle transitions.

---

## Decision

**Three-Layer Hybrid Gate Architecture** (gcs-pm#320 decision log):

| Layer | Surface | Gate strength | When it fires |
|-------|---------|--------------|---------------|
| L1 — Claude Code Hooks | `issue-context-gate.py`, `git-safety-check.sh` | Hard (exit 2) | Before every Edit/Write/Bash commit |
| L2 — GitHub Actions | `gcd-shared-actions` reusable workflow | Hard (required status check) | PR open/update, issue open/edit |
| L3 — Lifecycle Skill | `wi-lifecycle` (elevated `work-item-refinement`) | Soft-hard (stamp verified by L1) | Each phase transition |

---

## Lifecycle Gate Map

```
Issue Created
    └─▶ [L2] Issue template enforces: Summary, AC (free-text), Architecture Impact, Out of Scope
    └─▶ [L3] wi-lifecycle "create" → posts gap report to issue if required fields missing
             Output: ✅ LIFECYCLE:CREATE:PASS or ❌ LIFECYCLE:CREATE:FAIL — <gap list>

Branch cut  feat/issue-N-slug  (issue number parsed from branch: feat/issue-(\d+)-*)
    └─▶ [L1] issue-context-gate.py [PHASE=refine]:
              branch matches WI pattern? linked issue open? issue not closed?
    └─▶ [L3] wi-lifecycle "refine" → AC in Gherkin? Testability Notes present? DESIGN sub-issue
              linked in parent WI tasklist?
              MUST be invoked before any Edit/Write; stamp written on pass
             Output: ✅ LIFECYCLE:REFINE:PASS or ❌ LIFECYCLE:REFINE:FAIL — <gap list>

Code write  Edit / Write / MultiEdit  [PHASE=design → implement transition]
    └─▶ [L1] issue-context-gate.py [PHASE=implement]:
              stamp present and phase=implement? if absent → GitHub API fallback
              DESIGN sub-issue closed + status:approved by human?
              IMPL sub-issue exists + status:approved by human?
              Both sub-issues linked in parent WI tasklist?
             exit 2 with specific failing gate if any check fails

Commit
    └─▶ [L1] git-safety-check.sh:
              branch is NOT main/master/prod? → exit 2 if violated
              commit message matches  type(scope): WI-N.M — * ? → exit 2 if violated

PR opened
    └─▶ [L2] PR template populated: traceability, AC evidence links, review outcomes
    └─▶ [L2] GitHub Actions [PHASE=review]:
              AC checkboxes on parent WI issue all ticked?
              evidence comment per AC present on parent WI (marker: ✅ AC-N satisfied)?
              LIFECYCLE:CODE-REVIEW:PASS marker in a PR comment?
              LIFECYCLE:SECURITY-REVIEW:PASS marker in a PR comment?
              LIFECYCLE:DATA-RISK:ASSESSED marker in a PR comment?
              detect-secrets baseline clean on changed files?
              branch pattern valid? Closes #N issue open?
              all PR checklist boxes ticked?

PR merged
    └─▶ [L3] wi-lifecycle "close":
              all L2 checks confirmed via GitHub API?
              code review comment contains PASS verdict or explicit finding disposition?
              security review contains OWASP-aligned pass or accepted-risk statement?
              data risk comment present with justification?
              ADR filed/referenced if wire format, auth, or persistence changed?
              if all pass → post ✅ LIFECYCLE:CLOSE:PASS and permit Closes #N
              if any fail → post ❌ LIFECYCLE:CLOSE:FAIL — <gap list> and exit 2
```

---

## Issue Template — Required Sections by Phase Gate

### Gate 1 — Creation (required to open issue)

| Section | Format |
|---------|--------|
| `## Summary` | 1–3 sentences, problem statement |
| `## Acceptance Criteria` | Free-text at creation |
| `## Architecture Impact` | Rough — which systems/schemas touched |
| `## Out of Scope` | Explicit boundary |

### Gate 2 — Design gate (required before DESIGN sub-issue can be approved)

| Section | Upgrade required |
|---------|------------------|
| `## Acceptance Criteria` | Must be Gherkin (`Given/When/Then`) — QA refines |
| `## Architecture Impact` | Detailed — specific interfaces, schemas, services |
| `## Testability Notes` | QA-authored: test types, tooling, data requirements |

### Gate 3 — Implementation gate (required before Edit/Write unblocked)

| Artifact | Condition |
|----------|----------|
| `[DESIGN]` sub-issue | Closed + `status:approved` label |
| `[IMPL]` sub-issue | `status:approved` label + all required sections present |

---

## `[DESIGN]` Sub-issue — Required Sections

Approval model: structural sections present with non-trivial content + `status:approved` label
**set by a human reviewer** (Studio Lead or designated domain gem). Claude MUST NOT set
`status:approved` on a sub-issue it authored.

The parent WI tasklist MUST contain: `- [ ] #<DESIGN-issue-number>` before this gate can pass.

```markdown
## Schemas & Data Models
## Interface Signatures
## Rejected Alternatives
## Architecture Diagram / C4 Impact
## Open Questions
```

A section passes if it contains at least one non-blank, non-header line after the `##` marker.
`N/A` with a one-line justification counts as content; a completely empty section fails.

The L3 skill posts `✅ LIFECYCLE:DESIGN:READY` as a comment on the sub-issue when all sections
pass, signalling to the human reviewer that the sub-issue is ready for `status:approved`.

---

## `[IMPL]` Sub-issue — Required Sections

Approval model: all sections present + at least one TDD Cycle + `status:approved` label **set by
a human reviewer**. Claude MUST NOT set `status:approved` on a sub-issue it authored.

The parent WI tasklist MUST contain: `- [ ] #<IMPL-issue-number>` before this gate can pass.

```markdown
## Desired Outcome
[2–3 sentences: what this WI delivers from the user/system perspective]

## AC Coverage Map
| AC Ref | Scenario Title | Covered by Cycle(s) |
|--------|---------------|---------------------|
| AC-1   | ...           | Cycle 1, Cycle 2    |

## Technical Scope
### Schema & Migration Changes
### Port / Interface Changes
### Adapter / Implementation Notes

## TDD Cycles
### Cycle 1 — [descriptive name]
- **Red**: `test/path/file.test.ts` — asserts [X]
  Commit: `test(scope): WI-N.M — red: AC-K [X]`
- **Green**: `src/path/file.ts` — implements [Y]
  Commit: `feat(scope): WI-N.M — green: AC-K [Y]`
- **Blue**: refactor [Z]
  Commit: `refactor(scope): WI-N.M — blue: [Z]`

## Integration & E2E Verification

## Risk Register
| Risk | Likelihood | Impact | Mitigation |
|------|-----------|--------|------------|

## External Dependencies

## Rollback Plan

## Definition of Done
- [ ] All TDD cycles committed (red → green → blue)
- [ ] AC Coverage Map fully exercised
- [ ] Integration tests passing
- [ ] PR opened referencing parent WI and this sub-issue
```

### Machine-checkability contract

Required top-level section headers (12): `## Desired Outcome`, `## AC Coverage Map`,
`## Technical Scope`, `## TDD Cycles`, `## Integration & E2E Verification`,
`## Risk Register`, `## External Dependencies`, `## Rollback Plan`, `## Definition of Done`.
Required sub-headers under Technical Scope (3): `### Schema & Migration Changes`,
`### Port / Interface Changes`, `### Adapter / Implementation Notes`.

| Check | Layer | Rule |
|-------|-------|------|
| All required section headers present (9 top-level + 3 sub) | L1 hook | Regex on section names |
| At least 1 `### Cycle N — ` entry with descriptive name | L1 hook | Required before Edit/Write unblocked |
| Cycle names are non-generic | L3 skill | Reject names matching `^Cycle \d+ — (step\|task\|item) \d+$` |
| Each cycle has Red + Green + Blue legs | L3 skill | Checked at approval time |
| Commit message in each cycle references `AC-K` | L3 skill | Checked at approval time |
| AC Coverage Map rows ≥ parent WI AC count | L3 skill | Parity check at approval time |
| Risk Register non-empty | L3 skill | Hard reject on P0/P1; advisory on P2/P3 |
| Rollback Plan non-empty | L3 skill | Hard reject on P0/P1 |
| Max 10 cycles per IMPL | L3 skill | Flag WI as decomposition candidate if exceeded |
| `status:approved` label set by human (not by Claude) | L1 hook | Label must predate any Edit/Write on the branch |
| Parent WI tasklist contains `- [ ] #<IMPL-issue>` | L3 skill | Checked at approval time |
| `✅ LIFECYCLE:IMPL:READY` comment present | L3 skill | Posted by skill before human approval |

---

## PR Closure — Clean Closure Protocol (Option C)

Both evidence comments on the parent WI issue AND a PR checklist are required.

### Evidence comments (on the parent WI issue — durable)

Before `Closes #N` is written into the PR body, Claude must post one evidence comment per AC.
The comment MUST begin with the exact marker `✅ AC-N satisfied` (machine-parsed by L2 Action).

```markdown
✅ AC-1 satisfied — PR #<number>, commit <sha>
Scenario: `<Gherkin scenario title from parent WI>`
Test: `test/auth/jwt-validation.test.ts:42` — `JwtValidationService returns 401 on expired token`
Output:
```
PASS test/auth/jwt-validation.test.ts
  JwtValidationService
    ✓ returns 401 on expired token (12ms)
Test Suites: 1 passed | Tests: 1 passed
```
```

The PR number and commit SHA anchor the comment to a specific merge event. Evidence comments
survive PR deletion and form the permanent audit trail on the WI.

### PR template checklist (visible to reviewers)

```markdown
## PR Checklist

### Traceability
- [ ] PR title follows `feat(scope): WI-N.M — description`
- [ ] Parent WI linked: Closes #N (only tick when all AC boxes ticked on parent issue)
- [ ] `[IMPL]` sub-issue linked

### Acceptance Criteria Evidence
- [ ] AC-1: evidence comment posted on parent WI (link: )
- [ ] AC-2: evidence comment posted on parent WI (link: )
<!-- add one line per AC -->

### Code Review (mandatory — independent contradictory pass)
- [ ] `/review-pr-code-quality` run and all findings resolved or explicitly accepted with rationale
- [ ] No dead code, no commented-out blocks, no TODO left in changed files
- [ ] Naming, abstractions, and module boundaries reviewed against Clean Architecture rules
- [ ] Review outcome posted as PR comment beginning with `LIFECYCLE:CODE-REVIEW:PASS` or `LIFECYCLE:CODE-REVIEW:FINDINGS` followed by disposition for each finding

### Security Analysis (mandatory)
- [ ] `/review-pr-security` run against the diff
- [ ] No secrets, tokens, or credentials in any changed file (detect-secrets baseline clean)
- [ ] Auth/authz paths reviewed: no bypass, no privilege escalation, no missing guards
- [ ] Input validation reviewed at all system boundaries (user input, external APIs, WebSocket messages)
- [ ] Security review outcome posted as PR comment beginning with `LIFECYCLE:SECURITY-REVIEW:PASS` or `LIFECYCLE:SECURITY-REVIEW:FINDINGS` followed by OWASP finding list with disposition

### Data Loss & Destructive Operation Risk
- [ ] No irreversible schema migrations without a rollback script committed alongside
- [ ] No `DELETE`/`DROP`/`TRUNCATE` without explicit confirmation gate in code
- [ ] No voxel data, player state, or world data written without write-ahead or idempotency guarantee
- [ ] Data risk assessment posted as PR comment beginning with `LIFECYCLE:DATA-RISK:NONE`, `LIFECYCLE:DATA-RISK:MITIGATED`, or `LIFECYCLE:DATA-RISK:ACCEPTED` followed by justification

### Documentation
- [ ] All changed public interfaces have updated doc comments
- [ ] CHANGELOG updated (user-facing changes) or explicitly marked `N/A`
- [ ] If wire format, auth, or persistence changed: relevant ADR updated or new ADR filed
- [ ] If a new skill, hook, or gem was added: `gcs-plt-gemop` updated and symlinks verified

### Quality Gates
- [ ] All TDD cycles committed (red → green → blue per cycle)
- [ ] `./test.sh` passes locally
- [ ] No new lint or type errors
- [ ] No force-push to main

### Definition of Done
- [ ] `[IMPL]` sub-issue checklist complete
- [ ] CHANGELOG entry present or `N/A` justified
- [ ] Memory/tracker files updated
```

### L2 GitHub Actions validation

The reusable workflow in `gcd-shared-actions` validates on `pull_request` events:

| Check | Failure mode | Action |
|-------|-------------|--------|
| Branch name matches `feat/issue-N-*` or `fix/issue-N-*` | Block merge | Post comment with correct format |
| `Closes #N` present and issue #N exists + is open | Block merge | Post comment if issue closed or missing |
| AC checkboxes on parent WI issue are all ticked | Block merge | Post comment listing unticked boxes |
| Evidence comment exists on WI per AC | Block merge | Post comment listing missing ACs |
| PR checklist boxes all ticked | Block merge | Post comment listing unticked items |
| detect-secrets baseline clean on changed files | Block merge | Post comment with offending file list |
| Code review outcome comment present on PR | Block merge | Post reminder: `/review-pr-code-quality` required |
| Security review outcome comment present on PR | Block merge | Post reminder: `/review-pr-security` required |
| Data risk assessment comment present on PR | Block merge | Post reminder: data risk assessment required |

### L3 wi-lifecycle "close" gate additions

Before the `wi-lifecycle` skill permits issue closure, it also verifies:

| Check | Condition |
|-------|----------|
| Code review comment present on PR | Must contain pass verdict or explicit finding disposition |
| Security review comment present on PR | Must contain OWASP-aligned pass or accepted-risk statement |
| Data risk comment present on PR | Must exist; empty risk (`none`) is valid if justified |
| ADR filed or existing ADR referenced | Required if wire format, auth, or persistence was changed |
| Documentation checklist items all ticked | Hard reject if any doc item is unticked without `N/A` |

---

## Agent Behavioral Contract

This section defines hard constraints on AI agent behavior. Violation of any MUST NOT rule is
grounds for a hook to emit exit 2. These rules supplement the gate map — they are not optional.

### MUST NOT — hard prohibitions (L1 hook enforces these via exit 2)

| Prohibition | Enforcement |
|-------------|-------------|
| MUST NOT write `Closes #N` in a PR body before all AC checkboxes are ticked on the parent WI | L2 Action blocks merge |
| MUST NOT set `status:approved` on any sub-issue it authored — self-approval is forbidden | L1 hook checks label setter via GitHub API |
| MUST NOT commit directly to `main`, `master`, or `prod` | L1 `git-safety-check.sh` |
| MUST NOT commit to a branch that does not match `feat/issue-N-*` or `fix/issue-N-*` | L1 hook |
| MUST NOT create or modify source files without a valid open WI issue linked to the current branch | L1 `issue-context-gate.py` |
| MUST NOT skip a lifecycle gate — bypasses require a pre-posted audit comment and `lifecycle:bypass` label set by human | L1 hook checks label + comment |
| MUST NOT merge a PR with unresolved review threads | L2 Action (GitHub branch protection) |
| MUST NOT close a parent WI issue manually — closure only via `Closes #N` in a merged PR | L3 wi-lifecycle "close" gate |
| MUST NOT create `[DESIGN]` or `[IMPL]` sub-issues without linking them in the parent WI tasklist (`- [ ] #N`) | L3 skill validates at gate transition |
| MUST NOT proceed to the next lifecycle phase without the previous phase's `LIFECYCLE:*:PASS` comment present on the issue | L1 stamp + GitHub API fallback |

### MUST — mandatory behaviors

| Obligation | When |
|------------|------|
| Invoke `wi-lifecycle` skill at each phase transition | Before Edit/Write on a new phase |
| Post one `✅ AC-N satisfied` evidence comment per AC on the parent WI | Before opening a PR |
| Post `LIFECYCLE:CODE-REVIEW:PASS/FINDINGS` comment on PR | Before requesting merge |
| Post `LIFECYCLE:SECURITY-REVIEW:PASS/FINDINGS` comment on PR | Before requesting merge |
| Post `LIFECYCLE:DATA-RISK:*` comment on PR | Before requesting merge |
| Post audit comment explaining bypass reason BEFORE setting `lifecycle:bypass` label | On any bypass |
| File a GitHub Issue for any gap, defect, or action item discovered during work | Immediately on discovery |

### On gate failure — required agent response

When L1 emits exit 2, the agent MUST:
1. Read the full error message emitted to stderr — the gate name and specific failing condition are included.
2. Diagnose the root cause from the message. Do not attempt to re-issue the blocked command.
3. Take the corrective action dictated by the failing gate (e.g. invoke `wi-lifecycle`, create missing sub-issue, wait for human approval).
4. Only re-attempt the blocked command after the gate condition is satisfied and confirmed.

The agent MUST NOT attempt to work around a gate failure by using a different tool (e.g. switching from `Edit` to `Bash echo >`) or by approving its own bypass.

---

## Lifecycle Stamp Mechanism

The stamp bridges L3 (skill invocation) and L1 (hook enforcement), with resilience to skill
non-determinism.

### Write path (skill → stamp)

The hook determines repo and branch at runtime:
- `REPO=$(basename $(git rev-parse --show-toplevel))`
- `BRANCH=$(git rev-parse --abbrev-ref HEAD)`
- `ISSUE=$(echo $BRANCH | grep -oP 'issue-\K\d+')`  ← issue number parsed from branch name

When `wi-lifecycle` passes a phase gate, it:
1. Writes `/tmp/lifecycle/<repo>-<branch>.json` (fast local cache, per-branch, per-worktree)
2. Posts a structured comment on the GitHub issue (durable audit trail)

```json
{
  "repo": "gcp-aethel-server",
  "branch": "feat/issue-104-inventory-service",
  "issue": 104,
  "phase": "refine",
  "passed_at": "2026-06-09T14:30:00Z",
  "issue_state_hash": "sha256:abc123...",
  "gates_passed": ["ac_gherkin", "testability_notes", "design_sub_issue_linked"]
}
```

The GitHub comment begins with `✅ LIFECYCLE:<PHASE>:PASS` — this is the machine-parseable
marker the L1 hook searches for when `/tmp/` is absent.

### Read path (L1 hook → decision)

```
L1 hook fires on Edit/Write
  └─▶ Derive REPO, BRANCH, ISSUE from git commands
  └─▶ Check /tmp/lifecycle/<repo>-<branch>.json
        ├─▶ Present + phase matches required phase + hash matches issue state → proceed
        ├─▶ Present + hash stale → re-check GitHub issue comments directly (API call)
        └─▶ Absent (new session, reboot, or skill not invoked)
              └─▶ Query GitHub: latest comment on issue #ISSUE containing
                  LIFECYCLE:<REQUIRED-PHASE>:PASS
                    ├─▶ Found → write /tmp/ cache + proceed
                    └─▶ Not found → exit 2:
                        "❌ LIFECYCLE GATE BLOCKED [<REQUIRED-PHASE>]
                         Issue #<N> has not passed the <phase> gate.
                         Run: wi-lifecycle <phase> to validate and record passage.
                         Specific failing condition: <condition>"
```

Each worktree has its own `/tmp/lifecycle/<repo>-<branch>.json` — parallel WI agents MUST NOT
share stamp files across branches.

### Bypass escape

A human must:
1. Post a comment on the issue: `LIFECYCLE:BYPASS — gate: <gate-name> — reason: <reason>`
2. Set the `lifecycle:bypass` label on the issue.

The L1 hook checks for both the comment AND the label before permitting bypass. Claude MUST NOT
post the bypass comment on its own behalf or set the label itself. Silent bypass is never
permitted — the hook posts a second audit comment confirming which gate was bypassed.

---

## Delivery Phases

| Phase | Scope | Repos | Effort |
|-------|-------|-------|--------|
| P1 — Hook Extension | Extend `issue-context-gate.py`, `git-safety-check.sh`, stamp mechanism | `gcs-plt-gemop` | ~2 days |
| P2 — GitHub Actions Gate | Reusable workflow + issue/PR templates + rollout to 5 active repos | `gcd-shared-actions`, `gcp-aethel-server`, `gcp-aethel-client`, `gcl-srv-authentication`, `gcl-srv-persistence`, `gcp-aethel-pcg` | ~2 days |
| P3 — Lifecycle Skill Elevation | `wi-lifecycle` skill; `GOV-PROC-WI-001`; integration tests in `gcd-ops-scripts` | `gcs-plt-gemop`, `gcs-core-governance`, `gcd-ops-scripts` | ~2 days |

---

## Governance Contract Document

A single `GOV-PROC-WI-001` document in `gcs-core-governance` defines the canonical lifecycle
contract. All three layers reference it. Changes to gate requirements go through a PR on
`gcs-core-governance` first — the hook, action, and skill update as follow-up PRs.

---

## Constraints & Non-Goals

- The L1 hook validates **structure and state**, not content quality — quality is L3's job.
- The L3 skill validates **quality** at transition time only — not on every tool call.
- This spec does not cover the `[DESIGN]` sub-issue authoring workflow — governed by `work-item-refinement`.
- Skill non-determinism is a known constraint. The stamp + GitHub API fallback in L1 are the
  mitigations. The design does not assume Claude always invokes the skill.
- L1 hook cannot verify **who** set a label on a sub-issue without a GitHub API call to
  `GET /repos/{owner}/{repo}/issues/{number}/events` — this call is included in the hook's
  DESIGN/IMPL approval check to confirm the label setter is not the branch author.
- GitHub-unavailable / offline scenarios: if the GitHub API is unreachable, L1 falls back to
  the `/tmp/` stamp only. If `/tmp/` is also absent, L1 blocks with a connectivity advisory
  rather than a hard gate failure — this is the only case where a gate can be deferred.
- This spec does not govern exploratory or spike branches (named `spike/*`). Spike branches
  are exempt from lifecycle gates but MUST NOT be merged to `main` directly — a WI branch
  must be cut from the spike findings before merge.
