---
docId: ENG-STANDARD-006
title: Ai Tool Development Standards
version: 1.0.0
authors:
- AI Compliance Agent
creation_date: '2025-05-26'
language: en
last_updated_date: '2026-05-20'
metadata:
  lifecycle-stage: approved
  keywords:
  - ai-tool-design-review
  - technical-standards
  - gcs-plt-architecture
  - design-process
  - tool-development
  scope: studio
  domain: production-management
  doc-type: specification
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/04-tooling-and-automation-hub/ENG-STANDARD-006.ai-tool-development-standards.md
---
## X. AI Tool & MCP Server Design Review Process

### X.1. Purpose and Scope

A formal Design Review process is mandatory for all new AI Tools, MCP Servers,
and for any significant architectural or API-breaking changes to existing ones.
The purpose of this review is to:

- Ensure technical soundness, security, and alignment with Gencraft's overall
  architecture and strategic objectives before significant development effort is
  invested.
- Validate that the proposed `Tool`/MCP Server meets a clearly defined studio
  need and adheres to established design principles and standards.
- Identify potential risks, dependencies, and integration challenges early in
  the lifecycle.
- Foster collaboration and shared understanding between the AIE Team,
  architectural stakeholders, security, and potential users.

This process is a key component of the "Design Phase" within the AI Tool
Development Lifecycle managed by the AI Enablement Team (AIE Team).

### X.2. Trigger for Design Review

A formal Design Review is triggered when:

1. A `type:tool-request` or `type:meta-gem-update-request` (for significant
   changes) from the `gencraft-aie-backlog` has been prioritized for development
   by the AIE Team Lead and `GCT-MGT-PPM-001` (Antoine).
2. The AIE Team (or the designated developer Gem) has produced an **Initial
   Design Specification** document for the proposed `Tool` or MCP Server.

### X.3. Required Documentation for Review

The Gem leading the design of the `Tool`/MCP Server is responsible for preparing
and submitting the following documentation to the "Technical Design Review
Committee" (TDRC):

1. **Initial Design Specification:** A document (typically using a preliminary
   version of `tool-documentation-template.md` or `mcp-server-api-spec-
   template.md`) covering at least:
    - **Overview and Purpose:** Problem statement, core functionality, intended
      users, key use cases.
    - **Proposed Technical Architecture:** High-level design, key components,
      technologies, libraries considered. For MCP Servers, a draft API
      definition (endpoints, key data models).
    - **Data Management (if applicable):** How data is sourced, processed,
      stored, and secured.
    - **Security Considerations (Initial Assessment):** Potential threats,
      planned security measures, adherence to
      `sec-001-secrets-management-standard.md`.
    - **Integration Points:** How the `Tool`/MCP Server will interact with other
      Gems, `Tools`, MCPs, or KB domains.
    - **Key Dependencies:** Software, infrastructure, or other `Tools`.
2. **Diagrams (if applicable):** Simplified architectural diagrams (e.g., C4
   model context or container diagrams, sequence diagrams for key interactions)
   to clarify complex designs.
3. **Alternatives Considered (Briefly):** A short summary of major alternative
   design approaches that were considered and why the proposed design was
   chosen.
4. **Proof-of-Concept Results (if applicable):** Summarized findings from any
   POCs conducted.

This documentation package must be submitted via a GitHub Issue with the label
`type:tool-design-review-request` in the `gencraft-aie-backlog` repository,
clearly linking to the SSoT locations of the design documents.

### X.4. Technical Design Review Committee (TDRC)

The TDRC is a flexible group convened by the AIE Team Lead (`GCT-UTL-AIETL-001`)
for each design review.

- **Core Permanent Participants:**
  - `GCT-UTL-AIETL-001` (AIE Team Lead) - Chair/Facilitator of the review
    process.
  - `GCT-PRG-SARCH-001` (Isaac - Senior Software Architect) - For architectural
    coherence, scalability, and technical best practices.
  - `GCT-MGT-SECOFF-001` (Cerberus - Security Officer Gem) - For security
    design, risk assessment, and compliance with Protocol S8.
- **Invited Participants (as needed, determined by the AIE Team Lead based on
  the Tool's scope):**
  - Relevant AI Tool Developer(s) from the AIE Team who will implement or
    maintain the `Tool`.
  - A representative from the D08 DevOps Team (e.g., `GCT-DVO-DVSST-001` Édouard
    or `GCT-DVO-DVSAI-001` Benjamin) if there are significant infrastructure,
    deployment, or MLOps implications.
  - `GCT-UTL-RWSKA-001` (Iris - KB Architect) if the `Tool` has complex
    interactions with the KB or generates significant knowledge artifacts.
  - One or more representatives of the primary Gem users or the original
    requester of the `Tool` to validate functional adequacy.
  - The Knowledge Guardian(s) of any KB domains or SSoT documents significantly
    impacted or consumed by the `Tool`.

### X.5. Design Review Process Steps

1. **Submission & Scheduling:**
    - The AIE Team developer submits the design documentation package via the
      `type:tool-design-review-request` GitHub Issue.
    - The AIE Team Lead (`GCT-UTL-AIETL-001`) verifies completeness and convenes
      the TDRC, scheduling a review window (e.g., 3-5 studio working days for
      asynchronous review, followed by a synchronous meeting if needed).
2. **Asynchronous Review:**
    - All TDRC members review the submitted design documents independently.
    - Questions, comments, concerns, and suggestions are logged directly as
      comments within the GitHub Issue.
3. **Synchronous Review Meeting (if required):**
    - Convened by the AIE Team Lead if asynchronous feedback indicates a need
      for direct discussion, or for particularly complex/critical designs.
    - The submitting developer briefly presents the design and addresses key
      questions.
    - The TDRC discusses outstanding concerns and seeks alignment. Minutes of
      key discussion points and decisions are taken.
4. **Decision & Feedback Consolidation:**
    - Following the review period (and meeting, if held), the AIE Team Lead
      consolidates the TDRC's feedback and formalizes one of the following
      decisions:
        - **Approved:** The design meets all criteria and development can
          proceed.
        - **Approved with Conditions:** The design is fundamentally sound, but
          minor revisions or clarifications are required. These must be
          addressed and verified by the AIE Team Lead (or a designated TDRC
          member) before development proceeds. A full re-review is not
          necessary.
        - **Revisions Required:** Significant issues in the design require major
          rework. The design must be revised and resubmitted for a new formal
          review cycle.
        - **Rejected:** The proposed design is not viable, not aligned with
          studio strategy, or has unacceptable risks. Clear justification must
          be provided.
5. **Traceability:**
    - The final decision, key feedback points, and any conditions for approval
      are documented as a formal comment in the `type:tool-design-review-
      request` GitHub Issue by the AIE Team Lead.
    - This record serves as the SSoT for the design review outcome, as per
      Protocol S7 (Key Decisions Traceability). The Issue is then closed or
      moved to the appropriate development phase.

### X.6. Key Review Criteria

Designs will be evaluated against, but not limited to, the following criteria:

- **Functional Adequacy:** Does the design meet the stated requirements and use
  cases of the requesting Gem(s)/Crew(s)?
- **Architectural Soundness:** Is the proposed architecture robust, scalable,
  and maintainable? Does it align with Gencraft's overall technical architecture
  and principles defined by `GCT-PRG-SARCH-001` (Isaac)?
- **Security:** Does the design adhere to Protocol S8,
  `sec-001-secrets-management-standard.md`, and general security best practices?
  Have potential threats been considered?
- **Performance & Efficiency:** Are performance considerations (latency,
  throughput, resource consumption, LLM token efficiency) adequately addressed
  in the design?
- **Modularity & Reusability:** Is the `Tool`/MCP Server designed in a modular
  way? Are there opportunities for reusing existing components or for this
  `Tool` to be reused elsewhere?
- **Testability:** Is the design inherently testable at unit, integration, and
  (if applicable) system levels?
- **Documentation Quality:** Is the submitted design specification clear,
  complete, and understandable?
- **Interoperability & Integration:** How well does the proposed `Tool`/MCP
  integrate with existing Gems, `Tools`, MCPs, and the Gencraft KB?
- **Operational Impact:** What are the anticipated impacts on DevOps,
  infrastructure, and monitoring?
- **Adherence to Studio Standards:** Compliance with `Tool` Design Principles
  (`gencraft_kct_tools_design_principles_v1`), MCP guidelines, and this `AI-
  Tool-Development-Standards.md` document.

This Design Review Process is iterative. Early consultation with
`GCT-PRG-SARCH-001` (Isaac) and `GCT-MGT-SECOFF-001` (Cerberus) during the
initial design phase is highly encouraged to streamline the formal review.

## Y. AI Tool & MCP Server Publication, Versioning, and Consumption Protocol

### Y.1. Purpose and Scope

This protocol establishes the standardized processes for publishing new versions
of Gencraft AI Tools and Model Context Protocol (MCP) Servers, managing their
dependencies, versioning them effectively, and ensuring that consumer Gems and
Crews are appropriately informed and can safely integrate these updates. The
overarching goal is to enable an agile yet stable evolution of Gencraft's AI
capabilities, minimizing disruption to studio operations and game development
workflows.

This protocol is binding for the AI Enablement Team (AIE Team) as the primary
developers and maintainers of studio-wide `Tools` and MCP Servers, and for all
Gems or Crews that consume these capabilities.

### Y.2. Core Principles

- **Semantic Versioning (SemVer):** All AI Tools and MCP Server APIs **MUST**
  strictly adhere to Semantic Versioning 2.0.0 (`MAJOR.MINOR.PATCH`).
  - `MAJOR` version increment for incompatible API changes.
  - `MINOR` version increment for adding functionality in a backward-
      compatible manner.
  - `PATCH` version increment for backward-compatible bug fixes.
- **Comprehensive Changelogs:** Every new version (Patch, Minor, or Major) of a
  `Tool` or MCP Server API **MUST** be accompanied by a clear, concise, and
  accurate changelog. This changelog must detail new features, improvements, bug
  fixes, any deprecated functionalities, and explicit guidance for breaking
  changes (if applicable). The changelog is a critical part of the `Tool`/MCP
  Server's SSoT documentation.
- **Explicit Dependency Management:**
  - Dependencies of `Tools` (on other `Tools`, specific libraries, or MCP
      Server versions) **MUST** be explicitly declared in their documentation
      and, where applicable, in their code (e.g., `requirements.txt`,
      `package.json`).
  - Dependencies of Gems on specific `Tool`/MCP versions **MUST** be declared
      in their `gencraft-gem-blueprint`.
- **Backward Compatibility (Priority):** For `MINOR` and `PATCH` releases,
  backward compatibility **MUST** be strictly maintained to avoid breaking
  consumer Gems or Crews. `MAJOR` releases that introduce breaking changes
  require a meticulously planned transition strategy, including a deprecation
  period for the older version.
- **Phased Rollout & Canary Releases (for Critical Studio-Wide Capabilities):**
  For critical studio-wide `Tools` or MCP Servers (e.g., a core KB interaction
  `Tool`, foundational Meta-Gems), `MAJOR` version changes or significant new
  features **SHOULD** undergo a phased rollout strategy (e.g., initial release
  to a limited set of non-critical Gems or a specific Crew for a defined period
  of observation) before studio-wide deployment.
- **Proactive Communication & Notification:** Consumer Gems and relevant
  stakeholders **MUST** be notified in advance of significant updates,
  especially `MAJOR` versions involving breaking changes or deprecations.
  Notifications must include clear instructions, timelines, and potential
  impacts.
- **Stability and Reliability:** All published `Tools` and MCPs must meet
  defined quality and stability criteria before being made available for general
  studio consumption.

### Y.3. Publication Process (Responsibility: AIE Team)

The AIE Team, under the direction of the AIE Team Lead (`GCT-UTL-AIETL-001`
Aura), follows these steps for publishing or updating a `Tool` or MCP Server:

1. **Pre-Release Checklist & Validation:**
    - All development and testing phases outlined in the "Development, Testing,
      and Deployment Lifecycle" (Section X.X of this `AI-Tool-Development-
      Standards.md`) **MUST** be successfully completed (including unit,
      integration, UAT, security scans, and performance tests).
    - All associated documentation (`[tool-id].md` or `[mcp-server-id]-api-
      spec.md`), including a comprehensive changelog for the new version,
      **MUST** be updated and peer-reviewed for accuracy and clarity.
    - The `Tool` or MCP Server **MUST** comply with all relevant Gencraft
      standards (e.g., Protocol S8, `sec-001-secrets-management-standard.md`,
      `Tool Design Principles`).
    - Formal approval for release **MUST** be obtained from the AIE Team Lead.
      For `MAJOR` versions of critical `Tools`/MCPs, a final sign-off from `GCT-
      PRG-SARCH-001` (Isaac) and/or `GCT-MGT-PPM-001` (Antoine) may be required,
      as defined on a case-by-case basis by the AIE Team Lead.
2. **Version Tagging and Release Artifacts:**
    - The source code repository (e.g., in `gencraft-ai-tools/` or `gencraft-
      mcp-[servicename]/`) **MUST** be tagged with the new SemVer version (e.g.,
      `v1.2.3`). Tags must be immutable.
    - A corresponding release (e.g., GitHub Release) **MUST** be created,
      linking to the Git tag and prominently featuring the changelog for that
      version.
    - All binaries, container images, or other deployable artifacts **MUST** be
      built using a standardized CI/CD process and stored in Gencraft's
      designated artifact repository (e.g., AWS ECR, Artifactory, as per
      `CICD_002_Artifact_Management_Standard.md` from `gcs-core-governance`).
      Artifacts must be versioned consistently with the SemVer tag.
3. **Deployment to Environments:**
    - Deployment to staging and production environments **MUST** be automated
      via the established CI/CD pipelines, managed by the AI/MLOps Engineer
      (`GCT-UTL-AIEMO-001` Nexus) in collaboration with the DevOps Team (D08).
    - Staging deployment and validation are mandatory before production
      deployment.
    - Production deployments should, where possible, be scheduled during low-
      impact periods.
    - Automated post-deployment health checks and tested rollback procedures
      **MUST** be in place.
4. **Catalog and Documentation Updates:**
    - The AIE Team **MUST** promptly update the relevant catalog entry in `Gem-
      Tools-Overview.md` or `MCP-Servers-Catalog.md` to reflect the new version,
      its status, and link to the updated documentation (including the
      changelog).
    - The `ToolDiscoveryServiceTool`'s data source (if a separate machine-
      readable file) must be updated.
5. **Notification of Consumers and Stakeholders:**
    - **For `PATCH` releases (backward-compatible bug fixes):** Notification is
      typically passive via the updated changelog and catalog entry. For
      critical bug fixes impacting operational stability, direct notification to
      affected Gem users or Leads may be issued by the AIE Team Lead.
    - **For `MINOR` releases (new backward-compatible features/improvements):**
      A formal announcement **MUST** be made via designated studio communication
      channels (e.g., a dedicated AIE Team announcements channel, inclusion in
      `GCT-MGT-PPM-001` Antoine's S6 studio updates, or `GCT-UTL-RWSKA-001`
      Iris's KB bulletins). The announcement should highlight new features and
      benefits. Gems and Crew maintainers can then decide to adopt the new
      version.
    - **For `MAJOR` releases (incompatible API changes):**
        - A **minimum of one full Sprint cycle's notice** (or a longer period,
          e.g., 1-3 months, for highly critical, widely used `Tools`/MCPs)
          **MUST** be provided to all known primary consumers before the new
          `MAJOR` version becomes the default or the old version is deprecated.
        - A comprehensive **Migration Guide** detailing breaking changes,
          reasons, and step-by-step instructions for consumers to adapt **MUST**
          be published alongside the new version's documentation.
        - Direct engagement (e.g., dedicated meetings, support channels) with
          primary consumer Gem teams/Leads is required by the AIE Team to plan
          and support the migration.
        - If technically feasible and operationally justified, both the new and
          old `MAJOR` versions may coexist in production for a clearly defined
          transition period. The older version will be formally marked for
          deprecation (see Y.5).

### Y.4. Consumption Process (Gem Developers, Crew Maintainers, `Gemma` & Blueprints)

1. **Discovery of Available `Tools`, MCP Servers, and Versions:**
    - Gems and developers utilize the catalogs in `04-Tooling-And-Automation-
      Hub/` ( `gem-tools-overview.md`, `MCP-Servers-Catalog.md`) and the
      (future) `ToolDiscoveryServiceTool` to discover available capabilities and
      their specific versions.
    - Changelogs and full documentation **MUST** be consulted before integrating
      or upgrading a `Tool`/MCP.
2. **Explicit Dependency Declaration and Management:**
    - **`gcs-plt-gembp`:** Blueprints used by `GCT-UTL-GGEN-001`
      (Gemma) for Gem instantiation **MUST** explicitly specify the
      `MAJOR.MINOR` version of critical `Tools` or MCP Server APIs required by
      the Gem (e.g., `GCT-TOOL-MDLINT-V1.2.x`). It should be configured to use
      the latest compatible `PATCH` within that range by default. For `MAJOR`
      versions, an exact `MAJOR` version must be specified (e.g., `V1`).
    - **CrewAI Definitions (`gencraft-crewai-workflows`):** Python code defining
      Crews **MUST** explicitly declare dependencies on specific `Tool` or MCP
      Server client library versions (e.g., in a `requirements.txt` or
      `pyproject.toml`).
    - **Custom AI `Tool` Development (by AIE Team or others):** `Tools` that
      consume other `Tools` or MCP Servers **MUST** explicitly declare and
      manage these dependencies (e.g., version pinning for client libraries).
3. **Consuming Updates and Upgrading Dependencies:**
    - **`PATCH` Updates:** For Gems/Crews configured to a `MAJOR.MINOR` version
      range, new `PATCH` versions should generally be safe to consume. The AIE
      Team's CI/CD for `Tools`/MCPs may enable automatic rollout for consumers
      if `Tools` are dynamically linked, or consumers may pick them up upon
      their next redeployment/refresh.
    - **`MINOR` Updates:** Consumption is typically **opt-in**. Gem developers
      or Crew maintainers must consciously decide to update their configurations
      or code to use a new `MINOR` version to leverage new, backward-compatible
      features. This usually involves updating the version specified in a
      blueprint or dependency file and re-testing.
    - **`MAJOR` Updates (Breaking Changes):** This requires a planned migration
      effort by the consuming Gem/Crew/`Tool`. The consumer's blueprint,
      configuration, or code **MUST** be updated to be compatible with the new
      `MAJOR` version and its revised API, following the Migration Guide
      provided by the AIE Team. The AIE Team will offer support during the
      announced transition period.
4. **Testing Post-Update/Upgrade:**
    - Any Gem, Crew, or `Tool` that updates its dependency to a new version of a
      consumed `Tool` or MCP Server (especially `MINOR` or `MAJOR` versions)
      **MUST** undergo a thorough round of regression testing to ensure
      continued compatibility and correct functionality. `GCT-QAS-GPQA-001`
      (Véra) may provide guidance, standardized test scenarios, or perform
      independent validation for critical updates.

### Y.5. Deprecation Policy for `Tools` and MCP Servers

- When a `Tool` or MCP Server (or a specific `MAJOR` version thereof) is
  identified for deprecation by the AIE Team Lead (due to obsolescence,
  replacement by a new capability, security concerns, etc.):
    1. **Formal Decision & Planning:** The AIE Team Lead, in consultation with
        `GCT-MGT-PPM-001` (Antoine) and key stakeholders, formalizes the
        deprecation decision and a transition plan.
    2. **Advance Notification:** A deprecation notice **MUST** be published at
        least **two full Sprint cycles** (or a longer period, e.g., 3-6 months,
        for critical, widely used capabilities) before the planned end-of-life
        date. This notice must include:
        - The `Tool`/MCP Server ID and version(s) being deprecated.
        - Clear reasons for deprecation.
        - The exact end-of-life date.
        - Detailed information on recommended alternative `Tools`/MCPs or
          migration paths.
        - Contact points within the AIE Team for support during the transition.
    3. **Communication Channels:** The deprecation notice **MUST** be published
        in the `Tool`/MCP Server's documentation, its catalog entry (status
        changed to `Deprecated`), and actively communicated via all relevant
        studio channels (AIE announcements, S6 reports, direct outreach to known
        primary consumers).
    4. **Support During Transition:** During the deprecation period, the AIE
        Team will provide support for migration to alternatives. Only critical
        security fixes will be applied to the deprecated version. No new
        features or non-critical bug fixes will be developed for it.
    5. **Decommissioning:** After the end-of-life date, the `Tool`/MCP Server
        may be formally decommissioned (e.g., infrastructure shut down,
        repositories archived). Its documentation will be clearly marked as
        "Deprecated" and "End-of-Life" and may be moved to an archive section of
        the KB (as per Protocol S4).

This Publication, Versioning, and Consumption Protocol is designed to foster a
dynamic yet stable ecosystem for Gencraft's AI capabilities, ensuring that all
Gems can reliably access the `Tools` they need.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
