---
docId: GOV-PROP-001
title: 'Decision Record: Standardized Metadata and Tagging Policy'
version: 1.0.0
creation_date: '2025-06-17'
last_updated_date: '2026-05-20'
authors:
- Governance Crew
metadata:
  scope: studio
  domain: governance
  doc-type: proposal
  keywords:
  - ssot
  - metadata
  - tagging
  - decision-record
  lifecycle-stage: approved
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/proposals/GOV-PROP-001.decision-record-standardized-metadata-and-tagging-policy.md
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)
---
# Decision Record: Standardized Metadata and Tagging Policy

## 1. Summary

This document records the formal decision to adopt a new, structured metadata system for all SSoT documents. This system replaces the legacy free-form `tags:` field with a governed, multi-faceted `metadata:` block. The goal is to dramatically improve the consistency, discoverability, and machine-readability of our entire knowledge base.

## 2. Justification

The legacy free-form `tags:` system led to inconsistencies (e.g., `devops` vs. `infra`), making it unreliable for search and automation. The newly adopted standardized system is necessary to:

- **Ensure Consistency:** Guarantee that similar documents are categorized in the same way.
- **Enable Powerful Automation:** Allow AI Gems to reliably filter, process, and generate reports based on precise document attributes.
- **Improve Discoverability:** Facilitate precise and faceted search for all studio members.
- **Guide Contributors:** Provide a clear structure for authors to categorize their documents, reducing ambiguity.

## 3. Adopted Solution: The Stratified Metadata System

Following a successful review, the studio has adopted the stratified metadata system. This approach combines the rigor of a controlled dictionary with the flexibility of free keywords.

- **Deprecation of `tags:`:** The existing `tags:` list is officially deprecated.
- **Introduction of `metadata:`:** A new `metadata:` block is now mandatory in all SSoT document frontmatters.
- **Official Standard:** The structure and rules for this block are formally defined in the new standard **`GOV-STANDARD-006.metadata-and-tagging-policy.md`**.
- **Official Taxonomy:** The controlled vocabulary for the metadata facets is maintained in **`GOV-TAXONOMY-001.ssot-metadata-taxonomy.md`**.

## 4. Implementation Action Plan

The following actions have been approved and will be tracked via GitHub Issues:

1. **Ratify New Standards:** The documents `GOV-STANDARD-006` and `GOV-TAXONOMY-001` are now considered active and approved SSoT.
2. **Update Master Template:** The `METATEMPLATE.md` within the `gct-ssot-templates` repository must be updated to include the new `metadata:` block structure, serving as the foundation for all future documents.
3. **Update Tooling:** A task will be assigned to `Camille` to update the SSoT linter to enforce the new standard as defined in `GOV-STANDARD-006`.
4. **Plan Knowledge Base Migration:** A task will be assigned to the `AIE Team` to develop and execute a migration script. This script will:
    - Read all existing SSoT documents.
    - Convert the legacy `tags:` field to the new `metadata:` block, mapping old tags to the new taxonomy where possible.
    - Flag any documents where manual categorization is required.

## 5. Referenced SSoT Documents

- **Policy Standard:** `GOV-STANDARD-006.metadata-and-tagging-policy.md`
- **Taxonomy Dictionary:** `GOV-TAXONOMY-001.ssot-metadata-taxonomy.md`
