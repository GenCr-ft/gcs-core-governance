---
docId: GOV-GUIDE-HG-AC-003
title: Technical Constraints — Engineering and Quality
version: 1.0.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: guide
  intended-audience: [ai-agents]
  security-classification: l2_confidential
  source_version: "1.0.0"
  last_verified: "2026-06-27"
---
# Technical Constraints — Engineering and Quality

Extracted engineering constraints for AI agents. Each row is an actionable rule.

> **Source:** `execution-manuals/onboard-manuals/grounding-docs/GOV-GUIDE-017.unified-technical-standard-engineering-and-quality.md`

## Constraints Table

| Constraint | Domain | Enforcement | Source Section |
|-----------|--------|-------------|---------------|
| Branch from `develop` for features; squash-merge PR back to `develop`; release branch from `develop` → merge commit to `main` | Version Control | PR review gate | §2.1 Git Branching |
| All software artifacts follow SemVer `MAJOR.MINOR.PATCH` — MAJOR for breaking, MINOR for additive, PATCH for fixes | Versioning | Release checklist | §2.2 SemVer |
| Python module filenames: lowercase + underscores only; hyphens forbidden (causes `ImportError`) | Code | Pre-commit / CI lint | §2.3 Python Naming |
| DoD requires: code reviewed + merged, all CI tests pass, QA validated, no Blocker/Critical bugs, docs updated, PO accepted | Quality | Close gate | §3.1 DoD |
| Bug severity uses SEV-1 (Blocker) to SEV-5 (Trivial); priority P1 (Urgent) to P4 (Low) | Quality | Sprint triage | §3.2 Bug Triage |
| Security SDL mandatory: 7 phases — Training → Requirements → Design (threat modeling) → Implementation → Verification (SAST/SCA) → Release → Response | Security | PR gate + CI | §4.1 SDL |
| Security review mandatory in code review (Pillar 3) | Security | PR review gate | §4.1 SDL §5 |
| Minimum 80% unit test coverage for all TypeScript/Python services | Testing | CI coverage gate | §3.1 DoD |

## Key Agents Referenced

| Role | GemID | Responsibility |
|------|-------|---------------|
| QA Lead | GCT-QAS-QA-001 (Sentinel) | Bug triage, severity assignment |
| Product Owner | GCT-MGT-PM-001 (Béatrice) | Priority assignment, DoD acceptance |
| Security Officer | GCT-MGT-SECOFF-001 (Cerberus) | Security gate approval |
| Senior Architect | GCT-PRG-SARCH-001 (Isaac) | Engineering standard reviews |
