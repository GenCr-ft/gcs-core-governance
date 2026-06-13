---
docId: GOV-PLAN-379
title: "[CODE] Enforce parent back-references and branch relations on sub-issues"
issue-id: "GenCr-ft/gcs-plt-tools#379"
created: 2026-06-13
status: in-progress
---

# [CODE] Task Plan — Enforce parent back-references and branch relations on sub-issues (#379)

## Objectives
- Update the Work Item Lifecycle Quality Contract (`GOV-PROT-003`) to require `## Relations` section.
- Update the `wi-lifecycle` skill (`SKILL.md`) templates for `[DESIGN]` and `[IMPL]` sub-issues to include the `## Relations` section.
- Update the `wi-lifecycle close` gate requirements in the skill to verify that the `[IMPL]` sub-issue body contains a valid branch reference.

## Execution Checklist
- [ ] Add `## Relations` specifications to `GOV-PROT-003.wi-lifecycle-contract.md`.
- [ ] Add `## Relations` template content to `gcs-plt-gemop/skills/wi-lifecycle/SKILL.md`.
- [ ] Add branch verification validation to `wi-lifecycle close` gate in `SKILL.md`.
