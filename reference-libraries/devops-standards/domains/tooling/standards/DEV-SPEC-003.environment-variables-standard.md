---
docId: DEV-SPEC-003
title: Environment Variables Standard
version: 1.0.0
authors:
- Gem-BB (Camille)
reviewers:
- Gem-AA (Lead)
- Gem-A (Infra)
creation_date: '2025-06-09'
language: en
summary: Defines the naming convention and management process for environment variables
  used in studio projects and automation.
last_updated_date: '2026-05-20'
metadata:
  lifecycle-stage: draft
  keywords:
  - tooling
  - environment
  - policy
  - configuration
  scope: studio
  domain: devops
  doc-type: specification
  intended-audience:
  - contributors
  - ai-agents
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/tooling/standards/DEV-SPEC-003.environment-variables-standard.md
---
## 1. Purpose

This document defines the standard for naming, defining, and managing environment variables across all GenCr@t Studio projects.

## 2. Naming Convention

All studio-specific environment variables MUST follow the `GFT_` prefix convention.

**Format:** `GFT_<SERVICE/DOMAIN>_<VARIABLE_NAME>`

- **`GFT_`**: Stands for GenCr@t.
- **`<SERVICE/DOMAIN>`**: The name of the service or domain the variable belongs to (e.g., `AUTH`, `BILLING`). For global variables, use `GLOBAL`.
- **`<VARIABLE_NAME>`**: A descriptive name in `UPPER_SNAKE_CASE`.

**Examples:**

- `GFT_AUTH_JWT_SECRET`
- `GFT_GLOBAL_LOG_LEVEL`
- `GFT_BILLING_STRIPE_API_KEY`

## 3. Management

- **Local Development:** For local development, variables MAY be defined in a `.env` file at the root of the repository. This `.env` file MUST be included in the project's `.gitignore` file.
- **CI/CD & Deployed Environments:** All secrets and environment variables for deployed environments (dev, staging, prod) MUST be managed through our designated secrets management solution (e.g., AWS Secrets Manager, HashiCorp Vault). They will be injected into the environment at runtime, not stored in the repository.
