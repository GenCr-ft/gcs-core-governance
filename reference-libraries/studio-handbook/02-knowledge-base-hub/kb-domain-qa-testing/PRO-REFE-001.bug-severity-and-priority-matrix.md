---
docId: PRO-REFE-001
title: Bug Severity and Priority Matrix
version: 1.0.0
creation_date: '2025-06-13'
last_updated_date: '2026-05-20'
authors:
- "Zo\xE9 (GCT-QAS-QATL-001)"
knowledgeGuardian:
- "Zo\xE9 (GCT-QAS-QATL-001)"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/02-knowledge-base-hub/kb-domain-qa-testing/PRO-REFE-001.bug-severity-and-priority-matrix.md
metadata:
  lifecycle-stage: approved
  keywords:
  - quality
  - qa
  - bug
  - severity
  - priority
  - triage
  - scrum
  scope: studio
  domain: production-management
  doc-type: reference
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
---
# Bug Severity and Priority Matrix

## 1. Purpose

This document provides a standardized framework for classifying bugs based on their **Severity** and **Priority**. Its purpose is to ensure a consistent, objective, and efficient bug triage process, enabling the team to focus development resources on resolving the most critical issues first.

This framework is a critical tool for Protocol S15 (Agile/Scrum) and must be used when reporting and managing bugs via the `bug-report-template.md`.

## 2. Core Concepts: Severity vs. Priority

It is essential to understand the distinction between these two concepts:

- **Severity:** Describes the **impact of the bug on the system**. It is a measure of the technical and functional gravity of the defect. Severity is assessed by the QA Lead (`Zoé`) and development team (`Julien`).
- **Priority:** Describes the **urgency of fixing the bug from a project and business perspective**. It determines the order in which bugs should be fixed. Priority is ultimately decided by the Product Owner (`Béatrice`) in consultation with the Producer (`Antoine`) and technical leads.

**In short: Severity measures impact; Priority measures urgency.** A high-severity bug may sometimes have a low priority (e.g., a crash in an obscure, non-critical admin panel), and vice-versa.

## 3. Bug Triage and Prioritization Workflow

**Note for AI Gems:** The following diagram shows the standard process for handling a new bug report. Your role may involve reporting (Step 1), assessing (Step 2), or receiving prioritized tasks (Step 4).

```mermaid
graph TD
    A[<b>Start:</b> New Bug Reported<br><i>(via bug-report-template.md)</i>] --> B{<b>Step 1: QA Triage</b><br><i>Actor: Zoé (QA Lead)</i>};
    B --> C[Assigns <b>Severity</b><br>based on technical impact];
    C --> D[Consults Matrix for<br><b>Initial Priority</b> Recommendation];
    D --> E{<b>Step 2: Prioritization Meeting</b><br><i>Actors: Béatrice, Antoine, Julien, Zoé</i>};
    E --> F[Confirms or Adjusts<br><b>Final Priority</b>];
    F --> G[<b>End:</b> Bug is Prioritized<br>in the Product Backlog];

    style G fill:#d4edda,stroke:#155724,stroke-width:2px
```

## 4. Severity Levels

| Level       | ID      | Description                                                                                                                                      | Gencraft Examples                                                                                                                                |
| :---------- | :------ | :----------------------------------------------------------------------------------------------------------------------------------------------- | :----------------------------------------------------------------------------------------------------------------------------------------------- |
| **Blocker** | `SEV-1` | Prevents development or testing of other features. No workaround exists. Causes the entire application or a critical system to crash or be unusable. | Game fails to launch. CI/CD pipeline is completely broken. Main branch build is failing. Player login is impossible.                         |
| **Critical**| `SEV-2` | A core feature is unusable or fails completely. Causes data loss or data corruption. May lead to security vulnerabilities. Significant performance degradation. | A core gameplay mechanic (e.g., crafting, combat) does not work. Player inventory/progress is wiped. A frequent, reproducible game crash.          |
| **Major** | `SEV-3` | A major feature is partially non-functional, or a non-core feature is completely broken. The user experience is significantly degraded.            | A specific character skill fails under certain conditions. Major UI screen is broken or unresponsive. Significant visual artifacts on main assets. |
| **Minor** | `SEV-4` | A minor feature is non-functional, or a major feature has a minor issue. A workaround exists. Minor UI/UX or visual issues.                       | A tooltip displays incorrect information. A sound effect doesn't play. A minor graphical clipping issue with an armor piece.                    |
| **Trivial** | `SEV-5` | Cosmetic issue with no functional impact. Typo in a non-critical text field.                                                                     | A single voxel is miscolored on a non-critical prop. A typo in the game credits. A UI element is misaligned by one pixel.                   |

## 5. Priority Levels

| Level      | ID     | Description                                                                                                                                                    |
| :--------- | :----- | :------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| **Urgent** | `P1`   | **Fix Immediately.** This issue blocks the entire team or a critical project milestone. Must be addressed in the current sprint, potentially interrupting other work. |
| **High** | `P2`   | **Fix As Soon As Possible.** This is a high-priority item for the next sprint or to be included in the current sprint if capacity allows. Has a major user/business impact. |
| **Medium** | `P3`   | **Fix When Possible.** This issue should be addressed but does not block other work. It will be scheduled into a future sprint based on standard backlog priority.  |
| **Low** | `P4`   | **Fix if Time Allows.** This is a desirable fix but has low impact. It will only be addressed if there are no higher priority tasks. Can be deferred indefinitely.     |

## 6. Severity to Priority Mapping Matrix

This matrix provides the **recommended initial priority** based on a bug's severity. The final priority is subject to adjustment during the triage meeting.

| **Severity** | Recommended Initial **Priority** | Rationale                                                                        |
| :------------- | :------------------------------- | :------------------------------------------------------------------------------- |
| **SEV-1 Blocker** | **P1 - Urgent** | A blocker by definition requires immediate attention to unblock the team or project. |
| **SEV-2 Critical** | **P1 - Urgent** or **P2 - High** | Usually addressed urgently due to high impact on users or data integrity. May be P2 if a stable workaround exists and the fix is high-risk. |
| **SEV-3 Major** | **P2 - High** or **P3 - Medium** | Significantly impacts user experience and should be fixed soon. Can be P3 if it affects a smaller user segment or a less critical feature. |
| **SEV-4 Minor** | **P3 - Medium** or **P4 - Low** | A noticeable issue that should be fixed. Priority depends on visibility and user annoyance factor. |
| **SEV-5 Trivial** | **P4 - Low** | Cosmetic issues with no functional impact. Placed in the backlog to be fixed opportunistically. |

## 7. Overriding Priority

The Product Owner (`Béatrice`) has the final authority to change a bug's priority based on business goals, project roadmap, player feedback, and other strategic considerations. Any override of the matrix's recommendation must be discussed during the triage meeting and the rationale documented in the corresponding GitHub Issue.
