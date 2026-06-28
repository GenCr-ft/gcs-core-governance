---
docId: GOV-IDX-001
title: Rules Index — Canonical YAML Source Manifest
version: 1.1.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: reference
  intended-audience: [ai-agents]
  security-classification: l2_confidential
  source_version: "1.1.0"
  last_verified: "2026-06-28"
---
# Rules Index

Authoritative pointer manifest. All enforceable rules live in these YAML/JSON files. Protocol files in `agent-context/` cite these paths — never restate the rules.

## config-engines/metadata-schemas/

| File | Domain | Contents |
|------|--------|----------|
| `repository-catalog.yml` | Repository type catalog | Agent-accessible catalog listing all repositories with `type` field used by GOV_RULE_005 (`target_repository.type`) |
| `storage-rules.yml` | Document routing | 8 storage rules: EXPERIMENTAL, DATA_ARTIFACT, KNOWLEDGE_GOVERNANCE, KNOWLEDGE_HANDBOOK, INFRASTRUCTURE_CODE, PROCESS_DEFINITION, CODE_SHARED_LIBRARY, ASSET_PROJECT |
| `validation-rules.yml` | Document validation | Validation rules applied by the SSoT linter |
| `governance-config.schema.json` | Schema contract | JSON Schema Draft-7 for the resolved governance config object |
| `ontology.yml` | Knowledge ontology | RDF triples, class hierarchy, containment constraints |
| `taxonomy.yml` | Vocabulary taxonomy | SKOS concepts for artifact classes, domains, lifecycles |
| `organizational-entities.yml` | Org catalog | 25 entities: crews, project-teams, departments, gems |
| `governance-scopes.yml` | Scope catalog | governance scope definitions |
| `governance-kpi.yml` | KPIs | 3 governance KPIs with targets, owners, cadence, data-source, report-to, and alert-at fields |

## config-engines/api-parameters/

| File | Domain | Contents |
|------|--------|----------|
| `README.md` | API schema parameters | Placeholder explaining that per-service parameter contract files are pending authorship (see gcs-core-governance#207) |

## config-engines/pipeline-thresholds/

| File | Domain | Contents |
|------|--------|----------|
| `compression-thresholds.yml` | File compression | CLAUDE.md hard limit (200 nb, FAIL) and AGENTS.md soft limit (150 nb, WARN) |
| `coverage-floors.yml` | CI thresholds | Coverage floor pointers — cross-references `agent-context/grounding/technical-constraints.md` for the authoritative 80% unit-test coverage rule; does not restate the value |

## agent-context/grounding/

| File | Domain | Source Doc |
|------|--------|-----------|
| `agent-bootstrap.md` | Agent identity, ethics, escalation | GOV-GUIDE-006, GOV-GUIDE-012 |
| `studio-quick-ref.md` | Terminology, repo map, tech stack, security levels | GOV-GUIDE-412, README |
| `technical-constraints.md` | Engineering + quality constraints table (8 rules) | GOV-GUIDE-017 |
| `lexicon.yml` | Core vocabulary: 15 terms with definitions | GOV-GUIDE-412 §2 |
| `gop-index.yml` | GOP S-number lookup: S1–S20, protocol name, doc path, algorithm cross-ref | GOV-GUIDE-014, 01-operational-protocols/ |
| `strategic-context.md` | Studio mission, Aethel vision, 8 collaboration principles | GOV-GUIDE-414 |
| `gov-guide-001-ssot-contribution.md` | SSoT document structure, contribution workflow, 4 KC&T principles | GOV-GUIDE-001 |

## Key rule evaluation rules

- `storage-rules.yml`: **first-match wins** (top-down evaluation order, stated in file header)
- `validation-rules.yml`: all matching rules applied (cumulative)
- `governance-config.schema.json`: JSON Schema Draft-7 — `$ref` resolution is local (`#/definitions/`)
