---
docId: SEC-STAN-003
title: Sec 003 Secret Scanning Standard
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This standard mandates the use of GitHub Advanced Security and Gitleaks to
  detect and remediate secrets committed to Gencraft source code repositories. It
  requires automated scanning in pre-commit hooks, CI/CD pipelines, and periodic repository
  scans, with a defined process for managing false positives and ensuring immediate
  remediation of active secrets.
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - security-scanning
  - secrets-management
  - gitleaks
  - github-advanced-security
  - ci-cd
  - devops-standards
  - threat-detection
  - code-security
  scope: studio
  domain: security
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/security/standards/SEC-STAN-003.sec-003-secret-scanning-standard.md
---
## 1. Objective

This standard defines the mandatory strategy, tools, procedures, and responsibilities for detecting,
remediating, and preventing the accidental commitment of secrets (e.g., passwords, API keys, access
tokens, private certificates, sensitive configuration variables) into Gencraft source code repositories
and other non-secure locations within the studio's digital assets. The primary goal is to protect
Gencraft's systems, data, and reputation from unauthorized access and breaches resulting from exposed secrets.

## 2. Scope

This standard applies to:

- All Gencraft source code repositories within the `GenCr-ft` GitHub organization (including application
  code, IaC, scripts, documentation, configuration files).
- All Gencraft Gems (human and AI) and contributors who interact with or create content for these repositories.
- CI/CD pipelines processing Gencraft code.
- Local developer environments.

This standard complements `sec-001-secrets-management-standard.md`, which dictates _how_ secrets should be
managed; this document focuses on _detecting_ improperly managed secrets.

## 3. Standard

### 3.1. Core Principle: No Secrets in Code or Unsecured Locations

It is strictly PROHIBITED to store secrets directly in source code, configuration files committed to
repositories, issue trackers, wikis, or any other location not explicitly approved as a secure secret
store by `sec-001-secrets-management-standard.md`.

### 3.2. Approved Secret Scanning Tool(s)

- **Primary Tool(s):**
  - **GitHub Advanced Security (GHAS) Secret Scanning:** To be enabled on all Gencraft repositories
    where available. This provides automated detection for known secret patterns.
  - **Gitleaks (Open Source):** To be used for local pre-commit hooks and potentially for deeper or
    custom scans in CI/CD pipelines due to its configurability and speed.
- **Justification:**
  - GHAS offers seamless integration and a broad set of predefined patterns.
  - Gitleaks provides excellent performance, custom rule capabilities, and local execution for developers.
- **Configuration SSoT:**
  - GHAS: Configuration managed at the GitHub organization level by `Cerberus` and `Adam`.
  - Gitleaks: A baseline Gencraft configuration file (e.g., `.gitleaks.toml`) defining rules,
    exclusions, and sensitivity will be maintained in `gcs-core-governance/security/configs/gitleaks.
toml` (To Be Created by `Cerberus` and `Camille`). This configuration should be used by pre-commit
    hooks and CI jobs.
- **Version:** The latest stable version of Gitleaks as specified in
  `validate_gft_devops_environment_proj103.sh` must be used.

### 3.3. Integration Points and Scanning Cadence

1. **Local Pre-commit Hooks (MANDATORY):**
   - Tool: Gitleaks.
   - Execution: Automatically triggered on every `git commit` attempt.
   - Configuration: Managed via `../tooling/tool-004-git-hooks-standard.md`, using the central Gitleaks configuration.
   - Action: Commits MUST be blocked if secrets are detected. 2.**CI/CD Pipelines - Pull Request Checks (MANDATORY):**
   - Tool: GHAS Secret Scanning (if enabled and covers the PR diff) AND/OR Gitleaks scan of changes.
   - Execution: Automatically triggered on every Pull Request targeting protected branches (e.g., `main`,
     `develop`, release branches).
   - Action: PRs MUST be blocked (build/check fails) if new secrets are detected. 3.**Repository Scanning (Automated & Periodic):**
   - Tool: GHAS Secret Scanning (for continuous, automated scanning of repositories). Gitleaks for
     targeted, deeper, or periodic full-history scans.
   - Cadence:
     - GHAS: Continuous upon enablement.
     - Gitleaks Full History Scans:
       - Initial baseline scan of ALL existing repositories (coordinated by `Cerberus` and `Adam`).
       - Periodic re-scans (e.g., monthly or quarterly, or upon significant changes to Gitleaks rules) of all repositories.
   - Purpose: Detect secrets missed by PR checks (e.g., in non-protected branches subsequently merged,
     historical commits before standard implementation) or newly identified secret patterns.

### 3.4. Detection, Alerting, and False Positive Management

- **Alerting:**
  - GHAS: Alerts are typically surfaced in the repository's "Security" tab and can be configured to
    notify repository administrators and security managers (`Cerberus`).
  - Gitleaks (CI/Periodic Scans): Findings MUST generate high-priority alerts (e.g., automated P1/P2
    Issue creation in a dedicated security backlog like `gencraft-security-operations`, notifications to
    `Cerberus` and the repository's designated maintainers/Tech Lead).
- **Triage:** `Cerberus` (or delegated security team members) is responsible for triaging all reported secret scanning alerts.
- **False Positive Management:**
  - **Verification:** Any potential false positive MUST be rigorously investigated by the reporter and
    validated by `Cerberus` and at least one relevant technical specialist (e.g., the code author, Tech Lead).
  - **Criteria for FP:** Must be confirmed that the detected pattern is not a secret, is test/example
    data explicitly marked and non-functional, or is a pattern that cannot be exploited.
  - **Documentation:** Validated false positives MUST be documented. This can be done via:
    - Adding specific, narrow ignore rules to the Gitleaks configuration file (with comments
      justifying each rule), managed via PR by `Cerberus`.
    - Adding inline ignore comments (e.g., `gitleaks:allow`) in code for very specific, unavoidable
      cases. This practice should be used RARELY and requires explicit approval from `Cerberus` in the
      PR. The comment MUST include a justification and an Issue link tracking the FP.
    - For GHAS, use the platform's dismissal features with clear justification.
  - **Review of FPs:** The list of allowed false positives/ignored patterns MUST be reviewed quarterly
    by `Cerberus` to ensure they remain valid.
  - No sensitive production secret should ever be whitelisted as a false positive.

### 3.5. Remediation Process

1. **Containment (Immediate Action for Exposed Active Secrets):**
   - If an active/valid secret (especially for production or sensitive systems) is found: - **DO NOT DELETE THE PR/COMMIT YET** (unless it's the only way to prevent immediate misuse and
     revocation is impossible - consult `Cerberus`). This preserves evidence for investigation. - The exposed secret MUST be immediately revoked, rotated, or invalidated by the team responsible
     for that secret/system, with URGENCY. `Cerberus` coordinates this. - Access using the compromised secret must be audited. 2.**Code Remediation:**
   - The commit(s) containing the secret MUST be remediated.
   - **Preferred method:** The developer amends the commit locally to remove the secret (if not yet
     pushed to a shared branch) or creates a new commit that removes the secret and replaces its usage with
     a secure method (as per `sec-001-secrets-management-standard.md`). 3.**Removing Secrets from Git History (If Pushed to Shared/Protected Branches):**
   - This is a destructive and complex operation and should be a last resort after the secret is revoked.
   - **Tools:** `git filter-repo` (recommended) or BFG Repo-Cleaner.
   - **Procedure:**
     - MUST be performed by authorized and experienced DevOps personnel (`Adam`, `Benjamin`) under the
       direct supervision and approval of `Cerberus`.
     - The repository SHOULD be temporarily locked for writes.
     - All developers MUST be informed to re-clone/rebase after the operation.
     - A backup of the repository MUST be taken before attempting history rewriting.
   - **Caution:** Rewriting history can invalidate existing PRs, branches, and clones. 4.**Incident Response:**
   - Confirmed exposure of active production or highly sensitive secrets MUST trigger the Gencraft
     Security Incident Response Process (refer to `../../gcs-core-governance/01-operational-protocols/
s3-emergency-management.md` and any specific Security Incident Response Plan). `Cerberus` leads this. 5.**Verification & Closure:**
   - `Cerberus` verifies that the secret has been revoked and the code/history has been remediated.
   - The corresponding alert/issue is formally closed with documentation of actions taken.

### 3.6. Training and Awareness

- All Gencraft Gems and contributors involved with code MUST receive training on:
  - Secure secret management practices (`sec-001-secrets-management-standard.md`).
  - The risks of committing secrets.
  - How to use local pre-commit secret scanning hooks.
  - The Gencraft secret remediation process.
- Training is coordinated by `Adam` (for DevOps aspects) and `Cerberus` (for security aspects).

### 3.7. Custom Detections

- `Cerberus`, in collaboration with `Camille` and relevant Tech Leads, is responsible for identifying the
  need for and defining custom secret patterns specific to Gencraft (e.g., internal service token formats).
- These custom patterns will be added to the Gitleaks configuration file (`gcs-core-governance/security/
configs/gitleaks.toml`) and tested thoroughly.

### 3.8. Actionability for AI Gems

- **Code Generation:** AI Gems that generate code, configuration, or documentation (e.g., `Gemma`,
  `Oracle`) MUST be programmed or prompted to explicitly avoid embedding any placeholder or actual secrets.
  They should use placeholders like `{{ SECRET_NAME_FROM_VAULT }}` or follow `SEC_001` for referencing
  secrets.
- **Code Review Assistance:** Future AI Gems assisting in code reviews SHOULD be equipped to leverage
  secret scanning tool outputs or incorporate basic pattern matching for potential secrets.

## 4. Responsibilities

- **`Cerberus` (Security Officer Gem):**
  - Owner and Knowledge Guardian of this standard.
  - Defining and maintaining the SSoT Gitleaks configuration and custom detection patterns.
  - Leading the triage and remediation efforts for critical secret exposures.
  - Approving false positive declarations and whitelist entries.
  - Leading Security Incident Response for exposed secrets.
  - Conducting periodic reviews of the false positive list and overall process effectiveness.
- **`Camille` (Gem AB - Automation Specialist):**
  - Implementing and maintaining the integration of Gitleaks (and other scanners if needed) into CI/CD
    pipelines and pre-commit hooks.
  - Assisting `Cerberus` with tooling aspects and custom pattern implementation.
- **`Adam` (Gem AA - DevOps Team Lead):**
  - Ensuring DevOps processes and CI/CD pipelines adhere to this standard.
  - Authorizing and overseeing Git history rewriting operations when necessary.
  - Coordinating developer training on secret scanning tools and practices.
- **All Gencraft Developers/Contributors (Human and AI Gems):**
  - MANDATORY use of local pre-commit secret scanning hooks.
  - Responsibility for not committing secrets into repositories.
  - Promptly reporting any accidental secret commitments.
  - Cooperating fully with remediation procedures.
- **Repository Maintainers / Tech Leads:**
  - Ensuring secret scanning (e.g., GHAS) is enabled for their repositories.
  - Responding to alerts for secrets found in their repositories and assisting in remediation.
- **`Édouard` (Gem AD - DevOps Strategy Specialist):**
  - Ensuring this standard aligns with overall DevOps and security strategies.

## 5. Review and Evolution

This standard will be reviewed at least annually by `Cerberus` and `Adam`, or more frequently if
significant incidents occur or new scanning technologies become available. Changes will follow the S13
Global Protocol Evolution process.

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
