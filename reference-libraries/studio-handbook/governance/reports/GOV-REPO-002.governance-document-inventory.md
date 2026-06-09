---
docId: GOV-REPO-002
title: 'Governance Document Inventory – Studio Constitution Baseline'
version: 1.0.0
creation_date: '2025-02-14'
last_updated_date: '2026-06-02'
authors:
  - Iris (GCT-UTL-RWSKA-001)
knowledgeGuardian:
  - Iris (GCT-UTL-RWSKA-001)
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/governance/reports/GOV-REPO-002.governance-document-inventory.md
metadata:
  domain: governance
  lifecycle-stage: draft
  scope: studio
  doc-type: report
  security-classification: l2_confidential
---

# Governance Document Inventory – Studio Constitution Baseline

## 1. Purpose
This report satisfies Issue #28 by cataloging every governance-tagged document (`docId` starting with `GOV-`) that currently lives in the `gcs-core-governance` repository. It provides a single reference point before the Studio Constitution is drafted, clarifies what exists, and highlights structural overlaps or gaps.

## 2. Methodology
1. **Scope filter:** Programmatically listed every file path containing `GOV-` to avoid missing nested folders.
2. **Metadata capture:** Pulled each document’s `docId`, `title`, and storage path directly from front-matter to maintain traceability.
3. **Categorization:** Grouped artifacts into four clusters—Foundational Vision & Policy, Knowledge & SSoT Governance, AI/Automation Governance, and Oversight & Remediation—to mirror the eventual constitutional pillars.
4. **Validation:** Spot-checked document contents to summarize their governance focus areas and to flag anomalies (e.g., `docId` collisions).

## 3. Inventory at a Glance
| Category | Description | Count |
| --- | --- | --- |
| Foundational Vision & Policy | Studio culture, charters, and normative policies that define expected behavior. | 9 |
| Knowledge & SSoT Governance | Guides that regulate documentation quality, KB domains, and SSoT remediation. | 12 |
| AI & Automation Governance | Operational playbooks for Gems, AI ethics implementation, and SSoT automation scaffolding. | 8 |
| Oversight, Remediation & Proposals | Audit crews, investigative reports, and governance-change proposals. | 5 |
| **Total** | **All governance-labeled artifacts currently in repo.** | **34** |

## 4. Detailed Inventory

### 4.1 Foundational Vision & Policy (9 docs)
| docId | Title | Governance focus | Repository path |
| --- | --- | --- | --- |
| GOV-GUIDE-007 | Gencraft Studio - Knowledge Guardian Charter | Defines mandate, responsibilities, and escalation paths for knowledge guardians maintaining the SSoT. | `02-knowledge-base-hub/GOV-GUIDE-007.knowledge-management-and-contribution-guide.md` |
| GOV-GUIDE-008 | Guiding Principles for Knowledge Management & Traceability (KC&T) | Establishes KC&T philosophy, doc taxonomy expectations, and traceability guardrails. | `00-studio-vision-and-principles/GOV-GUIDE-008.kcandt-guiding-principles.md` |
| GOV-GUIDE-013 | Studio Culture and Values | Codifies shared studio values and conduct expectations that inform governance tone. | `00-studio-vision-and-principles/GOV-GUIDE-013.studio-culture-and-values.md` |
| GOV-GUIDE-016 | Governance Crew Charter | Details Governance Crew composition, decision rights, and oversight rituals. | `00-studio-vision-and-principles/GOV-GUIDE-016.governance-crew-charter.md` |
| GOV-GUIDE-411 | Organization and Roles | Maps the overall studio org structure, role responsibilities, and governance touchpoints. | `00-studio-vision-and-principles/GOV-GUIDE-411.organization-and-roles.md` |
| GOV-GUIDE-413 | AI Enablement Team Charter | Defines the AI Enablement crew’s scope, tooling authority, and cross-team governance duties. | `00-studio-vision-and-principles/GOV-GUIDE-413.ai-enablement-team-charter.md` |
| GOV-POLICY-001 | Code of Conduct | Sets behavioral expectations and enforcement levers for all studio participants. | `00-studio-vision-and-principles/GOV-POLICY-001.code-of-conduct.md` |
| GOV-POLICY-002 | AI Ethics Guidelines | Translates ethical AI principles into actionable studio standards. | `00-studio-vision-and-principles/GOV-POLICY-002.ai-ethics-guidelines.md` |
| GOV-POLICY-003 | Universal Gem Operating Principles | Provides baseline operating principles for Gem agents, including compliance obligations. | `00-studio-vision-and-principles/GOV-POLICY-003.universal-gem-operating-principles.md` |

### 4.2 Knowledge & SSoT Governance (12 docs)
| docId | Title | Governance focus | Repository path |
| --- | --- | --- | --- |
| GOV-GUIDE-007 | Knowledge Base Contribution and Style Guide | Enforces structure, metadata, and editorial process for KB submissions. | `02-knowledge-base-hub/GOV-GUIDE-007.knowledge-management-and-contribution-guide.md` |
| GOV-GUIDE-400 | KB: Art Direction and Style Guides | Domain-specific KB governance for art pipelines and approvals. | `02-knowledge-base-hub/GOV-GUIDE-400.kb-domain-art-direction.md` |
| GOV-GUIDE-401 | Audio Design Principles and Assets | Audio KB governance, asset standards, and approval flows. | `02-knowledge-base-hub/GOV-GUIDE-401.kb-domain-audio-design.md` |
| GOV-GUIDE-402 | DevOps, Infrastructure, and CI/CD | KB governance for DevOps standards, runbooks, and automation artifacts. | `02-knowledge-base-hub/GOV-GUIDE-402.kb-domain-devops-infra.md` |
| GOV-GUIDE-403 | Game Universe and Lore | Lore governance and canon control for narrative KB assets. | `02-knowledge-base-hub/GOV-GUIDE-403.kb-domain-game-universe.md` |
| GOV-GUIDE-404 | Gem AI Management and Evolution | Governs Gem lifecycle documentation, upgrades, and knowledge routing. | `02-knowledge-base-hub/GOV-GUIDE-404.kb-domain-gem-ai-management.md` |
| GOV-GUIDE-405 | Marketing, Sales, and Legal | Defines KB governance for GTM, brand, and legal assets. | `02-knowledge-base-hub/GOV-GUIDE-405.kb-domain-marketing-sales-legal.md` |
| GOV-GUIDE-406 | Product and Game Design | Product/game design KB governance, blueprint hygiene, and approval states. | `02-knowledge-base-hub/GOV-GUIDE-406.kb-domain-product-game-design.md` |
| GOV-GUIDE-407 | Quality Assurance and Testing | QA KB governance, defect taxonomy alignment, and readiness criteria. | `02-knowledge-base-hub/GOV-GUIDE-407.kb-domain-qa-testing.md` |
| GOV-GUIDE-408 | Technical Documentation Standards | Governs technical doc structure, diagrams, and verification requirements. | `02-knowledge-base-hub/GOV-GUIDE-408.kb-domain-technical-docs.md` |
| GOV-GUIDE-409 | UX/UI Design Principles and Guidelines | UX/UI KB governance and design system traceability. | `02-knowledge-base-hub/GOV-GUIDE-409.kb-domain-ux-ui-design.md` |
| GOV-GUIDE-410 | Watch, Research, and Feedback Management | Governs research repositories, watch data, and feedback loops. | `02-knowledge-base-hub/GOV-GUIDE-410.kb-domain-watch-research-feedback.md` |
| GOV-PRIN-001 | SSoT Documentation Principles | Cross-domain principles for writing, validating, and classifying SSoT artifacts. | `02-knowledge-base-hub/GOV-PRIN-001.ssot-documentation-principles.md` |

### 4.3 AI & Automation Governance (8 docs)
| docId | Title | Governance focus | Repository path |
| --- | --- | --- | --- |
| GOV-GUIDE-001 | SSoT Contributor Guide: Knowledge Management | Sets expectations for AI/Human contributors interacting with SSoT assets. | `ai-operational-guides/grounding-docs/GOV-GUIDE-001.ssot-contributor-guide-knowledge-management.md` |
| GOV-GUIDE-006 | GASAI v2.0: AI Agent Grounding Bootstrap | Defines AI agent onboarding, safety constraints, and operational baselines. | `ai-operational-guides/GOV-GUIDE-006.gasai-v2.0-ai-agent-grounding-bootstrap.md` |
| GOV-GUIDE-012 | Gencraft Agent Charter: Identity, Roles, and Ethics | Clarifies Gem identity, allowable actions, and ethical boundaries. | `ai-operational-guides/grounding-docs/GOV-GUIDE-012.gencraft-agent-charter-identity-roles-and-ethics.md` |
| GOV-GUIDE-014 | Operational Playbook: Core Collaboration Algorithms | Describes escalation algorithms, hand-offs, and collaboration etiquette for Gems. | `ai-operational-guides/grounding-docs/GOV-GUIDE-014.operational-playbook-core-collaboration-algorithms.md` |
| GOV-GUIDE-017 | Unified Technical Standard: Engineering and Quality | Captures unified engineering QA rules that AI tooling must enforce. | `ai-operational-guides/grounding-docs/GOV-GUIDE-017.unified-technical-standard-engineering-and-quality.md` |
| GOV-GUIDE-412 | Studio Reference: Core Lexicon & Capabilities | Provides canonical lexicon/capability mapping for AI reasoning. | `ai-operational-guides/grounding-docs/GOV-GUIDE-412.studio-reference-core-lexicon--capabilities.md` |
| GOV-GUIDE-414 | Studio Strategic Context | Aligns AI actions with studio strategy, constraints, and risk posture. | `ai-operational-guides/grounding-docs/GOV-GUIDE-414.studio-strategic-context.md` |
| GOV-CATALOG-006 | The SSoT Map: Repository Structure & Navigation | Catalogues repository topology for AI navigators to respect governance boundaries. | `ai-operational-guides/grounding-docs/GOV-CATALOG-006.the-ssot-map-repository-structure--navigation.md` |

### 4.4 Oversight, Remediation & Proposals (5 docs)
| docId | Title | Governance focus | Repository path |
| --- | --- | --- | --- |
| GOV-CHAR-002 | Knowledge Audit Crew Charter | Establishes the Knowledge Audit Crew, its audit scope, and reporting obligations. | `governance/charters/GOV-CHAR-002.knowledge-audit-crew-charter.md` |
| GOV-REPO-001 | From Chaos to Constitution: The SSoT Remediation Journey | Documents the historical audit that triggered the constitution effort. | `governance/reports/GOV-REPO-001.from-chaos-to-constitution.md` |
| GOV-REPO-002 | Governance Document Inventory – Studio Constitution Baseline | **This report—serves as the authoritative inventory baseline.** | `governance/reports/GOV-REPO-002.governance-document-inventory.md` |
| GOV-PROP-001 | Decision Record: Standardized Metadata and Tagging Policy | Captures the policy proposal that defined metadata/tagging SSoT rules. | `proposals/GOV-PROP-001.decision-record-standardized-metadata-and-tagging-policy.md` |
| GOV-GUIDE-101 | SSoT Remediation Guide: From Error to Compliance | Provides hands-on remediation playbook for fixing governance lint errors. | `sections/governance/GOV-GUIDE-101.ssot-remediation-guide.md` |

## 5. Key Observations for Constitution Authors
1. **Extensive KB governance, limited constitutional glue:** Eleven KB domain guides plus `GOV-PRIN-001` and `GOV-GUIDE-101` articulate operational discipline, but nothing currently unifies them into a single declarative law.
2. **Role charter saturation without hierarchy synthesis:** Multiple charters (`GOV-GUIDE-007`, `016`, `413`, `GOV-CHAR-002`) define responsibilities, yet there is no canonical hierarchy or conflict-resolution doctrine to arbitrate overlaps.
3. **`docId` collision resolved — GOV-GUIDE-415 removed (ghost entry):** The KB Watch guide retains `GOV-GUIDE-410`. `GOV-GUIDE-415` (GASAI v1.0 actionable guide, formerly `GOV-GUIDE-410`) was never committed as a file and has been superseded by `GOV-GUIDE-006` (GASAI v2.0). The inventory row for `GOV-GUIDE-415` has been removed.
4. **AI governance is advanced but siloed:** AI-focused documents are comprehensive, yet they mostly exist in the `ai-operational-guides/` tree, separate from human governance; the Constitution must bridge these practices so human and AI actors share a single rulebook.
5. **Change control mechanisms are sparse:** Aside from `GOV-PROP-001`, there is little procedural guidance on how governance artifacts evolve, suggesting the Constitution should formalize amendment pathways.

This inventory should be treated as the authoritative baseline—any future governance artifact must append itself here (or update this report) to maintain constitutional traceability.
