---
docId: OPS-GUIDE-002
title: "S2: Disagreement, Escalation, and Resolution Protocol"
version: 1.2
authors:
  - Governance Crew
  - Assistant Gem
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)
creation_date: '2025-06-11'
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
    - protocol
    - s2
    - governance
    - conflict-resolution
    - escalation

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-002.s2-disagreement-escalation.md
---

# S2: Disagreement, Escalation, and Resolution Protocol

## 2.0. Justification and Objectives

Disagreements are natural and often beneficial in complex, creative projects. This protocol provides a structured, fair, and transparent process to manage and resolve them, ensuring they lead to robust solutions rather than stagnation. Its objectives are to encourage constructive debate, ensure timely resolution, and provide clear escalation paths while maintaining a collaborative environment and full traceability.

## 2.1. Core Principles Guiding Disagreement Management

- **Resolve at the Lowest Possible Level:** Encourage direct discussion and resolution first.
- **Focus on Project Goals:** Frame arguments around what is best for the project and the studio.
- **Evidence-Based Discussion:** Support viewpoints with data and references to the SSoT.
- **Respectful Communication:** Adhere strictly to the `code-of-conduct.md`.
- **Clear Ownership of Decision:** At each stage, the decision-making authority must be unambiguous.

## 2.2. Escalation Steps

This tiered process is the SSoT for managing disagreements. All significant steps and decisions **must** be documented in a dedicated GitHub Issue using the `disagreement-formalization-template.md`.

### Step 1: Direct Discussion & Documented Resolution Attempt

- **Trigger:** A substantive disagreement is identified between two or more Gems.
- **Process:** The involved parties **must** first attempt direct, professional discussion. If unresolved, a GitHub Issue **must** be created to formally document the context and arguments.
- **Timeframe Guideline:** This stage should ideally not exceed 1-2 studio days.

### Step 2: Lead Mediation/Decision

- **Trigger:** No consensus reached in Step 1, or a task is critically blocked.
- **Process:** The Issue is escalated to the relevant team Lead(s). The Lead reviews the arguments and facilitates a decision.
- **Note on CSPs:** For disagreements related specifically to a Crew-Specific Protocol (CSP) as per S12, the designated **`CrewOps Arbitrator`** (`Antoine`) acts as the primary mediator at this stage.
- **Timeframe Guideline:** This stage should ideally not exceed 2 studio days.

### Step 3: Architectural Arbitration

- **Trigger:** The disagreement is of a significant technical or architectural nature and was not resolved at Step 2.
- **Process:** The Issue is escalated to the architect with the relevant purview:
    1. For disagreements concerning **game-specific architecture**: Escalate to the **`Game Architect` (`Isidore`)**.
    2. For disagreements concerning **studio platform architecture**: Escalate to the **`Platform Architect` (`Isaac`)**.
- If both architects are concerned and cannot reach a consensus, the issue is escalated to Step 4.
- **Timeframe Guideline:** This stage should ideally not exceed 2 studio days.

### Step 4: Production Arbitration

- **Trigger:** An issue remains unresolved after architectural review, or a non-architectural issue has a major impact on project scope, schedule, or resources.
- **Process:** The Issue is escalated to the **`Producer` (`Antoine`)** and/or the **`Product Manager` (`Béatrice`)**. They review the case from a project and product strategy perspective and make a binding decision.

### Step 5: Governance Crew Arbitration

- **Trigger:** A disagreement is systemic, relates to the interpretation or inadequacy of a Global Operational Protocol (GOP), or could not be resolved at the production level.
- **Process:** The Issue is formally escalated to the **`Governance Crew`**. The Crew's decision is final for internal studio governance. An outcome of this arbitration may be the initiation of a Proposal for Global Evolution (PGE) under Protocol S13.

### Step 6: Lug Consultation (Ultimate Escalation)

- **Trigger:** The `Governance Crew` or Studio Leadership determines that a decision carries extreme strategic risk or would fundamentally alter the studio's vision.
- **Process:** The matter is presented to Lug for a final directive, following the process outlined in Protocol S7.4.

## 2.3. Traceability (GitHub as SSoT)

All disagreements are tracked in a dedicated GitHub Issue. The issue's history, comments, and labels serve as the immutable SSoT for the entire process.

## 2.4. Distinguishing Legitimate Disagreement from Gem Malfunction

- **Trigger:** If any party in a disagreement suspects that a Gem's contribution is based on illogical reasoning or erratic behavior, they **must** flag it.
- **Process:**
    1. The GitHub Issue is labeled `flag:vera-review-needed`.
    2. This label **must** trigger an automatic notification to `Véra (Gem Performance & Quality Analyst)` with a structured payload containing: the GemID in question, the link to the Issue, and the specific comments or actions that triggered the flag.
    3. `Véra` will conduct an independent analysis in parallel. If a malfunction is confirmed, the Issue is reclassified as a `type:agent-quality-incident`, and the disagreement process is paused pending resolution.

## 2.5. Impact on AI Gems and Necessary `Tools`

AI Gems must be equipped with the logic and `Tools` to navigate this protocol. This includes:

- **Documentation `Tools`:** To create and comment on GitHub Issues using the correct templates.
- **Escalation `Tools`:** To change issue labels and assign the issue to the correct next step in the escalation path (e.g., Lead, `Isaac`, `Isidore`, `Governance Crew`). A `RouteDisagreementTool` should be developed to assist in choosing the correct target.
- **Notification `Tools`:** A `Tool` to formally notify `Véra` with a structured payload when a Gem's behavior is questioned.
- **Decision-Parsing Logic:** Gems must be able to parse and understand the structured decision comments logged at each stage to adapt their actions accordingly.

## 2.6. Communication of Final Resolution

For fairness and process completion, the final decision and its core rationale, once logged in the GitHub Issue by the final arbiter, **must** be clearly communicated back to all parties originally involved in the disagreement. Closing the issue with the decision comment serves as this formal notification.
