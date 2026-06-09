---
docId: DEV-STAN-010
title: Iac 005 Iac Resource Naming Conventions
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: "**DEPRECATION NOTICE:** The taxonomy and metadata rules previously defined in this document are now obsolete. The official and single source of truth for all studio-wide taxonomy, classification, and metadata rules is now defined in the standard `GOV-STANDARD-008: SSoT Master Taxonomy and Governance Standard`. Please refer to that document for all current definitions and to the `gcs.governance.yml` file for the raw vocabulary data."
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: deprecated
  keywords:
  - iac-naming-convention
  - cloud-resource-naming
  - terraform-naming
  - gencraft-standards
  - infrastructure-as-code
  - open-tofu
  - resource-naming-pattern
  scope: studio
  domain: devops
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/iac/standards/DEV-STAN-010.iac-005-iac-resource-naming-conventions.md
---

**DEPRECATION NOTICE:** The taxonomy and metadata rules previously defined in this document are now obsolete. The official and single source of truth for all studio-wide taxonomy, classification, and metadata rules is now defined in the standard `GOV-STANDARD-008: SSoT Master Taxonomy and Governance Standard`. Please refer to that document for all current definitions and to the `gcs.governance.yml` file for the raw vocabulary data.

## 1. Objective

This standard establishes a consistent and predictable naming convention for all cloud resources
provisioned via Infrastructure as Code (IaC) using OpenTofu within Gencraft. The objectives are to:

- Facilitate easy identification and understanding of resources by both humans and AI Gems.
- Improve resource management, filtering, and organization.
- Enable effective automation, scripting, and monitoring.
- Support accurate cost allocation and tracking through consistent naming in conjunction with tagging
  (`iac-002-cloud-resource-tagging-standard.md`).
- Minimize ambiguity and naming conflicts.

## 2. Scope

This standard applies to:

- The `Name` tag and any other primary naming attributes (e.g., identifiers, resource-specific name
  fields) of all cloud resources created and managed by OpenTofu.
- All Gencraft IaC repositories (e.g., `gencraft-studio-iac`, `gencraft-game-aethel-iac`).
- All Gencraft Gems and human contributors involved in IaC development and operations.

This standard primarily governs the names of resources as they appear in the cloud provider console and
APIs. For OpenTofu _logical resource names_ within `.tf` files, see section 3.3.

## 3. Standard Naming Conventions

### 3.1. General Principles

- **Case:** All resource names and name components MUST be **lowercase**.
- **Separators:** Hyphens (`-`) MUST be used as separators between components in a resource name.
  Underscores (`_`) are generally reserved for OpenTofu logical names or provider-specific internal naming.
- **Character Set:** Names MUST consist of alphanumeric characters (`a-z`, `0-9`) and hyphens (`-`). Avoid
  special characters not universally accepted by cloud providers.
- **Meaningful Components:** Each component of the name should be descriptive and add clear contextual
  information. Use Gencraft-approved abbreviations where defined (see `tag-definitions.md` for some codes).
- **Clarity over Brevity:** While names should not be excessively long, clarity of purpose is paramount.
  Adhere to cloud provider name length limitations (e.g., S3 buckets, IAM roles often have specific limits).
- **Uniqueness:** Ensure names are unique within their required scope (e.g., globally unique for S3
  buckets, unique within a region/VPC for others). The naming pattern should inherently promote uniqueness.

### 3.2. Cloud Resource Naming Pattern

The standard pattern for cloud resource names (typically applied to the `Name` tag) is:

**DEPRECATION NOTICE:** The taxonomy and metadata rules previously defined in this document are now obsolete. The official and single source of truth for all studio-wide taxonomy, classification, and metadata rules is now defined in the standard `GOV-STANDARD-008: SSoT Master Taxonomy and Governance Standard`. Please refer to that document for all current definitions and to the `gcs.governance.yml` file for the raw vocabulary data.

### 3.3. OpenTofu Logical Resource Names (within `.tf` files)

OpenTofu logical resource names (e.g., `my_s3_bucket` in `resource "aws_s3_bucket" "my_s3_bucket"`) are
scoped to the module they are defined in.

- **Case:** MUST be `lower_snake_case`.
- **Clarity:** Names SHOULD be descriptive of the resource's purpose _within that module's context_.
- **Pattern:** `<purpose_or_type_abbrev>_<description>`
  - Examples: `main_vpc`, `public_subnets`, `allow_ssh_sg`, `app_server_iam_role`, `website_bucket`.
- **Modules:** When instantiating a module, the local name for the module block SHOULD be descriptive of
  the module's instance or purpose.
  Example:

```terraform
module "production_vpc" {
    source = "../modules/vpc"
    # ... other variables
   }
```

### 3.4. Constructing Names in Modules

Reusable OpenTofu modules SHOULD allow for name components to be passed in as variables to construct full
cloud resource names according to this standard.

- Modules SHOULD accept variables like `project_code`, `environment_code`, `component_name`,
  `custom_name_suffix`, etc.
- Modules internally assemble the final name using these inputs.
  Example (conceptual inside a module):

```terraform
    resource "aws_s3_bucket" "this" {
      bucket = "gft-${var.project_code}-${var.environment_code}-${var.component_name}-${var.purpose}-${var.custom_name_suffix}"
      # ...
    }
```

The `Name` tag would also be constructed similarly.

### 3.5. Specific Resource Type Considerations (Examples)

While the general pattern applies, some resource types have specific constraints or common practices.

- **IAM Roles:** `gft-<project>-<env>-iam-<purpose>-role`
- **IAM Policies:** `gft-<project>-<env>-iam-<purpose>-policy`
- **Security Groups:** `gft-<project>-<env>-<component>-<purpose>-sg`
- **S3 Buckets:** Must be globally unique.
  `gft-<project_code_or_account_alias>-<env_code>-<purpose_or_component>
[-<region_if_meaningful_for_uniqueness_pattern>]` (e.g., `gft-aethel-prd-analytics-query-results-euw1`).
  Often, the `gft` prefix and account/project identifier help ensure global uniqueness.
- **VPCs:** `gft-<project>-<env>-<region>-vpc`
- **Subnets:** `gft-<project>-<env>-<region>-<vpc_name_short>-<type_and_az>-subnet` (e.g.,
  `gft-aethel-dev-euw1-main-priv-az1-subnet`)
- **EC2 Instances (if manually named, often auto-scaled):**
  `gft-<project>-<env>-<region>-<component>-<role>[-<id>]`

Always check cloud provider documentation for specific character limits and restrictions for each resource type.

### 3.6. Tagging Interaction

- The `Name` tag MUST follow this naming convention.
- Other tags defined in `iac-002-cloud-resource-tagging-standard.md` will provide additional structured
  metadata. This naming convention makes the `Name` tag human-readable and filterable.

### 3.7. Enforcement and Validation

- **Code Reviews:** Adherence to these naming conventions MUST be checked during IaC Pull Request reviews
  (as per Protocol S1).
- **Linters (Future):** Where possible, custom TFLint rules (or similar static analysis checks) MAY be
  developed to validate resource names against this standard. This is a future enhancement goal.
- **Module Design:** Reusable modules SHOULD be designed to enforce or simplify the application of these naming conventions.

## 4. Responsibilities

- **IaC Developers (All Gems contributing to IaC):**
  - MUST adhere to this standard when naming new cloud resources and OpenTofu logical resources.
  - SHOULD update existing resource names to comply during refactoring or significant updates, where feasible and safe.
- **`Benjamin` (Gem AC - Infrastructure Specialist):**
  - Co-Knowledge Guardian of this standard.
  - Championing the implementation and providing guidance on these conventions.
  - Leading efforts to refactor existing names where critical.
- **`Édouard` (Gem AD - DevOps Strategy Specialist):**
  - Co-Knowledge Guardian of this standard.
  - Ensuring this standard aligns with overall DevOps and IaC strategy.
  - Maintaining the SSoT for project codes, environment codes, and region codes (likely in `tag-definitions.md`).
- **Module Authors:**
  - Ensuring their modules facilitate the creation of names compliant with this standard.
- **Reviewers of IaC PRs:**
  - Verifying compliance with this naming standard.

## 5. Evolution

This standard will be reviewed periodically and updated as Gencraft's infrastructure પાણી_needs evolve or
new cloud services are adopted. Proposed changes should follow the S13 Global Protocol Evolution process.

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
