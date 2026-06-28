---
docId: GOV-GUIDE-HG-002
title: Work Item Lifecycle Flow
version: 1.0.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: guide
  intended-audience: [contributors]
  security-classification: l1_internal
---
# Work Item Lifecycle Flow

Visual guide to the 4-gate Work Item (WI) lifecycle. All states and transitions match `GOV-PROT-003.wi-lifecycle-contract.md` exactly.

> **Source:** `GOV-PROT-003.wi-lifecycle-contract.md` (canonical)

## State Diagram

```mermaid
stateDiagram-v2
    [*] --> Open : Issue filed

    Open --> REFINE_PASS : Gate 2 passed
    note right of Open
        Gate 1 (Create) checks:
        Summary, ACs, Architecture Impact,
        Out of Scope — all non-empty
    end note

    REFINE_PASS --> DESIGN_READY : [DESIGN] sub-issue authored
    note right of REFINE_PASS
        Gate 2 (Refine) checks:
        Gherkin ACs, Testability Notes,
        Sub-issues tasklist with [DESIGN] link
    end note

    DESIGN_READY --> IMPLEMENT_PASS : [DESIGN] + [IMPL] approved by human
    note right of DESIGN_READY
        Gate 3 (Design) checks:
        [DESIGN] all required sections present
        Adversary review PASS
        LIFECYCLE:DESIGN:READY posted
        Human sets status:approved on [DESIGN]
    end note

    IMPLEMENT_PASS --> CLOSE_PASS : PR open, all ACs ticked
    note right of IMPLEMENT_PASS
        Gate 4 (Implement) checks:
        [DESIGN] closed + status:approved
        [IMPL] open + status:approved
        Both sub-issues approved by non-self
        [IMPL] body has all required sections
        TDD commit policy followed
    end note

    CLOSE_PASS --> Closed : Closes #N written in PR
    note right of CLOSE_PASS
        Gate 5 (Close) checks:
        AC checkboxes ticked
        CODE-REVIEW + SECURITY-REVIEW + DATA-RISK
        PR adversary review PASS
        All PR checklist boxes ticked
    end note

    Closed --> [*]
```

## Gate Summary Table

| Gate | Name | Trigger | Key Checks |
|------|------|---------|------------|
| 1 | Create | Issue filed | Summary, ACs, Architecture Impact, Out of Scope |
| 2 | Refine | Branch cut | Gherkin ACs, Testability Notes, [DESIGN] link in Sub-issues |
| 3 | Design | [DESIGN] sub-issue authored | All required sections, adversary PASS, LIFECYCLE:DESIGN:READY posted |
| 4 | Implement | [DESIGN]+[IMPL] approved | Non-self approval, [IMPL] sections, TDD cycles |
| 5 | Close | PR open, all ACs ticked | Reviews, adversary, PR checklist, ADR if needed |

## TDD Commit Convention

Each TDD cycle produces exactly two commits:

```
test(scope): WI-N.M — red: <description of failing test>
feat(scope): WI-N.M — green: <description of implementation>
```

Refactor commits are optional but follow:
```
refactor(scope): WI-N.M — blue: <description>
```

## Sub-issue Naming Convention

| Type | Title pattern | Example | State when gate passes |
|------|--------------|---------|------------------------|
| `[DESIGN]` | `[DESIGN] WI-N.M — <parent WI title>` | `[DESIGN] WI-42.1 — fix auth bug` | Closed + `status:approved` (set by human) |
| `[IMPL]` | `[IMPL] WI-N.M — <parent WI title>` | `[IMPL] WI-42.1 — fix auth bug` | Open + `status:approved` (set by human) |

> **Self-approval is forbidden.** The person who sets `status:approved` must differ from the current GitHub actor. In a solo studio, this creates a gate that requires a second human reviewer.
