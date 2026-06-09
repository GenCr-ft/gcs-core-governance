---
docId: OPS-GUIDE-004
title: "S4: Architectural Review Process"
version: 1.0.0
authors:
  - Isaac (GCT-PRG-SARCH-001)
  - Isidore (GCT-PRG-GARCH-001)
creation_date: '2025-06-11'
last_updated_date: '2026-05-20'
language: en
metadata:
  scope: studio
  domain: governance
  doc-type: protocol
  lifecycle-stage: proposed
  security-classification: l1_internal
  intended-audience:
    - architects
    - governance-team
    - contributors
  keywords:
    - architectural-review
    - governance
    - adr
    - operational-protocols

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-004.s4-architectural-review-process.md
---

# S4: Architectural Review Process

## 4.0. Justification and Objectives

A formal, transparent, and traceable process for making significant architectural decisions is critical to ensure the technical quality, coherence, and long-term maintainability of Gencraft's systems. This protocol prevents architectural drift, reduces technical debt, and ensures that key technical choices are aligned with studio-wide strategies and constraints.

The objectives are to:

- Ensure architectural decisions are well-reasoned, reviewed by relevant experts, and formally approved.
- Document the context, rationale, and consequences of each significant decision in an immutable way.
- Provide a clear and predictable workflow for all Gems involved in proposing or being impacted by architectural changes.
- Support the KC&T principles of Traceability (Principle #4) and Quality of Information (Principle #3).

## 4.1. Guiding Principles

- **Evidence-Based Decisions:** Architectural choices must be supported by data, proof-of-concepts, trade-off analysis, or alignment with established best practices.
- **Transparency:** The entire lifecycle of a decision, from proposal to final outcome, is documented and visible to all relevant studio members.
- **Traceability (S7 Alignment):** Every approved decision results in an Architecture Decision Record (ADR), creating an auditable trail.
- **Clear Accountability:** The author, reviewers, and the final approver for each decision are explicitly identified.

## 4.2. Scope: When to Use This Process

This protocol **must** be initiated when a "significant architectural decision" is required. A decision is considered significant if it meets one or more of the following criteria:

- Introduction of a new technology, framework, Core Studio Service, or major library.
- A change to a public API or contract of a shared library (`gcl-`) or Core Studio Service.
- A decision with a significant impact on Non-Functional Requirements (NFRs) like security, performance, scalability, or cost.
- A decision that is difficult or costly to reverse.
- A choice that establishes a new architectural pattern or standard for the studio or a specific game project.

This process is not required for minor, localized implementation choices that do not affect other systems or teams.

## 4.3. The ADR as the Central Artifact

The **Architecture Decision Record (ADR)** is the central and sole SSoT artifact for documenting a decision made under this protocol.

- All ADRs **must** use the official template: `gcs-core-governance/02-knowledge-base-hub/templates/document-templates/adr-template.md`.
- ADRs **must** be stored in the Git repository relevant to their scope:
  - Platform ADRs in `gcs-plt-architecture/adrs/`.
  - Game ADRs (Aethel) in `gcp-aethel-architecture/adrs/`.

## 4.4. The Architectural Review Workflow

The lifecycle of an architectural decision follows these steps, visualized below.

```mermaid
graph TD
    A[Idea / Architectural Problem] --> B(Step 0: Socialization);
    B --> C[Step 1: Draft ADR<br>(Status: Proposed)];
    C --> D[Submit Pull Request];
    D --> E[Step 2: Asynchronous Review<br>(PR Comments)];
    E --> F{Sync Meeting Needed?};
    F -- Yes --> G[Step 3: Review Meeting];
    G --> H[Step 4: Final Decision];
    F -- No --> H;
    E --> H;
    H -- Approved --> I[Merge PR & Update ADR Status];
    I --> K[Step 5: Communication (S14)];
    H -- Rejected --> J[Close PR & Update ADR Status];
```

### Step 0: Socialization (Optional but Recommended)

Before formalizing a proposal, the authoring architect (`Isaac` or `Isidore`) is encouraged to discuss the problem and potential solutions informally with key stakeholders to gather initial feedback and build consensus.

### Step 1: Proposal & Draft ADR

The responsible architect (`Isaac` or `Isidore`) identifies the need for a decision. They create a new ADR document with the status "Proposed" and submit it via a **Pull Request (PR)** in the relevant architecture repository. The PR description summarizes the problem and the proposed solution.

### Step 2: Asynchronous Review

The PR is assigned to the relevant reviewers (e.g., technical leads, security, DevOps, design). Reviewers provide feedback, ask questions, and suggest alternatives directly in the PR comments.

- **Timeframe Guideline:** To avoid blocking projects, reviewers should provide feedback within a reasonable timeframe (e.g., 3-5 studio days).

### Step 3: Review Meeting (Optional)

If the discussion becomes complex or requires real-time debate, the author may call a synchronous review meeting with key stakeholders. The meeting's summary and conclusions **must** be posted back to the PR.

### Step 4: Decision & Approval

Based on the feedback, the author may update the ADR. The final decision is made by the designated approver.

- **Approval:** The approver formally approves the PR.
- **Rejection:** The approver closes the PR with a clear comment explaining the rationale for rejection. The ADR status is updated to "Rejected".

### Step 5: Integration and Communication

- Upon approval, the PR is merged. The author **must** perform a final commit to update the ADR's YAML frontmatter:
  - Set `status` to "Approved".
  - Set `date` to the current date.
  - Add a link to the merged PR in a `resolution_pr` field.
- The decision is communicated to impacted teams as per Protocol S14.

## 4.5. Roles and Responsibilities

- **Author:** The architect responsible for the domain (`Isaac` for Platform, `Isidore` for Game).
- **Reviewers:** Key experts from different departments whose domains are impacted by the decision. Their list is defined in the ADR's frontmatter.
- **Approver:**
  - For decisions within a single domain: The authoring architect (`Isaac` or `Isidore`).
  - For decisions with studio-wide strategic impact, high cost, or that resolve a conflict between architects: The **`Governance Crew`**.

## 4.6. Impact and Tooling for AI Gems

- **Consulting ADRs:** All Gems, especially those in development and design roles, must be able to query and understand approved ADRs via their `KnowledgeBaseSearchTool`. The structured format of ADRs facilitates this.
- **Proposing ADRs:** While primary authorship rests with `Isaac` and `Isidore`, other expert Gems may be tasked with preparing the initial draft of an ADR using a `Tool` that leverages the `adr-template.md`.
- **Traceability for `Véra`:** The structured process and the requirement to update the ADR status post-merge create a closed-loop system that `Véra` can audit to track the lifecycle of every architectural decision.
