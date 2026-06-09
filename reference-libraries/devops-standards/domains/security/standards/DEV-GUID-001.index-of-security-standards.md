---
docId: DEV-GUID-001
title: Index of Security Standards
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This document outlines security standards and best practices for the GenCr@ft
  project, emphasizing security by design, defense in depth, and compliance. It details
  key areas and responsibilities for maintaining a secure development and operational
  environment.
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - security-standards
  - devops
  - gencraft
  - security-best-practices
  - secrets-management
  - compliance
  - information-security
  scope: studio
  domain: devops
  doc-type: guide
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/security/standards/DEV-GUID-001.index-of-security-standards.md
---
# Index of Gencraft Studio Security Standards

This document serves as an index for all specific security standards defined within the Gencraft Studio's DevOps framework. These standards are essential for maintaining a robust security posture across our development and operational environments.

Please refer to the individual documents listed below for detailed policies and procedures related to each security area.

---

## Index of Contents

### Files

- [Sec 001 Secrets Management Standard](SEC-STAN-001.sec-001-secrets-management-standard.md): This standard outlines
  policies and procedures for managing secrets within Gencraft Studio, emphasizing centralized secure
  storage, least privilege access, encryption, auditing, and regular rotation. Secrets MUST NOT be hardcoded
  or committed to source control. The primary recommended solution is HashiCorp Vault or a cloud provider
  native secrets manager (e.g., AWS Secrets Manager), with strong emphasis on using OIDC for authentication
  and avoiding direct secret storage in IaC.
- [Sec 002 Iac Scanning Tool Selection](SEC-STAN-002.sec-002-iac-scanning-tool-selection.md): Gencraft will
  standardize on TFSec as the primary IaC security scanning tool for OpenTofu configurations. This decision
  prioritizes TFSec's specialization in IaC, its cloud provider coverage, and alignment with Gencraft’s
  technical and operational principles.
- [Sec 003 Secret Scanning Standard](SEC-STAN-003.sec-003-secret-scanning-standard.md): This standard mandates the
  use of GitHub Advanced Security and Gitleaks to detect and remediate secrets committed to Gencraft source
  code repositories. It requires automated scanning in pre-commit hooks, CI/CD pipelines, and periodic
  repository scans, with a defined process for managing false positives and ensuring immediate remediation
  of active secrets.

## IA Instructions

This document is the primary index for the specific security standards within the `gcs-core-governance/domains/security/standards/` directory.

**Purpose for AI Agents:**

- Use the `docId` (`GCSE-README-IDX-001`) for direct reference to this index.
- Navigate to individual standard documents using the relative links provided in the "Index of Contents". Each linked document details a specific security policy or procedure.
- The descriptions associated with each standard in the index provide a high-level understanding of its purpose.
- When needing to understand or apply a specific security control or best practice, consult this index to find the relevant security standard document.
