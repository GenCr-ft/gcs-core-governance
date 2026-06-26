---
docId: GOV-GUIDE-HG-004
title: SSoT Document Naming Cheatsheet
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
# SSoT Document Naming Cheatsheet

Quick reference for naming SSoT documents correctly. Every document ID (`docId`) follows the same pattern.

> **Source:** `config-engines/metadata-schemas/taxonomy.yml` (canonical)

## docId Anatomy

```
  ENG  -  SPEC  -  008
   │        │       │
   │        │       └── Three-digit sequence (001, 002 … 999)
   │        └────────── Document type code (see table below)
   └─────────────────── Domain code (see table below)
```

**Full docId format:** `{DOMAIN}-{TYPE}-{NNN}`

**Filename format:** `{docId}.{title-kebab-case}.md`

**Example:** `ENG-SPEC-008.hexagonal-ports-and-adapters.md`

## Domain Codes

| Code | Domain | Used In |
|------|--------|---------|
| `GOV` | Governance | `gcs-core-governance` |
| `ENG` | Engineering & Architecture | `gcs-engineering-handbook`, `gcp-aethel-architecture` |
| `GAM` | Game Design | `gcp-aethel-docs-gdd` |
| `ART` | Art & Audio | `gcs-studio-handbook` |
| `OPS` | Operations & Management | `gcs-project-management` |
| `SEC` | Security | `gcs-security-core` |
| `PCG` | Procedural Generation | `gcp-aethel-pcg` |
| `PLT` | Platform | `gcs-plt-*` repos |

## Document Type Codes

| Code | Type | Category | Example |
|------|------|----------|---------|
| `SPEC` | Specification | to-describe | `ENG-SPEC-001` |
| `STAN` | Standard | to-govern | `ENG-STAN-002` |
| `GUIDE` | Guide | to-instruct | `GOV-GUIDE-006` |
| `PLAY` | Playbook | to-instruct | `OPS-PLAY-001` |
| `ADR` | Architecture Decision Record | to-record | `ENG-ADR-070` |
| `PROT` | Protocol | to-instruct | `GOV-PROT-003` |
| `PLAN` | Plan | to-plan | `ENG-PLAN-001` |
| `POST` | Postmortem | to-record | `OPS-POST-001` |
| `POL` | Policy | to-govern | `SEC-POL-001` |
| `BACK` | Backlog entry | to-describe | `ENG-BACK-001` |
| `STAN` | Standard | to-govern | `GOV-STAN-001` |
| `OVER` | Overview | to-describe | `ENG-OVER-001` |
| `READ` | README / Navigation index | to-inform | `GOV-READ-001` |

## Frontmatter Template

Every SSoT document must include this YAML frontmatter:

```yaml
---
docId: {DOMAIN}-{TYPE}-{NNN}        # e.g. ENG-SPEC-008
title: Human-readable title
version: 1.0.0
authors: [Author Name or Gem ID]
metadata:
  lifecycle-stage: draft            # draft | proposed | approved | deprecated
  scope: studio                     # studio | project-aethel | etc.
  domain: engineering               # matches domain code above (lowercase)
  doc-type: specification           # matches type (lowercase)
  intended-audience: [contributors] # ai-agents | contributors | governance-team
  security-classification: l1_internal  # l0_public | l1_internal | l2_confidential | l3_secret
---
```

## Common Mistakes

| ❌ Wrong | ✅ Correct |
|---------|----------|
| `tags: [governance, standard]` | `metadata.keywords: [governance, standard]` (`tags:` is deprecated) |
| Relative link `../other.md` that doesn't resolve | Verify link before committing |
| `lifecycle-stage: active` | `lifecycle-stage: approved` (not "active") |
| `doc-type: Specification` | `doc-type: specification` (lowercase) |
| Missing `security-classification` | Required field — use `l1_internal` as default if unsure |
