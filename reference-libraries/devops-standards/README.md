---
docId: GOV-READ-DS-001
title: devops-standards — Navigation Index
version: 1.0.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: devops
  doc-type: readme
  intended-audience: [contributors, ai-agents]
  security-classification: l1_internal
---
# devops-standards/

Reference library for all DevOps standards across GenCr@ft Studio. Content is **FROZEN** — see canonical live versions in `config-engines/` for enforced rules.

## Top-Level Structure

| Folder | Purpose |
|--------|---------|
| `domains/` | Per-discipline standards (6 subdomains) |
| `foundations/` | Core governance and GitHub configuration |
| `records/` | ADRs, plans, postmortems, specs |
| `_shared/` | Cross-domain shared reference files |
| `_archived/` | Deprecated standards retained for history |

## Domains Index

| Subdomain | Path | Content |
|-----------|------|---------|
| CI/CD | `domains/cicd/` | Pipeline patterns, workflow standards |
| Engineering | `domains/engineering/` | Code quality, review, testing standards |
| IaC | `domains/iac/` | OpenTofu module conventions, GCP patterns |
| Operations | `domains/operations/` | Runbooks, incident response, oncall |
| Security | `domains/security/` | Secrets management, SAST, DAST, access control |
| Tooling | `domains/tooling/` | Developer tooling, linting, formatter configs |

## Foundations Index

| Subfolder | Content |
|-----------|---------|
| `foundations/github/` | GitHub org configuration, branch protection, CODEOWNERS |
| `foundations/governance/` | Governance config schemas, law files, validation rule references |

## Records Index

| Subfolder | Content |
|-----------|---------|
| `records/adrs/` | Architecture Decision Records (historical) |
| `records/plans/` | Sprint plans and delivery records |
| `records/postmortems/` | Incident postmortems |
| `records/specs/` | Technical specification snapshots |

> **Active rules** are enforced via `config-engines/metadata-schemas/validation-rules.yml` and `storage-rules.yml`. Files here are reference snapshots only.
