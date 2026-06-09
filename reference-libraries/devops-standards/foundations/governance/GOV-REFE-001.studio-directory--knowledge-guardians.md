---
docId: GOV-REFE-001
title: Studio Directory & Knowledge Guardians
version: 1.0.0
date: '2025-06-18'
authors:
- Governance Crew
knowledgeGuardian:
- Governance Crew
- Iris (GCT-UTL-RWSKA-001)
reviewers:
- Governance Crew
approvers:
- Lug (Studio Director)
metadata:
  scope: studio
  domain: governance
  doc-type: reference
  keywords:
  - directory
  - catalog
  - roles
  - knowledge-guardian
  lifecycle-stage: approved
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/foundations/governance/GOV-REFE-001.studio-directory--knowledge-guardians.md
---
# Studio Directory & Knowledge Guardians

## 1. Purpose

This document serves as the Single Source of Truth (SSoT) for the list of roles, teams, and individuals officially recognized as potential **Knowledge Guardians** within Gencraft Studio. Its primary objective is to provide a controlled and machine-readable list to validate and assist with the assignment of the `knowledgeGuardian` field in all document metadata.

Automated tooling (e.g., SSoT linters) MUST use the `directory.knowledge_guardians` list below as the source of truth for validation.

## 2. Official List of Knowledge Guardians

The following list is the definitive SSoT for all entities that can be assigned as a `knowledgeGuardian`.

```yaml
directory:
  knowledge_guardians:
    - name: "Governance Crew"
      description: "Team in charge of global processes and studio-wide standards."
    - name: "AIE Team Lead"
      description: "Lead of the AI Engineering Team, responsible for Gem blueprints and AI tooling."
    - name: "Lug (Studio Director)"
      description: "Studio Director, final approver for strategic documents."
    - name: "Antoine (GCT-MGT-PPM-001)"
      gemId: "GCT-MGT-PPM-001"
      description: "Producer / Project Manager, responsible for production and operational protocols."
    - name: "Béatrice (GCT-MGT-SPM-001)"
      gemId: "GCT-MGT-SPM-001"
      description: "Senior Product Manager, responsible for product vision and requirements."
    - name: "Isaac (GCT-PRG-SARCH-001)"
      gemId: "GCT-PRG-SARCH-001"
      description: "Senior Software Architect, responsible for platform and game architecture."
    - name: "Julien (GCT-PRG-LDTL-001)"
      gemId: "GCT-PRG-LDTL-001"
      description: "Lead Developer / Tech Lead, responsible for development standards and team guidance."
    - name: "Édouard (GCT-DVO-DVSST-001)"
      gemId: "GCT-DVO-DVSST-001"
      description: "DevOps Strategy Specialist, responsible for DevOps, IaC, and CI/CD standards."
    - name: "Iris (GCT-UTL-RWSKA-001)"
      gemId: "GCT-UTL-RWSKA-001"
      description: "Knowledge Architect, responsible for the SSoT structure and contribution guides."
    - name: "Véra (GCT-QAS-GPQA-001)"
      gemId: "GCT-QAS-GPQA-001"
      description: "Gem Performance & Quality Analyst, responsible for Gem onboarding and performance protocols."
    - name: "Zoé (GCT-QAS-QATL-001)"
      gemId: "GCT-QAS-QATL-001"
      description: "QA Lead, responsible for quality assurance standards and processes."
    - name: "Cerberus (GCT-MGT-SECOFF-001)"
      gemId: "GCT-MGT-SECOFF-001"
      description: "Security Officer, responsible for all security-related policies and standards."
    - name: "Henri (GCT-LEG-LCOUN-001)"
      gemId: "GCT-LEG-LCOUN-001"
      description: "Legal Counsel, responsible for all legal documents and compliance."
    - name: "Gemma's Maintainer"
      description: "The role responsible for maintaining the Gem Generator (`Gemma`), owner of its blueprints and core configuration."
```
