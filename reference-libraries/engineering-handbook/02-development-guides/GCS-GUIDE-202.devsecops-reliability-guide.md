---
docId: GCS-GUIDE-202
title: "The DevSecOps, Reliability & Cloud-Native Guide"
version: 1.0.0
status: Draft
date: 2025-06-18
authors:
  - "Technical Governance"
knowledgeGuardian:
  - "DevOps Lead"
  - "SRE Lead"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/02-development-guides/GCS-GUIDE-202.devsecops-reliability-guide.md
metadata:
  lifecycle-stage: approved
  domain: engineering
  doc-type: guide
  scope: studio-wide
  security-classification: l2_confidential
  keywords:
    - "devops"
    - "devsecops"
    - "sre"
    - "cloud-native"
    - "kubernetes"
    - "docker"
    - "ci-cd"
    - "reliability"
---

# The DevSecOps, Reliability & Cloud-Native Guide

## 1. Objective

This guide provides the standard procedures for building, deploying, securing, and operating reliable systems in a cloud-native ecosystem. It is the single source of truth for our DevOps, Security, and Site Reliability Engineering (SRE) practices. Adherence to these protocols is mandatory for all projects.

## 2. Containerization Recipes (Docker)

All applications MUST be deployed as Docker containers to ensure consistency across environments.

### 2.1. Dockerfile Best Practices

* **Use Multi-Stage Builds:** Multi-stage builds MUST be used to create lean production images. The final image should contain only the application runtime and its necessary dependencies, excluding build tools, compilers, and development libraries.
* **Use Specific Base Images:** Always use specific version tags for your base images (e.g., `node:18.16-alpine` instead of `node:latest`). This ensures reproducible builds.
* **Run as Non-Root User:** Containers MUST run with a non-root user for security. Create a dedicated user and group in the `Dockerfile`.
* **Minimize Layers:** Combine related `RUN` commands using `&&` to reduce the number of layers in the image, making it smaller and faster to pull.

## 3. Orchestration Protocols (Kubernetes)

Kubernetes is our standard for container orchestration.

### 3.1. Standard Manifests

* **Use Deployments for Stateless Apps:** All stateless applications MUST be managed via `Deployment` resources to handle rolling updates and scaling.
* **Use StatefulSets for Stateful Apps:** Applications requiring stable network identifiers and persistent storage MUST use `StatefulSet` resources.
* **Expose Services Correctly:** Use `ClusterIP` for internal communication, `NodePort` for non-production external access, and `LoadBalancer` (or `Ingress`) for production traffic.

### 3.2. Configuration and Secrets Management

* **Use ConfigMaps for Configuration:** Application configuration MUST be externalized from the container image and managed via `ConfigMap` resources.
* **Use Secrets for Sensitive Data:** All sensitive data (passwords, API keys, certificates) MUST be managed via `Secret` resources. Do not store secrets in `ConfigMaps` or container images [cite: GCS-ARCH-001].

## 4. CI/CD Pipeline & Supply Chain Security

Our CI/CD pipeline is the automated backbone of our development process.

1. **Mandatory CI Checks:** Every Pull Request MUST pass a series of automated checks before being eligible for merge:
    * Unit & Integration Tests [cite: GCS-GUIDE-203].
    * Static Code Analysis & Linting [cite: GCS-GUIDE-201].
    * **Software Composition Analysis (SCA):** A scan for known vulnerabilities in third-party dependencies MUST be performed. High or Critical vulnerabilities must be fixed or explicitly triaged.
    * **Container Image Scan:** The built Docker image MUST be scanned for OS-level vulnerabilities.
2. **SBOM Generation:** A Software Bill of Materials (SBOM) in SPDX or CycloneDX format MUST be generated for every production build. This artifact must be stored alongside the container image.
3. **Immutable Artifacts:** Once a container image is built and tagged for a specific version, it is considered immutable. It MUST NOT be modified. Any change requires a new build with a new version tag.

## 5. Reliability Engineering Principles

We build services that our users can rely on. This is achieved through engineering discipline, not hope.

### 5.1. Service Level Objectives (SLOs)

* **Definition:** An SLO is a target value or range of values for a service level that is measured by a Service Level Indicator (SLI). Every user-facing service MUST have defined SLOs for availability and latency.
  * **SLI (Indicator):** A quantitative measure of some aspect of the service (e.g., the ratio of successful HTTP requests).
  * **SLO (Objective):** The target for that SLI (e.g., 99.9% of requests successful over a 28-day window).
* **Procedure:** SLOs are defined in collaboration between product owners and engineering teams and are documented in a central registry.

### 5.2. Error Budgets

* **Definition:** The Error Budget is the inverse of the SLO (`100% - SLO`). For a 99.9% availability SLO, the error budget is 0.1%.
* **Purpose:** The error budget is the acceptable level of unreliability that a service can have. It empowers teams to balance innovation and reliability.
  * **If the service is operating within its error budget:** The team is allowed to ship new features and take calculated risks.
  * **If the service has exhausted its error budget:** All development on new features for that service HALTS. The team's priority becomes improving reliability (fixing bugs, improving tests, enhancing infrastructure) until the service is back within its budget.

## 6. Incident Response Protocol

When incidents happen, we respond in a calm, structured, and blameless manner.

1. **Detection & Alerting:** Incidents are primarily detected via automated alerts triggered by SLO violations.
2. **Incident Commander (IC):** For any significant incident, an Incident Commander is designated. The IC does not fix the problem directly but coordinates the response, communication, and resources.
3. **Communication:** A dedicated communication channel (e.g., a Slack channel) is opened. All communication related to the incident occurs there. Regular updates are provided to stakeholders.
4. **Priority #1: Mitigate:** The immediate priority is always to **stop the user impact** and restore service, even if it means rolling back a change or using a temporary fix. Understanding the root cause comes later.
5. **Blameless Postmortem:** Every significant incident MUST be followed by a blameless postmortem. The goal is to understand the systemic causes of the failure and produce actionable items to prevent its recurrence. The focus is on "what went wrong," not "who was wrong."
6. **Documentation:** All incidents and postmortems are documented in a central repository. This knowledge is shared with the team to improve future responses.

## 7. Continuous Improvement

Continuous improvement is a core principle of our DevSecOps and SRE practices.

* **Regular Reviews:** All processes, tools, and practices are reviewed regularly (at least quarterly) to identify areas for improvement.
* **Feedback Loops:** Teams are encouraged to provide feedback on the DevSecOps and SRE practices. This feedback is used to refine and enhance our protocols.
* **Training & Knowledge Sharing:** Regular training sessions and knowledge-sharing events are held to keep all team members up-to-date with the latest practices, tools, and technologies in DevSecOps and SRE.
* **Innovation Time:** Teams are encouraged to allocate time for innovation and experimentation with new tools, technologies, and practices that can enhance our DevSecOps and SRE capabilities.

## 8. Related Resources and Links

* [GCS DevOps Standards]
