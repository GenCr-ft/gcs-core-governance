---
docId: GOV-STAN-001
title: SSoT Document Naming and ID Convention
version: 2.2.0
authors:
- Gem-AA (Lead)
- Isaac (Architect)
- "\xC9douard (DevOps)"
knowledgeGuardian:
- Iris (GCT-UTL-RWSKA-001)
reviewers:
- Lug (Studio Director)
creation_date: '2025-06-10'
language: en
summary: "**DEPRECATION NOTICE:** The taxonomy and metadata rules previously defined in this document are now obsolete. The official and single source of truth for all studio-wide taxonomy, classification, and metadata rules is now defined in the standard `GOV-STANDARD-008: SSoT Master Taxonomy and Governance Standard`. Please refer to that document for all current definitions and to the `gcs.governance.yml` file for the raw vocabulary data."
metadata:
  scope: studio
  domain: governance
  doc-type: standard
  keywords:
  - docid
  - naming-convention
  - documentation
  lifecycle-stage: approved
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
last_updated_date: '2025-06-17'
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/foundations/governance/GOV-STAN-001.ssot-document-naming-and-id-convention.md
---
# SSoT Document Naming and ID Convention

## 1. Objective

This standard establishes the mandatory rules for assigning unique identifiers (`docId`) and filenames to all documents within the GenCr@ft Studio Single Source of Truth (SSoT). Adherence to this convention is critical for discoverability, traceability, and automated knowledge management.

## 2. The Convention

Every SSoT document MUST conform to the following rules:

1. **Unique Document ID (`docId`)**: The `docId` is the cornerstone of our SSoT. It MUST be stored in the document's YAML frontmatter.
2. **Strict Structure**: The `docId` MUST follow the `DOMAIN-TYPE-CODE` structure. Shortened forms are prohibited.
3. **Strict Casing**: All parts of the `docId` MUST be **UPPERCASE**.
4. **Matching Filename**: The document's filename MUST exactly mirror the `docId`, followed by a description.

### 2.1. `docId` Structure

**`DOMAIN-TYPE-CODE`**

- **`DOMAIN`**: A short, uppercase code representing the document's high-level domain.
- **`TYPE`**: An uppercase code defining the nature of the document.
- **`CODE`**: A unique, zero-padded 3-digit number, sequential within its `DOMAIN-TYPE` combination (e.g., `001`, `002`).

The official codes for `DOMAIN` and `TYPE` are defined in the YAML block in section 2.3.

**Full `docId` Example:** `GOV-STANDARD-005`

### 2.2. Filename Structure

**`<docId>.<description-in-kebab-case>.md`**

- **`<docId>`**: The full, uppercase `docId` from the frontmatter.
- **`<description-in-kebab-case>`**: A concise, lowercase summary of the document's content with words separated by hyphens.

**Full Filename Example:** `GOV-STANDARD-005.ssot-document-id-convention.md`

### 2.3. Official Codes Definition (SSoT)

This YAML block is the **single source of truth** for all official Domain and Type codes. It is designed to be parsed by tools like `gft-cli`.

```yaml
domain_codes:
  - code: ART
    name: Art & Creative
    description: Standards and guides for art, animation, and creative pipelines.
  - code: CICD
    name: Continuous Integration/Delivery
    description: Standards for build, test, and deployment automation.
  - code: ENG
    name: Engineering
    description: General software engineering principles, patterns, and practices.
  - code: GAME
    name: Game Design
    description: Game design documents, feature specifications, narrative content.
  - code: GIT
    name: GitHub Operations
    description: Standards for branching, commits, PRs, and repository management.
  - code: GOV
    name: Governance
    description: High-level studio policies, strategies, and foundational standards.
  - code: IAC
    name: Infrastructure as Code
    description: Standards and guides for managing cloud infrastructure.
  - code: LEGAL
    name: Legal & Compliance
    description: Licensing information, compliance policies, and legal notices.
  - code: OPS
    name: Operations
    description: Operational guides, onboarding procedures, and incident management.
  - code: QA
    name: Quality Assurance
    description: Test plans, QA processes, and quality metrics standards.
  - code: REC
    name: Records
    description: Immutable records such as ADRs and Postmortems.
  - code: SEC
    name: Security
    description: Security policies, procedures, and vulnerability management.
  - code: TOOL
    name: Tooling
    description: Specifications and guides for developer tools (e.g., gft-cli).

type_codes:
  - code: CAT
    name: Catalog / Registry (Short Form)
    description: A curated list or registry of assets.
  - code: STAN
    name: Standard (Short Form)
    description: A mandatory technical or procedural rule.
  - code: POL
    name: Policy (Short Form)
    description: A high-level, mandatory rule or principle.
  - code: ADR
    name: Architecture Decision Record
    description: A short document describing a key architectural decision.
  - code: CATALOG
    name: Catalog / Registry
    description: A curated list or registry of assets (e.g., repositories, tools).
  - code: GUIDE
    name: Guide / How-To
    description: A step-by-step instructional document for a specific task.
  - code: PLAN
    name: Plan
    description: A document outlining a plan for a project, migration, or test.
  - code: POLICY
    name: Policy
    description: A high-level, mandatory rule or principle for the studio.
  - code: POSTMORTEM
    name: Postmortem
    description: A formal analysis of an incident or event.
  - code: README
    name: README
    description: The primary entry-point documentation for a repository or directory.
  - code: REPORT
    name: Report
    description: The output of an analysis or audit.
  - code: REQ
    name: Requirement
    description: A formal specification of functional or non-functional requirements.
  - code: SPEC
    name: Specification
    description: A detailed technical specification for a tool, service, or API.
  - code: STANDARD
    name: Standard
    description: A mandatory technical or procedural rule to be followed.
  - code: STRATEGY
    name: Strategy
    description: A high-level document outlining the approach for a domain.
  - code: TPL
    name: Template
    description: A boilerplate document used to create other documents.
  - code: DOC
    name: Documentation
    description: A file that provides detailed information to users or developpers
```

## 4. Scope of Application

This convention applies to all Markdown (`.md`) documents intended to be part of the studio's official SSoT.

## 5. Automation and Tooling

The `gft-cli` tool and our CI/CD pipelines are designed to enforce this standard. The `gft docs new` command will use the codes defined in the YAML block above to generate compliant `docId`s and filenames.

## 6. Examples

### Correct Usage

- **A new security guide:**
  - `docId`: `SEC-GUIDE-004`
  - Filename: `SEC-GUIDE-004.how-to-use-vault.md`
- **A game design requirement for the player inventory:**
  - `docId`: `GAME-REQ-012`
  - Filename: `GAME-REQ-012.player-inventory-system.md`
- **An Architecture Decision Record for the CI/CD domain:**
  - `docId`: `CICD-ADR-001`
  - Filename: `CICD-ADR-001.switch-to-self-hosted-runners.md`

### Incorrect Usage

- `gov-001.md`: **Incorrect.** `docId` is lowercase, incomplete (missing `TYPE`), and the filename is not descriptive.
- `feature-flags-guide.md`: **Incorrect.** Missing a `docId` entirely.
- `TOOL-SPEC-001-gft-cli.md`: **Incorrect.** Description should not be part of the `docId`. The filename should be `TOOL-SPEC-001.gft-cli-specification.md`.
