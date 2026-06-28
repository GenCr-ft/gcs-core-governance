---
docId: GOV-GRND-001-SSOT
title: SSoT Contribution — Agent-Context Extraction
version: 1.0.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: guide
  intended-audience: [ai-agents]
  security-classification: l2_confidential
  source_version: "2.0.0"
  last_verified: "2026-06-27"
---
# SSoT Contribution — Agent-Context Extraction

Extracted from GOV-GUIDE-001 v2.0.0. Full document at `reference-libraries/studio-handbook/ai-operational-guides/grounding-docs/GOV-GUIDE-001.ssot-contributor-guide-knowledge-management.md`.

## Four KC&T Principles

| # | Principle | Rule |
|---|-----------|------|
| 1 | Single Source of Truth | Trust only designated SSoT Git repositories. Never use unofficial copies. |
| 2 | Quality & Reliability | Use documents with `lifecycle-stage: approved` and the latest `version`. Report outdated or incorrect information immediately. |
| 3 | Traceability | Every change must link to a GitHub Issue. Document decisions. |
| 4 | Structured, Machine-Readable Data | All docs MUST use YAML frontmatter with the mandatory `metadata` block. |

## Mandatory Document Structure

Every Markdown document you create or edit MUST have:

```yaml
---
docId: DOMAIN-TYPE-CODE        # unique ID, e.g. GOV-GUIDE-001
title: ...
version: MAJOR.MINOR.PATCH
authors: [...]
metadata:
  scope: studio | project-aethel
  domain: governance | engineering | ...
  doc-type: standard | guide | playbook | ...
  lifecycle-stage: approved | draft | deprecated
  security-classification: l0_public | l1_internal | l2_confidential | l3_secret
  keywords: [optional, list]   # replaces deprecated `tags` field
---
```

- `tags` is **deprecated** — use `metadata.keywords` instead.
- Do not skip heading levels (e.g., `##` → `####` is forbidden).

## Contribution Workflow (Mandatory)

1. **Track:** Open a GitHub Issue before making any change.
2. **Isolate:** Create a new Git branch.
3. **Write:** Apply all KC&T principles and mandatory structure above.
4. **Review:** Open a PR and assign the `knowledgeGuardian` as reviewer.
5. **Finalize:** Incorporate feedback; the `knowledgeGuardian` merges.

## Key Agent

| Role | GemID | Responsibility |
|------|-------|----------------|
| Knowledge Guardian | Iris (GCT-UTL-RWSKA-001) | Approves + merges all SSoT document changes |
