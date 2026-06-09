---
docId: ENG-REFE-001
title: Studio Global Engineering Standards
version: 1.1.0
date: '2025-06-17'
authors:
- Technical Governance
knowledgeGuardian:
- Principal Architect
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/01-manifesto-and-culture/ENG-REFE-001.studio-global-engineering-standards.md
metadata:
  scope: studio-wide
  domain: engineering
  doc-type: reference
  lifecycle-stage: approved
  security-classification: l2_confidential
  keywords:
    - "engineering-standards"
    - "sgs"
    - "governance"
    - "architecture"
    - "reference"
---
# Studio Global Engineering Standards (SGS)

## 1. Objective and Philosophy

This document is the Single Source of Truth for all core design, development, testing, and maintenance practices within the studio. It ensures that we build robust, secure, maintainable, and high-performance systems consistently across all projects.

Our philosophy is based on a hierarchical approach:
* **Studio Global Standards (SGS):** This document defines the non-negotiable rules applicable to **all** projects.
* **Project-Specific Conventions (PSC):** Each project (e.g., Aethel) will have its own document that inherits from these standards and specializes them where necessary. A PSC can strengthen an SGS but never contradict it.

All rules stated below refer to the detailed guides in our **Software Engineering Handbook**.

---

## 2. Design Rules

1.  **Requirements-Driven Design:** No design shall begin without a clear specification, documented in a User Story with defined Acceptance Criteria.
2.  **Secure by Design:** The principles of **Least Privilege** and **Defense in Depth** must be applied to any new architecture.
3.  **SOLID Principles Application:** Every new class or module must be designed in compliance with the five SOLID principles.
4.  **Justified Algorithmic Choice:** The choice of an algorithm or data structure must be justified in terms of Big O complexity, following the procedure in the **Practical Algorithm Guide**.
5.  **Use of Design Patterns:** Recurring design problems must be solved using proven patterns from the **Design & Architectural Patterns Grimoire**. The use of a pattern must be documented and justified.
6.  **Reliability-Oriented Design:** For any critical service, **Service Level Objectives (SLOs)** must be defined at the design stage.

## 3. Development Rules

1.  **Version Control Workflow (Git):** All projects MUST follow the **GitHub Flow** branching strategy. The `main` branch must always be in a deployable state.
2.  **Atomic and Semantic Commits:** Every commit MUST represent a single logical unit of work, and its message MUST be descriptive and prefixed (e.g., `feat:`, `fix:`, `refactor:`).
3.  **Test-Driven Development (TDD):** The **"Red-Green-Refactor"** cycle is the default development method for all new business logic.
4.  **Mandatory Defensive Coding:** All recipes from the **Application Security Guide** MUST be applied (prevention of injections, XSS, CSRF, etc.).
5.  **No Secrets in Plaintext:** Secrets MUST NEVER be stored in the source code. They must be managed via an approved secrets management system.

## 4. Testing Rules

1.  **Systematic Code Review:** No Pull Request (PR) can be merged without the approval of at least **one** other team member.
2.  **Automation in CI/CD:** Every PR MUST trigger a CI pipeline that includes, at a minimum: compilation, unit tests, code quality analysis, and security scans.
3.  **Minimum Test Coverage:** A minimum unit test coverage of **80%** is required for all new code. This threshold is enforced via a "Quality Gate".
4.  **Bug Triage Process:** Any identified bug MUST be documented and triaged according to the Severity/Priority matrix defined in the **Quality Assurance Framework**.

## 5. Evolution and Maintenance Rules

1.  **Proactive Technical Debt Management:** A minimum of **15%** of each sprint's time MUST be allocated to remediating technical debt.
2.  **Observability by Default:** Any new service deployed to production MUST expose the three pillars of observability: structured logs, metrics, and distributed traces.
3.  **Blameless Postmortems:** Any production incident that violates an SLO MUST be followed by a postmortem analysis.
