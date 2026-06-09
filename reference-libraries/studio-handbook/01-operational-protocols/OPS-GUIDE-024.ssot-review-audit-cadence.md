---
docId: OPS-GUIDE-024
title: "SSoT Review & Audit Cadence"
version: 1.0.0
authors:
  - gencraft-workspace-orchestrator
creation_date: '2026-06-06'
last_updated_date: '2026-06-06'
language: en
summary: "Schedule and process for the regular review and audit of the Single Source of Truth documentation."
metadata:
  lifecycle-stage: approved
  scope: studio-wide
  domain: governance
  doc-type: guide
  security-classification: l2_confidential
  keywords:
    - ssot
    - audit
    - governance
    - compliance

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-024.ssot-review-audit-cadence.md
---

# OPS-GUIDE-024: SSoT Review & Audit Cadence

**Date**: 2026-06-06
**Status**: Active

## 1. Purpose
To ensure that the Studio's Single Source of Truth (SSoT) remains accurate, compliant with formatting standards, and free of outdated or contradictory information, a regular audit cadence must be strictly followed.

## 2. Responsibilities
- **Knowledge Guardian**: Responsible for leading the audit, executing SSoT tooling (`gcd-ops-scripts`), and compiling the report.
- **Governance Crew**: Responsible for reviewing the audit report and enforcing remediation across teams.
- **Domain Leads**: Responsible for remediating issues identified in their respective domains within 7 days of the audit report.

## 3. Cadence
The SSoT audit is conducted **Quarterly** (every 3 months), during the final week of the quarter.
- **Q1 Audit**: End of March
- **Q2 Audit**: End of June
- **Q3 Audit**: End of September
- **Q4 Audit**: End of December

## 4. Audit Process
1. **Automated Sweep**: The Knowledge Guardian runs all pre-commit hooks and SSoT validation scripts (`metadata-linter`, `link-linter`, `naming-linter`) across all active repositories.
2. **Manual Review**: A sample of high-impact architecture (ADRs) and game design specifications are reviewed for logical drift or contradictions.
3. **Report Generation**: The Knowledge Guardian drafts an Audit Report (using the standard reporting template) and posts it as a Studio-wide GitHub Issue.
4. **Remediation**: Action items are extracted into the `PRO-REPO-002` master action tracker and assigned to Domain Leads for completion.

## 5. Links
- PROJ-099
