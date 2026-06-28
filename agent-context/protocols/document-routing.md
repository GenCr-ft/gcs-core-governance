---
docId: GOV-PROTO-DR-001
title: Document Routing Protocol
version: 1.0.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: protocol
  intended-audience: [ai-agents]
  security-classification: l2_confidential
  source_version: "1.0.0"
  last_verified: "2026-06-28"
---
# Document Routing Protocol

Extracted from `config-engines/metadata-schemas/storage-rules.yml` (first-match wins, top-down).
**Do not restate rules here** — cite the canonical path. This table is a navigation aid.

## Storage Routing Decision Table

| Rule ID | Condition (exact YAML field syntax from storage-rules.yml) | Target |
|---------|-----------|--------|
| `EXPERIMENTAL_STORAGE_RULE` | `metadata.lifecycle-phase: "experimental"` | repo prefix `gce-` |
| `SECURITY_SECRET_STORAGE` | `security-classification: "l3_secret"` | `gcs-vault-critical` |
| `KNOWLEDGE_GOVERNANCE_STORAGE` | `artifact-class: "knowledge"` + `domain: ["governance","engineering-and-architecture"]` + `classification.category: "to-govern"` | `gcs-core-governance` → `foundations/governance/{classification.type}/{docId}.md` |
| `KNOWLEDGE_HANDBOOK_STORAGE` | `artifact-class: "knowledge"` + `domain: ["governance","production-management","marketing-and-communication","legal","finance-and-hr"]` + `classification.category: ["to-instruct","to-inform","to-record","to-define"]` | `gcs-core-governance` → `reference-libraries/studio-handbook/sections/{domain}/{docId}.{title_kebab_case}.md` |
| `INFRASTRUCTURE_CODE_STORAGE` | `artifact-class: "infrastructure"` | repo prefix `gci-` |
| `PROCESS_DEFINITION_STORAGE` | `artifact-class: "process"` | `gcd-shared-actions` |
| `CODE_SHARED_LIBRARY_STORAGE` | `artifact-class: "code"` + `code-classification.type: "library"` | repo prefix `gcl-` |
| `ASSET_PROJECT_STORAGE` | `artifact-class: "asset"` + `scope: "project-aethel"` | repo prefix `gcp-aethel-assets-` |
| `DATA_ARTIFACT_STORAGE` | `artifact-class: "data"` | repo prefix `gcd-data-` → `datasets/{domain}/{docId}.{title_kebab_case}` |
| *(no match)* | None of the above rules matched | ⚠ File issue in `gcs-core-governance` — no routing rule defined for this artifact |

**Canonical source:** `config-engines/metadata-schemas/storage-rules.yml`

## Knowledge Guardian Assignments

For agents following Algorithm 1 (collaboration-algorithms.md): the table below maps governance document types to their assigned knowledgeGuardian. Use this to assign reviewers without reading individual protocol files or reference-libraries/.

| Domain | doc-type | knowledgeGuardian | GemID |
|--------|----------|-------------------|-------|
| governance | protocol | Orion | GCT-UTL-SLG-001 |
| governance | standard | Iris | GCT-UTL-RWSKA-001 |
| governance | reference | Iris | GCT-UTL-RWSKA-001 |

**Canonical source:** `reference-libraries/devops-standards/foundations/governance/GOV-REFE-001.studio-directory--knowledge-guardians.md`

## Validation Rules Quick Reference

Rules are cumulative (all matching rules apply). **Canonical source:** `config-engines/metadata-schemas/validation-rules.yml`

| Rule ID | Applies when | Enforcement |
|---------|-------------|-------------|
| `GOV_RULE_001` | knowledge + to-govern + domain=legal | required_reviewers: Henri |
| `GOV_RULE_002` | knowledge + type=standard + domain=engineering-and-architecture | required_reviewers: Isaac |
| `GOV_RULE_003` | knowledge + type=policy + domain=security-and-compliance | required_approvers: Cerberus |
| `GOV_RULE_004` | lifecycle-phase=deprecated | required_frontmatter: deprecation_justification |
| `GOV_RULE_005` | pull_request on code repo | body must contain: "References Definition of Done (PRO-STAN-001)" |
| `GOV_RULE_006` | type=contract + domain=legal | required_frontmatter: expiration_date + reviewer: Henri |

## Routing Decision Flowchart

```mermaid
flowchart TD
    A[New artifact to route] --> B{lifecycle-phase = experimental?}
    B -- Yes --> C[gce-* repo]
    B -- No --> SEC{security-classification = l3_secret?}
    SEC -- Yes --> L[gcs-vault-critical]
    SEC -- No --> D{artifact-class?}
    D -- infrastructure --> E[gci-* repo]
    D -- process --> F[gcd-shared-actions]
    D -- asset + project-aethel --> G[gcp-aethel-assets-*]
    D -- code + library --> H[gcl-* repo]
    D -- knowledge --> I{classification.category?}
    I -- to-govern + domain=governance/engineering-and-architecture --> J[gcs-core-governance/foundations/governance/]
    I -- to-instruct/inform/record/define --> K[gcs-core-governance/reference-libraries/studio-handbook/sections/{domain}/]
    D -- data --> N[gcd-data-* repo]
    D -- no match --> M[⚠ Escalate: file issue in gcs-core-governance\nNo routing rule matched]
```
