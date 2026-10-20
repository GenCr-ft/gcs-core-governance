---
docId: GOV-PLAN-376
title: "[SPEC] WI-376 — ENG-STAN-004 Changelog and Release Notes Standard"
issue-id: GenCr-ft/gcs-core-governance#376
status: complete
version: "1.0"
authors: [session-agent]
metadata:
  scope: workspace-ops
  domain: governance
  doc-type: plan
  lifecycle-stage: complete
---

# [SPEC] WI-376 — ENG-STAN-004 Changelog and Release Notes Standard

Parent: GenCr-ft/gcs-project-management#575. Design: GenCr-ft/gcs-project-management#613 (approved).
Tier: `wi:lightweight` (human-set).

## Changes

1. `tooling/ENG-STAN-004.changelog-and-release-notes-standard.md`, the standard (approved via #613).
2. `agent-context/grounding/technical-constraints.md`, one row so the sanctioned read path finds it.

## Deviation from design

The design named it `DEV-SPEC-015` under `reference-libraries/`. Changed for two reasons:
`reference-libraries/` is frozen (AGENTS.md "Never Do"), and `DEV` is not a valid domain code
in the current taxonomy (DEV-SPEC-012 fails the same check). `tooling/` is where ENG-STAN-002/003
live, and the SSoT linters run there.

## Verification

- metadata-, naming- and link-linter on the new file: OK.
- markdownlint on both files: Passed.
- `technical-constraints.md` naming-linter error is pre-existing on `origin/main` (control run).
