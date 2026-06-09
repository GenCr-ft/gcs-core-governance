---
docId: ARC-STANDARD-001
title: SSoT Governance and Automation Architecture
version: 2.0.1
date: '2026-06-01'
authors:
- Iris (GCT-UTL-RWSKA-001)
knowledgeGuardian:
- Iris (GCT-UTL-RWSKA-001)
reviewers:
- Governance Crew
- All Knowledge Guardians
approvers:
- Governance Crew
- Lug (Studio Director)
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/foundations/governance/ARC-STANDARD-001.md
metadata:
  domain: Governance
  classification:
    category: To Govern
    type: Standard
  lifecycle-stage: Approved
  provenance:
    source: ai_assisted
    authors:
      - "Iris (GCT-UTL-RWSKA-001)"
---

# ARC-STANDARD-001: SSoT Governance and Automation Architecture

## 1. Mandate and Scope

This document defines the foundational architecture of the Gencraft Studio Single Source of Truth (SSoT) governance system. It serves as the master "Constitution" for all studio artifacts, outlining the non-negotiable principles that govern how we create, classify, store, and validate information.

Its purpose is to establish an unambiguous, scalable, and automated framework that ensures the clarity, consistency, and traceability of our entire knowledge and production ecosystem. This standard is the ultimate authority on the structure and intent of our governance model.

## 2. The Architectural Principles

Our SSoT architecture is built upon nine immutable principles. All standards, tools, and processes must adhere to this foundation.

  --- **Core Principles of Structure** ---

1. **Principle of Modularity**: The governance SSoT is modular. The "Law" (machine-readable YAML files) resides in a dedicated directory and is composed of several single-responsibility files (e.g., `vocabularies/taxonomy.yml`, `vocabularies/ontology.yml`).

2. **Principle of Separation**: The "Law" (machine-readable) must be strictly separated from the "Guide" (human-readable Markdown standards). Tools read YAML; contributors read the Markdown that explains the YAML.

3. **Principle of the Conceptual Model (Container & Artifact)**: The SSoT recognizes two fundamental types of entities: **Containers** (logical spaces that organize work, e.g., a `repository`) and **Artifacts** (units of intellectual property stored within containers, e.g., a `document`, a `script`). This distinction structures our entire governance.

4. **Principle of Expressive Taxonomy**: Our classification of artifacts uses a rich semantic model. All artifacts are classified according to several mandatory facets that capture their context (e.g., `artifact-class`, `domain`, `classification`).

5. **Principle of Universal Governance**: The taxonomy, particularly the `artifact-class` facet, is designed to govern **all** studio outputs, not just documents.

--- **Core Principles of Process** ---

1. **Principle of Explicit Traceability**: Every "Reality" (an artifact) must be traceable to a formal "Intention" (e.g., a backlog Issue). Artifacts must carry an "Identity Card" (`.ssot.yml` file or embedded metadata) that ensures this chain of trust.

2. **Principle of Federated Governance (Cascade and Context)**: The SSoT is not a monolithic system but a **federation of governance scopes**. The global (Studio) scope defines the common law, but more specific scopes (e.g., Project) can extend, amend, or override it.
    * **Hierarchy:** Governance is resolved by following a context hierarchy, from most specific to most global (e.g., `Artifact` -> `Project` -> `Studio`).
    * **Precedence Rule:** Tooling MUST apply the **closest rule** to the artifact. Any local rule (e.g., within a project's dedicated governance repository) overrides and replaces any rule of the same nature and ID defined at a higher, more global level.
    * **Discovery Mechanism:** The location of all official governance scopes is defined in a central registry (`foundations/governance/catalogs/governance-scopes.yml`). Tooling MUST use this registry as its single source of truth to discover all applicable laws.

3. **Principle of Centralized Enforcement**: Compliance is automated and enforced through a **single point of entry**: a reusable CI/CD workflow. This centralized mechanism prevents configuration drift and ensures uniform application of the "Law".

4. **Principle of Systematic Verification**: No artifact may advance in its lifecycle without passing a formal verification gate appropriate to its nature. "Trust, but verify" is a core tenet. The specific verification gates (e.g., peer review, automated testing, linter validation) are detailed in the relevant operational protocols (e.g., **Protocol S1**, **Definition of Done**).

## 3. SSoT Repository Mandates

Our knowledge is distributed across specialized repositories, each with a clear mandate.

* `gcs-core-governance`: The SSoT for **Organizational Governance**. This includes the studio's mission, values, operational protocols (S1, S2, etc.), roles, and core collaboration playbooks. It answers, "How do we work together?"
* `gcs-core-governance`: The SSoT for **Technical Governance**. This includes all engineering, DevOps, and security standards, as well as the master governance "Law" files (YAML) in its `/foundations/governance/` directory. It answers, "How do we build things correctly?"
* `gcd-ops-scripts`: The SSoT for **Automation Tooling**. This repository houses the source code for our internal tools, including the Global SSoT Linter.
* `gcd-shared-actions`: The SSoT for **Reusable CI/CD Workflows**. This repository contains the master "caller" workflows, including the `reusable-ssot-linter.yml`, to enforce the Principle of Centralized Enforcement.
* `gcs-plt-architecture`: The SSoT for **Studio-Wide Architecture Decisions**. This contains the ADRs and TDDs that define our platform's technical strategy.
* `gcp-<project>-*`: A group of repositories dedicated to a **specific game project**, containing its code, assets, documentation, and backlog.

## 4. Automated Governance Mechanisms

Our governance is enforced through a cohesive, three-part automated system.

1. **The "Law" (YAML Files)**
    These files, located in `gcs-core-governance/foundations/governance/`, are the machine-readable source of truth. They define the exact vocabularies, catalogs, and rules that our tools use to validate compliance. They are the unambiguous reality of our governance.

2. **The Global Linter**
    This is the primary enforcement engine. As defined by the Principle of Centralized Enforcement, a reusable GitHub Actions workflow is triggered on every Pull Request. It fetches the "Law" files and the linter script from their respective SSoT repositories and validates the changed files in the PR. A failed check blocks the merge, guaranteeing that no non-compliant artifact enters a protected branch.

3. **The Gencraft CLI (`gft-cli`)**
    This command-line tool is the primary interface for contributors. It assists in creating compliant artifacts by reading the "Law" files. For example, when creating a new document, `gft-cli doc new` would present the user with the allowed `studio_domain` and `knowledge_classification_type` values pulled directly from `vocabularies/taxonomy.yml`, preventing errors before they are even committed.

4. **The Knowledge Discovery Mechanism (SSoT Indexing)**
   While the SSoT repositories provide the authoritative storage, a dedicated Indexing Service is responsible for consuming, parsing, and indexing the metadata of all SSoT artifacts. This service provides a queryable API (e.g., semantic search, filtered search based on taxonomy facets) that allows both humans and AI Agents to discover relevant information efficiently without having to scan every repository manually. This service is the primary entry point for any knowledge discovery task.

## 5. Standard Structure for Catalogs and Indexes

To ensure consistency across all catalog-type artifacts (e.g., `repository-catalog.yml`), the following structure is mandatory:

* A single top-level key named after the catalog (e.g., `repository_catalog:`).
* The value of this key must be an array of objects.
* Each object in the array represents an entry in the catalog and MUST contain at least the following two keys:
  * `id`: A unique, machine-readable identifier for the entry (e.g., `gcs-core-governance`).
  * `description`: A human-readable string explaining the purpose of the entry.
* Additional structured data SHOULD be nested under a `metadata:` key.

## 6. Standard Structure for Document Metadata

All SSoT documents (Markdown files, excluding repository-specific files like `README.md` or `LICENSE`) MUST begin with a YAML frontmatter block containing the following structure. The `metadata` block is mandatory.

```yaml
---
docId: [DOMAIN_CODE]-[TYPE_CODE]-[NNN]
title: "A Clear and Descriptive Title"
version: "1.0.0"
date: "YYYY-MM-DD"
authors:
  - "Name (GEM_ID)"
knowledgeGuardian: "Name (GEM_ID)"
reviewers:
  - "Name (GEM_ID)"
approvers:
  - "Name (GEM_ID)"
ssot_path: "repository-id/path/to/document.md"
metadata:
  domain: "Name of the Studio Domain"
  classification:
    category: "Name of the Knowledge Category"
    type: "Name of the Knowledge Type"
  lifecycle-stage: "Name of the Lifecycle Stage"
  security-classification: "l1_internal"
  intended-audience:
    - "allcontributors"
    - "aiagents"
  provenance:
    source: "name_of_provenance_source"
    authors: # Optional, for more detail
      - "Name (GEM_ID)"
  # Other optional metadata can be added here
---
```

All values for `domain`, `classification.category`, `classification.type`, `lifecycle-stage`, and `provenance.source` MUST correspond to a valid entry in `gcs-core-governance/foundations/governance/vocabularies/taxonomy.yml`.

## 7. Master Taxonomy Reference

The complete and authoritative set of controlled terms for all classification facets is defined in a dedicated SSoT file: `gcs-core-governance/foundations/governance/vocabularies/taxonomy.yml`. All contributors and tools MUST refer to this file as the single source of truth for metadata values.

## 8. Version History

| Version | Date       | Author(s)                  | Summary of Changes                               |
| :------ | :--------- | :------------------------- | :----------------------------------------------- |
| 1.0.0   | 2025-07-02 | Iris (GCT-UTL-RWSKA-001)   | Initial creation of the Governance Architecture Standard, formalizing the six core principles. |
| 1.1.0   | 2025-07-02 | Iris (GCT-UTL-RWSKA-001)   | Modularized governance files. Added standards for catalog and metadata structures. |
| 1.2.0   | 2025-07-03 | Iris (GCT-UTL-RWSKA-001)   | Added 'storage-rules.yml' to the modular architecture. |
| 1.3.0   | 2025-07-06 | Iris (GCT-UTL-RWSKA-001)   | Added principles 7 and 8 |
| 2.0.1   | 2026-06-01 | Codex                       | Aligned governance law-file paths with the current modular workspace layout. |
