---
docId: OPS-GUIDE-003
title: S3 Emergency Management
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
  - governance-team
  keywords:
  - emergency-management
  - incident-management
  - gencraft
  - critical-blocking
  - ai-gems
  - incident-response
  - gemma
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-003.s3-emergency-management.md
---

# Oper. Protocol - Section 3: Emergency and Critical Blocking Issue Management

## 3.0. Justification and Objectives

**Why this protocol is critical for Gencraft and its AI Gems:**
Unforeseen emergencies and critical blockers are inevitable in complex projects
like game development, especially with a sophisticated technical infrastructure
(managed via `gcs-core-governance`) and AI-driven workforce. A swift,
coordinated, well-documented, and learning-oriented response is crucial to:

- **Minimize Impact:** Reduce the negative consequences of an incident on the
  project (schedule, budget, quality of deliverables from `gcx-yyy` project
  repositories), on the studio's operations (e.g., CI/CD pipelines), on its data
  integrity, and potentially on its community or reputation if Gencraft were
  live.
- **Ensure Business/Operational Continuity:** Restore normal studio operations
  and Gem productivity as quickly and safely as possible.
- **Maintain Clarity and Reduce Panic/Chaos:** Provide clear, predefined steps
  and communication channels (primarily GitHub Issues in `gencraft-operations`
  or `gencraft-incidents` repository) to prevent confusion among Gems and enable
  focused, collaborative problem-solving during high-stress situations.
- **Facilitate Effective and Efficient Problem Solving:** Mobilize the correct
  Gem expertise efficiently and ensure a structured, methodical approach to
  diagnosis and resolution, leveraging existing knowledge (e.g., Runbooks in
  `gcs-core-governance`).
- **Enable Learning and Prevention (Continuous Improvement):** Systematically
  analyze incidents after they occur (via Blameless Post-Mortems, documented in
  the KB) to understand root causes and implement robust measures to prevent
  recurrence or improve future responses. This feeds into the Gencraft Knowledge
  Base and informs `Gemma` for Gem blueprint updates in `gencraft-gem-
  blueprints`.
- **Provide Full Traceability for Audit and Review:** Maintain a comprehensive,
  immutable record of all events, actions, communications, and decisions related
  to an incident. This is vital for internal reviews by `Véra` or `Antoine`, and
  for demonstrating operational maturity.

This protocol aims to provide **Gencraft** with a resilient, adaptive, and
continuously improving framework for handling critical operational situations
effectively.

## 3.1. Gencraft Criticality/Impact Matrix

**How it works and why for AI Gems:** A standardized matrix is **mandatory** for
objectively assessing and prioritizing all reported incidents. This ensures a
consistent understanding of severity and guides the response level, critical for
AI Gems needing unambiguous triggers.

- **Definition & SSoT:** The matrix is defined in `gcs-studio-
  handbook/02-knowledge-base-hub/KB-Domain-DevOps-Infra/Incident-Management-
  Severity-Matrix.md`. It cross-references **Criticism** levels (technical
  scope) and **Impact** levels (consequences) to yield a **Global Priority
  Level** (P1-Critical to P4-Low).
- **Criteria Documentation:** The SSoT document details specific, measurable
  criteria for each "Criticism" and "Impact" level tailored to **Gencraft**
  (e.g., "number of Gems blocked," "impact on `gcp-aethel-server`," "data
  loss risk"). These criteria must be parsable by AI.
- **Tooling & Application:**
  - An `IncidentPriorityAssessorTool` (callable by Gems, especially `Véra` or
    DevOps Gems) **must** be used.
    - **Inputs:** Structured data on symptoms/impact, based on KB criteria.
    - **Logic:** Implements the Gencraft Criticality/Impact Matrix.
    - **Output:** Priority Level (P1-P4) and assessment summary.
  - The Priority Level (e.g., `priority:P1-critical`) **must** label the GitHub
    Issue tracking the incident.
- **Responsibility:** Reporting Gem/`Tool` for initial assessment; Incident
  Commander (IC) for re-evaluation and updates, documenting rationale in the
  incident Issue.

## 3.2. Identification and Qualification of Incidents

**How it works and why for AI Gems:** Correct identification and consistent
assessment ensure critical issues get immediate attention.

1. **Identification:**
    - **Who:** Any Gem (AI, including `Véra`'s `GemMalfunctionDetectorTool`,
      DevOps Gems' `SystemHealthMonitorTool`; or human, Lug via `Orion`).
    - **What to look for (AI Gem detection examples):** Repeated `Tool`
      failures, corrupted task inputs, unresponsive core services (Git, build
      server), security alerts from `Tools`.
2. **Initial Qualification & Reporting (Standardized Process):**
    - The identifying Gem/`Tool` **must** qualify:
        - **Emergency:** Requires immediate action to prevent significant
          ongoing/imminent damage.
        - **Critical Blocking Issue:** Prevents essential work on `gcx-yyy`
          projects, unresolvable by S1/S2 protocols.
    - The Gem/`Tool` **must** use the Gencraft Criticality/Impact Matrix (via
      `IncidentPriorityAssessorTool`) to set the initial Priority Level.
    - This information initiates an alert (see 3.3).

**Responsibility:** All Gems for vigilance and using `ReportCriticalIssueTool`;
`Véra` and DevOps Gems for specific monitoring.

## 3.3. Immediate Alerting and Initial Response Assignment

**How it works and why for AI Gems:** Rapid, standardized alerts and prompt IC
assignment are crucial. This must be highly automatable.

1. **Alert Channel & Mechanism (GitHub Issue as SSoT):**
    - A **new GitHub Issue must be created immediately** in `gencraft-
      operations` (or `gencraft-incidents`). This is the SSoT.
    - **Automated Issue Creation (`CreateIncidentReportTool`):** This `Tool` (used by reporting Gems/`Tools`):
        - Takes structured input (symptoms, reporter GemID, priority from `IncidentPriorityAssessorTool`).
        - Uses `incident-report-template.md` (from `gcs-core-governance/02-knowledge-base-hub/Templates/Issue-Templates/`) for title (e.g., "P1-CRITICAL: Auth Service Timeout - Reporter: @[GemID]") and body.
        - Applies labels: `type:incident`, `priority:[P1-P4]`, `status:alert-raised`.
        - **Automatically @mentions pre-defined IC(s)** and stakeholder groups  (e.g., `@gencraft-devops-team`).
    - **Lug Notification:** For P1s or on request, `Orion` (tasked via @mention or by `Antoine`/IC) informs Lug (summary, link to Issue) using `InformLugTool`.
2. **Incident Commander (IC) Assignment & Acknowledgment:**
    - An IC is immediately assigned (single point of authority/coordination).
    - **Pre-defined ICs/Escalation** (SSoT: `gcs-core-governance/01-operational-protocols/Incident-Commander-Assignments.md`
    - **New KB page to create*):** This document lists primary/backup ICs by incident type/domain, and SLA for acknowledgment (e.g., P1: 15 mins).
    - IC **must acknowledge** within SLA by commenting in the Issue (e.g., "Acknowledged, @[IC_GemID] is IC. Assessment ongoing."). `Véra` may monitor acknowledgment times via `SLAComplianceMonitorTool`.

**Responsibility:** Reporting Gem/`Tool` for alert; IC for acknowledgment; `Orion` for Lug notifications.

## 3.4. Continuous and Centralized Communication (GitHub Issue & Virtual War Room)

**How it works and why for AI Gems:** Centralized communication in the GitHub Issue ensures traceability and asynchronous participation. AI Gems need structured, parsable updates.

- **Primary Hub: GitHub Issue.** All updates, findings, actions, decisions **must** be comments here.
- **IC Responsibility for Updates:** Regular, factual, clear updates. Frequency per priority (defined in `Incident-Commander-Assignments.md`).
- **Standard Update Template (for IC's `Tool`):** Use `incident-update-template.md` (from `gcs-core-governance/02-Knowledge-Base-Hub/Templates/Document-Templates/`) covering: Status Summary, Impact, Actions Taken, Next Steps, Blockers, ETR.
- **Virtual War Rooms (P1s/critical P2s):**
  - **Purpose:** Rapid, focused, near real-time collaboration for the core resolution team.
  - **Mechanism:** Intensified communication within the GitHub Issue thread, marked "**WAR ROOM LOG:**". Key outcomes summarized back to the main Issue flow.
  - **AI Gem `Tools`:** `GitHubIssueMonitorTool` should prioritize/filter "WARROOM LOG" comments for active participants.
- **Target Audience:** Defined by IC; generally, involved Gems, Leads, `Antoine`, `Béatrice`, Lug (via `Orion`).

**Responsibility:** IC for updates; involved Gems for contributing info.

## 3.5. Resolution Process (Leveraging Runbooks from KB)

**How it works and why for AI Gems:** Structured, knowledge-driven resolution.
AI Gems excel at following predefined procedures.

1. **Diagnosis:**
    - IC mobilizes expert Gems.
    - **Runbook Consultation (Mandatory if available):** IC (or `Tool`) **must**
      consult KB (`gcs-core-governance/02-knowledge-base-hub/KB-Domain-
      DevOps-Infra/Runbooks/`) for matching Runbooks using `Iris`'s
      `AccessRunbookTool`.
    - Diagnostic steps (from Runbook or systematic investigation) **must** be
      documented in the Issue.
2. **Action Plan Development:** Based on diagnosis/Runbook, plan (steps, owners,
   outcomes, rollback) is documented in the Issue.
3. **Resolution Implementation:** Assigned Gems execute plan using their `Tools`
   (e.g., `ExecuteDevOpsCommandTool`). Progress reported in Issue.
4. **Validation & Monitoring:** Fix/workaround validated by relevant Gem(s)
   (e.g., `Zoé`). System monitored for stability. Validation steps should be in
   Runbook or defined by IC.
5. **Incident Closure:** IC confirms resolution, adds final summary (resolution,
   impact, Runbook used) to Issue. Label `status:resolved`.

**Responsibility:** IC (management, Runbook adherence); expert Gems (diagnosis,
implementation); QA/relevant Gems (validation).

## 3.6. Supporting Tools and Methods for Incident Management (Integrated)

**How it works and why for AI Gems:** Integral elements for effective,
AI-assisted incident management.

1. **Communication Status Pages (Internal - SSoT in KB):**
    - **Purpose:** Single SSoT for all Gems on critical internal system status
      (`gcs-core-governance/02-knowledge-base-hub/KB-Domain-DevOps-
      Infra/System-Status.md`).
    - **Mechanism:** Updated by IC (or delegated DevOps Gem via
      `UpdateSystemStatusPageTool`) during P1/P2 incidents, linking to the
      incident Issue.
    - **AI Gem Access:** Gems query via `SystemStatusQueryTool` before tasks.
2. **Runbooks / Playbooks (Operational Guides in KB - SSoT):**
    - **Purpose:** Pre-defined, versioned procedures for known incidents.
      Essential for consistent AI Gem action.
    - **Content & Storage:** Detailed steps for diagnosis, resolution, rollback,
      escalation, communication templates. Stored in `gencraft-studio-
      handbook/02-knowledge-base-hub/KB-Domain-DevOps-
      Infra/Runbooks/[IncidentType].md`.
    - **Usage & Maintenance:** **Must** be consulted by ICs. `Iris`'s
      `AccessRunbookTool` helps find them. **Must** be updated after Post-
      Mortems. Knowledge Guardians (`Adam`, Leads) responsible for their
      domains.
3. **"Blameless Post-Mortems" Culture (Guiding Principle):**
    - **Purpose:** Ensure learning and system improvement, not blame. Critical
      for honest AI Gem logging and `Véra`'s analysis.
    - **Implementation:** Explicitly stated in Post-Mortem template (`post-
      mortem-report-template.md`) and reinforced by `Antoine`/Leads.

## 3.7. Post-Incident Communication (Post-Mortem - Documented in KB)

**How it works and why for AI Gems:** Structured review for organizational
learning. AI Gems can contribute data and benefit from updated knowledge.

1. **Requirement & Culture:** Mandatory for P1/P2s, adhering to "Blameless"
   culture.
2. **Responsibility for Leading:** IC, with `Antoine` for major incidents. Key
   Gems (whose `Tools` or configurations might be implicated) **must** provide
   input (e.g., logs from their `Tools`).
3. **Objectives (Input for AI Analysis by `Iris`/`Véra`):** Timeline, Root
   Cause(s) (technical, process, Gem config/`Tool`), full impact, response
   evaluation (vs. protocol/Runbook), actionable/assigned/time-bound follow-up
   actions.
4. **Deliverable: Post-Mortem Report (SSoT in KB):** Markdown, using standard
   template, stored in `gcs-core-governance/02-knowledge-base-hub/Post-
   Mortems/[YYYY-MM-IncidentID].md`, linked from incident Issue.
5. **Sharing & Follow-up (Automated Tracking):** Shared with relevant
   Gems/Leads/Lug. Action items **must** be new, trackable GitHub Issues
   (`type:post-mortem-action`), linked to report, tracked by `Antoine`/Leads.
   `Véra` monitors Gem-related actions. Key learnings **must** update KB
   (Runbooks, protocols, `Gemma` blueprints). `Iris` may propose these
   integrations.

**Responsibility:** IC/`Antoine` (lead); involved Gems (input); assignees
(actions); `Iris` (KB integration of learnings).

## 3.8. Traceability of Incidents (Recap)

**How it works and why for AI Gems:** Complete, auditable, machine-parsable
trail.

- **Primary Trace (Operational Log SSoT): GitHub Issue** in `gencraft-
  operations`. Labels, comments, links are key data for `Véra`/`Iris`.
- **KB Traces (Analysis & Learnings SSoT):** Post-Mortem reports, updated
  Runbooks/protocols in `gcs-core-governance` (Git versioned).
- **Version Control (Git):** Code changes (in `gcx-yyy` project repos or
  `gencraft-infrastructure-config`) for fixes **must** link to incident Issue.

**Responsibility:** IC (Issue); relevant Gems (KB updates); all Gems (linking
work).

## 3.9. Impact and Tooling for AI Gems (Detailed)

**How it affects Gems and what `Tools` they need:** AI Gems are integral as
reporters, participants, and subjects of learning.

- **Detection & Alerting `Tools`:**
  - Monitoring Gems (`Véra`'s `GemMalfunctionDetectorTool`, DevOps'
    `SystemHealthMonitorTool`) **must** auto-trigger `CreateIncidentReportTool`.
  - `CreateIncidentReportTool` **must** use `IncidentPriorityAssessorTool` and
    `incident-report-template.md`.
  - Operational Gems use `ReportCriticalIssueTool` (which wraps
    `CreateIncidentReportTool`).
- **Participation in Resolution - Diagnostic `Tools`:**
  - Expert Gems need: `FetchSystemLogsTool`, `QueryMetricsTool`,
    `AccessRunbookTool` (from `Iris`), `ExecuteDiagnosticScriptTool` (securely,
    from `gcs-core-governance` repo).
- **Participation in Resolution - Action Execution `Tools` (Secure MCP Servers
  Preferred):**
  - `DeployCodeVersionTool`, `RestartServiceTool`, `ReconfigureSystemTool`,
    `RollbackChangeTool`. These **must** log execution details (to incident
    Issue or audit log).
- **Communication & Awareness `Tools`:**
  - `GitHubIssueMonitorTool` (to track incident Issue, filter "WAR ROOM LOG").
  - `SystemStatusQueryTool` (to check `System-Status.md` in KB).
- **Post-Mortem Contribution & Learning `Tools`:**
  - `AnalyzeIncidentDataTool` (for `Véra`/`Iris`).
  - `DraftPostMortemSectionTool` (using template).
  - `Gemma` **must** be able to query KB (via `Iris`'s `Tools`) for Post-Mortem
    learnings/Runbook updates to inform Gem blueprint updates in `gencraft-gem-
    blueprints`.
  - `Proximo` may learn to generate prompts incorporating safety checks from
    Post-Mortems.
- **Incident Commander Gem (Advanced Capability):**
  - An `Antoine-IC-Mode` or `GencraftIncidentCoordinatorGem` for well-defined,
    lower-priority incidents would need advanced orchestration `Tools`, deep
    Runbook understanding, and decision-making logic, with clear escalation to
    human ICs.

This detailed protocol aims to make **Gencraft** resilient, responsive, and
capable of continuous learning from critical operational situations, fully
leveraging its AI Gem workforce.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
