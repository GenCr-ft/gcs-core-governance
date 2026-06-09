---
docId: GCS-GUIDE-403
title: "The Agile Project Management Playbook"
version: 1.1.0
status: Approved
date: 2025-06-18
last_updated_date: '2026-05-26'
authors:
  - "Technical Governance"
  - "Product Management"
knowledgeGuardian:
  - "Lead Product Manager"
  - "Scrum Master"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/04-process-guides/GCS-GUIDE-403.agile-playbook.md
metadata:
  lifecycle-stage: approved
  domain: engineering
  doc-type: guide
  scope: studio-wide
  security-classification: l2_confidential
  keywords:
    - "agile"
    - "scrum"
    - "process"
    - "playbook"
    - "project-management"
---

# The Agile Project Management Playbook

## 1. Objective

This guide defines the studio's official implementation of the **Scrum framework**. Its purpose is to create a predictable, transparent, and continuously improving process for delivering high-quality software. This playbook is the single source of truth for how our teams operate, plan, and collaborate.

## 2. Our Scrum Framework

We use Scrum to manage complex product development. It is built upon roles, events, and artifacts.

### 2.1. Roles and Responsibilities

Clearly defined roles are essential for a successful team.

* **Product Owner (PO):**
  * **Mission:** To maximize the value of the product resulting from the work of the Development Team.
  * **Responsibilities:** The PO is the sole person responsible for managing the **Product Backlog**. This includes creating, prioritizing, and clearly communicating backlog items. The PO represents the stakeholders and is the voice of the customer.

* **Scrum Master (SM):**
  * **Mission:** To help the team understand and enact Scrum theory, practices, rules, and values.
  * **Responsibilities:** The SM is a servant-leader for the team. They facilitate Scrum events, help remove impediments blocking the team's progress, and coach the team in self-organization and cross-functionality.

* **The Development Team:**
  * **Mission:** To deliver a potentially releasable Increment of "Done" product at the end of each Sprint.
  * **Responsibilities:** The team is self-organizing and cross-functional. They have all the skills necessary to create the product increment. They are responsible for estimating work, creating the Sprint Backlog, and holding each other accountable for quality and progress.

### 2.2. The Scrum Events (Ceremonies)

These events create regularity and minimize the need for meetings not defined in Scrum. All events are time-boxed.

* **The Sprint:**
  * A time-box of **two weeks** during which a "Done," usable, and potentially releasable product Increment is created.

* **Sprint Planning:**
  * **Purpose:** To plan the work to be performed for the Sprint.
  * **Procedure:** The PO presents the prioritized Product Backlog items. The Development Team selects the amount of work they believe they can complete and forecasts the functionality that will be developed. The result is the **Sprint Backlog** and the **Sprint Goal**.

* **Daily Stand-up:**
  * **Purpose:** A daily 15-minute meeting for the Development Team to synchronize activities and create a plan for the next 24 hours.
  * **Format:** Each team member answers three questions:
        1. What did I do yesterday that helped the team meet the Sprint Goal?
        2. What will I do today to help the team meet the Sprint Goal?
        3. Do I see any impediment that prevents me or the team from meeting the Sprint Goal?

* **Sprint Review:**
  * **Purpose:** To inspect the Increment and adapt the Product Backlog if needed.
  * **Procedure:** The Development Team demonstrates the work that it has "Done" and answers questions. The PO discusses the Product Backlog as it stands. It is an informal meeting, not a status meeting, and the presentation of the Increment is intended to elicit feedback and foster collaboration.

* **Sprint Retrospective:**
  * **Purpose:** An opportunity for the Scrum Team to inspect itself and create a plan for improvements to be enacted during the next Sprint.
  * **Procedure:** The team discusses what went well during the Sprint, what problems it ran into, and how those problems were (or were not) solved. The team identifies the most helpful changes to improve its effectiveness.

### 2.3. Scrum Artifacts

* **Product Backlog:**
  * An ordered list of everything that is known to be needed in the product. It is the single source of requirements for any changes to be made to the product.
  * Managed exclusively by the **Product Owner**.

* **Sprint Backlog:**
  * The set of Product Backlog items selected for the Sprint, plus a plan for delivering the product Increment and realizing the Sprint Goal.
  * It is a forecast by the Development Team about what functionality will be in the next Increment.
  * Owned and managed by the **Development Team**.

* **The Increment & The Definition of "Done" (DoD):**
  * The Increment is the sum of all the Product Backlog items completed during a Sprint and the value of the increments of all previous Sprints.
  * An item cannot be part of the Increment unless it meets our **Definition of "Done"**. The DoD is a shared understanding of what it means for work to be complete.
  * **Our Official Definition of "Done":**
        1. Upstream gates (**Refine → Design → Plan**) are fully satisfied, sibling `[DESIGN]` child sub-issue is officially closed, and approved plan is commented on the parent issue.
        2. Code is written, adheres to TDD commit cycles, and is peer-reviewed [cite: GCS-GUIDE-201].
        3. All automated tests (unit, integration) are passing [cite: GCS-GUIDE-203].
        4. CI pipeline is green [cite: GCS-GUIDE-202].
        5. Meets all refined Acceptance Criteria (formatted as Gherkin scenarios) [cite: GCS-GUIDE-401].
        6. Validated by the QA team [cite: GCS-GUIDE-404].
        7. Product Owner accepts the story.
* **Sprint Goal:**
  * The Sprint Goal is the single objective for the Sprint. It is created during Sprint Planning and provides guidance to the Development Team on why it is building the Increment.
  * The Sprint Goal is a commitment that the team makes to itself and to the stakeholders.

## 3. Our Agile Playbook — The Upstream Development Gates

To prevent "dark updates" (unplanned or undocumented changes) and guarantee high-quality engineering, every Scrum team and automated agent in our studio must follow the **Refine → Design → Plan → Code** sequence. Development must not start on any work item until the three upstream gates are satisfied.

### 3.1. The Upstream Gate Sequence

1. **Refining the Backlog (Gate 1 — Refine)**:
   * Prior to cutting a development branch, the assignee (human or agent) performs a thorough codebase design audit.
   * Gaps or ambiguities in the issue's requirements are resolved.
   * Acceptance Criteria are refined into concrete, testable Gherkin scenarios (Given/When/Then) and updated directly in the parent issue body.

2. **Technical Architecture (Gate 2 — Design)**:
   * A sibling child issue with the `[DESIGN]` prefix is created to document data models, interface signatures, schemas, and rejected alternative approaches.
   * If the work modifies core systems (e.g. wire formats, serialization, authentication/authorization, or persistence schemas), a new Architectural Decision Record (ADR) must be authored in `gcp-aethel-architecture` and formally approved.

3. **Execution Mapping (Gate 3 — Plan)**:
   * A concrete implementation plan (`implementation_plan.md`) is authored, detailing all files to be modified/created and the precise test strategies.
   * The plan is posted as a comment on the parent GitHub Issue for supervisor/lead architect approval.
   * Once approved, the `[DESIGN]` child sub-issue is officially closed with a link to the plan comment.

4. **TDD Cycle (Gate 4 — Code)**:
   * Only after Gates 1, 2, and 3 are verified can branch development begin.
   * Development follows a strict Test-Driven Development (TDD) red → green → blue cycle.

## 4. Continuous Improvement

We are committed to continuously improving our Scrum practices. After each Sprint, we reflect on our processes and make adjustments as needed. This is a key part of the Scrum framework and helps us adapt to changing circumstances and improve our effectiveness.

## 5. Conclusion

This Agile Project Management Playbook is our commitment to delivering high-quality software in a predictable, transparent, and continuously improving manner. By adhering to the Scrum framework and our studio's specific practices, we ensure that our teams are aligned, focused, and empowered to deliver value to our stakeholders.

## 6. References

* [Scrum Guide](https://scrumguides.org/scrum-guide.html)
