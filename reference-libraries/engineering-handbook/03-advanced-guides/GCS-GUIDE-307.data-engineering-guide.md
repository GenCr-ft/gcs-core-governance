---
docId: GCS-GUIDE-307
title: "The Data Engineering Guide"
version: 1.0.0
status: Draft
date: 2025-06-18
authors:
  - "Technical Governance"
knowledgeGuardian:
  - "Data Engineering Lead"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/03-advanced-guides/GCS-GUIDE-307.data-engineering-guide.md
metadata:
  lifecycle-stage: approved
  domain: engineering
  doc-type: guide
  scope: studio-wide
  security-classification: l2_confidential
  keywords:
    - "data-engineering"
    - "etl"
    - "elt"
    - "data-warehouse"
    - "data-governance"
---

# The Data Engineering Guide

## 1. Objective

This guide establishes the standard principles and practices for designing, building, and maintaining large-scale data systems and pipelines at the studio. Its purpose is to ensure our data is handled in a reliable, scalable, secure, and well-governed manner, treating data as a first-class product.

## 2. Core Principles of Data Engineering

All data engineering work MUST adhere to these foundational principles.

* **Data as a Product:** Every dataset or data pipeline is treated as a product. It must have a clear owner, well-defined quality standards (SLOs), and documentation for its consumers.
* **Schema on Write:** For our structured data warehouses, we enforce "schema on write." Data MUST be validated and conform to a predefined schema *before* it is loaded. This ensures data quality and consistency.
* **Data Governance by Default:** Data quality, security, and lineage are not afterthoughts. They must be designed into every data pipeline from the start.

## 3. Data Pipeline Design Protocol (ETL/ELT)

This protocol defines the standard steps for building a new data pipeline. Our studio favors an **ELT (Extract, Load, Transform)** approach for its flexibility.

### 3.1. Step 1: Extract

* **Source Connection:** Use approved connectors and libraries for accessing source systems (e.g., production databases, third-party APIs).
* **Extraction Method:** Whenever possible, use incremental extraction methods (based on timestamps or version numbers) to avoid full data dumps, which are inefficient and costly.
* **Data Format:** Raw extracted data should be kept in its original format or a simple, open format like JSON or Parquet.

### 3.2. Step 2: Load

* **Target:** The standard destination for raw, unprocessed data is our central data lake (e.g., an S3 bucket).
* **Structure:** Data in the data lake MUST be partitioned (e.g., by date) to allow for efficient querying and processing.
* **Idempotency:** The load process must be idempotent. Running it multiple times with the same source data must not create duplicate records in the raw layer.

### 3.3. Step 3: Transform

* **Tooling:** The standard tool for data transformation is **dbt (Data Build Tool)**. All transformations MUST be written as version-controlled SQL models.
* **Modeling Layers:** Transformations are organized into layers within our data warehouse:
    1. **Staging:** Raw data is cleaned, lightly transformed (e.g., casting types, renaming columns), and prepared for modeling. Staging models have a 1:1 relationship with source tables.
    2. **Intermediate:** Complex business logic and joins are performed here to create reusable data components.
    3. **Marts:** Final, aggregated data models tailored for specific business use cases (e.g., `dim_players`, `fct_daily_revenue`). These are the "data products" consumed by analysts and other services.
* **Testing:** Every transformation model MUST be accompanied by data tests (e.g., uniqueness, not-null constraints, accepted values) written within the dbt framework.

## 4. Data Warehousing & Modeling

* **Modeling Technique:** Our studio standard for data marts is **Dimensional Modeling (Kimball methodology)**. We build models around business processes, creating fact and dimension tables to form star schemas.
* **Naming Conventions:** All tables, columns, and models MUST adhere to the studio's official data naming conventions (e.g., `dim_` for dimensions, `fct_` for facts, snake_case for column names).
* **Documentation:** Every model in our data warehouse MUST be documented (describing its purpose, columns, and lineage) directly within the dbt project.
* **Version Control:** All dbt models and transformations MUST be stored in a version control system (e.g., Git). Changes to models MUST go through a pull request process with code reviews.
* **Data Marts:** Data marts are the final, curated datasets that are ready for consumption by analysts and data scientists. Each data mart MUST have:
  * A clear owner (data steward)
  * Defined Service Level Objectives (SLOs) for freshness and accuracy
  * Documentation in the data catalog
  * Automated tests to ensure data quality
* **Data Freshness:** Data marts MUST be updated regularly (e.g., daily, hourly) based on business needs. The frequency of updates MUST be defined in the dbt project and monitored for compliance.
* **Data Retention:** Data in the data warehouse MUST have defined retention policies. Historical data should be archived or purged according to business requirements.
* **Data Access:** Access to data marts MUST be controlled through role-based access control (RBAC). Sensitive data MUST be masked or encrypted as per the studio's data security policies.
* **Data Lineage:** All data transformations MUST maintain clear lineage from source to final data mart. This is automatically captured by dbt and visualized in our data cataloging tool.
* **Data Cataloging:** All data marts MUST be registered in our central data catalog. This includes metadata such as:
  * Owner (data steward)
  * Description
  * SLOs (e.g., freshness, accuracy)
  * Access controls
  * Change history
* **Data Discovery:** Analysts and data consumers MUST be able to discover data products through our data cataloging tool, which provides search, filtering, and lineage visualization capabilities.

## 5. Data Governance Framework

### 5.1. Data Quality

* **Automated Testing:** Data quality checks MUST be integrated and run automatically as part of the dbt transformation pipeline.
* **Alerting:** Build failures or data test failures MUST trigger an alert to the data engineering team.
* **Monitoring:** Use monitoring tools to track data freshness, volume, and anomalies. Data pipelines MUST have defined Service Level Objectives (SLOs) for freshness and accuracy.
* **Data Profiling:** Regular profiling of data in the warehouse is required to identify anomalies, trends, and potential issues. This can be done using tools like Great Expectations or custom dbt tests.

### 5.2. Data Cataloging & Lineage

* **Cataloging:** All data marts are automatically registered in our central data catalog.
* **Lineage:** End-to-end data lineage (from source to dashboard) is automatically generated and visualized by our tooling. This is crucial for impact analysis and debugging.
* **Metadata Management:** Each data product MUST have associated metadata, including:
  * Owner (data steward)
  * Description
  * SLOs (e.g., freshness, accuracy)
  * Access controls
  * Change history
* **Data Discovery:** Analysts and data consumers MUST be able to discover data products through our data cataloging tool, which provides search, filtering, and lineage visualization capabilities.

### 5.3. Data Security & Access Control

* **Classification:** Data MUST be classified at the column level (e.g., PII, Public, Confidential).
* **Access Control:** Access to data in the warehouse is role-based (RBAC) and managed through our central data governance tools. Access is granted on a need-to-know basis.
* **Auditing:** All access to sensitive data is logged and monitored. Regular audits are performed to ensure compliance with our data governance policies.

## 6. Tools and Technologies

* **Data Lake:** AWS S3 or Google Cloud Storage for raw data storage.
* **Data Warehouse:** Snowflake or BigQuery as our primary data warehouse solution.
* **ETL/ELT Tooling:** dbt for transformations, Airflow or Prefect for orchestration.
* **Data Catalog:** Amundsen or DataHub for data discovery and lineage visualization.
* **Monitoring & Alerting:** Use tools like Grafana or DataDog to monitor data pipelines and alert on failures or anomalies.

## 7. Responsibilities

* **Data Engineering Team:** Responsible for building, maintaining, and optimizing data pipelines, ensuring data quality, and adhering to governance standards.
* **Data Analysts:** Consume data products, provide feedback on data quality, and collaborate with the data engineering team to refine models.
* **Data Governance Lead:** Oversees data governance policies, ensures compliance, and manages access control.

## 8. Related Resources and Links

* [dbt Documentation](https://docs.getdbt.com/docs/introduction)
* [Data Governance Framework](https://example.com/data-governance-framework)
* [Dimensional Modeling Guide](https://example.com/dimensional-modeling-guide)
* [Data Cataloging Tool](https://example.com/data-catalog-tool)
* [Data Engineering Best Practices](https://example.com/data-engineering-best-practices)

## 9. Versioning and Change Management

* This guide is versioned according to the studio's [Semantic Versioning Standard](https://example.com/semantic-versioning-standard).
