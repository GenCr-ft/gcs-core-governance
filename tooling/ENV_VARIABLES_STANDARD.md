---
docId: ENG-STAN-002
title: Environment Variable Standard
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

# Environment Variable Standard

Parsed at runtime by `gcd-onboarding-scripts/includes/get_standard_env_vars.py`.
The script writes matching `export KEY=VALUE` lines into the engineer's shell profile.

## Common Variables

Required by every studio member regardless of role.

```env
GFT_PROJECTS_HOME="$HOME/gft_studio"
```

## Role Specific

Role-specific variables appended after the common block.
Section headings must match the role slug passed to the onboarding script (lowercase, hyphens).

### devops-specialist

```env
GFT_AWS_PROFILE="gft-devops"
```
