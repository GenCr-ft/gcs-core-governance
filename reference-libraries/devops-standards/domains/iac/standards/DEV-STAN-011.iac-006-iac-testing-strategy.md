---
docId: DEV-STAN-011
title: Iac 006 Iac Testing Strategy
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This standard defines a multi-layered testing strategy for OpenTofu-based
  Infrastructure as Code (IaC) at Gencraft. It emphasizes static analysis, unit testing,
  and integration testing to ensure syntactically correct, secure, and functional
  IaC code, ultimately increasing confidence in deployments and reducing risks.
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - iac-testing
  - open-tofu
  - testing-strategy
  - infrastructure-as-code
  - gencraft
  - static-analysis
  - unit-testing
  - integration-testing
  scope: studio
  domain: devops
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/iac/standards/DEV-STAN-011.iac-006-iac-testing-strategy.md
---
## 1. Objective

This standard defines the comprehensive testing strategy for Infrastructure as Code (IaC) developed using
OpenTofu at Gencraft. The primary objectives are to:

- Ensure IaC code is syntactically correct, compliant with Gencraft standards, and secure by design.
- Verify that provisioned infrastructure behaves as expected and meets functional and non-functional requirements.
- Increase confidence in IaC changes and reduce the risk of deployment failures or operational issues.
- Enable rapid feedback loops for IaC developers through automated testing.
- Provide a clear framework for different levels of testing applicable to IaC.

## 2. Scope

This standard applies to:

- All OpenTofu code, including root configurations and reusable modules, within all Gencraft IaC
  repositories (e.g., `gencraft-studio-iac`, `gencraft-game-aethel-iac`).
- All Gencraft Gems and human contributors involved in writing, reviewing, or deploying IaC.
- All stages of the IaC development lifecycle, from local development to CI/CD pipelines and
  post-deployment monitoring.

## 3. IaC Testing Strategy & Levels

Gencraft adopts a multi-layered IaC testing approach, often visualized as a testing pyramid, to provide
comprehensive coverage and rapid feedback.

### 3.1. Level 1: Static Analysis & Validation (Pre-Deployment)

This is the foundational level, focused on automated checks without deploying actual resources.

- **Linting & Formatting:**
  - **Tools:** `tofu fmt -check` (for formatting), `tflint` (for linting against best practices and
    Gencraft-specific rules if developed).
  - **Purpose:** Enforce code style consistency (`iac-004-clean-iac-principles.md`), detect stylistic
    errors, and identify potential issues or deviations from best practices.
  - **Execution:** Pre-commit hooks (`../tooling/tool-004-git-hooks-standard.md`), Pull Request (PR)
    checks in CI pipelines.
  - **Reference:** `iac-007-iac-static-analysis-standard.md`.
- **Security Scanning:**
  - **Tools:** `tfsec` (or Gencraft-approved alternative as per `../security/
sec-002-iac-scanning-tool-selection.md`).
  - **Purpose:** Identify security misconfigurations, vulnerabilities, and deviations from security best
    practices in IaC code.
  - **Execution:** Pre-commit hooks (recommended), PR checks in CI pipelines (mandatory).
  - **Reference:** `iac-007-iac-static-analysis-standard.md`.
- **Syntactic & Semantic Validation:**
  - **Tool:** `tofu validate`.
  - **Purpose:** Check the syntactic correctness of OpenTofu code and validate configurations against
    provider schemas and module definitions. Ensures references are valid and types match.
  - **Execution:** Pre-commit hooks, PR checks in CI pipelines.

### 3.2. Level 2: Unit Testing (for Modules - Pre-Deployment)

Focuses on testing individual OpenTofu modules in isolation.

- **Tool:** OpenTofu's native testing framework (`tofu test` command with `.tftest.hcl` assertion files).
- **Purpose:**
  - Verify that a module provisions resources as expected based on various input variable combinations.
  - Validate the module's output values against expected outcomes.
  - Test edge cases and conditional logic within the module.
  - Ensure the module adheres to its defined input/output contract.
- **Scope:** Test individual modules by deploying actual (but sandboxed and temporary) resources. Tests
  should be self-contained and clean up after themselves.
- **Execution:**
  - PR checks in CI when changes are made to a module.
  - Potentially nightly or weekly runs for critical shared modules to catch provider API changes.
- **Test Case Structure (`.tftest.hcl`):**
  - Define `variables` blocks for test inputs.
  - Use `run` blocks to execute `tofu apply`.
  - Use `assert` blocks with `condition` and `error_message` to check post-deployment state (e.g.,
    resource attributes, outputs).
- **Documentation:** Test files MUST reside within the module's directory (e.g., in a `/tests`
  subdirectory). The module's README SHOULD mention the testing approach.

### 3.3. Level 3: Integration Testing (Compositions & Root Configurations - Pre-Deployment)

Focuses on testing how different modules and resources interact within a larger configuration (e.g., an
environment slice or a full environment).

- **Tools:**
  - `tofu plan -out=plan.tfplan` followed by `tofu apply plan.tfplan` in a dedicated, ephemeral test environment.
  - Custom verification scripts (Bash, Python using cloud provider SDKs, or PowerShell) to check the
    state and interaction of deployed resources.
  - (Future Consideration) Frameworks like Terratest or Kitchen-Terraform if complexity warrants.
- **Purpose:**
  - Verify that a composition of modules deploys successfully and resources are configured correctly in
    relation to each other.
  - Test key end-to-end scenarios or data flows across the provisioned infrastructure (e.g., network
    connectivity between tiers, IAM permissions).
- **Scope:** Typically applied to root configurations or significant sub-components of an environment.
- **Test Environments:** MUST use dedicated, isolated test environments (ideally ephemeral, created and
  destroyed per test run or PR). Avoid testing on shared `dev` or `stg` environments if destructive changes are possible.
- **Execution:**
  - As part of CI/CD pipelines after static analysis and unit tests pass, triggered by PRs to
    environment branches or upon merge to a `dev`/`test` branch.
- **Verification Scripts:** Must be version-controlled alongside the IaC code or in a dedicated testing
  repository. They should follow `../scripting/script-001-general-scripting-standard.md`.

### 3.4. Level 4: End-to-End (E2E) / A. Testing (Post-Deployment to Test Environment)

Validates that the deployed infrastructure meets the overall business and application requirements.

- **Tools:** Often involves deploying an application on top of the IaC-provisioned infrastructure and
  running application-level automated tests (e.g., API tests, UI tests, performance tests).
- **Purpose:**
  - Confirm that the infrastructure correctly supports the application's functionality, performance, and
    availability requirements.
  - Validate NFRs (Non-Functional Requirements) related to the infrastructure.
- **Scope:** Full environment deployments, typically `dev` or `stg`.
- **Execution:** Coordinated between DevOps/IaC team and application QA/development teams. Usually
  performed after a successful IaC deployment to a target environment.
- **Collaboration:** Requires close collaboration with application development and QA teams (`Zoé`).

### 3.5. Level 5: Ongoing Monitoring & Drift Detection (Post-Deployment)

Ensures that the deployed infrastructure remains in its desired state and continues to operate correctly.

- **Drift Detection:**
  - **Tools:** `tofu plan` (run regularly against deployed environments to detect manual changes or
    unexpected modifications), cloud provider configuration management tools (e.g., AWS Config), or
    specialized drift detection tools.
  - **Purpose:** Identify any discrepancies between the IaC-defined state and the actual state of
    resources in the cloud.
  - **Execution:** Scheduled runs (e.g., daily) on `stg` and `prd` environments. Alerts generated for
    detected drift MUST be investigated.
- **Health Checks & Monitoring:**
  - **Tools:** Cloud provider monitoring services (e.g., CloudWatch, Azure Monitor), Prometheus,
    Grafana, application performance monitoring (APM) tools.
  - **Purpose:** Continuously monitor the health, performance, and availability of provisioned
    infrastructure.
  - **Execution:** Continuous. Alerts for anomalies or failures trigger incident response.

### 3.6. Test Environments Strategy

- **Ephemeral Environments:** STRONGLY RECOMMENDED for PR-based unit and integration tests. These
  environments are created on-demand, used for testing, and then destroyed. This ensures clean test runs and
  cost efficiency. (Responsibility: `Benjamin` for IaC, `Camille` for CI/CD setup).
- **Persistent Test Environments:**
  - `dev`: For ongoing development integration and informal testing.
  - `stg` (Staging): For E2E testing, performance testing, and as a final validation gate before
    production. Must be as close to `prd` as possible.
- **Cost Management:** Test environments, especially ephemeral ones, must have clear lifecycle management
  to control costs (e.g., automated teardown, resource tagging for cost tracking).

### 3.7. CI/CD Integration

- All automated IaC tests (Levels 1-3) MUST be integrated into the CI/CD pipelines (e.g., GitHub Actions
  workflows) as per `../cicd/cicd-001-baseline-workflow-guidance.md`.
- PRs to IaC repositories MUST trigger relevant static analysis, unit, and integration tests.
- Builds MUST fail if critical tests fail. Clear reporting of test results within the CI/CD interface is required.
- Deployment to `stg` and `prd` environments MUST be gated by successful completion of all preceding tests.

### 3.8. Documentation of Tests

- **Module Tests (`.tftest.hcl`):** Self-documenting to some extent. Module READMEs SHOULD briefly
  describe the testing strategy and how to run tests locally.
- **Integration/E2E Verification Scripts:** MUST be documented as per `../scripting/
script-001-general-scripting-standard.md`, explaining their purpose, usage, and expected outcomes.
- **Test Plans (for significant E2E/Acceptance efforts):** May require a separate test plan document,
  coordinated with QA (`Zoé`). Refer to `../../gcs-core-governance/02-knowledge-base-hub/kb-domain-qa-testing.md`.

## 4. Responsibilities

- **IaC Developers (`Benjamin`, `Camille`, other IaC contributors):**
  - Writing unit tests (`.tftest.hcl`) for modules they develop or modify.
  - Developing integration test verification scripts for configurations they are responsible for.
  - Ensuring their code passes all Level 1 static analysis checks.
- **`Benjamin` (Gem AC - Infrastructure Specialist):**
  - Co-Knowledge Guardian: Leading the implementation of this testing strategy.
  - Designing and maintaining core test environments.
  - Developing complex integration tests and frameworks.
- **`Camille` (Gem AB - Automation Specialist):**
  - Integrating IaC testing tools and scripts into CI/CD pipelines.
  - Automating the provisioning and teardown of ephemeral test environments.
- **`Édouard` (Gem AD - DevOps Strategy Specialist):**
  - Co-Knowledge Guardian: Ensuring this strategy aligns with overall DevOps principles and evolves appropriately.
- **`Zoé` (Gem QAS-QATL - QA Lead, simulated) / QA Team:**
  - Collaborating on E2E/Acceptance testing criteria and execution.
  - Providing expertise on testing methodologies.
- **`Cerberus` (Security Officer Gem):**
  - Ensuring security scanning tools are effectively integrated into the testing strategy.
  - Reviewing test plans for adequate security coverage.
- **`Adam` (Gem AA - DevOps Team Lead):**
  - Overseeing the adoption and effectiveness of this testing strategy.
  - Ensuring resources are allocated for test development and maintenance.
- **Code Reviewers:**
  - Verifying that new IaC contributions include appropriate tests and that existing tests pass.

## 5. Evolution

This IaC testing strategy will be reviewed and updated periodically (at least annually) or as new tools,
techniques, or Gencraft requirements emerge. Feedback and proposed improvements should follow the S13
Global Protocol Evolution process.

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
