---
docId: ENG-STAN-002
title: VS Code Extension Recommendations
version: 1.0.0
authors:
  - Studio DevOps (Gem-BB / Camille)
creation_date: '2026-06-17'
last_updated_date: '2026-06-17'
language: en
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: engineering
  doc-type: standard
  security-classification: l2_confidential
  intended-audience:
    - contributors
    - ai-agents
    - devops-team
---

# VS Code Extension Recommendations

Parsed at runtime by `gcd-onboarding-scripts/includes/get_vscode_extensions.py`.
Section headings must match the role slug passed to the onboarding script (lowercase, hyphens).
Role sections include both role-specific extensions and inherited extensions (flattened from GOV-GUIDE-010).

## Global Extensions

Installed for every studio member regardless of role.

- davidanson.vscode-markdownlint

## Role Extensions

### devops-specialist

Inherits: `devops-team-lead` → `lead-developer-tech-lead` → `common-base`

- ms-python.python
- dbaeumer.vscode-eslint
- esbenp.prettier-vscode
- hashicorp.terraform
- ms-azuretools.vscode-docker

### rendering-engine-developer

Inherits: `lead-developer-tech-lead` → `common-base`

- ms-python.python
- dbaeumer.vscode-eslint
- esbenp.prettier-vscode
- rust-lang.rust-analyzer

### lead-developer-tech-lead

Inherits: `common-base`

- ms-python.python
- dbaeumer.vscode-eslint
- esbenp.prettier-vscode

### game-designer

Inherits: `common-base`

- yzane.markdown-all-in-one

