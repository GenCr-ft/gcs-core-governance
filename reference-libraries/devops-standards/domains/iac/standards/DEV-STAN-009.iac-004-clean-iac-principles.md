---
docId: DEV-STAN-009
title: Iac 004 Clean Iac Principles
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: "This standard establishes core principles for \u201CClean Infrastructure\
  \ as Code\u201D (IaC) using OpenTofu at Gencraft, emphasizing idempotency, modularity,\
  \ readability, explicit dependencies, and security by design. These principles ensure\
  \ our IaC is understandable, maintainable, and secure."
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - iac-principles
  - clean-iac
  - opentofu
  - infrastructure-as-code
  - security
  - modularity
  - gencraft
  scope: studio
  domain: devops
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/iac/standards/DEV-STAN-009.iac-004-clean-iac-principles.md
---
## 1. Objective

This standard establishes the core principles for writing "Clean Infrastructure as Code" (IaC) using
OpenTofu at Gencraft. Adherence to these principles is mandatory to ensure that our IaC is understandable,
maintainable, scalable, reusable, secure, and reliable. These principles guide both human and AI Gem
contributors in producing high-quality IaC.

## 2. Scope

These principles apply to all OpenTofu code written for any Gencraft project or Gencraft studio
infrastructure, including modules and root configurations stored in repositories such as
gencraft-studio-iac and gencraft-game-aethel-iac as identified by Adam (Gem AA).

## 3. Core Clean IaC Principles

### 3.1. Idempotency

Principle: IaC configurations MUST be idempotent. Applying the same configuration multiple times MUST
result in the same desired state without unintended side effects or errors.

Implementation:

Use OpenTofu resource declarations that inherently manage state (create if not exists, update if changed,
do nothing if already in desired state).

Avoid using null_resource with local-exec or remote-exec provisioners for tasks that are not inherently
idempotent or do not have proper state guards. If provisioners are necessary, ensure their scripts are
idempotent.

Verification: Test plans (see IAC_005_IaC_Testing_Strategy.md) SHOULD include re-application tests.

### 3.2. Modularity & Reusability

Principle: Design IaC in a modular fashion. Create reusable modules for common infrastructure patterns or components.

Implementation:

Module Structure: Modules SHOULD be self-contained, with clearly defined input variables (variables.tf),
outputs (outputs.tf), and resources (main.tf, other .tf files). Each module MUST have a README.md
explaining its purpose, inputs (name, type, description, default, required), outputs, dependencies, and usage examples.

Granularity: Modules SHOULD be granular enough to be reusable but not so small as to create excessive
complexity in composition. Aim for modules that represent a logical unit of infrastructure (e.g., a VPC, a
Kubernetes node pool, an S3 bucket with standard configurations). A balance must be struck to avoid
over-fragmentation.

SSoT for Reusable Modules: Studio-wide reusable modules SHOULD be stored in a dedicated shared repository
(e.g., gencraft-iac-modules) or within the /modules directory of gencraft-studio-iac or
gencraft-game-aethel-iac if their scope is limited to that context.

Versioning: Shared modules MUST be versioned (e.g., using Git tags). Root configurations SHOULD reference
specific versions of shared modules.

Verification: Code reviews MUST assess modularity and potential for reuse.

### 3.3. Readability & Maintainability

Principle: IaC code MUST be easy to read, understand, and maintain by both humans and AI Gems.

Implementation:

Consistent Formatting: Code MUST be formatted using tofu fmt. This WILL BE enforced by pre-commit hooks
(TOOL_004_Git_Hooks_Standard.md [cite: tool_004_git_hooks_standard_v1_3_pure_raw_md]).

Naming Conventions: Adhere to IAC_00X_Naming_Conventions.md (To Be Created) for resources, variables,
outputs, and modules. Names SHOULD be descriptive and consistent.

Comments: Use comments (# or //) to explain complex logic, non-obvious configurations, or important
decisions. description attributes in variables and outputs MUST be used.

Organization: Group related resources logically within files or directories. Avoid overly large .tf files.

Minimize Complexity: Avoid overly complex expressions, nested conditional logic, or excessive use of count
and for_each where simpler constructs suffice. Prioritize clarity.

Verification: Code reviews are the primary mechanism. TFLint (see iac-007-iac-static-analysis-standard.md)
can help enforce some aspects.

### 3.4. Explicit Dependencies & No Hardcoding

Principle: Make dependencies between resources and modules explicit. Avoid hardcoding values that are
likely to change or are environment-specific.

Implementation:

Resource Dependencies: Rely on OpenTofu's implicit dependency graphing. Use depends_on sparingly and only
when necessary for non-obvious dependencies or to manage dependencies involving provisioners.

Variables: Use input variables for all configurable parameters (e.g., instance sizes, CIDR blocks,
environment names). Provide sensible defaults where appropriate. Variable definitions MUST include type,
description, and optionally validation rules.

Data Sources: Use data sources (e.g., aws_ami, terraform_remote_state) to fetch information dynamically
rather than hardcoding it.

Outputs: Expose necessary information from modules via outputs. Output definitions MUST include a
description.

No Magic Strings/Numbers: Use variables or local values for repeated strings or numbers that have a specific meaning.

Verification: Code reviews. TFLint can detect some hardcoded values or missing variable descriptions.

### 3.5. Security by Design (Secure Defaults)

Principle: Security considerations MUST be integrated into IaC from the outset. Modules and configurations
SHOULD implement secure defaults.

Implementation:

Least Privilege: IAM roles and policies defined in IaC MUST adhere to the principle of least privilege.

Encryption: Enable encryption at rest and in transit for resources where applicable and Gencraft data
classification requires it (e.g., S3 buckets, EBS volumes, RDS instances, ELB listeners).

Network Security: Implement restrictive security groups and network ACLs by default. Avoid overly
permissive rules (e.g., 0.0.0.0/0 for ingress unless explicitly justified for a public-facing service and
approved by Cerberus).

Secrets Management: Sensitive data (passwords, API keys) MUST NOT be stored in IaC code or state files.
Use a secrets manager as per sec-001-secrets-management-standard.md [gcs-core-governance/security/
sec-001-secrets-management-standard.md] and reference secrets dynamically (e.g., via data sources or
environment variables in CI that are themselves secrets).

Regular Scanning: IaC code MUST be scanned for security vulnerabilities using tools like TFSec (or
approved alternative, see iac-007-iac-static-analysis-standard.md [cite:
iac_static_analysis_standard_v1_1_and_report]).

Verification: TFSec (or alternative) scans, code reviews with Cerberus (Security Officer Gem) involvement
for critical infrastructure and security-sensitive resources.

### 3.6. Testability

Principle: IaC code SHOULD be designed with testability in mind to ensure reliability and correctness.

Implementation:

Modular Design (see 3.2): Smaller, focused modules with well-defined interfaces are easier to test independently.

Input Parameterization (see 3.4): Allows for testing modules and configurations with different valid and invalid inputs.

Clear Outputs (see 3.4): Facilitates verification of created resources and their attributes.

Strategy: Follow devops-standards/iac/IAC_005_IaC_Testing_Strategy.md (To Be Created) which will define
approaches for linting, validation, unit testing (e.g., with terraform test or other frameworks), contract
testing, integration testing, and end-to-end testing for IaC.

Verification: Adherence to IAC_005_IaC_Testing_Strategy.md, code reviews focusing on testability.

### 3.7. Version Control (Git)

Principle: All IaC code, including module definitions, configurations, and non-sensitive variable files (.
tfvars), MUST be stored in Git.

Implementation:

Follow GH_002_Branching_Strategy_Standard.md [cite: devops_standard_gh_002_branching_strategy_v1].

Use Conventional Commits (TOOL_001_Conventional_Commits_Standard.md [gcs-core-governance/tooling/
TOOL_001_Conventional_Commits_Standard.md]).

Use Git hooks for local validation (TOOL_004_Git_Hooks_Standard.md [cite:
tool_004_git_hooks_standard_v1_3_pure_raw_md]).

.tfstate files MUST NOT be committed to Git (managed by remote backend as per
IAC_003_IaC_State_Management_Standard.md).

Sensitive .tfvars files containing secrets MUST NOT be committed. Use environment-specific, non-committed .
auto.tfvars files populated from a secrets manager or CI/CD variables that are themselves secrets.
Non-sensitive default .tfvars (e.g., variables.tfvars.example) MAY be committed.

Verification: Code reviews, CI pipeline checks (e.g., for committed state files or secrets).

### 3.8. Documentation

Principle: IaC code MUST be well-documented to facilitate understanding, usage, and maintenance.

Implementation:

Module READMEs: Every reusable module MUST have a README.md detailing its purpose, input variables (name,
type, description, default value, whether required), outputs (name, description, sensitivity),
dependencies on other modules or providers, and clear usage examples. Tools like terraform-docs MAY be
used to help generate and maintain this documentation.

Root Configuration READMEs: Each root configuration (e.g., per environment/component) SHOULD have a README.
md explaining its purpose, high-level architecture, and how to apply it.

Inline Comments: Use comments (# or //) within .tf files to explain complex logic, non-obvious
configurations, or important design decisions.

Variable and Output Descriptions: The description attribute MUST be comprehensively filled for all input
variables and outputs.

Verification: Code reviews MUST check for documentation quality and completeness. TFLint rules (e.g.,
terraform_documented_variables, terraform_documented_outputs from IAC_007 [cite:
iac_static_analysis_standard_v1_1_and_report]) will enforce descriptions.

### 3.9. Environment Parity & Promotion

Principle: Strive for maximum parity between environments (e.g., dev, staging, prod) in terms of how
infrastructure is defined and provisioned. Configurations SHOULD be the primary differentiator, not the
code itself.

Implementation:

Use the same IaC modules and resource definitions across environments.

Manage environment-specific configurations (e.g., instance sizes, counts, feature flags, domain names) via
input variables and dedicated, environment-specific .tfvars files (or equivalent configuration management
for CI/CD, ensuring secrets are handled securely).

Promote IaC changes through environments (e.g., Dev -> Staging -> Prod) using a consistent, auditable CI/
CD process as defined in CICD_001_Baseline_Workflow_Guidance.md [gcs-core-governance/cicd/
CICD_001_Baseline_Workflow_Guidance.md] and CICD_003_Deployment_Strategies.md [gcs-core-governance/cicd/
CICD_003_Deployment_Strategies.md].

Verification: Review of deployment processes, environment configurations, and the IaC code structure for
reusability across environments.

### 3.10. Minimal Blast Radius

Principle: Structure IaC configurations to limit the potential impact (blast radius) of an error,
misconfiguration, or failed deployment.

Implementation:

State Isolation (see IAC_003_IaC_State_Management_Standard.md [cite:
iac_003_state_management_standard_v1_2_raw]): Strictly isolate state per environment and per major,
independently deployable component.

Smaller, Focused Root Configurations: Prefer multiple smaller root OpenTofu configurations (each managing
a distinct set of resources or a component) over a single monolithic configuration for an entire
environment or application.

Phased Rollouts & Progressive Delivery: For large or critical changes, consider strategies for phased
rollouts (e.g., blue/green, canary for application infrastructure if supported) as detailed in
CICD_003_Deployment_Strategies.md [gcs-core-governance/cicd/CICD_003_Deployment_Strategies.md].

Verification: Architectural reviews, review of state isolation strategy, and deployment plans for major changes.

## 4. Responsibilities

Édouard (Gem AD - DevOps Strategy):

Maintenance and evolution of this IAC_004 standard.

Promoting these principles across all IaC development and training initiatives.

Benjamin (Gem AC - Infrastructure Specialist):

Championing and implementing these principles in core infrastructure IaC.

Providing guidance, mentorship, and reviewing IaC contributions for adherence to these principles.

Developing and maintaining SSoT for reusable IaC modules.

Isaac (Gem SARCH - Software Architect):

Ensuring architectural decisions for applications and services facilitate adherence to these IaC
principles (e.g., designing for modular deployment).

Cerberus (Security Officer Gem):

Ensuring the "Security by Design" principle (3.5) is correctly interpreted, implemented, and audited across all IaC.

Reviewing IaC for security best practices.

All IaC Contributors (Gems and Humans):

Understanding, internalizing, and applying these principles in all IaC development.

Actively participating in code reviews to uphold these principles.

Raising questions or proposing improvements to these principles via Issues in devops-standards (using
knowledge-proposal-template.md [gcs-core-governance/02-knowledge-base-hub/Templates/Issue-Templates/
knowledge-proposal-template.md]).

## 5. Enforcement & Verification

Code Reviews (Protocol S1 [gcs-core-governance/01-operational-protocols/s1-feedback-approval.md]):
Mandatory for all IaC changes. Reviewers MUST explicitly check for adherence to these Clean IaC
Principles. A PR checklist item referencing this standard SHOULD be used.

Static Analysis (iac-007-iac-static-analysis-standard.md [cite:
iac_static_analysis_standard_v1_1_and_report]): Tools like TFLint and TFSec (or approved alternative) WILL
BE configured to enforce many of these principles automatically (e.g., formatting, naming conventions via
custom rules, security misconfigurations, use of descriptions).

Git Hooks (TOOL_004_Git_Hooks_Standard.md [cite: tool_004_git_hooks_standard_v1_3_pure_raw_md]): Local
pre-commit hooks WILL enforce formatting, basic linting, and secret scanning before code is committed.

CI/CD Pipelines (CICD_001_Baseline_Workflow_Guidance.md [gcs-core-governance/cicd/
CICD_001_Baseline_Workflow_Guidance.md]): Pipelines WILL run comprehensive static analysis, validation,
and potentially automated IaC tests. Non-compliance with critical principles (as detected by tools) MUST
fail the pipeline.

AI Gem Assistance: AI Gems (Véra for quality, or specialized IaC review Gems) MAY be developed or prompted
to assist in reviewing IaC against these principles or generating IaC code that adheres to them.

## 6. References & SSoTs

IAC_001_OpenTofu_Tooling_Standard.md

IAC_003_IaC_State_Management_Standard.md

iac-007-iac-static-analysis-standard.md

TOOL_001_Conventional_Commits_Standard.md [gcs-core-governance/tooling/
TOOL_001_Conventional_Commits_Standard.md]

TOOL_004_Git_Hooks_Standard.md [cite: tool_004_git_hooks_standard_v1_3_pure_raw_md]

sec-001-secrets-management-standard.md [gcs-core-governance/security/sec-001-secrets-management-standard.md]

CICD_001_Baseline_Workflow_Guidance.md [gcs-core-governance/cicd/CICD_001_Baseline_Workflow_Guidance.md]

CICD_003_Deployment_Strategies.md [gcs-core-governance/cicd/CICD_003_Deployment_Strategies.md]

GH_002_Branching_Strategy_Standard.md [cite: devops_standard_gh_002_branching_strategy_v1]

SSoT Documents (To Be Created/Finalized):

devops-standards/iac/IAC_00X_Naming_Conventions.md (by Édouard)

devops-standards/iac/IAC_005_IaC_Testing_Strategy.md (by Édouard, Benjamin)

gencraft-iac-modules/ (Conceptual SSoT repository for shared modules, if adopted - decision by Édouard, Isaac)

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
