---
docId: GOV-GUIDE-010
title: Role Tooling & Resource Matrix
version: 1.0.1
authors:
- Gem-BB (Camille)
reviewers:
- Gem-AA (Lead)
- Gem-D (Strategy)
- Studio Director
creation_date: '2025-06-11'
language: en
summary: This document is the SSoT that maps every studio role to its required command-line
  tools, software, VS Code extensions, and repositories for the automated onboarding
  process. It is based on the official studio organization and prioritizes FOSS.
last_updated_date: '2026-06-19'
metadata:
  lifecycle-stage: approved
  keywords:
  - governance
  - roles
  - onboarding
  - matrix
  - ssot
  - foss
  scope: studio
  domain: governance
  doc-type: policy
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/foundations/governance/GOV-GUIDE-010.role-tooling--resource-matrix.md
---
# Role Tooling & Resource Matrix

## 1. Purpose

This document provides the definitive data matrix for the automated onboarding script (`gft-onboarding.sh`). The script will parse the `yaml` code block below to determine which resources to install and configure for each specific role within the studio.

## 2. Role Matrix Data

The `yaml` block below is the machine-readable SSoT.

```yaml
# SSoT data for the gft-onboarding.sh script.
# FOSS (Free and Open-Source Software) is prioritized.

roles:
  # Defines a common base for all roles
  - name: common-base
    description: "Universal tools and resources for every member of GenCr@ft Studio."
    tools:
      - name: git
      - name: github-cli
    vscode_extensions:
      - "davidanson.vscode-markdownlint"
    repositories:
      - "gcs-core-governance"
      - "gcs-core-governance"

  # Department: Management & Production
  - name: producer-project-manager
    inherits: common-base
    description: "Manages project timelines, resources, and reporting."
    external_software: ["GitHub Projects"]
    repositories: ["gcs-project-management", "gcs-plt-backlog"]
  - name: product-manager
    inherits: producer-project-manager
    description: "Defines product vision, strategy, and feature roadmap."
    repositories: ["gcs-plt-docs-req"]

  # Department: Design
  - name: game-designer
    inherits: common-base
    description: "Designs core game mechanics, systems, and content."
    vscode_extensions: ["yzane.markdown-all-in-one"]
    repositories: ["gcs-plt-gembp"]
  - name: level-designer-procedural
    inherits: game-designer
    description: "Designs and scripts procedural level generation."
  - name: narrative-designer-procedural
    inherits: game-designer
    description: "Creates the story, characters, and procedural dialogue."
  - name: ux-ui-designer
    inherits: common-base
    description: "Designs user experience and interface flows."
    external_software: ["Penpot (FOSS)", "Inkscape (FOSS)"]
    repositories: ["gcs-global-assets"]

  # Department: Programming
  - name: lead-developer-tech-lead
    inherits: common-base
    description: "Leads the programming team and makes key technical decisions."
    tools: ["node-lts", "python", "docker", "prettier"]
    vscode_extensions:
      ["ms-python.python", "dbaeumer.vscode-eslint", "esbenp.prettier-vscode"]
    repositories: ["gct-service-template-py", "gcs-plt-tools"]
  - name: software-architect
    inherits: lead-developer-tech-lead
    description: "Designs the overall software structure and high-level architecture."
    vscode_extensions: ["hediet.vscode-drawio"]
    repositories: ["gcs-plt-architecture"]
  - name: gameplay-programmer
    inherits: lead-developer-tech-lead
    description: "Implements core gameplay features."
  - name: network-backend-programmer
    inherits: lead-developer-tech-lead
    description: "Develops server-side logic and network infrastructure."
  - name: rendering-engine-developer
    inherits: lead-developer-tech-lead
    description: "Works on the graphics engine and rendering pipeline (Godot 4 / GDScript client, gcl-voxel-engine server library)."
    tools: ["rustup", "wasm-pack", "wasm-bindgen-cli"]
    vscode_extensions: ["rust-lang.rust-analyzer"]
    repositories: ["gcl-voxel-engine", "gcp-aethel-client", "gcp-aethel-pcg"]
  - name: ui-developer-game
    inherits: lead-developer-tech-lead
    description: "Implements the in-game user interface."
  - name: pcg-specialist
    inherits: lead-developer-tech-lead
    description: "Specializes in procedural content generation algorithms (Rust/WASM noise core in gcp-aethel-pcg)."
    tools: ["rustup", "wasm-pack", "wasm-bindgen-cli"]
    vscode_extensions: ["rust-lang.rust-analyzer"]
    repositories: ["gcp-aethel-pcg"]

  # Department: Art
  - name: art-director
    inherits: common-base
    description: "Defines and maintains the overall visual style of the game."
    external_software: ["Krita (FOSS)", "GIMP (FOSS)", "PureRef (Freeware)"]
    repositories: ["gcs-global-assets"]
  - name: lead-artist
    inherits: art-director
    description: "Leads the art team and supervises asset creation."
  - name: concept-artist
    inherits: art-director
    description: "Creates initial concepts for characters, environments, and assets."
  - name: character-artist-3d-voxel
    inherits: art-director
    description: "Creates 3D voxel assets for characters."
    external_software: ["Blender (FOSS)", "MagicaVoxel (Freeware)"]
    vscode_extensions: ["blender.blender-vscode"]
  - name: environment-artist-3d-voxel
    inherits: character-artist-3d-voxel
    description: "Creates 3D voxel environments and props."
  - name: animator
    inherits: art-director
    description: "Creates animations for characters and objects."
    external_software: ["Blender (FOSS)"]
  - name: vfx-artist
    inherits: art-director
    description: "Creates visual effects."
    external_software: ["Blender (FOSS)"]
  - name: technical-artist
    inherits: lead-developer-tech-lead # Inherits tech for scripting needs
    description: "Bridges the gap between artists and programmers."
    repositories: ["gcs-global-assets"]

  # Department: Audio
  - name: sound-designer-procedural
    inherits: common-base
    description: "Creates and implements procedural sound effects."
    external_software:
      ["Audacity (FOSS)", "Wwise (Industry Standard w/ free tier)"]
    repositories: ["gcs-global-assets"]
  - name: composer-adaptive
    inherits: sound-designer-procedural
    description: "Writes and implements adaptive music scores."

  # Department: QA
  - name: qa-engineer-test-lead
    inherits: common-base
    description: "Designs and executes testing plans, leads the QA effort."
    tools: ["python"] # For test automation scripting
    repositories: ["gcs-plt-backlog"]

  # Department: DevOps
  - name: devops-team-lead
    inherits: lead-developer-tech-lead
    description: "Leads the DevOps team."
  - name: devops-specialist
    inherits: devops-team-lead
    description: "Manages infrastructure, automation, CI/CD, and studio tooling (grouping specialists A, B, C, D)."
    tools: ["opentofu", "kubectl", "helm"]
    vscode_extensions: ["hashicorp.terraform", "ms-azuretools.vscode-docker"]
    repositories:
      [
        "gencraft-iac",
        "gcd-backup-utilities",
        "gcd-onboarding-scripts",
        "gcd-shared-actions",
      ]

  # Department: Marketing, Sales, BizDev
  - name: marketing-manager
    inherits: common-base
    description: "Manages marketing campaigns and studio promotion."
  - name: sales-bizdev-manager
    inherits: common-base
    description: "Manages business development and sales strategies."

  # Department: Community & Support
  - name: community-manager
    inherits: common-base
    description: "Engages with the player community."
  - name: player-support
    inherits: common-base
    description: "Provides support to players."

  # Department: Legal
  - name: legal-counsel
    inherits: common-base
    description: "Provides legal advice and manages compliance."
    repositories: ["gcs-studio-legal"]

  # Department: Studio Support Functions (Meta-Gems)
  - name: cerberus-security-officer
    inherits: devops-specialist # High technical needs
    description: "Manages overall studio security."
    repositories: ["gcs-security-core"]
  - name: cresus-financial-resource-tracker
    inherits: common-base
    description: "Tracks studio finances and resources."
    external_software: ["GnuCash (FOSS)", "LibreOffice Calc (FOSS)"]
  - name: lexicon-glossary-master
    inherits: common-base
    description: "Maintains the studio's official glossary."
```
