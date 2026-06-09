---
docId: OPS-GUIDE-020
title: S20 Artifact Storage and Retention
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
  - devops-team
  keywords:
  - artifact-storage
  - retention
  - ssot
  - version-control
  - workflows
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-020.s20-artifact-storage-and-retention.md
---
# S20: Artifact Storage and Retention Standard

## 20.0. Justification and Objectives

**Why this protocol is critical for Gencraft and its AI Gems:**
In a collaborative and largely asynchronous environment like **Gencraft**,
particularly one driven by AI Gems, knowing precisely where to find
authoritative information and where to store new work products is paramount.
Without standardized storage locations and clear conventions:

- **Information Siloing & Inaccessibility:** Valuable knowledge and artifacts
  can become lost, difficult to find, or siloed within specific Gem "minds" or
  unmanaged locations, hindering collaboration, reuse, and discovery by `Iris`.
- **Version Control Chaos & Data Integrity Issues:** Multiple versions of the
  same document or artifact can proliferate in different places, leading to
  confusion, rework, and critical decisions based on outdated or incorrect
  information. This is especially problematic for AI Gems that need to rely on a
  definitive Single Source of Truth (SSoT).
- **Inefficiency and Wasted Gem Cycles:** Gems (AI and human) would spend
  excessive time and processing cycles searching for information or trying to
  determine which version of a document is the correct one, instead of focusing
  on productive tasks.
- **Onboarding Difficulties for New Gems:** New Gems (instantiated by `Gemma`
  using `gcs-plt-gembp`) would struggle to orient themselves and find
  the necessary context, resources, and SSoT locations for their roles if
  information is scattered.
- **Compromised Traceability, Auditing, and Compliance:** If artifacts are not
  stored in version-controlled, traceable locations (primarily `gcx-yyy`
  GitHub repositories), understanding their history, evolution, associated
  decisions, and ensuring compliance (e.g., with license terms managed by `Léo`)
  becomes nearly impossible for `Véra` or for project reviews.
- **Barriers to Automation and `Tool` Effectiveness:** AI Gems and their `Tools`
  that need to programmatically access, process, or update artifacts require
  predictable, standardized storage paths, formats (as per KC&T Guiding
  Principle #11), and APIs.

This protocol aims to:

- **Establish and Enforce a Single Source of Truth (SSoT) for All Studio
  Artifacts:** For every type of critical information or work product, there
  must be one clearly defined, authoritative, and version-controlled storage
  location.
- **Maximize Discoverability and Accessibility for All Gems:** Ensure all Gems
  can easily and reliably find the artifacts they need to perform their roles,
  using standardized search `Tools` (like `Iris`'s `KnowledgeBaseSearchTool`)
  and navigation paths defined in `gcs-core-governance`.
- **Facilitate Robust Collaboration and Version Control:** Leverage GitHub as
  the primary platform for its strengths in versioning, branching, merging, and
  review workflows (as per Protocol S1) for all applicable artifacts.
- **Streamline Information Workflows:** Reduce friction in how artifacts are
  created, shared, reviewed, approved, and archived by making storage locations
  and access methods predictable and protocol-driven.
- **Support the Integrity and Utility of the Gencraft Knowledge Base (KB):**
  Define where the components of the Gencraft KB (hub: `gcs-studio-
  handbook`; satellites: `gcp-aethel-docs-req`, `gcs-plt-architecture`, etc.)
  physically reside and how they are managed.
- **Ensure Long-Term Preservation, Security, and Integrity of Studio Assets:**
  Protect valuable studio assets, knowledge, and intellectual property through
  secure, managed, and versioned storage.

## 20.1. Core Principles for Artifact Storage at Gencraft

These storage protocols are guided by Gencraft's KC&T Guiding Principles,
especially:

- #1: Centralization and SSoT (GitHub as primary hub).
- #2: Accessibility and Transparency (Internal).
- #4: Exhaustive and Contextualized Traceability.
- #8: Security of Information.
- #11: Machine-Readable Structured Data by Default.
- #13: Maximal Contextual Awareness and Information Interconnection.

Additional principles specific to artifact storage include:

- **"As-Code" Philosophy for Documentation & Configuration:** Treat
  documentation (Markdown in `gcs-core-governance`, etc.), configuration
  files (YAML/JSON in `gcs-core-governance`, `gcs-plt-gembp`),
  and other text-based artifacts with the same rigor as application code
  (version control in Git, review via PRs, automated checks where possible).
  This is fundamental for AI Gem interaction and reliability.
- **Clear Ownership and Stewardship (Knowledge Guardianship):** Each primary
  storage location (e.g., a `gcx-yyy` GitHub repository) or major section
  within it (e.g., a domain in the KB) **must** have a designated Gem or
  department (Knowledge Guardian, as defined in `gcs-core-governance/00-studio-vision-and-principles/GOV-GUIDE-411.organization-and-roles.md`)
  responsible for its organization, upkeep, and adherence to storage standards.
- **Consistent Naming Conventions and Folder Structures:** These **must** be
  defined, documented (in `gcs-core-governance/02-knowledge-base-hub/KB-
  Contribution-And-Style-Guide.md`), and enforced (potentially via `Tools` or PR
  reviews by Knowledge Guardians or `Iris`) to aid navigation, search, and
  automation by AI Gems.
- **Minimize Unnecessary Redundancy; Maximize Linkage:** Avoid duplicating
  artifacts across multiple SSoT systems. If an artifact must be referenced
  elsewhere, use a direct, stable link (ideally a permalink from Git) to its
  SSoT. `Iris`'s `Tools` may help detect and flag significant duplication.

## 20.2. Standardized Storage Locations and Artifact Types

**How it works and why for AI Gems:** Specific types of artifacts are assigned
to predefined SSoT locations. This predictability is essential for AI Gems and
their `Tools` to reliably locate, read, and write information according to their
roles and tasks. The primary SSoT for most artifacts will be GitHub repositories
following the `gcx-yyy` naming convention.

### 20.2.1. Documentation, Knowledge Base (KB) Artifacts, Configurations, and Scripts

- **Types of Artifacts Covered:**
  - All content of the Gencraft Knowledge Base (GDDs in `gencraft-
        gamedesign-deepdive`, design specs in `gcp-aethel-docs-req`, lore in
        `gencraft-game-lore-and-world`, technical documentation in `gencraft-architecture` or `gencraft-engine-docs`, art/audio guidelines in `gcp-aethel-assets-styleguide`, UX/UI design system docs, QA
        strategies, operational protocols in `gcs-core-governance`,
        research summaries by `Iris` in `gencraft-studio-reports`, Gem
        dossiers by `Véra` in the KB, legal/license documentation by `Léo` in
        the KB).
  - Configuration files for systems and `Tools` (IaC scripts in `gcs-core-governance`, CI/CD pipeline definitions in project repos or
        `gcs-core-governance`, Gem `Tool` configurations in `gencraft-
        gem-blueprints` or `Tool` repos).
  - Meeting summaries and key decisions (if not directly in GitHub Issues,
        then as Markdown files linked from Issues, stored in relevant project
        or KB repos).
  - Scripts (Shell, Python, etc.) used for studio automation or
        development tasks (versioned in `gcs-core-governance` or
        specific `Tool` repos).
- **Primary Storage Location (SSoT):** Dedicated **`gcx-yyy` GitHub
    Repositories**.
  - The central `gcs-core-governance` for studio-wide knowledge and
        protocols.
  - Specialized satellite repositories for deep-domain knowledge (e.g., `gcp-aethel-docs-req`, `gcs-plt-architecture`, `gencraft-devops-standards`, `gcs-plt-gembp`, `gencraft-game-lore-and-world`).
  - Specific project code repositories (e.g., `gcl-voxel-engine`, `gcp-aethel-client`, `gcp-aethel-server`) will contain their own `README.md` files and potentially a `/docs` folder for highly specific technical documentation directly related to that codebase.
- **Primary Formats (for AI Gem processing):**
  - **Markdown (`.md`):** For all human-readable documents. **Must** include standardized YAML frontmatter for metadata (defined in `KB-Contribution-And-Style-Guide.md`).
  - **YAML (`.yml`, `.yaml`):** Preferred for human-readable and editable configuration files.
  - **JSON (`.json`):** For structured data interchange, machine-generated configurations, or when strict schema validation is paramount.
  - Other text-based formats (e.g., PlantUML source for diagrams rendered in Markdown, Gherkin `.feature` files for test cases) are also stored directly in Git.
- **Versioning & History:** Managed natively by **Git**. Every commit provides a traceable change. Branching strategies (e.g., GitFlow) will be
    defined in `gcs-core-governance`.
- **Review & Approval:** As per Protocol S1, all significant changes or new additions are proposed via **Pull Requests (PRs)**.
- **Organization:**
  - Clear, logical, and **consistently named folder structures** **must** be maintained within each repository.
  - These structures, along with file naming conventions, **must** be documented in `gcs-core-governance/02-knowledge-base-hub/KB-Contribution-And-Style-Guide.md`.
  - **For AI Gems:** Predictable paths and standardized frontmatter are essential for `Tools` like `Iris`'s `KBIndexerTool`, `Gemma`'s configuration `Tools`, and any Gem `Tool` that needs to read or write files (e.g., `GetKBArticleContentTool`, `MarkdownFileReadWriteTool`).

### 20.2.2. Large Binary Files

(Art Assets, Audio Assets, Game Builds, Voluminous Raw Data)

- **Types of Artifacts Covered:** As previously detailed (WIP large art/audio, final game-ready assets, game builds, large raw datasets).
- **Storage Strategy (Tiered Approach - SSoT for each tier):**
      1. **Final/Approved Game-Ready Assets (Primary SSoT for game integration):**
          - **Storage:** **Git LFS (Large File Storage)** integrated with relevant `gcx-yyy` GitHub repositories (e.g., a dedicated `gencraft-game-assets` repo, or within specific project repos like `gcp-aethel-client/assets/`).
          - **Process Link:** Approval process (Protocol S1) managed via GitHub Issues linking to previews; final commit to LFS signifies approved state.
      2. **Work-in-Progress (WIP) Very Large Files & Specialized Art/Audio Workflows (Primary SSoT for creation phase):**
          - **Storage:** A **dedicated, studio-managed Cloud Storage solution** (specific solution and guidelines in `gcs-core-governance/02-knowledge-base-hub/KB-Domain-DevOps-Infra/Cloud-Storage-Guidelines.md`).
          - **Process Link:** Existence, status, tasks, feedback, and approval **still managed via dedicated GitHub Issues** in relevant `gcx-yyy` project or asset repos. Issues **must** contain direct, stable links to the WIP files on cloud storage.
      3. **Game Builds (Internal Test, Release Candidates - SSoT for distributable game versions):**
          - **Storage:** A dedicated **artifact repository** (e.g., GitHub Packages, JFrog Artifactory, or a versioned section in cloud storage). CI/CD pipeline uploads builds here.
          - **Process Link:** Builds are versioned. Links to specific builds **must** be referenced in QA test cycle Issues and release Issues on GitHub.
      4. **Voluminous Raw Data (Logs, Telemetry - SSoT for raw analytical input):**
          - **Storage:** Cloud-based data warehousing or blob storage.
          - **Process Link:** `Iris` or other analytical Gems access this data via `Tools`/MCP Servers. Synthesized reports/analyses are then  stored as Markdown in the KB (e.g., `gencraft-studio-reports`). Access and retention policies are in `gcs-core-governance/03-Archiving-And-Retention/`.

### 20.2.3. Structured Data

(Game Parameters, LocalizationTables, Complex Asset Metadata - SSoT for queryable game data)

- **Types of Artifacts Covered:** Data best managed in a structured,
    queryable format.
- **Storage Strategy (Tiered Approach - SSoT for each tier):**
      1. **Simple to Moderately Complex Structured Data:**
          - **Storage:** **JSON, YAML, or CSV files** versioned within relevant `gcx-yyy` GitHub repositories (e.g., `gencraft-game-data/parameters/`, `gencraft-game-lore-and-world/localization/`). Schemas for these files (e.g., JSON Schema) should be co-located or in the KB.
      2. **Highly Relational or Large-Scale Transactional Data:**
          - **Storage:** A **dedicated database system** (e.g., PostgreSQL, cloud-hosted).
          - **Access for Gems:** **Exclusively via specific, secure `Tools` or MCP Servers** with well-defined APIs.
          - **Schema & API Documentation (SSoT):** Database schema (SQL DDL), migration scripts, and API documentation **must** be versioned in a Git repository (e.g., `gencraft-database-schemas`) and documented in the technical section of the KB.

### 20.2.4. Knowledge Base Portal & Discoverability (GitHub Pages from `gcs-core-governance`)

- **Primary Access Point for Humans:** The GitHub Pages site generated from
    `gcs-core-governance`.
- **Role for AI Gems:** The underlying well-structured Markdown and `Iris`'s
    index are the primary access for AI Gems. The portal serves as a human-
    friendly view of the same SSoT.

## 20.3. Responsibilities for Storage Management and Adherence

- **All Gems:** **Responsible** for storing their work products and
  communication artifacts in the correct SSoT locations, following naming/folder
  conventions (from `GOV-GUIDE-007.knowledge-management-and-contribution-guide.md`), and using PRs for
  changes to versioned SSoTs.
- **Lead Gems & Department Heads (Knowledge Guardians):** **Accountable** for
  their teams' adherence. Oversee artifact organization in their domains.
  Approve PRs.
- **`Isaac` (Software Architect) & `Édouard` (DevOps Specialist D - Strategy):**
  **Responsible** for defining/maintaining overall repository structure
  strategy, "as-Code" best practices, and the `gcs-core-governance` GitHub
  Pages setup. Key technical Knowledge Guardians.
- **DevOps Crew (`Adam`, `Benjamin`, `Camille`, `Diane`):** **Responsible** for
  technical setup/maintenance of storage infrastructure (Git LFS, cloud storage,
  artifact repos, DB hosting) and access permissions.
- **`Iris` (Research & Watch Specialist):** **Advises** on information
  architecture, helps ensure discoverability, maintains `Archive-Catalog.md`.
- **`Antoine` (Producer):** Overall **Accountability** for studio's
  information/artifact management practices.

## 20.4. Impact and Tooling for AI Gems

**How it affects Gems and what `Tools` they need:** AI Gems must autonomously
navigate and interact with these standardized storage locations.

- **Core GitHub Interaction `Tools` (Category 5 from
  `gencraft_kct_tools_categories_v1` - SSoT for these `Tool` specs is their own
  doc):**
  - `GitRepositoryTool(action, repo_url, path, content, branch, message,
    use_lfs_if_applicable)`: Enhanced to understand when to use LFS based on
    file type/size or repository configuration.
  - `MarkdownFileReadWriteTool(file_path, section_xpath_or_frontmatter_key,
    content_or_metadata_to_update, ensure_template_conformance)`: Must be
    template-aware and frontmatter-aware.
  - `PullRequestManagementTool`, `GitHubIssueManagementTool`.
- **Cloud Storage Interaction `Tools` (MCP Servers preferred, specs in `MCP-
  Servers-Catalog.md`):**
  - `CloudStorageAccessTool(action, storage_tier_config_name, remote_path,
    local_path_or_data, metadata)`: Action (upload, download, list,
    get_metadata, generate_link). `storage_tier_config_name` would point to a
    predefined configuration (e.g., "WIP_Art_Storage", "Build_Artifact_Archive")
    that includes bucket names, credentials (via secret manager), etc. This
    `Tool` **must** handle auth securely.
- **Knowledge Base Navigation & Search `Tools` (Category 1 from
  `gencraft_kct_tools_categories_v1` - SSoT for these `Tool` specs is their own
  doc or `Iris`'s Gem Blueprint):**
  - `KnowledgeBaseSearchTool`: **Must** be aware of the hybrid SSoT architecture
    (`gcs-core-governance` + satellites `gcx-yyy`). It needs to query
    `Iris`'s central index or know how to search across multiple configured
    repositories. It **must** understand and use the `KB-Contribution-And-Style-
    Guide.md` for paths and frontmatter YAML conventions.
  - `GetKBArticleTool(article_sso_path: str)`: Must resolve paths across the
    hybrid SSoT (e.g., `kb://gencraft-gamedesign-
    deepdive/mechanics/crafting.md`).
- **Specialized Data Store Interaction `Tools` (MCP Servers, specs in `MCP-
  Servers-Catalog.md`):**
  - `QueryGameParametersTool(parameter_group: str, version: Optional[str]) ->
    JSON`
  - `UpdateLocalizationStringTool(language_code: str, string_id: str, new_value:
    str, project_name: str) -> bool`
- **Awareness of SSoT and Structure (Configuration by `Gemma` from `gencraft-
  gem-blueprints`):**
  - A Gem's `backstory` or initial configuration **must** include:
    - Pointers to the SSoT for different data types relevant to its role (e.g.,
      `Étienne` "knows" GDD SSoT is `gcp-aethel-docs-gdd`).
    - Knowledge of, or a `Tool` to query, the `KB-Contribution-And-Style-
      Guide.md` for file/folder naming and Markdown/frontmatter conventions.
- **Validation `Tools` (potentially used by authoring `Tools` or PR checks):**
  - `FilePathConventionCheckTool(proposed_path, artifact_type, target_repo)`: To
    help Gems propose valid storage paths according to conventions.
  - `FrontmatterValidationTool(markdown_file_path,
    expected_schema_or_template_name)`: To ensure required metadata is present
    and correctly formatted before committing KB articles.
  - `MarkdownLinterTool(file_path, style_guide_profile)`: To check Markdown
    syntax and style.

This protocol for standardizing storage locations ensures that **Gencraft's**
collective knowledge and work products are meticulously organized, versioned,
secured, and readily accessible to all Gems (AI and human), forming a robust
foundation for all studio operations and future growth.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
