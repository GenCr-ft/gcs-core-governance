---
docId: ENG-STANDARD-004
title: Gem Tools Overview
version: 1.0.0
authors:
- AI Compliance Agent
creation_date: '2025-05-26'
language: en
last_updated_date: '2026-05-20'
metadata:
  lifecycle-stage: approved
  keywords:
  - ai-tools
  - gem-tools
  - tool-discovery
  - tool-development
  - ai-enablement
  - gencraft
  scope: studio
  domain: production-management
  doc-type: standard
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/04-tooling-and-automation-hub/ENG-STANDARD-004.gem-tools-overview.md
---
# Gem Tools Overview, Discovery, and Governance

## 1. Introduction and Philosophy

This document provides a comprehensive overview of Gencraft's AI Gem `Tool` ecosystem. AI Gem `Tools` are specific software functions, libraries, scripts, or interfaces that enhance and extend the capabilities of individual Gems, allowing them to perform specialized tasks efficiently and reliably. They are distinct from MCP Servers, which are typically more extensive, standalone services with their own APIs (cataloged in `MCP-Servers-Catalog.md`).

**Philosophy:**

- **Empowerment:** `Tools` are designed to augment Gem capabilities, not to replace Gem reasoning where it is crucial.
- **Modularity & Reusability:** `Tools` should be designed as discrete, well-defined components that can be potentially reused by multiple Gems or even composed into more complex operations.
- **Standardization:** Adherence to Gencraft's `Tool` Design Principles (`gencraft_kct_tools_design_principles_v1`) and `AI-Tool-Development-Standards.md` is mandatory.
- **Discoverability:** `Tools` must be easily discoverable by Gems that might need them. This document outlines that strategy.
- **Reliability & Robustness:** `Tools` must be well-tested and include proper error handling.

This overview serves as a primary reference for all Gems to understand available `Tool` capabilities, for `GCT-UTL-GGEN-001` (Gemma) when configuring new Gems with initial `Tool` sets, and for the AI Enablement Team (AIE Team) in managing the `Tool` lifecycle.

## 2. Tool Categories

Gencraft `Tools` are broadly categorized based on their functionality. These categories help in organizing the `Tool` catalog and assist Gems in finding relevant capabilities. The definitive list of categories is maintained in `gencraft_kct_tools_categories_v1` (external document/list, to be fully integrated or referenced here). Examples include:

- **KB Interaction `Tools`:** For reading, searching, writing, and validating content in the Gencraft Knowledge Base.
  - Example: `KnowledgeBaseSearchTool`, `MarkdownAuthoringTool`, `KBLinkValidatorTool`.
- **Version Control `Tools`:** For interacting with GitHub repositories.
  - Example: `GitRepositoryTool`, `PullRequestManagementTool`, `GitHubIssueManagementTool`.
- **Communication `Tools`:** For standardized inter-Gem or Gem-to-human communication.
  - Example: `FormattedReportGeneratorTool`, `NotificationDispatchTool`.
- **Data Analysis & Processing `Tools`:** For manipulating, analyzing, and visualizing data.
  - Example: `DataAnalysisTool`, `SpreadsheetModelingTool`.
- **Specialized Task `Tools`:** Specific to certain domains like game design, art asset processing, code analysis, etc.
  - Example: `GameBalanceSimulationTool`, `VoxelAssetOptimizationTool`, `StaticCodeAnalysisToolWrapper`.
- **Meta-Gem Support `Tools`:** Used by Meta-Gems like `Gemma` or `Proximo`.
  - Example: `GemBlueprintAccessTool`, `PromptTemplateLibraryAccessTool`.

-(This section will be further detailed and aligned with `gencraft_kct_tools_categories_v1` by the AIE Team Lead).-

## 3. Tool Design and Development

### 3.1. Guiding Principles

All `Tools` must adhere to the "Gencraft: General Design Principles for KC&T `Tools`" (ID: `gencraft_kct_tools_design_principles_v1`). These principles cover aspects like idempotence, clarity of function, error handling, security, and traceability.

### 3.2. Development Standards

The development, testing, documentation, and deployment of all custom AI `Tools` are governed by the `ai-tool-development-standards.md` document, maintained by the AIE Team.

### 3.3. Proposing New Tools

The process for proposing new `Tools` is detailed in the `ai-enablement-team-charter.md` (Section 4.1). It involves submitting a `type:tool-request` GitHub Issue to the `gencraft-aie-backlog` using the `tool-request-template.md`.

### 3.4. Design Review Process

All new `Tools` (and significant modifications to existing ones) must undergo the formal "AI Tool & MCP Server Design Review Process" as defined in `ai-tool-development-standards.md` (based on guidelines established in Point 2.3 of `actions_KCnT.md`).

## 4. Tool Discovery Strategy

For Gems to effectively leverage available `Tools`, a multi-faceted discovery strategy is in place:

### 4.1. Centralized Catalog (`Tool` Inventory)

- **This Document as Primary Catalog:** This `gem-tools-overview.md` document serves as the primary human-readable and machine-parsable catalog for all non-MCP `Tools`.
- **Structure of Catalog Entries:** Section 5 ("Catalog of Gencraft Gem Tools") details the standardized format for each `Tool` entry.
- **Maintenance:** The AIE Team is responsible for adding new `Tools` to this catalog and updating their status (e.g., `Production`, `Beta`, `Deprecated`) as part of their release process.
- **Machine-Readable Format (Future Action):** `GCT-UTL-RWSKA-001` (Iris) and the AIE Team will collaborate to define and maintain a companion machine-readable version of this catalog (e.g., YAML or JSON file, potentially auto-generated from this Markdown or vice-versa) to facilitate automated processing by the `ToolDiscoveryServiceTool`.

### 4.2. Programmable Discovery (`ToolDiscoveryServiceTool`)

- **Concept:** A dedicated `Tool`, named `ToolDiscoveryServiceTool` (or similar, e.g., `GCT-TOOL-FIND-V1`), will be developed and maintained by the AIE Team.
- **Functionality:** This `Tool` will provide a programmatic interface for Gems to:
  - `find_tools_by_capability(description_of_need: str, gem_role: str = None, category: str = None) -> List[ToolInfo]`: Allows a Gem to describe a task or capability it needs. The `Tool` searches the catalog (using keywords, descriptions, category tags) and returns a ranked list of potentially relevant `Tools`. `ToolInfo` would include `ToolID`, name, description, and a link to its full documentation.
  - `get_tool_details(tool_id: str) -> ToolSpecification`: Returns detailed information about a specific `Tool`, including its API/invocation method, parameters, and expected output, parsed from its full documentation file.
  - `list_available_tools(status: str = "Production", category: str = None, keyword: str = None) -> List[ToolInfo]`: Lists all tools matching the given criteria.
- **Data Source:** The `ToolDiscoveryServiceTool` will query the machine-readable version of the catalog(s) in this Hub.

### 4.3. Gem Onboarding and Configuration (`GCT-UTL-GGEN-001` Gemma)

- **Initial Toolset:** When `GCT-UTL-GGEN-001` (Gemma) instantiates a new Gem using a `gencraft-gem-blueprint`, the blueprint will specify a list of essential, pre-approved `Tools` that the new Gem is configured with by default.
- **Discovery Directive:** The `backstory` or initial configuration of each Gem will include:
  - Pointers to this `gem-tools-overview.md` and the `04-Tooling-And-Automation-Hub/` for general awareness.
  - Instructions on how to use the `ToolDiscoveryServiceTool` if its initial toolset is insufficient for a novel task.

### 4.4. Role of `GCT-UTL-PGEN-001` (Proximo)

- `GCT-UTL-PGEN-001` (Proximo), when assisting Gems in formulating tasks or queries, can be configured to:
  - Suggest the use of known `Tools` for common tasks.
  - Guide Gems in using the `ToolDiscoveryServiceTool` if a suitable `Tool` is not immediately obvious.

### 4.5. Role of `GCT-UTL-RWSKA-001` (Iris)

- `GCT-UTL-RWSKA-001` (Iris) is co-Knowledge Guardian of this document and ensures the catalog structure supports effective indexing and search.
- Collaborates with the AIE Team on the machine-readable format of the catalog and the query capabilities of the `ToolDiscoveryServiceTool`.

## 5. Catalog of Gencraft Gem Tools

This section lists all formally documented Gencraft Gem `Tools` (excluding MCP Servers, which are in `MCP-Servers-Catalog.md`). `Tools` are added here by the AIE Team upon their official release.

-(This section will be populated. Each Tool entry below is a placeholder for the structure.)-

---

### **Tool ID:** `GCT-TOOL-[ShortName]-[Version]`

- **Tool Name:** `[Descriptive Name of the Tool]`
- **Version:** `[Current Semantic Version, e.g., 1.0.2]`
- **Status:** `Production` | `Beta` | `Alpha` | `Deprecated`
- **Brief Description:** `[1-2 sentence summary of what the tool does.]`
- **Primary User Gem(s)/Role(s):** `[e.g., GCT-UTL-RWSKA-001 (Iris), All Knowledge Guardians, Content Authoring Gems]`
- **Category:** `[From gencraft_kct_tools_categories_v1, e.g., KB Interaction, Data Processing]`
- **Keywords/Tags:** `[comma, separated, list, of, keywords, for, search]`
- **Link to Full Documentation:** `[Relative link to ./Tools/[tool-id].md]`
- **Owner/Maintainer:** AIE Team

---
*Example Entry:*

### **Tool ID:** `GCT-TOOL-MDLINT-V1`

- **Tool Name:** `Markdown Linter and Style Checker`
- **Version:** `1.0.0`
- **Status:** `Production`
- **Brief Description:** Validates Markdown files against the rules defined in `GOV-GUIDE-007.knowledge-management-and-contribution-guide.md` and common Markdown best practices.
- **Primary User Gem(s)/Role(s):** `GCT-UTL-KFE-001` (Lexicon), All Knowledge Guardians, All Gems contributing to KB.
- **Category:** `KB Interaction Tool`
- **Keywords/Tags:** `markdown, lint, style, validation, kC&T`
- **Link to Full Documentation:** `./Tools/GCT-TOOL-MDLINT-V1.md`
- **Owner/Maintainer:** AIE Team

---

### S8 Security Tools

The following `Tools` are defined in OPS-GUIDE-008 §8.11 (Security Management Protocol). They are currently at `Alpha` status — their interfaces are specified but full implementations are pending. Full per-tool documentation will be authored in `./tools/` as each Tool is implemented.

#### Standard Security Tools (Available to All Gems)

---

### **Tool ID:** `GCT-TOOL-SEC-REPORT-V1`

- **Tool Name:** `Report Security Event`
- **Version:** `0.1.0`
- **Status:** `Alpha`
- **Brief Description:** Creates a confidential security report issue in `gcs-security-core` and notifies `Cerberus`. Covers vulnerability reports, policy violations, suspicious activity, and active incidents.
- **Primary User Gem(s)/Role(s):** All Gems (mandatory for security event reporting)
- **Category:** `Security`
- **Keywords/Tags:** `security, reporting, incident, vulnerability, cerberus`
- **Link to Full Documentation:** OPS-GUIDE-008 §8.11.2 (full spec TBD: `./tools/GCT-TOOL-SEC-REPORT-V1.md`)
- **Owner/Maintainer:** AIE Team / `Cerberus`

---

### **Tool ID:** `GCT-TOOL-SEC-GETSEC-V1`

- **Tool Name:** `Get Secret`
- **Version:** `0.1.0`
- **Status:** `Alpha`
- **Brief Description:** Securely retrieves a named credential from the Gencraft Secret Management System. Access is logged to `Véra`; the secret value itself is never logged.
- **Primary User Gem(s)/Role(s):** All Gems requiring runtime credential access
- **Category:** `Security`
- **Keywords/Tags:** `secrets, credentials, vault, security`
- **Link to Full Documentation:** OPS-GUIDE-008 §8.11.2 (full spec TBD: `./tools/GCT-TOOL-SEC-GETSEC-V1.md`)
- **Owner/Maintainer:** AIE Team / `Cerberus`

---

### **Tool ID:** `GCT-TOOL-SEC-CLASSIFY-V1`

- **Tool Name:** `Classify Data`
- **Version:** `0.1.0`
- **Status:** `Alpha`
- **Brief Description:** Suggests the Gencraft information classification level (L0–L3) for a given data sample or description, based on `SEC-STANDARD-001`.
- **Primary User Gem(s)/Role(s):** All Gems handling data of uncertain classification
- **Category:** `Security`
- **Keywords/Tags:** `data-classification, security, l2, l3, policy`
- **Link to Full Documentation:** OPS-GUIDE-008 §8.11.2 (full spec TBD: `./tools/GCT-TOOL-SEC-CLASSIFY-V1.md`)
- **Owner/Maintainer:** AIE Team / `Cerberus`

---

#### Specialised Security Tools (Cerberus, DevOps, AIE Team, Isaac)

---

### **Tool ID:** `GCT-TOOL-SEC-ENCRYPT-V1`

- **Tool Name:** `Encrypt / Decrypt Data`
- **Version:** `0.1.0`
- **Status:** `Alpha`
- **Brief Description:** Encrypts or decrypts data using keys from the Gencraft Secret Management System, enforcing the key hierarchy defined in `SEC-STANDARD-002`.
- **Primary User Gem(s)/Role(s):** `Cerberus`, `Adam` (GCT-DVO-DSINF-001), DevOps Gems
- **Category:** `Security`
- **Keywords/Tags:** `encryption, decryption, kms, data-security`
- **Link to Full Documentation:** OPS-GUIDE-008 §8.11.3 (full spec TBD: `./tools/GCT-TOOL-SEC-ENCRYPT-V1.md`)
- **Owner/Maintainer:** AIE Team / `Cerberus`

---

### **Tool ID:** `GCT-TOOL-SEC-SAST-V1`

- **Tool Name:** `Execute SAST Scan`
- **Version:** `0.1.0`
- **Status:** `Alpha`
- **Brief Description:** Runs a static application security test (SAST) scan against a code repository branch and returns a structured report of findings.
- **Primary User Gem(s)/Role(s):** `Cerberus`, `Adam`, CI/CD automation
- **Category:** `Security`
- **Keywords/Tags:** `sast, static-analysis, security-scanning, ci`
- **Link to Full Documentation:** OPS-GUIDE-008 §8.11.3 (full spec TBD: `./tools/GCT-TOOL-SEC-SAST-V1.md`)
- **Owner/Maintainer:** AIE Team / `Cerberus`

---

### **Tool ID:** `GCT-TOOL-SEC-SCA-V1`

- **Tool Name:** `Execute SCA (Dependency) Scan`
- **Version:** `0.1.0`
- **Status:** `Alpha`
- **Brief Description:** Scans a dependency manifest (`package.json`, `Cargo.toml`, `requirements.txt`) against known CVE databases and returns findings. Used in CI gates per `SEC-POLICY-001`.
- **Primary User Gem(s)/Role(s):** `Cerberus`, `Adam`, CI/CD automation, all code-producing Gems
- **Category:** `Security`
- **Keywords/Tags:** `sca, dependency-scanning, cve, supply-chain`
- **Link to Full Documentation:** OPS-GUIDE-008 §8.11.3 (full spec TBD: `./tools/GCT-TOOL-SEC-SCA-V1.md`)
- **Owner/Maintainer:** AIE Team / `Cerberus`

---

### **Tool ID:** `GCT-TOOL-SEC-INCIDENT-V1`

- **Tool Name:** `Assess and Coordinate Security Incident`
- **Version:** `0.1.0`
- **Status:** `Alpha`
- **Brief Description:** Composite tool set for incident commanders: assesses incident severity, coordinates SIRT actions, initiates containment (isolate system, quarantine Gem, block IP), and logs forensic chain of custody. See OPS-GUIDE-008 §8.11.3 for sub-tool signatures.
- **Primary User Gem(s)/Role(s):** `Cerberus` (IC), `Adam`, AIE Team
- **Category:** `Security`
- **Keywords/Tags:** `incident-response, sirp, containment, forensics, cerberus`
- **Link to Full Documentation:** OPS-GUIDE-008 §8.11.3 + `SEC-GUIDE-003` (full spec TBD: `./tools/GCT-TOOL-SEC-INCIDENT-V1.md`)
- **Owner/Maintainer:** AIE Team / `Cerberus`

---

### **Tool ID:** `GCT-TOOL-SEC-AUDIT-V1`

- **Tool Name:** `Security Audit Tools`
- **Version:** `0.1.0`
- **Status:** `Alpha`
- **Brief Description:** Suite of audit tools for `Cerberus`: audit data encryption settings, audit SDLC compliance, generate access reports, verify vulnerability fixes, query asset inventory, and ingest scan results. See OPS-GUIDE-008 §8.11.3 for per-function signatures.
- **Primary User Gem(s)/Role(s):** `Cerberus`, `Isaac` (GCT-PRG-SARCH-001)
- **Category:** `Security`
- **Keywords/Tags:** `audit, compliance, encryption, access-control, vulnerability`
- **Link to Full Documentation:** OPS-GUIDE-008 §8.11.3 (full spec TBD: `./tools/GCT-TOOL-SEC-AUDIT-V1.md`)
- **Owner/Maintainer:** AIE Team / `Cerberus`

---

### **Tool ID:** `GCT-TOOL-SEC-TRAINING-V1`

- **Tool Name:** `Security Awareness and Training Tools`
- **Version:** `0.1.0`
- **Status:** `Alpha`
- **Brief Description:** Tools for developing and distributing security awareness content: develop training module, broadcast security bulletin to Gems, and track training completion. See `SEC-GUIDE-004` for program context.
- **Primary User Gem(s)/Role(s):** `Cerberus`, `Véra` (GCT-UTL-QAMON-001)
- **Category:** `Security`
- **Keywords/Tags:** `training, awareness, bulletin, compliance, cerberus, vera`
- **Link to Full Documentation:** OPS-GUIDE-008 §8.11.3 + `SEC-GUIDE-004` (full spec TBD: `./tools/GCT-TOOL-SEC-TRAINING-V1.md`)
- **Owner/Maintainer:** AIE Team / `Cerberus`

---

-(End of catalog section. New `Tool` entries will follow this structure.)-

## 6. Governance of this Document

- This `gem-tools-overview.md` is a living document.
- Additions or significant modifications to the **Tool Discovery Strategy** (Section 4) or the **Catalog Structure** (Section 5) require discussion with and approval from the AIE Team Lead and `GCT-PRG-SARCH-001` (Isaac).
- The AIE Team is responsible for keeping the **Catalog of Gencraft Gem Tools** (Section 5 content) up-to-date as `Tools` are developed, versioned, and deprecated.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
