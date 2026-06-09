---
docId: DEV-STAN-014
title: Cicd 001 Baseline Workflow Guidance
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: "This document outlines a baseline CI/CD workflow for G@FT.ai Studio\u2019\
  s code repositories, emphasizing automation, security, and consistent quality checks.\
  \ It provides guidance on pipeline stages, tooling, and deployment strategies, primarily\
  \ utilizing GitHub Actions and reusable workflows."
last_updated_date: '2026-06-02'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - cicd
  - ci-cd
  - workflow
  - gft-ai
  - github-actions
  - automation
  - devops
  - security
  scope: studio
  domain: devops
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l3_secret

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/cicd/standards/DEV-STAN-014.cicd-001-baseline-workflow-guidance.md
---
## 1. Purpose

This document provides guidance and baseline requirements for establishing Continuous Integration (CI) and
Continuous Delivery/Deployment (CD) workflows for <G@FT.ai> Studio's code repositories. The goal is to
ensure consistent quality checks, automated builds, security scanning, and reliable deployment processes
across all projects.

These guidelines are intended for Gem BB (DevOps Automation Specialist) to implement, primarily using
**GitHub Actions** and leveraging **reusable workflows** stored in `GenCr-ft/gencraft-devops-automation`
or the organization-level `.github` repository.

## 2. Core CI/CD Principles

All CI/CD pipelines **MUST** adhere to the following principles:

- **Automation:** Maximize automation of build, test, and deployment processes.
- **Fast Feedback:** Developers should receive feedback from CI checks as quickly as possible (especially
  on Pull Requests). Optimize pipeline execution times.
- **Reproducibility & Idempotency:** Builds and deployments must be reproducible and pipeline stages
  idempotent. Use dependency lockfiles and consider containerized build/deployment environments.
- **Early Failure Detection:** Structure pipelines to fail fast (e.g., run linters and unit tests before
  longer integration tests or builds).
- **Security Integrated (DevSecOps):** Integrate security scanning (SAST, DAST, dependency scanning,
  secret scanning) into the pipelines.
- **Visibility & Traceability:** Pipeline status, logs, and artifacts must be easily accessible. Link CI/
  CD runs to commits and issues.
- **Consistency:** Use standardized tools and practices across similar repository types.
- **Reusable Workflows:** Prioritize the creation and use of centrally managed reusable GitHub Actions
  workflows to avoid duplication and ensure standards are applied consistently.
- **Environment Promotion:** Implement clear strategies for promoting artifacts through different
  environments (e.g., Dev -> Staging -> Prod).

## 3. Standard CI Pipeline Triggers

Baseline CI workflows **MUST** trigger on:

- Pushes to **any branch**.
- **Pull Requests** targeting the `main` branch or any `release/*` branches.
- (Optional, for CD) Pushes to `main` or `release/*` branches after PR merge (for deployments).
- (Optional) Scheduled runs (e.g., nightly builds, extended test suites).

## 4. Baseline CI Workflow Stages & Tooling by Technology

The following outlines the recommended baseline stages and associated tooling for CI pipelines. Gem BB
should adapt these into reusable workflows, referencing `../tooling/
tool-002-language-specific-tooling-standards.md` and `../tooling/tool-003-code-style-and-formatting.md`
for specific tool configurations.

### 4.1. General Stages (Applicable to most code repositories)

1. **Checkout Code:**
   - Action: `actions/checkout@vX` (use latest stable version).
   - Consider fetching full history if needed for tools like `semantic-release`.

2. **Setup Environment & Cache Dependencies:**
   - Set up the specific language runtime (Node.js, .NET, Python, Go, Rust).
   - Cache dependencies (`node_modules`, `nuget packages`, `pip cache`, `go mod cache`, `cargo registry/target`) to speed up subsequent runs.
   - Action examples: `actions/setup-node@vX`, `actions/setup-dotnet@vX`, `actions/setup-python@vX`, `actions/setup-go@vX`, `dtolnay/rust-toolchain@stable`.

3. **Install Dependencies:**
   - Use locked versions (e.g., `pnpm install --frozen-lockfile`, `dotnet restore --locked-mode`, `poetry install`, `go mod download`, `cargo fetch`).

4. **Lint & Format Check:**
   - Run linters and formatters in "check" mode.
   - Fail the build if linting errors or formatting inconsistencies are found.
   - Refer to `TOOL_002` and `TOOL_003` for specific tools (ESLint, Prettier, dotnet-format, golangci-lint, Ruff, rustfmt, clippy).

5. **Static Analysis & Security Scans (SAST):**
   - Run language-specific static analysis tools.
   - Run security-focused linters or SAST tools (e.g., SonarCloud free tier for open source, or language-specific tools).

6. **Unit Tests:**
   - Execute unit tests and collect code coverage.
   - Fail the build if tests fail or coverage drops below a defined threshold (80%).

7. **Integration Tests:**
   - Execute integration tests (may require setting up service dependencies like databases or mock servers).

8. **Build Application/Library:**
   - Compile code, bundle assets, create executables or packages.

9. **Dependency Vulnerability Scan:**
   - Scan dependencies for known vulnerabilities (e.g., `pnpm audit`, `dotnet list package --vulnerable`, `govulncheck`, `cargo audit`, `pip-audit`).
   - Fail the build based on vulnerability severity (e.g., fail on `high` or `critical`).

10. **(Optional) Build Container Image:**
   - If the application is containerized, build the Docker image.
   - Scan the image for vulnerabilities (e.g., Trivy, Snyk).

11. **(Optional) Publish Artifacts:**
   - For libraries: Publish versioned packages to GitHub Packages (or other configured registries). Versioning **MUST** be automated based on Conventional Commits (see Section 10 of GitHub Operational Standards and `TOOL_001`).
   - For applications: Store build artifacts (e.g., ZIP files, executables) in GitHub Releases or an artifact repository.
   - For container images: Push versioned images to GitHub Container Registry (GHCR) or other configured container registry.

### 4.2. Specifics for `gencraft-api-contracts`

The CI pipeline for `GenCr-ft/gencraft-api-contracts` has specific needs:

1. **Checkout Code** 2.**Setup Tooling** (e.g., Node.js for Spectral-CLI, OpenAPI Generator CLI). 3.**Validate Schema & Lint:** Use tools like Spectral to lint OpenAPI definitions or appropriate linters
   for Protobuf/JSON Schema. 4.**Check for Breaking Changes:** Compare the current contract against the previously released version
   (e.g., using `openapi-diff`). Fail PRs that introduce breaking changes without a corresponding MAJOR
   version increment (as per Conventional Commits). 5.**(Optional but Recommended) Generate SDKs/Stubs:** Use tools like OpenAPI Generator. 6.**(Optional) Test Generated SDKs:** Basic compilation or smoke tests for generated code. 7.**Publish Contracts & (Optional) SDKs:**
   - Version automatically based on Conventional Commits (SemVer).
   - Publish versioned contract files (e.g., `openapi.json`) and generated SDKs as packages to GitHub Packages.

## 5. Continuous Delivery/Deployment (CD) Strategy (High-Level Guidance)

While full CD is a more advanced topic, CI pipelines should be designed with CD in mind.

- **Environment-Specific Configurations:** Manage configurations for different environments (Dev, Staging,
  Prod) securely (e.g., using GitHub Actions encrypted secrets, Vault, or cloud provider secret managers).
- **Deployment Triggers:**
  - Deployments to **Dev/Staging** environments can be automated on merge to `main` or specific branches.
  - Deployments to **Prod** **MUST** require manual approval/trigger or follow a strict GitOps promotion
    process after successful staging validation.
- **Deployment Strategies:** Standardize on common deployment strategies (e.g., Blue/Green, Canary) where
  appropriate. This will be further detailed in `cicd-003-deployment-strategies.md`.
- **IaC Integration:** Deployments that involve infrastructure changes should integrate with the `GenCr-ft/
gencraft-iac` repository and its pipelines.
- **Rollback Plans:** Define and test rollback procedures for critical deployments.

## 6. Reusable Workflows Implementation

- Gem BB **MUST** prioritize creating **reusable workflows** in `GenCr-ft/gencraft-devops-automation` for
  common CI stages (e.g., a `typescript-ci-workflow`, `dotnet-ci-workflow`, `python-ci-workflow`,
  `publish-to-github-packages-workflow`).
- Repository-specific workflows (`.github/workflows/main.yml`) will then _call_ these reusable workflows
  with appropriate inputs/secrets.
- This approach ensures consistency, maintainability, and easy updates to CI processes across all
  repositories.
- When configuring branch protection rules (Section 4.5 of GitHub Operational Standards), required status
  checks **MUST** reference the job IDs from these reusable workflows to ensure their execution.

## 7. Monitoring and Reporting

- CI/CD pipelines should generate clear status reports (success/failure, test results, coverage).
- Integrate with GitHub Checks API for rich feedback on PRs.
- Consider collecting DORA metrics or other relevant DevOps performance indicators.

## 8. Review and Updates

This guidance document will be reviewed and updated periodically by the DevOps team in collaboration with
development leads and architects to incorporate new tools, best practices, and lessons learned.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
