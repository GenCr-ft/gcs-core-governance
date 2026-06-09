---
docId: GCS-GUIDE-504
title: "The Legal & Software Compliance Framework"
version: 1.0.0
status: Draft
date: 2025-06-19
authors:
  - "Legal Governance"
  - "Technical Governance"
knowledgeGuardian:
  - "Legal Counsel"
  - "Head of Engineering"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/05-governance-and-organization/GCS-GUIDE-504.legal-compliance-framework.md
metadata:
  lifecycle-stage: approved
  domain: engineering
  doc-type: guide
  scope: studio-wide
  security-classification: l2_confidential
  keywords:
    - "compliance"
    - "legal"
    - "gdpr"
    - "foss"
    - "license"
    - "governance"
---

# The Legal & Software Compliance Framework

## 1. Objective

This guide establishes the official studio framework for managing legal and software compliance obligations. Its purpose is to ensure that all our products and development practices adhere to relevant laws, regulations, and open-source software licenses. This framework is mandatory and designed to protect the studio, our products, and our users from legal and financial risks.

## 2. Open-Source Software (FOSS) License Policy

The use of Free and Open-Source Software (FOSS) is encouraged, but it must be managed responsibly.

### 2.1. License Categories and Usage Policy

We classify FOSS licenses into three categories. The use of any new dependency MUST be approved based on its license.

| License Category | Examples | Studio Policy | Rationale |
| :--- | :--- | :--- | :--- |
| **Permissive** | MIT, Apache 2.0, BSD | **Approved for General Use.** | These licenses have minimal restrictions and are compatible with commercial software. |
| **Weak Copyleft** | LGPL, MPL 2.0 | **Approved with Conditions.** Requires review by the Legal Counsel. | These licenses require us to share modifications to the library itself, but not necessarily our proprietary code that uses it. |
| **Strong Copyleft** | GPLv2, GPLv3, AGPL | **Generally Forbidden.** Requires explicit, high-level approval from both Legal and Engineering leadership. | These licenses are "viral" and may require us to open-source our entire proprietary product if we use them. AGPL is particularly restrictive for network services. |

### 2.2. Compliance Protocol

1. **Dependency Approval:** Before adding a new third-party dependency to a project, its license MUST be checked against the policy above.
2. **Automated Scanning:** Our CI/CD pipeline [cite: GCS-GUIDE-202] includes automated Software Composition Analysis (SCA) tools that scan for and flag non-compliant or unapproved licenses. A build will fail if a forbidden license is detected.
3. **Attribution:** For all shipped products, we MUST maintain an attribution file (`NOTICE.md`) that lists all FOSS components and their corresponding licenses, as required.

## 3. Data Protection & Privacy Compliance (GDPR)

All systems handling user data MUST be designed and built in compliance with data protection regulations like the GDPR.

### 3.1. Core Principles

* **Privacy by Design & by Default:** Systems must be designed with data protection as a core principle, not an afterthought.
* **Data Minimization:** We only collect and process personal data that is strictly necessary for a specific, declared purpose.
* **Purpose Limitation:** Data collected for one purpose cannot be used for another without user consent.

### 3.2. Developer Compliance Checklist

During development, every engineer MUST ensure the following:

* [ ] **Anonymization/Pseudonymization:** Is personal data anonymized or pseudonymized wherever possible, especially in logs and analytics?
* [ ] **User Consent:** Is clear and explicit user consent obtained before collecting any personal data?
* [ ] **Right to Access & Erasure:** Have we built the technical mechanisms to allow users to request access to their data and to be "forgotten" (i.e., have their data permanently deleted)?
* [ ] **Secure Storage:** Is all personally identifiable information (PII) encrypted at rest and in transit? [cite: GCS-GUIDE-306]

## 4. Audit Management Protocol

Our systems may be subject to internal or external security and compliance audits.

1. **Evidence Readiness:** Our engineering documentation serves as primary evidence during an audit. This includes:
    * Architecture diagrams [cite: GCS-GUIDE-301].
    * Software Bill of Materials (SBOMs) [cite: GCS-GUIDE-202].
    * Security scan reports from our CI/CD pipelines.
    * Incident postmortems [cite: GCS-GUIDE-202].
2. **Point of Contact:** During an audit, a single Point of Contact (PoC) will be designated by the Engineering leadership to coordinate all requests and responses.
3. **Remediation:** Any findings or non-compliance issues identified during an audit MUST be documented in our Technical Debt Backlog [cite: GCS-GUIDE-303] and prioritized for remediation.
