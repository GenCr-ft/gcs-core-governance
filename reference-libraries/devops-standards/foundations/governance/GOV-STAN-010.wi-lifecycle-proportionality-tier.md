---
docId: GOV-STAN-010
title: WI Lifecycle Proportionality Tier (wi:lightweight)
version: 1.0.0
date: '2026-08-05'
authors:
- Loig Allain (Studio Lead)
knowledgeGuardian:
- Orion (GEM-ORION)
reviewers:
- Isaac (GEM-ISAAC)
approvers:
- Studio Lead
ssot_path: gcs-core-governance/reference-libraries/devops-standards/foundations/governance/GOV-STAN-010.wi-lifecycle-proportionality-tier.md
metadata:
  lifecycle-stage: proposed
  scope: studio
  domain: governance
  doc-type: standard
  intended-audience:
  - contributors
  - ai-agents
  keywords:
  - wi-lifecycle
  - proportionality
  - lightweight
  - governance
  - gate
  security-classification: l2_confidential
---

# WI Lifecycle Proportionality Tier (`wi:lightweight`)

## 1. Purpose

The Work Item lifecycle (Refine → Design → Plan → Code) — with Gherkin acceptance
criteria, `[DESIGN]` and `[IMPL]` sub-issues, and two human `status:approved` gates — is
calibrated for substantive Work Items. For genuinely small, low-risk changes it is
disproportionate: the upstream ceremony costs more than the change it guards. This standard
defines a **proportionality tier**, `wi:lightweight`, that relaxes the *upstream* ceremony for
eligible Work Items while preserving the safety gates that earn their place.

Adopted by Studio Lead decision on gcs-project-management#526 (Option 5), under Initiative
gcs-project-management#525. This standard is the Single Source of Truth for tier eligibility;
its enforcement mechanism is specified in gcs-plt-gemop#348.

## 2. Scope

Applies to every GenCr@ft Work Item processed through the `wi-lifecycle` skill and the
`issue-context-gate` hook. It is a component of the canonical WI lifecycle contract
(`GOV-PROC-WI-001`); where that contract is authored later, this standard is incorporated by
reference.

## 3. The `wi:lightweight` tier

A Work Item carrying the `wi:lightweight` label, and touching **no** never-eligible surface
(§5), satisfies the REFINE gate with only:

- a non-empty `## Summary`, and
- a non-empty `## Acceptance Criteria`.

The following are **waived** for a lightweight WI: Gherkin (`Given/When/Then`) ACs, the
`## Testability Notes` section, and the `[DESIGN]` and `[IMPL]` sub-issues (and their two human
`status:approved` gates). The lifecycle stamp is still written.

The tier is the **normal path** for small work. `lifecycle:bypass` remains the true
break-glass (it skips *all* gates, including §4.1, and is reserved for exceptional cases).

## 4. Invariants (non-negotiable)

### 4.1 Adversary PR review is unconditional
The adversarial PR review in the CLOSE gate runs for **every** Work Item regardless of tier.
It is the highest-value gate — it catches defects that pass their own tests (e.g. the
clause-scoping bug caught on gcs-plt-gemop#345) — and is never waived by `wi:lightweight`.

### 4.2 The label is non-self-appliable
`wi:lightweight` MUST be applied by a human whose GitHub identity differs from the acting
agent. The `issue-context-gate` enforces this with the same setter ≠ actor check that guards
`lifecycle:bypass` and `status:approved`. An agent may never self-classify its own work as
lightweight.

### 4.3 Never-eligible surfaces override the label
If a Work Item touches any surface in §5, the `wi:lightweight` label is ignored and full
ceremony is required. Eligibility is a property of the *change*, not merely of the label.

## 5. Never-eligible surfaces (always full ceremony)

A Work Item that creates or modifies any of the following is **never** eligible for the tier,
regardless of size:

1. **Authentication & authorization** — identity, tokens, sessions, access control.
2. **Wire format / binary protocol** — any on-the-wire or serialization contract.
3. **Persistence & schema** — database schema, migrations, storage formats.
4. **Public API surface** — externally-consumed endpoints, SDK signatures, contracts.
5. **Security classification** — changes to a document's or asset's security tier.
6. **Blocking / enforcement hook behavior** — any hook that can deny a tool call
   (non-zero exit / hard block). *Advisory-only* hook changes (warn, exit 0) remain
   tier-eligible.
7. **Clean-architecture boundaries** — port/adapter definitions and hexagonal layer
   boundaries.

## 6. Eligible change classes (illustrative, non-exhaustive)

Subject to §5, the tier is appropriate for: documentation-only edits; comment/typo fixes;
test-only changes; a single additive configuration value or CLI flag; and dependency or
version bumps. When in doubt, a change is **not** lightweight — default to full ceremony.

## 7. Enforcement

| Concern | Mechanism | Location |
|---|---|---|
| Relaxed REFINE precondition | `wi-lifecycle` skill (REFINE phase) | gcs-plt-gemop |
| Label recognition, §5 exclusion, §4.2 actor check | `issue-context-gate.py` | gcs-plt-gemop |
| Unconditional adversary review (§4.1) | CLOSE gate (unchanged) | gcs-plt-gemop |

Implementation is tracked in gcs-plt-gemop#348.

## 8. Relationship to `lifecycle:bypass`

| | `wi:lightweight` (this standard) | `lifecycle:bypass` |
|---|---|---|
| Intent | Normal path for small, low-risk WIs | Exceptional break-glass |
| REFINE | Relaxed to Summary + ACs | Skipped entirely |
| Adversary PR review | **Runs** (§4.1) | May be skipped |
| Never-eligible surfaces (§5) | Enforced | Not enforced |
| Applied by | Human, non-self (§4.2) | Human, non-self |

## 9. Review & evolution

This standard is `proposed` pending Studio Lead approval (merge). After adoption, the
never-eligible list (§5) and eligible classes (§6) are reviewed after a pilot of the first
three lightweight Work Items; adjustments route through gcs-core-governance.
