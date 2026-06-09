---
docId: OPS-GUIDE-022
title: Devproc 001 SSoT Document Generation Process
version: 1.0.0
authors:
- AI Compliance Agent
creation_date: '2025-05-26'
last_updated_date: '2026-05-20'
language: en
metadata:
  scope: studio
  domain: governance
  doc-type: guide
  lifecycle-stage: approved
  security-classification: l1_internal
  intended-audience:
  - contributors
  - ai-agents
  - documentation-team
  keywords:
  - ssot-document-generation
  - knowledge-base
  - process-documentation
  - ai-assistance
  - workflow
  - documentation-standards
  related-documents:
  - ../README.md
  - ../00-studio-vision-and-principles/KC&T-Guiding-Principles.md
  - ../02-knowledge-base-hub/Templates/Document-Templates/ssot-template.md
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-022.devproc-001-ssot-document-generation-process.md
---
# SSoT Document Generation and Iterative Refinement Process

## 1. Objective

This document defines the standardized, iterative, and AI-assisted process for
generating high-quality, actionable Single Source of Truth (SSoT) documents
within Gencraft. This includes standards, protocols, guides, reports, and other
key knowledge artifacts. The process aims to ensure:

- **Clarity & Precision:** Documents are easy to understand and unambiguous,
  especially for AI Gem consumption.
- **Completeness:** All necessary aspects are covered comprehensively.
- **Consistency:** Uniformity in structure, formatting, and terminology across
  the SSoT.
- **Actionability:** Documents are directly usable by both human and AI Gems to
  guide actions and decisions.
- **Collaboration & Validation:** Relevant stakeholders and expert perspectives
  are integrated.
- **Efficiency:** Streamlined workflow leveraging AI assistance where
  beneficial.
- **Traceability:** Decisions and changes during the document lifecycle are
  traceable.

## 2. Scope

This process applies to the creation and significant updates of all official
SSoT documents destined for:

- `gcs-core-governance/`
- `gcs-core-governance/`
- Project-specific ADR (Architecture Decision Record) repositories (e.g.,
  `gcs-plt-architecture/adrs/`).
- Other designated SSoT locations as defined by the Governance Crew or Studio
  Leadership.

Minor typographical corrections or clarifications on already "Approved"
documents may follow a simpler review process as defined in
`GOV-GUIDE-007.knowledge-management-and-contribution-guide.md`.

## 3. Roles in the Document Generation Process

- **Document Initiator/Requester:** Any Gem (human or AI) or Crew identifying
  the need for a new SSoT document or a major revision to an existing one.
- **Lead Author (Rédacteur Principal):** A designated Gem (human or AI, e.g.,
  `Adam`, `Édouard`, `Cerberus`, `Iris`, or a domain expert) responsible for
  producing the initial draft, incorporating feedback, and stewarding the
  document through the process.
- **Reviewer(s):** Designated Gems (human or AI) providing expertise from
  specific perspectives (e.g., Security - `Cerberus`, Architecture - `Isaac`,
  DevOps Strategy - `Édouard`, Technical Specialization - `Benjamin`/`Camille`,
  QA - `Zoé`, Legal - `Henri`, KB Architecture - `Iris`).
- **Approver(s):** Designated Gems or a defined Governance body (e.g., Leads of
  affected domains, Governance Crew representatives) with the authority to
  approve the document for SSoT integration.
- **Knowledge Guardian(s):** One or more Gems assigned in the document's
  frontmatter, responsible for the long-term accuracy, relevance, and evolution
  of the document post-approval.
- **SSoT Integrator:** The individual (e.g., Project Lead managing the current
  initiative, or a dedicated KB Manager like `Iris`) responsible for the final
  technical act of merging/copy-pasting the approved Markdown into the official
  SSoT repository.
- **AI Facilitator (Optional but Recommended):** An AI Gem (like `Adam` in
  current context, or a future specialized Gem) that orchestrates or assists in
  this process, especially in simulating roles and ensuring AI-actionability.

## 4. SSoT Document Generation Workflow

This workflow is iterative and leverages AI assistance where practical. For
processes primarily executed by AI Gems (like the current one with Adam),
"simulated" means the AI Gem internally performs the role-play and consolidates
feedback. For human-led processes, these steps involve actual human
collaboration.

### Step 0: Initiation and Planning

1. **Identify Need:** A need for a new document or major revision is identified
    (e.g., via PROJ-103 deliverables, ADR proposal, gap in Handbook).
2. **Formalize Request (Optional but Recommended for major docs):** Initiator
    creates an Issue using `knowledge-proposal-template.md` or a similar project
    task.
3. **Define Scope & Objectives:**
    - Clearly define the document's purpose, intended audience, and key
      objectives.
    - Assign a preliminary ID (e.g., `OPS_00X`) and target SSoT path.
4. **Identify Key Personnel:**
    - Nominate Lead Author(s).
    - List preliminary Reviewers and Approvers (refer to `Studio-Organization-
      And-Roles.md` for relevant expertise).
5. **Select Template:** Choose the most appropriate document template from
    `/gcs-core-governance/02-knowledge-base-hub/Templates/Document-
    Templates/`. `Iris` can advise.

### Step 1: Initial Draft Creation (v0.1)

1. **Lead Author Action:** The Lead Author (human or AI Gem) creates the
    initial draft (Version 0.1, Status: Draft).
2. **Content Focus:**
    - Adherence to the selected template and its structural guidelines.
    - Comprehensive initial content addressing the defined objectives and scope.
    - Inclusion of a complete YAML frontmatter (ID, Title, Version, Status,
      proposed Authors, Reviewers, Approvers, Knowledge Guardians, Related
      Documents).
    - Proper citation of `Related Documents` using the `` format.
3. **AI Drafting Assistance (Recommended):**
    - Utilize AI tools (e.g., `Proximo`, specialized drafting Gems) for
      generating initial structure, boilerplate sections, or even content based
      on a detailed brief and references to existing SSoT documents. This can
      significantly accelerate the drafting phase.
    - The AI Facilitator can play this role if a dedicated drafting Gem is not
      available.

### Step 2: Multi-Perspective Review & Enrichment Cycle (Iterative)

This is a critical phase involving one or more iterations.

1. **Reviewer Persona Simulation/Assignment:** The Lead Author (or AI
    Facilitator) identifies the key Reviewer personas for the current iteration.
2. **Iterative Review:** For each designated Reviewer:
    - The AI Facilitator (or Lead Author if human) embodies the Reviewer's
      perspective, or the actual human Reviewer performs the review.
    - **Role-Specific Checklists (To Be Developed):** Review against a checklist
      specific to the reviewer's domain (e.g., `Cerberus` checks security
      aspects, `Isaac` architectural soundness, `Iris` KB coherence, `Édouard`
      strategic alignment).
    - **Feedback & Contributions:**
        - Identify gaps, inaccuracies, ambiguities.
        - Propose additions, clarifications, and corrections.
        - Suggest improvements for structure and flow.
    - **Focus on AI Actionability:** This is a key Gencraft requirement.
      Reviewers (especially AI Facilitator) must ensure:
        - Clear, explicit, and unambiguous language.
        - Well-defined terms (cross-reference with `glossary.md`).
        - Structured information where possible (e.g., tables, bullet points
          with consistent formatting, defined enums/vocabularies for key
          fields).
        - Clear instructions or procedural steps.
        - Examples that illustrate complex points.
3. **AI Document Analysis (Recommended):**
    - An AI Gem specialized in document analysis (e.g., future version of `Iris`
      or `Lexicon`) SHOULD be used to:
        - Check for semantic consistency within the document and with directly
          related SSoT entries.
        - Validate terminology against the `glossary.md`.
        - Assess overall clarity and conciseness.
        - Suggest rephrasing for improved readability by both humans and AI.
        - Verify basic adherence to `GOV-GUIDE-007.knowledge-management-and-contribution-guide.md`.
4. **Consolidation:** The Lead Author (or AI Facilitator) consolidates all
    feedback and edits, updating the document to a new minor version (e.g.,
    v0.2, v0.3). Disagreements are resolved via discussion or escalation if
    necessary (Protocol S2).

### Step 3: Final Author/Reviewer Iteration & "Satisfaction"

1. **Full Iteration:** The AI Facilitator (or Lead Author) re-assumes the
    perspective of each designated Author and Reviewer one last time on the
    consolidated draft.
2. **Addressing Remaining Gaps:** This pass focuses on ensuring all previous
    feedback has been adequately addressed and that the document is holistically
    sound from all key perspectives.
3. **Achieving "Satisfaction":** The document is considered ready for final
    approval simulation when the AI Facilitator (or Lead Author if human-led)
    judges that:
    - All critical objectives are met.
    - Content is accurate, complete, and clear.
    - It aligns with Gencraft standards and principles.
    - It is demonstrably "actionable by an AI Gem".
    - No significant concerns remain from the simulated (or actual) reviewer
      perspectives.

### Step 4: Automated Quality Checks

Before final submission, the candidate document (e.g., v0.9) MUST undergo
automated checks:

1. **Markdown Linting:** Process the document using `GCT-TOOL-MDLINT-V1` with
    the SSoT Gencraft linting configuration. All reported errors MUST be fixed.
2. **Link Validation (Future Enhancement):** Implement/use a tool to check all
    `` references for validity against the SSoT structure and ensure external
    URLs are live.
3. **Spell/Grammar Check (AI Assisted):** Utilize an AI Gem (e.g., `Lexicon`
    capabilities) for final polish.

### Step 5: Final Approval Simulation & Versioning

1. **Approval:** Based on the successful completion of Steps 3 and 4, the Lead
    Author (or AI Facilitator) designates the document as "Approved".
2. **Versioning:** The document version is set to `1.0` (or incremented
    appropriately for major revisions of existing documents).
3. **Frontmatter Update:** The YAML frontmatter is finalized with correct
    `Status: Approved`, `Version`, and lists of `Initial Reviewers` and `Final
    Approvers` reflecting the key roles involved in the (simulated) process.

### Step 6: Submission to SSoT Integrator

The AI Facilitator (or Lead Author) provides the final, approved Markdown
content (typically in a code block for easy copy-pasting) to the designated SSoT
Integrator.

### Step 7: SSoT Integration and Communication

1. **Integration:** The SSoT Integrator commits the document to its official
    SSoT path in the relevant repository. This MUST follow Git best practices,
    including a clear commit message referencing the document ID and version (as
    per `TOOL_001_Conventional_Commits_Standard.md`). For significant new
    documents or changes, a PR reviewed by the Knowledge Guardian(s) is
    recommended even at this stage.
2. **Communication:** The availability of the new/updated SSoT document is
    communicated to relevant Gencraft Gems and Crews as per Protocol S14.

## 5. Tooling and AI Assistance Supporting the Process

- **Document Templates:** SSoT in `/gcs-core-governance/02-Knowledge-Base-
  Hub/Templates/Document-Templates/`.
- **Issue Templates:** For proposing new documents or tracking major revisions,
  in `/gcs-core-governance/02-knowledge-base-hub/Templates/Issue-
  Templates/`.
- **AI Drafting Gems (e.g., `Proximo` or future specialized tools):** For
  generating initial structures and content.
- **AI Review & Analysis Gems (e.g., enhanced `Iris` or `Lexicon`):** For
  consistency, terminology, clarity, style guide adherence, and AI-actionability
  checks.
- **Markdown Linting Tools:** `GCT-TOOL-MDLINT-V1`.
- **Version Control System (Git & GitHub):** For SSoT storage, versioning, and
  collaborative review (PRs) in human-led scenarios.
- **Role-Specific Review Checklists:** To be developed and stored in the KB
  (e.g., within `GOV-GUIDE-007.knowledge-management-and-contribution-guide.md` or a dedicated section).

## 6. Continuous Improvement of This Process

This `DEVPROC_001` standard itself is subject to review and improvement:

- **Periodic Review:** At least annually, or as Gencraft's operational model
  evolves.
- **Feedback Loop:** Gems using this process are encouraged to propose
  improvements via Issues (using `knowledge-proposal-template.md`) tagged for
  the `DEVPROC_001` Knowledge Guardians.
- **Post-Mortems (S5):** For particularly complex or lengthy document generation
  efforts, a brief lessons-learned session (as per S5) can identify refinements
  for this process.
- **Updating AI Capabilities:** As AI Gem capabilities for drafting, review, and
  analysis improve, this process will be updated to leverage them more
  effectively.

This process aims to balance rigor with agility, ensuring Gencraft's SSoT
remains a valuable, high-quality, and actionable asset for all Gems.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
