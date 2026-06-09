---
docId: ENG-STANDARD-008
title: Semantic Versioning (SemVer) 2.0.0 Standard
version: 1.0.0
date: '2025-06-13'
authors:
- Camille (GCT-DVO-DVSAU-001)
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
reviewers:
- "\xC9douard (GCT-DVO-DVSST-001)"
- Isaac (GCT-PRG-SARCH-001)
- Antoine (GCT-MGT-PPM-001)
approvers:
- Governance Crew
relatedDocuments:
- GITHUB-STANDARD-001.branching-strategy.md
- s15-agile-scrum-project-management.md
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/foundations/governance/ENG-STANDARD-008.semantic-versioning-(semver)-2.0.0-standard.md
metadata:
  lifecycle-stage: approved
  keywords:
  - standard
  - versioning
  - semver
  - cicd
  - release
  scope: studio
  domain: devops
  doc-type: standard
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
---
# Semantic Versioning (SemVer) 2.0.0 Standard

## 1. Policy Statement

All software artifacts produced by Gencraft Studio that have a public API or are shared as versioned dependencies MUST be versioned according to the **Semantic Versioning 2.0.0 specification**. This includes, but is not limited to:

- Core Studio Services and MCP Servers
- Shared libraries (e.g., in `gcl-*` repositories)
- AI Gem `Tools` distributed as packages
- Game clients and servers released to players or testers

This standard ensures predictable dependency management and clear communication about the nature of changes between versions.

## 2. Version Format: MAJOR.MINOR.PATCH

The version number is specified in the format `MAJOR.MINOR.PATCH`.

- **MAJOR version:** Increment for incompatible API changes (breaking changes).
- **MINOR version:** Increment for adding functionality in a backward-compatible manner.
- **PATCH version:** Increment for making backward-compatible bug fixes.

**Note for AI Gems:** The following diagram illustrates the decision workflow for incrementing the correct version number. Release management `Tools` should be built upon this logic.

```mermaid
graph TD
    subgraph "Decision Flow for Version Increment"
        A{Start:<br>Changes Ready for Release} --> B{Do the changes include<br>any Breaking API Modifications?};
        B -- Yes --> C[<b>Increment MAJOR</b><br>e.g., 1.4.2 ➞ 2.0.0];
        B -- No --> D{Do the changes add<br>new, backward-compatible<br>functionality?};
        D -- Yes --> E[<b>Increment MINOR</b><br>e.g., 1.4.2 ➞ 1.5.0];
        D -- No --> F{Do the changes ONLY<br>contain backward-compatible<br>bug fixes?};
        F -- Yes --> G[<b>Increment PATCH</b><br>e.g., 1.4.2 ➞ 1.4.3];
        F -- No --> H[No Version Change<br><i>(e.g., docs, refactor)</i>];
    end

    style C fill:#f8d7da,stroke:#721c24,stroke-width:2px
    style E fill:#d1ecf1,stroke:#0c5460,stroke-width:2px
    style G fill:#d4edda,stroke:#155724,stroke-width:2px
    style H fill:#f0f0f0,stroke:#333
```

## 3. Pre-release & Build Metadata

- **Pre-release versions** MAY be denoted by appending a hyphen and a series of dot-separated identifiers immediately following the patch version. Pre-release versions have a lower precedence than the associated normal version.
  - Examples: `1.0.0-alpha.1`, `1.0.0-beta.2`, `1.2.0-rc.1`.
- **Build metadata** MAY be denoted by appending a plus sign and a series of dot-separated identifiers immediately following the patch or pre-release version. Build metadata MUST be ignored when determining version precedence.
  - Examples: `1.0.0+build.123`, `1.0.0-alpha.1+build.456`.

## 4. Initial Development (MAJOR Version Zero)

Initial development versions start at `0.1.0`. The public API should be considered unstable during this phase (MAJOR version zero). Anything MAY change at any time. The application should not be considered "production-ready" before version `1.0.0`.

## 5. Responsibilities

- **Development Teams:** Responsible for correctly identifying the nature of their changes (breaking, feature, or fix) and proposing the correct version increment in their Pull Requests.
- **Lead Developer (`Julien`) / Architect (`Isaac`):** Responsible for validating the proposed version increment during code review, especially for MAJOR version changes.
- **DevOps Automation (`Camille`):** Responsible for creating and maintaining CI/CD `Tools` that can automatically increment PATCH or MINOR versions based on commit history (e.g., using Conventional Commits standard).
- **Knowledge Guardian (`Édouard`):** Responsible for maintaining this standard.
- **Governance Crew:** Responsible for approving any changes to this standard and ensuring it remains aligned with Gencraft Studio's overall DevOps practices.

## 6. Related Resources and Links

- [Semantic Versioning 2.0.0 Specification](https://semver.org/spec/v2.0.0.html)
