---
docId: DEV-STAN-004
title: FF-001 Feature Flag Standard
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This standard establishes a governed approach for using feature flags within
  Gencraft applications, services, and configurations. It outlines objectives like
  decoupling code deployment, enabling trunk-based development, and providing operational
  control through kill switches. The standard emphasizes consistent implementation,
  management, and a defined lifecycle for flags.
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - feature-flagging
  - gencraft
  - standards
  - development
  - release-management
  - operations
  - testing
  scope: studio
  domain: devops
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/engineering/standards/DEV-STAN-004.ff-001-feature-flag-standard.md
---
## 1. Objective

This standard establishes a consistent and governed approach for using feature flags (also known as
feature toggles) within Gencraft applications, services, and potentially infrastructure configurations.
The objectives are to:

- **Decouple Code Deployment from Feature Release:** Allow code to be deployed to production environments
  frequently and safely, even if features are not yet ready for all users.
- **Enable Trunk-Based Development:** Minimize the use of long-lived feature branches by integrating code
  into the main trunk behind feature flags.
- **Facilitate Progressive Delivery:** Enable strategies like canary releases, dark launches, ring
  deployments, and A/B testing.
- **Provide Operational Control (Kill Switches):** Allow for the rapid disabling of problematic features
  in production without requiring a new deployment or rollback.
- **Manage Technical Debt:** Ensure flags have a defined lifecycle, including a process for removal.
- **Standardize Implementation:** Promote consistent implementation and management of flags across Gencraft.

## 2. Scope

This standard applies to:

- All new features developed for Gencraft applications and services where the benefits of flagging (e.g.,
  risk reduction, phased rollout) are identified.
- Significant refactoring or re-architecture efforts that might benefit from being flagged.
- Both backend services and client-side applications (including game clients).
- Potentially, conditional IaC configurations if managed via a compatible flagging mechanism.
- All Gencraft Gems (human and AI) involved in software development, release management, QA, and
  operations.

## 3. Standard

### 3.1. Core Principles of Feature Flagging

- **Purposeful Implementation:** Flags should be introduced with a clear purpose and an expected lifecycle.
- **Granularity:** Flags should control well-defined, discrete units of functionality. Avoid overly broad
  flags that hide too many unrelated changes.
- **Minimal Performance Impact:** The flag evaluation mechanism should be highly performant and not
  introduce significant latency.
- **Testability:** Code controlled by feature flags MUST be testable with the flag in all its relevant
  states (on, off, specific variations).
- **Central Management (Logical):** While implementation can be distributed, the definition, state, and
  lifecycle of flags should be managed or at least cataloged centrally for visibility and governance.
- **Security:** The feature flag system itself, and the configurations it manages, must be secure.

### 3.2. Types of Feature Flags (Categorization)

Gencraft recognizes the following primary categories of feature flags. Naming conventions (Section 3.4)
should reflect these categories.

- **Release Toggles (`release_`):**
  - **Purpose:** To enable or disable new features for a controlled rollout to production. Allows code
    to be deployed before the feature is ready for all users.
  - **Lifecycle:** Typically short to medium-lived. They MUST be removed once the feature is fully
    rolled out to 100% of the target audience and considered stable.
- **Experiment Toggles (`experiment_` or `ab_`):**
  - **Purpose:** To conduct A/B tests or other experiments by exposing different feature variations to
    different user segments simultaneously.
  - **Lifecycle:** Short-lived, tied to the duration of the experiment. They MUST be removed once the
    experiment concludes and a winning variation is chosen (or the feature is discarded).
- **Operational Toggles (`ops_` or `killswitch_`):**
  - **Purpose:** To quickly disable or degrade a feature in production in response to operational
    issues, high error rates, or performance degradation. Acts as a "kill switch".
  - **Lifecycle:** Can be permanent (as a safety mechanism for volatile features) but regularly
    reviewed, or temporary until the underlying issue is resolved. If temporary, a plan for a permanent
    fix or removal of the toggle is needed.
- **Permission Toggles (`permission_` or `access_`):**
  - **Purpose:** To control access to specific features based on user roles, entitlements, subscription
    tiers, or other user attributes (e.g., beta program members, internal users).
  - **Lifecycle:** Can be long-lived, as they are part of the ongoing access control model for features.

### 3.3. Feature Flag Management System

- **Selected System/Framework:**
  - _(Decision Pending - This section will be updated via an ADR once a specific tool/framework like
    Unleash, Flagsmith, LaunchDarkly, or a custom Gencraft solution is selected and approved. `Édouard`
    and `Isaac` to lead this selection process.)_
  - **Interim Principle:** If no central system is yet in place, feature flags may be implemented using
    simple, version-controlled configuration files (e.g., JSON, YAML) deployed alongside the application,
    or environment variables. This approach is suitable for a small number of simple flags but does not
    scale well for dynamic control or complex targeting. Any such interim solution MUST be approved by
    `Isaac` and `Cerberus`.
- **Configuration Storage & SSoT:**
  - Regardless of the system, the SSoT for flag definitions (name, description, type, possible values,
    default state, owner, intended lifecycle) MUST be maintained. This could be the flag management
    system's UI/API, or a version-controlled document if a simpler system is used.
  - Flag configurations for different environments (dev, stg, prd) MUST be managed separately and
    securely.
- **SDKs/Client Libraries:** Applications will use approved SDKs or client libraries to interact with the
  feature flag system. These libraries should provide:
  - Efficient flag evaluation (local caching with updates).
  - Default/fallback values if the system is unavailable.
  - Contextual evaluation (based on user ID, session attributes, etc.).

### 3.4. Naming Conventions for Flags

- **Format:** `<type_prefix>_<scope_or_feature_name>_<specific_aspect>`
- **Case:** `snake_case` (all lowercase).
- **`<type_prefix>`:**
  - `release_` (for Release Toggles)
  - `exp_` (for Experiment Toggles)
  - `ops_` (for Operational Toggles/Kill Switches)
  - `perm_` (for Permission Toggles)
- **`<scope_or_feature_name>`:** Descriptive name of the feature or system area being controlled (e.g.,
  `new_dashboard`, `user_profile_v2`, `realtime_notifications`).
- **`<specific_aspect>`:** (Optional) Further clarifies what the flag controls if the feature is complex
  (e.g., `enable_graph_view`, `use_new_algorithm`).

- **Examples:**
  - `release_new_dashboard_enable_widget_x`
  - `exp_search_results_use_semantic_ranking`
  - `ops_payment_gateway_disable_provider_b`
  - `perm_advanced_analytics_show_to_premium_users`

### 3.5. Implementation Guidelines

- **Granularity:** Design flags to control a single, logical piece of functionality.
- **Code Integration:**
  - Flag checks should be simple conditional statements (e.g., `if featureIsEnabled('my_feature_flag')
: ...`).
  - Avoid deeply nested conditional logic based on flags. Consider using strategy patterns or dependency
    injection to select different implementations based on flag state for more complex scenarios.
  - Ensure code paths for both "on" and "off" states are maintained and tested.
- **Default State:** Every flag MUST have a defined default state (typically "off" or the current
  production behavior) that is applied if the flag configuration cannot be fetched or evaluated.
- **Dynamic vs. Static Evaluation:** Prefer systems that allow dynamic updates to flag states without
  requiring application redeployment. If using static configuration files, these must be part of the
  deployment artifact.

### 3.6. Lifecycle Management of Feature Flags

1. **Creation:**
   - A new feature flag request SHOULD be part of the feature's design/planning phase.
   - The request MUST define: flag name (per convention), type, purpose, intended users/scope, expected
     lifecycle/TTL, owner (Tech Lead/Product Manager), and default state.
   - `Isaac` or a delegated architect/Tech Lead, in consultation with `Édouard` and `Cerberus` (for
     security/permission flags), approves the creation of new flags. 2.**Rollout Strategy:**
   - Defined by the feature owner, aligned with `../cicd/cicd-003-deployment-strategies.md`.
   - Examples: Internal Gencraft users first, then a small percentage of external users (canary), then
     gradual increase. 3.**Monitoring:**
   - The impact of enabling/disabling a feature flag (or its variations for experiments) MUST be
     monitored using application metrics, logs, and business KPIs.
   - Define success metrics for features rolled out via flags. 4.**Cleanup (Technical Debt Removal - MANDATORY):**
   - **Release Toggles & Experiment Toggles:** Once a feature is fully rolled out and stable, or an
     experiment is concluded, the associated flag(s) AND the dead code paths MUST be removed from the codebase.
   - **Defined TTL/Review:** Each flag (especially `release_` and `exp_`) MUST have an intended
     Time-To-Live (TTL) or a scheduled review date for removal. This should be tracked (e.g., in the flag
     definition SSoT or a dedicated issue). Default TTL for release flags: 1-2 sprints after 100% rollout.
     Default TTL for experiment flags: duration of experiment + 1 sprint.
   - **Process for Removal:** A dedicated task/issue MUST be created for removing each flag. This work
     should be prioritized to prevent accumulation of stale flags. `Adam` and Tech Leads are responsible
     for ensuring this cleanup happens.
   - `Ops_` and `Perm_` toggles may be long-lived but must be reviewed at least semi-annually for
     continued necessity and correctness.

### 3.7. Testing with Feature Flags

- Applications MUST be testable with feature flags in their different states.
- **Unit & Integration Tests:** Should cover code paths for both enabled and disabled flag states. Test
  frameworks should allow for easy mocking or setting of flag states.
- **End-to-End (E2E) Tests:** CI/CD pipelines SHOULD support running E2E tests against different flag
  configurations (e.g., all new features on, specific experiments active).
- QA (`Zoé` or QA team) must be aware of active feature flags and their impact on test plans.

### 3.8. Security Considerations

- **Flag Management System Security:** Access to the feature flag management system/configuration MUST be
  strictly controlled as per `../../gcs-core-governance/02-knowledge-base-hub/02-knowledge-base-hub/
kb-domain-security/access-control-policy.md`. Changes to flag states (especially in production) MUST be
  auditable (who, what, when).
- **Sensitive Operations:** Avoid using easily manipulated feature flags to control access to highly
  sensitive operations or data if not part of a robust `perm_` toggle design reviewed by `Cerberus`.
- **Flag Evaluation Logic:** Ensure that the client-side evaluation of flags (if applicable) cannot be
  easily tampered with by end-users to gain unauthorized feature access. Server-side evaluation is generally
  preferred for critical flags.
- **No Secrets in Flag Configuration:** Flag names or targeting attributes should not expose sensitive data.

### 3.9. Actionability for AI Gems

- **Querying Flag States:** AI Gems involved in automated testing or deployment verification might need to
  query the state of specific flags for a given context (user, environment).
- **Setting Flag States (Test Environments):** AI Gems might need to enable/disable flags in
  non-production environments to facilitate specific test scenarios. This requires secure programmatic
  access.
- **Code Generation:** AI Gems generating application code must be aware of how to correctly implement
- feature flag checks according to this standard.

## 4. Responsibilities

- **Feature Owners (Product Managers, Tech Leads):**
  - Defining the need for a feature flag and its intended behavior/lifecycle.
  - Defining rollout strategies and success metrics.
  - Requesting the removal of obsolete flags.
- **Development Teams (including AI Gems if they code):**
  - Implementing features behind flags according to this standard.
  - Writing tests for all flag states.
  - Removing flag-related code once a flag is obsolete.
- **`Isaac` (Gem SARCH - Software Architect) & Tech Leads:**
  - Approving the introduction of new feature flags from an architectural perspective.
  - Guiding teams on best practices for integrating flags into the codebase.
- **`Édouard` (Gem AD - DevOps Strategy Specialist):**
  - Co-Knowledge Guardian: Maintaining and evolving this standard.
  - Leading the selection/design of the feature flag management system.
- **`Camille` (Gem AB - Automation Specialist):**
  - Integrating feature flag management into CI/CD pipelines (e.g., for testing different
    configurations).
- **`Adam` (Gem AA - DevOps Team Lead):**
  - Overseeing the operational aspects of feature flagging.
  - Ensuring processes for flag review and cleanup are followed.
- **`Cerberus` (Security Officer Gem):**
  - Reviewing and approving security-sensitive flags (e.g., `perm_` toggles).
  - Ensuring the security of the flag management system and processes.
- **QA Team (`Zoé` or delegates):**
  - Developing test strategies that account for feature flags and their different states.

## 5. Review and Evolution

This standard will be reviewed at least annually or as new requirements and technologies emerge. Proposed
changes should follow the S13 Global Protocol Evolution process.

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
