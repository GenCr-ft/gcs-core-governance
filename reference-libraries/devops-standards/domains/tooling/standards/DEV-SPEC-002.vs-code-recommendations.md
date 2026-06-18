---
docId: DEV-SPEC-002
title: VS Code Recommendations
version: 1.0.0
authors:
- Gem-BB (Camille)
reviewers:
- Gem-AA (Lead)
creation_date: '2025-06-09'
language: en
summary: Provides a list of recommended Visual Studio Code extensions and settings
  to ensure a consistent development environment across the studio.
last_updated_date: '2026-06-18'
metadata:
  lifecycle-stage: approved
  keywords:
  - tooling
  - vscode
  - ide
  - developer-experience
  scope: studio
  domain: devops
  doc-type: specification
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/tooling/standards/DEV-SPEC-002.vs-code-recommendations.md
---
## 1. Purpose

This document lists the recommended Visual Studio Code extensions and settings for GenCr@t Studio. A consistent environment simplifies troubleshooting and onboarding.

> **Machine-readable companion:** `tooling/ENG-STAN-003.vs-code-extension-recommendations.md` is the authoritative source consumed by the onboarding parser (`get_vscode_extensions.py`). This document provides the human-readable rationale, `settings.json` recommendations, and role-inheritance context. Keep both in sync when modifying the extension catalogue.

## 2. Recommended Extensions

The following extensions should be installed. The onboarding script will attempt to install them automatically.

| Extension ID                     | Publisher   | Description                                      |
| -------------------------------- | ----------- | ------------------------------------------------ |
| `dbaeumer.vscode-eslint`         | Microsoft   | Integrates ESLint into VS Code.                  |
| `esbenp.prettier-vscode`         | Prettier    | Code formatter using Prettier.                   |
| `ms-python.python`               | Microsoft   | Linting, debugging, and IntelliSense for Python. |
| `ms-azuretools.vscode-docker`    | Microsoft   | Adds support for Docker containers.              |
| `redhat.vscode-yaml`             | Red Hat     | YAML language support with validation.           |
| `hashicorp.terraform`            | HashiCorp   | HCL language support for Terraform/OpenTofu.     |
| `davidanson.vscode-markdownlint` | David Anson | Markdown linter and style checker.               |

## 3. Recommended `settings.json`

It is recommended to include these settings in your user `settings.json` file.

```json
{
  // General
  "files.eol": "\n",
  "files.insertFinalNewline": true,
  "files.trimTrailingWhitespace": true,

  // Formatting
  "editor.formatOnSave": true,

  // Markdown
  "[markdown]": {
    "editor.defaultFormatter": "esbenp.prettier-vscode"
  },

  // Python
  "[python]": {
    "editor.defaultFormatter": "ms-python.black-formatter"
  }
}
```
