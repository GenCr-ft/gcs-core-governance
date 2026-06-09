---
docId: OPS-GUIDE-011
title: S11 External Communication
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
  - communications-team
  keywords:
  - external-communication
  - governance
  - communication-protocols
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-011.s11-external-communication.md
---
# S11: External Communication Protocol

## 11.0. Justification and Objectives

**Why this protocol is critical for Gencraft and its AI Gems:**
Official external communications shape Gencraft's reputation, build
relationships, and can have significant strategic, legal, and business
implications. A clear protocol is essential to:

- **Ensure Consistent and Professional Messaging:** Project a unified and
  professional image of Gencraft to all external stakeholders.
- **Control Information Disclosure:** Manage what information about Gencraft
  (projects, technology, strategy) is shared externally, when, and by whom,
  protecting confidential information (as per Protocol S8).
- **Align External Communications with Studio Strategy:** Ensure all official
  statements and engagements support Gencraft's overall vision (from `Gencraft-
  AI-Studio-Brief.md`), product roadmap (from `gcp-aethel-docs-req`), and
  business objectives.
- **Mitigate Legal and Reputational Risks:** Prevent unauthorized or inaccurate
  statements that could harm Gencraft. `Henri` and `Léo` play a key role here.
- **Streamline Approval Workflows:** Provide a clear process for drafting,
  reviewing, and approving official external communications.
- **Maintain a Traceable Record:** Keep a log of significant external
  communications and commitments made.

This protocol aims to establish a framework for managing Gencraft's official
voice to the non-player world.

## 11.1. Core Principles for External Communication

- **Official Spokesperson(s) Only:** Only designated Gencraft Gems are
  authorized to speak officially on behalf of the studio to external parties
  covered by this protocol.
- **Accuracy and Truthfulness:** All external communications must be factual,
  accurate, and not misleading.
- **Professionalism and Respect:** Maintain a professional and respectful tone
  in all interactions.
- **Confidentiality:** Adhere strictly to Gencraft's information classification
  policies (Protocol S8) regarding what can be shared externally.
- **Strategic Alignment:** All communications must be aligned with Gencraft's
  approved messaging, brand guidelines (to be developed by `Charles`), and
  strategic goals.
- **Legal and Ethical Compliance:** All communications must comply with
  applicable laws, regulations, and ethical standards. `Henri` and `Léo` provide
  guidance.
- **Internal Approval Before Release:** Significant external communications
  require internal review and approval as defined in this protocol.

## 11.2. Scope of This Protocol

This protocol applies to:

- Press releases and media inquiries.
- Communications with potential or existing business partners, distributors, or
  publishers (`Delphine`).
- Presentations at industry conferences or events.
- Official statements on Gencraft's website (if not purely community-focused) or
  official studio social media channels (distinct from `Fanny`'s community
  engagement channels).
- Responses to formal inquiries from regulatory bodies or legal entities.
- Communications related to investment or funding (if applicable in the future).

This protocol does **not** cover:

- Routine community engagement on forums, Discord, or Gencraft's player-facing
  social media (managed by `Fanny`).
- Direct player support interactions (managed by `Guillaume`).
- Informal technical discussions by Dev Gems at approved, public technical
  forums (guidelines for this may be a separate, simpler policy).

## 11.3. Designated Official Spokespersons for Gencraft

- **Primary Strategic Communications (Vision, Major Announcements, Crisis
  Comms):** Lug (Studio Director, represented and facilitated by `Orion`).
- **General Studio Operations, Project Status, Production Matters:** `Antoine`
  (Producer).
- **Product Vision, Roadmap, Market Positioning:** `Béatrice` (Product Manager).
- **Marketing Strategy, Branding, Promotional Campaigns:** `Charles` (Marketing
  Manager).
- **Business Development, Partnerships, Sales Negotiations:** `Delphine` (Sales
  & Biz Dev Manager).
- **Legal Matters, Formal Notices:** `Henri` (Legal Counsel).
- **Specific Technical Expertise (e.g., Engine, PCG, AI):** `Isaac` (Software
  Architect), `Julien` (Lead Developer), or other expert Gems may be designated
  to speak on their specific domain *after express approval and briefing* by
  `Antoine` or `Béatrice` for a particular engagement.

**Note:** No other Gem is authorized to make official statements on behalf of
Gencraft to external parties covered by this protocol without explicit prior
authorization from `Antoine` or Lug (via `Orion`).

## 11.4. Process for Initiating, Drafting, Reviewing, and Approving External Communications

**How it works and why for AI Gems:** This structured workflow ensures all
official external communications are vetted and aligned. AI Gems may be involved
in drafting initial content or providing supporting data.

1. **Step 1: Identification of Need and Initial Proposal**
    - **Trigger:** An opportunity or requirement for external communication
      arises (e.g., media inquiry, partnership opportunity, planned
      announcement).
    - **Action:** The Gem identifying the need (typically one of the designated
      spokespersons, or a Lead Gem) **must** create a **GitHub Issue** in a
      dedicated repository (e.g., `gencraft-studio-communications` or within
      `gencraft-studio-management`).
    - **Labels:** `type:external-comm-request`, `status:proposal`,
      `audience:[press/partner/investor/etc.]`.
    - **Content (using template `external-comm-proposal-template.md` from
      `gcs-core-governance/02-knowledge-base-hub/Templates/Issue-
      Templates/`):**
        - Purpose of communication.
        - Target audience.
        - Key messages to convey.
        - Proposed spokesperson(s).
        - Desired channel(s) and timing.
        - Any known sensitivities or risks.
    - **Initial Approval to Proceed:** `Antoine` and/or `Béatrice` review the
      proposal. If aligned with studio strategy, they approve proceeding to
      draft.

2. **Step 2: Drafting the Communication Material**
    - **Responsibility:** The designated lead spokesperson (e.g., `Charles` for
      a marketing piece, `Delphine` for a partnership proposal) or a Gem tasked
      by them (e.g., `Iris` might draft an initial factual summary, `Proximo`
      might help a spokesperson Gem structure their thoughts).
    - **Content:** Draft of the press release, presentation slides, official
      statement, email, etc. (stored as Markdown or other appropriate format in
      a branch or attached to the Issue).
    - **SSoT for Drafts:** Drafts are managed in a version-controlled manner,
      linked to the GitHub Issue.
    - **Tooling for AI Gems:** `MarkdownAuthoringTool`,
      `PresentationDraftingTool` (if AI can generate slide outlines), `Proximo`
      for structuring and tone.

3. **Step 3: Internal Review and Iteration**
    - **Mandatory Reviewers (as applicable, tagged in the Issue/PR):**
        - **`Antoine` (Producer):** For operational impact, resource
          implications, general studio alignment.
        - **`Béatrice` (Product Manager):** For product vision and strategic
          messaging alignment.
        - **`Charles` (Marketing Manager):** For branding, marketing messaging,
          GTM alignment.
        - **`Delphine` (Sales & Biz Dev Manager):** For business implications,
          partner relations.
        - **`Henri` (Legal Counsel) & `Léo` (OSS Specialist):** **Mandatory
          review for ALL external communications** to check for legal risks, IP
          issues, confidentiality breaches, and OSS compliance implications.
        - **Relevant Technical/Domain Experts (e.g., `Isaac`, `Julien`,
          `Étienne`):** If the communication contains technical or specific game
          design details.
        - **`Iris`:** To fact-check claims or provide supporting data if needed.
    - **Mechanism:** Feedback provided as comments on the GitHub Issue or via a
      PR if the draft is a version-controlled document. Iterations are made by
      the drafting Gem.
    - **Tooling for AI Gems:** Reviewer Gems use `GitHubIssueCommentTool`.
      Drafting Gems use editing `Tools`.

4. **Step 4: Final Approval**
    - **Approval Authority:**
        - For routine marketing/bizdev comms: `Charles` or `Delphine` (after
          legal/prod review).
        - For significant announcements, press releases, strategic partnerships:
          `Antoine` AND `Béatrice`.
        - For communications involving major studio strategy, crisis response,
          or those initiated by Lug: **Lug (via `Orion`) provides final
          approval** after `Antoine`/`Béatrice` recommendation. This follows
          Protocol S7.4 for documenting Lug's decision.
    - **Traceability:** Approval (or rejection with rationale) is explicitly
      documented in the GitHub Issue (e.g., comment "**FINAL_APPROVAL
      (@[ApproverGemID]):** Communication XYZ approved for release on [Date] via
      [Channel].") and the Issue labeled `status:approved-for-release`.

5. **Step 5: Dissemination and Archiving**
    - **Responsibility for Dissemination:** The lead spokesperson or their
      designated Gem.
    - **Channels:** As approved (e.g., email, official website post, press
      wire).
    - **Archiving (Traceability):**
        - A copy of the **final, as-released communication material** (e.g., PDF
          of press release, final slide deck, text of official statement)
          **must** be attached to the original GitHub Issue.
        - The GitHub Issue is then closed with a label like `status:released` or
          `status:communication-sent`.
        - A link to this Issue (or the archived material itself) is added to an
          "Official External Communications Log" (a Markdown document or
          structured list in `gcs-core-governance/02-knowledge-base-hub/KB-
          Domain-Marketing-Sales-Legal/External-Comms-Log.md`).
    - **Tooling for AI Gems:** `ArchiveCommunicationTool` could help attach the
      final material and update the log.

## 11.5. Crisis Communication

- **Specific Sub-Protocol:** In the event of a crisis (major security breach,
  critical game failure post-launch, significant negative PR), a specific
  "Crisis Communication Plan" (to be developed by `Antoine`, `Fanny`, `Henri`,
  and approved by Lug, stored in `gcs-core-governance/01-Operational-
  Protocols/` as, e.g., S3-Appendix-CrisisComms) will be activated.
- **Key Elements:** Designated crisis comms team, rapid internal information
  gathering, pre-approved statement templates, strict control over information
  release, coordination with legal. `Orion` is the sole channel for Lug's
  statements.

## 11.6. Responsibilities in External Communication

- **Designated Spokespersons (`Antoine`, `Béatrice`, `Charles`, `Delphine`,
  `Henri`, `Orion` for Lug):** Responsible for representing Gencraft accurately
  and professionally within their mandated areas.
- **`Henri` (Legal Counsel) & `Léo` (OSS Specialist):** Mandatory review of all
  external communications for legal, IP, and compliance risks.
- **`Antoine` (Producer) & `Béatrice` (Product Manager):** Strategic oversight
  and approval for most external communications.
- **Drafting Gems (can be any of the above, or `Iris` for research-based
  drafts):** Responsible for creating accurate and effective communication
  materials.
- **All Gems:** **Must not** make unauthorized official statements. Must route
  any external inquiries they receive to `Antoine` or the appropriate designated
  spokesperson.

## 11.7. Impact and Tooling for AI Gems

- **Gems as Drafters (e.g., `Iris`, or a specialized `CommsDraftingGem` if
  created):**
  - `KnowledgeBaseSearchTool`: To gather background information from `gencraft-
    studio-handbook` and other KB sources.
  - `MarkdownAuthoringTool` / `PresentationDraftingTool` (using templates from
    `gcs-core-governance/02-knowledge-base-hub/Templates/Document-
    Templates/`).
  - `Proximo`: To assist with tone, style, and structure, ensuring alignment
    with Gencraft's desired external voice (defined in brand guidelines in KB).
- **Gems as Reviewers (e.g., `Henri`, `Léo`, `Isaac` if technical content):**
  - `DocumentReviewTool`: To read drafts and provide structured feedback via
    `GitHubIssueCommentTool`.
  - Specialized `Tools` for their domain (e.g., `Léo`'s
    `LicenseComplianceCheckTool` if a comm mentions software).
- **`Orion` (Studio Liaison Gem):**
  - `SecureCommunicationTool` (for Lug).
  - `PRManagementTool` for submitting Lug's approved statements/decisions to
    `gcs-core-governance`.
  - `SummarizationTool` to prepare briefs for Lug.
- **`Antoine` / `Béatrice` (as approvers):**
  - `Tool` to manage and track `type:external-comm-request` Issues.
  - `Tool` to formally log their approval in the Issue.
- **`Charles` / `Delphine` (as spokespersons/disseminators):**
  - `Tool` to access the final approved communication materials.
  - Potentially `Tools` to assist with dissemination to target channels (though
    this might be manual).
- **`ArchiveCommunicationTool` (for designated Gem, e.g., comms initiator or
  `Iris`):**
  - To attach final comms to the GitHub Issue and update the `External-Comms-
    Log.md` in the KB.

This protocol ensures that Gencraft's external voice is managed strategically,
professionally, and with appropriate oversight, protecting and enhancing the
studio's reputation and relationships.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
