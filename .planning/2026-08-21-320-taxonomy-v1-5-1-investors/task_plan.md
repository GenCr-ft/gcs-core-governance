---
docId: GOV-PLAN-320
title: "[CODE] WI-320 — taxonomy v1.5.1: add intended_audience `investors` (ruled)"
issue-id: GenCr-ft/gcs-core-governance#320
status: in-progress
version: "1.0"
authors: [session-agent]
metadata:
  scope: workspace-ops
  domain: governance
  doc-type: plan
  lifecycle-stage: in-progress
---

# [CODE] WI-320 — taxonomy v1.5.1 (add `investors`)

Implements **Decision 3** of the #320 ruling (Studio Lead, 2026-08-21). Companion to #321, which
delivered v1.5.0 under the same pattern.

- `config-engines/metadata-schemas/taxonomy.yml`: add `intended_audience` entry `investors`;
  `ssot_version` 1.5.0 → 1.5.1.
- Re-baselined `governance/governed-paths.sha256` — `taxonomy.yml` is drift-block governed
  (30 governed files, exactly one hash changed).

## Why this term is added rather than mapped

#320's Decision 3 maps three of the four unknown `intended-audience` terms to existing vocabulary
(`template-creators` → `all-contributors`, `ux-researchers` → `designers`, `operations-team` →
`devops-crew`) and adds only `investors`. The reason: **all 21 pre-existing terms denote an internal
studio audience**, so there is nowhere to map an external reader without asserting something false
about who the document is for. That is a genuine gap in the vocabulary, not an authoring error.

This is consistent with, not a departure from, #321's *"map near-misses to existing. No ADD"* — the
other three are near-misses; `investors` has no near-miss.

## Tier

`wi:lightweight` (human-set). GOV-STAN-010 §6 names *"a single additive configuration value"* as an
eligible class; §5.3 ("database schema, migrations, storage formats") does not cover a
controlled-vocabulary config file, and §5.6 does not apply because an additive vocabulary entry can
only widen what the validator accepts — it cannot create a denial. #321's ratification note asserted
that `taxonomy.yml` edits need full ceremony or a bypass on §5 grounds; that reading of §5 does not
survive comparison with §5's text, and is flagged for correction on #321.

## Verification

1. **Additive-only across every vocabulary.** Parsed `origin/main` vs the working tree for all ten
   vocabularies: `intended_audience` 21 → 22, every other unchanged, **nothing removed**. A
   synthetic-removal control confirms the detector would catch a deletion.
2. **Functional, both directions** — a probe document declaring `intended-audience: [investors]`:
   - Law v1.5.0 → `[TAXONOMY_VALIDATOR] … The value(s) ['investors'] are not valid entries` (1 error)
   - Law patched → scans clean, 0 findings
3. **Drift baseline** — `verify_governed_paths.py` flags the edit before re-baselining (exit 1) and
   reports `30 governed files match` after (exit 0). A pristine `origin/main` checkout also reports
   30/clean, confirming the baseline was not weakened.
4. `taxonomy.yml` validates against `taxonomy.schema.json` — **but this proves little**: a control
   appending a malformed entry (`{not_a_prefLabel: x}`) is *also* accepted, so the schema does not
   constrain `intended_audience` entry shape. Recorded rather than presented as assurance.

## Out of scope

- **The three value maps** in Decision 3, and Decisions 1 and 2 (`NFR` → `REQ`, `deferred` →
  `ideation`) — all are per-repo document edits, landing in the #314 remediation WIs.
- **Tagging `v1.5.1` and the fleet re-pin** — post-merge steps 2 and 3, owned by
  `gcs-project-management#531` / `gcd-shared-actions#125`.
- **#321's step-4 renames** (`CATALOG`→`CAT`, `RPT`→`REP`, `REG`→`REGI`, `PRO`→`MGT`, `VAL`→`QA`).

## Observed while doing this, not fixed here

`governance/verify_governed_paths.py` resolves its root from `GOVERNANCE_REPO_ROOT` **or cwd**, and
`_drift_block_globs` swallows a missing manifest with a bare `except Exception: return []`. Run from
the wrong directory it prints `✅ governance-integrity: 0 governed files match the baseline` and
exits 0 — a green result that means "I found no manifest", indistinguishable from "nothing drifted".
Worth a guard that fails when zero governed files are discovered.

Ref #320, #321, #314, #310.
