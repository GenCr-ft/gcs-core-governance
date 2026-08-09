---
docId: GOV-PLAN-308
title: "[CODE] WI-308 — contract-backfill: document lifecycle-phase deprecated alias"
issue-id: GenCr-ft/gcs-core-governance#308
status: in-progress
version: "1.0"
authors: [session-agent]
metadata:
  scope: workspace-ops
  domain: governance
  doc-type: plan
  lifecycle-stage: in-progress
---

# [CODE] WI-308 — contract backfill (lifecycle-phase deprecated alias)

Backfills the WI-lifecycle contract for the ratified #309 decision + the #374 skill behavior
(GOV-PROT-003 §32 contract-first order). wi:lightweight (GOV-STAN-010) — docs-sync, no §5 surface.

- `GOV-PROT-003.wi-lifecycle-contract.md` — new subsection "Deprecated alias: lifecycle-phase"
  under "How to evaluate lifecycle-stage": documents `lifecycle-phase`/ADR-`status` fallback with
  value mapping `accepted→approved` (ratified #309), `design→proposed` (#374); plus canonical
  absent-key handling (absent→draft, skill must conform). Version 1.0.0→1.1.0.
- `agent-context/grounding/lexicon.yml` — `spec_refs` term augmented with the same alias rule.

Satisfies #308 ACs and #309's "update GOV-PROT-003 enum + #374 alias" AC. Ref #308, #309, #374.
