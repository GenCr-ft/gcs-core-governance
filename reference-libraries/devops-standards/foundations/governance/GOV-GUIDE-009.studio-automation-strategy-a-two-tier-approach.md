---
docId: GOV-GUIDE-009
title: 'Studio Automation Strategy: A Two-Tier Approach'
version: 1.0.0
authors:
- Gem-BB (Camille)
reviewers:
- Gem-AA (Lead)
- Gem-D (Strategy)
creation_date: '2025-06-11'
language: en
summary: This document outlines the studio's two-tier automation strategy, distinguishing
  between the user-facing `gft-cli` for daily tasks and event-driven AI Agent Crews
  for complex business process automation.
last_updated_date: '2026-05-20'
metadata:
  lifecycle-stage: approved
  keywords:
  - automation
  - strategy
  - cli
  - crewai
  - devops
  - governance
  scope: studio
  domain: governance
  doc-type: protocol
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/foundations/governance/GOV-GUIDE-009.studio-automation-strategy-a-two-tier-approach.md
---
# Studio Automation Strategy: A Two-Tier Approach

To effectively implement our "Everything as Code" philosophy, our automation strategy is built on two distinct but complementary tiers: the **Artisan's Tool** (`gft-cli`) and the **Studio's Processes** (AI Agent Crews).

## 1. Tier 1: The `gft-cli` - The Artisan's Tool

The `gft-cli` is the interactive, human-facing command-line interface. Its primary purpose is to streamline and standardize the daily, high-frequency, low-level tasks performed by all studio members.

- **Role:** Facilitate individual contribution and enforce standards at the source.
- **Nature:** Interactive, user-triggered.
- **Examples:**
  - `gft git commit`: Guided, compliant commit message creation.
  - `gft docs new`: Scaffolding a new SSoT document from a template.
  - `gft project new`: Automating repository creation from a studio template.

## 2. Tier 2: AI Agent Crews - The Studio's Automated Processes

Crews are autonomous groups of AI agents that handle complex, end-to-end business processes. They operate primarily on the backend and are triggered by events within our ecosystem (e.g., a GitHub webhook).

- **Role:** Automate multi-step, asynchronous, and high-level studio processes.
- **Nature:** Event-driven, automated, backend service.
- **Examples:**
  - **Triage Crew:** Automatically labels, categorizes, and assigns new GitHub issues.
  - **Lexicon Crew:** When an issue with the label `glossary-add` is created, this crew validates the term and automatically updates the `glossary.md` file.
  - **Release Crew:** Manages the process of creating release notes, versioning, and publishing software artifacts.

## 3. Synergy and Architecture Summary

The two tiers work in synergy. The `gft-cli` can act as a trigger for a Crew. For example, `gft-cli project new` could create an issue that triggers a "New Project Setup Crew" to configure permissions and integrations on the backend.

| Aspect                     | `gft-cli` (Artisan's Tool)                                                  | AI Agent Crews (Studio's Processes)                                |
| :------------------------- | :-------------------------------------------------------------------------- | :----------------------------------------------------------------- |
| **Raison d'être**          | Facilitate daily interactive tasks for individuals.                         | Automate complex, event-driven business processes.                 |
| **Emplacement du Code**    | `gcs-plt-tools`                                                             | `gcs-plt-crewwkf` (definitions) & `gcs-plt-tools` (specific tools) |
| **Méthode de Déploiement** | Standalone executable installed on user machines via the onboarding script. | Backend services (e.g., Docker containers) triggered by webhooks.  |
