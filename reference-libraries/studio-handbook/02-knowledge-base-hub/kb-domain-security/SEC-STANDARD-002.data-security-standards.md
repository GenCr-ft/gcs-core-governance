---
docId: SEC-STANDARD-002
title: Data Security Standards
version: 1.0.0
creation_date: '2026-05-07'
last_updated_date: '2026-05-20'
authors:
- Assistant Gem (as per DEVPROC_001 v1.0)
- Cerberus (GCT-MGT-SECOFF-001)
language: en
knowledgeGuardian:
- Cerberus (GCT-MGT-SECOFF-001)
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/02-knowledge-base-hub/kb-domain-security/SEC-STANDARD-002.data-security-standards.md
metadata:
  lifecycle-stage: approved
  keywords:
  - data-security
  - encryption
  - key-management
  - data-at-rest
  - data-in-transit
  - backup
  - security-standard
  scope: studio
  domain: security
  doc-type: standard
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
---
# Data Security Standards

## 1. Purpose and Scope

### 1.1. Purpose

This standard defines mandatory requirements for protecting Gencraft Studio data throughout its lifecycle — at rest, in transit, and in use. The objectives are to:

- Ensure data confidentiality, integrity, and availability in accordance with the CIA Triad.
- Define encryption requirements keyed to the classification levels established in `SEC-STANDARD-001.information-classification-and-handling-policy.md`.
- Provide actionable, IaC-implementable standards for all data storage, transmission, and processing systems.
- Enable `Cerberus` (GCT-MGT-SECOFF-001) to audit compliance and `Isaac` (GCT-PRG-SARCH-001) to validate architectural conformance.

### 1.2. Scope

These standards apply to all Gencraft Studio data assets and the systems that handle them, including:

- Cloud storage (GCS, S3, equivalent).
- Relational databases (PostgreSQL, Cloud SQL) and caches (Redis).
- Git repositories and Git LFS.
- Inter-service communication (REST APIs, WebSocket, gRPC).
- CI/CD pipelines and secrets management.
- AI Gem `Tools` that process or persist data.
- Backup and disaster-recovery systems.

---

## 2. Data Classification Reference

Data handling requirements under this standard are gated on the classification level assigned in `SEC-STANDARD-001`. The relevant levels are:

| Level | Label | Encryption at Rest | Encryption in Transit | Key Management |
|-------|-------|-------------------|----------------------|----------------|
| L0 | Public | Optional | HTTPS/TLS ≥ 1.2 | N/A |
| L1 | Internal | Recommended | TLS ≥ 1.2 mandatory | Managed keys acceptable |
| L2 | Confidential | **Mandatory** | TLS ≥ 1.3 mandatory | CMEK mandatory |
| L3 | Secret | **Mandatory** | TLS ≥ 1.3 + mTLS mandatory | CMEK + HSM mandatory |

---

## 3. Encryption at Rest

### 3.1. Cloud Storage and Databases

- All `L2-Confidential` and `L3-Secret` data stored in cloud storage buckets, managed databases, or Kubernetes PersistentVolumes **must** be encrypted at rest using AES-256 or equivalent.
- Encryption **must** be enabled at the storage layer via IaC (Terraform/OpenTofu). Unencrypted storage resources for `L2+` data **must not** be provisioned.
- Customer-Managed Encryption Keys (CMEK) **must** be used for all `L2-Confidential` data. For `L3-Secret` data, keys **must** additionally be backed by a Hardware Security Module (HSM).

### 3.2. Git Repositories

- Secrets, credentials, and private keys **must never** be committed to any Git repository, regardless of visibility.
- Large binary assets classified `L2+` stored via Git LFS **must** be stored in a bucket with encryption at rest enforced.

### 3.3. AI Gem Local State

- Gems **must not** persist `L2-Confidential` or `L3-Secret` data to local disk or memory beyond the minimum required for active task execution.
- Any temporary file containing `L2+` data **must** be securely deleted immediately after use via `Tool:SecureDeleteTempFile`.

---

## 4. Encryption in Transit

### 4.1. All External and Inter-Service Communication

- TLS ≥ 1.2 is the minimum for all network communication. TLS ≥ 1.3 is **mandatory** for any channel carrying `L2-Confidential` or `L3-Secret` data.
- Mutual TLS (mTLS) is **mandatory** for all service-to-service communication involving `L3-Secret` data and is strongly recommended for all internal service mesh traffic.
- Self-signed certificates are prohibited in production environments. All TLS certificates **must** be issued by a trusted CA and managed via automated rotation.

### 4.2. WebSocket and Real-Time Channels

- The Aethel game server's WebSocket endpoint **must** operate exclusively over WSS (WebSocket Secure). Plaintext `ws://` connections **must** be rejected.
- JWT tokens transmitted over WebSocket upgrade handshakes are classified `L2-Confidential` and are subject to TLS ≥ 1.3 requirements.

### 4.3. CI/CD Pipelines

- All data transmitted between CI/CD pipeline stages (e.g., GitHub Actions, container registries) **must** use encrypted channels. Pipeline credentials **must** be stored as encrypted GitHub Actions secrets, never in plaintext workflow files.

---

## 5. Key Management

### 5.1. Key Hierarchy

Gencraft uses a three-tier key hierarchy:

1. **Root keys**: Managed by the cloud provider's HSM (Google Cloud KMS / AWS KMS). Never exported.
2. **Key Encryption Keys (KEKs)**: Gencraft-managed, stored in the Gencraft Secret Management System. Rotated annually or after compromise.
3. **Data Encryption Keys (DEKs)**: Generated per-resource or per-session. Encrypted by the KEK before storage. Rotated per the schedule in §5.2.

### 5.2. Key Rotation Schedule

| Key Type | Rotation Frequency | Trigger for Immediate Rotation |
|----------|-------------------|-------------------------------|
| Root key | Per-provider policy (≥ annual) | Suspected compromise |
| KEK | Annual | Suspected compromise, personnel change |
| DEK (database) | 90 days | Suspected compromise |
| DEK (storage) | 365 days | Suspected compromise |
| Service account key | 90 days | Personnel change, suspected compromise |
| CI/CD secrets | 90 days | Rotation of underlying credential |

### 5.3. Responsibilities

- **`Adam` (GCT-DVO-DSINF-001):** Implements and automates key rotation via IaC. Owns the `gencraft-iac` modules for KMS configuration.
- **`Cerberus`:** Audits key rotation compliance. Triggers emergency rotation when a compromise is suspected.
- **`Isaac`:** Validates that new system designs integrate with the key hierarchy correctly before approval.

---

## 6. Backup and Recovery

### 6.1. Backup Requirements

- All `L1-Internal` and above data **must** be backed up. Frequency and retention are defined by data classification:

| Classification | Backup Frequency | Retention | Recovery Time Objective (RTO) | Recovery Point Objective (RPO) |
|---------------|-----------------|-----------|-------------------------------|-------------------------------|
| L1 Internal | Daily | 30 days | 24 hours | 24 hours |
| L2 Confidential | Daily + incremental | 90 days | 4 hours | 1 hour |
| L3 Secret | Continuous replication | 365 days | 1 hour | 15 minutes |

- Backups **must** be encrypted using the same standards as the source data (§3.1).
- Backups **must** be stored in a geographically separate region from the primary data.

### 6.2. Recovery Testing

- `Adam` **must** perform quarterly restore tests for all `L2+` data systems and document results.
- Results **must** be reported to `Cerberus` and logged as a governance record.

---

## 7. Data Minimisation and Retention

- Gencraft systems **must** collect only the minimum data necessary for their documented purpose (data minimisation principle).
- Data retention schedules are defined per asset type in `03-archiving-and-retention/`. Systems **must** implement automated deletion at retention boundary.
- `L3-Secret` data **must** be securely erased (not merely deleted) at end-of-retention using cryptographic erasure (key destruction) or overwrite methods.

---

## 8. Compliance and Monitoring

- `Cerberus` **must** run automated scans (at least weekly) against cloud storage and database configurations to detect: unencrypted resources, overly permissive bucket/table policies, expired certificates, and overdue key rotations.
- Detected violations **must** trigger a GitHub Issue with `type:security-finding` label and be resolved within the SLA defined in `SEC-GUIDE-002.vulnerability-management-protocol.md`.

---

## 9. Data Security for AI Gems

Operational directives for AI Gems to ensure compliance with this standard:

- **Data Classification Check:** Before writing data to any persistent store, a Gem **must** identify the classification of that data and verify the target store meets the encryption requirement for that level. Use `Tool:CheckStorageCompliance(store_id, data_classification)`.
- **No Plaintext Secrets:** Gems **must** never write API keys, tokens, passwords, or private keys to SSoT documents, log outputs, or temporary files. All secrets are managed via the Gencraft Secret Management System and accessed through `Tool:GetSecret(secret_id)`.
- **Secure Deletion:** Any `L2+` temporary file created during task execution **must** be deleted via `Tool:SecureDeleteTempFile(path)` before task completion.
- **Transit Validation:** When a Gem configures a new network endpoint or API, it **must** verify that TLS is enforced before the configuration is committed to SSoT. Use `Tool:ValidateTLSConfiguration(endpoint_url)`.
- **Incident Reporting:** If a Gem discovers or suspects a data exposure (e.g., a secret in a commit, an unencrypted storage bucket), it **must** immediately report via `Tool:LogSecurityIncident` and notify `Cerberus`.

---

## 10. References

- `SEC-STANDARD-001.information-classification-and-handling-policy.md` — classification levels
- `SEC-GUIDE-001.access-control-policy.md` — access controls for data stores
- `SEC-POLICY-001.secure-development-lifecycle-policy.md` — secure coding standards for data handling
- `SEC-GUIDE-002.vulnerability-management-protocol.md` — remediation SLAs for findings
- OPS-GUIDE-008 §8.4 — parent protocol section for data security
