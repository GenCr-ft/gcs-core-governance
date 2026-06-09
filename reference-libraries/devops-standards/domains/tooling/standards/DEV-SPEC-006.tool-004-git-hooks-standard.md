---
docId: DEV-SPEC-006
title: Tool 004 Git Hooks Standard
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This standard defines mandatory guidelines for utilizing Git hooks within
  Gencraft studio project repositories. It mandates the use of the `pre-commit` framework
  to automate quality checks, enforce coding standards, and provide immediate feedback,
  shifting quality control "left" in the development workflow.
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - git-hooks
  - pre-commit
  - quality-control
  - coding-standards
  - devops
  - automation
  - gencraft
  scope: studio
  domain: devops
  doc-type: specification
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/tooling/standards/DEV-SPEC-006.tool-004-git-hooks-standard.md
---
## 1. Objective

This standard defines the mandatory guidelines and best practices for the setup, configuration, and
utilization of client-side Git hooks within all Gencraft studio project repositories. The primary goals
are to automate essential quality checks, enforce compliance with studio coding and commit standards, and
provide immediate, actionable feedback to developers (both AI Gems and humans) _before_ code is pushed to
remote repositories. This "shift-left" approach aims to improve overall code quality, reduce CI pipeline
failures, and streamline the development workflow.

## 2. Scope

This standard applies to ALL Git repositories within the `GenCr-ft` GitHub organization that contain
version-controlled artifacts requiring quality and compliance checks, including but not limited to:

- Source code repositories (game projects, studio tools, AI Gem tools).
- Infrastructure as Code (IaC) repositories.
- "As-code" configuration repositories.
- "As-code" documentation repositories (e.g., `gcs-core-governance`, `gcs-core-governance`).

The specific set of hooks applied MAY vary slightly based on repository type (e.g., IaC repos will have
IaC-specific linters), but the framework and mandatory core hooks defined herein MUST be implemented.

## 3. Standard

### 3.1. Mandatory Framework: `pre-commit`

- **Standard Tool:** The `pre-commit` framework ([https://pre-commit.com/](https://pre-commit.com/)) IS
  THE MANDATORY tool for managing client-side Git hooks at Gencraft. Direct manual scripting of individual
  files in `.git/hooks/` for shared or mandatory hooks is PROHIBITED to ensure consistency, ease of
  management, and versioning of hook configurations.

- **Installation:**
  - Installation via `pipx install pre-commit` or `sudo apt install python3-pre-commit` (for WSL/Ubuntu)
    is recommended, as verified by `validate_gft_devops_environment_proj103.sh`. All contributors are
    responsible for having `pre-commit` installed in their development environment.
- **Configuration:**
  1. Each Gencraft Git repository subject to this standard MUST contain a valid `.pre-commit-config.
yaml` file at its root, versioned within the repository. 2.**SSoT Template (Action for `Camille` - Gem AB):** A baseline `.pre-commit-config.yaml` template,
     including all mandatory and recommended Gencraft hooks with approved revisions (`rev:`), MUST be
     created and maintained at `configs/.pre-commit-config.yaml`.
     3.Repository maintainers MUST use this SSoT template as the starting point for their project's `.
pre-commit-config.yaml`.
     4.Project-specific additions or overrides to the SSoT template are permissible but MUST be justified
     in the project's `README.md` or a dedicated `DEVELOPMENT_GUIDE.md`, and SHOULD be reviewed by
     `Édouard` (Gem AD) or `Camille` (Gem AB) for alignment with studio best practices. Omission of
     MANDATORY hooks from the SSoT template is NOT PERMITTED without a formal exception (see Section 6).

### 3.2. Mandatory Standard Hooks (to be included in SSoT `.pre-commit-config.yaml`)

The SSoT template will define the exact hook `id`, `repo`, `rev`, and `args`.

1.**Commit Message Validation (`commit-msg` hook) - MANDATORY:**

- **Objective:** Enforce `tool-001-conventional-commits-standard.md`.
- **Tool:** `commitlint` (via a `pre-commit` compatible hook).
- **Configuration:** MUST use the Gencraft standard `commitlint` configuration (SSoT: `../commitlint.
config.js` - To Be Created by `Édouard`).

  2.**Basic File Sanity Checks (`pre-commit` hook) - MANDATORY:**

- **Objective:** Ensure consistent file endings, remove trailing whitespace, check for large files
  added accidentally.
- **Tool:** Standard hooks from `pre-commit-hooks` repository (e.g., `check-added-large-files`,
  `end-of-file-fixer`, `trailing-whitespace`, `check-yaml`, `check-json`).
- **Configuration:** Sensible defaults from the SSoT template. Max file size for
  `check-added-large-files` to be defined by `Édouard` (e.g., 1MB, with Git LFS as the alternative for larger assets).

  3.**Markdown Linting (`pre-commit` hook) - MANDATORY for repositories with `.md` files:**

- **Objective:** Enforce `../../gcs-core-governance/02-knowledge-base-hub/
kb-contribution-and-style-guide.md` for Markdown quality.
- **Tool:** `mdl` (via `GCT-TOOL_MDLINT-V1` or a pre-commit compatible wrapper).
- **Configuration:** MUST use the studio's standard `.mdlrc` (SSoT: `gcs-core-governance/linting/
configs/.mdlrc` - To Be Created by `Édouard`).

  4.**Secrets Detection (`pre-commit` hook) - MANDATORY:**

- **Objective:** Prevent accidental commit of sensitive information (API keys, passwords, etc.).
- **Tool:** The Gencraft standard secret scanning tool (e.g., `gitleaks`, `detect-secrets`), as
  defined in `gcs-core-governance/security/SEC_00X_Secret_Scanning_Tool_Standard.md` (To Be Created by
  `Cerberus`/`Édouard`).
- **Configuration:** MUST use Gencraft standard configuration for the chosen tool, including any
  custom detection rules or a baseline of allowed patterns (false positives).

### 3.3. Strongly Recommended Standard Hooks

(to be included in SSoT `.pre-commit-config.yaml`but may bevdisabled with justification)

1. **Automatic Code Formatting (`pre-commit` hook):**

   - **Objective:** Enforce `tool-003-code-style-and-formatting.md`.
   - **Tools:** `prettier`, `black`, `clang-format`, etc., based on language.
   - **Configuration:** MUST use Gencraft standard configurations for these formatters (SSoT for configs:
     `gcs-core-governance/formatting/configs/` - To Be Populated by `Édouard`).

2.**IaC Linting & Security Scanning (`pre-commit` hook) - For IaC repositories:**

- **Objective:** Enforce `../iac/iac-007-iac-static-analysis-standard.md`.
- **Tools:** `tflint`, `tfsec` (or approved alternative).
- **Configuration:** Must use repository-level (`.tflint.hcl`) or SSoT configurations.

  3.**Language-Specific Linting (`pre-commit` hook):**

- **Objective:** Enforce `tool-002-language-specific-tooling-standards.md`.
- **Tools:** `eslint`, `pylint`, `flake8`, etc.
- **Configuration:** MUST use Gencraft standard configurations for these linters (SSoT for configs:
  `gcs-core-governance/linting/configs/`).

### 3.4. Installation and Usage in Repositories

1.**AI Gem (`Camille` or Dev Lead Gem) Action for Repository Setup:** When initializing a new repository
or applying this standard to an existing one, the responsible Gem MUST: - Copy the SSoT `.pre-commit-config.yaml` template from `gencraft-devops-automation/git-hooks/
    templates/` to the repository root. - Copy any required SSoT tool configuration files (e.g., `.mdlrc`, `.tflint.hcl` template, formatter
configs, `../commitlint.config.js`) from their respective SSoT locations in `gcs-core-governance/` to
the repository root or the conventional location expected by the hook. - Customize the `.pre-commit-config.yaml` if necessary (e.g., add project-specific hooks, adjust file
inclusions/exclusions for specific linters). Justifications for disabling MANDATORY hooks from the
SSoT template require a formal exception (Section 6). - Commit these configuration files to the repository. - Update the repository's `README.md` or `DEVELOPMENT_GUIDE.md` to instruct contributors on installing
and using the hooks. 2.**All Contributors (Gems and Humans) Action:** Upon cloning or pulling a repository containing a `.
pre-commit-config.yaml` for the first time, or after an update to the config file: - MUST run `pre-commit install` to install or update the hooks locally. - MUST run `pre-commit install --hook-type commit-msg` if `commit-msg` hooks are defined (which is mandatory). - Hooks will then run automatically on `git commit`. Failed hooks will prevent the commit. - To run all hooks on all files (e.g., before a PR): `pre-commit run --all-files`. - To run hooks only on staged files: `pre-commit run`. 3.**Bypassing Hooks:**

- Temporarily bypassing hooks (e.g., for work-in-progress commits _on local feature branches only_)
  can be done using `git commit --no-verify`.
- This MUST be used sparingly and with explicit justification if the code is to be shared.
- Code pushed to remote branches that are targets for Pull Requests (e.g., `develop`, `main`) MUST
  have passed all relevant hooks. CI pipelines will also enforce these checks.

### 3.5. Custom Hooks for Gencraft

- Project-specific custom hooks MAY be developed if standard community hooks are insufficient.
- Custom hook scripts MUST be stored within the repository, typically in a `.githooks/` or `scripts/
git-hooks/` directory, and referenced as `local` hooks in `.pre-commit-config.yaml`.
- They MUST be well-documented (purpose, usage, dependencies, programming language) and adhere to `../
scripting/script-001-general-scripting-standard.md`.
- **SSoT for Gencraft-wide reusable custom hook scripts:** `gencraft-devops-automation/git-hooks/
custom-hooks/` (To Be Populated by `Camille` as needs arise).

### 3.6. Management and Updates

- The `.pre-commit-config.yaml` file is versioned with its repository.
- **SSoT Template Updates (`Camille`, `Édouard`):** `Édouard` (Gem AD) and `Camille` (Gem AB) are
  responsible for periodically reviewing and updating the SSoT `.pre-commit-config.yaml` template in
  `gcs-devops-automation/git-hooks/templates/` with new hook versions (`rev:`), improved
  configurations, or new standard hooks. This update process SHOULD involve testing.
- **Project-Level Updates (Repository Maintainers):** Repository maintainers are responsible for
  periodically updating their project's `.pre-commit-config.yaml` based on updates to the SSoT template or
  specific project needs. The command `pre-commit autoupdate` can assist, but manual review and testing are
  necessary.

## 4. Responsibilities

- **`Édouard` (Gem AD - DevOps Strategy):**
  - Maintenance and evolution of this standard.
  - Maintenance of SSoT tool configuration files (e.g., `.mdlrc`, `../commitlint.config.js`, formatter configs) in `gcs-core-governance/`.
- **`Camille` (Gem AB - Automation Specialist):**
  - Maintenance of the SSoT `.pre-commit-config.yaml` template.
  - Development and maintenance of SSoT for Gencraft-wide custom hook scripts.
  - Providing guidance on `pre-commit` framework usage and hook development.
- **Repository Maintainers / Technical Leads:**
  - Ensuring an appropriate `.pre-commit-config.yaml` (based on SSoT template) is implemented and
    maintained in their repositories.
  - Managing project-specific hook customizations and justifications.
- **All Gencraft Contributors (Gems and Humans):**
  - Installing and using `pre-commit` hooks in their local development environments for all relevant
    repositories.
  - Addressing issues flagged by hooks before committing.

## 5. Exceptions & Deviations

- Deviations from using the `pre-commit` framework, or disabling MANDATORY hooks defined in the SSoT
  template, require a formal exception.
- Exception requests MUST be documented in an Issue in `gcs-core-governance`, detailing the
  justification, scope, duration, and potential risks.
- Approval requires consensus from `Édouard` (Gem AD) and `Adam` (Gem AA). Significant deviations may
  require Governance Crew approval.
- Any approved deviation MUST be clearly documented in the `README.md` of the affected repository.

## 6. References & SSoTs

- `pre-commit` Framework Documentation: [https://pre-commit.com/](https://pre-commit.com/)
- `tool-001-conventional-commits-standard.md`
- `tool-003-code-style-and-formatting.md`
- `GCT-TOOL_MDLINT-V1` (Markdown Linter Tool)
- `../iac/iac-007-iac-static-analysis-standard.md`
- `../scripting/script-001-general-scripting-standard.md` (To Be Created by `Édouard`)
- **SSoT Locations for Configurations & Templates (To Be Created/Populated):**
  - `gcs-core-governance/linting/configs/.mdlrc` (by `Édouard`)
  - `../commitlint.config.js` (by `Édouard`)
  - `gcs-core-governance/formatting/configs/` (by `Édouard`)
  - `gcs-core-governance/security/sec_00x_secret_scanning_tool_standard.md` (by `Cerberus`/`Édouard`)
  - `configs/.pre-commit-config.yaml` (by `Camille`)
  - `gencraft-devops-automation/git-hooks/custom-hooks/` (by `Camille` as needed)

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
