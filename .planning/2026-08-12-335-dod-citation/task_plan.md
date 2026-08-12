---
docId: GOV-PLAN-335
title: WI-335 — dod citation
issue-id: GenCr-ft/gcs-core-governance#335
status: approved
---

# [CODE] WI-335 — dod citation

Implementation plan for GenCr-ft/gcs-core-governance#335.

## The defect

`human-guides/validation-rules-summary.md` documents GOV_RULE_005 as requiring
`"References Definition of Done (PRO-STAN-001)"`. The rule engine requires a different string —
`config-engines/metadata-schemas/validation-rules.yml:52`:

```yaml
body_must_contain_string: "References Definition of Done (OPS-STANDARD-001)"
```

GOV_RULE_005 is a literal substring match with no near-miss tolerance, so a contributor who follows the
guide is rejected by the gate and given no reason to suspect the guide.

`agent-context/grounding/lexicon.yml:60` independently agrees with the engine ("Document:
OPS-STANDARD-001"), so it is two machine-readable sources against one human summary.

## Scope, established by audit rather than assumed

The issue's AC-2 requires the whole table be compared, not just the known-bad row — fixing one instance of
a class leaves the class. Audit run before touching anything:

```
rule ids in engine and guide            identical, all 6, no drift
docIds cited in engine                  LEG-LCOUN-001, MGT-SECOFF-001, OPS-STANDARD-001, PRG-SARCH-001
docIds cited in guide                   PRO-STAN-001
cited in guide but not in engine        PRO-STAN-001
per-rule enforced-string mismatches     1  (GOV_RULE_005 only)
```

The owner columns render as names (Isaac, Cerberus, Henri) where the engine holds docIds
(`PRG-SARCH-001`, `MGT-SECOFF-001`, `LEG-LCOUN-001`). That is presentation for a human audience, not drift,
and is deliberately left alone.

So the change is exactly 2 lines, and that number is measured.

## Out of scope

**Which DoD document is canonical.** Both docIds resolve to real files —
`PRO-STAN-001.definition-of-done.md` under `devops-standards` and
`OPS-STANDARD-001.definition-of-done-(dod).md` under `studio-handbook`. That is a governance ruling, filed
as #336, and it may later move the gate's string; this WI only makes the guide agree with the gate as
enforced today. Deciding canonicality here would be making a governance call inside a docs fix.

## Verification

1. `PRO-STAN-001` no longer appears in the guide; `OPS-STANDARD-001` appears in both rows.
2. The audit re-run reports 0 mismatches across all six rules.
3. `git diff --stat` shows exactly 2 changed lines in 1 file.
4. `bash test.sh` exits 0.
5. Must-fire: the audit script must be shown to *detect* a mismatch, by re-introducing one, so its
   "0 mismatches" carries information.
