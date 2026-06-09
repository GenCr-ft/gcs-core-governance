---
docId: GCS-GUIDE-304
title: "The Observability & Monitoring Guide"
version: 1.0.0
status: Draft
date: 2025-06-18
authors:
  - "Technical Governance"
knowledgeGuardian:
  - "SRE Lead"
  - "DevOps Lead"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/03-advanced-guides/GCS-GUIDE-304.observability-guide.md
metadata:
  lifecycle-stage: approved
  domain: engineering
  doc-type: guide
  scope: studio-wide
  security-classification: l2_confidential
  keywords:
    - "observability"
    - "monitoring"
    - "metrics"
    - "logs"
    - "tracing"
    - "prometheus"
    - "grafana"
---

# The Observability & Monitoring Guide

## 1. Objective

This guide establishes the studio's standard practices and tools for achieving system observability. Its purpose is to ensure that all our production systems are instrumented to provide the necessary data to understand their behavior, diagnose problems, and answer questions about their state without needing to ship new code.

Observability is a core component of our reliability engineering practices [cite: GCS-GUIDE-202].

## 2. Monitoring vs. Observability: A Critical Distinction

It is crucial to understand the difference between these two concepts:

* **Monitoring:** The practice of collecting and analyzing data from predefined metrics and logs to watch for *known* failure modes. Monitoring tells you *whether* a system is working. **It is reactive.**
* **Observability:** The ability to ask arbitrary questions about your system's behavior from the outside, without having to know in advance what you'll need to ask. Observability lets you understand *why* a system isn't working. **It is proactive and essential for debugging unknown issues in complex, distributed systems.**

Our studio strives for **observability**, which is achieved through the proper implementation of the three pillars below.

## 3. The Three Pillars of Observability

Every service deployed in the studio MUST be instrumented to expose these three types of telemetry data.

### 3.1. Logs (The "What")

* **Definition:** Logs are immutable, timestamped records of discrete events that happened over time. They provide detailed, contextual information about a specific event.
* **Standard Protocol:**
  * All logs MUST be written to `stdout` / `stderr` in a **structured format**, specifically **JSON**. Unstructured, human-readable strings are forbidden in production as they are not machine-parsable.
  * Logs MUST include a consistent set of fields: a timestamp, a severity level (`INFO`, `WARN`, `ERROR`), the service name, and the event-specific payload.
  * NEVER log sensitive information (PII, passwords, API keys) [cite: GCS-GUIDE-306].

### 3.2. Metrics (The "How Much")

* **Definition:** Metrics are a numerical representation of data measured over intervals of time. They are aggregatable and ideal for building dashboards and triggering alerts.
* **Standard Protocol:**
  * Services MUST expose key performance indicators as metrics. We standardize on the four "Golden Signals":
        1. **Latency:** The time it takes to serve a request.
        2. **Traffic:** A measure of how much demand is being placed on your system (e.g., requests per second).
        3. **Errors:** The rate of requests that fail.
        4. **Saturation:** How "full" your service is (e.g., CPU or memory utilization).
  * Metrics MUST be exposed via a `/metrics` endpoint in a format compatible with our standard stack.

### 3.3. Distributed Traces (The "Where")

* **Definition:** A trace represents the end-to-end journey of a single request as it moves through all the services in our distributed system. Each step in the journey is a "span".
* **Standard Protocol:**
  * All services MUST participate in the distributed trace. They must be ableto receive a trace context from an incoming request and propagate it to any downstream requests they make.
  * This allows us to visualize the entire call graph for a request, pinpointing which service is responsible for errors or high latency.

## 4. The Standard Observability Stack

To ensure consistency, we use a standardized, open-source stack for collecting and analyzing telemetry data.

* **Metrics:** **Prometheus** is our standard for collecting and storing time-series metric data.
* **Visualization:** **Grafana** is our standard for creating dashboards and visualizing data from Prometheus and other sources.
* **Log Aggregation:** **Loki** (or a compatible alternative like Elasticsearch) is used to aggregate logs from all services.
* **Distributed Tracing:** **Jaeger** (or a compatible OpenTelemetry-based tool) is our standard for collecting and visualizing traces.

## 5. Implementation Protocol

1. **Instrumentation by Default:** All new services MUST be instrumented with libraries that expose logs, metrics, and traces according to the protocols defined in this guide **before** their first deployment to production.
2. **Dashboarding:** Every service MUST have a corresponding Grafana dashboard displaying its key health metrics (the Golden Signals).
3. **Alerting on SLOs:** Alerts SHOULD be configured based on the violation of Service Level Objectives (SLOs), not on raw metrics. For example, alert when the error budget is burning too fast [cite: GCS-GUIDE-202].
4. **Centralized Configuration:** All observability configurations (e.g., Prometheus scrape configs, Grafana dashboards) MUST be stored in a central repository (`gcs-observability-configs`) and version-controlled.
5. **Review and Approval:** All observability configurations MUST be reviewed and approved by the SRE team before deployment to production, following Protocol S1: Feedback & Approval.
6. **Documentation:** Each service MUST include documentation on its observability setup, including:
    * The metrics it exposes.
    * The logs it generates.
    * How to interpret its traces.
    * Links to its Grafana dashboard.
7. **Training:** All developers MUST receive training on how to use the observability stack effectively, including how to query logs, visualize metrics, and analyze traces.

## 6. Responsibilities

* **SRE Team:** Responsible for maintaining the observability stack, ensuring it is properly configured, and providing support to developers.
* **Development Teams:** Responsible for instrumenting their services according to this guide, maintaining their observability configurations, and ensuring their services are observable by default.
* **Product Owners:** Responsible for defining SLOs and ensuring that observability practices align with business objectives.
