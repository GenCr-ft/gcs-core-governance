---
docId: SEC-STAN-001
title: SEC 001 Secrets Management Standard
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This standard outlines policies and procedures for managing secrets within
  G@FT.ai Studio, emphasizing centralized secure storage, least privilege access,
  encryption, auditing, and regular rotation. Secrets MUST NOT be hardcoded or committed
  to source control. The primary recommended solution is HashiCorp Vault or a cloud
  provider native secrets manager (e.g., AWS Secrets Manager), with strong emphasis
  on using OIDC for authentication and avoiding direct secret storage in IaC.
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - secrets-management
  - security
  - vault
  - aws-secrets-manager
  - ci-cd
  - iac
  - encryption
  - access-control
  - gft-ai
  scope: studio
  domain: security
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/security/standards/SEC-STAN-001.sec-001-secrets-management-standard.md
---
## 1. Purpose

This standard defines the policies, procedures, and recommended tooling for managing secrets within <G@FT.
ai> Studio. Secrets include any sensitive information that grants access to resources or data, such as:

- API keys and tokens (cloud provider, third-party services)
- Database credentials (usernames, passwords)
- Private cryptographic keys (TLS/SSL certificates, SSH keys, signing keys)
- Sensitive configuration parameters
- OAuth client secrets

Effective secrets management is crucial for protecting our intellectual property, user data,
infrastructure, and overall operational security. **Under no circumstances should secrets be hardcoded
into source code, committed to Git repositories, or logged in plain text.**

## 2. Core Principles

1. **Centralized Secure Storage:** Secrets **MUST** be stored in a dedicated, secure, and audited secrets management solution. 2.**Least Privilege:** Applications, services, and users **MUST** only be granted access to the specific
   secrets they absolutely require to perform their functions. 3.**Encryption at Rest and In Transit:** Secrets **MUST** be encrypted both when stored (at rest) and
   when transmitted (in transit). 4.**Auditing:** Access to secrets and changes to secrets **MUST** be auditable. 5.**Rotation:** Secrets (especially passwords, API keys, and certificates) **SHOULD** be rotated
   regularly or upon suspicion of compromise. Automated rotation is preferred where possible. 6.**Ephemeral Secrets:** Prefer short-lived, dynamically generated secrets over long-lived static secrets where feasible. 7.**No Secrets in Git:** Repeating for emphasis: **Secrets MUST NOT be committed to any Git repository**,
   including private ones. Use `.gitignore` to prevent accidental commits of secret files. 8.**Infrastructure as Code (IaC) for Secrets Management Infrastructure:** The infrastructure for the
   secrets management solution itself (e.g., Vault cluster, IAM roles for cloud secret managers) **MUST** be
   managed via IaC (`GenCr-ft/gencraft-iac`). The secrets _themselves_ are not stored in IaC. 9.**Separation of Duties:** Access to manage the secrets store **SHOULD** be restricted to a minimal set
   of authorized personnel (e.g., DevOps Team, specific security roles).

## 3. Recommended Secrets Management Solutions

The choice of a secrets management solution depends on the context (application, infrastructure, CI/CD).
The following are approved for consideration and use within <G@FT.ai>:

### 3.1. Primary Recommended Solution: Dedicated Secrets Manager

- **Tool Recommendation:** **HashiCorp Vault (Open Source or Cloud offering)** or a **Cloud Provider
  Native Solution (e.g., AWS Secrets Manager, Google Secret Manager, Azure Key Vault)**.
  - **HashiCorp Vault:**
    - _Pros:_ Feature-rich, platform-agnostic, strong encryption, dynamic secrets, fine-grained access
      control, audit logs, OSS option provides control.
    - _Cons:_ Self-hosting the OSS version requires significant operational overhead for setup,
      maintenance, HA, and backups. Vault Cloud can mitigate this.
  - **Cloud Provider Native Solutions (e.g., AWS Secrets Manager):**
    - _Pros:_ Managed service (reduced operational overhead), good integration with other cloud services,
      IAM-based access control, often cost-effective for basic use.
    - _Cons:_ Tied to a specific cloud provider. May have fewer advanced features than Vault for some use cases.
- **Decision Criteria:** The choice between Vault and a cloud-native solution will be made based on an ADR
  considering factors like complexity, feature requirements (e.g., dynamic secrets for databases),
  cross-cloud needs, operational capacity, and cost for specific use cases. **For <G@FT.ai>'s current
  primary cloud (assumed AWS based on `gencraft-iac` backend), AWS Secrets Manager is a strong default
  candidate for application and IaC secrets.**

### 3.2. CI/CD Pipeline Secrets

- **GitHub Actions Encrypted Secrets:**
  - **Usage:** For secrets required by GitHub Actions workflows (e.g., cloud provider credentials for
    deployment, API keys for third-party service integration during CI/CD).
  - **Scope:** Secrets can be defined at the organization, repository, or environment level. Use the narrowest scope necessary.
  - **Management:** Managed through the GitHub UI or programmatically via the GitHub API (which can be
    wrapped by IaC for _some_ aspects like organization secrets, though repository-level secrets are often
    managed directly).
  - **Security:** GitHub encrypts these secrets. Access to configure them should be tightly controlled.
  - **OIDC Preferred:** For authenticating to cloud providers (AWS, Azure, GCP) from GitHub Actions, **IAM
    OIDC Connectors MUST be preferred** over static access keys stored as GitHub secrets (see Section 3.2 of
    CICD-003). This allows workflows to assume roles with short-lived credentials.

### 3.3. Local Development Environment Secrets

- **`.env` Files (Git Ignored):** For local development, connection strings or API keys can be stored in `.
env` files at the root of a project. These files **MUST** be listed in the project's `.gitignore` file and
  **NEVER** committed to the repository. Developers are responsible for managing their local `.env` files.
- **Project-Specific Secret Stores:** Some projects may use local instances of tools like Vault Docker
  containers for more sophisticated local secret management.
- **IDE/OS Keychain:** For very sensitive personal access tokens, developers may use their IDE's secure
  storage or the operating system's keychain.

## 4. Accessing Secrets

### 4.1. Applications & Services

- Applications **MUST NOT** read secrets directly from environment variables in production if a dedicated
  secrets manager is available and appropriate for the secret type.
- **Recommended Pattern:**
  1. The application/service authenticates to the secrets management solution (e.g., Vault, AWS Secrets
     Manager) using a secure identity mechanism (e.g., IAM role for EC2/ECS/Lambda, Kubernetes service
     account identity).
     2.The application retrieves secrets at runtime as needed.
     3.Retrieved secrets should be cached in memory for a short duration if appropriate, but not written to disk or logs.
- For simpler configurations or where a full secrets manager is overkill, secrets might be injected as
  environment variables from a secure source by the deployment orchestrator (e.g., Kubernetes secrets, ECS
  task definition secrets injected from AWS Secrets Manager).

### 4.2. Infrastructure as Code (IaC)

- IaC code (Terraform/OpenTofu in `GenCr-ft/gencraft-iac`) **MUST NOT** have secrets hardcoded or committed.
- **Recommended Pattern:**
  1. Use data sources within Terraform/OpenTofu to fetch secrets at `plan` or `apply` time directly from
     the secrets management solution (e.g., `aws_secretsmanager_secret_version` data source,
     `vault_generic_secret` data source).
     2.The CI/CD pipeline executing the IaC **MUST** have an identity (e.g., an IAM role via OIDC) with
     the necessary permissions to read these secrets from the store.

### 4.3. CI/CD Pipelines

- Secrets required during CI/CD (e.g., for deploying, publishing artifacts) **MUST** be provided via
  GitHub Actions Encrypted Secrets or dynamically fetched using OIDC if interacting with cloud services.

## 5. Secret Rotation

- **Policy:** Define rotation policies for different types of secrets.
  - High-privilege credentials (e.g., database root passwords, cloud admin keys - though these should
    rarely be used by apps): Rotate frequently (e.g., every 90 days or less).
  - API Keys: Rotate according to vendor recommendations or at least annually.
  - Certificates: Rotate well before expiration.
- **Automation:** Automate secret rotation where possible using features of the secrets management
  solution (e.g., AWS Secrets Manager can rotate RDS credentials).
- **Emergency Rotation:** A clear procedure **MUST** be in place for immediate rotation of any secret suspected of compromise.

## 6. Auditing

- The chosen secrets management solution **MUST** provide audit logs of who accessed or modified which secrets and when.
- These logs **SHOULD** be ingested into a central logging/SIEM solution (if available) for monitoring and
  alerting on suspicious activity.
- Regular (e.g., quarterly) reviews of access patterns and audit logs **SHOULD** be conducted by the DevOps/Security team.

## 7. Training and Awareness

- All <G@FT.ai> Studio members who handle code or infrastructure **MUST** be trained on this Secrets
  Management Standard and general security best practices.
- Emphasize the importance of not sharing secrets, not committing them to Git, and reporting any suspected compromises immediately.

## 8. Handling a Suspected Compromise

1. **Identify & Contain:** Determine the scope of the suspected compromise. 2.**Rotate:** Immediately rotate the suspected compromised secret(s). 3.**Revoke:** Revoke any access granted by the old secret(s). 4.**Investigate:** Understand how the compromise occurred. 5.**Remediate:** Address the root cause to prevent recurrence. 6.**Report:** Report the incident according to <G@FT.ai>'s incident response plan (to be developed).

## 9. Review and Updates

This standard is a living document and will be reviewed at least annually, or as new threats, tools, or
best practices emerge. Updates will be managed via PRs to the `GenCr-ft/devops-standards` repository.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
