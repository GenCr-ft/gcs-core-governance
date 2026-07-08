---
docId: GOV-STAN-009
title: PCG Roadmap Governance and Wave Rules
version: 1.0.0
authors:
- gencraft-workspace-orchestrator
- Orion (GCT-UTL-SLG-001)
knowledgeGuardian:
- Orion (GCT-UTL-SLG-001)
reviewers:
- Isaac (GCT-PRG-SARCH-001)
creation_date: '2026-07-08'
last_updated_date: '2026-07-08'
language: en
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/foundations/governance/GOV-STAN-009.pcg-roadmap-governance-and-wave-rules.md
metadata:
  scope: project-aethel
  domain: governance
  doc-type: standard
  lifecycle-stage: approved
  intended-audience:
  - project-leads
  - ai-agents
  - governance-crew
  - architects
  security-classification: l2_confidential
  keywords:
  - pcg
  - roadmap-governance
  - wave-rules
  - epic-template
  - feature-template
  - acceptance-criteria
  - taxonomy
---
# PCG Roadmap Governance and Wave Rules

## 1. Objective

This standard defines the governance rules for expanding Procedural Content
Generation (PCG) work **wave-by-wave**, and ratifies the canonical epic/feature
templates and acceptance-criteria (AC) rubric used to author and heal the PCG
work-item tree. It establishes when future PCG items become `[SPEC]`, `[DESIGN]`,
`[CODE]`, QA, or deferred work, and prevents broad PCG planning from decaying into
a batch of stale implementation issues.

This document is the terminal deliverable of the spike feature **PCG-FEAT-003**
([`GenCr-ft/gcp-aethel-backlog#770`](https://github.com/GenCr-ft/gcp-aethel-backlog/issues/770)),
a child of **PCG-EPIC-001**
([`GenCr-ft/gcp-aethel-backlog#753`](https://github.com/GenCr-ft/gcp-aethel-backlog/issues/753)),
under initiative **PCG-INIT-001**
([`GenCr-ft/gcs-project-management#359`](https://github.com/GenCr-ft/gcs-project-management/issues/359)).
It is also the ratified **template source** for the systematic PCG-healing effort.

### 1.1 Scope

**In scope:**

- Wave activation criteria for PCG epics — section [(a)](#a-wave-activation-checklist-objective).
- Valid outputs at each hierarchy level — section [(b)](#b-valid-outputs-per-hierarchy-level).
- Promotion of future PCG domains from PCG-INIT-002 into active planning — section [(c)](#c-pcg-init-002-to-active-promotion-gate).
- PCG-specific escalation triggers, referencing (not redefining) `gcs-plt-gemop`
  protocols — section [(d)](#d-escalation-triggers-pcg-specific).
- The ratified canonical EPIC/FEATURE templates, AC rubric, and taxonomy-tag rule
  — section [4](#4-ratified-canonical-templates).

**Out of scope:**

- Activating all future waves immediately.
- Creating implementation issues.
- Reprioritizing Phase 6 persistence/multiplayer work.
- Redefining studio-wide process owned by `gcs-plt-gemop`.

### 1.2 Relationship to existing SSoT

This standard governs PCG **roadmap mechanics**. It does not restate or supersede:

- [`GOV-STAN-001`](./GOV-STAN-001.ssot-document-naming-and-id-convention.md) — SSoT
  document naming and `docId` convention.
- [`GOV-STANDARD-008`](./GOV-STANDARD-008.ssot-master-taxonomy-and-governance.md) —
  SSoT master taxonomy and governance (the single source of truth for classification
  vocabularies).

The normative PCG **determinism/reproducibility contract** is governed by
`ENG-ADR-085` (see [Decision Record D1](#51-decision-record-d1--contract-ownership)),
with supporting specifications `ENG-SPEC-009` (PCG algorithm taxonomy), `ENG-SPEC-010`
(PCG authority matrix), and `ENG-SPEC-011` (PCG primitives contract) in
`GenCr-ft/gcp-aethel-architecture`. This standard references those artifacts but does
not redefine their content.

---

## 2. Roadmap Governance Rules

### (a) Wave activation checklist (objective)

An epic is **"activated"** only when ALL of the following are true:

- [ ] Parent initiative accepted.
- [ ] All upstream dependency epics/issues closed or explicitly waived.
- [ ] All authority-matrix rows for the epic's domains resolved (none `authority-missing`).
- [ ] Wave declared for the epic on
  [`GenCr-ft/gcs-project-management#359`](https://github.com/GenCr-ft/gcs-project-management/issues/359).

No `[CODE]` or `[IMPL]` child may be created for an epic until **every** box above
is ticked. Activation is per-epic and is recorded against the initiative wave state.

### (b) Valid outputs per hierarchy level

| Level | Valid output |
|---|---|
| Initiative | scope, child-epic map, wave state |
| Epic | scope, deps (up+down), child-feature links, artifact-anchored ACs, output artifact |
| Feature | spec/spike deliverable doc, artifact-anchored ACs, output artifact |
| User Story | `[SPEC]` / `[SPIKE]` refinement work item |
| Implementation | `[CODE]` work item (only after the epic's wave is activated) |

An output that does not match the row for its level is invalid and must be re-scoped
before the item advances.

### (c) PCG-INIT-002 to active promotion gate

A deferred PCG domain moves from **PCG-INIT-002**
([`GenCr-ft/gcs-project-management#360`](https://github.com/GenCr-ft/gcs-project-management/issues/360))
to **active** only via **all** of:

1. A `decision-advisor` brief.
2. An initiative wave declaration.
3. Authority-matrix rows seeded for the domain.

**No automatic promotion.** A domain remaining in PCG-INIT-002 without all three
artifacts stays deferred.

### (d) Escalation triggers (PCG-specific)

These triggers **reference, and do not redefine,** the `gcs-plt-gemop` protocols.

| Trigger | Route |
|---|---|
| Scope/architecture ambiguity | `questioning-inter-gem` / `questioning-user` |
| Game-design ambiguity | `decision-advisor` (never autonomous) |
| Wire-format / auth / persistence change | ADR + architecture veto |

---

## 3. Applying the Rules — Worked Example

To demonstrate rule (a) against a sample epic, consider **PCG-EPIC-002**
([`GenCr-ft/gcp-aethel-backlog#754`](https://github.com/GenCr-ft/gcp-aethel-backlog/issues/754)):

1. Parent initiative PCG-INIT-001 (#359) — accepted. ✔
2. Upstream dependency PCG-EPIC-001 (#753) governance contracts — resolved via the
   ratified templates in this document and `ENG-ADR-085`. ✔
3. Authority-matrix rows for the epic's domains — resolved by `ENG-SPEC-010` / the
   authority-matrix feature (`GenCr-ft/gcp-aethel-backlog#767`). ✔
4. Wave declared on #359. ✔

Only after all four boxes are ticked may `[CODE]` children be created — which is why
PCG-EPIC-002's implementation bricks (seed, noise, spatial, symbolic) were authored
as `[CODE]` work items **after** activation, not before.

---

## 4. Ratified Canonical Templates

The following templates and rubric are **ratified** and are the authoritative source
for authoring and healing every PCG epic and feature.

### 4.1 EPIC template

> **Goal** · **Product Increment** · **Repository** · **Scope** (in/out) ·
> **Dependencies** (upstream + downstream) · **Child Features** (live links) ·
> **Acceptance Criteria** (artifact-anchored) · **Output Artifact** (docId + path) ·
> **Authority/Review gate**.

### 4.2 FEATURE template

> **Description** · **Scope** · **Dependencies** · **Parent Epic** ·
> **Output Artifact** (docId + path) · **Acceptance Criteria** (artifact-anchored) ·
> **taxonomy tag**.

### 4.3 Acceptance-Criteria (AC) rubric

Every acceptance criterion MUST be **artifact-anchored** and follow this form:

```text
Given <state>
When <named artifact> is published
Then <objective property verifiable by inspection or CI>
```

An AC that cannot be verified by inspection or CI against a named, published artifact
does not satisfy the rubric and must be rewritten.

### 4.4 Taxonomy-tag rule (Decision D2)

Epic-tier children use `[FEATURE]` + the `feature` label **tree-wide**;
`[SPEC]` / `[CODE]` / `[SPIKE]` are reserved for the work-item tier **below** features.

**Recorded exception:** PCG-EPIC-001's governance children (including this spike,
PCG-FEAT-003 / #770) intentionally retain `[SPEC]` / `[SPIKE]`. This exception is
recorded here so the distinction is deliberate, not accidental. See
[Decision Record D2](#52-decision-record-d2--taxonomy-tag).

---

## 5. Decision Records

### 5.1 Decision Record D1 — Contract ownership

| Field | Value |
|---|---|
| **Decision ID** | D1 (PCG contract ownership) |
| **Question** | Which epic owns the PCG deterministic seed/PRNG/hashing/reproducibility contract? |
| **Status** | Decided — Closed |
| **Ruled on** | [`GenCr-ft/gcp-aethel-architecture#118`](https://github.com/GenCr-ft/gcp-aethel-architecture/issues/118) |
| **Authority** | Isaac (GCT-PRG-SARCH-001), architecture authority |
| **Outcome** | **Option 3 — Split** |

**Decision:** The PCG deterministic seed/PRNG/hashing/reproducibility contract is a
cross-cutting normative invariant. It is bound to an ADR — **`ENG-ADR-085`
(`ENG-ADR-085.pcg-determinism-contract.md`)** — which is the single source of truth
that the PCG authority matrix routes to.

- **PCG-EPIC-001** (#753) **owns and governs** the normative contract as a design
  contract (the ADR), via feature **PCG-FEAT-079**
  ([`GenCr-ft/gcp-aethel-backlog#862`](https://github.com/GenCr-ft/gcp-aethel-backlog/issues/862)).
- **PCG-EPIC-002** (#754) **implements** the primitive algorithms and **proves**
  conformance via the golden-vector fixtures that satisfy the contract.

**Rationale (transcribed from arch#118):** the contract simultaneously constrains
persistence regeneration, wire-format behaviour on the client/server boundary,
multiplayer authority consistency, and cross-language parity between the Rust/WASM
production path and the Python parity path. A contract of that authority class cannot
live inside an implementation epic (Option 1 understates it) nor inside a governance
epic without an architectural anchor (Option 2 gives it no supersession/veto trace).
Binding it to an ADR makes reproducibility a first-class, vetoable architecture
contract.

**Condition of record:** `ENG-ADR-085` must reach `Accepted` status before any
PCG primitive in #754 ships a golden vector that other repositories consume, so that
the conformance evidence always has a normative anchor.

### 5.2 Decision Record D2 — Taxonomy tag

| Field | Value |
|---|---|
| **Decision ID** | D2 (taxonomy tag) |
| **Question** | Which tag/label do epic-tier children carry, and where are `[SPEC]`/`[CODE]`/`[SPIKE]` valid? |
| **Status** | Decided — Ratified in PCG-FEAT-003 (#770) |
| **Authority** | PCG roadmap governance (this standard) |
| **Outcome** | Epic-tier children use `[FEATURE]` + `feature` label tree-wide |

**Decision:** Epic-tier children use `[FEATURE]` + the `feature` label tree-wide.
`[SPEC]` / `[CODE]` / `[SPIKE]` are reserved for the work-item tier below features.
PCG-EPIC-001's governance children intentionally retain `[SPEC]` / `[SPIKE]`, and this
exception is recorded (see [section 4.4](#44-taxonomy-tag-rule-decision-d2)) so the
distinction is deliberate.

---

## 6. Traceability

| Artifact | Reference |
|---|---|
| Spike feature (this doc's origin) | `GenCr-ft/gcp-aethel-backlog#770` (PCG-FEAT-003) |
| Parent epic | `GenCr-ft/gcp-aethel-backlog#753` (PCG-EPIC-001) |
| Implementation epic | `GenCr-ft/gcp-aethel-backlog#754` (PCG-EPIC-002) |
| Active initiative (roadmap boundary) | `GenCr-ft/gcs-project-management#359` (PCG-INIT-001) |
| Deferred initiative (roadmap boundary) | `GenCr-ft/gcs-project-management#360` (PCG-INIT-002) |
| D1 decision | `GenCr-ft/gcp-aethel-architecture#118` |
| Determinism contract | `ENG-ADR-085` (PCG-FEAT-079 / `GenCr-ft/gcp-aethel-backlog#862`) |
| PCG algorithm taxonomy | `ENG-SPEC-009` |
| PCG authority matrix | `ENG-SPEC-010` (`GenCr-ft/gcp-aethel-backlog#767`) |
| PCG primitives contract | `ENG-SPEC-011` |
