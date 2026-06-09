---
docId: GCS-GUIDE-405
title: ".planning/ Directory Retention Policy"
version: 1.0.0
status: Approved
date: 2026-06-02
authors:
  - "Engineering Lead"
knowledgeGuardian:
  - "Engineering Lead"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/04-process-guides/GCS-GUIDE-405.planning-directory-retention-policy.md
metadata:
  lifecycle-stage: approved
  domain: engineering
  doc-type: guide
  scope: studio-wide
  security-classification: l2_confidential
  keywords:
    - "planning"
    - "task-plan"
    - "agent-workflow"
    - "retention"
    - "ephemeral"
    - "process"
---

# .planning/ Directory Retention Policy

## 1. Objective

This policy defines the lifecycle of task plan files stored in `.planning/` directories across all GenCr@ft Studio repositories. It prevents the accumulation of stale, completed plans that can cause AI agents to re-execute already-merged work items.

## 2. Scope

This policy applies to all repositories in the GenCr@ft Studio workspace that contain a `.planning/` directory. The following eight repositories were identified as affected at the time this policy was authored:

- `gcl-srv-authentication`
- `gcl-srv-persistence`
- `gcs-project-management`
- `gcp-aethel-architecture`
- `gcp-aethel-client`
- `gcs-plt-tools`
- `gcs-engineering-handbook`
- `gcp-aethel-docs-req`

Any repository that introduces a `.planning/` directory in the future is automatically subject to this policy.

## 3. Plan File Frontmatter

Every `.planning/` task plan file MUST include a `status` field in its YAML frontmatter. The allowed values are:

| Value | Meaning |
|-------|---------|
| `in_progress` | The plan is actively being executed in the current or a future session. |
| `approved` | The plan has been authored and approved but execution has not yet started. |
| `blocked` | Execution is paused pending an external dependency or decision. |
| `complete` | All tasks in the plan are checked and the associated PR has been merged. |

Example frontmatter:

```yaml
---
plan_id: WI-6.3-player-position-persistence
status: in_progress
created: 2026-05-28
work_item: https://github.com/GenCr-ft/gcp-aethel-backlog/issues/NNN
---
```

## 4. Retention Rules

### Rule 1 — Plans are session-ephemeral artefacts

A `.planning/` task plan exists only during the working session that produced it. Once the associated work item is complete and its PR is merged, the plan has fulfilled its purpose and must be deleted.

### Rule 2 — Completed plans must not be committed to main

A plan file with `status: complete` MUST be deleted by the authoring agent before or immediately after the PR merge that completes the work. A completed plan must never be committed to `main` in its completed state.

### Rule 3 — In-progress or blocked plans may survive across sessions on the working branch

A plan with `status: approved`, `status: in_progress`, or `status: blocked` MAY be committed to the working branch so that it survives across sessions. This is the only permitted case for committing a `.planning/` file to a branch.

### Rule 4 — Plans must be deleted at merge time

When a PR is merged, any `.planning/` file that was committed to the feature branch MUST be deleted. The deletion must occur in the merge commit itself or in a follow-up cleanup commit on `main` immediately after merge. No completed plan survives the merge boundary.

### Rule 5 — Agents must not act on completed plans

An agent that encounters a `.planning/` directory containing a file with `status: complete` or with all tasks checked MUST treat it as a stale artefact and ignore it entirely. The agent must not re-execute the tasks described in that plan.

## 5. Pre-commit Hook Gate

A pre-commit hook warns when a `status: complete` plan file is staged for commit. This is a **reminder gate, not a hard block** — it surfaces the violation so the author can delete the file rather than accidentally committing it. The hook implementation is tracked in [gcs-plt-gemop#144](https://github.com/GenCr-ft/gcs-plt-gemop/issues/144).

If the pre-commit hook fires on a `status: complete` plan file, the correct resolution is to delete the file and re-stage.

## 6. Rationale

Accumulated stale plans create a hazard for AI agents operating across sessions. When an agent discovers a `.planning/` directory containing all-checked plans, it may interpret the plans as pending work and attempt to re-execute already-merged work items. This results in duplicate branches, conflicting PRs, and wasted session time. The retention policy eliminates the hazard at its source by making plan deletion a required part of the PR merge workflow.

## 7. Enforcement Summary

| Scenario | Required Action |
|----------|----------------|
| PR merged, plan `status: complete` | Delete the plan file in or immediately after the merge commit. |
| PR merged, plan was committed to branch with `status: in_progress` | Update `status` to `complete`, then delete the file before or during merge. |
| Pre-commit hook warns on `status: complete` plan | Delete the file, do not commit it. |
| Agent finds a `status: complete` plan in `.planning/` | Treat as stale; ignore entirely; do not re-execute tasks. |
| New repo introduces `.planning/` | This policy applies automatically; no additional opt-in required. |

## 8. Related Documents

- [`GCS-GUIDE-201`](../02-development-guides/GCS-GUIDE-201.developer-guide.md) — The Everyday Developer's Guide (Git workflow)
- `GCS-GUIDE-203` — TDD Guide
- [`ENG-REFE-001`](../01-manifesto-and-culture/ENG-REFE-001.studio-global-engineering-standards.md) — Studio Global Engineering Standards
- [`../AGENTS.md`](../AGENTS.md) — Agent orientation guide for this repo
