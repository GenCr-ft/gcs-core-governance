---
docId: ENG-GUIDE-001
title: Studio Crews Overview
version: 1.0.0
authors:
- AI Compliance Agent
creation_date: '2025-05-26'
language: en
last_updated_date: '2026-05-20'
metadata:
  lifecycle-stage: approved
  keywords:
  - crewai
  - gencraft
  - automation
  - ai-gems
  - workflow
  - studio-operations
  scope: studio
  domain: production-management
  doc-type: charter
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/04-tooling-and-automation-hub/ENG-GUIDE-001.studio-crews-overview.md
---
# Gencraft Studio Crews Overview

## 1. Introduction

This document provides an overview and catalog of formally defined Gencraft
"Crews." A Crew is a team of specialized AI Gems configured to collaborate
autonomously on specific, complex, and often recurring workflows using the
CrewAI framework. These Crews are designed to automate or significantly augment
studio processes, enhancing efficiency, ensuring consistency, and enabling
sophisticated task execution across all Gencraft operations, from game
development to studio management.

The purpose of this overview is to:

- List all active, planned, and potential Gencraft Crews.
- Clearly describe the mission, primary functions, and expected deliverables of
  each Crew.
- Identify the typical Gem roles (or specific Gems if fixed) composing each Crew
  and their core responsibilities within the Crew.
- Provide direct links to the SSoT Git repositories containing the CrewAI Python
  definitions, configurations, and any specific operational protocols or
  documentation for each Crew.
- Clarify the primary `Tools`, MCP Servers, and KB domains leveraged by each
  Crew.
- Outline the performance metrics or KPIs by which each Crew's effectiveness can
  be measured (guidance for `GCT-QAS-GPQA-001` Véra).

This document serves as a central reference for understanding how Gencraft
operationalizes teamwork between its AI Gems. It is maintained by the AI
Enablement Team (AIE Team) in collaboration with relevant Department Leads,
Knowledge Guardians, and `GCT-QAS-GPQA-001` (Véra) for performance aspects.

## 2. CrewAI Foundational Principles at Gencraft

All Gencraft Crews are designed and operated according to the following
principles:

- **Orchestration & Autonomy:** Crews are orchestrated using the CrewAI
  framework (`https://github.com/crewAIInc/crewAI`). Once initiated with a clear
  goal and context, a Crew should operate with a high degree of autonomy to
  achieve its defined tasks, only escalating or requesting human intervention
  for exceptions or predefined decision points.
- **SSoT for Definitions:** The Python code defining each Crew's agents (Gems
  within the Crew context), tasks, tools, and process logic resides in a
  dedicated, version-controlled Git repository (e.g., `gencraft-crewai-
  workflows/[crew-name]/` or within project-specific repositories for project-
  dedicated Crews). This document *must* link to these SSoTs.
- **Modularity & Reusability:** Crews and their constituent agent/task
  definitions should be designed for modularity and reusability where practical,
  potentially allowing their services or sub-tasks to be invoked by other Gems
  or Crews.
- **Clear Mandates & Deliverables:** Each Crew has a clearly defined mission,
  scope of responsibility, and expected set of deliverables or outcomes. These
  must be documented in their specific SSoT.
- **Traceability & Reporting:** Crew operations, critical decisions made during
  a task execution, and significant outputs are expected to be rigorously
  traceable as per Gencraft's KC&T protocols (notably S4 and S7). Crews should
  generate concise operational logs and summary reports (potentially leveraging
  `Tools` to assist in S6 Report generation for their supervising Gem).
- **Tool & KB Usage:** Crews leverage the standard Gencraft Gem `Tools` and MCP
  Servers documented in this Hub. Their constituent Gems must be configured to
  effectively query and utilize the Gencraft KB for context and operational
  guidance.
- **Error Handling & Escalation:** Crew definitions must include robust error
  handling mechanisms and clearly defined escalation paths (potentially to their
  Orchestrator Gem or a designated support Gem like `GCT-DVO-DVSOS-001` Diane
  for operational issues) when they encounter situations beyond their autonomous
  capabilities.
- **Performance & Efficiency:** Crews are subject to performance monitoring by
  `GCT-QAS-GPQA-001` (Véra). Their design should prioritize efficiency in task
  completion, resource utilization, and LLM token consumption.

## 3. Catalog of Gencraft Crews

This section catalogs all formally defined Gencraft Crews. The status of each
crew (e.g., `Concept`, `Planned`, `In Development`, `Operational`, `Deprecated`)
will be indicated.

*(This section will be populated by the AIE Team as Crews are formally designed,
developed, and deployed. Each entry below is a placeholder for a potential
future Crew or an example structure.)*

---

### 3.1. Crew Example: "KB Content Ingestion & Structuring Crew"

- **Crew ID:** `CREW-KB-INGEST-001`
- **Status:** `Planned`
- **Mission:** To autonomously process raw, unstructured information from
  designated sources (e.g., meeting transcripts provided by `GCT-UTL-SLG-001`
  Orion, research summaries from `GCT-UTL-RWSKA-001` Iris, outputs from other
  Gems) and transform it into well-structured, draft Knowledge Base articles in
  Markdown, adhering to Gencraft's `GOV-GUIDE-007.knowledge-management-and-contribution-guide.md`. The
  output is a PR ready for KG review.
- **Typical Gem Composition (Roles within the Crew):**
  - `InformationExtractionAgent`: Specializes in identifying key facts,
    decisions, and action items from raw text.
  - `KBDraftingAgent`: Takes extracted information and drafts a KB article using
    the appropriate template (e.g., `kb-article-generic-template.md`, `decision-
    record-template.md`).
  - `KBFormattingStyleAgent`: Reviews the draft for strict adherence to `KB-
    Contribution-And-Style-Guide.md` (formatting, linking, GemID usage).
  - `MetadataTaggingAgent`: Proposes relevant YAML frontmatter (KG, status,
    version) and keyword tags for discoverability.
  - `PRCreationAgent`: Bundles the final draft and submits a Pull Request to the
    `gcs-core-governance` repository, assigning the relevant Knowledge
    Guardian.
- **Orchestrator Gem (Initiates/Supervises & acts as final internal
  validator):** `GCT-UTL-RWSKA-001` (Iris)
- **Key `Tools` & MCPs Used:**
  - `TextSummarizationTool`, `EntityRecognitionTool`
  - `MarkdownAuthoringTool` (template-aware), `KBTemplatesAccessTool`
  - `KBStyleGuideValidationTool` (conceptual)
  - `MetadataSuggestionTool` (conceptual, leveraging KB taxonomy)
  - `GitHubPullRequestTool`
- **Primary KB Domains Utilized:** `GOV-GUIDE-007.knowledge-management-and-contribution-guide.md`,
  `Templates/`, `glossary.md`.
- **Workflow SSoT Repository:** `gencraft-crewai-workflows/kb-content-
  ingestion/`
- **Key Performance Indicators (KPIs):**
  - Turnaround time from raw input to draft PR.
  - Adherence rate of drafts to style guide (pre-`GCT-UTL-KFE-001` Lexicon
    review).
  - Accuracy of extracted information.

---

### 3.2. Crew Example: "Automated Code Review & Analysis Crew"

- **Crew ID:** `CREW-CODE-REVIEW-001`
- **Status:** `Under Consideration`
- **Mission:** To perform initial automated code reviews, static analysis,
  security vulnerability checks (SAST), and adherence checks to coding standards
  for submitted Pull Requests in Gencraft's software project repositories
  (`gcl-voxel-engine`, `gcp-aethel-client`, `gcp-aethel-server`, `gencraft-ai-
  tools`, etc.). To provide formatted feedback as PR comments for human Lead
  Developer review.
- **Typical Gem Composition (Roles within the Crew):**
  - `CodeRetrievalAgent`: Fetches code changes from a specified Pull Request.
  - `StaticAnalysisExecutionAgent`: Executes configured linters (e.g., ESLint,
    Pylint), SAST tools (e.g., Snyk, Semgrep via `Tool` wrappers), and code
    complexity analyzers.
  - `CodingStandardVerificationAgent`: Checks code against `gencraft-devops-
    standards/tooling/tool-003-code-style-and-formatting.md` and project-
    specific coding standards.
  - `SecurityVulnerabilityReportingAgent`: Highlights potential vulnerabilities
    identified by SAST tools, referencing `GCT-MGT-SECOFF-001` (Cerberus)'s risk
    levels.
  - `ReviewSummaryAgent`: Consolidates all findings into a structured Markdown
    report.
  - `PRCommentSubmissionAgent`: Posts the summary report as a comment on the
    Pull Request.
- **Orchestrator Gem (Trigger/Supervisor):** Typically triggered by a GitHub
  Action on PR creation/update. Supervised implicitly by the AIE Team and
  relevant Dev Leads like `GCT-PRG-LDTL-001` (Julien).
- **Key `Tools` & MCPs Used:**
  - `GitRepositoryTool`, `GitHubAPITool` (for PR interaction)
  - `LintingToolWrapper` (for various linters)
  - `SASTExecutionTool` (interface for Snyk, Semgrep, etc.)
  - `CodeComplexityAnalysisTool`
  - `MarkdownFormattingTool`
- **Primary KB Domains Utilizado:** `gcs-core-governance/tooling/`,
  Protocol S8.
- **Workflow SSoT Repository:** `gencraft-crewai-workflows/code-review-
  automation/`
- **Key Performance Indicators (KPIs):**
  - Percentage of common coding standard violations caught automatically.
  - Time taken to provide initial feedback on a PR.
  - Accuracy of reported vulnerabilities (reduction of false positives over
    time).

---
*(New Crew definitions will be added here by the AIE Team following the
structure above.)*

## 4. Proposing, Developing, and Maintaining Crews

### 4.1. Proposal and Prioritization

- The need for a new Crew should be identified based on recurring, complex,
  multi-step workflows suitable for automation by a team of collaborating Gems.
  Benefits should include significant efficiency gains, quality improvements, or
  enablement of new capabilities.
- Proposals for new Crews must be submitted to the **AI Enablement Team (AIE
  Team)** by creating a GitHub Issue with the label `type:crew-proposal` in the
  `gencraft-aie-backlog` repository.
- The proposal should use a specific template (`crew-proposal-template.md` - *To
  Be Created, linked to Action 3.1*) detailing:
  - Crew Mission and Objectives.
  - Detailed description of the workflow to be automated/augmented.
  - Proposed Gem roles within the Crew and their interactions.
  - Required `Tools`, MCPs, and KB access.
  - Expected deliverables and success metrics (KPIs).
  - Estimated impact and ROI for the studio.
- The AIE Team Lead, in collaboration with `GCT-MGT-PPM-001` (Antoine) and other
  relevant stakeholders, will evaluate, refine, and prioritize these proposals.

### 4.2. Development and Deployment

- Approved Crew concepts will be developed by the AIE Team, or by other
  designated development Gems under the AIE Team's technical guidance and
  standards.
- Development will follow the `ai-tool-development-standards.md` where
  applicable, including rigorous testing (unit, integration, and end-to-end
  workflow testing).
- Each Crew will have its Python definition and supporting configuration files
  stored in a dedicated, version-controlled SSoT repository.
- Deployment will be managed by the AIE Team in coordination with DevOps (D08)
  if infrastructure dependencies exist.

### 4.3. Documentation and Registration

- Upon successful testing and deployment, the AIE Team is responsible for:
  - Ensuring comprehensive documentation for the Crew (operational guide,
    troubleshooting, Python code comments) is available in its SSoT repository.
  - Adding or updating the Crew's entry in this `Studio-Crews-Overview.md`
    document.
  - Communicating the availability and functionality of the new Crew to relevant
    studio members (as per Protocol S14).

### 4.4. Maintenance and Evolution

- The AIE Team is responsible for the ongoing maintenance, monitoring (in
  collaboration with `GCT-QAS-GPQA-001` Véra), and evolution of operational
  Crews.
- This includes bug fixing, performance optimization, and adapting Crews to
  changes in Gencraft protocols, `Tools`, or studio needs.
- Requests for enhancements to existing Crews follow the same process as new
  Crew proposals.

## 5. Governance and Oversight

- This `Studio-Crews-Overview.md` document is maintained by the AIE Team Lead.
- The overall strategy for Crew utilization and the prioritization of major new
  Crew developments fall under the strategic oversight of `GCT-MGT-PPM-001`
  (Antoine) and the AIE Team Lead.
- Significant changes to this overview document or the fundamental principles of
  Crew operation require review and approval from the AIE Team Lead and `GCT-
  MGT-PPM-001` (Antoine).

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
