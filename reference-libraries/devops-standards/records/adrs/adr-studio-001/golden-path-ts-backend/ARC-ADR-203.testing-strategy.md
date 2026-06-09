---
docId: ARC-ADR-203
title: "Golden Path Decision: Testing Strategy"
version: "1.0.0"
date: "2025-07-12"
authors:
  - "Architecture Crew (CC)"
  - "DevOps Crew (EE)"
  - "QA Crew"
knowledgeGuardian: "Zoé (QA Team Lead)"
status: "Approved"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/records/adrs/adr-studio-001/golden-path-ts-backend/ARC-ADR-203.testing-strategy.md
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

# ADR-203: Golden Path Decision on Testing Strategy

## 1. Context

Following the decisions on our application framework (`ARC-ADR-200`) and data access (`ARC-ADR-201`), we must now define a standard testing strategy. A consistent approach to testing is essential to guarantee the quality, reliability, and maintainability of our backend services. The adoption of a Hexagonal Architecture was made explicitly to enhance testability; this ADR formalizes how we will capitalize on that decision.

## 2. Decision Drivers

* **Quality & Reliability:** Ensure our services are robust and function as expected.
* **Confidence:** Allow teams to deploy to production with high confidence and low risk of regression.
* **Maintainability:** Tests serve as living documentation and prevent future changes from breaking existing functionality.
* **Developer Experience:** Provide a clear, consistent, and efficient framework for writing tests.

## 3. Considered Options

1. **Laissez-Faire Approach:** Allow each team to define its own testing frameworks, strategies, and quality gates. This was rejected as it perpetuates the very inconsistency we aim to solve.
2. **Strict Mandate:** Impose a rigid set of rules, including specific libraries for every type of test, and a strict, non-negotiable code coverage percentage. This was deemed too inflexible and could stifle productivity.
3. **Guided Framework:** Standardize on a core testing framework and a conceptual model (the Testing Pyramid), while providing clear guidelines and tools. This approach balances consistency with pragmatic flexibility.

## 4. Decision Outcome

**Decision:** We will adopt the **Guided Framework** approach (Option 3). Our testing strategy is based on the Testing Pyramid concept and standardizes on a core set of tools.

### *Decision 4.1: Standard Testing Framework**

* **Loi :** **Jest** is the mandatory testing framework for all TypeScript backend services.
* **Justification :** Jest is the default and well-integrated testing framework for NestJS. It provides a comprehensive solution for test running, assertions, and mocking, reducing the need for additional libraries.

### **Decision 4.2: The Testing Pyramid**

* **Loi :** All services MUST structure their testing efforts according to the Testing Pyramid model.
* **Justification :** This model provides the best return on investment, focusing effort on fast, reliable unit tests while using slower, more complex tests sparingly for critical paths.
* **Implementation in our Golden Path:**
    1. **Unit Tests (Base of the Pyramid):**
        * **Scope:** Test individual units (classes, functions) of the core domain logic (`/src/core`) in complete isolation. All external dependencies (adapters) MUST be mocked.
        * **Goal:** High volume, very fast execution. This is where the bulk of our testing effort should be.
    2. **Integration Tests (Middle of the Pyramid):**
        * **Scope:** Test the integration between our application's ports and adapters. This includes testing NestJS controllers, database adapters against a real test database, and adapters for external services against their mocks.
        * **Goal:** Medium volume, slower execution. Verifies that our code correctly interacts with the framework and infrastructure.
    3. **End-to-End (E2E) Tests (Top of the Pyramid):**
        * **Scope:** Test a complete user flow from the API endpoint down to the database. These tests should be few in number and cover only the most critical business workflows.
        * **Goal:** Low volume, slow execution. Provides confidence that the system works as a whole.

### **Decision 4.3: Quality Gates**

* **Loi :** The CI/CD pipeline MUST enforce a minimum code coverage threshold of **80%**, measured on unit tests.
* **Justification :** This is not a measure of quality абсолютная, but a **safety net** to prevent untested code from being merged. It encourages a baseline of testing discipline. Teams are encouraged to aim higher for critical components.

### **Decision 4.4: Test Data Management**

* **Loi :** A dedicated, ephemeral test database MUST be used for running integration tests. This database is automatically created and seeded before the test suite runs, and destroyed afterwards.
* **Justification :** This ensures that tests are repeatable and run in a clean, isolated environment, preventing data pollution between test runs.
* **Implémentation :** The Golden Path template will include scripts (e.g., using Docker Compose) to manage the lifecycle of the test database.

## 5. Consequences

* **Positive:**
  * Provides a clear and consistent testing strategy for all teams.
  * Improves the overall quality and reliability of our software.
  * The focus on unit testing the core domain logic aligns perfectly with our Hexagonal Architecture.
  * Automated quality gates provide a consistent baseline for code quality.
* **Negative:**
  * Teams lose the flexibility to choose other testing frameworks. This is an acceptable trade-off for studio-wide consistency.
  * Requires discipline from developers to write meaningful tests and not just "game" the coverage metric.
