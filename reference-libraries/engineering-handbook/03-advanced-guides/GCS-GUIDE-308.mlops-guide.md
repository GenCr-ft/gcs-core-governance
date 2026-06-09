---
docId: GCS-GUIDE-308
title: "The MLOps (ML Engineering) Guide"
version: 1.0.0
status: Draft
date: 2025-06-18
authors:
  - "Technical Governance"
knowledgeGuardian:
  - "ML Engineering Lead"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/03-advanced-guides/GCS-GUIDE-308.mlops-guide.md
metadata:
  lifecycle-stage: approved
  domain: engineering
  doc-type: guide
  scope: studio-wide
  security-classification: l2_confidential
  keywords:
    - "mlops"
    - "machine-learning"
    - "ai"
    - "ci-cd-ml"
    - "model-lifecycle"
---

# The MLOps (ML Engineering) Guide

## 1. Objective

This guide establishes the studio's standard practices for operationalizing the entire Machine Learning (ML) lifecycle. Its purpose is to bring software engineering discipline to ML projects, ensuring that our models are reproducible, testable, reliable, and continuously monitored in production. MLOps is the application of our DevOps culture [cite: GCS-GUIDE-202] to the unique challenges of Machine Learning.

## 2. The MLOps Lifecycle Protocol

All ML projects MUST follow this structured lifecycle to ensure consistency and quality.

### 2.1. Step 1: Data Management & Versioning

* **Data is Code:** Datasets are treated as critical source artifacts. All datasets used for training or evaluation MUST be version-controlled.
* **Standard Protocol:** We use **DVC (Data Version Control)** in conjunction with Git. Git stores the metadata and pointers, while DVC handles the storage and versioning of the large data files in a designated cloud storage.
* **Feature Stores:** For projects with reusable features, a centralized **Feature Store** should be considered to avoid duplication of effort and ensure consistency across models.

### 2.2. Step 2: Model Development & Experiment Tracking

* **Reproducibility:** Experiments must be reproducible. All training runs MUST be logged.
* **Standard Protocol:** We use **MLflow Tracking** to log experiment parameters, code versions, metrics, and output artifacts for every training run. This allows us to compare results and revert to previous versions.
* **Notebooks for Exploration Only:** Jupyter notebooks are excellent tools for initial data exploration and prototyping. However, all production-worthy training code MUST be refactored into version-controlled Python scripts or modules.

### 2.3. Step 3: Model Training & Versioning (CI/CD for ML)

* **Continuous Training (CT):** We implement CI/CD pipelines specifically for ML models. A new model version is automatically trained and evaluated when there is a significant change in the code or the underlying data.
* **Model Registry:** Trained and validated models are registered in our central **MLflow Model Registry**. The registry manages model versions, stages (Staging, Production), and associated metadata.

### 2.4. Step 4: Model Deployment

* **Deployment as Code:** Model deployment infrastructure is managed as code. Models are served as containerized services on our Kubernetes platform [cite: GCS-GUIDE-202].
* **Deployment Strategies:**
  * **Canary Deployment:** Gradually roll out a new model version to a small subset of users to evaluate its performance before a full release.
  * **Shadow Deployment:** Deploy the new model alongside the old one, feeding it the same production traffic but not acting on its predictions. This allows for performance comparison without user impact. This is our preferred strategy for validating a new model version.

### 2.5. Step 5: Model Monitoring

* **ML Systems Fail Silently:** Unlike traditional software, ML models can fail silently in production due to changes in the data distribution. Continuous monitoring is therefore non-negotiable.
* **Standard Protocol:** We monitor three key aspects:
    1. **Model Performance:** Track business metrics (e.g., click-through rate) and model-specific metrics (e.g., accuracy, precision-recall).
    2. **Data Drift:** Monitor the statistical properties of the input data to detect if the production data has started to differ significantly from the training data.
    3. **Prediction/Outlier Detection:** Monitor the distribution of model predictions to detect unexpected shifts or outliers.
* **Alerting:** Alerts MUST be configured to notify the team of significant model performance degradation or data drift, triggering a potential retraining cycle.

## 3. Ethical AI Protocol

All ML models must be developed in accordance with our studio's commitment to responsible AI. Before deployment, every model must pass an ethical review checklist.

* **Fairness & Bias:** Has the model been evaluated for biased behavior across different user subgroups?
* **Explainability:** Can we reasonably explain the model's predictions, especially for critical decisions?
* **Accountability:** Is there a clear owner for the model and a process for addressing issues?
* **Transparency:** Are users informed when they are interacting with an AI system?

## 4. Standard MLOps Tooling

* **Data Versioning:** DVC
* **Experiment Tracking & Model Registry:** MLflow
* **Model Serving:** Seldon Core (on Kubernetes)
* **Workflow Orchestration:** Kubeflow Pipelines or Argo Workflows
* **Monitoring:** Prometheus and Grafana for metrics, Seldon Core for model-specific monitoring
* **CI/CD:** GitHub Actions or Jenkins for automating training, testing, and deployment pipelines

## 5. Conclusion

This guide provides a comprehensive framework for implementing MLOps practices in our studio. By adhering to these standards, we ensure that our ML projects are robust, maintainable, and aligned with our ethical principles. Continuous improvement and adaptation of these practices will be essential as the field of Machine Learning evolves.
