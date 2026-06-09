---
docId: ARC-SPEC-003
title: "Technical Specification: gft-cli Golden Path Commands"
version: "1.0.0"
date: "2025-07-12"
authors:
  - "Architecture Crew (CC)"
  - "DevOps Crew (EE)"
knowledgeGuardian: "Édouard (DevOps Crew)"
status: "Approved"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/records/specs/ARC-SPEC-003.gft-cli-golden-path.md
metadata:
  domain: architecture
  classification:
    category: to-describe
    type: specification
  lifecycle-stage: approved
  security-classification: "l2-confidential"
  intended-audience:
    - devops-crew
    - architects
---

# Technical Specification: gft-cli Golden Path Commands

## 1. Objective

This document provides the detailed technical specification for the `gft-cli`, our primary tool for interacting with the Gencraft SSoT. It translates the architectural decisions defined in ADRs 200-205 into concrete functional requirements for the tooling team. The goal is to ensure the CLI effectively implements our "Golden Path," abstracting complexity and guaranteeing compliance for all developers.

## 2. Guiding Principles

The CLI's implementation MUST adhere to these core principles:

* **Governance-Driven:** The tool's behavior is dynamically configured by the resolved governance files (`taxonomy.yml`, `rules/*.yml`, etc.), not hardcoded.
* **Context-Aware:** The tool MUST implement the "Governance Resolver" to apply the correct set of global and local rules based on the execution context.
* **User-Centric:** The tool's interface MUST be intuitive, asking questions in plain language and presenting human-readable options.

## 3. Command Specification: `gft new`

This is the primary command for scaffolding new, compliant services.

### 3.1. Prerequisites

* **Repository Provisioning:** This command MUST be executed from within an empty local directory that has been initialized as a Git repository (`git init`) and is linked to a remote origin (`git remote add origin ...`). The remote repository on GitHub MUST have been provisioned beforehand through the official IaC process managed in the `gencraft-iac` repository. The `gft-cli` is NOT responsible for creating the remote repository.

### 3.2. Signature

```bash
gft new --template <template_name> --name <service_name>
```

* `--template <template_name>`: Mandatory. For the MVP, the only accepted value is `service-backend-ts`.
* `--name <service_name>`: Mandatory. The machine-readable name for the new service (e.g., `aethel-inventory-service`).

### 3.3. Orchestration Workflow

The command **MUST** execute the following sequence of operations:

1. **Context Validation**: The CLI verifies it is being run from within a valid Gencraft project environment.
2. **Governance Resolution**: The CLI executes the Governance Resolver to produce the unified, in-memory configuration object based on the current context (merging global and project-specific laws).
3. **Template Discovery**: The CLI reads the resolved `repository_catalog` to find the Git URL of the specified template repository (e.g., `gct-service-template-ts`).
4. **Cloning**: The CLI clones the template repository into a new local directory named `<service_name>`. If the directory already exists, it must fail with a clear error message.
5. **Interactive Metadata Wizard**: The CLI initiates an interactive session to gather the required metadata for the new service's "Identity Card" (`.ssot.yml`).
    * It prompts the user for fields like `description`, `owner_crew_id`, etc.
    * For fields linked to the taxonomy (e.g., `domain`), it **MUST** present a choice list populated with the human-readable `skos:definitions`, while storing the corresponding kebab-case `skos:prefLabel`.
6. **Identity Card Generation**: The CLI generates a unique `docId` (e.g., `CODE-SVC-001`) and creates the `.ssot.yml` file at the root of the new service directory, populating it with the collected metadata.
7. **Variable Substitution**: The CLI scans all files within the new service directory for standard placeholders and replaces them. The standard placeholders are:
    * `__SERVICE_NAME__`: The `<service_name>` provided by the user.
    * `__DOC_ID__`: The newly generated `docId`.
    * `__OWNER_CREW_ID__`: The owner crew ID collected during the wizard.
    * `__CURRENT_DATE__`: The current date in `YYYY-MM-DD` format.
8. **Post-Clone Initialization**: The CLI orchestrates the final setup steps inside the new service directory:
    * Deletes the `.git` directory from the cloned template.
    * Executes `git init` to create a fresh local repository.
    * Copies the `.env.template` file to a new `.env` file to provide local environment variables.
    * Executes `npm install` to install all necessary dependencies.
9. **Final Validation**: The CLI automatically runs `gft validate .` on the newly created service directory to ensure it is 100% compliant from birth.
10. **Success Message**: Upon successful completion of all steps, the CLI prints a confirmation message indicating the path to the new service and key next steps for the developer.

## 4. Command Specification: `gft validate`

This command is the local entry point to our SSoT Linter.

### 4.1. Signature

```bash
gft validate <path_to_artifact_or_directory>
```

### 4.2. Logic

1. **Context Discovery & Resolution**: The command executes the Governance Resolver to load the applicable set of laws for the given path.
2. **Validation Execution**: It performs a multi-level validation:
    * **Structural Validation**: Validates all relevant governance files (the `.yml` laws, `.ssot.yml` identity cards, `.md` frontmatters) against their corresponding `.schema.json` files.
    * **Semantic Validation**: Performs cross-validation checks. For example, it verifies that the value of a `domain` field in a frontmatter corresponds to an actual term defined in the resolved `taxonomy.yml`.
    * **Rule Validation**: Applies the logic from the resolved `validation-rules.yml` to the artifact.
3. **Reporting**: Reports all errors in a clear, actionable format, specifying the file, the line number, the violated rule, and a suggestion for remediation.

## 5. Error Handling

The `gft-cli` must be robust. The specification must include detailed error handling for cases such as:

* Destination directory for `gft new` already exists.
* Required tools (Git, Node.js, npm) are not installed on the user's machine.
* Failure to clone the template repository (e.g., authentication issue, network error).
* `npm install` fails.
* User provides invalid input during the interactive wizard.
* The final `gft validate` check fails.

For each case, the CLI must exit with a non-zero status code and provide a helpful message to the user.
