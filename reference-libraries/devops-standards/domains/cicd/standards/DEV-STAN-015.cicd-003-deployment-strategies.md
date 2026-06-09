---
docId: DEV-STAN-015
title: Cicd 003 Deployment Strategies
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This document outlines standard deployment strategies for applications within
  the G@FT.ai Studio, emphasizing automation, immutability, and infrastructure as
  code. It details approved strategies like rolling updates, blue/green deployments,
  and canary releases, alongside key principles for minimizing downtime, reducing
  risk, and ensuring reliable deployments.
last_updated_date: '2026-06-02'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - cicd-deployment-strategies
  - technical-writing
  - devops
  - gft-ai
  - infrastructure-as-code
  - blue-green-deployment
  - canary-release
  - rolling-update
  scope: studio
  domain: devops
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/cicd/standards/DEV-STAN-015.cicd-003-deployment-strategies.md
---
## 1. Purpose

This document outlines the standard principles and high-level strategies for deploying applications and
services within the <G@FT.ai> Studio. Effective deployment strategies are crucial for:

- **Minimizing Downtime:** Ensuring services remain available during updates.
- **Reducing Risk:** Allowing for safe rollouts and quick rollbacks if issues occur.
- **Predictability & Reliability:** Making deployments consistent and dependable.
- **Speed & Agility:** Enabling frequent updates to deliver value faster.
- **User Experience:** Minimizing disruption to users during updates.

This document provides a conceptual framework. Specific implementation details will depend on the target
environment (e.g., Kubernetes, AWS ECS, Serverless, Game Server Hosting Platform) and will be detailed in
environment-specific IaC configurations and deployment scripts.

## 2. Core Deployment Principles

All deployment processes and strategies **MUST** adhere to the following principles:

1. **Automation:** Deployments **MUST** be fully automated via CI/CD pipelines. Manual deployments to
   Staging and Production environments are strongly discouraged and require explicit justification. 2.**Immutability:** Strive for immutable infrastructure and deployments. Instead of updating existing
   servers/containers in place, deploy new versions and switch traffic. 3.**Infrastructure as Code (IaC):** All target infrastructure supporting deployments (e.g., compute
   instances, load balancers, service configurations) **MUST** be managed via IaC (`GenCr-ft/gencraft-iac`). 4.**Environment Parity:** Aim for consistency between Staging and Production environments to ensure
   testing accurately reflects production behavior. Dev environments may differ more significantly for cost/speed. 5.**Zero-Downtime (Goal):** For user-facing services, deployment strategies **SHOULD** aim for zero or
   minimal perceived downtime. 6.**Progressive Exposure:** For significant changes or new features, consider strategies that
   progressively expose the new version to users (e.g., Canary, Feature Flags). 7.**Monitoring & Validation:** Deployments **MUST** be followed by automated health checks and
   monitoring to quickly detect issues. Key performance indicators (KPIs) should be tracked post-deployment. 8.**Rollback Capability:** All deployment strategies **MUST** include a clear, tested, and preferably
   automated rollback plan. 9.**Security:** Deployment processes **MUST** be secure, managing secrets appropriately and ensuring
   images/artifacts are scanned and verified.

## 3. Standard Environments

<G@FT.ai> will utilize the following standard environments. Deployments **MUST** typically progress through
these environments in sequence.

- **Development (`dev`):**
  - Purpose: For developers to deploy and test their features in an integrated environment. Can be more
    dynamic and less stable.
  - Deployment Trigger: Often automated on merge to `main` or feature branches.
- **Staging (`staging` or `qa`):**
  - Purpose: For formal QA testing, user acceptance testing (UAT), and pre-production validation. Should
    closely mirror Production.
  - Deployment Trigger: Automated or manually triggered promotion from `dev` (e.g., after `main` branch
    builds that have passed initial tests).
- **Production (`prod`):**
  - Purpose: Live environment accessible to end-users.
  - Deployment Trigger: **MUST** be manually triggered or require explicit approval after successful
    validation in Staging. Deployments should ideally occur during off-peak hours or announced maintenance
    windows if downtime is unavoidable.

## 4. Common Deployment Strategies (Overview & Applicability)

The choice of deployment strategy will depend on the service's criticality, architecture, and risk
tolerance. The following strategies are approved for consideration. Specific selection and implementation
will be an architectural decision, implemented by DevOps (Gems A, B).

### 4.1. Rolling Update

- **Description:** Gradually replaces instances of the old version with instances of the new version, one
  by one or in batches. Load balancers direct traffic away from instances being updated.
- **Pros:** Simple to implement, resource-efficient (no need to double capacity).
- **Cons:** Rollback can be slow if issues are detected late. Can have a period where both old and new
  versions are running, potentially causing compatibility issues if not handled carefully. Brief downtime
  for individual instances during update.
- **Applicability:** Suitable for stateless services, backend services where temporary mixed versions are
  acceptable, or when minimal downtime per instance is tolerable. Good for initial MVP services.

### 4.2. Blue/Green Deployment (Red/Black Deployment)

- **Description:** Two identical production environments are maintained: "Blue" (current live) and "Green"
  (new version). Traffic is switched from Blue to Green once Green is fully tested and ready. Blue is kept
  on standby for quick rollback.
- **Pros:** Near zero-downtime switchover, instant rollback by switching traffic back to Blue. Testing can
  be done on the full Green environment before exposing it to users.
- **Cons:** Requires doubling infrastructure resources (potentially costly, though temporary). Can be
  complex to manage database schema changes or stateful services.
- **Applicability:** Excellent for critical applications where downtime is unacceptable and instant
  rollback is essential. Suitable for web applications, APIs, and potentially game server fleets.

### 4.3. Canary Release

- **Description:** The new version is rolled out to a small subset of users/servers first. If it performs
  well (based on monitoring key metrics), the rollout is gradually expanded to the entire user base.
- **Pros:** Allows for testing in production with real users but limited blast radius. Early detection of
  issues. Gradual performance impact.
- **Cons:** More complex to set up and manage (requires sophisticated traffic routing and monitoring). Can
  be slower to roll out fully.
- **Applicability:** Ideal for user-facing applications where new features need to be tested for
  performance, stability, and user acceptance with minimal risk. Good for large-scale services.

### 4.4. Feature Flags (Feature Toggles)

- **Description:** Deploy new features to production in a "dark" or "off" state, then enable (toggle) them
  for specific users, user groups, or a percentage of users independently of code deployments.
- **Pros:** Decouples feature releases from code deployments. Allows for A/B testing, phased rollouts, and
  quick disabling of features if issues arise. Reduces risk per deployment.
- **Cons:** Adds complexity to the codebase (managing flags). Requires a robust feature flag management
  system. Can lead to "flag debt" if flags are not cleaned up.
- **Applicability:** Very powerful for user-facing features, A_B testing, and managing risk of new
  functionality. Complements other deployment strategies.

### 4.5. Recreate (Big Bang - To be used with caution)

- **Description:** The old version is stopped, and the new version is deployed.
- **Pros:** Simple to understand.
- **Cons:** Incurs downtime. Rollback involves redeploying the old version. High risk.
- **Applicability:** **Generally discouraged for Production.** May be acceptable for some non-critical
  internal tools, very early-stage dev environments, or scenarios where scheduled downtime is permissible and understood.

## 5. Deployment Automation & Tooling

- **CI/CD Pipeline:** Deployments **MUST** be orchestrated by the CI/CD pipeline (GitHub Actions).
- **IaC:** Infrastructure changes associated with a deployment (e.g., new server configurations, load
  balancer rules) **MUST** be managed via `GenCr-ft/gencraft-iac`.
- **Configuration Management:** Application configuration (distinct from infrastructure) **MUST** be
  managed externally from the application artifact (e.g., environment variables, config files deployed
  separately, services like AWS AppConfig or HashiCorp Consul). Secrets **MUST** be managed via a secure
  secret store (e.g., HashiCorp Vault, AWS Secrets Manager).
- **Health Checks & Monitoring:** Automated health checks **MUST** be part of the deployment process to
  validate a new version. Comprehensive monitoring and alerting **MUST** be in place to detect issues
  post-deployment.

## 6. Environment Promotion Workflow

1. **Build & Test:** Code is built and tested in CI (PR/feature branch). 2.**Merge to `main`:** Upon successful review and CI, code is merged to `main`. 3.**Deploy to `dev` (Optional Auto):** An artifact from `main` _may_ be automatically deployed to the
   `dev` environment for integration testing. 4.**Promote to `staging`:** A specific, versioned artifact (e.g., from a `main` build or a release
   candidate branch) is deployed to `staging`. This step often requires manual approval or trigger. 5.**Validate in `staging`:** Thorough QA, UAT, and performance testing occurs in `staging`. 6.**Promote to `prod`:** After successful validation in `staging` and explicit approval (e.g., from
   Producer/PM, QA Lead, Tech Lead), the same versioned artifact is deployed to `prod` using the chosen
   deployment strategy. 7.**Post-Deployment Monitoring:** Closely monitor production environment.

## 7. Game Specific Deployments (Client & Server)

- **Game Client:**
  - Updates may be delivered via platform stores (Steam, Epic, mobile stores) or a custom launcher.
  - Strategies like phased rollouts (if supported by the platform) are recommended.
  - Versioning is critical for compatibility with server versions.
- **Game Server:**
  - Fleets of game servers may require rolling updates or blue/green deployments to maintain session availability.
  - State management for active game sessions during deployment is a key challenge (e.g., session
    draining, state migration if possible).
  - Matchmaking services must be aware of server versions.

Detailed deployment strategies for specific components (e.g., `gcp-aethel-client`, `gcp-aethel-server-core`,
individual microservices) will be documented in their respective architectural plans or deployment
runbooks, adhering to the principles and options outlined in this standard.

## 8. Review and Updates

This standard provides a high-level framework. It will be reviewed and updated as our project evolves, our
infrastructure matures, and new best practices emerge. Specific implementation details for each service/
application will be documented in ADRs or service-specific design documents.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
