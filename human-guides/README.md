---
docId: GOV-GUIDE-HG-001
title: human-guides — Entry Point
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
# human-guides/

Visual and diagram-enriched governance guides for **human contributors** at GenCr@ft Studio. Every guide is self-contained, links to its canonical YAML source, and renders on GitHub without any tooling.

> **AI Agents:** Use [`agent-context/`](../agent-context/) instead — this folder is optimized for humans, not token-efficient machine parsing.

## Navigation Table

| Question | Guide |
|----------|-------|
| How does a Work Item move through its lifecycle? | [wi-lifecycle-flow.md](wi-lifecycle-flow.md) |
| Which repo should I put my document in? | [document-routing.md](document-routing.md) |
| How do I name my SSoT document? | [ssot-naming-cheatsheet.md](ssot-naming-cheatsheet.md) |
| What validation rules apply to my document? | [validation-rules-summary.md](validation-rules-summary.md) |
| Which repos exist and what do they do? | [repo-map.md](repo-map.md) |
| Where do agents read from vs where do humans read from? | [folder-map.md](folder-map.md) |

## Audience

These guides are for:
- **New contributors** getting oriented to studio governance
- **Reviewers** checking document compliance
- **Studio leads** explaining processes to new team members

They are **not** the authoritative source — changes to rules must go in `config-engines/*.yml` first; these guides are updated as a follow-on step.

## Source of Truth

All rules visualized here are derived from:

| Source file | Content |
|-------------|---------|
| `config-engines/metadata-schemas/storage-rules.yml` | Document routing rules |
| `config-engines/metadata-schemas/validation-rules.yml` | Validation rules |
| `config-engines/metadata-schemas/taxonomy.yml` | Vocabulary and doc type codes |
| `GOV-PROT-003.wi-lifecycle-contract.md` | WI lifecycle gate definitions |
