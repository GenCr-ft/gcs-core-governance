---
docId: GOV-PROT-003
title: Work Item Lifecycle Quality Contract
version: 1.0.0
authors: [Studio Lead]
knowledgeGuardian:
- Orion (GCT-GOV-ORN-001)
creation_date: '2026-06-09'
last_updated_date: '2026-06-11'
language: en
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/GOV-PROT-003.wi-lifecycle-contract.md
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: protocol
  intended-audience:
  - ai-agents
  - contributors
  - governance-team
  security-classification: l2_confidential
---

# Work Item Lifecycle Quality Contract

**Spec:** `docs/superpowers/specs/2026-06-09-wi-lifecycle-enforcement-design.md`
**Epic:** https://github.com/GenCr-ft/gcs-project-management/issues/320

This document is the canonical definition of what must be true at each Work Item lifecycle
gate. All three enforcement layers (L1 hooks, L2 GitHub Actions, L3 wi-lifecycle skill)
reference this contract. Changes to gate requirements require a PR to this document first;
hook, Action, and skill updates follow as separate PRs.

---

## Phase Gates

### Gate 1 — Creation

| Section | Minimum content |
|---------|----------------|
| `## Summary` | 1–3 sentences, problem statement |
| `## Acceptance Criteria` | ≥1 AC bullet (free-text) |
| `## Architecture Impact` | ≥1 non-blank line (rough) |
| `## Out of Scope` | ≥1 non-blank line |

### Gate 2 — Refine (before DESIGN sub-issue is approved)

| Upgrade required | Condition |
|-----------------|-----------|
| `## Acceptance Criteria` | All ACs in Gherkin (`Given/When/Then`) |
| `## Architecture Impact` | Detailed: interfaces, schemas, services |
| `## Testability Notes` | QA-authored: test types, tooling, data |
| `## Sub-issues` tasklist | Contains `- [ ] #N` for `[DESIGN]` sub-issue |

### Gate 3 — Implement (before Edit/Write is unblocked)

| Artifact | Required state |
|----------|---------------|
| `[DESIGN]` sub-issue | Closed + `status:approved` set by human reviewer |
| `[IMPL]` sub-issue | `status:approved` set by human reviewer |
| Both sub-issues | Linked in parent WI tasklist |
| Self-approval | Forbidden — label setter must differ from current GitHub actor |

### Gate 4 — Close (before `Closes #N` written)

| Check | Required |
|-------|---------|
| AC checkboxes on parent WI | All ticked |
| `✅ AC-N satisfied` comments | One per AC on parent WI |
| `LIFECYCLE:CODE-REVIEW:*` PR comment | Present with pass or finding disposition |
| `LIFECYCLE:SECURITY-REVIEW:*` PR comment | Present with OWASP pass or accepted-risk |
| `LIFECYCLE:DATA-RISK:*` PR comment | NONE/MITIGATED/ACCEPTED with justification |
| ADR | Referenced if wire format, auth, or persistence changed |
| PR checklist | All boxes ticked |

---

## Sub-issue Contracts

### `[DESIGN]` Required Sections

```
## Schemas & Data Models
## Interface Signatures
## Rejected Alternatives
## Architecture Diagram / C4 Impact
## Open Questions
```

A section passes with ≥1 non-blank, non-header line. `N/A` + one-line justification is valid.

### `[IMPL]` Required Sections (12 headers)

```
## Desired Outcome
## AC Coverage Map
## Technical Scope
  ### Schema & Migration Changes
  ### Port / Interface Changes
  ### Adapter / Implementation Notes
## TDD Cycles
  ### Cycle N — [descriptive name]
## Integration & E2E Verification
## Risk Register
## External Dependencies
## Rollback Plan
## Definition of Done
```

Constraints: ≥1 cycle with Red/Green/Blue legs; cycle names non-generic;
≤10 cycles (else decompose); Risk Register + Rollback non-empty on P0/P1;
AC Coverage Map rows ≥ parent AC count.

---

## Agent Behavioral Contract

### MUST NOT (hard-blocked via exit 2 or required status check)

1. Write `Closes #N` before all AC checkboxes are ticked and evidence comments are present.
2. Set `status:approved` on any sub-issue (Claude is never the approver).
3. Post `LIFECYCLE:BYPASS` on its own behalf.
4. Commit to `main`, `master`, or `prod`.
5. Commit without a `WI-N.M` ref in the message.
6. Modify source files without a valid open WI issue linked to the current branch.
7. Skip a gate without human-set `lifecycle:bypass` label AND pre-posted bypass comment.
8. Close the parent WI issue manually.
9. Begin Edit/Write on `implement`-phase work before the implement gate passes.
10. Merge a PR without all L2 required status checks green.

### MUST (obligations)

1. Invoke `wi-lifecycle <phase>` at each phase transition.
2. Post `✅ AC-N satisfied` evidence comments on the parent WI for each AC.
3. Post review outcome markers (`LIFECYCLE:CODE-REVIEW:`, `LIFECYCLE:SECURITY-REVIEW:`,
   `LIFECYCLE:DATA-RISK:`) as PR comments before the close gate.
4. Author `[DESIGN]` and `[IMPL]` sub-issues before the design gate is validated.
5. Link sub-issues in the parent WI tasklist.
6. Run `./test.sh` before opening a PR.
7. Post fix-pointer comments on resolved PR review threads.

### Gate Failure Protocol

1. Post `❌ LIFECYCLE:<PHASE>:FAIL — <gap list>` to the issue.
2. Stop all work on the WI.
3. Communicate the specific gaps to the user.
4. Wait for user direction before attempting any gap remediation that requires
   design judgement or human approval.

---

## Bypass Protocol

A **human** (not Claude) must:
1. Post on the issue: `LIFECYCLE:BYPASS — gate: <name> — reason: <justification>`
2. Set `lifecycle:bypass` label on the issue.

The L1 hook verifies both. Claude cannot satisfy either condition on its own behalf.

---

## Lifecycle Marker Tokens

Machine-parseable token set used by all three enforcement layers:

| Token | Meaning |
|-------|---------|
| `✅ LIFECYCLE:<PHASE>:PASS` | Phase gate passed; written to issue comment |
| `❌ LIFECYCLE:<PHASE>:FAIL — <gaps>` | Phase gate failed; written to issue comment |
| `LIFECYCLE:CODE-REVIEW:PASS` | Code review clean |
| `LIFECYCLE:CODE-REVIEW:FINDINGS` | Code review findings with accepted dispositions |
| `LIFECYCLE:SECURITY-REVIEW:PASS` | OWASP scan clean |
| `LIFECYCLE:SECURITY-REVIEW:FINDINGS` | Security findings with accepted-risk statements |
| `LIFECYCLE:DATA-RISK:NONE` | No data loss or destructive operation risk |
| `LIFECYCLE:DATA-RISK:MITIGATED` | Data risk present and mitigated |
| `LIFECYCLE:DATA-RISK:ACCEPTED` | Data risk accepted with justification |
| `LIFECYCLE:BYPASS — gate: <name> — reason: <text>` | Human-authored bypass justification |

---

## Evidence Comment Format

```
✅ AC-N satisfied — PR #<number>, commit <sha>
Scenario: `<Gherkin scenario title>`
Test: `<file>:<line>` — `<test description>`
Output:
\`\`\`
<actual test runner output — not placeholder>
\`\`\`
```

---

## Sub-issue Naming Convention

| Type | Title pattern | Example |
|------|--------------|---------|
| `[DESIGN]` | `[DESIGN] WI-N.M — <parent WI title>` | `[DESIGN] WI-320.3 — phase-aware issue-context-gate` |
| `[IMPL]` | `[IMPL] WI-N.M — <parent WI title>` | `[IMPL] WI-320.3 — phase-aware issue-context-gate` |

## Tasklist Position Convention

In the parent WI body, the Sub-issues tasklist must follow this order:
1. First entry: `[DESIGN]` sub-issue link
2. Second entry: `[IMPL]` sub-issue link

This order is relied on by `github_api.get_subissues_from_tasklist` in `gcs-plt-gemop/hooks/github_api.py`.
