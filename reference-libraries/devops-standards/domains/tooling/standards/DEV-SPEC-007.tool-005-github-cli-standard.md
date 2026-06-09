---
docId: DEV-SPEC-007
title: Tool 005 Github Cli Standard
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This standard defines mandatory guidelines for using the GitHub CLI (`gh`)
  within the Gencraft studio, focusing on installation, secure authentication (using
  PATs or GitHub App tokens), and script usage for automation by AI Gems and human
  developers.
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - github-cli
  - gh
  - automation
  - security
  - standard
  - tooling
  - ai-gems
  scope: studio
  domain: devops
  doc-type: specification
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/tooling/standards/DEV-SPEC-007.tool-005-github-cli-standard.md
---
## 1. Objective

This standard defines the mandatory guidelines for the installation, configuration, and secure, efficient
usage of the GitHub CLI (`gh`) tool within the Gencraft studio. The objective is to ensure consistent and
auditable interactions with GitHub, particularly for automated operations by AI Gems and human developers,
and for repository and workflow management tasks. Adherence to this standard is critical for maintaining
security and operational stability.

## 2. Scope

This standard applies to ALL usages of the GitHub CLI (`gh`) by any Gencraft Gem or human contributor
interacting with the `GenCr-ft` GitHub organization and its repositories. This includes interactive
terminal usage, scripting for automation (local or CI/CD), and any `Tool` developed by the AI Enablement
Team that leverages `gh`.

## 3. Standard

### 3.1. Installation and Versioning

- **Minimum Required Version:** `2.20.0` (or as specified in the latest
  `validate_gft_devops_environment_proj103.sh` script [cite: devops_env_validation_script_proj103] and
  `gcs-core-governance/tooling/TOOL_README.md` which should list current tool versions). This ensures
  access to necessary features (e.g., advanced `--template` options) and security patches.
- **Installation Method:** Adherence to official instructions at [https://github.com/cli/cli#installation]
  (<https://github.com/cli/cli#installation>) is mandatory. For WSL/Ubuntu environments, the method via `apt`
  after adding the GitHub repository is the recommended SSoT.
- **Verification:** The presence and version of `gh` MUST be verifiable by the
  `validate_gft_devops_environment_proj103.sh` script [cite: devops_env_validation_script_proj103].
  `Camille` (Gem AB) is responsible for updating this validation script if the standard version changes.

### 3.2. Authentication

- **Primary Method (Interactive Use):** Authentication MUST be performed via `gh auth login`, prioritizing
  browser-based OAuth flow. Two-factor authentication (2FA) MUST be enabled on the associated GitHub account.
- **Tokens for Automation (CI/CD, Scripts, AI Gems):** 1.**Token Types:** GitHub Personal Access Tokens (PATs - fine-grained preferred over classic) or
  GitHub App installation tokens MUST be used. PATs associated with individual human accounts are
  STRONGLY DISCOURAGED for shared or service automations; prefer GitHub App tokens or dedicated service
  account PATs (if unavoidable and strictly managed). 2.**Scope (Least Privilege):** Tokens MUST be created with the absolute minimum required scopes
  (Principle of Least Privilege) for the intended operations. Scopes MUST be documented alongside the
  token's purpose and SSoT location (e.g., in the secrets manager description). `Cerberus` (Security
  Officer Gem) MUST be consulted for scope definition on sensitive operations. 3.**Storage & Access (Security):** Tokens MUST be stored securely as per `../security/
sec-001-secrets-management-standard.md` [gcs-core-governance/security/
  sec-001-secrets-management-standard.md]. - For CI/CD (GitHub Actions): Use encrypted organization or repository secrets. - For local Gem/script usage by AI Gems or humans: Use the studio's approved secrets management
  tool (e.g., HashiCorp Vault, or other as defined by `Cerberus`). - Tokens MUST NEVER be hardcoded in scripts, committed to repositories, or logged. 4.**Environment Variables:** When `gh` uses a token via an environment variable (e.g., `GH_TOKEN`,
  `GITHUB_TOKEN`), the script or process sourcing this variable MUST ensure it's not exposed in logs (e.
  g., by using `set +x` in Bash before sourcing, or GitHub Actions' secret masking). 5.**Expiration and Rotation:** PATs SHOULD have an expiration date. A process for regular review and
  rotation of tokens used by critical automations MUST be established by `Cerberus` and `Adam` (Gem AA).
- **Verification:** The `validate_gft_devops_environment_proj103.sh` script [cite:
  devops_env_validation_script_proj103] checks basic authentication status. `Cerberus` (Security Officer
  Gem) is responsible for auditing token scopes, storage, and rotation policies.

### 3.3. Usage in Scripts (Actionability for AI Gems)

- **Non-Interactivity:** Scripts utilizing `gh` MUST be designed for non-interactive execution. All
  necessary inputs MUST be provided via arguments or environment variables. Interactive prompts are
  FORBIDDEN in automated scripts. Use options like `--yes` for `gh repo rename` or ensure all confirmation
  paths are handled programmatically.
- **Error Handling & Logging:**
  1. Scripts MUST robustly check the exit code of every `gh` command.
     2.Comprehensive error handling and logging MUST be implemented as per `../scripting/
script-001-general-scripting-standard.md` (To Be Created). This includes logging context, command
     executed (excluding sensitive parts), and exit code.
     3.Sensitive information (tokens, private data) from error messages or command outputs MUST NOT be
     logged directly. Log error codes or sanitized, generic messages instead.
- **JSON Output and Parsing:**

  1. For data retrieval, `gh` commands MUST use the `--json <fields>` option to request only the
     specific fields needed, in JSON format. This minimizes data transfer and simplifies parsing.
     2.The output MUST be parsed using `jq` (as per `tool-006-jq-usage-standard.md` - To Be Created) or
     `gh`'s built-in `--jq <expression>` or `--template <templateString>` options for simpler cases. 3.**Example (Get PR number, title, and author login for open PRs):**

  ```bash
      # Assumes REPO_URL and GH_TOKEN are set
      gh pr list --repo "$REPO_URL" --state open \
        --json number,title,author \
        --jq '.[] | {pr_number: .number, pr_title: .title, pr_author: .author.login}'
  ```

- **API Rate Limit Consideration:**
  1. Scripts making numerous `gh` calls, especially `gh api` or listing commands with pagination, MUST
     be designed to respect GitHub API rate limits.
     2.Implement appropriate delays (`sleep`), use conditional requests (e.g., with ETags if using `gh
api`), and handle rate limit error responses gracefully (e.g., retry with backoff).
     3.Log rate limit information (`X-RateLimit-Remaining` header via `gh api -i`) if performing bulk
     operations, to aid in debugging and optimization.
- **Advanced Interactions via `gh api`:**
  1. The `gh api` subcommand SHOULD be used for interactions not adequately covered by native `gh`
     commands.
     2.The exact API endpoint (versioned, e.g., `/repos/{owner}/{repo}/actions/runs`), HTTP method, and
     request body (if any) MUST be clearly documented within the script or its accompanying documentation.
     3.Token scopes for `gh api` calls MUST be meticulously defined and minimized for the specific
     endpoint being accessed. Consult `Cerberus` for scope validation.
- **Idempotency:** Scripts that modify state (e.g., creating labels, setting repository options) SHOULD be
  designed to be idempotent where feasible (applying the script multiple times yields the same end state
  without error or unintended side effects). This might involve checking for existence before creating, or
  using commands that inherently support "create or update" semantics.

### 3.4. Common Use Cases & Gencraft Helper Scripts

- **Core Operations:** Repository management (as per PROJ-103 [cite: devops_transformation_plan_proj103]),
  PR/Issue management, GitHub Actions workflow interactions, release management.
- **Gencraft Helper Scripts/Aliases (`Camille` - Gem AB):**
  1. Frequently used sequences of `gh` commands or complex queries MAY be encapsulated into reusable
     helper scripts (Bash, Python) or shell aliases. 2.**SSoT for Helpers:** `gencraft-devops-automation/scripts/gh-helpers/` (To Be Populated by
     `Camille`).
     3.These helpers MUST adhere to all sections of this standard (error handling, security,
     non-interactivity, etc.) and be well-documented (purpose, arguments, usage examples, required token
     scopes).
     4.Example helpers: `create-standard-repo.sh`, `get-pr-details.sh`, `trigger-release-pipeline.sh`.

### 3.5. Security Considerations

- Reiteration: Principle of Least Privilege for tokens is paramount.
- Regular audit of PATs and GitHub App permissions (Responsibility: `Cerberus`, `Adam`).
- Avoid exposing sensitive data (repository contents, private issue details, user PII) in logs unless
  explicitly required for a documented purpose and logs are appropriately secured and have retention policies.
- Scripts using `gh` to modify critical settings (e.g., branch protections, repository visibility) MUST
  have an additional layer of approval or be executed by highly privileged automation with strict controls.

## 4. Responsibilities

- **`Édouard` (Gem AD - DevOps Strategy):**
  - Maintenance and evolution of this standard.
  - Proposing updates based on new `gh` features, security best practices, or studio needs.
  - Ensuring dependent standards (scripting, jq, secrets) are created and maintained.
- **`Camille` (Gem AB - Automation Specialist):**
  - Developing and maintaining SSoT helper scripts in `gencraft-devops-automation/scripts/gh-helpers/`.
  - Advising other Gems on best practices for scripting `gh` commands.
- **All DevOps Gems & AI Tool Developers (e.g., `Vector` from AIE Team):**
  - Strict adherence to this standard when scripting interactions with GitHub via `gh`.
- **`Cerberus` (Security Officer Gem):**
  - Auditing the secure use of `gh` tokens, scopes, and permissions granted.
  - Approving token scopes for sensitive operations.
  - Defining standards for secure token storage and rotation.
- **Repository Maintainers / Technical Leads:**
  - Ensuring scripts within their repositories that use `gh` comply with this standard.

## 5. References & SSoTs

- Official GitHub CLI Documentation: [https://cli.github.com/manual/](https://cli.github.com/manual/)
- `../security/sec-001-secrets-management-standard.md` [gcs-core-governance/security/
  sec-001-secrets-management-standard.md]
- `validate_gft_devops_environment_proj103.sh` [cite: devops_env_validation_script_proj103]
- `gencraft-devops-automation/scripts/gh-helpers/` (To Be Populated by `Camille`)
- `../scripting/script-001-general-scripting-standard.md` (To Be Created by `Édouard`)
- `tool-006-jq-usage-standard.md` (To Be Created by `Édouard`)
- `../../gcs-core-governance/02-knowledge-base-hub/02-knowledge-base-hub/kb-domain-security/
access-control-policy.md` [gcs-core-governance/02-knowledge-base-hub/02-knowledge-base-hub/
  kb-domain-security/access-control-policy.md]

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
