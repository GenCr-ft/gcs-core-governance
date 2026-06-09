---
docId: DEV-STAN-007
title: Iac 002 Cloud Resource Tagging Standard
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-06-30'
language: en
summary: "**DEPRECATION NOTICE:** The taxonomy and metadata rules previously defined in this document are now obsolete. The official and single source of truth for all studio-wide taxonomy, classification, and metadata rules is now defined in the standard `GOV-STANDARD-008: SSoT Master Taxonomy and Governance Standard`. Please refer to that document for all current definitions and to the `gcs.governance.yml` file for the raw vocabulary data."
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: deprecated
  keywords:
  - cloud-resource-tagging
  - iac
  - gft
  - cost-management
  - automation
  - resource-organization
  scope: studio
  domain: devops
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/iac/standards/DEV-STAN-007.iac-002-cloud-resource-tagging-standard.md
---

**DEPRECATION NOTICE:** The taxonomy and metadata rules previously defined in this document are now obsolete. The official and single source of truth for all studio-wide taxonomy, classification, and metadata rules is now defined in the standard `GOV-STANDARD-008: SSoT Master Taxonomy and Governance Standard`. Please refer to that document for all current definitions and to the `gcs.governance.yml` file for the raw vocabulary data.

## 1. Purpose

This standard defines the mandatory and recommended tagging strategy for all cloud resources provisioned
within <G@FT.ai> Studio's cloud environments (e.g., AWS, Azure, GCP). Consistent and comprehensive tagging
is critical for:

- **Cost Management & Allocation:** Tracking costs by project, environment, service, or owner.
- **Automation:** Enabling automated actions based on tags (e.g., startup/shutdown scripts, backup
  policies).
- **Resource Organization & Discovery:** Simplifying the identification and grouping of related resources.
- **Security & Compliance:** Identifying resources subject to specific security policies or compliance requirements.
- **Operational Management:** Assisting in troubleshooting, monitoring, and incident response.

## 2. Core Principles

1. **Mandatory Tagging:** A defined set of tags **MUST** be applied to all provisionable cloud resources.
2. **IaC Enforcement:** Tags **MUST** be defined and applied via Infrastructure as Code (e.g., Terraform/ OpenTofu configurations within `GenCr-ft/gencraft-iac`). Manual tagging via cloud provider consoles is discouraged and should be corrected by IaC.
3. **Consistency:** Use consistent tag keys and value formats across all resources and services.
4. **Clarity:** Tag values should be clear, concise, and easily understandable.
5. **Lowercase & Hyphens:** Tag keys and values **SHOULD** generally use lowercase letters, numbers, and hyphens (`-`) for separators. Avoid spaces or special characters where possible to ensure compatibility across tools and services.
6. **Automation Focus:** Consider tags that can drive automation (e.g., backup schedules, auto-scaling group identification).
7. **Granularity:** Apply tags at the most granular level appropriate for the resource.

## 3. Standard Tag Keys

The following tag keys are defined. "Mandatory" tags **MUST** be present on all resources where the cloud
provider supports tagging for that resource type. "Recommended" tags **SHOULD** be used where applicable
and beneficial. "Optional" tags can be used for more specific needs.

## 5. Implementation in IaC (Terraform/OpenTofu Example)

Tags should be defined as variables or locals within Terraform/OpenTofu modules and configurations to
ensure they are applied consistently.

**Example (`main.tf` or module variables):**

```terraform
locals {
  common_tags = {
    "gft:environment"   = var.environment # e.g., "dev", "staging", "prod"
    "gft:project"       = "gencraft"
    "gft:owner-team"    = "server-dev-team" # Specific to the module/resource
    "gft:managed-by"    = "iac-gencraft"
    "gft:creation-date" = timestamp() # Or a fixed date for module version
  }
}

resource "aws_instance" "example" {
  ami           = "ami-xxxxxxxxxxxxxxxxx"
  instance_type = "t3.micro"

  tags = merge(
    local.common_tags,
    {
      "gft:service-name"  = "my-example-app-server"
      "gft:instance-role" = "web-server"
      "Name"              = "my-example-app-server-01" # Provider-specific name tag
    }
  )
}
```

### 6. Implementation in IaC (Terraform/OpenTofu Example)

Tags should be defined as variables or locals within Terraform/OpenTofu modules and configurations to
ensure they are applied consistently.

**Example (`main.tf` or module variables):**

```terraform
locals {
  # Common tags applied to most resources within a specific service/component
  service_common_tags = {
    "gft:environment"   = var.environment # e.g., "dev", "staging", "prod" - usually passed from workspace/environment config
    "gft:project"       = "gencraft"      # Could also be a variable if managing multiple projects
    "gft:owner-team"    = "server-dev-team" # Example: This should be specific to the team owning the service
    "gft:managed-by"    = "iac-gencraft"
    "gft:creation-date" = formatdate("YYYY-MM-DD", timestamp()) # Captures apply date, or use a fixed date for module version
  }
}

variable "environment" {
  type        = string
  description = "Deployment environment (e.g., dev, staging, prod)."
}

resource "aws_instance" "example_server" {
  ami           = "ami-xxxxxxxxxxxxxxxxx" # Replace with actual AMI ID
  instance_type = "t3.micro"

  tags = merge(
    local.service_common_tags, # Apply common tags for this service
    {
      # Resource-specific tags
      "gft:service-name"  = "gencraft-auth-service-app"
      "gft:instance-role" = "application-server"
      "Name"              = "gencraft-auth-service-app-<span class="math-inline">\{var\.environment\}\-01" \# Human\-readable name, including environment
"gft\:backup\-policy" \= "daily\-7d\-retention" \# Example recommended tag
\}
\)
\}
resource "aws\_s3\_bucket" "example\_bucket" \{
bucket \= "gencraft\-my\-service\-data\-</span>{var.environment}" # Bucket names must be globally unique

  tags = merge(
    local.service_common_tags, # Apply common tags
    {
      "gft:service-name"     = "gencraft-auth-service-storage"
      "gft:data-sensitivity" = "confidential" # Example recommended tag
      "Name"                 = "gencraft-auth-service-storage-${var.environment}"
    }
  )
}
```

- **Provider-Level Default Tags (Highly Recommended):**
  Where the cloud provider and Terraform/OpenTofu provider support it (e.g., the AWS provider
  `default_tags` block within the `provider` configuration), these **MUST** be used to configure mandatory
  tags that apply to all taggable resources created by that provider instance. This helps ensure baseline
  tagging compliance.

  **Example (in `../../gencraft-iac/environments/github-org/provider.tf` or similar, per environment/workspace):**

```terraform
  variable "aws_region" {
    type        = string
    default     = "eu-west-3" # Example region for G@FT.ai
    description = "AWS region for deployment."
  }

  variable "workspace_environment" {
    type        = string
    description = "Current Terraform workspace environment (e.g., dev, staging, prod). Used for default tags."
    # This variable would typically be set via TF_VAR_workspace_environment in the CI/CD pipeline
    # or derived from `terraform.workspace`.
  }

  provider "aws" {
    region = var.aws_region

    default_tags {
      tags = {
        "gft:environment"   = var.workspace_environment
        "gft:project"       = "gencraft" # This can be a variable if managing multiple distinct projects
        "gft:managed-by"  = "iac-gencraft"
        # Add other tags here that are universally applicable for all resources
        # created by this provider configuration within this workspace.
        # For example, if a cost-center is consistent for an entire AWS account or workspace:
        # "gft:cost-center" = "game-development-main"
      }
    }
  }
```

**Note**: Resource-specific tags explicitly set on a resource will merge with or override
`default_tags` based on standard Terraform merge behavior (resource tags take precedence).

## 7. Governance and Enforcement

- **IaC Reviews (Mandatory):** Tagging consistency and correctness **MUST** be a specific checklist item
  during Pull Request reviews for any changes to the `GenCr-ft/gencraft-iac` repository.
- **Automated Checks (Highly Recommended):**
  - Implement automated checks within the `gencraft-iac` CI/CD pipeline to validate the presence and
    format of mandatory tags on defined resources.
  - Tools like `tfsec`, `checkov`, or Open Policy Agent (OPA) with Rego policies can be used for static
    analysis of Terraform/OpenTofu code to enforce tagging policies _before_ `apply`.
- **Periodic Audits (Recommended):**
  - The DevOps team (Gem C - Ops/Support, guided by Gem D - Strategy) **SHOULD** perform periodic (e.g.,
    quarterly) audits of cloud resources to identify any untagged or incorrectly tagged resources
    (especially those that might have been created outside of the standard IaC process, which should be an
    exception and rare).
  - Discrepancies **MUST** be remediated by bringing the resources under IaC management or correcting
    tags via IaC.
- **Education & Documentation:**
  - This tagging standard **MUST** be communicated to all engineers and teams working with or requesting
    cloud resources.
  - A list of predefined values for common tags (like `gft:environment`, `gft:data-sensitivity`,
    `gft:owner-team`) **SHOULD** be maintained within the `GenCr-ft/devops-standards` repository (e.g., in
    `tag-definitions.md` or a similar reference file) for easy reference by developers and IaC contributors.

## 8. Tagging for Specific Cloud Services

While the general tags apply broadly, some cloud services may have specific tagging needs, limitations, or
propagate tags differently to underlying resources. These specifics should be documented as addendums to
this standard or within service-specific IaC module READMEs.

- **Example: Kubernetes Resources:** If using Kubernetes (e.g., EKS on AWS), apply both Kubernetes
  `labels` (for internal K8s organization, selectors, and potentially cost allocation tools that understand
  K8s labels) and ensure that relevant G@FT tags are propagated to the underlying cloud resources (nodes,
  load balancers, persistent volumes) provisioned for the cluster.
- **Example: Serverless Functions:** Ensure functions and related resources like API Gateways are tagged appropriately.

## 9. Review and Updates

This tagging standard will be reviewed at least annually, or as significant changes in our cloud usage,
tooling, or organizational structure occur. Reviews will be conducted by the DevOps Team (Strategy D,
Infrastructure A) in consultation with Architecture (Gem I) and Finance/PM (especially regarding
cost-related tags). Proposed changes should follow the contribution process for the `GenCr-ft/
gcs-core-governance` repository.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
