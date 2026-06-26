---
docId: GOV-GUIDE-HG-005
title: Validation Rules Summary
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
# Validation Rules Summary

Human-readable annotated summary of all active studio validation rules.

> **Source:** `config-engines/metadata-schemas/validation-rules.yml` (canonical — this file is a visual summary only)

## Rules at a Glance

```mermaid
flowchart LR
    DOC[Your document or PR]

    DOC --> R1{Legal knowledge\ndomain = legal?}
    DOC --> R3{Security policy\ndomain = security?}
    DOC --> R4{lifecycle-phase\n= deprecated?}
    DOC --> R5{Event = PR\non a code repo?}
    DOC --> R6{Contract\ndomain = legal?}

    R1 -- Yes --> A1[Requires reviewer:\nHenri - Legal Counsel]
    R3 -- Yes --> A3[Requires approver:\nCerberus - Security Officer]
    R4 -- Yes --> A4[Must have\ndeprecation_justification\nin frontmatter]
    R5 -- Yes --> A5[PR body must contain:\nReferences Definition of Done]
    R6 -- Yes --> A6[Must have expiration_date\n+ Henri reviewer]

    style A1 fill:#fff3cd
    style A3 fill:#f8d7da
    style A4 fill:#d1ecf1
    style A5 fill:#d4edda
    style A6 fill:#f8d7da
```

## Annotated Rules Table

| Rule ID | Applies When | Enforcement | Who Approves | Frontmatter Required |
|---------|-------------|-------------|--------------|---------------------|
| GOV_RULE_001 | Knowledge doc + domain=legal + category=to-govern | PR review gate | Henri (Legal Counsel) | — |
| GOV_RULE_002 | Knowledge doc + type=standard + domain=engineering | PR review gate | Isaac (Senior Architect) | — |
| GOV_RULE_003 | Knowledge doc + type=policy + domain=security | PR approval gate | Cerberus (Security Officer) | — |
| GOV_RULE_004 | Any artifact with `lifecycle-phase: deprecated` | SSoT linter CI | — | `deprecation_justification:` |
| GOV_RULE_005 | Pull Request on a code repository | PR body check | — | PR body must include `"References Definition of Done (PRO-STAN-001)"` |
| GOV_RULE_006 | Knowledge doc + type=contract + domain=legal | PR review + frontmatter | Henri (Legal Counsel) | `expiration_date:` |

## What Triggers a Validation Failure?

| Scenario | Rule Triggered | Fix |
|----------|---------------|-----|
| New security policy PR merged without Cerberus approval | GOV_RULE_003 | Add Cerberus as required reviewer |
| Deprecated doc missing justification | GOV_RULE_004 | Add `deprecation_justification: "Replaced by {docId}"` |
| PR to a code repo body has no DoD reference | GOV_RULE_005 | Add `References Definition of Done (PRO-STAN-001)` to PR body |
| Legal contract doc missing expiry | GOV_RULE_006 | Add `expiration_date: "YYYY-MM-DD"` to frontmatter |

## Enforcement Layers

Rules are enforced at two layers:

1. **CI (GitHub Actions)** — `gcd-ops-scripts` SSoT linter runs on every PR targeting main
2. **Pre-commit hook** — locally installed via `./onboard.sh` in each repo

> If a validation fails in CI but you believe it is a false positive, open an issue in `gcs-core-governance` with label `governance`.
