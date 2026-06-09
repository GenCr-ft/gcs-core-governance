---
docId: ARC-ADR-201
title: "Golden Path Decision: Data Access Strategy"
version: "1.0.0"
date: "2025-07-11"
authors:
  - "Architecture Crew (CC)"
  - "DevOps Crew (EE)"
  - "Lead Developers Committee"
knowledgeGuardian: "Isaac (Architecture Crew)"
status: "Approved"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/records/adrs/adr-studio-001/golden-path-ts-backend/ARC-ADR-201.data-access-strategy.md
metadata:
  domain: architecture
  classification:
    category: to-record
    type: adr
  security-classification: "l2-confidential"
  lifecycle-stage: approved
  doc-type: adr
  intended-audience:
    - architects
    - devops-crew
    - all-contributors
---

# ADR-201: Golden Path Decision on Data Access Strategy

## 1. Context

This decision follows `ARC-ADR-200` and defines the standard for data access within our TypeScript backend services. The goal is to select a strategy that maximizes developer velocity and type safety while ensuring performance and maintainability. The full analysis of the options is available in `ARC-REFE-001`.

## 2. Decision Drivers

* **Developer Experience:** Provide a type-safe, intuitive, and productive way to interact with the database.
* **Performance:** Ensure that data access patterns are efficient and do not become a bottleneck.
* **Maintainability:** The data model and migration path must be clear, version-controlled, and reliable.
* **Security:** Minimize the risk of SQL injection and other data-related vulnerabilities.

## 3. Considered Options

1. **Prisma (Full ORM & Toolkit):** A modern ORM that provides a fully-typed client generated from a declarative schema. It includes a robust, built-in migration system.
2. **Kysely (Type-Safe SQL Query Builder):** A lightweight library that provides a type-safe API for building raw SQL queries, offering maximum control and performance.

## 4. Decision Outcome

**Decision 4.1: Primary Standard**
We will adopt **Prisma** as the mandatory, default tool for all database interactions in our backend services. The `schema.prisma` file is the SSoT for the data model, and `prisma migrate` is the standard tool for schema migrations.

**Decision 4.2: Performance Escape Hatch**
The use of **Kysely** is authorized as an exception for performance-critical queries, under the following strict and mandatory process:

1. **Performance Justification:** The development team MUST first provide documented proof (benchmarks, load tests) that the equivalent Prisma query does not meet the service's performance requirements.
2. **Formal ADR:** This justification and the decision to use Kysely for a specific query MUST be recorded in a dedicated ADR.
3. **SSoT Traceability:** The component's `.ssot.yml` file MUST reference the ADR via a `related_adr` field. A custom linter rule will enforce this link.
4. **Security Review:** Any Pull Request introducing Kysely code MUST undergo a formal security review by the Security Crew (`Cerberus`) to prevent SQL injection vulnerabilities.

**Decision 4.3: Migration Workflow**
Database migrations (`prisma migrate deploy`) MUST NOT be run automatically in the CI/CD pipeline. The deployment workflow will include a **manually-triggered job** that must be consciously activated by an authorized team member (e.g., a Tech Lead or DevOps engineer) to apply migrations to an environment.

### Justification

* **Prisma** is chosen as the default for its immense boost to developer productivity and type safety. For the vast majority of our needs, it is the most efficient and secure tool.
* The governed **Kysely escape hatch** provides a necessary safety valve. It gives us the power of raw SQL performance when we truly need it, without sacrificing our governance model. The ADR process ensures this exception remains rare, justified, and traceable.
* The **manual migration trigger** is a critical safety measure that balances the convenience of Prisma's migration tool with the operational reality of managing production database schemas, preventing accidental and unreviewed changes.

## 5. Consequences

* **Positive:**
  * Development of data-driven features will be significantly faster.
  * A whole class of bugs related to type mismatches between the application and the database is eliminated.
  * The data model is clearly defined and version-controlled.
  * We retain the ability to performance-tune critical queries when necessary.
* **Negative:**
  * Adds a dependency on the Prisma ecosystem.
  * The process for performance exceptions introduces a deliberate, but necessary, amount of friction.
