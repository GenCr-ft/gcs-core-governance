---
docId: ENG-STAN-001
title: Ver 001 Semantic Versioning Standard
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This standard mandates the use of Semantic Versioning (SemVer) 2.0.0 for
  all software releases, APIs, libraries, and Infrastructure as Code modules within
  Gencraft. It establishes a consistent methodology for communicating changes, managing
  dependencies, and facilitating automated processes.
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - semantic-versioning
  - semver
  - versioning
  - software-standards
  - gencraft
  - devops
  - artifact-management
  scope: studio
  domain: engineering
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/engineering/standards/ENG-STAN-001.ver-001-semantic-versioning-standard.md
---
## 1. Objective

This standard establishes a mandatory, consistent, and predictable methodology for versioning all software
releases, APIs, libraries, modules (including Infrastructure as Code modules), and tools developed and
maintained within Gencraft. It is based on the **Semantic Versioning 2.0.0** specification.

The objectives are to:

- Clearly communicate the nature of changes between releases (breaking changes, new features, bug fixes).
- Enable reliable dependency management for internal and potentially external consumers.
- Facilitate automated version bumping and changelog generation.
- Standardize release processes and artifact identification.
- Reduce the risk of "dependency hell" by providing clear versioning semantics.

## 2. Scope

This standard applies to all versioned artifacts produced or managed by Gencraft, including but not limited to:

- Software applications (e.g., game client, game server, studio platform services).
- Application Programming Interfaces (APIs), both internal and external.
- Reusable software libraries, packages, and frameworks.
- Infrastructure as Code (IaC) modules (e.g., OpenTofu modules).
- Docker images.
- Command-line interface (CLI) tools.
- Versioned documentation sets (if their lifecycle is independent of code).
- AI Gem models or blueprints if they are versioned artifacts.

## 3. Standard: Semantic Versioning (SemVer) 2.0.0

All versioned artifacts MUST follow the `MAJOR.MINOR.PATCH` numbering scheme as defined by Semantic
Versioning 2.0.0 ([https://semver.org/](https://semver.org/)).

### 3.1. Core Version Format: `MAJOR.MINOR.PATCH`

- **`MAJOR`**: Incremented when incompatible API changes are made. Reset `MINOR` and `PATCH` to 0.
- **`MINOR`**: Incremented when functionality is added in a backward-compatible manner. Reset `PATCH` to 0.
- **`PATCH`**: Incremented when backward-compatible bug fixes are made.

### 3.2. Pre-release Versions

Used for versions that are not yet stable (e.g., alpha, beta, release candidates).

- **Format:** Appended to the `PATCH` version, separated by a hyphen. Consists of a series of
  dot-separated identifiers. Identifiers MUST comprise only ASCII alphanumerics and hyphens [0-9A-Za-z-].
  Numeric identifiers MUST NOT include leading zeroes.
  - Examples: `1.0.0-alpha.1`, `1.0.0-beta.2`, `2.1.0-rc.1`
- **Precedence:** Pre-release versions have lower precedence than the associated normal version (e.g., `1.
0.0-alpha` < `1.0.0`). Precedence for two pre-release versions with the same normal version is determined
  by comparing each dot-separated identifier from left to right (numeric identifiers are compared
  numerically, lexicographical identifiers are compared lexicographically in ASCII sort order).
- **Usage:**
  - `alpha`: Initial testing phase, highly unstable, features may be incomplete or change.
  - `beta`: Feature-complete or close, but known bugs may exist; for broader testing and feedback.
  - `rc` (Release Candidate): Believed to be stable and ready for final release, pending final testing.
    No new features, only critical bug fixes.

### 3.3. Build Metadata

Optional build metadata may be appended to the `PATCH` or pre-release version, separated by a plus sign (`+`).

- **Format:** Consists of a series of dot-separated identifiers. Identifiers MUST comprise only ASCII
  alphanumerics and hyphens [0-9A-Za-z-].
  - Examples: `1.0.0+git.sha.abcdef0`, `1.2.3-beta.1+001.build.timestamp.1678886400`
- **Precedence:** Build metadata is IGNORED when determining version precedence. Thus, `1.0.0+build1` and
  `1.0.0+build2` are considered the same version for dependency resolution, but identify different builds.
- **Usage:** CI build numbers, commit SHAs, build timestamps, or other build-specific information.

### 3.4. Initial Development (Version 0.y.z)

- **Starting Version:** Initial development of any new artifact SHOULD start at `0.1.0`.
- **Stability:** During the `0.y.z` phase, the public API (or contract of the artifact) SHOULD NOT be
  considered stable. Anything MAY change at any time.
- **Breaking Changes:** In `0.y.z` versions, even `MINOR` or `PATCH` increments MAY introduce breaking
  changes. This allows for rapid iteration and API refinement before a stable release. However, clear
  communication of such changes in changelogs is still crucial.

### 3.5. Transition to Stable Release (1.0.0)

- **Significance:** Version `1.0.0` marks the first stable, production-ready release of an artifact. Its
  public API is now defined and stable.
- **Strict Adherence:** After `1.0.0`, all SemVer rules regarding `MAJOR`, `MINOR`, and `PATCH` increments
  (as per section 3.1) MUST be strictly followed. Breaking changes MUST result in a `MAJOR` version increment.

### 3.6. Specific Artifact Versioning Guidelines

- **APIs (REST, gRPC, etc.):**
  - The `MAJOR` version of an API SHOULD be included in its access path or endpoint (e.g., `/api/v1/
users`, `/v2/items-service`).
  - Backward-incompatible API changes necessitate a new `MAJOR` version (e.g., evolving from `/api/v1`
    to `/api/v2`).
  - API documentation (e.g., OpenAPI/Swagger specifications) MUST be versioned in sync with the API.
- **Software Libraries & Packages (e.g., Python packages, npm modules):**
  - Consumers SHOULD be able to specify dependency versions using SemVer-compatible ranges (e.g., `~1.2.
3` for patch updates, `^1.2.0` for minor and patch updates).
  - Breaking changes (requiring a `MAJOR` bump) must be clearly communicated to consumers.
- **Infrastructure as Code (IaC) Modules (OpenTofu):**
  - Reusable, shared IaC modules (as per `../iac/iac-001-opentofu-tooling-standard.md`) stored in
    dedicated repositories MUST be versioned using Git tags that strictly follow SemVer (e.g., `v1.0.0`,
    `v1.0.1`, `v0.2.0-alpha.1`).
  - Root configurations or other modules consuming these shared modules MUST reference specific tagged
    versions to ensure predictable deployments.
  - Breaking changes in a module's input variables or output structure require a `MAJOR` version increment.
- **Docker Images:**
  - Docker images built by CI/CD pipelines MUST be tagged with the full SemVer of the artifact they
    contain (e.g., `my-app:1.2.3`, `my-service:2.0.0-beta.1`).
  - Additional tags like `latest` (for the most recent stable release), branch names (e.g., `main`,
    `develop`), or commit SHAs MAY be used for convenience but SemVer is the primary identifier for releases.
  - Refer to `../cicd/cicd-002-artifact-management-standard.md` for more details on image tagging.
- **Documentation Sets:**
  - If a documentation set (e.g., user manual, API reference) has a lifecycle independent of a specific
    software artifact, it SHOULD be versioned using SemVer.
  - If documentation is tightly coupled with a versioned artifact (e.g., API docs for API v1), it
    typically shares that artifact's version.

### 3.7. Version Bumping and Release Process

- **Decision Authority:** The decision to bump a `MAJOR`, `MINOR`, or `PATCH` version depends on the
  nature of changes introduced. This is typically determined by the Tech Lead, Product Owner, or designated
  Release Manager for the artifact, in consultation with the development team.
- **Automation (CI/CD):**
  - The CI/CD pipeline (`../cicd/cicd-001-baseline-workflow-guidance.md`) SHOULD facilitate automated
    version bumping and tagging where possible.
  - `../tooling/tool-001-conventional-commits-standard.md` is MANDATORY. Commit messages adhering to
    this standard enable automated determination of SemVer bumps (e.g., `fix:` -> PATCH, `feat:` -> MINOR,
    `BREAKING CHANGE:` -> MAJOR) and automatic changelog generation.
  - Tools like `semantic-release` or custom scripts managed by `Camille` (Gem AB) can be used for this
    automation.
- **Changelog:** All releases (especially `1.0.0` and later) MUST be accompanied by an updated changelog
  detailing notable changes, features, bug fixes, and any breaking changes. Conventional Commits greatly aid this.
- **Branching Strategy Alignment:** Versioning practices must align with the Gencraft branching strategy
  (`gh-001.1-branching-strategy-and-protection.md`). For example:
  - Release branches (e.g., `release/v1.2`) MAY be created for stabilizing MAJOR or MINOR releases.
  - Hotfixes for PATCH releases are typically branched from the corresponding release tag or main
    production branch.

### 3.8. Deprecation Policy

- When a `MAJOR` version of an API or widely used library is deprecated, a clear deprecation notice and
  migration path MUST be provided to consumers.
- The old version should be supported for a reasonable, communicated period before being retired. This
  policy will be detailed in a future API Lifecycle Management standard.

## 4. Responsibilities

- **Artifact Owners (Tech Leads, Product Owners, Module Maintainers):**
  - Ensuring their artifacts are versioned according to this standard.
  - Making decisions on version increments based on the nature of changes.
  - Ensuring changelogs are accurate and maintained.
- **`Édouard` (Gem AD - DevOps Strategy Specialist):**
  - Knowledge Guardian for this standard.
  - Providing guidance and training on SemVer practices.
  - Ensuring this standard is consistently applied across Gencraft.
- **`Camille` (Gem AB - Automation Specialist):**
  - Implementing and maintaining automation for version bumping, tagging, and changelog generation in CI/CD pipelines.
- **`Adam` (Gem AA - DevOps Team Lead):**
  - Overseeing the integration of SemVer practices into release management processes.
- **All Gencraft Developers/Contributors:**
  - Understanding and correctly applying SemVer principles.
  - Adhering to Conventional Commits to facilitate automated versioning.
- **Architects (`Isaac` and others):**
  - Considering SemVer implications during API design and system architecture to manage dependencies and
    backward compatibility effectively.

## 5. Compliance and Enforcement

- **Automated Checks:** CI/CD pipelines will attempt to validate commit messages (for Conventional
  Commits) and may incorporate tools to suggest or automate SemVer bumps.
- **Code Reviews (S1 Protocol):** Reviewers MUST check that version numbers are updated appropriately in
  PRs that constitute a release or introduce versionable changes to shared modules/libraries.
- **Release Process:** The formal release process for critical artifacts MUST include a step to verify and
  finalize the SemVer number.

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
