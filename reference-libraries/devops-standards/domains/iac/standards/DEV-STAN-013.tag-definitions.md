---
docId: DEV-STAN-013
title: Tag Definitions
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-06-30'
language: en
summary: "**DEPRECATION NOTICE:** The taxonomy and metadata rules previously defined in this document are now obsolete. The official and single source of truth for all studio-wide taxonomy, classification, and metadata rules is now defined in the standard `GOV-STANDARD-008: SSoT Master Taxonomy and Governance Standard`. Please refer to that document for all current definitions and to the `gcs.governance.yml` file for the raw vocabulary data."
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: deprecated
  keywords:
  - tag-iac-standards
  - tag-resource-tagging
  - tag-gft-environment
  - tag-gft-project
  - tag-gft-owner-team
  - tag-gft-data-sensitivity
  - tag-gft-backup-policy
  scope: studio
  domain: devops
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/iac/standards/DEV-STAN-013.tag-definitions.md
---

**DEPRECATION NOTICE:** The taxonomy and metadata rules previously defined in this document are now obsolete. The official and single source of truth for all studio-wide taxonomy, classification, and metadata rules is now defined in the standard `GOV-STANDARD-008: SSoT Master Taxonomy and Governance Standard`. Please refer to that document for all current definitions and to the `gcs.governance.yml` file for the raw vocabulary data.

## 1. Purpose

This document provides the standard predefined values for commonly used tag keys as defined in `IAC-002:
Cloud Resource Tagging Standard`. Using a consistent set of values is crucial for effective cost
management, automation, resource organization, security, and operational management.

These values should be used whenever applying the corresponding tags via Infrastructure as Code (IaC).

## 2. Standard Tag Value Definitions

**DEPRECATION NOTICE:** The taxonomy and metadata rules previously defined in this document are now obsolete. The official and single source of truth for all studio-wide taxonomy, classification, and metadata rules is now defined in the standard `GOV-STANDARD-008: SSoT Master Taxonomy and Governance Standard`. Please refer to that document for all current definitions and to the `gcs.governance.yml` file for the raw vocabulary data.

## 3. Maintaining these Definitions

- This document serves as the master list for approved tag values for the keys specified.
- When new standard values are needed (e.g., a new environment type, a new project, a new data sensitivity
  level), they **MUST** be proposed via a Pull Request to this document in the `GenCr-ft/devops-standards`
  repository and reviewed by the DevOps team and relevant stakeholders.
- IaC configurations (`GenCr-ft/gencraft-iac`) **SHOULD** reference or validate against these approved
  values where possible (e.g., using variable validation rules in Terraform/OpenTofu).

## 4. Review and Updates

This list of tag definitions will be reviewed at least annually, or as needed, alongside `IAC-002: Cloud
Resource Tagging Standard`.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
