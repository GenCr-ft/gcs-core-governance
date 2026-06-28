---
docId: GOV-GUIDE-HG-003
title: Document Storage Routing Decision Tree
version: 1.0.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: guide
  intended-audience: [contributors]
  security-classification: l1_internal
---
# Document Storage Routing Decision Tree

Visual decision tree for routing any artifact to the correct repository. Rules are evaluated top-down; first match wins.

> **Source:** `config-engines/metadata-schemas/storage-rules.yml` (canonical)

## Routing Flowchart

```mermaid
flowchart TD
    START([New artifact to store]) --> Q1{lifecycle-phase\n= experimental?}

    Q1 -- Yes --> R1[🧪 gce-* repo\nExperimental repository]
    Q1 -- No --> Q3{artifact-class\n= infrastructure?}

    Q3 -- Yes --> R3[⚙️ gci-*\nOpenTofu IaC repos]
    Q3 -- No --> Q4{artifact-class\n= process?}

    Q4 -- Yes --> R4[🔄 gcd-shared-actions\nReusable GitHub Actions]
    Q4 -- No --> Q5{artifact-class\n= code\nAND type = library?}

    Q5 -- Yes --> R5[📦 gcl-* repo\nShared library repos]
    Q5 -- No --> Q6{artifact-class\n= asset\nAND scope = project-aethel?}

    Q6 -- Yes --> R6[🎨 gcp-aethel-assets-*\nAethel asset repos]
    Q6 -- No --> Q7{artifact-class = knowledge\nAND domain = governance\nAND category = to-govern?}

    Q7 -- Yes --> R7[📋 gcs-core-governance\nfoundations/governance/]
    Q7 -- No --> Q8{artifact-class = knowledge\nAND domain IN\ngov/ops/legal/marketing/finance?}

    Q8 -- Yes --> R8[📖 gcs-core-governance\nreference-libraries/studio-handbook/sections/{domain}/]
    Q8 -- No --> Q9{artifact-class\n= data?}

    Q9 -- Yes --> R9[📊 gcd-data-*\nData artifact repos]
    Q9 -- No --> R10[❓ No matching rule\nFile governance issue to add one]

    style R9 fill:#d4edda

    style R1 fill:#fff3cd
    style R2 fill:#f8d7da
    style R3 fill:#d1ecf1
    style R4 fill:#d4edda
    style R5 fill:#d4edda
    style R6 fill:#e2d9f3
    style R7 fill:#cce5ff
    style R8 fill:#cce5ff
    style R9 fill:#f8d7da
```

## Rules Reference Table

| Rule ID | Condition | Target | Justification |
|---------|-----------|--------|---------------|
| EXPERIMENTAL_STORAGE_RULE | `lifecycle-phase: experimental` | `gce-*` | Isolates experimental work |
| INFRASTRUCTURE_CODE_STORAGE | `artifact-class: infrastructure` | `gci-*` | IaC centralization |
| PROCESS_DEFINITION_STORAGE | `artifact-class: process` | `gcd-shared-actions` | Workflow centralization |
| CODE_SHARED_LIBRARY_STORAGE | `artifact-class: code` + `type: library` | `gcl-*` | Library convention |
| ASSET_PROJECT_STORAGE | `artifact-class: asset` + `scope: project-aethel` | `gcp-aethel-assets-*` | Asset isolation |
| KNOWLEDGE_GOVERNANCE_STORAGE | knowledge + governance + to-govern | `gcs-core-governance/foundations/governance/` | Laws with configs |
| KNOWLEDGE_HANDBOOK_STORAGE | knowledge + ops/legal/marketing domains | `gcs-core-governance/reference-libraries/studio-handbook/sections/{domain}/{docId}.{title_kebab_case}.md` | Operational centralization |
| DATA_ARTIFACT_STORAGE | `artifact-class: data` | `gcd-data-*` → `datasets/{domain}/` | Data centralization |

> **Rule evaluation is sequential.** A document matching multiple conditions stops at the FIRST matching rule (top of table wins).
