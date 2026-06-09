---
docId: DEV-SPEC-010
title: 'Specification: GenCr@ft Studio CLI (gft-cli)'
version: 1.6.0
authors:
- Gem-BB (Camille)
reviewers:
- Gem-AA (Lead)
- Gem-D (Strategy)
- Gem-A (Infra)
creation_date: '2025-06-13'
language: en
summary: This document provides the complete and final specifications for the `gft-cli`,
  a unified command-line interface to automate studio workflows, with a strict adherence
  to IaC principles and fully aligned with the SSoT naming conventions.
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: approved
  keywords:
  - cli
  - automation
  - specification
  - devops
  - iac
  - ssot-driven
  scope: studio
  domain: devops
  doc-type: specification
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/tooling/standards/DEV-SPEC-010.specification-gencrft-studio-cli-gft-cli.md
---
# Specification: GenCr@ft Studio CLI (`gft-cli`)

## 1. Vision & Objectives

The `gft-cli` will be the primary tool for interacting with the studio's standardized processes. It aims to reduce cognitive load and enforce SSoT standards seamlessly.

## 2. Core Principles

- **SSoT-Driven:** The CLI **must** dynamically read its configurations, templates, and available options from the relevant standard documents within the SSoT ecosystem, referencing them by their official, standardized `docId`.
- **Role-Aware:** The CLI's behavior adapts based on the user's role.
- **IaC Compliant:** The CLI **must not** create or manage infrastructure resources (like GitHub repositories).

## 3. Technology Stack & Architecture

- **Language**: Python 3.9+
- **Framework**: Typer
- **Key Libraries**: `questionary`, `PyYAML`, `GitPython`.
- **Distribution**: Packaged as a standalone executable.
- **Architecture**: Follows the two-tier automation strategy (CLI for individuals, Crews for backend processes) defined in `GOV-STRATEGY-006`.

## 4. Command Structure

- `gft config ...`
- `gft docs ...`
- `gft git ...`
- `gft template ...`
- `gft readme ...`

## 5. Detailed Feature Specifications

### 5.1. `gft config`

- **`gft config set-role`**: Sets the user's role by interactively reading from **`GOV-MATRIX-004.role-tooling-matrix.md`**.

### 5.2. `gft git` (Enhanced Specification)

- **`gft git branch`**:
  - **SSoT Integration:** It **must** read the allowed branch `type`s (e.g., `feature`, `fix`) directly from the standard **`GITHUB-STANDARD-001.branching-strategy.md`**.
  - **Input:** It will ask for the `<issue-id>` and `<short-description>` to construct a compliant branch name.

- **`gft git commit`**: A guided helper to build a compliant Conventional Commit message, with types read from **`TOOL-STANDARD-001.conventional-commits-standard.md`**.

- **`gft git pr create --issue <ISSUE_NUMBER>`**:
  - **SSoT Integration:**
    - It **must** fetch the content of the official PR template (**`GITHUB-TEMPLATE-001.pull-request-template.md`**) from the organization's `.github` repository.
    - It **must** intelligently pre-fill the PR body based on the issue details and branch type.

### 5.3. `gft docs` (Enhanced Specification)

- **`gft docs new`**:
  - **SSoT Integration:** It **must** follow the workflow described in **`GOV-PROCESS-001.ssot-document-generation-process.md`**. This includes:
    1. Reading the **`GOV-CATALOG-001.ssot-repository-catalog.md`** to allow domain selection.
    2. Discovering and using available document templates.
    3. Generating a compliant `docId` and filename based on the **`GOV-STANDARD-005.ssot-document-id-convention.md`**.

- **`gft docs check-frontmatter [FILE_PATH]`**: Validates a document's frontmatter against the rules in `GOV-STANDARD-005`.

- **`gft docs add-ia-instructions [FILE_PATH]`**: Appends the standard "IA Instructions" boilerplate section.

### 5.4. `gft template`

- **`gft template apply`**: Initializes the current directory with a standard studio template (e.g., `gct-repo-template-standard`).

### 5.5. `gft readme`

- **`gft readme index [DIRECTORY_PATH]`**: Automatically updates the `Index of Contents` in a `README.md` file.

## 6. Acceptance Criteria

- **AC 4.1 (`gft git branch`):** The command **must** present a list of branch types read dynamically from `GITHUB-STANDARD-001`.
- **AC 4.2 (`gft git pr create`):** The created PR on GitHub **must** use the content from `GITHUB-TEMPLATE-001` and be pre-filled.
- **AC 4.3 (`gft docs new`):** The entire creation flow **must** match the steps defined in `GOV-PROCESS-001` and use the conventions from `GOV-STANDARD-005`.
- **AC 5.1 (`gft template apply`):** The command **must** successfully populate the current empty directory with the contents of a selected template.
- **AC 5.2 (IaC Compliance):** There **must be no command** in the `gft-cli` that creates infrastructure resources.

## 7. Non-Functional Requirements

- **Performance:** The CLI must respond to user commands within 2 seconds for all operations.
- **Security:** The CLI must not store sensitive information in plaintext and must use secure methods for authentication (e.g., OAuth tokens).
- **Usability:** The CLI must provide clear, interactive prompts and error messages to guide users through its features.

## 8. Future Enhancements

- **`gft crew`**: A future command group to manage backend processes and workflows, as defined in `GOV-STRATEGY-006`.

## 9. References

- **`GOV-MATRIX-004.role-tooling-matrix.md`**: Defines the roles and their capabilities.
- **`GITHUB-STANDARD-001.branching-strategy.md`**: Defines the mandatory Git branching strategy.
- **`TOOL-STANDARD-001.conventional-commits-standard.md`**: Defines the Conventional Commits standard.
- **`GOV-PROCESS-001.ssot-document-generation-process.md`**: Defines the document generation process.
- **`GOV-STANDARD-005.ssot-document-id-convention.md`**: Defines the document ID conventions.

## 10. IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.

- **Purpose for AI Agents**: This document serves as the primary specification for the `gft-cli`. When a user asks "What is the gft-cli?", reference this document.
- **Context for AI Agents**: The `gft-cli` is a tool that automates studio workflows, ensuring compliance with SSoT standards and IaC principles. It is designed to be role-aware and fully integrated with the studio's operational protocols.
- **Action for AI Agents**: When a user asks how to use the `gft-cli`, provide them with the command structure and examples from this document. If they ask about specific commands, refer them to the relevant sections.
- **Updates for AI Agents**: If the `gft-cli` is updated, ensure this document reflects the latest features and specifications. Use the versioning system to track changes.
- **Compliance Check for AI Agents**: Ensure that any new features or commands added to the `gft-cli` adhere to the principles outlined in this document, particularly regarding SSoT integration and IaC compliance.
- **Feedback Loop for AI Agents**: If users report issues or suggest improvements, log these in the `gft-cli` issue tracker and update this document as necessary.
- **Documentation Updates for AI Agents**: When new commands or features are added, update the relevant sections in this document to maintain clarity and usability for all users.
- **Training for AI Agents**: Ensure that all AI agents interacting with the `gft-cli` are trained on this document and understand its structure and content.
- **Version Control for AI Agents**: Use the versioning system to track changes to this document, ensuring that all updates are documented and communicated to users.
- **Compliance with Studio Standards**: Ensure that the `gft-cli` remains compliant with all studio standards and protocols, particularly those related to DevOps and IaC.
- **User Education for AI Agents**: Provide users with educational resources and examples on how to effectively use the `gft-cli`, including common workflows and best practices.
- **Error Handling for AI Agents**: Implement robust error handling in the `gft-cli` to provide users with clear feedback when commands fail or when they do not comply with the expected standards.
- **Performance Monitoring for AI Agents**: Monitor the performance of the `gft-cli` to ensure it meets the specified response times and usability standards.
- **Security Practices for AI Agents**: Ensure that the `gft-cli` follows best security practices, particularly regarding sensitive information and authentication methods.
- **Community Contributions for AI Agents**: Encourage community contributions to the `gft-cli` and ensure that all contributions are reviewed against the standards outlined in this document.
- **Future Enhancements for AI Agents**: Keep track of potential future enhancements and features that could be added to the `gft-cli`, ensuring they align with the studio's strategic goals and operational protocols.
- **Feedback Mechanism for AI Agents**: Implement a feedback mechanism within the `gft-cli` to allow users to report issues, suggest improvements, and provide general feedback on their experience.
- **Documentation Clarity for AI Agents**: Ensure that this document is clear, concise, and easy to navigate for all users, providing them with the information they need to effectively use the `gft-cli`.
- **Compliance with SSoT Standards**: Ensure that all commands and features of the `gft-cli` are compliant with the SSoT standards defined in the studio's governance documents.
- **Integration with Other Tools**: Ensure that the `gft-cli` can integrate with other tools and services used within the studio, such as GitHub, to provide a seamless user experience.
- **User Support for AI Agents**: Provide users with support resources, such as FAQs and troubleshooting guides, to help them resolve common issues and understand how to use the `gft-cli` effectively.
- **Version History for AI Agents**: Maintain a version history of this document, including changes made, reasons for changes, and the date of each update, to ensure transparency and traceability.
- **Compliance with IaC Principles**: Ensure that the `gft-cli` adheres to Infrastructure as Code (IaC) principles, particularly in how it interacts with GitHub repositories and other infrastructure components.
- **Training for New Users**: Provide training materials and sessions for new users to help them understand how to use the `gft-cli` effectively and in compliance with studio standards.
- **Community Engagement**: Engage with the community to gather feedback, suggestions, and contributions to improve the `gft-cli` and its documentation.
[] - **Usage:** `gft docs new --template <template_id> --domain <domain>`
[] - **`gft docs check-frontmatter [FILE_PATH]`**: Validates the frontmatter of a document against the rules defined in `GOV-STANDARD-005.ssot-document-id-convention.md`.
[] - **`gft docs add-ia-instructions [FILE_PATH]`**: Appends the standard "IA Instructions" boilerplate section to a document.
[] -  **`gft template apply`**: Initializes the current directory with a standard studio template (e.g., `gct-repo-template-standard`).
[] - **`gft readme index [DIRECTORY_PATH]`**: Automatically updates the `Index of Contents` in a `README.md` file.
