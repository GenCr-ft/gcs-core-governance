---
docId: OPS-GUIDE-015
title: S15 Agile Scrum Project Management
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
  - agile
  - scrum
  - project-management
  - collaboration
  - workflows
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-015.s15-agile-scrum-project-management.md
---
# S15: Agile Scrum Project Management Protocol

## 15.0. Justification and Objectives

**Why this protocol is critical for Gencraft and its AI Gems:**
Game development, especially for ambitious and innovative projects like
Gencraft's flagship, is characterized by evolving requirements, creative
iteration, and technical complexity. An Agile/Scrum framework provides a
structured yet flexible approach to:

- **Enhance Adaptability and Responsiveness to Change:** Allow Gencraft to
  embrace changing requirements and iterate on designs and features based on
  feedback and new insights.
- **Improve Predictability and Progress Visibility:** Provide regular cadences
  (Sprints) for delivering functional increments and for tracking progress
  against goals. This is crucial for `Antoine`'s project management and for
  Lug's oversight.
- **Foster Collaboration and Communication:** Promote close collaboration
  between different Gem roles and Crews (Design, Programming, Art, QA, etc.).
- **Focus on Delivering Value:** Prioritize work based on value to the project
  and Gencraft's strategic objectives.
- **Enable Continuous Improvement (Kaizen):** Incorporate regular reflection
  (Sprint Retrospectives) to improve team processes and Gem collaboration,
  feeding into S5: Lessons Learned.
- **Structure AI Gem Work:** Provide a framework for AI Gems to receive,
  process, and report on tasks within defined cycles, making their contributions
  more manageable and measurable by `Véra` (GCT-QAS-GPQA-001).

This S15 protocol aims to establish a clear, consistent, and effective
Agile/Scrum framework tailored to Gencraft's unique AI-driven virtual studio
environment.

## 15.1. Core Agile Principles Adopted by Gencraft

Gencraft embraces the core values and principles of the Agile Manifesto, adapted
for its virtual, AI-Gem-based workforce:

- **Individuals and Interactions** (Gems and their `Tool`-mediated
  collaboration) over Processes and Tools (while recognizing the need for robust
  protocols and `Tools` for AI Gems).
- **Working Software** (functional game builds, operational `Tools`, complete
  SSoT articles) over Comprehensive Documentation (but SSoT documentation in
  `gcs-core-governance` and `gcx-yyy` repos is still vital for AI
  understanding and studio memory).
- **Customer Collaboration** (Lug as a primary stakeholder, direct player
  feedback via Community Gems like `Fanny`/`Guillaume` - conceptual Gems) over
  Contract Negotiation.
- **Responding to Change** over Following a Rigid Plan (while maintaining a
  strategic roadmap managed by `Béatrice` (Product Manager)).

## 15.2. Gencraft's Scrum Framework Implementation

Gencraft will adopt core elements of the Scrum framework, managed primarily
through GitHub Issues and Project Boards within relevant `gcx-yyy`
repositories, adhering to `GH_001_Operational_Standards_Overview.md`.

### 15.2.1. Scrum Roles at Gencraft

- **Product Owner (PO):**
  - **Designated Gem:** `Béatrice` (GCT-MGT-SPM-001, Product Manager).
  - **Responsibilities:** Owns and manages the Product Backlog for the
      flagship game and other major studio products. Defines User Stories (using
      `user-story-template.md`) and Acceptance Criteria. Prioritizes backlog
      items based on strategic value, market feedback (potentially from `Iris`
      (Research Gem)), and Lug's directives. Represents the "voice of the
      customer/player" and studio vision. Accountable for maximizing the value
      of the work done by the development Crews.
- **Scrum Master (SM):**
  - **Designated Gem:** `Antoine` (GCT-MGT-PPM-001, Producer / Project
      Manager).
  - **Responsibilities:** Facilitates Scrum events. Ensures the Scrum process
      (this S15 protocol) is understood and followed by all Gems/Crews. Helps
      remove impediments reported by Crews. Coaches Crews in self-organization
      and cross-functionality. Protects the Crews from external distractions
      during a Sprint. Works with `Véra` to identify process inefficiencies and
      report on Agile metrics (S6).
- **Development Team(s) (Crews):**
  - **Composition:** Cross-functional groups of AI Gems from various
      departments (Design, Programming, Art, Audio, QA) assembled to work on
      specific projects or product increments (e.g., "Flagship Game Core
      Gameplay Crew," "Engine Feature Crew"). Crew composition can be dynamic,
      managed by `Antoine` and relevant Department/Crew Leads.
  - **Responsibilities:** Self-organize to complete the work selected for a
      Sprint. Create increments of "Done" product according to the Definition of
      Done (DoD). All members are collectively responsible for the quality and
      completion of their Sprint Backlog items.
- **Stakeholders:**
  - **Primary Stakeholder:** Lug (Studio Director), potentially represented by
      `Orion` (GCT-UTL-SLG-001, Studio Liaison Gem) for operational updates.
  - **Other Key Stakeholders:** Leads of departments not directly in a
      Development Crew but whose input is needed or who are impacted by the
      Increment (e.g., `Henri` (Legal Counsel) for compliance, Marketing Manager
      (`Charles` - conceptual Gem) for game features).

### 15.2.2. Scrum Events (Ceremonies) at Gencraft

- **The Sprint:**
  - **Duration:** A fixed length, time-boxed iteration (e.g., **2 or 3
      weeks**). The definitive duration will be decided by the Governance Crew
      and documented in `gcs-core-governance/02-knowledge-base-hub/KB-
      Domain-Project-Management/Agile-Scrum-Parameters.md` (To Be Created). A
      new Sprint starts immediately after the conclusion of the previous Sprint.
  - **Goal:** To deliver a "Done," usable, and potentially releasable product
      Increment.
  - **AI Gem Implication:** AI Gems' task management `Tools` must be aware of
      Sprint boundaries (start/end dates, Sprint Goal). `Véra` tracks progress
      within Sprints.
- **Sprint Planning:**
  - **When:** At the beginning of each Sprint.
  - **Participants:** Product Owner (`Béatrice`), Scrum Master (`Antoine`),
      and the entire Development Team (relevant Crew(s)).
  - **Purpose:** To collaboratively select Product Backlog Items (PBIs) for
      the Sprint and decompose them into a Sprint Backlog (a plan of tasks for
      the Sprint). A clear Sprint Goal is defined.
  - **Process:** `Béatrice` presents the highest priority PBIs. The Crew(s)
      discuss, estimate (if Gencraft adopts estimation - see `Agile-Scrum-
      Parameters.md`), and select the work they forecast they can complete.
      Tasks are created/updated as GitHub Issues and assigned to the Sprint
      milestone/project board.
  - **AI Gem Implication:** Lead Gems (or designated "planning" specialist
      Gems within Crews) use `Tools` to access the Product Backlog (GitHub
      Issues managed by `Béatrice`), contribute to effort estimation (if
      applicable, using historical data from `Véra` or their own heuristics),
      and populate/assign Sprint tasks in the Sprint Backlog. The Sprint Goal
      must be parsable and understood by all participating Gems.
- **Daily Scrum (Daily Stand-up):**
  - **When:** Daily, at the same time and virtual place, strictly time-boxed
      (e.g., 15 minutes).
  - **Participants:** Development Team(s) and Scrum Master (`Antoine`
      facilitates). Product Owner (`Béatrice`) is optional but encouraged to
      attend as an observer.
  - **Purpose:** For the Development Team to inspect progress toward the
      Sprint Goal and adapt the Sprint Backlog and upcoming planned work as
      necessary. It is a synchronization and impediment identification event,
      not a problem-solving session.
  - **Format (for each Gem or sub-team lead):**
        1. What did I/we complete yesterday that helped the Development Team
            meet the Sprint Goal? (Referencing specific Issue IDs and their
            status change).
        2. What will I/we do today to help the Development Team meet the Sprint
            Goal? (Referencing specific Issue IDs).
        3. Do I/we see any impediments that prevent me/us or the Development
            Team from meeting the Sprint Goal? (If yes, clearly state the
            impediment for `Antoine` to track).
  - **AI Gem Implication:** Each Gem (or its designated Crew representative
      Gem) **must** provide its update. This will be achieved via:
    - A `Tool: GenerateDailyScrumUpdate` that automatically formulates a
          concise status update based on its assigned GitHub Issues (status,
          progress) and any logged blockers.
    - `Antoine` uses a `Tool: AggregateDailyScrumReport` to collect these
          updates, log them (e.g., in a dedicated Discord channel or a daily KB
          page linked to the Sprint), and explicitly track identified
          impediments in a designated GitHub Issue list or board.
- **Sprint Review:**
  - **When:** At the end of the Sprint, before the Sprint Retrospective.
  - **Participants:** Product Owner (`Béatrice`), Scrum Master (`Antoine`),
      Development Team(s), key Stakeholders (including Lug via `Orion`).
  - **Purpose:** To inspect the Increment and adapt the Product Backlog if
      needed. The Development Team demonstrates the work that is "Done" and
      answers questions about the Increment.
  - **Process:** This is an informal meeting, not a status report. The focus
      is on the product Increment and collaborative discussion. Feedback from
      stakeholders is actively solicited and captured by `Béatrice`.
  - **AI Gem Implication:** Gems whose work contributed to the Increment may
      have their `Tools` generate automated demonstrations, visualizations, or
      provide data outputs for the review. `Béatrice` uses a `Tool:
      UpdateProductBacklogFromFeedback` to efficiently translate stakeholder
      feedback into new or modified Product Backlog Items (GitHub Issues).
- **Sprint Retrospective:**
  - **When:** After the Sprint Review and prior to the next Sprint Planning.
      This is the final event of the Sprint.
  - **Participants:** Product Owner (`Béatrice`), Scrum Master (`Antoine`),
      and the entire Development Team(s).
  - **Purpose:** To reflect on the past Sprint regarding individuals,
      interactions, processes, tools, and their Definition of Done. The goal is
      to identify and order the major items that went well and potential
      improvements, then create a plan for implementing improvements in the way
      the Scrum Team performs its work.
  - **Process:** `Antoine` facilitates this event. Key discussion points often
      include: "What went well during the Sprint?", "What could be improved?",
      "What will we commit to improve in the next Sprint?". Action items for
      improvement **must** be captured as actionable GitHub Issues (e.g., in a
      Crew's process improvement backlog or a central `gencraft-studio-
      improvement` repository) and assigned an owner and target.
  - **AI Gem Implication:** `Véra` (GCT-QAS-GPQA-001) may provide anonymized
      data on Gem/Crew performance, tool usage patterns, or common error rates
      during the Sprint to inform the Retrospective. `Antoine` uses a `Tool:
      LogRetrospectiveActions` to document key discussion points and track
      improvement action items. Significant learnings from Retrospectives
      **must** be considered for contribution to the SSoT via Protocol S5:
      Lessons Learned.

### 15.2.3. Scrum Artifacts at Gencraft (SSoT on GitHub)

- **Product Backlog:**
  - **SSoT:** A dynamic, prioritized list of all desired features, functions,
      requirements, enhancements, and fixes for Gencraft's product(s). Managed
      as **GitHub Issues** within a dedicated project backlog repository (e.g.,
      `gencraft-product-backlog`) or within the main project repositories (e.g.,
      `gencraft-flagship-game`), tagged and organized appropriately.
  - **Owner:** `Béatrice` (GCT-MGT-SPM-001, Product Owner) is solely
      responsible for its content, availability, and ordering.
  - **AI Gem Access:** Gems (especially Lead Gems and those involved in
      planning or requirement analysis) use `Tools` (e.g., `Tool:
      QueryProductBacklog`) to access, view, and potentially analyze items from
      the Product Backlog under `Béatrice`'s direction.
- **Sprint Backlog:**
  - **SSoT:** The set of Product Backlog items selected for the Sprint, plus a
      plan for delivering the product Increment and realizing the Sprint Goal.
      Managed as a **GitHub Project Board** and/or a **GitHub Milestone**
      containing the selected GitHub Issues for a specific Sprint.
  - **Owner:** The Development Team (Crew) owns the Sprint Backlog. Only the
      Development Team can change its Sprint Backlog during a Sprint (major
      scope changes impacting the Sprint Goal must be negotiated with the
      Product Owner).
  - **AI Gem Access:** Individual AI Gems view their assigned tasks (GitHub
      Issues) from the Sprint Backlog via their `Tool: ViewAssignedTasks` or
      equivalent interface with GitHub.
- **Increment:**
  - **Definition:** The sum of all Product Backlog items completed during a
      Sprint and all previous Sprints. At the end of a Sprint, the new Increment
      **must** be "Done" according to the Definition of Done (DoD) and be in a
      usable condition, potentially releasable.
  - **Definition of Done (DoD):** A shared, explicit understanding within
      Gencraft Studio of what it means for work to be complete to ensure a high
      level of quality and consistency. The Gencraft enterprise-level DoD
      **must** be documented in `gcs-core-governance/02-Knowledge-Base-
      Hub/KB-Domain-QA-And-Testing/definition-of-done.md` (To Be Created). This
      DoD typically includes criteria such as: code implemented, reviewed (S1),
      unit and integration tests passed, QA tested and approved by `Zoé` (QA
      Lead - conceptual Gem), documentation updated, and the increment
      integrated into the main baseline. Specific projects or Crews may extend
      the enterprise DoD with more stringent criteria.
  - **AI Gem Implication:** AI Gems' `Tool: MarkTaskAsDone` (or similar) might
      include automated checks or require explicit confirmation that all
      relevant DoD criteria are met before an Issue can be marked as complete.

## 15.3. Responsibilities in Gencraft's Agile/Scrum Framework

- **`Béatrice` (GCT-MGT-SPM-001, Product Owner):** Accountable for Product
  Backlog management, clear articulation of PBIs (User Stories, Acceptance
  Criteria), prioritization to maximize value, and ensuring the Development Team
  understands the vision and requirements.
- **`Antoine` (GCT-MGT-PPM-001, Scrum Master):** Accountable for the Scrum
  process (this S15 protocol) being adopted, understood, and used effectively.
  Facilitator of Scrum events, impediment remover, and coach for the Scrum Team
  on Agile principles and practices. Guardian of this S15 Protocol.
- **Crew Leads (or designated Lead Gems within Development Teams):** Responsible
  for guiding their Crew in Sprint Planning, managing the Crew's Sprint Backlog
  execution, facilitating Daily Scrums for their Crew if `Antoine` delegates,
  and ensuring the Crew collaborates effectively to deliver a "Done" Increment.
- **Development Team Gems (All members of active Crews):** Responsible for self-
  organizing to complete Sprint work, upholding quality standards (DoD),
  collaborating effectively with other Crew members, and proactively
  communicating progress and impediments.
- **`Véra` (GCT-QAS-GPQA-001, Gem Performance & Quality Analyst):** Provides
  objective data on Crew/Gem performance, adherence to DoD, cycle times, and
  other Agile metrics to inform Sprint Retrospectives and overall process
  improvement initiatives. Monitors adherence to key elements of this S15
  protocol.
- **`Orion` (GCT-UTL-SLG-001, Studio Liaison Gem):** Ensures Lug (Studio
  Director) and other key human stakeholders are appropriately informed of
  Sprint outcomes (e.g., via S6 reports derived from Sprint Reviews) and can
  participate effectively in key events like Sprint Reviews when necessary.

## 15.4. Traceability of Agile/Scrum Activities

- **Product Backlog & Sprint Backlogs:** GitHub Issues, Milestones, and Project
  Boards in relevant `gcx-yyy` repositories provide full traceability of
  work items, their status, assignments, and discussions. Linkage between PBIs,
  Sprint Backlog Items, and code commits/PRs is mandatory.
- **Sprint Goals:** Documented within the GitHub Sprint Milestone description or
  a pinned Issue for the Sprint, ensuring visibility for the Crew and
  stakeholders.
- **Impediments:** Tracked as specific GitHub Issues (e.g., labeled
  `type:impediment`, `status:blocked`) linked to the relevant Sprint and
  assigned for resolution. Discussed in Daily Scrums and managed by `Antoine`.
- **Sprint Review Outcomes:** Feedback and new requirements identified during
  the Sprint Review are captured by `Béatrice` and translated into new or
  updated Product Backlog Items (GitHub Issues) for future consideration. Key
  decisions from Sprint Reviews are logged as per S7.
- **Sprint Retrospective Action Items:** Captured as actionable GitHub Issues,
  assigned an owner, and tracked to completion. These contribute to Protocol S5:
  Lessons Learned.
- **Definition of Done (DoD):** A version-controlled SSoT document located at
  `gcs-core-governance/02-knowledge-base-hub/KB-Domain-QA-And-
  Testing/definition-of-done.md`.

## 15.5. Impact and Tooling for AI Gems

This Agile/Scrum framework is designed to be highly actionable by AI Gems,
supported by specialized `Tools`.

- **Core Task Management `Tools` (interfacing with GitHub Issues):**
  - `Tool: ViewAssignedTasks(sprint_milestone_filter, assigned_to_filter)`:
      Allows Gems to retrieve their tasks for the current Sprint.
  - `Tool: UpdateTaskStatus(issue_id, new_status_label,
      comment_markdown_optional)`: Enables Gems to update the status of their
      tasks.
  - `Tool: LogWorkOrBlocker(issue_id, comment_markdown,
      is_blocker_flag_optional)`: Allows Gems to log progress or report
      impediments.
  - `Tool: MarkTaskAsDone(issue_id,
      dod_checklist_confirmation_data_optional)`: Marks a task as complete,
      potentially requiring confirmation that DoD criteria are met.
  - `Tool: GenerateDailyScrumUpdate()`: Automatically formulates a Gem's daily
      update based on task progress and blockers.
- **`Tools` for `Béatrice` (GCT-MGT-SPM-001, Product Owner):**
  - `Tool: ManageProductBacklog`: Interface to create, edit, prioritize, and
      groom PBIs (GitHub Issues) in the designated backlog repository.
  - `Tool: AuthorUserStory` (with `Proximo` (GCT-UTL-PGEN-001) assistance): To
      write well-formed user stories, acceptance criteria, and link to parent
      Features/Epics.
  - `Tool: CaptureSprintReviewFeedback`: To structure and log feedback during
      Sprint Reviews and translate it into actionable PBIs.
- **`Tools` for `Antoine` (GCT-MGT-PPM-001, Scrum Master):**
  - `Tool: AggregateDailyScrumReport`: Collects and summarizes daily updates
      from Gems/Crews.
  - `Tool: ManageImpedimentLog`: Tracks and monitors the status of identified
      impediments.
  - `Tool: LogRetrospectiveActions`: Documents Retrospective outcomes and
      ensures improvement actions are created as trackable Issues.
  - `Tool: FacilitateSprintEvent`: (Conceptual) A tool to help `Antoine`
      manage the flow and timeboxing of Scrum events, potentially with
      checklists or prompts.
- **`Tools` for Crew Leads / Planning Specialist Gems:**
  - `Tool: SprintPlanningAssistant`: To view and filter the Product Backlog,
      select PBIs for a Sprint, assist with task decomposition, and populate the
      Sprint Backlog on a GitHub Project Board/Milestone. May include features
      for capacity consideration if estimations are used.
- **`Tools` for All Development Team Gems:**
  - Access to their Crew's Sprint Backlog (GitHub Project/Milestone) via their
      `Tool: ViewAssignedTasks`.
  - `Tools` to collaborate on tasks within the SSoT (e.g., Git commands via a
      `Tool`, PR creation/review `Tools` as per S1).
- **`Tools` for `Véra` (GCT-QAS-GPQA-001):**
  - `Tool: ExtractAgileMetrics`: To extract data from GitHub (e.g., Issue
      cycle time, Sprint goal completion rates, number of impediments, DoD
      adherence rates) to report on Crew and process performance as per S6.

This Agile/Scrum framework, supported by specialized AI Gem tooling, aims to
provide Gencraft Studio with a structured, adaptive, and efficient approach to
managing its complex development efforts. It emphasizes iterative delivery,
close collaboration between Gems and human supervisors, and a culture of
continuous improvement. This S15 protocol is a living document and will evolve
based on learnings (S5) and studio needs, under the governance of S13.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
