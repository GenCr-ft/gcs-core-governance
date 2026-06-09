---
docId: OPS-GUIDE-021
title: S1 Feedback Approval
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
  - gencraft
  - feedback
  - approval
  - deliverables
  - studio-protocols
  - github
  - quality-assurance
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-021.s1-feedback-approval.md
---
# Gencraft Operational Protocol - Section 1: Feedback and Approval of Deliverables

## 1.0. Justification and Objectives

**Why this protocol?** In any creative and technical endeavor, especially game
development, deliverables (code, art, design documents, etc.) must undergo
review to ensure quality, coherence with the project vision, and technical
soundness. This protocol aims to:

- **Standardize the Review Process:** Ensure all major deliverables are reviewed
  consistently across **Gencraft**.
- **Improve Deliverable Quality:** Leverage collective expertise to identify
  issues and areas for improvement early.
- **Ensure Alignment:** Verify that deliverables meet requirements (from
  `gcp-aethel-docs-req` or design docs in `gcp-aethel-docs-gdd`),
  adhere to artistic (from `gcp-aethel-assets-styleguide`) and technical
  guidelines (from `gcs-plt-architecture` or `gcs-core-governance`), and
  contribute to project goals.
- **Provide Clear Accountability:** Define who is responsible for creating,
  reviewing, and approving deliverables.
- **Facilitate Traceability:** Maintain a clear record of feedback, revisions,
  and approvals (primarily on GitHub Issues/PRs within project repositories like
  `gcp-aethel-client`, `gcp-aethel-server`, or knowledge repositories like
  `gcs-core-governance`) for future reference and learning.

## 1.1. Standardized Deliverable Statuses (GitHub Labels)

**How it works:** To provide immediate visibility into the state of any
deliverable being tracked (typically via a GitHub Issue or Pull Request within a
`gcx-yyy` repository), a set of standardized labels will be used. These
labels represent the lifecycle stages of a deliverable. `Véra` may monitor the
correct application of these statuses.

- **`status:draft`** (or **`status:in-progress`**): The deliverable is currently
  being created or actively worked on by the assigned Gem. *Initial state for
  new work.*
- **`status:ready-for-review`**: The author Gem considers the deliverable
  complete enough for initial or final review and has submitted it.
- **`status:in-review`**: A designated reviewer Gem has started the review
  process. *This indicates active examination.*
- **`status:revisions-requested`**: The reviewer has provided feedback, and
  modifications are required from the author Gem. The deliverable returns to a
  `status:in-progress` or similar state for the author.
- **`status:approved`**: The deliverable has been reviewed and all necessary
  criteria are met. It is considered final for its current stage.
- **`status:rejected`**: The deliverable, after review, is deemed unsuitable or
  fundamentally flawed and will not be used in its current form. A clear
  justification is mandatory.
- **`status:on-hold`** (optional): Work on the deliverable has been temporarily
  paused for strategic or dependency-related reasons.

**Responsibility:** The Gem primarily working on the deliverable is responsible
for updating its status label on the relevant GitHub Issue/PR. Reviewers may
also update statuses.

## 1.2. Assigned Review and Approval Roles

**How it works:** Specific Gems are designated as primary reviewers and
approvers. These roles are documented in
`gcs-core-governance/00-studio-vision-and-principles/GOV-GUIDE-411.organization-and-roles.md`.

- **Producer (`Antoine`):** Final approval for major project milestones, overall
  feature completion (scope, time, budget alignment), and key production process
  documents.
- **Product Manager (`Béatrice`):** Approval of product requirements, user
  stories, and feature specifications for alignment with product vision and
  market needs (references `gcp-aethel-docs-req`).
- **Lead Developer (`Julien`):** Technical approval of code (via PR reviews in
  `gcx-yyy` code repos), architectural compliance of implemented features
  (references `gcs-plt-architecture`).
- **Software Architect (`Isaac`):** Approval of high-level software architecture
  documents and significant technical design choices (primary author/guardian of
  content in `gcs-plt-architecture`).
- **Lead Artist (`Quentin`):** Approval of final art assets (models, textures,
  animations) for quality and consistency with art production guidelines
  (references `gcp-aethel-assets-styleguide`).
- **Art Director (`Pascal`):** Final approval on art direction, style guides,
  and key visual benchmarks to ensure alignment with the game's artistic vision
  (primary author/guardian of content in `gcp-aethel-assets-styleguide`).
- **Game Designer (`Étienne`):** Approval of game design documents, mechanic
  specifications, level design concepts (from `Florence`), and narrative
  elements (from `Gaspard`) for gameplay coherence and vision (primary
  author/guardian of content in `gcp-aethel-docs-gdd`).
- **UX/UI Designer (`Hélène`):** Approval of UI implementations (by `Olivier`)
  for fidelity to mockups, usability, and adherence to the UI Design System
  (documented in the KB, likely linked from `gcs-studio-
  handbook/02-knowledge-base-hub/KB-Domain-UX-UI-Design.md`).
- **QA Lead (`Zoé`):** "Approval" that a feature or build meets quality criteria
  for release to the next stage (e.g., playtest, production). Certifies test
  coverage and critical bug resolution.
- **Lug (Studio Director, via `Orion`):** Final approval for critical strategic
  deliverables, major changes in direction, or high-impact GDD sections.
  (Decisions traced as per Protocol S7).

**Documentation:** Detailed role assignments for approvals are in the Gencraft
Knowledge Base (KB)
(`gcs-core-governance/00-studio-vision-and-principles/GOV-GUIDE-411.organization-and-roles.md`).

## 1.3. Structured Review Process (GitHub-centric)

**How it works:** Managed within GitHub Issues/PRs in the relevant
`gcx-yyy` repository to ensure transparency and traceability.

1. **Submission for Review:** Author Gem completes work.
    - For code/documentation (in `gcx-yyy` repos, including `gcs-
      studio-handbook` for protocols/KB articles): Create a Pull Request (PR).
    - For other deliverables (e.g., art assets where previews are reviewed):
      Update the corresponding GitHub Issue, attach/link previews, and set
      status label to `status:ready-for-review`.
    - Notify designated approver(s) by assigning them to the PR/Issue or
      @mentioning them.
2. **Review Execution:** Reviewer(s) acknowledge (e.g., by commenting or self-
   assigning) and change status label to `status:in-review`. Feedback (specific,
   actionable, constructive) is logged in PR/Issue comments, referencing KB
   standards (e.g., `gcs-core-governance/02-knowledge-base-hub/KB-
   Contribution-And-Style-Guide.md` or specific technical standards from
   `gcs-core-governance`).
3. **Addressing Feedback:** Author Gem reviews feedback. If modifications are
   needed, status label is typically changed to `status:revisions-requested` (or
   `status:in-progress` by the author). Author implements changes and resubmits
   (pushes new commits to PR branch, or updates Issue with new previews and
   notifies reviewers).
4. **Approval/Rejection Cycle:** This cycle of review and revision continues
   until the reviewer(s) are satisfied.
    - **Approval:** The PR is formally "approved" in GitHub's UI and then merged
      (by the Lead Dev, document maintainer, or an authorized Gem). The Issue is
      marked with `status:approved` and closed. A comment confirming approval is
      good practice.
    - **Rejection:** If the deliverable is fundamentally flawed or misaligned,
      the PR is closed without merging, or the Issue is marked `status:rejected`
      and closed. A clear, documented explanation for the rejection **must** be
      provided in the PR/Issue.

## 1.4. Tooling (GitHub-centric)

**How it works:** GitHub is the cornerstone for this protocol.

- **GitHub Repositories (`gcx-yyy`):** House all version-controlled
  deliverables: code, Markdown documents (KB articles in `gcs-studio-
  handbook`, GDDs in `gcp-aethel-docs-gdd`, requirements in `gencraft-
  requirements`, etc.).
- **GitHub Issues:** Track all non-code deliverables (e.g., art assets, high-
  level features, tasks) and serve as the hub for discussion, feedback, and
  status updates for these items. Used for managing the lifecycle of a
  deliverable from conception to approval.
- **GitHub Pull Requests (PRs):** The primary mechanism for reviewing and
  approving changes to code and all Markdown-based documentation within any
  `gcx-yyy` repository. Enforces a review gate before integration into the
  main branch.
- **GitHub Labels:** Used extensively on Issues and PRs to denote `status:`,
  `type:[deliverable_type]`, `priority:`, `department:[dept_code]`, `gem-
  assigned:[GemID]`, etc., enabling filtering, dashboarding (via GitHub
  Projects), and automated processing by `Tools`.
- **GitHub Projects (Boards):** Kanban-style boards can be used to visualize the
  workflow of deliverables across different statuses (e.g., "Draft," "Ready for
  Review," "In Review," "Approved").
- **Git LFS (Large File Storage):** Used for versioning large binary assets
  (final art, audio) within Git repositories. The approval process for these
  assets is still managed via GitHub Issues (linking to previews).
- **External Cloud Storage (if used for WIP large assets):** Links to these
  files are placed in the relevant GitHub Issue for review context, but the
  *process* (feedback, status, approval) remains on GitHub.

## 1.5. Traceability

**How it works:** GitHub's inherent features provide robust traceability for
this protocol.

- **Commit History (Git):** Every change to code or Markdown documents is
  versioned with an author GemID, timestamp, and a descriptive commit message
  (which should reference the related Issue/PR ID).
- **PR History:** Records all discussions, code/text changes, review comments
  (including suggestions, approvals, requested changes), approver GemIDs, and
  the merge event (including who merged and when).
- **Issue History:** Records all comments, status changes (via labels),
  assignments, links to PRs/commits, and the closure event (including reason if
  applicable).
- **Links:** GitHub allows robust linking between Issues, PRs, commits, and even
  across `gcx-yyy` repositories, creating a rich, interconnected web of
  information that traces the deliverable's journey.

This detailed history allows any authorized Gem (especially `Véra` for audits,
`Antoine` for project tracking, or Gems onboarding on a feature) to reconstruct
the entire lifecycle of a deliverable, understand the feedback given, see who
approved it, and when.

## 1.6. Impact on AI Gems and Necessary `Tools`

**How it affects Gems and what `Tools` they need:** AI Gems must be designed by
`Gemma` (using blueprints from `gcs-plt-gembp`) and equipped with
`Tools` to participate effectively and autonomously in this protocol.

- **Understanding & Updating Statuses:**
  - **Need:** Gems must interpret status labels on Issues/PRs and update them.
  - **`Tool`:** `GitHubStatusUpdateTool(target_url: str, new_status_label: str,
    old_status_label: Optional[str]) -> bool`. This `Tool` would use the GitHub
    API to add/remove labels.
- **Submitting for Review:**
  - **Need:** Author Gems must correctly submit deliverables for review.
  - **`Tools`:**
    - `CreatePullRequestTool(repo_url: str, branch_name: str, base_branch: str,
      title: str, body_markdown: str, reviewers: List[GemID], linked_issue_url:
      Optional[str]) -> GitHubPRURL`. The body should use a template from
      `gcs-core-governance/02-knowledge-base-hub/Templates/PR-Templates/`.
    - `SubmitIssueForReviewTool(issue_url: str, reviewer_gem_ids: List[GemID],
      comment_markdown: Optional[str]) -> bool`. This `Tool` would assign
      reviewers, set `status:ready-for-review`, and post an optional comment.
- **Interpreting Feedback:**
  - **Need:** Gems must parse review comments to understand requested changes.
    This is a complex AI challenge.
  - **Approach:**
    - Feedback from human reviewers or other Gems should ideally follow a
      **structured format** (defined in `gcs-core-governance/02-knowledge-
      base-hub../02-knowledge-base-hub/GOV-GUIDE-007.knowledge-management-and-contribution-guide.md`, section on "Providing
      Feedback for AI Gems"). This might include specific keywords (e.g.,
      "ACTION_REQUIRED:", "SUGGESTION:", "CLARIFICATION_NEEDED:") or formatted
      checklists.
    - **`Tool`:** `ParseReviewFeedbackTool(comments:
      List[str_or_structured_comment_object]) -> StructuredFeedbackSummary`.
      This `Tool` would attempt to extract actionable items. `Proximo` could
      assist reviewers in formatting their feedback for AIs.
    - Human oversight by the author Gem's Lead may be needed for complex or
      nuanced feedback.
- **Applying Revisions:**
  - **Need:** Based on parsed feedback, Gems may attempt to make revisions.
  - **`Tools`:** `MarkdownFileEditTool(file_path, changes_json)` or
    `SourceCodeEditTool(file_path, changes_json)` (these are advanced `Tools`
    representing significant AI capability). The "changes_json" would be a
    structured representation of the edits to make.
- **Acknowledging Approval/Rejection:**
  - **Need:** Gems must understand the final outcome of a review.
  - **`Tool`:** Their `GitHubIssueMonitorTool` or `PullRequestMonitorTool` would
    detect changes to `status:` labels (e.g., `status:approved`,
    `status:rejected`) or PR merge/closure events and parse associated final
    comments.
- **General GitHub Interaction `Tools` (from Category 5 of
  `gencraft_kct_tools_categories_v1`):**
  - `GitHubIssueManagementTool` and `PullRequestManagementTool` will be
    fundamental building blocks for the more specialized `Tools` above.
- **MCP Servers for Complex Interactions:** Operations like advanced feedback
  parsing, complex PR creation with multiple file changes, or automated
  application of revisions might be better handled by dedicated MCP Servers,
  callable by the Gems via simpler `Tool` interfaces. These MCP Servers would be
  catalogued in `gcs-core-governance/04-tooling-and-automation-hub/mcp-
  servers-catalog.md`.

By adhering to this protocol, Gencraft aims to ensure a high standard of quality
and clear traceability for all its deliverables, leveraging the capabilities of
its AI Gem workforce within a structured GitHub-centric environment.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
