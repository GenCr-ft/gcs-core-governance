---
docId: ENG-STAN-003
title: VS Code Extension Recommendations
version: 1.0.0
authors:
  - Studio DevOps (Gem-BB / Camille)
creation_date: '2026-06-17'
last_updated_date: '2026-06-18'
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
Each role section lists that role's extensions in full; extensions inherited from parent roles are pre-flattened into the section by the author, not resolved at parse time. Extensions common to all roles live in `## Global Extensions` and are output separately.
The `Inherits:` lines in each role section are human-readable documentation only; they are not parsed by the script.

> **Human-readable companion:** `reference-libraries/devops-standards/domains/tooling/standards/DEV-SPEC-002.vs-code-recommendations.md` provides the rationale, `settings.json` recommendations, and role-inheritance context. This file is the authoritative source for the parser; DEV-SPEC-002 is the authoritative source for human decision-making.

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

### software-architect

Inherits: `lead-developer-tech-lead` → `common-base`

- ms-python.python
- dbaeumer.vscode-eslint
- esbenp.prettier-vscode
- drawio.hiker-drawio

### gameplay-programmer

Inherits: `lead-developer-tech-lead` → `common-base`

- ms-python.python
- dbaeumer.vscode-eslint
- esbenp.prettier-vscode

### network-backend-programmer

Inherits: `lead-developer-tech-lead` → `common-base`

- ms-python.python
- dbaeumer.vscode-eslint
- esbenp.prettier-vscode

### ui-developer-game

Inherits: `lead-developer-tech-lead` → `common-base`

- ms-python.python
- dbaeumer.vscode-eslint
- esbenp.prettier-vscode

### pcg-specialist

Inherits: `lead-developer-tech-lead` → `common-base`

- ms-python.python
- dbaeumer.vscode-eslint
- esbenp.prettier-vscode
- rust-lang.rust-analyzer

### devops-team-lead

Inherits: `lead-developer-tech-lead` → `common-base`

- ms-python.python
- dbaeumer.vscode-eslint
- esbenp.prettier-vscode

### character-artist-3d-voxel

Inherits: `art-director` → `common-base`

- blender.blender-vscode

### environment-artist-3d-voxel

Inherits: `character-artist-3d-voxel` → `art-director` → `common-base`

- blender.blender-vscode

### cerberus-security-officer

Inherits: `devops-specialist` → `devops-team-lead` → `lead-developer-tech-lead` → `common-base`

- ms-python.python
- dbaeumer.vscode-eslint
- esbenp.prettier-vscode
- hashicorp.terraform
- ms-azuretools.vscode-docker

### technical-artist

Inherits: `lead-developer-tech-lead` → `common-base`

- ms-python.python
- dbaeumer.vscode-eslint
- esbenp.prettier-vscode

### level-designer-procedural

Inherits: `game-designer` → `common-base`

- yzane.markdown-all-in-one

### narrative-designer-procedural

Inherits: `game-designer` → `common-base`

- yzane.markdown-all-in-one
