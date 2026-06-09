---
docId: GCS-GUIDE-203
title: "The Practical TDD Guide"
version: 1.0.0
status: Draft
date: 2025-06-18
authors:
  - "Technical Governance"
knowledgeGuardian:
  - "Lead Developer"
  - "QA Lead"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/02-development-guides/GCS-GUIDE-203.tdd-guide.md
metadata:
  lifecycle-stage: approved
  domain: engineering
  doc-type: guide
  scope: studio-wide
  security-classification: l2_confidential
  keywords:
    - "tdd"
    - "testing"
    - "unit-testing"
    - "refactoring"
    - "design"
---

# The Practical TDD Guide

## 1. Objective

This guide establishes Test-Driven Development (TDD) as a fundamental design discipline for all engineering teams at the studio. Its purpose is to define the protocols and practices that ensure quality is built into our software from the very beginning, not checked at the end.

TDD is not primarily a testing technique; it is a **design methodology**. By writing a failing test before writing production code, we are forced to think about the requirements and the interface of our code first. This practice leads to more modular, maintainable, and robust systems, directly reducing the Total Cost of Ownership (TCO).

## 2. The Core Protocol: Red-Green-Refactor

All new business logic MUST be developed following the TDD cycle. This cycle is a short, repetitive loop composed of three distinct steps:

1. **RED - Write a Failing Test:**
    * Before writing any production code, write a single, small, automated test case that describes a piece of the desired functionality.
    * The test MUST fail because the corresponding production code does not yet exist. A compilation error is considered a failure.
    * This step forces you to clearly define what you want to achieve.

2. **GREEN - Make the Test Pass:**
    * Write the **absolute minimum** amount of production code required to make the failing test pass.
    * The goal at this stage is not elegance or optimization. It is acceptable to write "ugly" or "stupid" code simply to get to a green bar. This isolates the problem of "making it work" from "making it right."

3. **REFACTOR - Improve the Design:**
    * With the confidence of a passing test suite, improve the internal structure of the newly written code (both production and test code).
    * Remove duplication, improve names, simplify logic, and ensure the code adheres to our **Clean Code** principles [cite: GCS-GUIDE-201].
    * Re-run all tests to ensure that the refactoring has not altered the external behavior.
    * **This step is not optional.** Skipping the refactor step negates the primary design benefits of TDD.

## 3. Role-Specific Protocols

TDD is a team sport. Each role has specific responsibilities to ensure its success.

### 3.1. For Developers

* **Discipline:** Adhere strictly to the "Red-Green-Refactor" cycle for all new features and bug fixes involving logic.
* **Small Steps:** Each cycle should represent a tiny, incremental step forward in functionality.
* **Test Isolation:** Unit tests must be independent and must not rely on external systems like databases or networks. Use mocks, stubs, or fakes to isolate the unit under test.

### 3.2. For QA Engineers

* **Collaboration on Acceptance Criteria:** Work with Product Owners and Developers *before* development begins to define clear, testable acceptance criteria for each User Story, often using Gherkin syntax (Given/When/Then). This is the foundation for Acceptance Test-Driven Development (ATDD) or Behavior-Driven Development (BDD).
* **Reviewing Tests:** During code reviews, assess the quality and coverage of the unit tests alongside the production code. Do the tests accurately reflect the requirements?

### 3.3. For Architects

* **Design for Testability:** Ensure that architectural decisions promote testability. Favor decoupled components and dependency injection, which make it easier to test modules in isolation.
* **Championing TDD:** Act as a mentor and advocate for the TDD discipline, explaining its long-term architectural benefits (maintainability, flexibility).

## 4. TDD in our Workflow

* **Code Reviews:** A Pull Request that adds or modifies business logic MUST include the corresponding unit tests. The PR will not be approved if the tests are missing or inadequate.
* **CI Pipeline:** The test suite is executed automatically on every commit via our CI pipeline [cite: GCS-GUIDE-202]. A failing test breaks the build, and fixing it is the team's highest priority. The feedback loop from the CI server must be as fast as possible.

## 5. Automated TDD Commit Verification Gates

Our platform enforces TDD discipline programmatically to guarantee that quality gates are satisfied before merging:

* **TDD Commit Conventions**: Developers must split their feature branch work into atomic, sequential commits reflecting the Red-Green-Refactor cycle:
  1. **Red Phase**: Commit a failing unit test first. Commit message prefix MUST be `test(...)` with the red label: `test(server): WI-6.1 — red: assert login fails with invalid password`.
  2. **Green Phase**: Commit the minimal implementation to pass the test. Commit message prefix MUST be `feat(...)` with the green label: `feat(server): WI-6.1 — green: implement login validations`.
  3. **Blue Phase (Refactoring)**: Refactor and clean up code structure. Commit message prefix MUST be `refactor(...)` or `style(...)` with the blue label: `refactor(server): WI-6.1 — blue: optimize login error handlers`.
* **Automated Auditing Tool (`gft tdd status`)**: The platform CLI contains a static commit auditor command. Running `gft tdd status` scans all branch commits from `main` to `HEAD` to assert that:
  - At least one red-phase test commit exists.
  - At least one green-phase feature commit exists.
  - Diff analysis confirms that a unit test file (e.g. `test_*.py` or `*.spec.ts`) was physically modified alongside the production source files.
* **Pull Request Gates**: The `gft pr preflight` auditor enforces these TDD commit requirements automatically. PRs lacking atomic TDD commits are blocked from merging.
