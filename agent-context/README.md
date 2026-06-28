---
docId: GOV-READ-008
title: agent-context — Machine-Readable Protocol Layer
version: 1.0.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: readme
  intended-audience: [ai-agents]
  security-classification: l2_confidential
---
# agent-context/

Machine-readable protocol layer for AI agents operating in GenCr@ft Studio. Read this folder instead of `reference-libraries/` — it contains dense, structured extractions that answer operational questions directly.

## Navigation — Protocol Questions

| Question | File | Format |
|----------|------|--------|
| How do I route a document to the correct repo? | [protocols/document-routing.md](protocols/document-routing.md) | Decision table + flowchart |
| What are the WI lifecycle gate requirements? | [protocols/wi-lifecycle-gates.yml](protocols/wi-lifecycle-gates.yml) | YAML |
| What collaboration algorithm should I follow? | [protocols/collaboration-algorithms.md](protocols/collaboration-algorithms.md) | Numbered steps |
| What does GOP S-number Sn cover? | [protocols/gop-s-number-index.md](protocols/gop-s-number-index.md) | Lookup table |
| What CLI commands and error paths do I need? | [protocols/ops-runbook.md](protocols/ops-runbook.md) | YAML command ref |

## Navigation — Grounding Questions

| Question | File | Format |
|----------|------|--------|
| What is my identity and operational context? | [grounding/agent-bootstrap.md](grounding/agent-bootstrap.md) | Distilled guide |
| What studio facts do I need? | [grounding/studio-quick-ref.md](grounding/studio-quick-ref.md) | Reference table |
| What engineering constraints apply? | [grounding/technical-constraints.md](grounding/technical-constraints.md) | Constraint table |
| What does this term mean? | [grounding/lexicon.yml](grounding/lexicon.yml) | YAML glossary |
| What does GOP S-number Sn mean? Where is its document? | [grounding/gop-index.yml](grounding/gop-index.yml) | YAML lookup table |
| What is the studio mission and project context? | [grounding/strategic-context.md](grounding/strategic-context.md) | Exec summary |
| Where are the authoritative rule YAML files? | [rules-index.md](rules-index.md) | Pointer manifest |

## Folder Architecture

Complete folder-purpose table for `gcs-core-governance`. Use this to determine which layer to read or write.

| Folder | Primary Audience | Content Type | Edit Policy |
|--------|-----------------|-------------|-------------|
| `config-engines/` | AI Agents + Tooling | JSON Schema, YAML rule files | Open governance issue first; PR required |
| `agent-context/` | AI Agents | Extracted protocols, pointer manifests | Update when `config-engines/` changes |
| `human-guides/` | Human Contributors | Mermaid diagrams, annotated tables | Update when `config-engines/` changes |
| `reference-libraries/` | Human Contributors | Long-form narrative Markdown | FROZEN — additive README files only |
| `execution-manuals/` | (Deprecated) | Old agent runbooks | No new content; migrate to `agent-context/` |

## Design Principles

1. **No rule duplication** — every rule cites its canonical path in `config-engines/`. Never restates rules inline.
2. **Token budget** — each file targets ≤200 lines. Prefer tables over prose.
3. **Stateless** — each file is self-contained; no cross-file dependencies required for a single question.
4. **Migrated from execution-manuals/** — `execution-manuals/` is deprecated and its content is migrating into this layer. Source files originate there (e.g., `execution-manuals/onboard-manuals/GOV-GUIDE-006.gasai-v2.0-ai-agent-grounding-bootstrap.md` → `grounding/agent-bootstrap.md`). `reference-libraries/` is a separate frozen human-oriented docs folder unrelated to agent-context provenance.

## Canonical sources

- Machine schemas + rules: `config-engines/metadata-schemas/`
- WI lifecycle contract: `GOV-PROT-003.wi-lifecycle-contract.md`
- Governance scopes: `config-engines/metadata-schemas/governance-config.schema.json`
