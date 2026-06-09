---
docId: ARC-ADR-200
title: "Golden Path Decision: Application Framework and Pattern"
version: "1.0.0"
date: "2025-07-11"
authors:
  - "Architecture Crew (CC)"
  - "DevOps Crew (EE)"
knowledgeGuardian: "Isaac (Architecture Crew)"
status: "Approved"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/records/adrs/adr-studio-001/golden-path-ts-backend/ARC-ADR-200.application-framework-and-pattern.md
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

# ADR-200: Golden Path Decision on Application Framework and Pattern

## 1. Context

To address historical inconsistencies and technical debt, Gencraft Studio is defining a "Golden Path" for creating new backend services. A foundational decision is the choice of a standard application framework and architectural pattern. This decision aims to balance developer velocity, long-term maintainability, performance, and security. The full analysis of the options is available in `ARC-REFE-001`.

## 2. Decision Drivers

* **Developer Experience (DevEx):** Reduce cognitive load and accelerate onboarding.
* **Maintainability:** Ensure consistency and readability across all services.
* **Testability:** Facilitate unit and integration testing.
* **Scalability & Performance:** Meet the performance requirements of our services.
* **Security:** Adhere to security best practices.

## 3. Considered Options

1. **NestJS (Batteries-Included Framework):** An opinionated framework that imposes a strong, modular structure, with built-in dependency injection and a rich ecosystem.
2. **Fastify (Minimalist Framework):** A high-performance, low-overhead framework that provides maximum flexibility, requiring the development team to define its own structure and patterns.

## 4. Decision Outcome

**Decision:** We will adopt **NestJS** as the mandatory framework for all new TypeScript backend services.

This decision is conditional upon a critical secondary decision:

**Decision:** All NestJS services MUST implement a **Hexagonal Architecture (Ports & Adapters)** pattern. The standard project template will enforce a directory structure that isolates the core domain logic from the framework and infrastructure concerns.

### Justification

* **NestJS** was chosen because the benefits of its enforced structure, reduced cognitive load, and rich ecosystem heavily outweigh the minor performance overhead for our typical use cases. It directly addresses our primary problem of project inconsistency.
* The mandated **Hexagonal Architecture** mitigates the main risk of using an opinionated framework: vendor lock-in. By keeping our core logic pure and framework-agnostic, we ensure our services are maintainable and can be evolved independently of NestJS if necessary in the future.

## 5. Consequences

* **Positive:**
  * Increased developer velocity for new projects.
  * Improved consistency and maintainability across all backend services.
  * Simplified onboarding for new developers.
  * Enhanced testability due to dependency injection and clear architectural boundaries.
* **Negative:**
  * Reduced flexibility for teams who might prefer a different framework.
  * The framework introduces a layer of abstraction that can have a slight performance cost and may complicate debugging in some edge cases. This is considered an acceptable trade-off.
