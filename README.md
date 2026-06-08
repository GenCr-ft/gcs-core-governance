---
docId: GOV-REPO-001
title: Core Governance Repository
version: 1.0.0
authors: ["Principal AI Architect"]
creation_date: '2026-06-08'
last_updated_date: '2026-06-08'
language: en
summary: "Centralized computable governance rules and metadata schemas."
metadata:
  lifecycle-stage: approved
  scope: studio-wide
  domain: governance
  doc-type: readme
  security-classification: l2_confidential
  keywords: ["governance", "schemas", "rules"]
---

# GenCr@ft Studio: Core Governance

Welcome to the `gcs-core-governance` repository. This repository serves as the **Operational Control Plane** for the entire GenCr@ft Studio portfolio. It replaces passive natural language documentation with active, computable schemas, linters, and blueprints.

## Three-Tier Layout

1. **`config-engines/`**: Machine-readable constraints only (JSON/YAML). Contains metadata schemas, pipeline thresholds, AI Gem blueprints, and API parameters.
2. **`execution-manuals/`**: Flat, rule-based execution checklists (Zero narrative prose). Contains onboarding manuals, release protocols, security checklists, and testing playbooks.
3. **`reference-libraries/`**: Preserved human reference files, including the Godot Engine Bible, PCG Guidelines, and Legal Charters.
