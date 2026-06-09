---
docId: ARC-ADR-205
title: "Golden Path Decision: API Contract and Documentation Strategy"
version: "1.0.0"
date: "2025-07-12"
authors:
  - "Architecture Crew (CC)"
  - "DevOps Crew (EE)"
  - "Frontend Crew"
knowledgeGuardian: "Isaac (Architecture Crew)"
status: "Approved"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/records/adrs/adr-studio-001/golden-path-ts-backend/ARC-ADR-205.api-contract-strategy.md
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

# ADR-205: Golden Path Decision on API Contract and Documentation Strategy

## 1. Context

As we build a distributed system of microservices, ensuring clear, consistent, and reliable communication between them is paramount. A service without a formal, machine-readable contract is a black box that hinders integration, testing, and adoption by consumer teams (e.g., frontend applications, other backend services). This ADR defines the standard for how all RESTful APIs must be described and documented.

## 2. Decision Drivers

* **Interoperability:** Provide a language-agnostic way for services to communicate reliably.
* **Developer Experience:** Enable consuming teams to easily discover and understand an API's capabilities.
* **Automation:** The API contract should be a machine-readable artifact that can be used to auto-generate clients, tests, and documentation.
* **Accuracy & Traceability:** The documentation must always be synchronized with the actual implementation and versioned alongside the code.

## 3. Considered Options

1. **Manual Documentation:** Each team writes and maintains API documentation manually (e.g., in Markdown files or a wiki). This option was rejected as it inevitably leads to outdated documentation and is not machine-readable.
2. **Code-First, Auto-Generated Specification:** Use tooling and code decorators to generate the API specification directly from the source code. This approach makes the code the single source of truth for the API contract.

## 4. Decision Outcome

**Decision:** We will adopt the **Code-First, Auto-Generated Specification** approach (Option 2).

**Decision 4.1: API Specification Standard**

* **Loi:** The **OpenAPI 3.x** specification is the mandatory standard for describing all RESTful APIs developed within the studio.
* **Justification:** OpenAPI (formerly Swagger) is the undisputed industry standard, with a massive ecosystem of tools for documentation, code generation, and testing.

**Decision 4.2: Generation Strategy**

* **Loi:** The OpenAPI specification MUST be **auto-generated directly from the service's source code**.
* **Justification:** This guarantees that the documentation is never out of sync with the implementation. The code is the SSoT.
* **Implementation:** The Golden Path template for NestJS MUST include and pre-configure the `@nestjs/swagger` package. Developers are REQUIRED to use its decorators (e.g., `@ApiOperation`, `@ApiResponse`, `@ApiProperty`) on their controllers and DTOs to enrich the generated specification.

**Decision 4.3: Publication and Accessibility**

* **Loi:** Every service MUST expose its interactive API documentation (the Swagger UI) on a standard `/api-docs` endpoint. This endpoint MUST be disabled in production environments for security reasons.
* **Loi:** The CI/CD pipeline MUST include a job that automatically generates the static `openapi.json` specification file and publishes it as a versioned artifact to the **Central Artifact Registry**.
* **Justification:** This provides a dual-access model: developers get an interactive UI for exploration in development environments, and our automated systems get a stable, versioned JSON file from the registry for tasks like client generation or contract testing.

## 5. Consequences

* **Positive:**
  * API documentation will always be accurate and synchronized with the code.
  * Frontend and other consumer teams can auto-generate type-safe clients, drastically reducing integration errors and development time.
  * The QA team can leverage the specification to automate contract testing.
  * The process is highly automated and integrated into our CI/CD workflow.
* **Negative:**
  * It introduces a small amount of "ceremony" for backend developers, who must diligently apply the necessary decorators in their code. This is considered a highly valuable trade-off.
