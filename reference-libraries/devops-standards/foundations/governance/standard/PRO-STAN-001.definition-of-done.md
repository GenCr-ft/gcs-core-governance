---
docId: PRO-STAN-001
title: Definition of Done
version: 1.0.0
authors:
- Priscilla (GCT-MGT-PPM-001)
reviewers:
- Isaac (GCT-PRG-SARCH-001)
knowledgeGuardian:
- Priscilla (GCT-MGT-PPM-001)
creation_date: '2026-06-27'
language: en
summary: "Mandatory checklist of criteria a Work Item must satisfy before it may be\
  \ considered complete and its PR merged."
last_updated_date: '2026-06-27'
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: standard
  classification:
    category: to-govern
    type: standard
  keywords:
  - definition-of-done
  - dod
  - work-item
  - quality-gate
  - pr-checklist
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
---
# Definition of Done (PRO-STAN-001)

## 1. Purpose

This standard defines the mandatory exit criteria that every Work Item (WI) must
satisfy before its Pull Request may be merged. It is the authoritative reference
for `GOV_RULE_005`, which requires all PR bodies on code repositories to contain
the string `References Definition of Done (PRO-STAN-001)`.

## 2. Scope

Applies to all Work Items across all GenCr@ft Studio code repositories, regardless
of size or type (feature, fix, chore, documentation).

## 3. Definition of Done Checklist

A Work Item is considered **Done** when **all** of the following criteria are met:

### 3.1 Code Quality

- [ ] All new and modified code passes the linter (`eslint`, `ruff`, `clippy`, or
      equivalent) with zero errors.
- [ ] No new `TODO`, `FIXME`, or `HACK` comments have been introduced without a
      linked GitHub Issue.
- [ ] No empty `catch` blocks have been introduced.

### 3.2 Tests

- [ ] Unit tests cover all new logic; overall coverage does not decrease below the
      repository threshold (80% for TypeScript/Python, `cargo test` passing for Rust).
- [ ] All existing tests pass in CI.
- [ ] Integration or end-to-end tests updated or added where the change touches an
      integration boundary.

### 3.3 Architecture and Design

- [ ] The implementation matches the `[DESIGN]` sub-issue approved for this WI.
- [ ] If the change modifies a wire format, auth flow, or data-storage schema, an ADR
      has been authored and linked.
- [ ] Hexagonal architecture boundaries are respected (no direct adapter-to-adapter
      calls without a port).

### 3.4 Documentation

- [ ] Public APIs, ports, and domain entities are documented (JSDoc / docstrings /
      rustdoc as appropriate).
- [ ] `CHANGELOG.md` updated if the change is user-facing or breaking.
- [ ] Relevant SSoT documents (`AGENTS.md`, README, specs) updated to reflect the
      change.

### 3.5 Governance and Process

- [ ] PR body contains `References Definition of Done (PRO-STAN-001)` (satisfies
      `GOV_RULE_005`).
- [ ] PR is linked to its parent GitHub Issue.
- [ ] PR title follows Conventional Commits: `feat(scope): WI-X.Y — <description>`.
- [ ] All open review threads are resolved before merge.
- [ ] No force-push to `main` without explicit Studio Lead approval.

### 3.6 Security

- [ ] No secrets, credentials, or PII introduced in code or tests.
- [ ] `detect-secrets` baseline updated if new non-secret patterns were flagged.

## 4. Relation to Other Documents

| Document | Relationship |
|----------|--------------|
| `GOV-PROT-003` (WI Lifecycle Contract) | Governs the 5-gate lifecycle; DoD is the exit gate for the *Implement* phase. |
| `validation-rules.yml` `GOV_RULE_005` | Enforces that every code-repo PR body cites this document. |
| `agent-context/grounding/lexicon.yml` | Defines `DoD` term, citing this document as the canonical reference. |

## 5. Versioning

Changes to this standard require:
1. A GitHub Issue in `gcs-core-governance`.
2. Review by the Knowledge Guardian (Priscilla) and Senior Architect (Isaac).
3. A version bump following Semantic Versioning (PRO-STAN-001 v*X.Y.Z*).
