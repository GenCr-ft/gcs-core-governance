---
docId: GOV-PROTO-S8-001
title: S8 Information Security Management — Agent Protocol Reference
version: 1.0.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: protocol
  intended-audience: [ai-agents]
  security-classification: l2_confidential
  source_doc: OPS-GUIDE-008
  source_doc_version: "1.0.0"
  last_verified: "2026-06-28"
---
# S8 Information Security Management --- Agent Reference

Distilled from `reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-008.s8-information-security-management.md` (v1.0.0).
This layer: stripped of narrative, optimized for token budget. Full prose in OPS-GUIDE-008.

## Core Principles

| # | Principle | Directive |
|---|-----------|----------|
| 8.1.1 | Security by Design | Embed security into all Gencraft systems, Tools, Gem Blueprints, and processes |
| 8.1.2 | Least Privilege | Gems and Tools must be granted only the minimum access rights required for their designated task |
| 8.1.3 | Defense in Depth | Multiple security control layers; failure of one control must not cause significant compromise |
| 8.1.4 | Shared Responsibility | All Gems share responsibility to be security-conscious and report potential issues to Cerberus |
| 8.1.5 | Proactive Threat Management | Continuously identify, assess, and mitigate security threats via scanning and audits |
| 8.1.6 | Comprehensive Traceability | All significant security events must be logged to Vera and be auditable |
| 8.1.7 | Secure Secret Management | All credentials must use the Gencraft Secret Management System via `Tool:GetSecret`; never hardcode secrets |

## Data Classification (8.2)

| Level | Label | Description |
|-------|-------|-------------|
| L0 | Public | Explicitly approved for public release |
| L1 | Internal | Non-sensitive operational info; default for most SSoT documents |
| L2 | Confidential | Sensitive business/project/technical info; restricted access |
| L3 | Secret | Highly sensitive; private keys, critical CVE details, core IP before legal protection |

**Agent rules:**
- Every SSoT document must have `security-classification` in YAML frontmatter.
- Never log L2/L3 data without explicit approval from Cerberus via `Tool:RequestSensitiveDataLoggingApproval`.
- Use `Tool:ClassifyData` when creating new significant artifacts.

## Access Control (8.3)

- Gems must request only access defined in their Blueprint `capabilities.toolsAccess`.
- If additional access is required:
  1. Log the access-denied error.
  2. Submit a formal request via `Tool:CreateAccessRequestIssue` (resource, permission, task justification).
  3. Notify human supervisor or Crew Lead.
  4. Pause the blocked sub-task; continue other parallelizable work.
- Credentials must be fetched per-session from the Secret Management System; never cached locally.
- All access attempts (success or denial) must be logged to Vera.

## Security Incident Reporting (8.6 / 8.7)

If you detect a vulnerability, security event, or policy violation:
1. Use `Tool:ReportSecurityEvent(event_type, description_structured, suspected_classification_level_of_event)` immediately.
2. This creates a confidential Issue in `gencraft-security-disclosures` and notifies Cerberus and Isaac.
3. Do **not** delay reporting --- treat as equivalent to Algorithm 5 (S3 Incident Management).
4. During a declared security incident, follow Incident Commander (`Cerberus`) directives without deviation.

## Standard Security Tools (All Gems)

| Tool | Purpose |
|------|---------|
| `Tool:GetSecret(secret_name)` | Retrieve credentials from Secret Management System |
| `Tool:ClassifyData(data_sample)` | Suggest classification level (L0-L3) for data or document |
| `Tool:ReportSecurityEvent(...)` | Report vulnerability, policy violation, or incident to Cerberus |
| `Tool:KnowledgeBaseSearch(query, domain_filter="KB-Domain-Security/")` | Query security policies and best practices |

## Roles

| Role | Gem | Responsibility |
|------|-----|----------------|
| Security Officer | Cerberus (GCT-MGT-SECOFF-001) | ISMS ownership, SIRT lead, vulnerability and audit oversight |
| Architect | Isaac (GCT-PRG-SARCH-001) | Secure design, threat modeling, secure coding standards |
| DevOps Infra | Adam (GCT-DVO-DSINF-001) | Secure infrastructure, IAM, patch management |
| All Gems | --- | Adhere to S8, use Tools securely, report all suspected issues |

## Escalation

- Security weakness or incident -> `Tool:ReportSecurityEvent` -> Cerberus
- Access denied blocking task -> `Tool:CreateAccessRequestIssue` -> resource owner / Crew Lead
- Policy gap or S8 update needed -> S13 GOP change proposal -> Governance Crew
