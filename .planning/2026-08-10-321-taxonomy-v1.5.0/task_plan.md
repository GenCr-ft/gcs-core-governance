---
docId: GOV-PLAN-321
title: "[CODE] WI-321 — taxonomy v1.5.0: add REQ + INIT (ratified)"
issue-id: GenCr-ft/gcs-core-governance#321
status: in-progress
version: "1.0"
authors: [session-agent]
metadata:
  scope: workspace-ops
  domain: governance
  doc-type: plan
  lifecycle-stage: in-progress
---

# [CODE] WI-321 — taxonomy v1.5.0 (add REQ + INIT)

Implements the ratified #321 ruling (Isaac; Studio-Lead ratified; L1 gate via human `lifecycle:bypass`).

- `config-engines/metadata-schemas/taxonomy.yml`: add `knowledge_classification_type` entries
  `requirement/REQ` (to-describe) and `initiative/INIT` (to-plan); `ssot_version` 1.4.0 → 1.5.0.
- Re-baselined `governance/governed-paths.sha256` (taxonomy.yml is drift-blocked; 30 governed files).
- Proven: a probe `ENG-REQ-999` doc scans with 0 `Document Type 'REQ'` errors under the new Law.

The RENAMEs (CATALOG→CAT, RPT→REP, REG→REGI, PRO→MGT, VAL→QA) + metadata value maps are per-repo
and land in the #314 remediation WIs. Post-merge: tag v1.5.0 → re-pin the 6 repos' governance-version.
Ref #321, #314, #310.
