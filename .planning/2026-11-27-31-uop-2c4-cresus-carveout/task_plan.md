---
docId: GOV-PLAN-031
title: "[FIX] WI-31 — amend GOV-POLICY-003 UOP 2.C.4 with the Cresus conversational carve-out"
issue-id: GenCr-ft/gcs-core-governance#31
status: complete
version: "1.0"
authors: [session-agent]
metadata:
  scope: workspace-ops
  domain: governance
  doc-type: plan
  lifecycle-stage: complete
---

# [FIX] WI-31 — amend GOV-POLICY-003 UOP 2.C.4

Tier: `wi:lightweight`, set by the Studio Lead in the web UI. REFINE-LIGHTWEIGHT:PASS is posted on the issue.

## Decisions (Studio Lead, 2026-11-27)

- Amend the policy to match the reviewed Cresus carve-out (GenCr-ft/gcs-plt-gemop#75); Cresus stays as it is.
- The exception covers Cresus only.
- MINOR bump, 1.1.0 → 1.2.0.
- "Lug" and "the Studio Director" are the same principal.
- Edit in place under `reference-libraries/`, as an explicit single-file exception to AGENTS.md:82 (Never Do).

## Changes

1. `reference-libraries/studio-handbook/00-studio-vision-and-principles/GOV-POLICY-003.universal-gem-operating-principles.md`: UOP 2.C.4 gets one bounded exception; version 1.2.0; `last_updated_date` 2026-11-27.
2. `governance/governed-paths.sha256`: re-baselined with `verify_governed_paths.py --update`; exactly one hash changed.
3. `CHANGELOG.md`: one `### Changed` entry.

## Verification

- `verify_governed_paths.py`: rc=1 before re-baselining (it names this file), rc=0 after.
- AC-4: grep of `gcs-plt-gemop` `origin/main` `agents-src/` for French, Français, `\bFR\b` and `fr-FR` finds the Cresus carve-out (now covered by the policy) and Codex's "French law" (a jurisdiction, not a language rule).
