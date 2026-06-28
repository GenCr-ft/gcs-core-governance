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
| What CLI commands and error paths do I need? | [protocols/ops-runbook.md](protocols/ops-runbook.md) | YAML command ref |

## Navigation — Grounding Questions

| Question | File | Format |
|----------|------|--------|
| What is my identity and operational context? | [grounding/agent-bootstrap.md](grounding/agent-bootstrap.md) | Distilled guide |
| What studio facts do I need? | [grounding/studio-quick-ref.md](grounding/studio-quick-ref.md) | Reference table |
| What engineering constraints apply? | [grounding/technical-constraints.md](grounding/technical-constraints.md) | Constraint table |
| What does this term mean? | [grounding/lexicon.yml](grounding/lexicon.yml) | YAML glossary |
| What is the studio mission and project context? | [grounding/strategic-context.md](grounding/strategic-context.md) | Exec summary |
| Where are the authoritative rule YAML files? | [rules-index.md](rules-index.md) | Pointer manifest |

## Design Principles

1. **No rule duplication** — every rule cites its canonical path in `config-engines/`. Never restates rules inline.
2. **Token budget** — each file targets ≤200 lines. Prefer tables over prose.
3. **Stateless** — each file is self-contained; no cross-file dependencies required for a single question.
4. **Frozen reference-libraries/** — `reference-libraries/` is NOT modified. This layer derives from it.

## Canonical sources

- Machine schemas + rules: `config-engines/metadata-schemas/`
- WI lifecycle contract: `GOV-PROT-003.wi-lifecycle-contract.md`
- Governance scopes: `config-engines/metadata-schemas/governance-config.schema.json`
