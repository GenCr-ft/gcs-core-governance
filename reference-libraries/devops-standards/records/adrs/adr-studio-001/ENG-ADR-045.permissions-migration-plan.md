---
docId: ENG-ADR-045
title: Permissions Migration Plan
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This document outlines a GitHub permissions migration plan for the adr-studio-001.md
  implementation, aiming to establish a standardized, role-based access control system
  based on the principle of least privilege. It details the target state, including
  GitHub Team structure, repository categories, and default permission levels, to
  ensure secure and scalable access management.
last_updated_date: '2026-05-20'
metadata:
  lifecycle-stage: draft
  keywords:
  - github-permissions
  - access-control
  - migration
  - role-based-access-control
  - devops
  - security
  - adrs
  - studio-organization
  scope: studio
  domain: devops
  doc-type: adr
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/records/adrs/adr-studio-001/ENG-ADR-045.permissions-migration-plan.md
---
## 1. Objective

This document outlines the comprehensive plan for defining, implementing, and migrating GitHub permissions for repositories and GitHub Teams within the `GenCr-ft` organization. This plan aligns with the repository restructuring and Role-Based Access Control (RBAC) strategy defined in `adr-studio-001.md` as part of PROJ-103.

The primary goals are:

- To establish a clear, standardized, and secure permissions model rooted in the **principle of least privilege**.
- To ensure access is granted only as necessary for individuals to perform their assigned duties, considering repository sensitivity as defined in `../../gcs-core-governance/02-knowledge-base-hub/kb-domain-security/information-classification-and-handling-policy.md`.
- To facilitate scalable and auditable permissions management, with a clear strategy for transitioning to Infrastructure as Code (IaC).
- To ensure all studio members have appropriate access while robustly protecting sensitive code, configurations, and data.

## 2. Current State Overview

The pre-migration state of GitHub permissions within `GenCr-ft` was largely unstandardized, characterized by a mix of direct user access grants to repositories and inconsistently defined or overly broad GitHub Teams. This plan aims to rectify this by implementing a structured, role-based system.

## 3. Target State: Permissions Model (Post-Migration)

The target state will adhere to the principles outlined in `adr-studio-001.md` and the `../../gcs-core-governance/02-knowledge-base-hub/02-knowledge-base-hub/kb-domain-security/access-control-policy.md`.

### 3.1. GitHub Teams

- **Team Structure:** GitHub Teams will be the primary mechanism for granting access. Teams will generally
  be mapped from the functional Crews and key Roles defined in `../../gcs-core-governance/
00-studio-vision-and-principles/studio-organization-and-roles.md`.
- **Naming Convention for GitHub Teams:** `team-<crew_or_role_identifier>[-<specialization_or_project>]`
  (e.g., `team-devops-admins`, `team-developers-projectphoenix`, `team-developers-projectphoenix-leads`,
  `team-artists-characters`, `team-external-projectphoenix-vendorX`). This uses the `team-` prefix for
  clarity and automation.
- **Membership:** Assignment to GitHub Teams will be based on an individual's active role and project
  assignments. Changes will follow the Access Request Process (see Section 6.3).
- **Default Organization Role for New Members:** New members invited to the `GenCr-ft` GitHub organization
  will have `No access` by default to any repositories until explicitly added to the relevant GitHub Team
  (s). They may be added to a default `team-all-members-readonly` granting read access to a very limited set
  of public/internal informational repositories (e.g., `gcs-core-governance`).

### 3.2. Repository Categories and Default GitHub Team Permissions

Repository categories (e.g., `gcs-`, `gci-`, `gcp-`) are defined by `adr-studio-001.md`. The following
matrix outlines baseline permission levels. Specific repository needs, data classification (Confidential,
Restricted, Internal, Public), or project requirements may necessitate approved deviations.

| GitHub Team (`team-<name>`)          | Repo Category Example(s)                                          | Default GitHub Permission | Justification / Notes                                                                                                                                        |
| :----------------------------------- | :---------------------------------------------------------------- | :------------------------ | :----------------------------------------------------------------------------------------------------------------------------------------------------------- |
| `team-devops-superadmins`            | All; especially `gci-*` (IaC), `gcd-*` (DevOps Auto)              | `admin`                   | For critical infrastructure, org-level configurations, emergency overrides. Highly restricted membership, dual authorization for changes if possible.        |
| `team-devops`                        | `gci-*`, `gcd-*`                                                  | `maintain`                | Manage DevOps repositories, CI/CD, IaC tools, and their settings.                                                                                            |
| `team-devops`                        | Other categories (e.g., `gcp-*`, `gcl-*`)                         | `read` / `triage`         | View code, manage issues for support purposes. `write` on specific utility/tooling repos they own or actively contribute to.                                 |
| `team-security-officers` (Cerberus)  | All                                                               | `admin`                   | Full access for security audits, configuration management, incident response, enforcing security policies. Membership aligned with Security Officer role(s). |
| `team-knowledge-guardians` (Lexicon) | `gcs-core-governance`, documentation repos/dirs                   | `admin` / `maintain`      | Manage SSoT, handbook, documentation standards.                                                                                                              |
| `team-management`                    | Most project oversight repos; read-only on most technical         | `maintain` / `read`       | Oversight and reporting. `maintain` on high-level project/summary repos, `read` on most technical implementation repos.                                      |
| `team-developers-<project>-leads`    | `gcp-<project>-*`, owned `gcl-<projectlibrary>-*`                 | `maintain`                | Manage project repository settings (webhooks, labels, milestones), PR merges, release drafts, branch protections (within policy).                            |
| `team-developers-<project>`          | `gcp-<project>-*`, owned `gcl-<projectlibrary>-*`                 | `write`                   | Day-to-day development: push to feature branches, create/manage PRs, resolve discussions.                                                                    |
| `team-artists-<specialty>-<project>` | Specific project asset repos (e.g., `gcp-<project>-assets`)       | `write`                   | Contribute and manage assets for their specialty within assigned projects.                                                                                   |
| `team-qa-<project>`                  | `gcp-<project>-*`, test plan repos                                | `triage` / `write`        | Report issues, manage test cases. `write` access to test-specific branches or dedicated test artifact repositories if needed.                                |
| `team-all-members-readonly`          | `gcs-core-governance`, selected `gcs-` public/internal info repos | `read`                    | Default access for all authenticated organization members to essential studio information.                                                                   |
| `team-external-<project>-<vendor>`   | Specific `gcp-<project>-subcomponent` or defined paths            | `read` or `write`         | Highly scoped, time-limited access for external collaborators, approved via formal process. Access reviewed regularly and revoked upon contract end.         |

- **GitHub Permission Levels Used (in ascending order of privilege):**
  - `read`: Recommended for most users on repositories outside their direct contribution scope. Allows
    pulling code, viewing issues/PRs/wikis, and commenting.
  - `triage`: `read` + ability to manage issues and PRs (labels, assignees, milestones, closing/
    reopening). Suitable for QA, PMs on repos they don't write code for.
  - `write`: `triage` + ability to push to non-protected branches, create branches, manage PRs
    (including merging if branch protections allow), manage own work. Standard for contributors on their
    active repositories.
  - `maintain`: `write` + ability to manage repository settings (topics, collaborators, some branch
    protections), manage releases, push to protected branches (only if explicitly allowed outside of PRs,
    rare). Suitable for tech leads, primary maintainers of a repository.
  - `admin`: `maintain` + full control including managing access directly on the repo (discouraged,
    prefer team-based IaC), deleting the repository, changing visibility. Highly restricted; primarily for
    `team-devops-superadmins` on specific infrastructure repositories or `team-security-officers`.

### 3.3. Branch Protections

- Branch protection rules will be strictly enforced as per `gh-001.1-branching-strategy-and-protection.md`
  and `adr-studio-001.md`.
- Key protections for `main` and `develop` branches (and other designated protected branches) include:
  required PR reviews (e.g., from CODEOWNERS or a minimum number of reviewers), required status checks to
  pass, and restriction of direct pushes.
- "Allow force pushes" and "Allow deletions" for protected branches will be **disabled** for all users,
  except potentially for a highly restricted `team-devops-superadmins` role to be used only in documented
  emergency recovery scenarios with explicit approval.
- Merging PRs into protected branches will be restricted to designated roles (e.g.,
  `team-developers-<project>-leads` or individuals specified in CODEOWNERS with `maintain` rights).

### 3.4. Management Method

- **Short-term (PROJ-103 Phase 1):** The initial creation of core GitHub Teams, population with initial
  members, and baseline repository permission assignments (for newly structured/created repositories) will
  be executed via `gh api` scripts. These scripts will be developed, tested, and logged as part of the
  `migration-toolkit-guide.md`.
- **Long-term (Target for PROJ-103 Phase 2 onwards):** All GitHub Team structures, memberships (for stable
  core teams), repository permissions, and branch protections will be codified and managed as Infrastructure
  as Code (IaC) using OpenTofu. The `gencraft-iac` repository and its CI/CD workflow (`../../gencraft-iac/.
github/workflows/terraform-ci-cd.yml`) will become the Single Source of Truth (SSoT) for these
  configurations. Manual changes to permissions via the GitHub UI or non-IaC `gh` commands will be strongly
  discouraged and subject to revert by IaC.

## 4. Migration Strategy

1. **Audit Current State:** (Completed for critical automations via A0.2). For existing repository
   permissions (if migrating repositories not just creating new ones as per adr-studio-001.md's focus), a
   separate, more granular audit would be needed to map old permissions to the new model. _Initial PROJ-103
   phases focus on new structure; existing repo permission migration is a subsequent consideration if they
   are not being archived or replaced._ 2.**Define and Create Core GitHub Teams:** Based on Section 3.1 and `../../gcs-core-governance/
00-studio-vision-and-principles/studio-organization-and-roles.md`, create the defined GitHub teams (e.g.,
   `team-devops`, `team-developers-projectphoenix`, `team-developers-projectphoenix-leads`,
   `team-all-members-readonly`) using `gh api` scripts. 3.**Populate Core Teams:** Assign studio members to these GitHub teams based on their primary roles and project assignments. 4.**Apply Default Permissions & Branch Protections:** For each new repository created or restructured
   during PROJ-103 Phase 1, apply the default team permissions (as per Section 3.2) and branch protections
   (as per Section 3.3) using `gh api` scripts. 5.**Transition to IaC Management (PROJ-103 Phase 2):**
   - Develop and test OpenTofu modules in `gencraft-iac` to define all teams, memberships, repository
     permissions, and branch protections according to this plan.
   - Import existing scripted configurations into OpenTofu state (`tofu import`) to ensure a smooth
     transition without resource recreation, or carefully plan resource adoption/recreation if import is not feasible.
   - Roll out IaC management progressively. 6.**Communication:** Announce the new permission model, any changes to user access, and the process for
     requesting access via channels defined in `communication-pal.md`. 7.**Training & Documentation:** Provide clear documentation within `gcs-core-governance` on the new
     permission model, team structures, and the access request process.

## 5. Implementation Plan (Key Steps for PROJ-103 Phase 1.2 & 1.3)

1. **Finalize Team Definitions & Detailed Permission Matrix:** Confirm the precise list of GitHub teams,
   their exact SSoT names, initial membership lists, and the finalized permission matrix with Crew Leads and
   Management. (Responsibility: Gem-AA, Lug, Crew Leads). 2.**Develop & Test `gh api` Scripts:** Create, test, and peer-review scripts for:
   - GitHub Team creation and membership management.
   - Assigning GitHub Team permissions to repositories.
   - Applying standard branch protection rules.
   - (Responsibility: Gem-AA). Store these scripts in `gencraft-devops-automation/scripts/migration/permissions/`. 3.**Execution - Phase 1.2 (Configure GitHub teams and permissions):**
   - Execute scripts to create GitHub Teams.
   - Execute scripts to add members to GitHub Teams.
   - Execute scripts to assign default GitHub Team permissions to newly created/structured repositories
     (from PROJ-103 Phase 1.1).
   - (Responsibility: Gem-AA, supervised by Lug; actions meticulously logged). 4.**Execution - Phase 1.3 (Apply branch protection rules):**
   - Execute scripts to apply defined branch protection rules to new/structured repositories.
   - (Responsibility: Gem-AA, supervised by Lug; actions meticulously logged). 5.**Verification:**
   - Conduct an audit of implemented teams, memberships, repository permissions, and branch protections
     against this plan for a significant subset of resources.
   - Utilize scripts to dump current configurations for comparison.
   - (Responsibility: Gem-AA, Camille (Gem AB) for audit assistance, Cerberus for security spot-check). 6.**IaC Transition Planning:** Initiate detailed planning for codifying these permissions in OpenTofu
     (for PROJ-103 Phase 2), including state import strategy.

## 6. Permissions Review, Auditing, and Exceptions

- **Regular Review:** Team memberships and repository permissions shall be reviewed at least quarterly by
  Team Leads (for their teams) and the DevOps team (for overall consistency and high-privilege teams).
  `team-devops-superadmins` and `team-security-officers` memberships will be validated monthly.
- **Auditing:** GitHub audit logs will be configured for export and periodic review (e.g., by Cerberus)
  for anomalous permission changes. Automated scripts using `gh api` will be developed to periodically dump
  current effective permissions and compare them against the IaC SSoT (once implemented) or this documented plan.
- **Access Request Process:**
  - Standard access is granted via membership in a defined GitHub Team.
  - Requests for new team membership, changes to team permissions, or temporary access not covered by
    this plan must be submitted using the `../../gcs-core-governance/02-knowledge-base-hub/templates/
issue-templates/access-request-template.md`.
  - Reviews will be conducted by the resource owner(s) (if applicable, e.g., via CODEOWNERS), the
    requestor's Crew Lead, DevOps (Gem-AA), and for sensitive access or policy deviations, by Cerberus
    (Security Officer Gem).
  - All approved exceptions must be documented with justification, scope, duration (if temporary), and
    an explicit review date.
- **Process for External Collaborators:**
  - External collaborators must be sponsored by an internal Crew Lead.
  - Access will be granted via dedicated GitHub Teams (e.g., `team-external-<project>-<vendor>`) with
    the least privilege necessary and for a defined, limited duration.
  - A formal review will be conducted before access renewal. Access will be revoked promptly upon
    contract termination.
- **Escalation:** Disputes regarding access or complex permission requirements not resolved through the
  standard request process will be escalated to Lug (Supervisor) and, if necessary, the Governance Crew as
  per `../../gcs-core-governance/01-operational-protocols/s2-disagreement-escalation.md`.

## 7. Document History

- v1.0 (2025-05-22): Initial draft by Gem-AA.
- v2.0 (2025-05-22): Amended and augmented after simulated review cycles (Cerberus, Lexicon, Crew Lead
  Rep, Lug). Status: Approved.

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
