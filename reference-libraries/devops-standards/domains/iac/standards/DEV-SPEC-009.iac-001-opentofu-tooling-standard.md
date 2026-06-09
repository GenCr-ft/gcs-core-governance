---
docId: DEV-SPEC-009
title: Iac 001 Opentofu Tooling Standard
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: "This standard defines the Gencraft studio\u2019s official tooling, versioning,\
  \ and environment configuration for Infrastructure as Code (IaC) development using\
  \ OpenTofu. It ensures consistency across all IaC projects, simplifies onboarding,\
  \ and maintains a secure IaC development lifecycle."
last_updated_date: '2026-06-02'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - iac
  - opentofu
  - infrastructure-as-code
  - tooling
  - environment-standard
  - terraform
  - genco
  scope: studio
  domain: devops
  doc-type: specification
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/iac/standards/DEV-SPEC-009.iac-001-opentofu-tooling-standard.md
---
## 1. Objective

This standard defines the Gencraft studio's official tooling, versioning, and environment configuration
for Infrastructure as Code (IaC) development using OpenTofu. The objectives are to ensure consistency
across all IaC projects, simplify onboarding, facilitate automation, and maintain a secure and stable IaC
development lifecycle. This standard is critical for the successful execution of PROJ-103 [cite:
devops_transformation_plan_proj103] and ongoing IaC operations.

## 2. Scope

This standard applies to:

- All Gencraft Gems and human contributors involved in writing, reviewing, or executing OpenTofu code.
- All local development environments where OpenTofu code is authored or tested.
- All CI/CD pipelines that execute OpenTofu commands.
- All Gencraft repositories containing OpenTofu code (e.g., `gencraft-studio-iac`,
  `gencraft-game-aethel-iac`).

## 3. Standard Tool: OpenTofu

### 3.1. Official IaC Tool

- **Tool:** OpenTofu ([https://opentofu.org/](https://opentofu.org/)) IS THE MANDATORY IaC tool for
  provisioning and managing infrastructure at Gencraft.

- **Justification:** Open Source (aligns with UOP 2.7 [gcs-core-governance/
  00-studio-vision-and-principles/universal-gem-operating-principles.md]), Terraform-compatible syntax and
  ecosystem, active community support, and a commitment to remaining a truly open-source project.

### 3.2. Versioning

1. **Studio Standard Version (Action for `Édouard` - Gem AD):**

   - A specific version of OpenTofu (MAJOR.MINOR) MUST be declared as the studio-wide standard. This
     version will be the target for all development and CI/CD environments.
   - **Current Standard Version:** OpenTofu `v1.6.x` (Patch versions within the `1.6` minor release are
     generally acceptable, but CI will use a pinned patch version).
   - **SSoT for Version:** This standard (IAC_001) and the `validate_gft_devops_environment_proj103.sh`
     script [cite: devops_env_validation_script_proj103] will reflect the current standard version. 2.**Updating the Standard Version:**
   - Proposals to update the studio standard OpenTofu version MUST be submitted as an ADR (Architectural
     Decision Record) or an update to this standard, led by `Édouard` (Gem AD).
   - The proposal MUST include justification, impact analysis (especially on existing IaC code and CI/CD
     pipelines), and a migration plan if necessary.
   - Approval by the Governance Crew (or designated technical council) is required. 3.**Repository-Level Pinning:**

   - Each IaC repository MUST specify the required OpenTofu version in its root `../../gencraft-iac/
environments/github-org/versions.tf` file using a pessimistic version constraint that aligns with the
     studio standard minor version.
   - **Example `../../gencraft-iac/environments/github-org/versions.tf`:**

   ```terraform
     terraform {
       required_version = "~> 1.6.0" // Allows 1.6.0, 1.6.1, etc., but not 1.7.0 or 2.0.0

       required_providers {
         # Provider versions also pinned here
         aws = {
           source  = "hashicorp/aws"
           version = "~> 5.30" # Example, SSoT for provider versions to be defined
         }
         github = {
           source  = "integrations/github"
           version = "~> 5.40" # Example
         }
       }
     }
   ```

   - **SSoT for Provider Versions (Action for `Édouard` - Gem AD):** A central document,
     `gcs-core-governance/iac/IAC_00X_Provider_Versioning_Standard.md` (To Be Created), will list approved
     versions for commonly used providers.

### 3.3. Local Development Environment Setup

1. **Mandatory Guide & Script (Action for `Benjamin` - Gem AC):**
   - A standardized guide for setting up a local OpenTofu development environment MUST be maintained.
   - **SSoT Guide:** `gcs-core-governance/guides/setup_opuntofu_local_env_v2.md` (To Be Created by `Benjamin`).
   - An automation script to facilitate this setup MUST be provided and maintained.
   - **SSoT Script:** `gencraft-iac/scripts/environment-setup/initialize_gft_tofu_workspace.sh` (To
     Be Created — tracked in GenCr-ft/gencraft-iac). 2.**Contents of Standard Setup:** The guide and script MUST ensure the installation of:
   - The Gencraft standard version of OpenTofu.
   - `TFLint` (as per `iac-007-iac-static-analysis-standard.md` [cite:
     iac_static_analysis_standard_v1_1_and_report]).
   - `TFSec` (or approved alternative, as per `IAC_007` and `SEC_00X_IaC_Scanning_Tool_Selection.md`).
   - `pre-commit` framework and standard Gencraft Git hooks (as per `../tooling/
tool-004-git-hooks-standard.md` [cite: tool_004_git_hooks_standard_v1_3_pure_raw_md]).
   - `jq` for JSON parsing.
   - Any other essential helper tools. 3.**Verification:** The `validate_gft_devops_environment_proj103.sh` script [cite:
     devops_env_validation_script_proj103] MUST be used by contributors to verify their local environment
     conforms to these requirements.

### 3.4. CI/CD Environment Configuration

1. **Consistency (Action for `Camille` - Gem AB):** CI/CD environments (e.g., GitHub Actions runners)
   executing OpenTofu commands MUST use the exact same Gencraft standard version of OpenTofu as defined in
   Section 3.2.1. 2.**Tooling:** CI/CD environments MUST have `TFLint`, `TFSec` (or alternative), and `jq` available. 3.**Authentication:** Authentication of OpenTofu to cloud providers in CI/CD MUST use secure,
   short-lived credentials managed via mechanisms like OIDC with the cloud provider, or secrets managed as
   per `../security/sec-001-secrets-management-standard.md` [gcs-core-governance/security/
   sec-001-secrets-management-standard.md]. Static, long-lived credentials in CI environment variables are PROHIBITED.

### 3.5. OpenTofu Wrapper Scripts (Optional)

- **Purpose:** For complex or frequently repeated sequences of OpenTofu commands, wrapper scripts MAY be developed.
- **SSoT for Wrapper Scripts:** `gencraft-iac/scripts/tofu-wrappers/` (To Be Populated as needed).
- These scripts MUST adhere to `../scripting/script-001-general-scripting-standard.md` and clearly
  document their purpose, parameters, and any environment assumptions.

## 4. Responsibilities

- **`Édouard` (Gem AD - DevOps Strategy):**
  - Maintenance and evolution of this IAC_001 standard.
  - Defining and updating the studio standard OpenTofu version.
  - Defining and maintaining `IAC_00X_Provider_Versioning_Standard.md`.
- **`Benjamin` (Gem AC - Infrastructure Specialist):**
  - Creation and maintenance of the SSoT local environment setup guide (`setup_opuntofu_local_env_v2.md`).
  - Creation and maintenance of the SSoT setup script (`initialize_gft_tofu_workspace.sh`).
  - Ensuring IaC repositories correctly pin OpenTofu and provider versions.
  - Developing SSoT OpenTofu wrapper scripts if deemed necessary.
- **`Camille` (Gem AB - Automation Specialist):**
  - Ensuring CI/CD environments use the standard OpenTofu version and have required tools.
  - Developing SSoT OpenTofu wrapper scripts if deemed necessary.
- **All IaC Contributors (Gems and Humans):**
  - Adherence to this standard, including using the correct OpenTofu version and a properly configured
    local environment.
  - Using the `validate_gft_devops_environment_proj103.sh` script [cite:
    devops_env_validation_script_proj103] to check their environment.

## 5. References & SSoTs

- OpenTofu Official Documentation: [https://opentofu.org/docs/](https://opentofu.org/docs/)
- `validate_gft_devops_environment_proj103.sh` [cite: devops_env_validation_script_proj103]
- **SSoT Documents (To Be Created/Finalized as part of this standard's implementation):**
  - `gcs-core-governance/guides/setup_opuntofu_local_env_v2.md` (by `Benjamin`)
  - `gencraft-iac/scripts/environment-setup/initialize_gft_tofu_workspace.sh` (canonical home: GenCr-ft/gencraft-iac)
  - `gcs-core-governance/iac/IAC_00X_Provider_Versioning_Standard.md` (by `Édouard`)
  - `gencraft-iac/scripts/tofu-wrappers/` (canonical home: GenCr-ft/gencraft-iac)
- **Related Gencraft Standards:**
  - `iac-004-clean-iac-principles.md`
  - `iac-007-iac-static-analysis-standard.md` [cite: iac_static_analysis_standard_v1_1_and_report]
  - `../tooling/tool-004-git-hooks-standard.md` [cite: tool_004_git_hooks_standard_v1_3_pure_raw_md]
  - `../security/sec-001-secrets-management-standard.md` [gcs-core-governance/security/
    sec-001-secrets-management-standard.md]
  - `../scripting/script-001-general-scripting-standard.md`

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
