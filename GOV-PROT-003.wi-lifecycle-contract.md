---
docId: GOV-PROT-003
title: Work Item Lifecycle Quality Contract
version: 1.0.0
authors: [Studio Lead]
knowledgeGuardian:
- Orion (GCT-UTL-SLG-001)
creation_date: '2026-06-09'
last_updated_date: '2026-06-27'
language: en
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/GOV-PROT-003.wi-lifecycle-contract.md
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: protocol
  intended-audience:
  - ai-agents
  - contributors
  - governance-team
  security-classification: l2_confidential
---

# Work Item Lifecycle Quality Contract

**Spec:** `docs/superpowers/specs/2026-06-09-wi-lifecycle-enforcement-design.md`
**Epic:** <https://github.com/GenCr-ft/gcs-project-management/issues/320>

This document is the canonical definition of what must be true at each Work Item lifecycle
gate. All three enforcement layers (L1 hooks, L2 GitHub Actions, L3 wi-lifecycle skill)
reference this contract. Changes to gate requirements require a PR to this document first;
hook, Action, and skill updates follow as separate PRs.

---

## Phase Gates

### Gate 1 — Creation

| Section | Minimum content |
|---------|----------------|
| `## Summary` | 1–3 sentences, problem statement |
| `## Acceptance Criteria` | ≥1 AC bullet (free-text) |
| `## Architecture Impact` | ≥1 non-blank line (rough) |
| `## Out of Scope` | ≥1 non-blank line |

**Spec-refs blocker (hard-block):** If the WI `## Relations` section links any specification document whose `metadata.lifecycle-stage` frontmatter value is `draft`, `proposed`, or absent, the CREATE gate fails. An agent evaluates this by fetching each linked document and reading its `lifecycle-stage` field. See `agent-context/grounding/lexicon.yml` term `spec_refs` for the full evaluation algorithm.

### Gate 2 — Refine (before DESIGN sub-issue is approved)

| Upgrade required | Condition |
|-----------------|-----------|
| `## Acceptance Criteria` | All ACs in Gherkin (`Given/When/Then`) |
| `## Architecture Impact` | Detailed: interfaces, schemas, services |
| `## Testability Notes` | QA-authored: test types, tooling, data |
| `## Sub-issues` tasklist | Contains `- [ ] #N` for `[DESIGN]` sub-issue |

**Spec-refs advisory check:** All spec documents linked in `## Relations` must still carry `lifecycle-stage: approved`. This is an `additional_checks` condition (advisory, not hard-block): a demotion to `draft` or `proposed` surfaces as a warning that the linked spec may no longer support the WI's design. See `agent-context/grounding/lexicon.yml` term `spec_refs` for the evaluation algorithm.

### Gate 3 — Design (before [IMPL] sub-issue is authored)

| Artifact | Required state |
|----------|---------------|
| `[DESIGN]` sub-issue | Authored with all required sections (see Sub-issue Contracts) |
| Adversary review | Dispatched; critical/high findings resolved |
| Output token | `LIFECYCLE:DESIGN:READY` posted on [DESIGN] sub-issue |
| Human review | Human sets `status:approved` on [DESIGN] sub-issue |

### Gate 4 — Implement (before Edit/Write is unblocked)

| Artifact | Required state |
|----------|---------------|
| `[DESIGN]` sub-issue | Closed + `status:approved` set by human reviewer |
| `[IMPL]` sub-issue | `status:approved` set by human reviewer |
| Both sub-issues | Linked in parent WI tasklist |
| Self-approval | Forbidden — label setter must differ from current GitHub actor |

### Gate 5 — Close (before `Closes #N` written)

| Check | Required |
|-------|---------|
| AC checkboxes on parent WI | All ticked |
| `✅ AC-N satisfied` comments | One per AC on parent WI |
| `LIFECYCLE:CODE-REVIEW:*` PR comment | Present with pass or finding disposition |
| `LIFECYCLE:SECURITY-REVIEW:*` PR comment | Present with OWASP pass or accepted-risk |
| `LIFECYCLE:DATA-RISK:*` PR comment | NONE/MITIGATED/ACCEPTED with justification |
| ADR | Referenced if wire format, auth, or persistence changed |
| PR checklist | All boxes ticked |
| `[IMPL]` Relations Check | `[IMPL]` sub-issue body contains a valid branch or PR reference in its `## Relations` section |

---

## Spec Reference Contract

A **spec_ref** is a specification document linked or referenced in a Work Item body. This section is the canonical definition required by `wi-lifecycle-gates.yml` (lines 20 and 30).

### What qualifies as a spec_ref

A document or issue qualifies as a spec_ref if:
- Its `docId` frontmatter field starts with a recognized spec prefix: `ENG-SPEC-`, `GAM-SPEC-`, `GOV-SPEC-`, or any studio-registered docId pattern ending in `-SPEC-`.
- It is a GitHub Issue carrying the `spec` label.
- It is explicitly named as a spec in the WI body using the format `**Spec:** <link>`.

### How to identify spec_refs on a WI

Scan the WI issue body for:
1. Lines matching `**Spec:** <url-or-issue-ref>`
2. Linked issues that carry the `spec` label.
3. File paths matching the docId patterns above in the `## Architecture Impact` or `## Relations` sections.

If none are found, the spec_ref set is considered **absent**.

### How to evaluate lifecycle-stage

| Source type | Where to read lifecycle-stage |
|-------------|------------------------------|
| Markdown file with YAML frontmatter | `metadata.lifecycle-stage` field |
| GitHub Issue | Label starting with `lifecycle:` (e.g. `lifecycle:approved`) |
| No frontmatter and no label | Treat as `draft` |

Valid lifecycle-stage values: `draft`, `proposed`, `approved`, `deprecated`, `archived`.

### Gate evaluation rules

| Gate key | Location in YAML | Blocks when |
|----------|-----------------|-------------|
| `spec_refs_with_lifecycle_stage: ["draft", "proposed", "absent"]` | create phase `blockers:` | Any linked spec_ref has lifecycle-stage `draft` or `proposed`, OR the spec_ref set is absent |
| `spec_refs_still_approved: true` | refine phase `blockers:` | Any linked spec_ref no longer has lifecycle-stage `approved` at refine time |

---

## Sub-issue Contracts

### `## Relations` Section Format

Every `[DESIGN]` and `[IMPL]` sub-issue body must include a `## Relations` section conforming to this format:

```markdown
## Relations
- **Parent WI:** GenCr-ft/<repo>#<number>
- **Dev branch:** `feat/issue-<number>-<slug>` (or link to PR once opened)
```

### `[DESIGN]` Required Sections

```text
## Relations
## Schemas & Data Models
## Interface Signatures
## Rejected Alternatives
## Architecture Diagram / C4 Impact
## Open Questions
```

A section passes with ≥1 non-blank, non-header line. `N/A` + one-line justification is valid.

### `[IMPL]` Required Sections (13 headers)

```text
## Relations
## Desired Outcome
## AC Coverage Map
## Technical Scope
  ### Schema & Migration Changes
  ### Port / Interface Changes
  ### Adapter / Implementation Notes
## TDD Cycles
  ### Cycle N — [descriptive name]
## Integration & E2E Verification
## Risk Register
## External Dependencies
## Rollback Plan
## Definition of Done
```

Constraints: ≥1 cycle with Red/Green/Blue legs; cycle names non-generic;
≤10 cycles (else decompose); Risk Register + Rollback non-empty on P0/P1;
AC Coverage Map rows ≥ parent AC count.

---

## Agent Behavioral Contract

### MUST NOT (hard-blocked via exit 2 or required status check)

1. Write `Closes #N` before all AC checkboxes are ticked and evidence comments are present.
2. Set `status:approved` on any sub-issue (Claude is never the approver).
3. Post `LIFECYCLE:BYPASS` on its own behalf.
4. Commit to `main`, `master`, or `prod`.
5. Commit without a `WI-N.M` ref in the message.
6. Modify source files without a valid open WI issue linked to the current branch.
7. Skip a gate without human-set `lifecycle:bypass` label AND pre-posted bypass comment.
8. Close the parent WI issue manually.
9. Begin Edit/Write on `implement`-phase work before the implement gate passes.
10. Merge a PR without all L2 required status checks green.

### MUST (obligations)

1. Invoke `wi-lifecycle <phase>` at each phase transition.
2. Post `✅ AC-N satisfied` evidence comments on the parent WI for each AC.
3. Post review outcome markers (`LIFECYCLE:CODE-REVIEW:`, `LIFECYCLE:SECURITY-REVIEW:`,
   `LIFECYCLE:DATA-RISK:`) as PR comments before the close gate.
4. Author `[DESIGN]` and `[IMPL]` sub-issues before the design gate is validated.
5. Link sub-issues in the parent WI tasklist.
6. Run `./test.sh` before opening a PR.
7. Post fix-pointer comments on resolved PR review threads.

### Gate Failure Protocol

1. Post `❌ LIFECYCLE:<PHASE>:FAIL — <gap list>` to the issue.
2. Stop all work on the WI.
3. Communicate the specific gaps to the user.
4. Wait for user direction before attempting any gap remediation that requires
   design judgement or human approval.

---

## Bypass Protocol

A **human** (not Claude) must:

1. Post on the issue: `LIFECYCLE:BYPASS — gate: <name> — reason: <justification>`
2. Set `lifecycle:bypass` label on the issue.

The L1 hook verifies both. Claude cannot satisfy either condition on its own behalf.

---

## Lifecycle Marker Tokens

Machine-parseable token set used by all three enforcement layers:

| Token | Meaning |
|-------|---------|
| `✅ LIFECYCLE:<PHASE>:PASS` | Phase gate passed; written to issue comment |
| `❌ LIFECYCLE:<PHASE>:FAIL — <gaps>` | Phase gate failed; written to issue comment |
| `LIFECYCLE:DESIGN:READY` | Design sub-issue complete; ready for human review and `status:approved` label |
| `LIFECYCLE:CODE-REVIEW:PASS` | Code review clean |
| `LIFECYCLE:CODE-REVIEW:FINDINGS` | Code review findings with accepted dispositions |
| `LIFECYCLE:SECURITY-REVIEW:PASS` | OWASP scan clean |
| `LIFECYCLE:SECURITY-REVIEW:FINDINGS` | Security findings with accepted-risk statements |
| `LIFECYCLE:DATA-RISK:NONE` | No data loss or destructive operation risk |
| `LIFECYCLE:DATA-RISK:MITIGATED` | Data risk present and mitigated |
| `LIFECYCLE:DATA-RISK:ACCEPTED` | Data risk accepted with justification |
| `LIFECYCLE:BYPASS — gate: <name> — reason: <text>` | Human-authored bypass justification |

---

## Evidence Comment Format

```markdown
✅ AC-N satisfied — PR #<number>, commit <sha>
Scenario: `<Gherkin scenario title>`
Test: `<file>:<line>` — `<test description>`
Output:
\`\`\`
<actual test runner output — not placeholder>
\`\`\`
```

---

## Sub-issue Naming Convention

| Type | Title pattern | Example |
|------|--------------|---------|
| `[DESIGN]` | `[DESIGN] WI-N.M — <parent WI title>` | `[DESIGN] WI-320.3 — phase-aware issue-context-gate` |
| `[IMPL]` | `[IMPL] WI-N.M — <parent WI title>` | `[IMPL] WI-320.3 — phase-aware issue-context-gate` |

## Tasklist Position Convention

In the parent WI body, the Sub-issues tasklist must follow this order:

1. First entry: `[DESIGN]` sub-issue link
2. Second entry: `[IMPL]` sub-issue link

This order is relied on by `github_api.get_subissues_from_tasklist` in `gcs-plt-gemop/hooks/github_api.py`.
