---
docId: GCS-GUIDE-503
title: "The Cost Management (FinOps) Guide"
version: 1.0.0
status: Draft
date: 2025-06-19
authors:
  - "Technical Governance"
  - "Finance Governance"
knowledgeGuardian:
  - "Head of Engineering"
  - "Finance Business Partner"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/05-governance-and-organization/GCS-GUIDE-503.finops-guide.md
metadata:
  lifecycle-stage: approved
  domain: engineering
  doc-type: guide
  scope: studio-wide
  security-classification: l2_confidential
  keywords:
    - "finops"
    - "cloud-cost"
    - "governance"
    - "finance"
    - "budget"
---

# The Cost Management (FinOps) Guide

## 1. Objective

This guide establishes the official studio framework for Cloud Financial Management, also known as **FinOps**. Its purpose is to instill a culture of financial accountability within our engineering practices, ensuring that we build and operate systems in a cost-effective manner. FinOps is a collaborative effort between engineering, finance, and product teams to manage our cloud costs effectively.

## 2. Core Principles of FinOps

Our approach to FinOps is built on these core principles:

* **Collaboration is Key:** Teams must collaborate. Engineering, finance, and product teams work together to make trade-offs between speed, cost, and quality.
* **Everyone Takes Ownership:** Cloud cost is a shared responsibility. Every engineer is accountable for the cost of the resources their services consume.
* **Centralized Governance, Decentralized Execution:** A central FinOps team provides governance, best practices, and tooling, but the individual development teams are empowered to manage and optimize their own costs.
* **Data-Driven Decisions:** All cost optimization decisions must be based on timely and accurate data.

## 3. The FinOps Lifecycle Protocol

Our FinOps practice follows a continuous, iterative lifecycle.

### 3.1. Phase 1: Inform (Visibility and Allocation)

The first step is to understand where our money is going.

* **Tagging and Labeling Standard:** All cloud resources MUST be tagged with, at a minimum: `project`, `service`, and `owner`. This is a mandatory requirement enforced by automated policies. Untagged resources will be flagged for termination.
* **Cost Dashboards:** We use a centralized cost visualization tool (e.g., the cloud provider's cost explorer, or a dedicated tool like Cloudability/Harness) to provide real-time visibility into spending. Each team has access to a dashboard filtered to their specific projects and services.
* **Budgeting and Forecasting:** Each team works with the FinOps team to set a quarterly budget for their cloud spend. Forecasts are reviewed monthly.

### 3.2. Phase 2: Optimize (Cost Reduction and Efficiency)

Once we have visibility, we can optimize.

* **Rightsizing Resources:** Teams are responsible for regularly reviewing the utilization of their resources (e.g., virtual machines, databases) and rightsizing them to match the actual workload. Unused or underutilized resources MUST be terminated.
* **Leveraging Reserved Instances & Savings Plans:** For services with predictable, steady-state workloads, the FinOps team will centrally purchase Reserved Instances (RIs) or Savings Plans to significantly reduce costs.
* **Architectural Optimization:** During design reviews, cost must be considered as a non-functional requirement. This includes choosing cost-effective storage tiers, leveraging serverless architectures where appropriate, and designing for scalability to avoid over-provisioning.

### 3.3. Phase 3: Operate (Continuous Improvement)

FinOps is an ongoing process, not a one-time project.

* **Automated Cost Anomaly Detection:** We use automated tools to detect sudden spikes in spending, which trigger alerts to the responsible team and the FinOps team.
* **Cost as a CI/CD Metric:** Cost estimation tools are integrated into our CI/CD pipelines [cite: GCS-GUIDE-202]. A Pull Request that is predicted to cause a significant cost increase will require an additional layer of approval.
* **Regular Reviews:** Cost optimization is a standing agenda item in team meetings and sprint retrospectives [cite: GCS-GUIDE-403].

## 4. Standard Tooling

* **Cost Visualization:** Cloud Provider's Native Cost Explorer / Harness Cloud Cost Management.
* **Infrastructure as Code (IaC):** Terraform / OpenTofu for provisioning resources, which allows for cost estimation before deployment.
* **Automated Tagging Enforcement:** Custom scripts or provider-specific policy engines.
