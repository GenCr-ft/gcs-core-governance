---
docId: GOV-GUIDE-017
title: 'Unified Technical Standard: Engineering and Quality'
version: 1.0.0
creation_date: '2025-06-15'
last_updated_date: '2026-05-20'
authors:
- Governance Crew
knowledgeGuardian:
- Isaac (GCT-PRG-SARCH-001)
- "\xC9douard (GCT-DVO-DVSST-001)"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/ai-operational-guides/grounding-docs/GOV-GUIDE-017.unified-technical-standard-engineering-and-quality.md
metadata:
  lifecycle-stage: approved
  keywords:
  - grounding
  - standard
  - technical
  - engineering
  - quality
  - security
  scope: studio
  domain: production-management
  doc-type: playbook
  intended-audience:
  - contributors
  - ai-agents
  security-classification: l2_confidential
---
# Unified Technical Standard: Engineering and Quality

## 1. Objective and Role in the Grounding System

This document is the **single source of truth for all technical, quality, and security standards** at Gencraft Studio. It answers the question: **"How do I build things correctly?"**

It provides the fundamental rules for any Gem involved in engineering, development, testing, or operations. You must adhere to these standards in all your technical work.

**Note for AI Agents:** This standard is your "engineering playbook." Use the diagrams to understand the required workflows for code management, security, and quality assurance.

```mermaid
graph TD
    A["<b>1. Agent Charter (Me)</b>"] --> C["<b>3. Unified Technical Standard (Build)</b><br><i>Your Guide for Building</i>"];
    C --> B["<b>2. Operational Playbook (Act)</b>"];
    C --> D["<b>4. SSoT Contributor Guide (Document)</b>"];
    C --> E["<b>5. Studio Reference (Know)</b>"];

    style C fill:#cce5ff,stroke:#004085,stroke-width:3px
```

## 2. Pillar 1: Code and Version Management

This pillar governs how we manage our source code and artifacts.

### 2.1. Git Branching Strategy

All repositories must follow the "Gencraft Hybrid Flow".

```mermaid
graph TD
    subgraph "Feature Flow"
        A(develop) --> B(Branch to feature/...);
        B --> C(Work on Feature);
        C --> D(Create PR to develop);
        D --> E{Squash & Merge};
        E --> A;
    end
    subgraph "Release Flow"
        A --> F(Branch to release/vX.Y.Z);
        F --> G(Stabilize & Fix);
        G --> H(PR to main);
        H --> I{Merge Commit};
        I --> J(main);
        I --> A;
    end
```

- **Develop** on a `feature/...` branch created from `develop`.
- **Merge** features back into `develop` via a Pull Request (PR) using **Squash and Merge**.
- **Releases** are prepared on a `release/...` branch created from `develop`.
- **Merge** releases into `main` via a PR using a **Merge Commit**.

### 2.2. Semantic Versioning (SemVer)

All software artifacts (services, libraries, game builds) MUST follow SemVer `MAJOR.MINOR.PATCH`.

- Increment **MAJOR** for incompatible, breaking API changes.
- Increment **MINOR** for new, backward-compatible functionality.
- Increment **PATCH** for backward-compatible bug fixes.

#### 2.3. Python Module Naming Conventions

To ensure interoperability and compliance with the Python ecosystem, all files containing Python code intended to be imported (i.e., modules) MUST follow strict naming rules:

- **Allowed Characters:** `.py` filenames must only contain lowercase letters, numbers, and underscores (`_`).
- **Hyphens Forbidden:** The use of a hyphen (`-`) is strictly forbidden in module filenames, as it is not a valid character for a Python identifier and causes import errors (`ImportError`).
  - **Incorrect:** `my-super-module.py`
  - **Correct:** `my_super_module.py`

## 3. Pillar 2: Quality Assurance

This pillar defines our commitment to quality.

### 3.1. The Definition of Done (DoD)

A task is only "Done" when it passes all quality gates.

```mermaid
graph TD
    A[In Development] --> B(Code & Unit Tests);
    B --> C(Peer Review<br>Approved & Merged);
    C --> D(CI Pipeline<br>All Checks Pass);
    D --> E(QA Validation);
    E --> F(Documentation Updated);
    F --> G[Product Owner<br>Approval];
    G --> H((DONE));

    style H fill:#d4edda,stroke:#155724,stroke-width:2px
```

- **Core DoD Criteria:**
    1. Code is peer-reviewed and merged.
    2. All automated tests (unit, integration) pass in the CI pipeline.
    3. QA has validated that all acceptance criteria are met.
    4. No "Blocker" or "Critical" bugs are introduced.
    5. Relevant documentation is updated.
    6. The Product Owner (`Béatrice`) has accepted the feature.

### 3.2. Bug Triage

Bugs are classified by **Severity** (technical impact) and **Priority** (business urgency).

- **Severity Levels (SEV-1 to SEV-5):** From `Blocker` (prevents work) to `Trivial` (cosmetic). Assessed by QA (`Zoé`).
- **Priority Levels (P1 to P4):** From `Urgent` (fix immediately) to `Low` (fix if time allows). Set by the Product Owner (`Béatrice`).

## 4. Pillar 3: Security by Design

This pillar ensures security is integrated into our entire development process.

### 4.1. Secure Development Lifecycle (SDL)

All development must follow these seven phases.

```mermaid
graph TD
    A(1. Training) --> B(2. Requirements);
    B -- Security NFRs --> C(3. Design);
    C -- Threat Modeling --> D(4. Implementation);
    D -- Secure Coding --> E(5. Verification);
    E -- SAST/SCA/QA --> F(6. Release);
    F -- Final Review --> G(7. Response);
    G -- Feedback Loop --> A;
```

- **Design Phase:** Threat modeling is mandatory for new features.
- **Implementation Phase:** Adhere to secure coding standards.
- **Verification Phase:** Automated SAST/SCA scans are mandatory in the CI pipeline. Code reviews must include a security check.

### 4.2. Data Classification and Handling

You MUST handle all data according to its classification level.

- **L0 (Public):** Approved for public release.
- **L1 (Internal):** Default for internal operations. Requires authentication.
- **L2 (Confidential):** Sensitive data. Requires need-to-know access and encryption.
- **L3 (Secret):** Critical studio IP/credentials. Requires strictest controls.

Access to data is governed by the `access-control-policy.md`. When in doubt, treat information as **L1-Internal** and request clarification.

## 5. Pillar 4: Artifact and Infrastructure Management

This pillar covers the management of our technical assets.

### 5.1. Artifact Storage (S20)

- **Code & Documents:** Stored in version-controlled **Git repositories**.
- **Large Binary Files (Art/Audio/Builds):** Stored in **Git LFS** or a designated cloud storage solution, with metadata and process tracked in Git.

### 5.2. Infrastructure as Code (IaC)

All cloud infrastructure (servers, networks, databases) MUST be defined and managed as code in the `gencraft-iac` repository to ensure consistency, security, and traceability.
