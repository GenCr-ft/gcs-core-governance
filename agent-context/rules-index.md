---
docId: GOV-RULES-IDX-001
title: Rules Index — Canonical YAML Source Manifest
version: 1.0.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: reference
  intended-audience: [ai-agents]
  security-classification: l2_confidential
---
# Rules Index

Authoritative pointer manifest. All enforceable rules live in these YAML/JSON files. Protocol files in `agent-context/` cite these paths — never restate the rules.

## config-engines/metadata-schemas/

| File | Domain | Contents |
|------|--------|----------|
| `storage-rules.yml` | Document routing | 8 storage rules: EXPERIMENTAL, KNOWLEDGE_GOVERNANCE, KNOWLEDGE_HANDBOOK, INFRASTRUCTURE_CODE, PROCESS_DEFINITION, CODE_SHARED_LIBRARY, ASSET_PROJECT, SECURITY_SECRET |
| `validation-rules.yml` | Document validation | Validation rules applied by the SSoT linter |
| `governance-config.schema.json` | Schema contract | JSON Schema Draft-7 for the resolved governance config object |
| `ontology.yml` | Knowledge ontology | RDF triples, class hierarchy, containment constraints |
| `taxonomy.yml` | Vocabulary taxonomy | SKOS concepts for artifact classes, domains, lifecycles |
| `organizational-entities.yml` → `reference-libraries/devops-standards/foundations/governance/catalogs/` | Org catalog | 25 entities: crews, project-teams, departments, gems |
| `governance-scopes.yml` → `reference-libraries/devops-standards/foundations/governance/catalogs/` | Scope catalog | governance scope definitions |
| `governance-kpi.yml` | KPIs | 3 governance KPIs with targets |

## config-engines/api-parameters/

| File | Domain | Contents |
|------|--------|----------|
| *(see directory listing)* | API schema parameters | Per-service parameter contracts |

## config-engines/pipeline-thresholds/

| File | Domain | Contents |
|------|--------|----------|
| *(see directory listing)* | CI thresholds | Coverage floors, lint budgets |

## Key rule evaluation rules

- `storage-rules.yml`: **first-match wins** (top-down evaluation order, stated in file header)
- `validation-rules.yml`: all matching rules applied (cumulative)
- `governance-config.schema.json`: JSON Schema Draft-7 — `$ref` resolution is local (`#/definitions/`)
