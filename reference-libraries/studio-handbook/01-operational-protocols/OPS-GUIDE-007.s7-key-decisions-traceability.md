---
docId: OPS-GUIDE-007
title: S7 Key Decisions Traceability
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
  - governance-team
  - contributors
  - ai-agents
  keywords:
  - operational-protocol
  - traceability
  - decision-management
  - ai-gems
  - kc-and-t
  - gencraft
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-007.s7-key-decisions-traceability.md
---
# Gencraft Operational Protocol - Section 7: Traceability of Key Decisions and Justifications

## 7.0. Justification and Objectives

**Why this protocol is critical for Gencraft and its AI Gems:**
Decisions are the pivotal moments that shape Gencraft's projects (e.g.,
`gencraft-flagship-game`), processes (defined in this
`gcs-core-governance`), tools (catalogued in
`gcs-core-governance/04-tooling-and-automation-hub/`), and overall
strategic direction. Without a rigorous and transparent system for tracing these
decisions and their rationales:

- **Loss of Context & "Corporate Amnesia":** The "why" behind a choice can be
  quickly forgotten, leading to repeated debates, inconsistent follow-up
  actions, or an inability to learn from past outcomes. This is especially
  problematic with an AI workforce (Gems like `Étienne`, `Isaac`, `Véra`) that
  relies on explicit, accessible knowledge from the KB.
- **Difficulty in Assessing Impact:** Without knowing the assumptions and
  justifications for a decision, it's hard to evaluate its actual impact later
  or to understand why a certain path was chosen over alternatives. This hinders
  `Véra`'s ability to analyze process effectiveness.
- **Reduced Accountability:** Clear traceability links decisions to deciders
  (specific GemIDs) and the information available at the time, fostering
  responsible decision-making as per Gencraft's values (see `gcs-studio-
  handbook/00-studio-vision-and-principles/studio-culture-and-values.md`).
- **Ineffective Onboarding/Context Transfer:** New Gems (instantiated by `Gemma`
  using `gcs-plt-gembp`) or existing Gems tackling new areas would
  struggle to understand the current state of affairs without access to the
  history of key decisions that shaped it.
- **Impeded Learning and Adaptation:** If Gencraft cannot revisit and understand
  its past decisions (successes and failures), its ability to learn and adapt (a
  core KC&T Guiding Principle #10) is severely hampered. `Iris` would lack
  crucial data for her analytical reports.
- **Incoherence in AI Gem Behavior:** AI Gems need to operate based on the
  latest, authoritative decisions. If these are not clearly traceable and
  accessible (via `KnowledgeBaseSearchTool` or specific decision-log `Tools`),
  their actions can become misaligned or based on outdated information.
- **Challenges in "Managing Your Manager" (Lug's Principle):** Provides Lug with
  a clear, reviewable record of his own strategic directives and their context,
  allowing for informed reflection, consistent messaging to the Gems (via
  `Orion`), and potential adjustments based on new information.

This protocol aims to ensure that every significant decision made within
Gencraft is:

- **Explicitly Documented:** The decision itself is clearly stated.
- **Contextualized:** The situation leading to the decision is understood.
- **Justified:** The rationale, data, and arguments supporting the decision are
  recorded.
- **Attributed:** The decider(s) (GemID or role) are clearly identified.
- **Timestamped:** The date of the decision is recorded.
- **Accessible:** Stored in a SSoT (primarily GitHub Issues/PRs within relevant
  `gcx-yyy` repositories and key strategic decisions in `gcs-studio-
  handbook`) for authorized Gems.
- **Versioned/Immutable (once made):** The record of the decision should be
  stable. Any subsequent *new* decisions that supersede it must also be traced,
  explicitly referencing and obsoleting the prior decision (as per Protocol
  S5.7).

## 7.1. General Principles for Tracing Decisions

These specific principles build upon Gencraft's overarching KC&T Guiding
Principles (ID: `gencraft_kct_guiding_principles_v2_enriched`):

- **Mandatory Documentation for Significant Decisions:** All decisions meeting
  predefined criteria of significance (see specific sections below) **must** be
  documented according to this protocol.
- **Rationale is as Important as the Decision:** The "why" (justification,
  alternatives considered and why rejected, data used) **must** be a core part
  of the traced record. This is vital for AI Gems to "understand" the decision
  beyond a simple instruction.
- **Context is King:** The information, discussions, and options considered
  leading up to a decision should be linked or summarized in the decision
  record.
- **Clear Decider(s) and Authority:** It **must** be unambiguous who had the
  authority to make the decision (as per `gcs-core-governance/00-Studio-
  Vision-And-Principles/studio-organization-and-roles.md`) and who ultimately
  made it.
- **Timeliness of Documentation:** Decisions should be documented as
  contemporaneously as possible with when they are made to ensure accuracy and
  completeness of context.
- **Centralization and SSoT on GitHub:** GitHub Issues and Pull Requests (in
  relevant `gcx-yyy` repositories) are the primary mechanisms for
  proposing, discussing, and formally recording most operational decisions. Key
  strategic decisions are also enshrined in Markdown files within `gencraft-
  studio-handbook` (versioned by Git).
- **Machine-Readability for AI Gems (KC&T Principle #11):** Decision records
  (especially summaries or key fields) **must** use structured formats (e.g.,
  specific Markdown sections with predictable headings, YAML frontmatter in
  decision documents, standardized GitHub Issue labels/templates from `gencraft-
  studio-handbook/02-knowledge-base-hub/Templates/`) to facilitate parsing and
  utilization by AI Gems and their `Tools`.

## 7.2. Decisions Arising from Disagreement Escalation (Cross-ref Protocol S2)

- **Description:** Decisions made at any level of the escalation process defined
  in "Section S2: Disagreement and Escalation Management" (ID:
  `gencraft_protocol_s2_disagreement_escalation_v3_review_en`). These are
  typically decisions resolving conflicting viewpoints on technical, design, or
  operational matters within a `gcx-yyy` project or process.
- **Method of Traceability (Recap & Detail for AI Gem processing):**
    1. The final decision and its comprehensive justification are **logged as a
       specifically formatted comment in the dedicated GitHub Issue** tracking
       the disagreement (Issue labeled `type:disagreement`).
    2. This comment **must** use the standardized template `decision-log-
       comment-template.md` (from `gcs-core-governance/02-Knowledge-Base-
       Hub/Templates/Issue-Templates/`) to ensure parsability by AI Gems. This
       template includes mandatory fields such as:
        - `**DECISION_MAKER_GEMID:** @[GemID_of_Decider_Role]`
        - `**DECISION_DATE:** YYYY-MM-DD`
        - `**DECISION_STATUS:** Final`
        - `**DECISION_SUMMARY:** [Clear, concise statement of the decision
          taken.]`
        - `**DECISION_RATIONALE:** [Detailed justification, referencing
          arguments from the Issue, relevant KB articles (e.g., from`gencraft-
          architecture` or `gcp-aethel-docs-gdd`), or data.]`
        - `**ALTERNATIVES_CONSIDERED_AND_REJECTED:** [Brief summary of other
          options and why they were not chosen, with links if applicable.]`
        - `**IMPACTED_GEMS_OR_SYSTEMS:** [List of GemIDs, roles, or system names
          primarily affected.]`
        - `**NEXT_ACTIONS_OR_LINKED_ISSUES:** [Links to new GitHub Issues
          created for tasks resulting from this decision.]`
    3. The Gem(s) making the decision at that escalation step are
       **responsible** for ensuring this comment is accurately logged using
       their `GitHubIssueCommentTool` (which **must** support template usage,
       potentially via `Proximo`).
    4. The Issue is then typically labeled `status:resolved` or
       `status:decision-made` by the decider or an automated `Tool`.
- **Responsibility for Trace:** The decider(s) at the relevant escalation level
  (Lead, Director, `Antoine`/`Béatrice`).
- **Impact on AI Gems:**
  - AI Gems involved in the disagreement (or whose work is affected) **must** be
    able to parse this structured decision comment via their
    `GitHubIssueMonitorTool` or a specialized `DecisionLogParseTool`.
  - Their core logic **must** then adapt their plans and actions to align with
    the decision. `Gemma` might use a history of such decisions (queried by
    `Iris`) to refine `backstory` elements related to problem-solving or
    adherence to authority for certain Gem roles defined in `gencraft-gem-
    blueprints`.

## 7.3. Decisions on Deliverable Approval or Rejection (Cross-ref Protocol S1)

- **Description:** Formal approval or rejection of key deliverables (code,
  documents, art assets, etc.) as part of the review process defined in "Section
  S1: Feedback and Approval of Deliverables" (ID:
  `gencraft_protocol_s1_feedback_approval_v3_review_en`).
- **Method of Traceability (Recap & Detail for AI Gem processing):**
    1. Traced via **GitHub Issues and/or Pull Requests** associated with the
       deliverables within the relevant `gcx-yyy` repositories.
    2. **Approval:**
        - For PRs: The formal "Approve" action in the GitHub UI by a designated
          approver Gem. The PR merge message **must** reference the approval and
          link to the relevant Issue if the PR is for a task. The merge itself
          signifies the decision.
        - For Issues (e.g., art asset approval): A comment from the designated
          approver Gem using a structured template (`deliverable-approval-
          comment-template.md` from `gcs-core-governance/02-Knowledge-Base-
          Hub/Templates/Issue-Templates/`) e.g., "**DELIVERABLE_APPROVAL
          (@[ApproverGemID]):** Approved. **VERSION_APPROVED:** [e.g., Commit
          SHA, Asset vX.Y]. **COMMENTS:** [Optional brief comments]." and the
          application of the `status:approved` label.
    3. **Rejection:**
        - For PRs: Closing the PR without merging, with a clear comment (using
          `deliverable-rejection-comment-template.md`) explaining the reasons
          for rejection.
        - For Issues: A comment from the approver Gem using the `deliverable-
          rejection-comment-template.md` e.g., "**DELIVERABLE_REJECTION
          (@[ApproverGemID]):** Rejected. **REASONS:** [Detailed, actionable
          reasons for rejection, linking to specific unmet criteria or feedback
          points]. **NEXT_STEPS_FOR_AUTHOR:** [e.g., 'Requires major rework
          based on feedback X, Y, Z. Please submit a new version for review.']."
          Application of the `status:rejected` label.
    4. All justifications for rejection **must** be clear, constructive, and
       actionable for the author Gem.
- **Responsibility for Trace:** The designated Gem approver(s) for the specific
  deliverable type (as per `gcs-core-governance/00-studio-vision-and-
  principles/studio-organization-and-roles.md`).
- **Impact on AI Gems:**
  - Author Gems **must** be able to parse the approval/rejection status and
    associated structured comments/reasons via their `Tools` to understand the
    outcome and next steps.
  - Downstream Gems (whose tasks depend on an approved deliverable) need `Tools`
    to verify the `status:approved` of prerequisites before starting their work.

## 7.4. Strategic Decisions and Directives from Lug (Studio Director)

- **Description:** High-level strategic decisions, major directional changes for
  Gencraft or its products, arbitrations on critical matters escalated to Lug,
  or specific directives issued by Lug that have broad studio-wide impact.
- **Method of Traceability Protocol (Recap & Detail for AI Gem processing):**
    1. **Initiation:** When a strategic question is posed to Lug (typically via
       `Orion`) and a formal decision/directive is expected.
    2. **Documentation Creation by `Orion` (or `Antoine`):**
        - A **new Markdown file** (e.g., `YYYY-MM-DD-lug-
          directive-[topic_slug].md`) **must** be created in `gencraft-studio-
          handbook/02-knowledge-base-hub/kd-domain-gem-ai-management/Lug-
          Directives/`.
        - This Markdown file **must** use the standard template `lug-directive-
          documentation-template.md` (from `gencraft-studio-
          handbook/02-knowledge-base-hub/Templates/Document-Templates/`). The
          template will enforce inclusion of structured YAML frontmatter and
          Markdown sections for:
            - `decision_id: LUG-DEC-YYYYMMDD-NNN` (auto-generated or assigned)
            - `date_decision: YYYY-MM-DD`
            - `author_gem_id_doc: @Orion` (or documenting Gem)
            - `validated_by_lug_status: [pending_final_review/confirmed_YYYY-MM-
              DD]`
            - `title: [Clear title of the decision/directive]`
            - `context_summary_markdown: [Brief of the situation/question, with
              links to relevant Issues or KB articles.]`
            - `options_considered_markdown: [Summary of key alternatives
              presented to Lug, if any.]`
            - `lug_decision_directive_markdown: [Lug's final decision or
              directive, stated clearly and unambiguously.]`
            - `lug_rationale_markdown: [Lug's detailed justification and
              reasoning, as conveyed to Orion.]`
            - `impacted_areas_gems_list: [List of Gencraft domains, Gem roles,
              or projects primarily affected, for`Iris`'s indexing]`
            - `follow_up_actions_required_json: [{action_description,
              responsible_lead_gem_id, target_issue_url (optional)} ]`
    3. **Submission via Pull Request (PR) to `gcs-core-governance`:** The
       new/updated Markdown file is submitted via a PR.
    4. **PR Description:** The PR description **must** summarize the decision
       and its purpose, state it documents a directive from Lug, and link to any
       original GitHub Issue that prompted the consultation.
    5. **PR Review (for Clarity, Completeness, and Acknowledgement by Studio
       Leadership):** The PR is reviewed by key Gems (`Antoine`, `Béatrice`,
       relevant Leads). Their review focuses on ensuring the decision and its
       context are accurately, clearly, and completely documented for studio
       operationalization. Their "approval" of the PR signifies acknowledgment
       and confirmation of the documentation's fidelity for studio use.
    6. **PR Merge (Formal Enactment after Lug's Final Validation):** After
       review and **Lug's final confirmation** (conveyed via `Orion`) that the
       Markdown accurately reflects his decision and rationale, the PR is merged
       by `Orion` or `Antoine`. This merge officially records the decision into
       the versioned Gencraft Knowledge Base.
- **Responsibility for Trace:**
  - **Lug:** For making the decision and validating the accuracy of its
    documentation.
  - **`Orion` (or `Antoine`):** For managing the entire documentation process
    (Markdown creation using `MarkdownAuthoringTool` with template support, PR
    submission using `PullRequestManagementTool`, merge coordination).
  - **Key Reviewers (`Antoine`, `Béatrice`, etc.):** For PR review to ensure
    documentation quality and operational understanding.
- **Impact on AI Gems:**
  - Strategic decisions documented this way become **authoritative SSoT articles
    in the KB**.
  - `Iris`'s `KBIndexerTool` **must** index these decision documents with high
    priority, making them searchable via `KnowledgeBaseSearchTool`. The
    structured frontmatter and content are key for this.
  - `Gemma` (Gem Generator) **must** consult these directives (especially if
    they impact studio structure, roles, or core project goals defined in
    `gcs-plt-gembp`) when configuring or updating Gem `backstories` or
    `goals`.
  - All Gems, when faced with tasks related to the directive, should be able to
    reference this SSoT via `KnowledgeBaseSearchTool`.

## 7.5. Dec. on Protocol or Studio Structure Modifications (Cross-ref Protocol S13)

- **Description:** Decisions to adopt new Gencraft operational protocols (new
  SX.md files), significantly amend existing ones, or make notable changes to
  the Gencraft studio structure (e.g., creating new departments, merging Gem
  roles, as documented in `gcs-core-governance/00-studio-vision-and-
  principles/studio-organization-and-roles.md`).
- **Method of Traceability (Recap & Detail for AI Gem processing):**
    1. **Proposal via GitHub Issue:** As per Protocol S13 (ID:
       `gencraft_protocol_s13_global_protocol_evolution_v1_en`), significant
       proposals are first discussed in a dedicated GitHub Issue in `gencraft-
       studio-handbook` (or `gencraft-studio-governance` repo) using `gop-
       evolution-proposal-template.md`.
    2. **Discussion and Approval by `Governance Crew`:** The `Governance Crew`
       reviews, discusses, and makes a decision. This decision (approved,
       rejected, modified) and its rationale are logged in the Issue using `gop-
       decision-comment-template.md`.
    3. **Documentation Change via Pull Request:** If approved, the actual
       changes to protocol documents (Markdown files in `gencraft-studio-
       handbook/01-operational-protocols/` or `../00-studio-vision-and-
       Principles/`) are made via a **Pull Request**.
    4. The PR description **must link to the original proposal/approval Issue**
       and summarize the approved changes.
    5. The PR is reviewed by the `Governance Crew` or designated approvers.
    6. The merge of the PR enacts the change.
- **Responsibility for Trace:** The Gem or crew proposing the change for
  initiating the Issue and PR; `Governance Crew` for the decision and PR
  approval.
- **Impact on AI Gems:**
  - All Gems' operational logic (potentially embedded in their `backstory` or
    `Tool` configurations) **must** be updated by `Gemma` or their maintainers
    to reflect significant changes in protocols or structure. This is a critical
    follow-up action from such decisions, tracked via a linked Issue.
  - `Véra` would update her audit criteria based on new/changed protocols.
    `Iris` would re-index changed protocol documents.

## 7.6. Importance of Justifications, Context, and Alternatives in Decision Traces

- **Principle:** For *all* types of decisions traced, the **rationale,
  justification, alternatives considered (and why rejected, if applicable), and
  relevant context** are as crucial as the decision itself. This information
  **must be explicitly and clearly documented** within the relevant GitHub
  Issue, PR description, commit message, or Markdown decision file, using the
  defined templates.
- **Impact on AI Gems:** This contextual information is vital for Gems
  (especially analytical ones like `Iris` or `Véra`, or operational Gems trying
  to understand the "spirit" of a rule or decision) to perform more effectively,
  to make better "local" choices aligned with global intent, and to facilitate
  future learning and adaptation for the studio. `Proximo` **must** be aware of
  the need for justification when helping Gems formulate decision proposals or
  records. `KnowledgeBaseSearchTool` should be able to retrieve not just
  decisions but also their rationales.

This detailed protocol for tracing key decisions ensures that **Gencraft**
maintains a robust, transparent, auditable, and "intelligent" decision memory,
supporting its long-term strategic goals, operational excellence, and the
effective functioning of its AI Gem workforce.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
