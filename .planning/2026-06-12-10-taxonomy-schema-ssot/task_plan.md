---
docId: GOV-PLAN-10
issue-id: GenCr-ft/gcs-core-governance#10
title: "[CODE] Restructure taxonomy schema definition requirement"
created: 2026-06-12
status: approved
---

# [CODE] Task Plan - Restructure Taxonomy Schema Definition Requirement

## Goal
Restructure taxonomy schema so skos:definition is required for non-category concepts but optional for categories, and keep both taxonomy schema files in sync.

## Phases

### Phase 1: Implementation
- [x] Restore skos:definition as required in generic skosConcept in config-engines/metadata-schemas/taxonomy.schema.json.
- [x] Sync reference-libraries/devops-standards/foundations/governance/schemas/law-files/taxonomy.schema.json to match config-engines one exactly.
- Status: complete

### Phase 2: Verification
- [x] Run pre-commit hooks to ensure taxonomy yml passes validation.
- Status: complete
