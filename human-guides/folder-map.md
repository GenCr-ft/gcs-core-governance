---
docId: GOV-GUIDE-HG-007
title: Agent vs Human Folder Map
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
# Agent vs Human Folder Map

Shows which folder in `gcs-core-governance` serves each audience and purpose.

## Folder Architecture Diagram

```mermaid
flowchart LR
    subgraph REPO["gcs-core-governance/"]

        subgraph MACHINE["🤖 Machine Layer (AI Agents)"]
            CE["config-engines/\n──────────────\nJSON Schema & YAML\nCanonical rule definitions\n\nDO NOT edit without\na governance ADR"]
            AC["agent-context/\n──────────────\nExtracted protocols (YAML/MD)\nPointer manifests\nAgent bootstrap grounding\n\nREAD for machine-readable\ninstructions"]
        end

        subgraph HUMAN["👤 Human Layer (Contributors)"]
            HG["human-guides/\n──────────────\nMermaid diagrams\nAnnotated tables\nDecision trees\n\nREAD for visual orientation"]
            RL["reference-libraries/\n──────────────\nFROZEN narrative docs\nGodot bible, PCG guidelines\nStudio handbook, DevOps standards\n\nREAD for deep reference\nDO NOT restructure"]
        end

        subgraph DEPRECATED["⚠️ Deprecated"]
            EM["execution-manuals/\n──────────────\nMigrating to agent-context/\nKeep for backward compat\n\nDO NOT add new content"]
        end

    end

    AGENT(["AI Agent\ncold start"]) -->|"Step 1: read\nAGENTS.md"| REPO
    AGENT -->|"Step 2: read\nrules/protocols"| AC
    AGENT -->|"Step 3: validate\nagainst"| CE

    HUMAN_USER(["Human\ncontributor"]) -->|"Orientation"| HG
    HUMAN_USER -->|"Deep reference"| RL

    style CE fill:#dbeafe,stroke:#1d4ed8
    style AC fill:#dbeafe,stroke:#1d4ed8
    style HG fill:#dcfce7,stroke:#16a34a
    style RL fill:#fef3c7,stroke:#d97706
    style EM fill:#fee2e2,stroke:#dc2626
```

## Folder Purpose Table

| Folder | Primary Audience | Content Type | Edit Policy |
|--------|-----------------|-------------|-------------|
| `config-engines/` | AI Agents + Tooling | JSON Schema, YAML rule files | Open governance issue first; PR required |
| `agent-context/` | AI Agents | Extracted protocols, pointer manifests | Update when `config-engines/` changes |
| `human-guides/` | Human Contributors | Mermaid diagrams, annotated tables | Update when `config-engines/` changes |
| `reference-libraries/` | Human Contributors | Long-form narrative Markdown | FROZEN — additive README files only |
| `execution-manuals/` | (Deprecated) | Old agent runbooks | No new content; migrate to `agent-context/` |

## Navigation by Question

| I want to… | Go to… |
|-----------|--------|
| Find the storage routing rule for my document type | `config-engines/metadata-schemas/storage-rules.yml` |
| Understand routing visually without reading YAML | `human-guides/document-routing.md` |
| Get a machine-readable routing table (AI) | `agent-context/protocols/document-routing.md` |
| See the WI lifecycle as a flowchart | `human-guides/wi-lifecycle-flow.md` |
| Get the lifecycle gates in YAML (AI) | `agent-context/protocols/wi-lifecycle-gates.yml` |
| Deep-read Godot 4 patterns | `reference-libraries/godot-bible/` |
| Deep-read operational protocols S1–S20 | `reference-libraries/studio-handbook/01-operational-protocols/` |
| Find all repo prefixes and their purpose | `human-guides/repo-map.md` |
| Bootstrap a new AI agent persona | `agent-context/grounding/agent-bootstrap.md` |
