---
docId: OPS-GUIDE-013
title: S13 Global Protocol Evolution
version: 1.0.0
authors:
- AI Compliance Agent
creation_date: '2025-05-26'
last_updated_date: '2026-05-20'
language: en
metadata:
  scope: studio
  domain: governance
  doc-type: protocol
  lifecycle-stage: approved
  security-classification: l1_internal
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  keywords:
  - protocol-evolution
  - gops
  - adaptability
  - continuous-improvement
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-013.s13-global-protocol-evolution.md
---
# S13: Global Protocol Evolution Protocol

## 13.0. Justification and Objectives

This protocol establishes the formal, transparent, and traceable process for proposing, reviewing, approving, and implementing significant changes to Gencraft's Global Operational Protocols (GOPs) and other foundational SSoT documents. It ensures the studio's operational framework remains adaptive, efficient, and aligned with its strategic goals, while managing change in a controlled manner.

## 13.1. Key Definitions

- **Global Operational Protocol (GOP):** Any protocol in the `01-operational-protocols/` directory or a foundational document in `00-studio-vision-and-principles/`.
- **Proposal for Global Evolution (PGE):** A formal suggestion, tracked via a GitHub Issue, to create, significantly amend, or deprecate a GOP.
- **`Governance Crew`:** The designated body responsible for reviewing and deciding on PGEs. Its mandate is defined in the `governance-crew-charter.md`.

## 13.2. Triggers for a Proposal for Global Evolution (PGE)

A PGE is required for any significant change to a GOP. Triggers include, but are not limited to:

- A successful Crew-Specific Protocol (CSP) identified for studio-wide adoption, formally recommended by the **`CrewOps Arbitrator` (`Antoine`)**.
- Systemic inefficiencies or risks identified by `Véra`.
- Strategic recommendations from `Iris`.
- Action items from a Post-Mortem (S5).
- A directive from Studio Leadership (S7).

## 13.3. The Global Evolution Workflow

The entire process is tracked via GitHub Issues in the `gcs-core-governance` repository.

```mermaid
graph TD
    subgraph "Phase 1: Proposition"
        A[Déclenchement du Besoin<br>(ex: Leçon Apprise S5, CSP à globaliser S12)] --> B[Step 1: Création d'une Issue PGE<br>Template: protocol-change-proposal.md<br>Status: pending-review];
    end

    subgraph "Phase 2: Revue & Décision par le Governance Crew"
        B --> C{Step 2: Revue Initiale};
        C -- Analyse d'Impact Requise --> D[Demande aux Experts<br>(Isaac, Isidore, Véra...)];
        D --> E[Réception des Analyses];
        E --> C;
        C -- Prêt pour Décision --> F[Step 3: Décision Formelle];
    end

    subgraph "Phase 3: Implémentation & Clôture"
        F -- Approuvé --> G[Mise à jour du statut de l'Issue<br>status: approved];
        G --> H[Step 4: Création de la Pull Request<br>pour modifier le SSoT];
        H --> I[Revue & Merge de la PR];
        I --> J[Step 5: Communication (S14)<br>& Création d'Issues de suivi<br>(ex: MàJ des Blueprints)];
        J --> L([Clôture Finale]);

        F -- Rejeté/Différé --> K[Mise à jour du statut de l'Issue<br>status: rejected/deferred];
        K --> L;
    end
```

### Step 1: Proposal Submission (PGE)

- **Action:** The initiating Gem (via their Lead) creates a GitHub Issue using the `protocol-change-proposal-template.md`.
- **Content Note:** The "Potential Impact Analysis" required by the template is understood to be a **preliminary assessment**. A deeper analysis will be requested by the Governance Crew as needed.
- **Labels:** The Issue **must** be labeled `type:protocol-change` and `status:pending-review`.

### Step 2: Review by the `Governance Crew`

- **Action:** The Issue is assigned to the `Governance Crew`. The status is changed to `status:under-review`.
- **Process:** The `Governance Crew` reviews the proposal. They may form a **working group** with the proposer to refine complex ideas. For any non-trivial change, they **must** request a formal impact analysis from relevant experts:
  - `Isaac` (Platform Architect) for platform impacts.
  - `Isidore` (Game Architect) for game impacts.
  - `Véra` (Quality Analyst) for impacts on Gem performance and monitoring.
  - `Henri` (Legal Counsel) for legal or compliance impacts.
- All analysis and discussion are documented in the Issue comments.

### Step 3: Formal Decision

- **Action:** The `Governance Crew` makes a decision based on the proposal and the impact analyses.
- **Decision Options:** `Approved`, `Approved with Revisions`, `Rejected`, `Deferred`.
- **Traceability (S7 Alignment):** The final decision and its rationale **must** be logged in a structured comment within the Issue, following the `decision-record-template.md` format. The status label is updated accordingly (e.g., `status:approved`).

### Step 4: Implementation

- **Action:** If approved, a Pull Request is created to modify the relevant SSoT document(s).
- **Linkage:** The PR description **must** link to the approval Issue.
- **Review & Merge:** The PR is reviewed by the `Governance Crew` or designated Knowledge Guardians and merged upon final approval. The original Issue is then closed.

## 13.4. Communication and SSoT Integration

- **Communication (S14):** The approved change **must** be communicated to all relevant Gems and human personnel.
- **AI Gem Blueprint Updates:** If the change impacts Gem behavior, a new Issue **must** be created in the `gcs-plt-gembp` repository to track the necessary updates to Gem Blueprints. This is a critical step to ensure the AI workforce adapts correctly.
- **`Véra`'s Audit Baseline:** `Véra` is automatically notified of the change to update her audit and compliance-checking baselines.

## 13.5. Impact and Tooling for AI Gems

- **Proposing Changes:** Gems can use a `ProposeProtocolChangeTool` that utilizes the `protocol-change-proposal-template.md`.
- **Expert Analysis:** Expert Gems (`Isaac`, `Véra`, etc.) must have `Tools` to perform their impact analyses and report the findings in a structured format.
- **Awareness:** All Gems must be able to query the latest versions of protocols via their `KnowledgeBaseSearchTool`. `Gemma` must consult the latest protocols when instantiating new Gems.
- **Process Tracking:** The use of standardized labels (`status:pending-review`, `status:under-review`, etc.) allows Gems like `Véra` and `Antoine` to programmatically track the progress and efficiency of the governance process.
