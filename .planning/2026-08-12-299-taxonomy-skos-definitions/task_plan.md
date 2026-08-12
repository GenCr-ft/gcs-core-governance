---
docId: GOV-PLAN-299
title: WI-299 — taxonomy skos definitions
issue-id: GenCr-ft/gcs-core-governance#299
status: approved
---

# [CODE] WI-299 — taxonomy skos definitions

Implementation plan for GenCr-ft/gcs-core-governance#299.

## The defect

`config-engines/metadata-schemas/taxonomy.yml` fails validation against `taxonomy.schema.json`, which
sits in the same directory and declares at line 31:

```json
"category": ["skos:definition"]
```

Thirteen entries under `knowledge_classification_type` carry `category` without `skos:definition`:
`principle`, `protocol`, `technical-design-detail`, `technical-story`, `template`, `overview`,
`bug-report`, `registry`, `roadmap`, `enhancement-request`, `backlog`, `session`, `index`.

Open since March, reported three times independently — `gft verify --metadata` (this issue), a
`pre-commit` run in `gcl-srv-authentication` (`gcd-ops-scripts#115`), and now a **CI gate**
(`gcd-ops-scripts` step 9, red on `main`). Every reporter has been downstream; nothing in this
repository validates its own taxonomy on push.

## Decision: fix the data, not the schema

The facet has **40 entries and 27 already carry a `skos:definition`**. The established practice is that
a classification type is defined, so the 13 are omissions rather than proof the rule is too strict.
Narrowing the schema dependency would ratify an accident and discard 27 entries of precedent.

## Scope

In:

1. Add `skos:definition` to exactly those 13 entries.
2. Nothing else. No existing definition is altered — that is an explicit AC, verified by diff.

Out:

- Sharpening the `protocol` / `agent-protocol` and `roadmap` / `plan` boundaries. Both drafted
  definitions are correct; distinguishing them is a `skos:scopeNote` question and separate work.
- Adding a validation gate to this repository so it stops depending on downstream consumers. Genuinely
  needed, and filed separately rather than bundled here.

## Source of the definitions

A complete draft of all 13 already existed uncommitted in a workspace clone, preserved at
`agents/session/299-draft-skos-definitions.patch` in the operator's session directory. Reviewed against
the house style of the 27 existing definitions: **11 accepted verbatim, 2 corrected for defects** —
`principle` (unfinished sentence: "serves as the foundation" of what?) and `index` ("alphabetical" is
factually wrong for this taxonomy's indexes, `rules-index` being ordered by rule). Full review with
before/after wording is on the issue.

## Implementation

Targeted line insertion, not a YAML round-trip. `ruamel`/`yaml` re-emission would reformat the entire
2,000-line document and bury a 13-line change in noise, making the "no existing definition altered" AC
unreviewable. Each definition is inserted after the final line of its own entry block, matching where
the draft placed them.

## Verification

1. `jsonschema` validation of the whole document passes — 0 violations, down from 13.
2. `git diff --stat` shows exactly 13 insertions, 0 deletions, in 1 file.
3. Programmatic check that all 27 pre-existing definitions are byte-identical before and after.
4. Must-fire: delete one `skos:definition` and confirm validation fails and names that entry.
5. **End-to-end against the real consumer** — `gcd-ops-scripts#141` added a `GOVERNANCE_REF` knob, so
   its drift check can be pointed at this branch before merge:
   `GOVERNANCE_REF=fix/issue-299-taxonomy-skos-definitions pytest tests/test_taxonomy_drift.py`.
   That turns "should fix the red gate" into a measured result rather than a prediction.
