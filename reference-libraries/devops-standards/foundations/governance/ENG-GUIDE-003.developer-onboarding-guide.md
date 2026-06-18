---
docId: ENG-GUIDE-003
title: Developer Onboarding Guide
version: 1.0.0
authors:
- Gem-BB (Camille)
reviewers:
- Gem-AA (Lead)
- HR-Gem
creation_date: '2025-06-09'
language: en
summary: This guide provides a step-by-step checklist for new technical team members
  to set up their environment, get access to required tools, and understand studio
  processes.
last_updated_date: '2026-06-18'
metadata:
  lifecycle-stage: draft
  keywords:
  - governance
  - onboarding
  - guide
  - developer-experience
  scope: studio
  domain: devops
  doc-type: guide
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/foundations/governance/ENG-GUIDE-003.developer-onboarding-guide.md
---
## 1. Welcome to GenCr@t

Welcome to the team! This guide will help you get set up and productive as quickly as possible. Our philosophy is built on automation and clear standards, so let's get you started.

## 2. Week 1 Checklist

### Day 1: Essentials

- [ ] **HR Onboarding:** Complete all required HR paperwork with `HR-Gem`.
- [ ] **Accounts & Access:** Ensure you have access to core systems (Email, Slack, Jira, GitHub).
- [ ] **Meet the Team:** Introduction to your assigned mentor and the DevOps team.

### Day 2-3: Environment Setup

- [ ] **Run the Onboarding Script:** This is the most critical step. Clone the `gcd-onboarding-scripts` repository and run the `gft-onboarding.sh` script. This will install all required tools and configure your environment.
  - _Note: This script will be developed in Phase 2 of our mission._
- [ ] **IDE Configuration:** VS Code extensions are installed automatically by the onboarding script. The canonical extension catalogue is `tooling/ENG-STAN-003.vs-code-extension-recommendations.md`.
- [ ] **Environment Variables:** Role-specific environment variables are applied automatically. The canonical definitions are in `tooling/ENG-STAN-002.environment-variable-standard.md`.
- [ ] **Docker Images:** Studio container images to pre-pull are listed in `tooling/ssot/.docker-images-gft`.
- [ ] **SSH & GPG Keys:** Ensure your SSH key is added to your GitHub account for secure access.

### Day 4-5: Understanding the Ecosystem

- [ ] **Clone Key Repositories:**
  - [ ] `gcs-core-governance`: Read the "Vision and Principles" section.
  - [ ] `gcs-core-governance`: Familiarize yourself with the repository structure.
- [ ] **First Task:** Your team lead will assign you a small, well-defined "starter" task or issue.

## 3. Key Resources & Communication

- **Daily Stand-up:** `[Time]`, `[Slack/Meet Link]`
- **Documentation SSoT:** `gcs-core-governance` (Why) and `gcs-core-governance` (How).
- **Primary Slack Channels:** `#dev-general`, `#devops-support`, `#[your-team-channel]`.
