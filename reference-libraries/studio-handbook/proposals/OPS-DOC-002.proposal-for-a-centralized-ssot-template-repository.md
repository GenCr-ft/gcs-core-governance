---
docId: OPS-DOC-002
title: Proposal for a Centralized SSoT Template Repository
version: 1.0.0
creation_date: '2025-06-16'
last_updated_date: '2026-05-20'
authors:
- "B\xE9atrice (GCT-MGT-SPM-001)"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/proposals/OPS-DOC-002.proposal-for-a-centralized-ssot-template-repository.md
metadata:
  lifecycle-stage: approved
  keywords:
  - templates
  - ssot
  - tooling
  - gft-cli
  - governance
  - adr-pending
  scope: studio
  domain: production-management
  doc-type: protocol-change
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)
---
# Proposal: Centralized SSoT Template Repository

## 1. Summary

This document proposes the creation of a new, dedicated repository: `gct-ssot-templates`. This repository will serve as the Single Source of Truth (SSoT) for all document and issue templates used across Gencraft Studio. It aims to replace the current, decentralized storage of templates within the `gcs-core-governance`.

## 2. Justification

The current practice of storing templates inside the `gcs-core-governance` is suboptimal. A dedicated repository provides significant advantages:

- **Clarity & Centralization:** A single, discoverable location for all templates simplifies maintenance and usage for all Gems.
- **Tooling Optimization:** It provides a stable, predictable target for our `gft-cli` tool, simplifying its configuration and enhancing its reliability when scaffolding new documents.
- **Decoupled Versioning:** Templates can be versioned and updated independently of the handbook's content, allowing for more agile iteration on our tooling and standards.
- **Focused Governance:** We can establish specific ownership and contribution rules for templates, managed by designated Knowledge Guardians like `Iris`.

## 3. Final Proposed Directory Structure (Consolidated)

Based on a collaborative review by all studio stakeholders, the following structure is proposed to meet the needs of every department:

```bash
gct-ssot-templates/
├── .github/
├── docs/
│   ├── engineering/
│   │   ├── adr-template.md
│   │   ├── api-specification-template.md
│   │   └── technical-design-document-template.md
│   ├── game-design/
│   │   ├── gdd-section-template.md
│   │   └── narrative-beat-template.md
│   ├── governance/
│   │   ├── meeting-notes-template.md
│   │   ├── protocol-standard-template.md
│   │   └── weekly-progress-report-template.md
│   ├── legal/
│   │   ├── contract-summary-template.md
│   │   └── nda-template.md
│   ├── marketing/
│   │   ├── marketing-campaign-brief-template.md
│   │   └── press-release-template.md
│   ├── operations/
│   │   ├── deployment-plan-template.md
│   │   └── service-level-agreement-template.md
│   ├── requirements/
│   │   ├── epic-template.md
│   │   ├── feature-template.md
│   │   ├── product-brief-template.md
│   │   └── user-story-template.md
│   └── ux-research/
│       └── user-interview-template.md
├── issues/
│   ├── bug-report-template.md
│   ├── communication-request-template.md
│   ├── feature-request-template.md
│   ├── knowledge-proposal-template.md
│   ├── protocol-change-proposal-template.md
│   ├── task-template.md
│   ├── template-request-template.md
│   └── tool-request-template.md
├── prs/
│   └── pull-request-template.md
├── qa/
│   ├── post-mortem-report-template.md
│   ├── test-case-template.md
│   └── test-plan-template.md
├── METATEMPLATE.md
└── README.md
```

## 4. `gft-cli` Integration

The `gft-cli` tool will be updated to use this repository as its primary source for all template-related commands. The command structure will map directly to the directory structure (e.g., `gft-cli new requirement --type=feature`). It will also include a new command: `gft-cli new request --type=template`.

## 5. Migration and Action Plan

1. **Approve Decision:** The `Governance Crew` must formally approve this proposal.
2. **Formalize Decision:** Create an Architecture Decision Record (ADR) in `gcs-plt-architecture` to document this change to the SSoT structure.
3. **Create Epic:** Create a tracking Epic in our project management system.
4. **Execute Tasks:**
    - **`Édouard`:** Create the `gct-ssot-templates` repository with the approved structure.
    - **`Iris`:** Lead the migration of existing templates from `gcs-core-governance` to the new repository and create the `METATEMPLATE.md` guide.
    - **All `Knowledge Guardians`:** Create the new placeholder templates for their respective domains.
    - **`Camille`:** Update the `gft-cli` tool to point to the new SSoT.
5. **Communicate:** Announce the change and the new `gft-cli` version to all studio members.

## 6. Governance

- **Knowledge Guardian:** The primary KG for this repository will be `Iris (GCT-UTL-RWSKA-001)`, with oversight from the `Governance Crew`.
- **Contribution:** All changes to templates MUST follow Protocol S1 (PR review) and be reviewed by the designated guardians.

---
