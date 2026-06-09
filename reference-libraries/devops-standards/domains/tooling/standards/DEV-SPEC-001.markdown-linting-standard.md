---
title: Markdown Linting Standard
version: 1.0.0
last_updated: '2025-06-07'
reviewers:
- Gem-AA (DevOps Team Lead)
- Gem-D (Knowledge Guardian)
docId: DEV-SPEC-001
authors:
- Gem-BB (Camille)
metadata:
  lifecycle-stage: draft
  keywords:
  - tooling
  - markdown
  - linting
  - standard
  scope: studio
  domain: devops
  doc-type: specification
  intended-audience:
  - ai-agents
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/tooling/standards/DEV-SPEC-001.markdown-linting-standard.md
---
## 1. Overview

This document establishes `markdownlint` as the official linter for all Markdown (`*.md`) files
within the Gencraft Studio organization. Its purpose is to enforce structural consistency,
syntactical correctness, and adherence to readability rules across all our documentation, which
constitutes our Single Source of Truth (SSoT).

This standard complements `TOOL-003`, which handles code formatting (via Prettier).

## 2. Core Components

### 2.1. Linter Tool

The official command-line tool used in our CI/CD pipelines is `markdownlint-cli`.

### 2.2. VS Code Extension

For local development, all developers must install the `DavidAnson.vscode-markdownlint` extension.
This is specified in `VSCODE_RECOMMENDATIONS.md` and will be installed by the onboarding script.

### 2.3. Configuration

The Single Source of Truth for our `markdownlint` configuration is located at:
`configs/.markdownlint.yaml`.

_Note: This file was originally located at `linting/configs/` and should be moved as part of the
repository cleanup initiative._

All projects MUST use this configuration as a base.

## 3. Key Rules

The full ruleset is defined in the configuration file. However, a key organizational rule is:

- **Line Length (MD013):** All lines of prose must be limited to **120 characters**. This rule is
  disabled for tables and code blocks to maintain readability.

## 4. Enforcement

Adherence to this standard is enforced at two levels:

- **Local Development:** Real-time linting via the recommended VS Code extension.
- **Continuous Integration (CI):** A dedicated step in our CI pipelines will run `markdownlint-cli`
  against all `.md` files in a pull request.
