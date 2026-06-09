---
docId: GOV-PLAN-001
title: SSoT Remediation Plan
version: 1.1.0
date: '2025-07-01'
authors:
- Knowledge Audit Crew
knowledgeGuardian:
- Iris (GCT-UTL-RWSKA-001)
reviewers:
- Governance Crew
approvers:
- Governance Crew
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/records/plans/GOV-PLAN-001.ssot-remediation-plan.md
metadata:
  artifact-class: Knowledge
  domain: Governance
  classification:
    category: To Plan
    type: Roadmap
  lifecycle-stage: Design
  provenance:
    source: manual
    authors:
      - "Iris (GCT-UTL-RWSKA-001)"
---
# GOV-PLAN-001: SSoT Remediation Plan

## 1. Executive Summary

This document is the master plan for the Gencraft Studio SSoT Remediation Campaign. It translates the 1,310 findings from the `State-of-Chaos-Report.md` into a complete, prioritized, and actionable set of tasks. Its purpose is to guide the systematic migration of all studio artifacts to full compliance with the `GOV-STANDARD-008: SSoT Master Taxonomy and Governance Standard`.

The execution of this plan is mandatory and will be tracked by the studio's production management.

## 2. Guiding Principles

The remediation will be executed according to the following principles:

* **Data-Driven:** Every action corresponds to a finding from the `ssot_audit_report.json`.
* **Phased Approach:** Actions are grouped into logical "Migration Waves" to manage complexity.
* **Automated Validation:** All changes submitted as part of this plan MUST pass the `ssot-linter`.
* **Traceability:** Every action will be tracked via a dedicated GitHub Issue.

## 3. Migration Waves

The remediation is structured into the following sequential waves:

* **Wave 1: Constitutional Crisis.** Address all critical `docId` duplicates. This must be done first to restore a baseline of trust in our identification system.
* **Wave 2: Governance Foundation.** Remediate all artifacts in the `Governance` domain, including the old standards that need to be formally deprecated.
* **Wave 3: Technical Foundation.** Remediate `Engineering` and `DevOps` domains.
* **Wave 4: Creative & Product Foundation.** Remediate `Product & Game Design`, `Art`, and `Audio` domains.
* **Wave 5: Business & Support Foundation.** Remediate all remaining domains (`Finance`, `Legal`, etc.).
* **Wave 6: Final Audit.** Rerun the `SSoT Discovery Scanner` to ensure zero findings remain.

## 4. Detailed Remediation Actions

This table is the master checklist for the remediation effort.

### Wave 1: Constitutional Crisis (`docId` Duplicates)

| Action ID | Source Path 1 | Source Path 2 | Action Type | Assigned To | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **REM-001** | `ENG-STANDARD-003.ai-tool-development-standards.md` | `ENG-STANDARD-003.crewai-workflows-repository-standard.md` | **MERGE** | `GCT-PRG-SARCH-001` | `To Do` |
| **REM-002** | `gcp-aethel-architecture/adrs/ENG-ADR-001.0002...` | `gcp-aethel-docs-req/decisions/ENG-ADR-001.decision-001.md` | **MERGE** | `GCT-PRG-SARCH-001` | `To Do` |
| **REM-003** | `gcp-aethel-architecture/ENG-SPEC-001...` | `gcp-aethel-architecture/c4/level-2-containers/ENG-SPEC-001...` | **MERGE** | `GCT-PRG-SARCH-001` | `To Do` |
| *... (etc. for all duplicates)* | | | | | |

### Wave 2: Governance Foundation

| Action ID | Source Path | Target Path | Action Type | Assigned To | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **REM-050** | `gcs-core-governance/foundations/governance/GOV-STAN-001...md` | `gcs-core-governance/records/deprecated/GOV-STAN-001...md` | **DEPRECATE** | `GCT-UTL-RWSKA-001` | `To Do` |
| **REM-051** | `gcs-core-governance/foundations/governance/GOV-REFE-002...md` | `gcs-core-governance/records/deprecated/GOV-REFE-002...md` | **DEPRECATE** | `GCT-UTL-RWSKA-001` | `To Do` |
| **REM-052** | `gcs-core-governance/01-operational-protocols/OPS-GUIDE-001.s1-feedback-approval.md` | `gcs-core-governance/01-operational-protocols/GOV-PROT-001.s1-feedback-approval.md` | **MOVE/FIX_META** | `GCT-MGT-PPM-001` | `To Do` |
| **REM-053**| `gcs-core-governance/00-studio-vision-and-principles/GOV-POLICY-001.code-of-conduct.md` | - | **FIX_META** | `Governance Crew` | `To Do` |
| *... (etc. for all governance files)* | | | | | |

### Wave 3: Technical Foundation

| Action ID | Source Path | Target Path | Action Type | Assigned To | Status |
| :--- | :--- | :--- | :--- | :--- | :--- |
| **REM-200** | `gcs-core-governance/domains/engineering/standards/DEV-STAN-005.script-001-general-scripting-standard.md` | `gcs-core-governance/domains/engineering/standards/ENG-STAN-005.general-scripting-standard.md` | **MOVE/FIX_META** | `GCT-DVO-DVSST-001` | `To Do` |
| *... (etc.)* | | | | | |

## 5. Rollback Plan

In the event of a critical failure during a migration wave, the primary rollback mechanism will be to revert the associated Pull Requests. Given the "baseline" tags created in Step 1, a full repository state restoration is possible but should only be considered in extreme circumstances, upon approval by the Governance Crew.
