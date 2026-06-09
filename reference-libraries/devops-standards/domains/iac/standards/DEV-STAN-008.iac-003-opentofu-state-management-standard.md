---
docId: DEV-STAN-008
title: Iac 003 Opentofu State Management Standard
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This standard mandates the use of AWS S3 with DynamoDB for OpenTofu state
  management within Gencraft. It emphasizes secure state file storage, locking mechanisms,
  and isolation strategies to ensure integrity, availability, and prevent conflicts,
  crucial for reliable Infrastructure as Code operations.
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - open-tofu
  - state-management
  - aws-s3
  - dynamodb
  - infrastructure-as-code
  - gencraft
  scope: studio
  domain: devops
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/iac/standards/DEV-STAN-008.iac-003-opentofu-state-management-standard.md
---
## 1. Objective

This standard defines the mandatory requirements and best practices for managing OpenTofu state files
within Gencraft. The objectives are to ensure state file security, integrity, availability, and to prevent
concurrent state modifications that can lead to corruption or misconfiguration. Proper state management is
critical for reliable and collaborative Infrastructure as Code (IaC) operations.

## 2. Scope

This standard applies to all OpenTofu configurations and state files managed within the `GenCr-ft` GitHub
organization, for all environments (development, staging, production) and all projects (e.g.,
`gencraft-studio-iac`, `gencraft-game-aethel-iac`).

## 3. Core Principles for State Management

- **Remote State:** Local state files (`terraform.tfstate`) for shared infrastructure are PROHIBITED. All
  OpenTofu state MUST be stored remotely.
- **Security:** State files can contain sensitive information. They MUST be encrypted at rest and access
  to them MUST be strictly controlled.
- **Locking:** State locking MUST be implemented for all remote state backends to prevent concurrent `tofu
apply` operations on the same state.
- **Isolation:** State files SHOULD be isolated per environment (e.g., dev, staging, prod) and per major
  component or service to limit the blast radius of potential state corruption or errors.
- **Versioning:** State file backends MUST support versioning to allow rollback in case of accidental
  corruption (though OpenTofu operations should be the primary way to manage state).
- **Accessibility:** State files MUST be accessible to authorized CI/CD pipelines and authorized personnel/Gems.

## 4. Standard Remote Backend Configuration

### 4.1. Approved Backend Technology

- **Primary Backend:** AWS S3 with DynamoDB for locking is the Gencraft standard remote backend for
  OpenTofu state.

  - **S3 Bucket:** Used for storing the `terraform.tfstate` files.
  - **DynamoDB Table:** Used for state locking and consistency checking.

- **Justification:** Mature, highly available, secure, cost-effective, and well-integrated with OpenTofu.
  Supports encryption and versioning.
- **Alternative Backends:** Use of other backends (e.g., Terraform Cloud, Azure Blob Storage, Google Cloud
  Storage) requires a formal ADR and approval from `Édouard` (Gem AD) AND `Isaac` (Gem SARCH).

### 4.2. S3 Bucket Configuration for State Files

1. **Naming Convention:** `gft-[environment]-[region]-[component]-tfstate` (e.g.,
   `gft-prod-eu-west-3-vpc-tfstate`). A central SSoT for this naming will be in `gcs-core-governance/iac/
IAC_00X_Naming_Conventions.md` (To Be Created by `Édouard`). 2.**Encryption:** Server-Side Encryption with AWS S3-Managed Keys (SSE-S3) or AWS KMS-Managed Keys
   (SSE-KMS) MUST be enabled on the S3 bucket. SSE-KMS is preferred for finer-grained control if required. 3.**Versioning:** S3 bucket versioning MUST be enabled. 4.**Access Control:**
   - IAM policies MUST strictly limit access (read/write) to the S3 bucket and specific state file paths
     to only authorized IAM roles/users (e.g., CI/CD pipeline roles, specific DevOps Gem roles). Principle
     of Least Privilege applies.
   - Public access of any kind MUST be disabled. 5.**Logging:** S3 server access logging MUST be enabled for audit purposes.

### 4.3. DynamoDB Table Configuration for Locking

1. **Naming Convention:** `gft-[environment]-[region]-[component]-tfstate-lock` (e.g.,
   `gft-prod-eu-west-3-vpc-tfstate-lock`). A central SSoT for this naming will be in `gcs-core-governance/
iac/IAC_00X_Naming_Conventions.md` (To Be Created by `Édouard`). 2.**Primary Key:** MUST be `LockID` (String type). 3.**Provisioned Throughput:** Use on-demand capacity mode or provision minimal capacity as locking
   operations are generally infrequent but critical. 4.**Encryption:** Server-Side Encryption MUST be enabled. 5.**Access Control:** IAM policies MUST strictly limit access (read/write on the table items) to
   authorized IAM roles/users.

### 4.4. OpenTofu Backend Configuration (`../../gencraft-iac/environments/github-org/backend.tf`)

- Each root OpenTofu module (typically per environment/component) MUST define its backend configuration in
  a `../../gencraft-iac/environments/github-org/backend.tf` file (or within `main.tf` or a dedicated
  `terraform.tf` block).

- **Example `../../gencraft-iac/environments/github-org/backend.tf` for AWS S3:**

```terraform
  terraform {
    backend "s3" {
      bucket         = "gft-prod-eu-west-3-vpc-tfstate" # Parameterize or use partial config
      key            = "network/vpc.tfstate"            # Path within the bucket
      region         = "eu-west-3"
      dynamodb_table = "gft-prod-eu-west-3-vpc-tfstate-lock"
      encrypt        = true
      # profile        = "shared_credentials_profile" # For local execution, if applicable
      # role_arn       = "arn:aws:iam::ACCOUNT_ID:role/TofuExecutionRole" # For CI/CD
    }
  }
```

- **Parameterization:** Bucket names, keys, regions, and DynamoDB table names SHOULD be parameterized or
  dynamically configured per environment (e.g., using Terragrunt wrappers, partial backend configuration
  with `-backend-config` CLI options in CI/CD, or CI/CD-generated `../../gencraft-iac/environments/
github-org/backend.tf` files for advanced scenarios) to avoid hardcoding and facilitate reuse.
- **Initialization:** `tofu init` will initialize the backend. If migrating existing local state (e.g.,
  from initial local development before shared setup), `tofu init -migrate-state` MUST be used.

## 5. State File Isolation Strategy

1. **Per Environment:** Each distinct deployment environment (e.g., `dev-services`, `staging-game`,
   `prod-core-infra`) MUST have its own set of isolated state files (e.g., separate S3 buckets or distinct
   key prefixes within a shared bucket if access is strictly controlled per prefix via IAM). 2.**Per Major Component/Service:** Within an environment, large or independently managed components (e.
   g., VPC, Kubernetes cluster, main application database, shared monitoring stack) SHOULD have their own
   state files. - **Rationale:** Limits blast radius of potential errors, reduces `tofu plan/apply` times, allows for
   independent team management or ownership. - **Mechanism:** Achieved by having separate root OpenTofu modules (i.e., separate directories with
   their own `../../gencraft-iac/environments/github-org/backend.tf`) for each such component. 3.**Data Sharing Between States:** Use `terraform_remote_state` data source to share outputs between
   isolated states. Access to remote state data sources MUST also be strictly controlled via IAM policies,
   granting read-only access only to the necessary state file paths.

## 6. State Manipulation and Security

1. **Primary Tool:** OpenTofu CLI (`tofu apply`, `tofu destroy`, `tofu import`, `tofu state *`) is the
   ONLY approved method for modifying state files under normal operations. Direct manual editing of state
   files in S3 (or any other backend) is STRICTLY PROHIBITED. 2.**`tofu state` Commands:**
   - Commands like `tofu state mv`, `tofu state rm`, `tofu state replace-provider` are powerful and MUST
     be used with extreme caution.
   - Their usage requires:
     - A documented justification in a GitHub Issue.
     - Peer review of the planned commands and procedure (e.g., via a PR on a script or a documented manual runbook).
     - Approval from at least one senior DevOps Gem (e.g., `Benjamin` or `Adam`).
     - Execution in a controlled manner, with outputs logged.
   - A backup of the state file (see Section 7.3) MUST be taken immediately before executing significant
     `tofu state` manipulations. 3.**Access Control for State Manipulation:**
   - IAM permissions to modify state (via `tofu apply` or `tofu state *`) MUST be more restrictive than
     read-only access and granted only to specific CI/CD pipeline roles and authorized senior DevOps Gems.
   - CI/CD pipelines for `prod` environments applying changes MUST run with specific, tightly-scoped IAM
     roles that have write access only to the relevant state and cloud resources. 4.**Secrets in State:**
   - While OpenTofu attempts to redact sensitive outputs, state files CAN contain sensitive data (e.g.,
     database passwords, API keys if not managed via a separate secrets provider referenced by OpenTofu).
   - This reinforces the critical need for strict S3 bucket encryption (Section 4.2.2) and granular IAM
     access control (Section 4.2.4).
   - Sensitive values SHOULD NEVER be hardcoded in OpenTofu configurations or committed `.tfvars` files.
     They MUST be passed to OpenTofu as variables from a secure secrets manager (e.g., HashiCorp Vault, AWS
     Secrets Manager) at runtime, as per `../security/sec-001-secrets-management-standard.md`
     [gcs-core-governance/security/sec-001-secrets-management-standard.md].

## 7. Backup and Disaster Recovery (DR)

1. **S3 Versioning:** S3 bucket versioning (Section 4.2.3) MUST be enabled and provides the primary
   mechanism for recovering previous state versions. 2.**S3 Replication (Recommended for Production):** For critical production state, cross-region
   replication (CRR) of the S3 state bucket SHOULD be configured to a DR region. 3.**Manual Backups:** Before high-risk operations (e.g., major OpenTofu version upgrade, complex `tofu
state` manipulations, backend migrations), a manual backup of the specific state file(s) from S3 MUST be
   performed and stored securely. 4.**DR Plan (Action for `Benjamin`, `Cerberus`):** The overall DR strategy for IaC state files,
   including recovery procedures and RTO/RPO objectives, MUST be documented in `../dr/
dr-001-backup-restore-strategy.md` (To Be Created).

## 8. Responsibilities

- **`Benjamin` (Gem AC - Infrastructure Specialist):**
  - Implementation, maintenance, and security of the S3/DynamoDB backend infrastructure (provisioned via
    IaC, e.g., from `gencraft-studio-iac`).
  - Defining and enforcing IAM policies for state access, in consultation with `Cerberus`.
  - Managing state file isolation strategies and backend configurations in IaC repositories.
  - Performing or supervising complex `tofu state` manipulations, ensuring procedures are followed.
  - Primary contact for state-related operational issues.
  - Co-authoring and maintaining `../dr/dr-001-backup-restore-strategy.md`.
- **`Édouard` (Gem AD - DevOps Strategy):**
  - Maintenance and evolution of this IAC_003 standard.
  - Approving alternative backend solutions (with `Isaac`).
  - Defining and maintaining `gcs-core-governance/iac/IAC_00X_Naming_Conventions.md` for state
    resources.
- **`Camille` (Gem AB - Automation Specialist):**
  - Ensuring CI/CD pipelines correctly and securely configure and use remote state backends, including
    parameterization and secure authentication methods (e.g., OIDC).
- **`Cerberus` (Security Officer Gem):**
  - Auditing security configurations of S3 buckets and DynamoDB tables used for state.
  - Auditing IAM policies related to state access and ensuring least privilege.
  - Approving security aspects of alternative backend solutions.
  - Co-authoring and approving `../dr/dr-001-backup-restore-strategy.md`.
- **All IaC Contributors (Gems and Humans):**
  - Adherence to this standard when configuring and interacting with OpenTofu backends.
  - NEVER committing local `terraform.tfstate` files for shared infrastructure to Git.
  - Reporting any suspected state file corruption or security issues immediately to `Benjamin` and `Cerberus`.

## 9. References & SSoTs

- OpenTofu Backend Documentation: [https://opentofu.org/docs/language/settings/backends/introduction/](https://opentofu.org/docs/language/settings/backends/introduction/)
- OpenTofu S3 Backend: [https://opentofu.org/docs/language/settings/backends/s3/](https://opentofu.org/docs/language/settings/backends/s3/)
- **Gencraft Standards:**
  - `iac-001-opentofu-tooling-standard.md` [cite: iac_001_opentofu_standard_v1_2_raw_markdown]
  - `iac-004-clean-iac-principles.md` (To Be Created by `Édouard`)
  - `../security/sec-001-secrets-management-standard.md` [gcs-core-governance/security/sec-001-secrets-management-standard.md]
  - `../../gcs-core-governance/02-knowledge-base-hub/02-knowledge-base-hub/kb-domain-security/access-control-policy.md` [gcs-core-governance/02-knowledge-base-hub/02-knowledge-base-hub/kb-domain-security/access-control-policy.md]
  - `../cicd/cicd-001-baseline-workflow-guidance.md` [gcs-core-governance/cicd/CICD_001_Baseline_Workflow_Guidance.md]
- **SSoT Documents (To Be Created/Finalized as part of this standard's implementation):**
  - `gcs-core-governance/iac/IAC_00X_Naming_Conventions.md` (by `Édouard`)
  - `../dr/dr-001-backup-restore-strategy.md` (by `Benjamin`, `Cerberus`)
  - `../scripting/script-001-general-scripting-standard.md` (by `Édouard`)

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
