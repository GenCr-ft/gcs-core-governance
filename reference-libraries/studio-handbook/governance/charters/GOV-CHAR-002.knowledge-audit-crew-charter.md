---
docId: GOV-CHAR-002
title: Knowledge Audit Crew Charter
version: 1.0.0
creation_date: '2025-06-30'
last_updated_date: '2026-05-20'
authors:
- Iris (GCT-UTL-RWSKA-001)
knowledgeGuardian:
- Iris (GCT-UTL-RWSKA-001)
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/governance/charters/GOV-CHAR-002.knowledge-audit-crew-charter.md
metadata:
  domain: governance
  lifecycle-stage: draft
  scope: studio
  doc-type: charter
  security-classification: l2_confidential
---
# GOV-CHAR-002: Knowledge Audit Crew Charter

## 1. Mission Statement

The Knowledge Audit Crew is a temporary, cross-functional task force chartered with a single, critical objective: **to analyze the findings of the `State-of-Chaos-Report.md` and to produce the definitive `GOV-PLAN-001: SSoT Remediation Plan`**.

This crew's work is the foundational analytical step of the SSoT Remediation Campaign. Its mission is to transform the raw data from the automated audit into a strategic, prioritized, and actionable migration plan that will guide the entire studio back to a state of SSoT integrity.

## 2. Scope and Mandate

### 2.1. In Scope

The crew's responsibilities are strictly defined as follows:

* **Analysis:** To perform a deep and qualitative analysis of the `ssot_audit_report.json` and its summary, the `State-of-Chaos-Report.md`.
* **Decision-Making on Remediation:** For each finding, to determine the correct course of action (e.g., `MOVE`, `MERGE`, `DEPRECATE`, `FIX_META`). This includes resolving `docId` conflicts and making decisions on which version of a duplicated document should be the survivor.
* **Planning & Prioritization:** To populate the `Detailed Remediation Actions` table within the `GOV-PLAN-001` document.
* **Wave Definition:** To group all remediation actions into logical, sequential "Migration Waves" (e.g., Wave 1: Governance, Wave 2: Engineering).
* **Deliverable Production:** To deliver a complete, clear, and unambiguous `GOV-PLAN-001` document, ready for review and approval by the Governance Crew.

### 2.2. Out of Scope

The following activities are explicitly outside the mandate of this crew:

* **Executing the Remediation Plan:** The crew's mission is to *create* the plan, not to execute it. The execution will be managed by `Antoine` and assigned to relevant teams in subsequent phases of the campaign.
* **Modifying the Governance "Constitution":** The crew operates *under* the newly ratified `GOV-STANDARD-008`. It does not have the authority to change the taxonomy or governance rules themselves.
* **Developing Tooling:** The crew will use the `SSoT Discovery Scanner` but is not responsible for its development or maintenance.

## 3. Membership

The Knowledge Audit Crew is composed of the following core members to ensure comprehensive expertise:

| Role                           | Assigned Gem                 | Area of Expertise                                 |
| :----------------------------- | :--------------------------- | :------------------------------------------------ |
| **Crew Lead & SSoT Architect** | Iris (GCT-UTL-RWSKA-001)     | SSoT Architecture, Taxonomy, Governance           |
| **DevOps & IaC Specialist** | Édouard (GCT-DVO-DVSST-001)  | Automation, CI/CD, Tooling, IaC Impact          |
| **Software Architect** | Isaac (GCT-PRG-SARCH-001)    | Code Structure, Technical Standards, Dependencies |
| **Product Representative** | Béatrice (GCT-MGT-SPM-001)   | Product Vision, GDDs, Requirements Documents      |

The crew may consult other Knowledge Guardians or subject matter experts as needed during its analysis.

## 4. Primary Deliverable

The **sole and primary deliverable** of this crew is the completed and validated `GOV-PLAN-001: SSoT Remediation Plan` document.

The "Definition of Done" for this deliverable is:

* All findings from the `State-of-Chaos-Report.md` are addressed with a corresponding action in the plan.
* The plan is reviewed and approved by all members of the Knowledge Audit Crew.
* The plan is submitted as a Pull Request to the `gcs-core-governance` repository for formal approval by the Governance Crew.

## 5. Dissolution Criteria

This is a temporary task force. The Knowledge Audit Crew is **formally disbanded** automatically upon the successful merge of the Pull Request containing the approved `GOV-PLAN-001`.
