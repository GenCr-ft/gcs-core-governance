---
docId: ARC-ADR-202
title: "Golden Path Decision: Build and Containerization Strategy"
version: "1.0.0"
date: "2025-07-11"
authors:
  - "DevOps Crew (EE)"
  - "Security Crew"
  - "Architecture Crew (CC)"
knowledgeGuardian: "Isaac (Architecture Crew)"
status: "Approved"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/records/adrs/adr-studio-001/golden-path-ts-backend/ARC-ADR-202.build-and-containerization-strategy.md
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

# ADR-202: Golden Path Decision on Build and Containerization Strategy

## 1. Context

This decision follows `ARC-ADR-201` and defines the standard for building, packaging, and containerizing our TypeScript backend services. The objective is to select a strategy that maximizes CI/CD performance and security posture, while providing a good developer experience for debugging. The full analysis of the options is available in `ARC-REFE-001`.

## 2. Decision Drivers

* **Security:** Minimize the attack surface of our production container images.
* **Performance:** Reduce CI/CD pipeline duration and container image pull times.
* **Size:** Produce the smallest possible container images to reduce storage costs.
* **Developer Experience (DevEx):** Ensure developers have effective methods for debugging services running in containers.

## 3. Considered Options

1. **Standard Tooling (`tsc` + `node:20-alpine`):** A traditional approach using the official TypeScript compiler and a popular, lightweight base image.
2. **Modern Tooling (`esbuild` + `distroless`):** A modern approach using a high-performance bundler and a minimal, highly secure base image from Google.

## 4. Decision Outcome

**Decision 4.1: Standard Build & Containerization Tooling**
We will adopt **`esbuild`** as the mandatory tool for transpiling and bundling our TypeScript code, and **Google's `distroless` base images** as the mandatory foundation for our production container images.

**Decision 4.2: Multi-Stage Dockerfile for DevEx and Security**
All services MUST use a standard, multi-stage `Dockerfile` that produces two distinct targets:

1. **A `production` target:** Built on a `distroless` base image. This image is ultra-lightweight and contains only the application and its runtime dependencies. It has no shell or package manager. This is the **only** image that can be deployed to production environments.
2. **A `debug` target:** Built on a standard `node:20-alpine` base image. This image includes a shell and common debugging tools, and is intended exclusively for local development and non-production environments.

### Justification

* **`esbuild` + `distroless`** is chosen for its undeniable strategic advantages. The significant improvement in CI/CD speed directly translates to higher developer productivity. The minimal nature of `distroless` images drastically reduces our security attack surface, a non-negotiable requirement from our Security Crew.
* The **multi-stage Dockerfile** is a pragmatic solution that resolves the primary drawback of `distroless` images. It provides the best of both worlds: maximum security in production and a comfortable, tool-rich debugging experience for developers in their local environments.

## 5. Consequences

* **Positive:**
  * CI/CD pipeline execution times will be significantly reduced.
  * Our security posture is dramatically improved by minimizing vulnerabilities in the container's OS layer.
  * Container image size is minimized, leading to lower storage costs and faster deployment times.
* **Negative:**
  * Developers must learn to use the `debug` target of the Dockerfile for interactive debugging sessions, which is a minor change in workflow.
  * The build process requires a two-step type-checking and transpiling process (`tsc --noEmit` followed by `esbuild`), which will be abstracted away by our standard CI/CD workflow.
