---
docId: OPS-GUIDE-012
title: S12 Crew Specific Amendments
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
  - crew-specific-protocols
  - gops
  - amendments
  - governance
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-012.s12-crew-specific-amendments.md
---
# S12: Crew Specific Amendments

## 12.0. Justification and Objectives

**Why this protocol is critical for Gencraft and its AI Gems:**
While Global Operational Protocols (GOPs) provide essential consistency across
Gencraft, individual Crews may have unique workflows, tools (specific `Tools`
from `gcs-core-governance/04-tooling-and-automation-hub/` or custom ones),
or contexts that benefit from localized adaptations. A formal process for these
adaptations is crucial to:

- **Enable Localized Efficiency and Innovation:** Allow Crews to tailor
  processes to their specific needs, fostering ownership and potentially leading
  to more effective ways of working within their domain. This aligns with
  Gencraft's value of empowering its Gems.
- **Maintain Global Coherence and Prevent Fragmentation:** Ensure that local
  adaptations do not contradict Gencraft's core principles (KC&T Guiding
  Principles ID: `gencraft_kct_guiding_principles_v2_enriched`), strategic
  objectives, or negatively impact other Crews or studio-wide processes.
- **Provide a Clear, Traceable Framework for Local Adaptation:** Offer a
  structured process for proposing, reviewing, approving, documenting, and
  communicating Crew-Specific Protocols (CSPs). This ensures that adaptations
  are deliberate, understood, and their rationale (traced via GitHub Issues in
  Crew repositories like `gcs-core-governance`) is preserved.
- **Facilitate Learning and Best Practice Sharing Across Crews:** Allow
  successful local adaptations, identified by the `CrewOps Arbitrator`, to be
  potentially proposed as improvements to the GOPs for wider studio benefit
  (feeding into Protocol S13: "Proposing Evolution of Global Protocols").
- **Ensure Traceability of Local Adaptations:** Document the specifics and
  justification of how and why a Crew adapts or specifies a GOP for its local
  context. This is vital for `Véra`'s audits of Gem adherence to *all*
  applicable protocols (GOPs and CSPs) and for understanding process evolution.

This protocol aims to strike a balance between necessary studio-wide
standardization and beneficial local flexibility, enabling Gencraft to be both
robust and agile.

## 12.1. Key Definitions

- **Global Operational Protocol (GOP):** Any protocol defined in `gencraft-
  studio-handbook/01-operational-protocols/` (e.g., S1, S2, ... S11, and future
  global protocols like S13-S17). These apply studio-wide by default and are the
  SSoT for general operations.
- **Crew:** A defined team or department within Gencraft, typically with a
  designated Lead Gem (e.g., "DevOps Crew," "Art Department," "Game Design
  Team"), as listed and detailed in `gcs-core-governance/00-Studio-Vision-
  And-Principles/studio-organization-and-roles.md`.
- **Crew-Specific Protocol (CSP):** A documented adaptation, specification, or
  extension of one or more GOPs that applies *only* within a particular Crew. A
  CSP clarifies, details, or provides a local implementation variant of a GOP
  for that Crew's specific context. It **must not** fundamentally replace or
  negate a GOP unless an explicit deviation is justified and approved as per
  this protocol by the `CrewOps Arbitrator`.
- **Local Amendment:** A proposal to create a new CSP or modify an existing one.
- **Global Amendment:** A proposal to modify a GOP directly (covered by Protocol
  S13).
- **`CrewOps Arbitrator`:** A designated role responsible for overseeing the
  coherence of CSPs with GOPs and Gencraft's overall strategic objectives and
  guiding principles. This role is initially held by **`Antoine` (Producer)**.
  He is assisted in his analysis by `Véra` (Gem Performance & Quality Analyst),
  `Isaac` (Software Architect), and `Iris` (Research & Watch Specialist / KB
  Coherence). The mandate and support structure for the `CrewOps Arbitrator` are
  further detailed in `gcs-core-governance/00-studio-vision-and-
  principles/studio-organization-and-roles.md`.

## 12.2. Guiding Principles for Crew-Specific Protocols (CSPs)

All CSPs must adhere to the following principles:

- **Principle of Subsidiarity and Necessity:** A CSP should only be created if
  there is a genuine, documented need for local adaptation of a GOP that cannot
  be reasonably addressed by the GOP itself, and the adaptation is not broadly
  applicable or necessary for the entire studio. The default **must** be to
  follow the GOP.
- **Principle of Non-Contradiction (with GOPs and Gencraft Guiding
  Principles):** A CSP **must not** contradict Gencraft's 13 KC&T Guiding
  Principles (ID: `gencraft_kct_guiding_principles_v2_enriched`) or the
  fundamental intent and critical requirements of the GOP(s) it adapts.
  Explicit, justified deviations require prior consultation and formal approval
  from the `CrewOps Arbitrator`.
- **Principle of Clear Documentation and Accessibility (SSoT within Crew's
  Repository):**
  - Each CSP **must** be documented in **English** using Markdown, following the
    template `csp-document-template.md` (from `gencraft-studio-
    handbook/02-knowledge-base-hub/Templates/Document-Templates/`).
  - The SSoT for a Crew's CSPs is a designated folder, named precisely `crew-
    protocols/`, within that Crew's primary satellite GitHub repository (e.g.,
    `gcs-core-governance/crew-protocols/`, `gencraft-art-bible-and-assets-
    specs/crew-protocols/`). This location **must** be linked from the Crew's
    descriptive section in `gcs-core-governance/00-studio-vision-and-
    Principles/studio-organization-and-roles.md` and the index in `gencraft-
    studio-handbook/01-operational-protocols/README.md`.
  - CSPs must be easily accessible for review by all Crew members, the Crew
    Lead, the `CrewOps Arbitrator`, `Véra`, and `Iris` (via her indexing
    `Tools`).
- **Principle of Crew Lead Approval and Accountability:** All CSPs (and
  significant modifications thereto) **must** be formally reviewed and approved
  by the Lead Gem of the respective Crew. This approval signifies the Lead's
  accountability for the CSP's local application, its effectiveness, and its
  impact.
- **Principle of Coherence Review by `CrewOps Arbitrator`:** The `CrewOps
  Arbitrator` **must** be notified of all new or significantly modified CSPs and
  has the authority and responsibility to review them for coherence with global
  standards, to identify potential conflicts, redundancies, or learnings that
  could benefit other Crews or inform GOP evolution.

## 12.3. Process for Creating or Modifying a Crew-Specific Protocol (CSP)

**How it works and why for AI Gems:** This structured process ensures local
needs are addressed methodically while maintaining oversight. AI Gems within a
Crew need to be aware of and operate according to their local CSPs. Lead Gems
(even if AI) need appropriate `Tools` to manage this process effectively.

1. **Step 1: Identification of Need for Local Adaptation within a Crew**
    - **Trigger:** One or more Gems within a Crew (or the Crew Lead) identify a
      recurring issue, inefficiency, or ambiguity when applying a GOP to their
      specific tasks. Alternatively, they may develop a more effective local
      practice that warrants formalization as a CSP.
    - **Action:** The Gem(s) **must** first discuss this need internally within
      their Crew, facilitated by the Crew Lead. The goal is to confirm a genuine
      local need and explore if existing GOPs or minor clarifications suffice.
    - **For AI Gems:** An AI Gem might identify such a need if its `Tools`
      consistently encounter issues with a GOP in its specific operational
      context (e.g., a `Tool` reports that a GOP step is unimplementable with
      current Crew resources/`Tools`), or if `Véra`'s analysis of its
      performance within the Crew suggests a process friction point related to a
      GOP. The Gem would report this (structured finding) to its Lead.

2. **Step 2: Internal Crew Discussion and Proposal Formulation for CSP**
    - **Mechanism:** The internal Crew discussion and the initial proposal for a
      CSP **must** be traced via a **GitHub Issue** within the Crew's primary
      satellite repository (e.g., an Issue in `gcs-core-governance` for
      the DevOps Crew).
    - **Labels:** The Issue should be labeled appropriately (e.g., `type:csp-
      proposal`, `status:crew-discussion`, `gop-affected:S[X]`).
    - **Content (using template `csp-proposal-template.md` from `gcs-
      studio-handbook/02-knowledge-base-hub/Templates/Issue-Templates/`):** The
      Issue must detail the GOP in question, the specific problem or opportunity
      for local adaptation, the proposed solution or the core elements of the
      new/modified CSP, and initial thoughts on its benefits and potential
      impacts within the Crew.
    - **For AI Gems:** They use their `GitHubIssueManagementTool` to participate
      in or document these discussions. `Proximo` can assist in structuring the
      proposal content according to the template.

3. **Step 3: Formalization of the CSP Draft by the Crew**
    - **Action:** If the internal Crew discussion supports the idea, a
      designated Gem within the Crew (often the Lead, or a Gem with strong
      documentation `Tools` like `MarkdownAuthoringTool`) drafts the CSP as a
      Markdown document. This draft is created in a feature branch or a `/draft-
      crew-protocols/` folder within the Crew's satellite repository.
    - The draft CSP **must** use the `csp-document-template.md` and clearly
      state all required fields (CSP Title, Version, Related GOPs, Applicable
      Crew, Lead Approver, Date Proposed, Justification, Detailed Procedure,
      Alignment with Guiding Principles, Known Differences from GOP &
      Rationale).
    - **For AI Gems:** The `MarkdownAuthoringTool` (template-aware, potentially
      calling `Proximo` for content generation assistance) should be used. It
      must ensure all metadata fields in the template are addressed.

4. **Step 4: Review and Approval by Crew Lead**
    - **Mechanism:** The draft CSP **must** be submitted to the Crew Lead for
      formal review. This is done via a **Pull Request (PR)** in the Crew's
      satellite repository, targeting the branch where the final CSPs are stored
      (e.g., `main` branch, within the `crew-protocols/` folder).
    - **Criteria for Lead's Review:** The Crew Lead reviews for: necessity,
      clarity, effectiveness for the Crew, internal consistency, ease of
      application by their Gems, resource implications, and alignment with
      Gencraft's Guiding Principles and the spirit of the GOPs. They also check
      if the CSP might have unintended negative consequences for other Crews (if
      so, it might need to become a Global Evolution Proposal - S13).
    - **Traceability:** The Lead's feedback, any ensuing discussion, and the
      final approval (PR merge) or rejection (PR closed with rationale) are
      documented within the PR itself. The merge commit message should reference
      the approval.
    - **For AI Lead Gems:** They would use `PullRequestManagementTool`
      (potentially with a `CSPReviewChecklistTool` based on the criteria) and
      their decision logic would be based on these review criteria. They must
      document their approval rationale in the PR.

5. **Step 5: Documentation and Publication of Approved CSP in Crew's SSoT**
    - **Action:** Once approved and merged by the Crew Lead, the CSP Markdown
      document is officially part of the Crew's SSoT in their `crew-protocols/`
      folder.
    - The document's frontmatter YAML **must** be updated by the Lead (or their
      `Tool`) with `csp_version: 1.0` (or incremented), `status: enacted`,
      `date_enacted: YYYY-MM-DD`, `lead_approval_pr_link:
      https://docs.github.com/articles/merging-a-pull-request`.
    - The original GitHub Issue (`type:csp-proposal`) is updated with a link to
      the final CSP document in the Crew's repository and closed with a status
      like `status:csp-enacted`.
    - **For AI Gems:** `GitRepositoryTool` and `MarkdownFileReadWriteTool` (for
      frontmatter updates) are used.

6. **Step 6: Notification to `CrewOps Arbitrator` (`Antoine`)**
    - **Responsibility:** The Crew Lead is **responsible** for promptly
      notifying the `CrewOps Arbitrator` (`Antoine`) of the newly enacted or
      significantly modified CSP. This is a mandatory step for global coherence.
    - **Mechanism (Tool-assisted for AI Leads):**
        1. The Crew Lead (or a Gem delegated, using a `NotifyCrewOpsOfCSPTool`)
           creates a **new GitHub Issue** in the `gcs-core-governance`
           repository (or a dedicated `gencraft-studio-governance` repository).
        2. **Labels:** `type:csp-notification`, `status:pending-coherence-
           review`, `crew:[CrewName]`, `gop-related:S[X]`.
        3. **Assignee:** `@Antoine` (CrewOps Arbitrator).
        4. **Content (using template `csp-notification-template.md` from
           `gcs-core-governance/02-knowledge-base-hub/templates/issue-
           templates/`):** Must include Crew Name, direct link to enacted CSP,
           summary, confirmation of Lead approval (link to PR), and explicit
           statement of any perceived differences from GOPs.
    - **For AI Lead Gems:** Their `NotifyCrewOpsOfCSPTool` would use
      `CreateKCGovernanceIssueTool` with the specific template and assign it to
      `Antoine`.

## 12.4. Role and Process of the `CrewOps Arbitrator` (`Antoine`)

**How it works and why for AI Gems:** This central review by `Antoine` (assisted
by `Véra`, `Isaac`, `Iris` using their specialized `Tools`) ensures local
adaptations don't create studio-wide problems or deviate from core principles.
`Antoine` needs clear, structured input.

1. **Receiving Notification:** `Antoine` (or his `NotificationProcessingTool`)
   receives and acknowledges the `type:csp-notification` Issue.
2. **Coherence Review by `Antoine` (assisted by `Véra`, `Isaac`, `Iris`):**
    - `Antoine` reviews the CSP. May task (via linked Issues or `Tool` calls):
        - `Véra`: Assess impact on Gem consistency/performance across Crews
          (`CSPImpactAnalysisTool`).
        - `Isaac`: Review for technical coherence/conflicts
          (`TechnicalCoherenceReviewTool`).
        - `Iris`: Check for KB conflicts, ensure CSP discoverability
          (`KBConflictScanTool`).
    - Sub-reviews traced in the `type:csp-notification` Issue.
    - **Primary Checks by `Antoine`:** Genuine local need? Adherence to Guiding
      Principles? No major GOP conflict? No unacceptable risks/dependencies for
      others? Clear documentation?
3. **Dialogue and Resolution (if concerns):** `Antoine` discusses concerns with
   Crew Lead via the notification Issue.
4. **Formal Coherence Validation or Feedback by `Antoine`:**
    - **Validation:** If coherent, `Antoine` comments in Issue (using `csp-
      coherence-validation-comment-template.md`):
      "**CREWOPS_COHERENCE_VALIDATION (@Antoine):** CSP `[CSP_Name]` from Crew
      `[CrewName]` (link: `[URL_to_CSP]`) reviewed and validated for global
      coherence...". Issue labeled `status:coherence-validated` and closed.
    - **Request for Modification:** If issues, `Antoine` details them:
      "**CREWOPS_REVISION_REQUESTED (@Antoine):** CSP `[CSP_Name]` requires
      revision...". Issue `status:csp-revision-requested-by-crewops`. CSP not
      fully aligned until validation.
    - **Arbitration for Unresolvable Conflicts:** If dialogue fails, `Antoine`
      makes final call (reject CSP or approve with caveats), consulting Lug (via
      S7.4) for strategic deviations. Decision documented.
5. **Identification of GOP Improvement Needs:** If multiple Crews create similar
   CSPs, or a CSP reveals GOP flaws, `Antoine` initiates a PGE for the GOP
   (Protocol S13).

## 12.5. Documentation, Accessibility, and Visibility of CSPs

**How it works and why for AI Gems:** CSPs must be discoverable by Crew members
and oversight Gems. AI Gems need to reliably find and apply the correct
protocol.

- **SSoT for CSPs:** The `crew-protocols/` folder in each Crew's primary
  satellite `gcx-yyy` repository. Each CSP is a versioned Markdown with
  standardized frontmatter (including `crew_name:`, `gop_adapted:`, `status:
  enacted`, `crewops_validation_issue: [link]`).
- **Visibility in `gcs-core-governance` (Central Hub):**
  - `gcs-core-governance/01-operational-protocols/README.md` (or a linked
    `S12-Appendix-Crew-Specific-Protocols.md`) **must** have an "Index of Crew-
    Specific Protocol (CSP) Locations."
  - This lists each Crew and links to their `crew-protocols/README.md` in their
    satellite repo.
  - Each Crew's `crew-protocols/README.md` lists its own enacted, validated
    CSPs.
- **Indexing by `Iris`:**
  - `Iris`'s `KBStructureCrawlerAndIndexerTool` **must** be configured (via
    manifest in `gcs-core-governance`) to crawl and index these declared
    `crew-protocols/` folders.
  - `KnowledgeBaseSearchTool` results **must clearly indicate** if info is from
    a GOP (global) or a CSP (local to Crew X), using CSP frontmatter.

## 12.6. Impact and Tooling for AI Gems

- **All Gems within a Specific Crew:**
  - `backstory` (from `Gemma` via `gcs-plt-gembp`) **must** state they
    are bound by their Crew's enacted, validated CSPs (found via `Iris` in their
    Crew's `/crew-protocols/`) in addition to GOPs; CSPs take precedence
    locally.
  - `KnowledgeBaseSearchTool` **must** find and prioritize relevant CSPs for
    their tasks.
  - `Tools` for proposing CSPs (e.g., `ProposeCSPTool` using
    `GitHubIssueManagementTool` with templates for their Crew's repo).
- **Lead Gems (Human or AI):**
  - `Tools` to manage CSP lifecycle in their Crew's repo (review PRs, approve
    Issues, `GitRepositoryTool`).
  - `NotifyCrewOpsOfCSPTool` (using `CreateKCGovernanceIssueTool` with `csp-
    notification-template.md`) for `Antoine`.
- **`Antoine` (as `CrewOps Arbitrator`, AI-assisted):**
  - `Tool` to monitor/manage `type:csp-notification` Issues.
  - `CSPCoherenceAnalysisTool` (advanced, using `Véra`/`Isaac`'s `Tools`).
  - `Tool` to generate structured "Coherence Validation" comments.
- **`Iris` (global KB management):** `KBStructureCrawlerAndIndexerTool`
  configured for CSPs. Search results logic differentiates GOPs/CSPs.
- **`Véra` (Gem quality/process audit):** Accesses validated CSPs (via `Iris`)
  to understand local context for audits.

This protocol allows Gencraft to balance studio-wide standardization with
Crew-level agility and expertise.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
