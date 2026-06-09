---
docId: OPS-GUIDE-019
title: S19 Action Item Management Protocol
version: 1.0.0
authors:
- AI Compliance Agent
creation_date: '2025-05-26'
last_updated_date: '2026-05-20'
language: en
metadata:
  scope: studio
  domain: governance
  doc-type: protocol
  lifecycle-stage: approved
  security-classification: l1_internal
  intended-audience:
  - contributors
  - ai-agents
  - project-managers
  keywords:
  - action-items
  - management
  - markdown-tracker
  - github-projects
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-019.s19-action-item-management-protocol.md
---
# S19: Action Item Management Protocol

## 1. Purpose

This protocol defines the standardized process for identifying, creating,
tracking, updating, and closing action items across the GenCr@ft project. The
aim is to ensure clarity, accountability, and timely resolution of all defined
actions not managed within specialized backlogs (e.g., development sprint
backlogs).

This protocol governs the dual-tracker model: the high-level design-roadmap is managed in `PRO-REPO-002.master-action-tracker.md`, while all active engineering, operational, and development tracking is fully migrated to GitHub Projects and domain-specific `STATUS.md` dashboards.

## 2. Scope

This protocol applies to all GenCr@ft team members and AI Gems involved in
identifying, assigning, or executing action items that are:

- Strategic in nature.
- Arise from meetings, decisions, or reviews.
- Require follow-up but do not immediately translate into a development user
  story or bug report in a sprint backlog.
- Necessary for the creation or maintenance of project documentation and
  operational infrastructure.

This protocol does **not** replace specialized task management within
development sprints (which may use GitHub Issues/Projects or other Agile tools
directly) but aims to consolidate higher-level or cross-cutting actions.

## 3. Definitions

- **Action Item:** A discrete task or activity that needs to be performed by one
  or more individuals to achieve a specific outcome, with defined deliverable(s)
  and/or acceptance criteria.
- **Interim SSoT (Single Source of Truth):** For the immediate future, the
  centralized Markdown-based "Master Action Tracker" file.
- **Future SSoT:** GitHub Projects (for detailed, operational, and development-
  related tasks).
- **Owner (Principal Responsible):** The single individual primarily responsible
  for driving the Action Item to completion, providing status updates, and
  seeking help if blocked. Other individuals may be involved or contribute.
- **Stakeholders:** Individuals or teams affected by or interested in the
  outcome of an Action Item.
- **Deliverable(s):** The tangible output(s) expected from the completion of an
  Action Item (e.g., an updated document, a decision record, a piece of code, a
  configured system).
- **Acceptance Criteria (ACs):** The conditions that must be met for the Action
  Item to be considered "DONE (Validated)".

## 4. The Interim Master Action Tracker (Markdown SSoT)

### 4.1. Location

- A new, central Markdown file will be created. Path: `GenCr-ft/gencraft-
  requirements/08_Project_Management/MASTER_ACTION_TRACKER.md`.
  - *(Rationale: Keeps project management artifacts co-located. The now-empty
      `GenCr-ft/actions.md` can be removed or repurposed to link to this new
      SSoT).*
- Existing actions from `GenCr-ft/gencraft-
  requirements/08_Project_Management/Action_Items_Tracker.md` and relevant, non-
  handbook-specific strategic actions from `GenCr-ft/gcs-studio-
  handbook/actions_KCnT.md` will be migrated to this new Master Action Tracker.
  The `actions_KCnT.md` file can continue to be used for the highly specific
  Handbook sanitization effort if its detailed workflow is preferred for that
  initiative by its managers.

### 4.2. Structure (Columns)

The Master Action Tracker will be a Markdown table with the following columns:

| ID         | Action Description                       | Source/Context (Link to Meeting, Decision, Doc) | Priority | Status     | Owner (Principal Responsible) | Contributor(s) (Optional) | Due Date   | Dependencies (Other Action IDs) | Notes / Acceptance Criteria / Deliverable(s)                    | Date Created | Date Last Updated | Reviewer(s) (For 'Pending Review') |
| :--------- | :--------------------------------------- | :---------------------------------------------- | :------- | :--------- | :---------------------------- | :------------------------ | :--------- | :------------------------------ | :-------------------------------------------------------------- | :----------- | :---------------- | :------------------------------- |
| `PROJ-XXX` | Clear, concise description of the action | e.g., `DECISION-007`, `Meeting_YYYYMMDD_Summary.md#section-X` | High/Med/Low | (See 4.3)  | Name (Single)                 | Name(s) / Team            | YYYY-MM-DD | e.g., `PROJ-YYY`                | **Deliverable(s):** ... <br> **ACs:** ... <br> **Notes:** ... | YYYY-MM-DD   | YYYY-MM-DD        | Name(s) / Crew                   |

**Note on Consistency:** For optimal readability and actionability (especially
by AI tools), it is crucial to maintain consistency in data formatting:

- Dates (Due Date, Date Created, Date Last Updated) must follow the `YYYY-MM-DD`
  format.
- Markdown links in `Source/Context` and IDs in `Dependencies` must be accurate
  and correctly formatted.

### 4.3. Status Legend

This legend adapts and refines statuses for broad project use:

- **`TO DO`**: The action has not been started or only very preliminary thought
  has been given.
- **`DRAFTED (Esquissé)`**: (Optional) A first draft of a deliverable exists or
  initial work has been done, but it's not yet in full progress or ready for
  review.
- **`IN PROGRESS`**: The action is actively being worked on. Intermediate
  results may exist.
- **`BLOCKED (Dependency)`**: The action cannot proceed until another specified
  action/event (noted in 'Dependencies' column) is completed.
- **`BLOCKED (Clarification)`**: The action cannot proceed until further
  information or clarification is received (details in 'Notes').
- **`PENDING REVIEW`**: A deliverable or proposal related to the action is ready
  and awaits review/validation from stakeholder(s) specified in the
  'Reviewer(s)' column (e.g., "Pending Review - Lug", "Pending Review -
  Governance Crew").
- **`DONE (Validated)`**: The action has been completed, and its primary
  deliverable(s)/outcome(s) have been validated by the specified reviewer(s).
  Ready for SSoT integration or formal closure.
- **`CLOSED (Integrated/Archived)`**: The action is fully completed, validated,
  deliverables are appropriately integrated into the SSoT (if applicable), and
  the action is formally archived by the Project Manager or Knowledge Guardian.
- **`CANCELLED`**: A decision has been made not to pursue this action. Rationale
  should be in 'Notes'.
- **`ON HOLD`**: Work on the action has been intentionally paused and may be
  resumed later. Rationale and expected resume conditions in 'Notes'.

### 4.4. ID System

- A simple, unique prefix `PROJ-` followed by a sequential number (e.g.,
  `PROJ-001`, `PROJ-002`) will be used for this Master Action Tracker to
  maintain simplicity and distinction from specialized trackers.

## 5. Process for Managing Action Items

### 5.1. Identification and Creation

- **Sources:** Actions can be identified from meetings, document reviews, ADRs,
  operational needs, or strategic planning sessions.

- **Creation:** Any team member can propose an action. The Project Manager (or a
  designated Lead/Crew for specific domains) is responsible for formally adding
  it to the `MASTER_ACTION_TRACKER.md` after ensuring it's well-defined.
- **Details:** When creating an action:
  - All relevant columns must be filled in as accurately as possible.
  - "Action Description" must start with an action verb and be specific enough
      to avoid ambiguity regarding the objective.
  - The creator must endeavor to define initial **"Deliverable(s)"** and
      **"Acceptance Criteria (ACs)"** upon creation. If not immediately
      possible, a note must be added indicating when and by whom these elements
      will be defined (before the action moves to `IN PROGRESS`).
  - If an action arises from a meeting, the `Source/Context` column **must**
      link to the specific meeting notes document and relevant section/page
      number (e.g.,
      `../meeting_notes/producer/2025-05-04_083007_User_Sync_Detailed_Summary.md#action-
      items`).

### 5.2. Assignment and Ownership

- Every action MUST have a single designated **Owner (Principal Responsible)**
  for accountability.

- Other individuals or teams involved can be listed as **Contributor(s)**.
- The Owner is responsible for driving the action to completion, providing
  status updates, and proactively communicating any blockers or anticipated
  delays.

### 5.3. Prioritization

- The "Priority" column (High, Medium, Low – definitions to be agreed upon and
  documented, e.g., High: Critical/Blocks others; Medium: Important/Flexible;
  Low: Desirable/When resources allow) should be set by the Project Manager or
  relevant Lead in consultation with stakeholders.

- Priorities must be reviewed regularly during project meetings.

### 5.4. Tracking and Updates

- **Owners** are responsible for updating the Status, Notes (including
  progress), and Due Date (if it changes) of their assigned actions in the
  `MASTER_ACTION_TRACKER.md` *at least weekly*, or immediately upon a
  significant change in status (e.g., becoming blocked, deliverable ready for
  review).

- All updates must include the `Date Last Updated`.
- Updates must accurately reflect the current state of the action, including any
  new relevant information in the "Notes" section.

### 5.5. Review Cycle

- The `MASTER_ACTION_TRACKER.md` will be a standing agenda item in regular
  project/team lead meetings.

- During these reviews:
  - Review `IN PROGRESS` items for progress and blockers.
  - Assign reviewers for items moving to `PENDING REVIEW`.
  - Review `PENDING REVIEW` items for validation and feedback.
  - Review `BLOCKED` items to identify and pursue resolutions for dependencies
      or clarifications.
  - Review `TO DO` items for assignment and prioritization.

### 5.6. Closure and Archival

- An action moves to `DONE (Validated)` once the Owner confirms completion of
  all ACs/Deliverables and the designated `Reviewer(s)` have validated the
  outcome (as per `s1-feedback-approval.md` if applicable).

- The Project Manager or a designated Knowledge Guardian moves items from `DONE
  (Validated)` to `CLOSED (Integrated/Archived)` once deliverables are confirmed
  to be integrated into the SSoT.
- At the end of each major project phase (e.g., MVP, MVP+1), `CLOSED` and
  `CANCELLED` items older than a defined period (e.g., 3 months) can be moved by
  the Project Manager to a separate `MASTER_ACTION_TRACKER_ARCHIVE_YYYY.md` file
  to keep the active list manageable.

### 5.7. Guidelines for Optimizing Actionability (Human and AI)

To ensure this tracker is a reliable and easily actionable source of
information, including by AI systems, the following best practices must be
observed:

- **Consistent Data Formatting:**
  - **Dates:** Always use the `YYYY-MM-DD` format (e.g., `2025-05-17`).
  - **Links:** Ensure Markdown links in `Source/Context` are valid and point
      to the relevant documents or sections. IDs in `Dependencies` must exactly
      match the IDs of the dependent actions.
- **Quality of Action Descriptions (`Action Description`):**
  - Start with a **clear action verb** (e.g., "Write...", "Analyze...",
      "Implement...", "Decide...").
  - Be **specific and unambiguous**. Avoid vague terms.
  - Must allow understanding of the main objective without requiring an in-
      depth reading of the notes (though notes provide detail).
- **Precision of Deliverables (`Deliverable(s)`):**
  - Describe the **tangible outputs** expected. Examples: "Specification
      document for X", "Functional prototype of Y", "Decision log Z published".
  - If multiple deliverables, list them clearly.
- **Clarity of Acceptance Criteria (`Acceptance Criteria (ACs)`):**
  - Define the conditions that must be met for the action to be considered
      `DONE (Validated)`.
  - ACs should be **SMART** (Specific, Measurable, Achievable, Relevant, Time-
      bound) as much as possible.
  - Formulate ACs so they are **testable/verifiable**. Examples: "Document X
      is approved by [Name/Role] and available at [Location Y]", "Feature Z is
      deployed to the staging environment and all associated integration tests
      pass."
- **Use of the `Notes` Section:**
  - For any contextual information that doesn't fit in other fields.
  - To track important discussion points, obstacles encountered, and solutions
      applied.
  - **(Optional - Advanced Practice):** For advanced AI analysis needs, the
      use of prefixed keywords can be considered for certain types of recurring
      information (e.g., `BLOCKER_TYPE: External`, `BUDGET_IMPACT: Yes`). This
      must be decided collectively if deemed useful.
- **Comprehensive Completion:**
  - Strive to fill all relevant columns for each action. An "Owner" and a
      "Priority" (even if "Low") are almost always necessary.

- **Completed Transition:** The transition to GitHub Projects and Bounded Workspaces is fully complete and operational.
- **The Dual-Tracker Model**:
  1. **Design & Planning Roadmap**: `gcs-project-management/PRO-REPO-002.master-action-tracker.md` remains the authoritative tracker for high-level strategic tasks (PROJ-NNN) across execution phases.
  2. **Active Engineering & Operations**: Domain-specific `STATUS.md` dashboards under `gcs-project-management/workspaces/<workspace-id>/STATUS.md` track the live status (Active Work, Blockers, Next Action) for each Bounded Workspace.
  3. **Execution View**: All active issues and Pull Requests are dynamically mapped onto **GitHub Project Board #16** (org-wide) and the specific domain project boards (#17, #18, #19, #20, #22).
- **Linking**: When a strategic `PROJ-NNN` task becomes active, a GitHub Issue is opened and linked to the tracking card, ensuring full traceability from the planning repository to the code-level PR.

## 7. Responsibilities

- **Project Manager (or designated Lead/Governance Crew):** Overall
  responsibility for maintaining the integrity of the
  `MASTER_ACTION_TRACKER.md`, ensuring new actions are well-defined (clear
  description, owner, initial priority, deliverables/ACs as per Section 5.7),
  facilitating review meetings, and ensuring the protocol is followed.
- **Action Owners (Principal Responsibles):** Responsible for executing their
  assigned actions, proactively communicating blockers or delays, and keeping
  their statuses and notes up-to-date.
- **All Team Members:** Responsible for identifying potential actions, proposing
  them for inclusion according to this protocol, and consulting the tracker for
  relevant information.

## 8. Protocol Review and Evolution

This protocol will be reviewed periodically (e.g., quarterly, or after major
project milestones) by the Governance Crew or Project Lead and updated as
necessary to reflect evolving project needs and the transition to new tools,
following `s13-global-protocol-evolution.md`.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
