---
docId: GOV-STANDARD-008
title: 'SSoT Master Taxonomy and Governance Standard'
version: 1.1.2
date: '2026-06-01'
authors:
- Iris (GCT-UTL-RWSKA-001)
- Édouard (GCT-DVO-DVSST-001)
knowledgeGuardian:
- Iris (GCT-UTL-RWSKA-001)
reviewers:
- Governance Crew
- All Knowledge Guardians
approvers:
- Governance Crew
- Lug (Studio Director)
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/foundations/governance/GOV-STANDARD-008.ssot-master-taxonomy-and-governance.md
metadata:
  domain: Governance
  classification:
    category: To Govern
    type: Standard
  lifecycle-stage: Review
  provenance:
    source: ai_assisted
    authors:
      - "Iris (GCT-UTL-RWSKA-001)"
      - "Édouard (GCT-DVO-DVSST-001)"
---

# GOV-STANDARD-008: SSoT Master Taxonomy and Governance Standard

## 1. Policy Statement

This document defines the philosophy and application of Gencraft Studio's master governance system. It serves as the human-readable guide to the rules and vocabularies that structure our entire digital ecosystem.

This standard is one of three core artifacts that form our "Constitution":

1. **This Document (The Guidebook):** Explains the "why" and "how".
2. **Modular governance law files (The Law):** The machine-readable SSoT files under `foundations/governance/vocabularies/`, `foundations/governance/catalogs/`, and `foundations/governance/rules/`.
3. **`governance-config.schema.json` (The Validator):** The formal JSON Schema that defines the resolved governance configuration contract.

This standard supersedes all previous documentation on taxonomy, `docId` conventions, and metadata.

## 2. Getting Started: How to Read This Standard

For any contributor, understanding our governance starts here.

* To understand our **classification philosophy**, read **Section 4**.
* To see the **list of allowed terms** (e.g., available domains, artifact types), consult the modular governance law files under `foundations/governance/`, especially `vocabularies/taxonomy.yml`.
* To understand **how we enforce these rules**, read **Section 6**.
* To understand **how to propose a change** to the rules, read **Section 5.2**.

## 3. Core Principles

Our governance is built on two core principles:

1. **Everything as Code:** All elements of our studio's structure—repositories, labels, rules, and documentation—are defined as data in a version-controlled SSoT.
2. **Governance by Automation:** Compliance with these standards is not optional. It is enforced automatically by linters and CI/CD pipelines at every stage of contribution.

## 4. The Governance Model Explained

Our model classifies every studio artifact using a set of orthogonal facets defined in the modular governance law files under `foundations/governance/`. Understanding these facets is mandatory for all contributors.

### 4.1. `artifact-class`: The Physical Nature

This facet answers: "What *is* this thing?". It describes the physical or technical nature of the artifact.

* **`Knowledge`**: A document, like this one.
* **`Code`**: Source code for a module, service, or application.
* **`Asset`**: A creative work, like a 3D model or an audio file.
* *Refer to `foundations/governance/vocabularies/taxonomy.yml` for the complete, authoritative list.*

### 4.2. `classification`: The Intellectual Intent

This facet, primarily for the `Knowledge` class, answers: "Why was this written?".

* **`category`**: Describes the high-level purpose (e.g., `To Govern`, `To Instruct`).
* **`type`**: Describes the specific form of the document (e.g., `Standard`, `Guide`).

### 4.3. Other Core Facets

* **`domain`**: The functional area of the studio (`Engineering`, `Art`, etc.).
* **`lifecycle-phase`**: The current stage of the artifact in our production pipeline (`Design`, `Operations`, etc.).
* **`provenance`**: The origin of the artifact (`manual`, `ai_generated`, etc.), ensuring traceability.

## 5. Universal Governance Process

### 5.1. The "Intention and Reality" Principle

The creation of any significant new artifact is governed by a "pull" model:

1. **Intention:** A formal "intention" to create the artifact must first be registered (e.g., as a GitHub Issue in a backlog).
2. **Reality:** The artifact, when created, must contain an "identity card" (`.ssot.yml` file or equivalent metadata) that links back to its approved intention.
3. **Enforcement:** Automated linters will block any contribution that creates an artifact without a corresponding, approved intention.

### 5.2. Updating the Governance SSoT

Any change to the modular governance law files under `foundations/governance/` is a change to the studio's constitution and is our most strictly controlled process.

1. **Proposal:** A change must be proposed via a Pull Request against `gcs-core-governance`, following Protocol S13.
2. **Dual Review:** The PR must be approved by:
    * **Governance & Semantics:** At least one `Knowledge Guardian` from the `Governance` domain (`Iris`) to ensure the change is logical and coherent.
    * **Technical Feasibility:** At least one specialist from the `DevOps` team (`Édouard`) to ensure the change can be technically enforced by our tools.
3. **Versioning:** The version of the affected governance standard or law file must be incremented following Semantic Versioning. Major, breaking changes require a studio-wide migration plan.

## 6. Enforcement by Automation

Compliance is not optional. It is guaranteed by our tooling.

* **`governance-config.schema.json`**: This file provides a formal JSON Schema for validating the resolved governance configuration assembled from the modular law files.
* **`gft-cli`**: Our command-line tool will use the modular governance law files to assist contributors in creating compliant artifacts.
* **Global Linter (GitHub Action):** Deployed on all repositories, this action will fetch the latest modular governance law files and schema to validate all new or modified artifacts in a PR. **It will block any PR that is not compliant.**

### 6.1. Linter Deployment: Centralized Reusable Workflow

To prevent configuration drift and ensure consistent enforcement across all studio repositories, the Global SSoT Linter **MUST** be deployed using GitHub's **Reusable Workflow** feature.

**This principle forbids the direct copying of linter workflow files into individual repositories.**

The enforcement mechanism is composed of two parts:

1. **The Reusable "Master" Workflow:**
    * **SSoT Location:** A single, authoritative workflow file located at `.github/workflows/reusable-ssot-linter.yml` within the `gcs-core-governance` repository.
    * **Function:** This file contains all the logic for checking out repositories, setting up the environment, and running the linter script against the resolved modular governance law files.
    * **Maintenance:** All updates to the linting process **MUST** be made exclusively to this file.

2. **The "Caller" Workflow:**
    * **SSoT Location:** A minimal workflow file (`.github/workflows/ssot-compliance.yml`) that **MUST** be present in every other studio repository.
    * **Function:** The sole purpose of this file is to call the "Master" reusable workflow from the `gcs-core-governance` repository, referencing a specific version tag for stability (e.g., `uses: GenCr-ft/gcs-core-governance/.github/workflows/reusable-ssot-linter.yml@v1.0`).

3. **Respect for `.gitignore`:** The linter **MUST** parse and respect the `.gitignore` file located at the root of any repository it scans. Any file or directory matching a pattern in `.gitignore` is considered out of scope for SSoT validation.
4. **Exclusion of Standard Repository Files:** The linter **MUST** systematically ignore common repository files that are not considered formal SSoT documents. This list of files to ignore includes, but is not limited to:
    * `README.md`
    * `LICENSE`
    * `CONTRIBUTING.md`
    * `CHANGELOG.md`
5. **Self-Exclusion:** The linter **MUST** ignore any internal directories it creates during its own execution (e.g., the `.ssot/` directory used by the CI workflow).

This centralized model ensures that any improvement to our governance linter is instantly and consistently propagated across the entire studio, in alignment with the principles of `GOV-PROT-002: Protocol for Studio-Wide Tooling Configuration Rollout`.

## 7. Version History

* **v1.1.2 (2026-06-01):** Aligned law-file and validator references with the current modular governance layout.
* **v1.1.0 (2025-06-30):** Amended version incorporating feedback from Édouard. Adds the concept of a governance validator, clarifies the application of rules for GitHub labels, and formalizes the structure for validation rules.
* **v1.0.0 (2025-06-30):** Initial creation of the master standard, unifying all previous taxonomy and `docId` conventions into a single SSoT.

This standard is the foundation upon which we build a scalable, resilient, and intelligent SSoT.
