---
docId: DEV-ARCH-003
title: "DEV-STAN-003 Historical Content (Archive)"
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
archive_date: "2026-06-08"
source_document: DEV-STAN-003
last_updated_date: '2026-06-08'
metadata:
  lifecycle-stage: archived
  security-classification: l2_confidential
  domain: devops
  scope: studio
  doc-type: archive
  keywords:
  - github-standards
  - devops
  - branching-strategy
  - github-flow
  - iac
  - operational-standards
  - archive

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/foundations/github/_archived/DEV-ARCH-003.gh-001-operational-standards-archive.md
---

> **Archived content.** These standards are no longer active requirements.
> Current standards: [DEV-STAN-014, DEV-STAN-015, DEV-STAN-016](../../../domains/cicd/standards/).

**DEPRECATION NOTICE:** The taxonomy and metadata rules previously defined in this document are now obsolete. The official and single source of truth for all studio-wide taxonomy, classification, and metadata rules is now defined in the standard `GOV-STANDARD-008: SSoT Master Taxonomy and Governance Standard`. Please refer to that document for all current definitions and to the `gcs.governance.yml` file for the raw vocabulary data.

## 1. Introduction

This document outlines the comprehensive operational standards for using GitHub within the <G@FT.ai>
Studio's organization (`GenCr-ft`). Adherence to these standards is crucial for maintaining consistency,
security, efficiency, and a high-quality Developer Experience (DevEx) across all projects.

These standards build upon:

- **ADR_0001: Multi-repo/Hybrid Strategy**
- **GFT-DEVOPS-STD-001: GitHub Repository Management via Infrastructure as Code**

All repository configurations, team permissions, and branch protections mandated by these standards are to
be implemented and managed via Infrastructure as Code (IaC) in the `GenCr-ft/gencraft-iac` repository,
unless explicitly stated otherwise.

## 2. Scope

These standards apply to all members of the <G@FT.ai> Studio interacting with the `GenCr-ft` GitHub
organization and its repositories. This includes, but is not limited to, code repositories, backlog
management repositories, documentation repositories, and foundational DevOps repositories.

## 3. Document Structure

This document is organized into the following sections:

- **Section 4: Branching Strategy & Protection Rules**
- **Section 5: Issue Management Standards**
- **Section 6: GitHub Team Structures & Permissions**
- **Section 7: Baseline CI/CD Workflow Definitions (Guidance for Gem B)**
- **Section 8: Repository & Organization Security Settings**
- **Section 9: Documentation of Standards (This Document)**
- **Section 10: Conventional Commits Standard** (Moved here for logical flow)
- **Section 11: Git Workflow Standard** (Moved here for logical flow)

## 4. Branching Strategy & Protection Rules

This section defines the standard branching strategy and the mandatory branch protection rules for
repositories within the `GenCr-ft` organization.

### 4.1. Default Branch Name

- All new repositories **MUST** use `main` as their default branch name. Existing repositories should be
  renamed if they use legacy names like `master`.

### 4.2. Core Branching Strategy: Gencraft Hybrid Flow (Default)

Per the **Governance Crew decision dated 2025-07-01**, the entire studio defaults to the **Gencraft Hybrid
Flow** defined in DEV-STAN-001. The key elements are:

- `main` represents the latest production-ready, tagged release and is heavily protected.
- `develop` is the integration branch for the next release. All `feature/*` and `bugfix/*` branches merge
  into `develop` through reviewed Pull Requests.
- `release/vX.Y.Z` branches are used to stabilize a candidate build before shipping, then merge into `main`
  and back into `develop`.
- `hotfix/vX.Y.Z-*` branches are created from the affected release tag on `main` to address urgent
  production issues. They merge into `main`, `develop`, and any active `release/*` branches.
- Branch naming, commit standards, PR reviews, and protections mirror DEV-STAN-001 Sections 4-7.

This hybrid model balances continuous integration with structured releases, and is the assumed workflow for
all repositories unless a documented tier exception applies.

### 4.3. Tier-Based Exceptions and GitHub Flow Usage

To reduce overhead on lower-risk repositories, governance recognizes the following tiers:

- **Tier 1 (Default):** Implements the full hybrid strategy described above. Applies to all repositories by
  default, especially game codebases, IaC, shared tooling, and automation.
- **Tier 2 (Simplified Hybrid):** When approved, teams may omit `release/*` branches and merge releases
  directly from `develop` to `main`. A tag on `main` is still required and hotfixes must be backported to
  `develop`. The tier designation and approval reference MUST live in the repository `README`.
- **Tier 3 (GitHub Flow Exception):** Extremely low-risk or generated repositories MAY operate with GitHub
  Flow (`main` + short-lived topic branches) if approved via ADR or governance ticket. Branch protection,
  naming, commit, and review requirements remain mandatory. Tier 3 repos revalidate the exception at least
  quarterly with Governance.

Repositories not explicitly listed as Tier 2 or Tier 3 are assumed to be Tier 1.

### 4.4. Release Branches (for applicable repositories)

For repositories that have distinct release cycles (e.g., `gcp-aethel-client`, `gcp-aethel-server-core`),
`release/vX.Y.Z` branches _must_ be used under the hybrid default and _may_ be optional for Tier 2. When
employed:

- `release/vX.Y.Z` branches are created from `develop` once the backlog for that version is feature-complete.
- The branch is used for final testing, bug fixing, and release preparation (e.g., version bumping,
  changelog generation, localization updates).
- Only release-critical bug fixes are merged into a release branch (these must also be merged back into
  `develop`).
- Once the release is ready, the branch merges into `main`, the version tag is applied to `main`, and the
  branch is merged back into `develop`.
- Strict access controls apply to release branches and should mirror the protection rules for `main` and
  `develop`.

### 4.5. Branch Naming Conventions

- **Feature/Topic Branches:** Use a descriptive, hyphenated name, optionally prefixed with issue number or type:
  - `feat/add-new-auth-endpoint`
  - `fix/resolve-login-bug-123`
  - `chore/update-readme`
  - `refactor/optimize-rendering-pipeline`
  - `doc/add-api-contract-guide`
  - `[USER_STORY_ID]/short-description` (e.g., `US-123/implement-voxel-placement`)
- **Release Branches:** `release/vX.Y.Z` (e.g., `release/v0.1.0`)

### 4.6. Mandatory Branch Protection Rules (to be enforced via IaC)

Branch protection rules **MUST** be configured for the `main` branch (and any `release/*` branches) in all
repositories via IaC (`GenCr-ft/gencraft-iac`). The following baseline requirements apply, **subject to
the limitations of the organization's current GitHub plan (assumed Free plan for private repositories)**.
Features marked with `[Paid Plan Required]` are only enforceable on private repositories if the
organization uses GitHub Pro, Team, or Enterprise.

The IaC code (`github_branch_protection` resources) **MUST** only implement settings compatible with the
current GitHub plan to avoid API errors.

**4.6.1. Common Rules for `main` branch across ALL Repository Types (Reflecting Free Plan limitations for Private Repos):**

- **Require a pull request before merging:** `true` (Available on Free plan)
  - **Dismiss stale pull request approvals when new commits are pushed:** `true` (Available on Free plan)
  - **Require review from Code Owners:** `true` **[Paid Plan Required for private repos]**
    _(Note: Cannot be enforced via IaC on private repos under the Free plan. Define CODEOWNERS for
    documentation and use manual processes or team conventions to encourage review by owners.)_
- **Require status checks to pass before merging:** `true` (Available on Free plan)
  - At least one status check (e.g., primary CI workflow) **MUST** be configured and required.
- **Require conversation resolution before merging:** `true` (Available on Free plan)
- **Require signed commits:** `false` (Available on Free plan, but not mandated by default)
- **Require linear history:** `false` (Available on Free plan, but not mandated by default; Squash & Merge
  preferred - see Section 11.3)
- **Restrict who can push to matching branches:** `true` (Basic restriction available on Free plan -
  prevent direct pushes for non-admins).
  _(Note: Fine-grained restrictions based on specific users or teams often require a paid plan.)_
- **Allow force pushes:** `false` (Available on Free plan - MANDATORY setting)
- **Allow deletions:** `false` (Available on Free plan - MANDATORY setting)

**4.6.2. Specific Rules by Repository Type (for `main` branch - Adapted for Free Plan on Private Repos):**

-(This table clarifies expected minimums enforceable via IaC on Free Plan)-

| Repository Type (`GenCr-ft/...`)                   | Min. Required Approving Reviews (Enforceable) | Required Status Checks (Examples)                  | Code Owner Reviews (Enforceable via IaC) | Notes                                                                                                                      |
| :------------------------------------------------- | :-------------------------------------------- | :------------------------------------------------- | :--------------------------------------- | :------------------------------------------------------------------------------------------------------------------------- |
| **`gencraft-backlog`**                             | 1                                             | (Optional: Issue Lint/Validation)                  | `No (Plan Limitation)`                   | Enforce PRs, 1 approval, conversation resolution.                                                                          |
| **`gcp-aethel-client`**                            | 1                                             | `CI Checks (Lint, Format, Test, Build, Vuln Scan)` | `No (Plan Limitation)`                   | Enforce PRs, 1 approval, CI checks. Code Owner review is a **manual team convention**.                                     |
| **`gcp-aethel-server-core`**                       | 1                                             | `CI Checks (Lint, Format, Test, Build, Vuln Scan)` | `No (Plan Limitation)`                   | Enforce PRs, 1 approval, CI checks. Code Owner review is a **manual team convention**.                                     |
| ... _(Adjust other code repo types similarly)_ ... | 1                                             | `Relevant CI Checks`                               | `No (Plan Limitation)`                   | Enforce PRs, 1 approval, CI checks. Code Owner review is a **manual team convention**.                                     |
| **`gencraft-iac`**                                 | 1                                             | `Format`, `Validate`, `Security Scan`              | `No (Plan Limitation)`                   | Enforce PRs, 1 approval, CI checks. **Team Convention:** Requires manual review from >=1 other DevOps member before merge. |
| **`gcs-core-governance`**                         | 1                                             | (Optional: Markdown Lint)                          | `No (Plan Limitation)`                   | Enforce PRs, 1 approval.                                                                                                   |

**4.6.3. Specific Rules by Repository Type (for `main` branch):**

| Repository Type                           | Min. Required Approving Reviews   | Required Status Checks (Examples)                                                                                                | Notes                                                                                                                             |
| :---------------------------------------- | :-------------------------------- | :------------------------------------------------------------------------------------------------------------------------------- | :-------------------------------------------------------------------------------------------------------------------------------- |
| **`gencraft-backlog`**                    | 1 (e.g., Product Manager)         | `Lint Issue Content` (if automated), `Validate Project Structure` (if applicable)                                                | Primarily for issue/project management. PRs may be less frequent unless config (labels, milestones via GitOps) is managed here.   |
| **`gcp-aethel-client`** (TS)              | 1-2 (e.g., Lead Dev, Peer)        | `Lint & Format`, `Unit Tests`, `Integration Tests`, `Build`, `Security Audit (npm/pnpm audit)`                                   | Consider 2 reviews for critical path changes.                                                                                     |
| **`gcp-aethel-server-core`** (C#/Go/Rust) | 1-2 (e.g., Lead Dev, Peer)        | `Lint & Format`, `Unit Tests`, `Integration Tests`, `Build`, `Security Audit (dotnet vulnerable, govulncheck, cargo audit)`      | Consider 2 reviews for critical path changes.                                                                                     |
| **`gcp-aethel-server-pcg`** (Python)      | 1-2 (e.g., Lead Dev, PCG Spec.)   | `Lint & Format`, `Unit Tests`, `Integration Tests`, `Type Check (mypy)`, `Security Audit (pip-audit)`                            | Designers (Level/PCG) with write access for config might require lighter review process for specific config files via CODEOWNERS. |
| **`gencraft-service-*`** (Polyglot)       | 1-2 (e.g., Lead Dev, Peer)        | Similar to Server/Client based on language: `Lint & Format`, `Unit Tests`, `Integration Tests`, `Build`, `Security Audit`        | Consider 2 reviews for core services.                                                                                             |
| **`gencraft-api-contracts`**              | 2 (e.g., Architect, Lead Dev)     | `Schema Validation (OpenAPI lint)`, `Breaking Change Detection`, (Optional: `SDK Generation Test`)                               | Critical repository. Strict change control.                                                                                       |
| **`gencraft-iac`**                        | 2 (DevOps Lead, another DevOps)   | `Terraform/OpenTofu Format`, `Terraform/OpenTofu Validate`, `Security Scan (tfsec/checkov)`, `Plan Output Verification (manual)` | Critical for infrastructure and org management.                                                                                   |
| **`gcd-shared-actions`**                  | 1-2 (DevOps Lead, another DevOps) | `Lint Scripts/Workflows`, `Workflow Validation`, `Security Scan`                                                                 | Reusable GitHub Actions (successor to `gencraft-devops-automation`).                                                              |
| **`gcd-ops-scripts`**                    | 1-2 (DevOps Lead, another DevOps) | `Lint Scripts`, `Security Scan`                                                                                                  | Operational automation scripts (successor to `gencraft-devops-automation`).                                                       |
| **`gencraft-documentation`**              | 1 (e.g., relevant SME, PM)        | `Markdown Lint`, `Link Checker`                                                                                                  |                                                                                                                                   |
| **`gencraft-build-tools`**                | 1-2 (DevOps team)                 | `Dockerfile Lint`, `Security Scan (image)`                                                                                       | For shared CI build images.                                                                                                       |
| **`.github` (Org-Level)**                 | 2 (DevOps Lead, PM/Producer)      | `Lint Templates/Workflows`                                                                                                       | For org-wide templates and settings.                                                                                              |

### 4.7 Standard Repository Files

To ensure consistency and provide essential information, repositories within the `GenCr-ft` organization
should include the following standard files where applicable:

- **`README.md` (Mandatory):**
  - Must exist at the root of every repository.
  - Should clearly explain the repository's purpose, how to set it up (if applicable), how to
    contribute, and link to relevant documentation or standards.
  - Content standards for READMEs may be further defined in project documentation guidelines.
- **`.gitignore` (Mandatory for code/tooling repositories):**
  - Must be present to exclude unnecessary files (build artifacts, logs, local configurations, IDE
    files) from version control.
  - Use standard templates appropriate for the repository's language/technology (e.g., from [github/gitignore](https://github.com/github/gitignore)).
- **`../../gcp-aethel-architecture/license` (Mandatory):**
  - Must exist at the root of every repository containing code or creative works.
  - **Action Required:** The specific license file and its content MUST be provided or approved by G@FT.
    ai's Legal Counsel (Gem HH). A placeholder note or a default approved license (pending legal
    confirmation) should be used initially.
- **`CONTRIBUTING.md` (Recommended):**
  - Recommended for repositories expecting contributions (especially code, IaC, documentation).
  - Should outline the contribution process, setup steps, coding standards (or link to them), and
    expectations for Pull Requests, referencing these Operational Standards.
- **`../../gcs-core-governance/00-studio-vision-and-principles/code-of-conduct.md` (Recommended):**
  - Recommended for all repositories to foster an open and welcoming environment.
  - A standard template (e.g., Contributor Covenant) should be adopted studio-wide and placed in
    repositories.
- **`.editorconfig` (Mandatory):**
  - Must exist at the root of repositories containing text files (code, markdown, config) to help
    maintain consistent coding styles (indentation, line endings, etc.) across different editors and IDEs.
  - A standard <G@FT.ai> `.editorconfig` file will be provided and should be used. It should be managed
    via IaC for relevant repository types or included in repository templates.

These files, particularly `.gitignore`, `../../gcp-aethel-architecture/license`, and `.editorconfig`,
should ideally be included when repositories are bootstrapped or provisioned via IaC where
feasible, using centrally approved templates or content

---

## 5. Issue Management Standards

Effective issue management is crucial for project tracking, collaboration, and transparency. These
standards apply primarily to the `GenCr-ft/gencraft-backlog` repository for product backlog management,
but the principles (especially labels and linking) should also be adopted for managing technical tasks,
bugs, and improvements within code repositories. All label and issue template configurations discussed
here are intended to be managed via IaC (`GenCr-ft/gencraft-iac`) where feasible.

### 5.1. General Principles

- **Clarity and Conciseness:** Issue titles should be clear and concise. Descriptions should provide all
  necessary context.
- **Atomicity (where applicable):** User Stories and Tasks should be small enough to be completed within
  a reasonable timeframe (e.g., a single sprint or part of a sprint).
- **Actionability:** Issues should represent actionable work or clearly defined problems.
- **Assignment:** All active issues (e.g., `status:in-progress`, `status:in-review/qa`) should be
  assigned to a responsible individual or team.
- **Updates:** Issues should be kept up-to-date with progress, comments, and status changes.
- **Linking:** Related issues, PRs, Epics, and Features should be linked using GitHub's referencing
  capabilities (e.g., `Fixes #123`, `Related to EPIC-CORE-PLAYER`).

### 5.2. Standard GitHub Labels

A consistent set of labels helps categorize, prioritize, and filter issues. Labels **MUST** be created
and managed via IaC (`GenCr-ft/gencraft-iac` using the `github_label` resource) to ensure consistency
across repositories, especially `GenCr-ft/gencraft-backlog`.

**Note:** The exact color codes are suggestions; ensure they provide good visual contrast and are
consistent. The Producer/PM (Management Gem A) should review and finalize the color palette based on the
"GitHub Configuration V1 Révisée" and accessibility considerations.

#### **5.2.1. Issue Type Labels (`type:*`)**

| Label Name            | Color     | Description                                                                                                                                                                              |
| :-------------------- | :-------- | :--------------------------------------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `type:epic`           | `#1D76DB` | A large body of work that can be broken down into multiple features or user stories. (Corresponds to `../../gcp-aethel-docs-req/99-project-resources/templates/epic-template.md`)        |
| `type:feature`        | `#74B5F9` | A distinct piece of functionality that delivers value to the user. (Corresponds to `../../gcp-aethel-docs-req/99-project-resources/templates/feature-template.md`)                       |
| `type:user-story`     | `#A2D1F5` | A small, self-contained unit of work from the user's perspective. (Corresponds to `../../gcs-core-governance/02-knowledge-base-hub/templates/document-templates/user-story-template.md`) |
| `type:task`           | `#FAD8C7` | A specific technical or operational piece of work, often part of a user story or feature.                                                                                                |
| `type:bug`            | `#D93F0B` | An error or flaw in the system that causes incorrect or unexpected results.                                                                                                              |
| `type:chore`          | `#F2DA78` | Maintenance, refactoring, or other tasks that don't directly add user-facing features but improve the system.                                                                            |
| `type:improvement`    | `#F9D0C4` | An enhancement to an existing feature or process.                                                                                                                                        |
| `type:documentation`  | `#C2E0C6` | Tasks related to writing or updating documentation.                                                                                                                                      |
| `type:question`       | `#D4C5F9` | A question that needs an answer or clarification before work can proceed.                                                                                                                |
| `type:security`       | `#B60205` | A security vulnerability or concern that needs to be addressed.                                                                                                                          |
| `type:technical-debt` | `#BFDADC` | Identifies work related to addressing known technical debt.                                                                                                                              |
| `type:spike`          | `#E3D8F2` | A time-boxed investigation or research task to understand a problem or solution better.                                                                                                  |

#### **5.2.2. Issue Status Labels (`status:*`)**

| Label Name                  | Color     | Description                                                                                                      |
| :-------------------------- | :-------- | :--------------------------------------------------------------------------------------------------------------- |
| `status:backlog/icebox`     | `#CCCCCC` | Item is in the backlog, not yet prioritized for active development.                                              |
| `status:todo/ready-for-dev` | `#F29513` | Item is prioritized, clearly defined, and ready to be picked up for development.                                 |
| `status:in-progress`        | `#F9D0C4` | Item is actively being worked on.                                                                                |
| `status:blocked`            | `#000000` | Work on this item is blocked by an external dependency or another issue. (Ensure reason for block is commented). |
| `status:in-review/pr`       | `#A2EEEF` | Work is complete, and a Pull Request has been opened for review.                                                 |
| `status:in-qa`              | `#C5DEF5` | Item has passed code review and is ready for or currently undergoing QA testing.                                 |
| `status:done/closed`        | `#0E8A16` | Item is completed, tested, merged, and/or resolved.                                                              |
| `status:wont-fix/invalid`   | `#FFFFFF` | Item will not be fixed, or was reported in error (often used with `status:done/closed`).                         |

#### **5.2.3. Priority Labels (`priority:*`)**

| Label Name          | Color     | Description                                                                        |
| :------------------ | :-------- | :--------------------------------------------------------------------------------- |
| `priority:critical` | `#D93F0B` | Must be addressed immediately; blocks further progress or has severe user impact.  |
| `priority:high`     | `#F29513` | Important to address soon; significant user impact or blocks other important work. |
| `priority:medium`   | `#FBCA04` | Should be addressed in due course; moderate user impact. Default priority.         |
| `priority:low`      | `#0E8A16` | Nice to have; minor user impact or can be deferred.                                |

#### **5.2.4. Team/Component/Area Labels (`team:*`, `area:*`, `component:*`)**

_(This category is highly project-specific. The Producer/PM should define the exact list based on team
structure and project components. Examples provided below.)_

| Label Name                 | Color     | Description                                         |
| :------------------------- | :-------- | :-------------------------------------------------- |
| `team:client-dev`          | `#BFD4F2` | Related to the client development team.             |
| `team:server-dev`          | `#D4C5F9` | Related to the server development team.             |
| `team:pcg-dev`             | `#F2DA78` | Related to the PCG development team.                |
| `team:services-dev`        | `#DBF2E3` | Related to backend microservices development.       |
| `team:ux-ui-design`        | `#FAD8C7` | Requires input from or relates to UX/UI design.     |
| `team:qa`                  | `#A2D1F5` | Related to the QA team or testing activities.       |
| `team:devops`              | `#E3D8F2` | Related to DevOps tasks or infrastructure.          |
| `component:authentication` | `#F9D0C4` | Pertains to the authentication service or features. |
| `component:voxel-engine`   | `#C2E0C6` | Pertains to the core voxel engine.                  |

#### **5.2.5. Other Useful Labels**

| Label Name            | Color     | Description                                                                                      |
| :-------------------- | :-------- | :----------------------------------------------------------------------------------------------- |
| `good first issue`    | `#7057FF` | Suitable for new contributors to the project.                                                    |
| `help wanted`         | `#008672` | Seeking help from the community or other team members.                                           |
| `needs:clarification` | `#B60205` | More information or clarification is needed before work can proceed.                             |
| `needs:design`        | `#F9D0C4` | Requires input or review from the design team (UX/UI, Game Design).                              |
| `needs:architecture`  | `#D4C5F9` | Requires input or review from the Software Architect.                                            |
| `sprint:Sprint X`     | `#CCCCCC` | (If using Sprints) Links issue to a specific Sprint. Create one label per Sprint.                |
| `epic:[EPIC_NAME]`    | `#1D76DB` | Links features/stories to a parent Epic. (e.g. `epic:PLAYER-CORE`). Create one per Epic defined. |
| `release:vX.Y.Z`      | `#BFDADC` | Links issue to a specific release version.                                                       |

### 5.3. Standard GitHub Issue Templates

Standardized Issue Templates ensure that all necessary information is provided when creating new issues,
improving clarity and reducing back-and-forth.

**Recommendation:** Implement these using **GitHub Issue Forms (YAML format)** as they provide a more
structured input experience. The Markdown content provided below (based on templates from
`gcp-aethel-docs-req/99-project-resources/Templates/`) should be translated into the YAML form structure.

These template files (YAML) **MUST** be stored in the `.github/ISSUE_TEMPLATE/` directory of the
`GenCr-ft/gencraft-backlog` repository. Their creation and updates should be managed via IaC (`GenCr-ft/
gencraft-iac` using the `github_repository_file` resource), ensuring consistency. The source for these
YAML forms will be new files created within `gencraft-iac` (e.g., in `gencraft-iac/environments/
github-org/issue_templates/gencraft-backlog/`).

#### **5.3.1. Bug Report (`bug_report.yml`)**

```yaml
name: "\U0001F41B Bug Report"
description: "Report a bug or issue encountered in the G@FT.ai project."
title: "[BUG] Brief description of bug"
labels: ["type:bug", "priority:medium", "status:todo/ready-for-dev"]
body:
  - type: markdown
    attributes:
      value: "Thank you for taking the time to fill out this bug report! Please provide as much detail as possible."
  - type: textarea
    id: description
    attributes:
      label: "Description of the Bug"
      description: "A clear and concise description of what the bug is."
      placeholder: "e.g., Player character falls through the world when..."
    validations:
      required: true
  - type: textarea
    id: steps-to-reproduce
    attributes:
      label: "Steps to Reproduce"
      description: "Detail the exact steps to reproduce the behavior."
      placeholder: |
        1. Go to '...'
        2. Click on '....'
        3. Scroll down to '....'
        4. See error
    validations:
      required: true
  - type: textarea
    id: expected-behavior
    attributes:
      label: "Expected Behavior"
      description: "A clear and concise description of what you expected to happen."
    validations:
      required: true
  - type: textarea
    id: actual-behavior
    attributes:
      label: "Actual Behavior"
      description: "A clear and concise description of what actually happened."
    validations:
      required: true
  - type: input
    id: game-version
    attributes:
      label: "Game Version / Environment"
      description: "Specify the version of the game, client, server, or environment where the bug occurred."
      placeholder: "e.g., Client v0.1.2, Development Server"
    validations:
      required: false
  - type: textarea
    id: logs-screenshots
    attributes:
      label: "Screenshots, Logs, or Other Context"
      description: "If applicable, add screenshots, logs, or any other context to help explain your problem. Drag & drop files here."
    validations:
      required: false
  - type: dropdown
    id: severity
    attributes:
      label: "Severity (Optional)"
      description: "How critical is this bug?"
      options:
        - "Critical (Blocks core functionality, major data loss)"
        - "High (Impairs core functionality, no workaround)"
        - "Medium (Impairs non-core functionality, or core with workaround)"
        - "Low (Minor issue, cosmetic, or low impact)"
    validations:
      required: false
  - type: dropdown
    id: affected-area
    attributes:
      label: "Affected Area/Component (Optional)"
      description: "Which part of the game or system is affected?"
      options: # This list should be populated with relevant components from your project
        - "Client UI"
        - "Gameplay - Voxel Interaction"
        - "Gameplay - Combat"
        - "Server - Authentication"
        - "PCG - World Generation"
        - "Other (Please specify in description)"
    validations:
      required: false
```

#### **5.3.2. Feature Request (`feature_request.yml`)**

_(Based on `../../gcp-aethel-docs-req/99-project-resources/templates/feature-template.md` principles)_

```yaml
name: "\U0001F680 Feature Request"
description: "Suggest an idea or new feature for the G@FT.ai project."
title: "[FEAT] Brief description of feature"
labels: ["type:feature", "priority:medium", "status:backlog/icebox"]
body:
  - type: markdown
    attributes:
      value: "Thanks for suggesting an idea! Please provide details to help us understand your proposal."
  - type: textarea
    id: problem-description
    attributes:
      label: "Problem Description / User Need"
      description: "Is your feature request related to a problem? Please describe. What user need does this address?"
      placeholder: "e.g., As a player, I find it difficult to..."
    validations:
      required: true
  - type: textarea
    id: proposed-solution
    attributes:
      label: "Proposed Solution / Feature Description"
      description: "A clear and concise description of what you want to happen. How would this feature work?"
    validations:
      required: true
  - type: textarea
    id: acceptance-criteria
    attributes:
      label: "Acceptance Criteria (Optional)"
      description: "How will we know this feature is complete and working correctly? (Use Gherkin format if possible: Given/When/Then)"
      placeholder: |
        - Given [context], when [action], then [outcome].
        - ...
    validations:
      required: false
  - type: textarea
    id: alternatives-considered
    attributes:
      label: "Alternatives Considered (Optional)"
      description: "Have you considered any alternative solutions or features?"
    validations:
      required: false
  - type: textarea
    id: user-value-impact
    attributes:
      label: "User Value / Business Impact (Optional)"
      description: "What is the value to the user or the business if this feature is implemented?"
    validations:
      required: false
  - type: dropdown
    id: target-audience
    attributes:
      label: "Target Audience (Optional)"
      description: "Which user personas would benefit most from this feature?"
      options: # Populate with your defined personas e.g., from gcp-aethel-docs-req/02_Target_Audience/personas/
        - "P_ARC (Architect Player)"
        - "P_EXP (Explorer Player)"
        - "P_SOC (Social Player)"
        - "P_MOD (Modder/Creator)"
        - "All Players"
    validations:
      required: false
```

#### **5.3.3. User Story (`user_story.yml`)**

(Based on `../../gcs-core-governance/02-knowledge-base-hub/templates/document-templates/user-story-template.md` principles)

```yaml
name: "\U0001F464 User Story"
description: "Define a user-centric requirement for the G@FT.ai project."
title: "[US] Brief description of user story" # e.g., [US-ID] As a [Role], I want [Goal], so that [Reason]
labels: ["type:user-story", "priority:medium", "status:todo/ready-for-dev"]
body:
  - type: input
    id: user-story-title
    attributes:
      label: "User Story Statement"
      description: "Follow the format: As a [type of user], I want [an action] so that [a benefit/value]."
      placeholder: "As a Player, I want to place voxels precisely, so that I can build detailed structures."
    validations:
      required: true
  - type: textarea
    id: acceptance-criteria
    attributes:
      label: "Acceptance Criteria"
      description: "Define clear, testable acceptance criteria. Use Gherkin format (Given/When/Then) where possible. Each criterion should be on a new line starting with '-'."
      placeholder: |
        - Given the player has selected a voxel type from their inventory
        - When the player targets a valid surface and clicks the primary action button
        - Then the selected voxel is placed at the targeted location
        - And one unit of the voxel is consumed from the player's inventory
    validations:
      required: true
  - type: textarea
    id: tasks-breakdown
    attributes:
      label: "Technical Tasks / Implementation Notes (Optional)"
      description: "List any known technical tasks or implementation details needed to complete this story. These can be created as separate `type:task` issues and linked."
      placeholder: |
        - Implement voxel placement logic in client.
        - Validate placement on server.
        - Update inventory service.
    validations:
      required: false
  - type: input
    id: epic-link
    attributes:
      label: "Parent Epic (Optional)"
      description: "Link to the parent Epic issue (e.g., #EPIC-ID or `epic:EPIC-NAME` label)."
      placeholder: "e.g., #12 or epic:PLAYER-CORE"
    validations:
      required: false
  - type: input
    id: feature-link
    attributes:
      label: "Parent Feature (Optional)"
      description: "Link to the parent Feature issue (e.g., #FEATURE-ID)."
      placeholder: "e.g., #34"
    validations:
      required: false
  - type: dropdown
    id: story-points
    attributes:
      label: "Story Points (Optional - if using)"
      description: "Estimate the effort using Story Points (e.g., Fibonacci sequence)."
      options:
        - "1"
        - "2"
        - "3"
        - "5"
        - "8"
        - "13"
        - "?" # For items needing more discussion before estimation
    validations:
      required: false
```

#### **5.3.4. Technical Task (`technical_task.yml`)**

```yaml
name: "\U0001F527 Technical Task"
description: "Define a specific technical task or chore."
title: "[TASK] Brief description of task"
labels: ["type:task", "priority:medium", "status:todo/ready-for-dev"]
body:
  - type: textarea
    id: description
    attributes:
      label: "Task Description"
      description: "A clear and concise description of the technical task to be performed."
    validations:
      required: true
  - type: textarea
    id: technical-details
    attributes:
      label: "Technical Details / Proposed Approach (Optional)"
      description: "Provide any relevant technical details, proposed implementation approach, or considerations."
    validations:
      required: false
  - type: textarea
    id: acceptance-criteria
    attributes:
      label: "Acceptance Criteria / Definition of Done"
      description: "How will we know this task is complete?"
      placeholder: |
        - Code implemented as per technical details.
        - Unit tests written and passing (if applicable).
        - Documentation updated (if applicable).
        - PR reviewed and merged.
    validations:
      required: true
  - type: input
    id: parent-link
    attributes:
      label: "Parent User Story / Feature / Epic (Optional)"
      description: "Link to the parent item this task supports (e.g., #US-ID, #FEAT-ID)."
      placeholder: "e.g., #123"
    validations:
      required: false
  - type: dropdown
    id: assigned-team-component
    attributes:
      label: "Primary Team/Component (Optional)"
      description: "Which team or component is primarily responsible or most affected by this task?"
      options: # Populate with relevant team/component labels from section 5.2.4
        - "team:client-dev"
        - "team:server-dev"
        - "team:pcg-dev"
        - "team:services-dev"
        - "team:devops"
        - "component:authentication"
        - "component:voxel-engine"
    validations:
      required: false
```

#### \*5.3.5. Epic Definition (`epic_definition.yml`)\*\*

(Based on `gcp-aethel-docs-req/99-project-resources/Templates/EPIC_Template.md principles`. Epics are
high-level; this template helps define them as issues for tracking.)

```yaml
name: "\U0001F3AF Epic Definition"
description: "Define a new Epic for the G@FT.ai project."
title: "[EPIC] Name of the Epic"
labels: ["type:epic", "status:backlog/icebox"] # Default status
body:
  - type: markdown
    attributes:
      value: "Use this template to define a new Epic. Epics represent large bodies of work."
  - type: textarea
    id: epic-description
    attributes:
      label: "Epic Description & Goals"
      description: "Provide a high-level description of the Epic and its main objectives or user problems it solves."
    validations:
      required: true
  - type: textarea
    id: scope-key-features
    attributes:
      label: "Scope / Key Features (Optional)"
      description: "Outline the key features or user stories that might fall under this Epic. This can be high-level."
      placeholder: |
        - Feature 1: ...
        - User Story Group A: ...
    validations:
      required: false
  - type: textarea
    id: success-metrics
    attributes:
      label: "Success Metrics / Business Value (Optional)"
      description: "How will we measure the success of this Epic? What is its business value?"
    validations:
      required: false
  - type: input
    id: target-release
    attributes:
      label: "Target Release / Milestone (Optional)"
      description: "Is this Epic targeted for a specific release or milestone (e.g., MVP, MVP+1)?"
      placeholder: "e.g., MVP, MVP+1"
    validations:
      required: false
  - type: dropdown
    id: epic-owner
    attributes:
      label: "Epic Owner/Champion (Optional)"
      description: "Who is the primary point of contact or champion for this Epic (e.g., Product Manager, Lead Designer)?"
      options: # Should be populated by relevant leads/roles
        - "Product Manager (Dept 01)"
        - "Game Designer (Dept 03)"
        - "Software Architect (Dept 04)"
    validations:
      required: false
```

#### **\*5.3.6. Action Item (`action_item.yml`)**

(Based on `../../gcp-aethel-docs-req/99-project-resources/templates/action-item-template.md`
principles. Useful for tracking follow-up tasks from meetings or discussions.)

```yaml
name: "\U0001F4DD Action Item"
description: "Track a specific action item or follow-up task."
title: "[ACTION] Brief description of action item"
labels: ["type:task", "status:todo/ready-for-dev"] # Often a task, but can be adjusted
body:
  - type: textarea
    id: action-description
    attributes:
      label: "Action Item Description"
      description: "Clearly describe the action to be taken."
    validations:
      required: true
  - type: input
    id: assigned-to
    attributes:
      label: "Assigned To (GitHub Username or Team)"
      description: "Who is responsible for this action item?"
      placeholder: "@username or @G-FT-ai/team-name"
    validations:
      required: true # Actions should always have an owner
  - type: input
    id: due-date
    attributes:
      label: "Due Date (Optional)"
      description: "When should this action item be completed? (YYYY-MM-DD)"
      placeholder: "YYYY-MM-DD"
    validations:
      required: false
  - type: textarea
    id: context-source
    attributes:
      label: "Context / Source (Optional)"
      description: "Where did this action item originate from? (e.g., link to meeting notes, discussion, related issue)."
    validations:
      required: false
  - type: checkboxes
    id: definition-of-done
    attributes:
      label: "Definition of Done (Optional)"
      description: "What needs to be true for this action to be considered complete?"
      options:
        - label: "Required actions performed."
        - label: "Relevant parties informed."
        - label: "Documentation updated (if any)."
```

### 5.4. Milestones

- Milestones in `GenCr-ft/gencraft-backlog` **MUST** be used to track progress towards significant goals,
  releases, or sprint cycles.
- Examples: `MVP Release`, `Sprint 1 (YYYY-MM-DD to YYYY-MM-DD)`, `Alpha Tech Demo`, `Q3-2025 Goals`.
- Each Milestone **MUST** have a clear due date (if applicable) and a description of its objectives.
- Milestones **MUST** be created and managed via IaC (`GenCr-ft/gencraft-iac` using the
  `github_milestone` resource).
- The Producer/PM (Management Gem A) is responsible for defining and updating Milestones in alignment
  with the project roadmap and sprint planning.

### 5.5. Project Boards (GitHub Projects - New Version)

- GitHub Projects (new version) are the recommended tool for visualizing workflows (e.g., Kanban boards
  for Sprints, roadmap visualization, feature tracking).
- **IaC Approach:**
  - The **existence** of core project boards (e.g., "<G@FT.ai> - Main Product Backlog Board," "Current
    Sprint Task Board") **SHOULD** be managed via IaC (`github_organization_project` or
    `github_repository_project` in `gencraft-iac`). This ensures the project board itself is version controlled.
  - The **detailed internal configuration** of these boards (columns/views, custom fields, automation
    rules) will **initially be managed manually** through the GitHub UI by the Producer/PM or relevant team
    leads. This configuration should be documented (e.g., in the project board's description or a linked
    document within the `GenCr-ft/devops-standards` repository).
  - Full IaC management of board internals (views, fields, items) will be revisited as Terraform provider
    support matures and if a critical need for automation arises.
- The Producer/PM (Management Gem A) is responsible for the setup and maintenance of the project board
  views and workflows, based on the "GitHub Configuration V1 Révisée" for `GenCr-ft/gencraft-backlog` and
  overall project needs. Standard column names for a Kanban-style board could include: `Backlog`, `To Do /
Ready for Dev`, `In Progress`, `In Review / PR`, `In QA`, `Done`.

## 6. GitHub Team Structures & Permissions

A clear team structure with appropriate permissions is essential for security and efficient
collaboration. All GitHub Teams and their repository permissions **MUST** be managed via IaC in the
`GenCr-ft/gencraft-iac` repository using resources like `github_team` and `github_team_repository`. This
ensures the Principle of Least Privilege is applied consistently.

### 6.1. Core GitHub Teams

The following core GitHub Teams should be created, mapping to <G@FT.ai> Studio departments/roles.
Additional project-specific or feature-focused teams can be created as needed following the same IaC
process. Team names should use a consistent prefix (e.g., `gft-`) for clarity. Team membership should
ideally be managed via IaC as well, or via a central identity provider if implemented in the future.

| Proposed GitHub Team Name    | Corresponding <G@FT.ai> Roles/Departments                                                          | Purpose                                                                       |
| :--------------------------- | :------------------------------------------------------------------------------------------------- | :---------------------------------------------------------------------------- |
| `gft-all-members`            | All studio personnel (every Gem)                                                                   | General read access, ability to create issues in specific repos.              |
| `gft-devops-team`            | DevOps Team (AA, BB, CC, EE/D)                                                                     | Administer DevOps tools, IaC, CI/CD, org settings.                            |
| `gft-architects`             | Software Architect (I), potentially Art Director (P) for art architecture.                         | Define & oversee technical/artistic architecture, review critical changes.    |
| `gft-product-management`     | Product Manager, Producer/PM (Dept 01)                                                             | Manage product backlog, roadmap, requirements, project boards.                |
| `gft-programming-leads`      | Lead Developer/Tech Lead (J)                                                                       | Technical leadership for programming, code reviews, maintain repo quality.    |
| `gft-developers-client`      | UI Developer (Game), Rendering Engine Dev, Gameplay Prog (client-focused)                          | Develop and maintain client-side code.                                        |
| `gft-developers-server-core` | Network/Backend Prog, Gameplay Prog (server-focused), PCG Specialist (if server stack)             | Develop and maintain core game server logic.                                  |
| `gft-developers-server-pcg`  | PCG Specialist, relevant programmers (if separate stack/repo for PCG)                              | Develop and maintain PCG systems.                                             |
| `gft-developers-services`    | Network/Backend Prog (for general backend services)                                                | Develop and maintain backend microservices.                                   |
| `gft-artists-technical`      | Technical Artist (R)                                                                               | Manage art pipeline, tools, shaders, assist with client-side art integration. |
| `gft-artists-production`     | Lead Artist (Q), Env Artist (T), Char Artist (U), Animator (V), VFX Artist (W), Concept Artist (S) | Create and manage art assets.                                                 |
| `gft-designers-game`         | Game Designer (E)                                                                                  | Define game mechanics, systems, and rules.                                    |
| `gft-designers-level-pcg`    | Level Designer (Procedural) (F), Narrative Designer (Procedural Focus) (G)                         | Design and tune procedural generation for levels and narrative.               |
| `gft-designers-ux-ui`        | UX/UI Designer (H)                                                                                 | Design user experience and interfaces.                                        |
| `gft-qa-team`                | QA Engineer/Test Lead (Z), potentially other QA specialists                                        | Define & execute test strategy, manage bug reports, ensure quality.           |
| `gft-audio-team`             | Sound Designer (X), Composer (Y)                                                                   | Create and implement audio assets and systems.                                |
| `gft-marketing-sales`        | Marketing Mgr (C), Sales/BizDev Mgr (D)                                                            | Marketing, sales, business development activities.                            |
| `gft-community-support`      | Community Manager (FF), Player Support (GG)                                                        | Community engagement and player support.                                      |
| `gft-legal-team`             | Legal Counsel (HH)                                                                                 | Legal matters.                                                                |

### 6.2. Baseline Repository Permissions by Team

The following table outlines baseline permission levels for each core team on the _core repository
types_. These **MUST** be implemented via IaC (`github_team_repository` resource). The principle of least
privilege is paramount.

- **`read`**: View, clone, fork, open/comment on issues & PRs.
- **`triage`**: Manage issues & PRs (label, assign, close, etc.).
- **`write`**: Push to non-protected branches, manage issues/PRs, create branches.
- **`maintain`**: Manage repo settings (description, topics, etc.), manage releases, manage some protections.
- **`admin`**: Full control, including sensitive settings & deletion.

| Repository Type (`GenCr-ft/...`) | `gft-devops-team` | `gft-architects` | `gft-product-management` | `gft-programming-leads` | Specific Dev Team\* | Specific Design Team\*\* | `gft-qa-team` | `gft-artists-technical` | `gft-artists-production` | `gft-all-members` |
| :------------------------------- | :---------------- | :--------------- | :----------------------- | :---------------------- | :------------------ | :----------------------- | :------------ | :---------------------- | :----------------------- | :---------------- |
| `gencraft-backlog`               | `admin`           | `read`           | `maintain`               | `write`                 | `write`             | `write`                  | `write`       | `read`                  | `read`                   | `triage`          |
| `gcp-aethel-client`              | `admin`           | `write`          | `read`                   | `maintain`              | `write` (client)    | `read` (UX/UI)           | `write`       | `write`                 | `read`                   | `read`            |
| `gcp-aethel-server-core`         | `admin`           | `write`          | `read`                   | `maintain`              | `write` (serv-core) | `read` (Game/Lvl)        | `write`       | `read`                  | `read`                   | `read`            |
| `gcp-aethel-server-pcg`          | `admin`           | `write`          | `read`                   | `maintain`              | `write` (serv-pcg)  | `write` (Lvl/PCG/Narr)   | `write`       | `read`                  | `read`                   | `read`            |
| `gencraft-service-*`             | `admin`           | `write`          | `read`                   | `maintain`              | `write` (services)  | `read`                   | `write`       | `read`                  | `read`                   | `read`            |
| `gencraft-api-contracts`         | `admin`           | `maintain`       | `read`                   | `write`                 | `read` (all devs)   | `read`                   | `triage`      | `read`                  | `read`                   | `read`            |
| `gencraft-assets-voxel` (TBD)    | `admin`           | `read`           | `read`                   | `read`                  | `read` (client)     | `read`                   | `read`        | `write`                 | `write` (Env/Char Art)   | `read`            |
| `gcs-core-governance` (New)     | `maintain`        | `write`          | `write`                  | `write`                 | `read` (all devs)   | `read` (all designers)   | `read`        | `read`                  | `read`                   | `read`            |
| `gencraft-iac`                   | `admin`           | `read`           | `read`                   | `read`                  | `read`              | `read`                   | `read`        | `read`                  | `read`                   | `read`            |
| `gcd-shared-actions`             | `admin`           | `read`           | `read`                   | `read`                  | `read`              | `read`                   | `read`        | `read`                  | `read`                   | `read`            |
| `gcd-ops-scripts`                | `admin`           | `read`           | `read`                   | `read`                  | `read`              | `read`                   | `read`        | `read`                  | `read`                   | `read`            |
| `gencraft-documentation`         | `maintain`        | `write`          | `write`                  | `write`                 | `write`             | `write`                  | `write`       | `write`                 | `write`                  | `read`            |
| `.github` (Org-Level)            | `admin`           | `read`           | `read`                   | `read`                  | `read`              | `read`                   | `read`        | `read`                  | `read`                   | `read`            |

_\*Specific Dev Team:_ e.g., `gft-developers-client` for `gcp-aethel-client`. Assign relevant dev teams.
_\*\*Specific Design Team:_ e.g., `gft-designers-ux-ui` for `gcp-aethel-client`,
`gft-designers-level-pcg` for `gcp-aethel-server-pcg`. Assign relevant design teams.

**Notes:**

- Use `CODEOWNERS` files within repositories to designate default reviewers for specific paths.

## 7. Baseline CI/CD Workflow Definitions (Guidance for Gem B)

This section provides high-level guidance for Gem B (Automation) on establishing baseline Continuous
Integration (CI) workflows for different types of code repositories. Implementation should leverage
**reusable GitHub Actions workflows** stored centrally in `GenCr-ft/gcd-shared-actions` or
the org-level `GenCr-ft/.github` repository.

### 7.1. General CI Principles

- **Trigger:** Run on pushes to all branches and Pull Requests targeting `main`/`release/*`.
- **Feedback Speed:** Optimize for fast feedback, running quick checks first.
- **Coverage:** Include linting, formatting checks, unit tests, integration tests, security scans, and builds.
- **Reproducibility:** Use dependency lockfiles and consider containerized builds.
- **Artifacts:** Version artifacts using SemVer (derived from Conventional Commits) and publish to GitHub Packages/GHCR.

### 7.2. Baseline Stages & Tools by Repository/Technology Type

**(Note: The tool examples below are illustrative; the specific choice should be confirmed based on team
preference and effectiveness, adhering to the OSS/Free preference where possible.)**

#### **7.2.1. TypeScript / Babylon.js (e.g., `gcp-aethel-client`)**

- `Checkout` -> `Setup Node/pnpm` -> `Install Deps (frozen lockfile)` -> `Lint (ESLint)` -> `Format Check
(Prettier)` -> `Type Check (tsc)` -> `Unit Tests (Vitest/Jest)` -> `Integration Tests` -> `Build (Vite/
Webpack)` -> `Security Audit (pnpm audit)` -> `(Optional) Publish/Store Artifact`

#### **7.2.2. C# / .NET (e.g., `gcp-aethel-server-core`, some `gencraft-service-*`)**

- `Checkout` -> `Setup .NET SDK` -> `Restore Deps` -> `Format Check (dotnet format)` -> `Lint/Analyze
(dotnet build /warnaserror)` -> `Unit Tests (dotnet test)` -> `Integration Tests` -> `Build (dotnet build)
` -> `Security Audit (dotnet list vulnerable)` -> `(Optional) Pack/Publish Lib (dotnet nuget push)` -> `
(Optional) Build/Push Image (Docker)`

#### **7.2.3. Go (e.g., `gcp-aethel-server-core` option, some `gencraft-service-*`)**

- `Checkout` -> `Setup Go` -> `Tidy Deps (go mod tidy)` -> `Format Check (gofmt/goimports)` -> `Lint
(golangci-lint)` -> `Unit Tests (go test)` -> `Integration Tests` -> `Build (go build)` -> `Security
Audit (govulncheck)` -> `(Optional) Build/Push Image (Docker)`

#### **7.2.4. Rust (e.g., `gcp-aethel-server-core` option, `gcp-aethel-server-pcg` option)**

- `Checkout` -> `Setup Rust (toolchain file)` -> `Format Check (cargo fmt)` -> `Lint (cargo clippy)` ->
  `Unit/Integration Tests (cargo test)` -> `Build (cargo build)` -> `Security Audit (cargo audit)` -> `
(Optional) Publish Lib` -> `(Optional) Build/Push Image (Docker)`

#### **7.2.5. Python (e.g., `gcp-aethel-server-pcg`, some `gencraft-service-*`)**

- `Checkout` -> `Setup Python/Poetry` -> `Install Deps (poetry install)` -> `Lint (Ruff/Flake8)` -> ####
  `Format Check (Black/Ruff)` -> `Type Check (mypy)` -> `Unit Tests (pytest)` -> `Integration Tests` ->
  `Build (poetry build)` -> `Security Audit (pip-audit)` -> `(Optional) Publish Lib/Package` -> `(Optional)
Build/Push Image (Docker)`

#### **7.2.6. `gencraft-api-contracts`**

- `Checkout` -> `Setup Tooling (Node/Spectral/etc.)` -> `Validate Schema (Lint)` -> `Check Breaking
Changes` -> `(Optional) Generate SDKs` -> `(Optional) Test SDKs` -> `Publish Contracts/SDKs (versioned)`

## 8. Repository & Organization Security Settings

These settings establish a secure baseline for the `GenCr-ft` organization and its repositories. IaC
(`gencraft-iac`) should be used to enforce these settings where possible via the GitHub provider or
organization settings APIs.

### 8.1. Organization-Level Security Settings (Mandatory Configuration by Owners/DevOps)

- **Two-Factor Authentication (2FA):** **MANDATORY** for all members. **(Highest Priority)**
- **Base Member Privileges:** Set to `No permission` or `Read` by default. Access MUST be granted via specific team membership.
- **Repository Creation Permissions:** Restricted to Organization Owners / `gft-devops-team`.
- **Repository Visibility Change Permissions:** Restricted.
- **Repository Deletion/Transfer Permissions:** Restricted.
- **Team Creation Permissions:** Restricted to Organization Owners / `gft-devops-team`.
- **Third-Party Application Access Policy:** Restrictive. Enable request/approval flow. Regularly audit approved apps.
- **Verified Domains:** Configure if applicable.
- **Audit Log Monitoring:** Define a process for periodic review of the organization audit log by the DevOps team.

### 8.2. Default Repository Security Settings (Enforce via IaC & Org Defaults)

For all new repositories:

- **Dependabot Alerts:** **Enabled**.
- **Dependabot Security Updates:** **Enabled**. (Teams are responsible for reviewing/merging Dependabot PRs promptly).
- **Secret Scanning:** **Enabled**.
- **Visibility:** Default to `private`.
- **Branch Protections:** Apply rules as defined in Section 4.5.

## 9. Documentation of Standards (This Document)

- **Central Location:** These comprehensive "GitHub Operational Standards" **MUST** reside in the
  dedicated **`GenCr-ft/devops-standards`** repository. This ensures a single source of truth for all
  DevOps-related standards and guidelines.
- **Structure:** The standards should be organized logically within this repository (e.g., using
  subdirectories like `github/`, `cicd/`, `tooling/`, `iac/`) for clarity and maintainability. _(Refer to
  the structure proposed during the discussion on where to store this document)_.
- **Format:** All documentation **MUST** be in **Markdown**.
- **Updates:** Changes to these standards **MUST** be proposed via **Pull Requests** to the `GenCr-ft/
devops-standards` repository, reviewed by relevant stakeholders (DevOps, Architecture, Leads), and
  approved before merging.

## 10. Conventional Commits Standard

To ensure consistent commit histories, enable automated changelog generation, and facilitate automated
semantic versioning, all commits to repositories within the `GenCr-ft` organization (especially those
containing application code, IaC, automation scripts, or significant documentation) **MUST** adhere
strictly to the **Conventional Commits v1.0.0 specification**. This is essential for generating automated
changelogs and enabling automated semantic versioning.

### 10.1. Commit Message Format

The commit message structure is as follows:

- **Header:** Contains the mandatory `<type>`, optional `(<scope>)`, and a short `<description>` (max
  ~50-72 characters).
- **Body:** Optional. Provides additional context, explaining the "why" and "how" of the change. Use
  imperative mood (e.g., "Fix bug" not "Fixed bug"). Separate from the header by a blank line.
- **Footer:** Optional. Contains metadata like issue references (`Fixes #123`, `Closes #456`) or breaking
  change information (`BREAKING CHANGE:`). Separate from the body by a blank line.

### 10.2. Core Commit Types (`<type>`)

The following types **MUST** be used:

- **`feat`**: A new feature is introduced into the codebase (correlates with `MINOR` in Semantic Versioning).
- **`fix`**: A bug fix in the codebase (correlates with `PATCH` in Semantic Versioning).
- **`docs`**: Documentation only changes (e.g., updates to README, guides, comments).
- **`style`**: Changes that do not affect the meaning or logic of the code (e.g., white-space,
  formatting, missing semi-colons, code style adjustments).
- **`refactor`**: A code change that neither fixes a bug nor adds a feature, but improves code structure,
  readability, or performance without changing external behavior.
- **`perf`**: A code change that improves performance.
- **`test`**: Adding missing tests or correcting existing tests. Does not change production code.
- **`build`**: Changes that affect the build system, build scripts, or external dependencies (example
  scopes: webpack, npm, docker, make).
- **`ci`**: Changes to CI/CD configuration files and scripts (example scopes: GitHub Actions, Jenkins).
- **`chore`**: Other changes that don't modify `src` or `test` files, such as updating dependencies,
  managing project configuration, or minor tooling adjustments.
- **`revert`**: Reverts a previous commit. The header should be `revert: <header of commit being
reverted>`, and the body should state `This reverts commit <hash>.`

### 10.3. Breaking Changes

- A commit that introduces a breaking change (incompatible API change) **MUST** include `BREAKING
CHANGE:` (or `BREAKING-CHANGE:`) in the **footer**, followed by a clear description of the breaking
  change and any migration instructions. This triggers a `MAJOR` version bump in Semantic Versioning.
- Alternatively, an `!` can be appended to the `<type>` or `<type>(<scope>)` prefix (e.g., `feat!: ...`
  or `fix(api)!: ...`) to signify a breaking change. The `BREAKING CHANGE:` footer is still required for clarity.

### 10.4. Scope (`[optional scope]`)

- The scope provides additional contextual information about the commit's impact area. It's contained
  within parentheses following the type (e.g., `feat(client): ...`, `fix(auth-service): ...`, `docs(readme): ...`).
- Scopes should be agreed upon within teams or per repository (e.g., component name, module name, configuration area).

### 10.5. Enforcement & Tooling

- **Commit Linting:** Adherence to this standard **MUST** be enforced using an automated commit message linter.
  - **Recommendation:** Use `commitlint` configured with `@commitlint/config-conventional`.
  - **Implementation:** Integrate `commitlint` with `husky` (Git hooks) in each repository's development
    environment setup to validate messages _before_ commits are created locally. Add a check step in CI
    pipelines as a safety net. A standard `../commitlint.config.js` and `husky` setup will be provided.
- **Automated Versioning/Changelog:** Tools like `semantic-release` or `standard-version` **SHOULD** be
  used in CI/CD release pipelines to automate version bumping (based on commit types) and generate
  `CHANGELOG.md` files.

### 10.6. Reference

- **Official Specification:** [Conventional Commits v1.0.0](https://www.conventionalcommits.org/en/v1.0.0/)

## 11. Git Workflow Standard (Pull Request & Review Process)

This section details the standard practices for the daily Git workflow within the <G@FT.ai> Studio,
focusing on ensuring code quality, collaboration, and a clean history. It complements the branching
strategy defined in Section 4.

### 11.1. Pull Requests (PRs)

- **Requirement:** All changes intended for integration into `main` (or `release/*` branches) **MUST** be
  submitted via a Pull Request. Direct pushes to these protected branches are forbidden (except for
  specific automated processes or emergency fixes by authorized personnel, which must be documented).
- **PR Title:** **MUST** follow the Conventional Commits format (e.g., `feat(client): Add new login
button`). This title often becomes the commit message when using Squash and Merge.
- **PR Description:** **MUST** be comprehensive:
  - Clearly explain the **purpose ("why")** of the changes.
  - Summarize the **implementation ("what" and "how")** at a high level.
  - **Link to relevant Issue(s)** using GitHub keywords (`Fixes #123`, `Closes #456`, `Related to #789`)
    to automatically link or close issues upon merging. Use the correct keyword based on whether the PR
    fully resolves the issue.
  - Provide clear **testing instructions** or steps for reviewers and QA, if applicable.
  - Include **screenshots or GIFs** for any UI/visual changes.
  - Mention any potential **risks or side effects**.
  - A standard **PR Template** (managed via IaC in `.github/pull_request_template.md`) **MUST** be used
    to guide authors.
- **Size & Focus:** PRs should be kept **small and focused**, ideally addressing a single feature, bug
  fix, or logical unit of work. Avoid large, multi-purpose PRs which are difficult and slow to review.
  Break down larger features into smaller, mergeable PRs.
- **Draft PRs:** Use GitHub's "Draft" status for PRs that are work-in-progress. This indicates the PR is
  not yet ready for formal review but allows running CI checks and soliciting early feedback. Convert to
  "Ready for Review" when appropriate.

### 11.2. Code Review Expectations

Code reviews are a critical practice for ensuring quality, sharing knowledge, and maintaining standards.

- **Requirement:** All PRs targeting protected branches **MUST** receive the minimum number of approving
  reviews defined in the branch protection rules (Section 4.5).
- **Reviewers:** Should be assigned (or requested) based on expertise in the code area (`CODEOWNERS` file
  helps automate this). Aim for at least one reviewer familiar with the specific component.
- **Timeliness:** Reviewers should aim to provide feedback within a reasonable timeframe (e.g., 1
  business day) to avoid blocking progress. If unable to review promptly, they should communicate this to
  the PR author.
- **Review Quality:**
  - Reviews **MUST** be **constructive, specific, and respectful**. Focus on the code, not the author.
  - Check for **correctness, potential bugs, edge cases, performance issues, security vulnerabilities,
    adherence to coding standards (language-specific best practices, naming conventions), adherence to
    architectural principles, test coverage, and overall clarity/maintainability.**
  - Provide actionable suggestions for improvement where possible.
  - Use GitHub's review features (comments, suggestions, approve/request changes/comment statuses).
- **Author Responsibility:**
  - Authors should respond to review comments promptly and respectfully.
  - Address all requested changes or provide clear justification if a suggestion is not implemented.
  - Ensure all CI checks are passing after making changes.
  - Notify reviewers once the PR is updated and ready for another look.

### 11.3. Merging Pull Requests

- **Merge Criteria:** A PR can only be merged when:
  - All required CI status checks are passing successfully.
  - The minimum number of required approving reviews has been met.
  - All review comments and conversations have been resolved or explicitly acknowledged.
- **Merge Method:** The **preferred merge method** for merging feature branches into `main` is **Squash and Merge**.
  - **Rationale:** This keeps the `main` branch history clean and linear, with each merge representing a
    complete feature or fix summarized by a single, well-crafted Conventional Commit message (usually
    derived from the PR title and body).
  - **Alternative:** Rebase and Merge _may_ be used in specific repositories or circumstances if
    preserving the detailed commit history from the feature branch onto `main` is deemed valuable and the
    team maintains excellent commit hygiene on feature branches. This requires explicit team agreement per
    repository. Regular merges (creating merge commits) are generally discouraged on `main` to maintain
    linearity.
- **Merge Commit Message:** When using Squash and Merge, ensure the final commit message adheres to the
  Conventional Commits standard (Section 10) and accurately summarizes the changes introduced by the PR.
  GitHub's default squash message often needs editing.
- **Branch Cleanup:** Feature branches **MUST** be deleted after their corresponding PR is successfully
  merged. GitHub can be configured to offer automatic branch deletion upon merging.

### 11.4. Commit Hygiene on Feature Branches

While working on feature branches:

- **Adhere to Conventional Commits:** Strive to follow the format even for intermediate commits on your
  feature branch. This makes the branch history easier to understand.
- **Atomic Commits:** Make frequent, small, atomic commits representing logical steps in your work. Avoid
  large, infrequent commits.
- **Clear Messages:** Write clear messages explaining the _why_ behind each commit.
- **Clean Up Before PR (Optional but Recommended):** Before marking a PR as "Ready for Review", consider
  cleaning up your feature branch history using interactive rebase (`git rebase -i main`). This allows you
  to reorder, squash "fixup" or "WIP" commits, and reword messages for clarity before presenting the work
  for review. This is particularly important if Rebase and Merge is used.

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
