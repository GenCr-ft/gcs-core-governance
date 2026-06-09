---
docId: ARC-ADR-204
title: "Golden Path Decision: Observability Strategy"
version: "1.0.0"
date: "2025-07-12"
authors:
  - "DevOps Crew (EE)"
  - "Architecture Crew (CC)"
knowledgeGuardian: "Édouard (DevOps Crew)"
status: "Approved"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/records/adrs/adr-studio-001/golden-path-ts-backend/ARC-ADR-204.observability-strategy.md
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

# ADR-204: Golden Path Decision on Observability Strategy

## 1. Context

Following the decisions on our core application architecture, this ADR addresses the critical "blind spot" of observability. A service running in production without proper logging, metrics, and tracing is a black box, making debugging difficult, performance analysis impossible, and incident response slow. We need a standardized approach to ensure all our services are observable by default.

## 2. Decision Drivers

* **Reliability:** Enable rapid debugging and root cause analysis during incidents.
* **Performance Monitoring:** Proactively identify performance bottlenecks and resource saturation.
* **Proactive Alerting:** Establish a consistent data source for our monitoring and alerting systems.
* **Consistency:** Ensure that all services, regardless of the team that built them, can be monitored using a single set of tools and dashboards.

## 3. Considered Options

1. **Team-Specific Strategy:** Allow each development team to choose and implement its own observability stack (logging libraries, metrics formats, etc.). This option was rejected as it would create operational chaos and prevent a unified view of system health.
2. **Standardized "Observability Kit":** Mandate a specific set of formats and core libraries for the three pillars of observability (Logging, Metrics, Tracing) to be included in the Golden Path. This ensures consistency from day one.

## 4. Decision Outcome

**Decision:** We will adopt the **Standardized "Observability Kit"** approach (Option 2).

**Decision 4.1: Logging**

* **Loi:** All services MUST produce **structured logs in JSON format** written to `stdout`. Logs MUST include standard fields such as a timestamp, log level, message, and a context object for structured data.
* **Justification:** JSON logs are machine-parsable, allowing for efficient ingestion, indexing, and querying in a centralized logging platform (e.g., OpenSearch, Datadog).
* **Implementation:** The Golden Path template for NestJS will include a pre-configured `LoggerModule` that enforces this JSON output format.

**Decision 4.2: Metrics**

* **Loi:** All services MUST expose a standard `/metrics` endpoint that presents application metrics in the **Prometheus exposition format**.
* **Justification:** Prometheus is the de facto industry standard for metrics in cloud-native ecosystems. This allows for seamless integration with our planned monitoring stack.
* **Implementation:** The template will include and configure a library such as `prom-client` to automatically instrument standard Node.js and NestJS metrics (e.g., event loop lag, memory usage) and expose the endpoint.

**Decision 4.3: Distributed Tracing**

* **Loi:** All services MUST be instrumented for distributed tracing using the **OpenTelemetry** standard.
* **Justification:** OpenTelemetry is the open-source, vendor-neutral standard for observability, preventing vendor lock-in. It is essential for tracing requests across multiple microservices to understand complex user flows and identify performance issues in a distributed system.
* **Implementation:** The template will include the basic OpenTelemetry SDK and auto-instrumentation packages for NestJS, ensuring that every incoming request and outgoing API call is traced by default.

## 5. Consequences

* **Positive:**
  * Provides uniform observability across all backend services from day one.
  * Drastically simplifies the setup of centralized monitoring, logging, and alerting.
  * Reduces the mean time to resolution (MTTR) for production incidents.
  * Empowers developers by giving them a standard way to understand their service's behavior in production.
* **Negative:**
  * Adds a small amount of boilerplate dependencies and configuration to every new service. This is mitigated by its inclusion and pre-configuration in the `gct-service-template-ts` template.
  * Teams lose the flexibility to choose alternative observability libraries. This is a deliberate and accepted trade-off for studio-wide consistency.
