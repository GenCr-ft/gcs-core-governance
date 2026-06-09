---
docId: DEV-STAN-006
title: Index of Infrastructure as Code (IaC) Standards
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This document outlines Infrastructure as Code (IaC) standards for the GenCr@ft
  project, primarily using Terraform. It details best practices for consistent, secure,
  and auditable infrastructure provisioning and management, emphasizing declarative
  configuration and version control.
last_updated_date: '2026-06-02'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - iac-standards
  - terraform
  - infrastructure-as-code
  - devops
  - gencraft
  - automation
  - configuration-management
  scope: studio
  domain: devops
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/iac/standards/DEV-STAN-006.index-of-infrastructure-as-code-(iac)-standards.md
---
# Index of Gencraft Studio IaC Standards

This document serves as an index for all specific Infrastructure as Code (IaC) standards defined within the Gencraft Studio's DevOps framework, primarily focusing on OpenTofu (Terraform). These standards are designed to ensure consistency, security, and auditability in our infrastructure provisioning and management processes.

Please refer to the individual documents listed below for detailed policies, best practices, and procedures related to each aspect of our IaC implementation.

---

## Index of Contents

### Subdirectories

- [templates/](./templates/)

### Files

- [Iac 001 Opentofu Tooling Standard](DEV-SPEC-009.iac-001-opentofu-tooling-standard.md): This standard defines the
  Gencraft studio’s official tooling, versioning, and environment configuration for Infrastructure as Code
  (IaC) development using OpenTofu. It ensures consistency across all IaC projects, simplifies onboarding,
  and maintains a secure IaC development lifecycle.
- [Iac 002 Cloud Resource Tagging Standard](DEV-STAN-007.iac-002-cloud-resource-tagging-standard.md): This standard
  mandates a consistent cloud resource tagging strategy across Gencraft Studio's cloud environments,
  primarily focused on cost management, automation, and resource organization. It requires mandatory tags
  like environment, project, and owner-team, alongside recommended tags for further refinement.
- [Iac 003 Opentofu State Management Standard](DEV-STAN-008.iac-003-opentofu-state-management-standard.md): This
  standard mandates the use of AWS S3 with DynamoDB for OpenTofu state management within Gencraft. It
  emphasizes secure state file storage, locking mechanisms, and isolation strategies to ensure integrity,
  availability, and prevent conflicts, crucial for reliable Infrastructure as Code operations.
- [Iac 004 Clean Iac Principles](DEV-STAN-009.iac-004-clean-iac-principles.md): This standard establishes core
  principles for “Clean Infrastructure as Code” (IaC) using OpenTofu at Gencraft, emphasizing idempotency,
  modularity, readability, explicit dependencies, and security by design. These principles ensure our IaC is
  understandable, maintainable, and secure.
- [Iac 005 Iac Resource Naming Conventions](DEV-STAN-010.iac-005-iac-resource-naming-conventions.md): This standard
  establishes a consistent naming convention for all cloud resources provisioned via OpenTofu within
  Gencraft. It emphasizes lowercase names with hyphens, a defined pattern for clarity, and promotes reusable
  modules for constructing full resource names.
- [Iac 006 Iac Testing Strategy](DEV-STAN-011.iac-006-iac-testing-strategy.md): This standard defines a multi-layered
  testing strategy for OpenTofu-based Infrastructure as Code (IaC) at Gencraft. It emphasizes static
  analysis, unit testing, and integration testing to ensure syntactically correct, secure, and functional
  IaC code, ultimately increasing confidence in deployments and reducing risks.
- [Iac 007 Iac Static Analysis Standard](DEV-STAN-012.iac-007-iac-static-analysis-standard.md): This standard
  mandates the use of static analysis tools, TFLint and TFSec (or equivalent), for OpenTofu infrastructure as
  code within Gencraft. It aims to proactively detect errors, best practice deviations, and security
  vulnerabilities before deployment, integrated into CI/CD pipelines for automated validation.
- [Tag Definitions](DEV-STAN-013.tag-definitions.md): This document defines standard tag values for commonly used
  resource tags, including `gft:environment`, `gft:project`, `gft:owner-team`, `gft:data-sensitivity`,
  `gft:backup-policy`, and `gft:automation`. These tags are crucial for consistent resource management
  across Gencraft Studio.

## IA Instructions

This document is the primary index for the specific Infrastructure as Code (IaC) standards within the `gcs-core-governance/domains/iac/standards/` directory.

**Purpose for AI Agents:**

- Use the `docId` (`DEV-STAN-006`) for direct reference to this index.
- Navigate to individual standard documents using the relative links provided in the "Index of Contents". Each linked document details a specific IaC policy, best practice, or procedure, primarily for OpenTofu.
- The descriptions associated with each standard in the index provide a high-level understanding of its purpose.
- When needing to understand or apply a specific IaC control, naming convention, testing strategy, or tooling standard, consult this index to find the relevant IaC standard document.
