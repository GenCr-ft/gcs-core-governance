---
docId: DEV-PROT-002
title: Ops 001 Iac Scan Exception Log Standard
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This document outlines the standard for requesting, approving, and logging
  exceptions to findings from Infrastructure as Code (IaC) security scanning tools.
  It defines criteria for exceptions (false positives, accepted risk, temporary fixes,
  or tool limitations) and establishes a centralized, version-controlled log for tracking
  all approved deviations, ensuring auditability and risk mitigation.
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - iac-scanning
  - exception-management
  - security-standards
  - compliance
  - risk-management
  - governance
  scope: studio
  domain: devops
  doc-type: protocol
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/operations/guides/DEV-PROT-002.ops-001-iac-scan-exception-log-standard.md
---
**Author(s):** `Adam` (Gem AA - DevOps Team Lead)
**Initial Reviewers:** `Cerberus` (Security Officer Gem), `Isaac` (Gem SARCH - Software Architect), `Édouard` (Gem AD - DevOps Strategy Specialist), `Benjamin` (Gem AC - Infrastructure Specialist)
**Final Approvers:** `Adam` (Gem AA - DevOps Team Lead), `Cerberus` (Security Officer Gem), `Isaac` (Gem SARCH - Software Architect), `Édouard` (Gem AD - DevOps Strategy Specialist)
**Knowledge Guardian(s):** `Adam` (Gem AA - DevOps Team Lead), `Cerberus` (Security Officer Gem)
**Related Documents:**

- `iac-007-iac-static-analysis-standard.md`
  _`sec-001-secrets-management-standard.md`
  _ `s1-feedback-approval.md` (Studio Protocol for PRs)
  _`s7-key-decisions-traceability.md` (Studio Protocol for Key Decisions)
  _ `s19-action-item-management-protocol.md`
  _`information-classification-and-handling-policy.md`
  _ `access-control-policy.md`
  \_ `gh-001.1-branching-strategy-and-protection.md` \* Template d'Issue "IaC Scan Exception Request" (À créer dans `gencraft-operations/.github/ISSUE_TEMPLATE/`)

---

## 1. Objective

This standard defines the mandatory guidelines for requesting, approving, logging, and reviewing exceptions to findings identified by Infrastructure as Code (IaC) security and compliance scanning tools (e.g., TFSec, Checkov, as mandated by `iac-007-iac-static-analysis-standard.md`).

The objectives are to:

- Ensure that any deviation from IaC security and compliance best practices is a deliberate, justified, and time-bound decision.
- Maintain a clear audit trail of all approved exceptions.
- Facilitate regular review of active exceptions to minimize risk exposure and maintain architectural coherence.
- Provide a consistent process for all Gencraft Gems and human contributors.
- Ensure that the exception process itself is secure and adheres to the Principle of Least Privilege.
- Provide metrics and data for the continuous improvement of our IaC practices and security posture.

## 2. Scope

This standard applies to:

- All IaC scanning tools used within Gencraft.
- All Gencraft repositories containing IaC (e.g., `gencraft-studio-iac`, `gencraft-game-aethel-iac`, and any future IaC repositories).
- All Gencraft Gems (human or AI) involved in the development, review, deployment, or security oversight of IaC.

This standard does NOT cover exceptions for application code scanning or other non-IaC security findings, which are managed by their respective processes.

## 3. Standard

### 3.1. Exception Criteria

An exception to an IaC scan finding may be considered ONLY under the following circumstances:

- **False Positive (`FALSE_POSITIVE`):** The finding is confirmed by `Cerberus` (Security Officer Gem) and relevant technical specialists (e.g., `Benjamin` - IaC Specialist, `Isaac` - Architect, or a relevant Tech Lead) to be a false positive from the scanning tool. The configuration MUST be deemed secure and compliant despite the tool's finding. Justification MUST include detailed analysis and evidence (e.g., link to PR comment, tool documentation). If possible, the scan tool configuration should be improved to globally ignore validated false positives.
- **Accepted Risk with Documented Mitigating Controls (`ACCEPTED_RISK`):** The risk introduced by the finding is understood and formally accepted by the designated approvers (see 3.4). This acceptance MUST be based on a documented risk assessment (considering impact x probability, aligned with `information-classification-and-handling-policy.md`). Specific, documented, and verifiable mitigating controls MUST be in place that reduce the residual risk to an acceptable level. The justification MUST clearly articulate why the standard fix cannot be applied and how the mitigating controls are effective and maintained.
- **Temporary Exception with Approved Remediation Plan (`TEMPORARY_FIX`):** A standard fix is not immediately feasible due to urgent operational needs or overriding technical constraints, AND a detailed, technically viable, and time-bound remediation plan has been approved by the relevant technical authorities (e.g., Tech Lead, `Isaac`) and `Cerberus`. This type of exception MUST have the shortest possible, clearly defined expiry date (e.g., max 3 months, subject to review).
- **No Standard Fix Available (Tool/Provider Limitation) (`NO_STANDARD_FIX`):** The finding highlights an issue for which no standard secure configuration or fix is currently available through the IaC provider or tool, and potential workarounds introduce greater risk or are infeasible. This requires thorough investigation, documentation, and high-level architectural and security approval. Frequent exceptions of this type for a specific component may trigger a dedicated architectural review.

### 3.2. Exception Logging Format and SSoT

All approved exceptions MUST be logged.

- **SSoT for Exception Log:**
  - A dedicated, version-controlled Markdown file: `gencraft-operations/iac-scan-exceptions/iac_scan_exception_log.md`.
  - This file MUST be protected by branch protection rules, requiring Pull Requests (PRs) and approvals from at least `Adam` and `Cerberus` for any changes, as per `gh-001.1-branching-strategy-and-protection.md` and `access-control-policy.md`. Only explicitly authorized Gems can merge these PRs.
- **Log Entry Format:** Each entry in `iac_scan_exception_log.md` MUST be a table row. For AI actionability and future scalability, column order and naming MUST remain consistent. Dates MUST be in `YYYY-MM-DD` format. GemIDs MUST be used for individuals.

  | Log Date   | Exception ID    | IaC Repo         | Affected System/Component | Resource Address/File Path  | Scan Tool   | Finding ID/Rule | Finding Severity (Gencraft) | Data Classification | Justification Summary                    | Exception Type                                                        | Mitigating Controls Summary (or N/A) | Approver(s) (GemIDs)                            | Expiry Date | Next Review Date | Remediation Issue Link (or N/A) | Status (ACTIVE, EXPIRED, REMEDIATED, REVOKED) | Last Review Date | Review Outcome & Notes |
  | :--------- | :-------------- | :--------------- | :------------------------ | :-------------------------- | :---------- | :-------------- | :-------------------------- | :------------------ | :--------------------------------------- | :-------------------------------------------------------------------- | :----------------------------------- | :---------------------------------------------- | :---------- | :--------------- | :------------------------------ | :-------------------------------------------- | :--------------- | :--------------------- |
  | YYYY-MM-DD | `EXC-YYYY-NNNN` | e.g., studio-iac | e.g., VPC Core Services   | e.g., `module.x.resource.y` | e.g., TFSec | e.g., AWS018    | e.g., HIGH                  | e.g., Confidential  | e.g., "Required for X, risk Y accepted." | `FALSE_POSITIVE`, `ACCEPTED_RISK`, `TEMPORARY_FIX`, `NO_STANDARD_FIX` | e.g., "Monitored by Alert X"         | e.g., `GCT-MGT-SECOFF-001`, `GCT-DVO-DVOTL-001` | YYYY-MM-DD  | YYYY-MM-DD       | e.g., `[org]/[repo]#123`        | `ACTIVE`                                      | YYYY-MM-DD       | e.g., Re-approved      |

- **Field Definitions for Log Entry:**
  - `Log Date`: Date the exception was formally logged (YYYY-MM-DD).
  - `Exception ID`: Unique identifier (Format: `EXC-YYYY-NNNN`). `Adam`'s crew (DevOps) manages issuance.
  - `IaC Repo`: The Gencraft repository where the IaC code resides.
  - `Affected System/Component`: High-level system or component impacted.
  - `Resource Address/File Path`: Specific OpenTofu resource address or file path and line number(s).
  - `Scan Tool`: Name of the IaC scanning tool (e.g., TFSec, Checkov).
  - `Finding ID/Rule`: The specific ID or rule name from the scanning tool.
  - `Finding Severity (Gencraft)`: Severity assessed by Gencraft (CRITICAL, HIGH, MEDIUM, LOW, INFORMATIONAL), guided by `information-classification-and-handling-policy.md`. `Cerberus` confirms/assigns this.
  - `Data Classification`: Classification of the data/resource affected, as per Gencraft policy.
  - `Justification Summary`: Concise summary. Full details in the linked PR/Issue.
  - `Exception Type`: Enum: `FALSE_POSITIVE`, `ACCEPTED_RISK`, `TEMPORARY_FIX`, `NO_STANDARD_FIX`.
  - `Mitigating Controls Summary`: Brief summary. Full details in linked PR/Issue.
  - `Approver(s) (GemIDs)`: Comma-separated list of GemIDs of formal approvers.
  - `Expiry Date`: Mandatory (YYYY-MM-DD). For `FALSE_POSITIVE`, may be "N/A" or a distant review date (e.g., next major tool version). `ACCEPTED_RISK` max 1 year. `TEMPORARY_FIX` max 3 months, ideally shorter.
  - `Next Review Date`: Calculated based on Expiry Date or review cadence (YYYY-MM-DD).
  - `Remediation Issue Link`: Link to the issue tracking remediation (mandatory for `TEMPORARY_FIX`), following `s19-action-item-management-protocol.md`.
  - `Status`: Enum: `ACTIVE`, `EXPIRED`, `REMEDIATED`, `REVOKED`.
  - `Last Review Date`: Date of the last formal review of this exception (YYYY-MM-DD).
  - `Review Outcome & Notes`: Summary of the last review outcome and key notes.

### 3.3. Exception Request Process

1.**Identification & Initial Analysis:** An IaC scan finding is identified. The responsible Gem (Developer/Requester) analyzes it. If a standard fix is feasible, it MUST be applied. 2.**Request Initiation:** If an exception is deemed necessary per criteria in 3.1: - The requester MUST open an Issue in `gencraft-operations` using the "IaC Scan Exception Request" template (To Be Created by `Adam`). This template will guide the provision of all necessary information. - The Issue must detail: - All fields required for the log entry (see 3.2). - Full justification addressing specific criteria from 3.1. - Evidence for false positives (e.g., link to PR comment where analysis was performed). - Detailed description and validation plan for mitigating controls (for `ACCEPTED_RISK`). - Concrete, technically viable remediation plan and timeline (for `TEMPORARY_FIX`). - Impact analysis (security, compliance, architectural, operational) of _not_ fixing versus the impact of the exception. - Proposed `Expiry Date` and `Exception Type`.
3.The Issue is then assigned for review as per section 3.4.

### 3.4. Exception Review and Approval Process

1.**Assignment & Review Panel:** The request Issue is assigned to `Cerberus` and `Adam`. - `Cerberus` MUST review all requests for security implications. Cerberus's opinion on security risk is binding unless formally escalated via S2. - `Adam` (or a senior DevOps delegate like `Édouard` or `Benjamin`) reviews for operational/technical feasibility. - For architecturally significant exceptions (affecting critical resources or core design, identified by `Adam` or `Cerberus`), `Isaac` (or SARCH delegate/relevant Tech Lead) MUST be included. 2.**Approval Authority & Quorum:** - **`FALSE_POSITIVE`**: Requires approval from `Cerberus` AND one relevant technical specialist (e.g., `Benjamin`, `Adam`, Tech Lead). - **`TEMPORARY_FIX` (LOW/MEDIUM Gencraft Severity Finding)**: Requires approval from `Cerberus` AND `Adam`. - **`ACCEPTED_RISK` (any severity) & `TEMPORARY_FIX` (HIGH/CRITICAL Gencraft Severity Finding)**: Requires approval from `Cerberus`, `Adam`, AND `Isaac` (or SARCH delegate/Tech Lead). Justification for "temporary" nature of high/critical issues must be exceptionally strong. - **`NO_STANDARD_FIX`**: Requires approval from `Cerberus`, `Adam`, AND `Isaac`. 3.**Decision & Traceability:** - Approval/rejection, rationale, and confirmation that OPS_001 criteria were met MUST be documented in the request Issue. - Approved exceptions result in a PR to update `iac_scan_exception_log.md`, reviewed by `Adam` and `Cerberus`. - Adheres to S1 for PRs and S7 for decisions.

### 3.5. Review of Active Exceptions

1.**Cadence:** - `TEMPORARY_FIX`: Reviewed at least one week before `Expiry Date`. - `ACCEPTED_RISK`: Reviewed quarterly by `Cerberus` and `Adam`. If Gencraft Severity is HIGH/CRITICAL, reviewed monthly. - `FALSE_POSITIVE`: Reviewed annually or when scan tool major versions change. - `NO_STANDARD_FIX`: Reviewed at least semi-annually. 2.**Process:** - `Diane` (Gem AE), potentially assisted by AI tools or scripts (developed by `Camille`), generates a report of exceptions due for review and assigns review tasks. - The original approvers (or role successors) re-evaluate the exception. - **Outcomes:** - **Remediate:** Exception no longer needed; finding fixed. Log status: `REMEDIATED`. - **Re-approve:** Justification and mitigating controls (if any) re-validated. `Expiry Date` and `Next Review Date` updated. Log updated. - **Revoke:** Exception no longer justified. Remediation prioritized. Log status: `REVOKED` (until fixed, then `REMEDIATED`). 3.**Log Updates:** All review activities and outcomes MUST be updated in `iac_scan_exception_log.md` via PR. `Last Review Date` and `Review Outcome & Notes` fields are updated.

### 3.6. Tooling and Automation (Actionability for AI Gems)

- **Log Parsing:** The Markdown table format, with consistent column order and date formats (YYYY-MM-DD), MUST be maintained for reliable parsing by AI Gems. Enum values for `Exception Type` and `Status` MUST be used.
- **Automated AI Assistance (Development goal for AIE Team / DevOps Automation):**
  - Monitor `Expiry Date`s / `Next Review Date`s and generate review tasks/reminders for `Adam`, `Cerberus`, and `Diane`.
  - Validate new log entries for completeness and correct enum usage.
  - Assist in pre-filling log entries from "IaC Scan Exception Request" Issues.
  - Cross-reference active exceptions with new scan results (potential for future suppression list generation, especially for `FALSE_POSITIVE`s).
  - Flag exceptions where mitigating controls may have drifted (if controls are also machine-readable).

## 4. Responsibilities

- **IaC Developers (e.g., `Benjamin`, `Camille`, other Gems/humans contributing to IaC, Tech Leads):**
  - Fixing IaC scan findings as the default action.
  - Initiating well-justified exception requests per 3.3.
  - Implementing remediation plans.
- **`Adam` (Gem AA - DevOps Team Lead):**
  - Co-Knowledge Guardian of this standard.
  - Reviewing/co-approving exception requests and log updates.
  - Overseeing the process, managing `Exception ID` issuance.
- **`Cerberus` (Security Officer Gem):**
  - Co-Knowledge Guardian of this standard.
  - Primary security reviewer/approver for exceptions.
  - Leading reviews of `ACCEPTED_RISK` exceptions.
  - Assigning Gencraft Severity to findings.
  - Maintaining an overview of the IaC risk profile from exceptions and reporting significant risks.
- **`Isaac` (Gem SARCH - Software Architect) / Relevant Tech Leads:**
  - Reviewing/co-approving exceptions with architectural significance or high/critical severity.
  - Validating technical viability of remediation plans or "No Standard Fix" justifications.
- **`Édouard` (Gem AD - DevOps Strategy Specialist):**
  - Advising on process efficiency and alignment with other DevOps standards.
  - Proposing evolutions to this standard.
- **`Diane` (Gem AE - Ops/Support Specialist):**
  - Generating reports for periodic exception reviews.
  - Assisting in maintaining the log file's integrity under supervision.
- **`Camille` (Gem AB - Automation Specialist):**
  - Developing scripts/automation to support the exception management process (e.g., log parsing, report generation) as prioritized.
- **Authors of other IaC Standards (e.g., for `IAC_007`):**
  - Consulting OPS_001 to ensure process coherence.
- **Governance Crew (Relevant Subset):**
  - Approving this standard document.
  - Point of escalation for unresolved disagreements (per S2).

## 5. References & SSoTs

- **Primary SSoT:**
  - `iac_scan_exception_log.md`: Located at `gencraft-operations/iac-scan-exceptions/iac_scan_exception_log.md`.
- **Supporting Documents & Standards:**
  - `iac-007-iac-static-analysis-standard.md`
  - `sec-001-secrets-management-standard.md`
  - `s1-feedback-approval.md`
  - `s2-disagreement-escalation.md`
  - `s7-key-decisions-traceability.md`
  - `s19-action-item-management-protocol.md`
  - `gh-001.1-branching-strategy-and-protection.md`
  - `access-control-policy.md`
  - `information-classification-and-handling-policy.md`
- **Templates:**
  - "IaC Scan Exception Request" Issue Template (To Be Created by `Adam` in `gencraft-operations/.github/ISSUE_TEMPLATE/`).

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
