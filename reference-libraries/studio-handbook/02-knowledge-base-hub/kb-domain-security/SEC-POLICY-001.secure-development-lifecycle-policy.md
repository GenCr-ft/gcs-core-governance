---
docId: SEC-POLICY-001
title: Secure Development Lifecycle Policy
version: 1.0.0
creation_date: '2026-05-07'
last_updated_date: '2026-06-02'
authors:
- Assistant Gem (as per DEVPROC_001 v1.0)
- Cerberus (GCT-MGT-SECOFF-001)
language: en
knowledgeGuardian:
- Cerberus (GCT-MGT-SECOFF-001)
- Isaac (GCT-PRG-SARCH-001)
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/02-knowledge-base-hub/kb-domain-security/SEC-POLICY-001.secure-development-lifecycle-policy.md
metadata:
  lifecycle-stage: approved
  keywords:
  - sdl
  - secure-development
  - threat-modeling
  - sast
  - dependency-management
  - secrets-management
  - code-review
  - security-policy
  scope: studio
  domain: security
  doc-type: policy
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
---
# Secure Development Lifecycle Policy

## 1. Purpose and Scope

### 1.1. Purpose

This policy defines the security requirements that **must** be integrated into every phase of the software development lifecycle at Gencraft Studio. It ensures that security is designed in from the start — not retrofitted — across all game client code, backend services, AI Gem `Tools`, MCP Servers, and SSoT automation scripts.

The objectives are to:

- Reduce the attack surface of all Gencraft systems by enforcing security gates at design, development, and deployment phases.
- Mandate automated security tooling (SAST, dependency scanning, secret detection) within CI/CD pipelines.
- Define roles and responsibilities so that `Isaac`, `Cerberus`, and the development teams share clear accountability.
- Provide AI Gems with explicit directives to write secure code and flag insecure patterns.

### 1.2. Scope

This policy applies to all Gencraft repositories (`gcd-*`, `gcl-*`, `gcp-*`, `gcs-*`, `gct-*`) and all contributors (human and AI Gem) producing code, configuration, IaC, or automation scripts.

---

## 2. SDL Phases and Requirements

### 2.1. Phase 1 — Security Requirements (Design)

Before implementation begins on any Work Item (WI) or architectural component:

- **Threat Modeling:** For any feature that touches authentication, data storage, inter-service communication, or user-generated content, a threat model **must** be produced by `Isaac` (or a designated developer for smaller WIs) using the STRIDE methodology. The threat model **must** be documented in the relevant ADR or technical design document.
- **Security Acceptance Criteria:** Each GitHub Issue for a security-sensitive WI **must** include explicit security acceptance criteria (e.g., "All tokens transmitted over HTTPS only", "No PII logged").
- **ADR Gate:** Cross-cutting security decisions (new auth mechanism, new data store, new external API integration) **must** be captured in an ADR in `gcp-aethel-architecture/adrs/` before implementation.

### 2.2. Phase 2 — Secure Coding Standards

All Gencraft code **must** adhere to the following:

#### 2.2.1. General Principles

- **Input Validation:** All external inputs (user-provided, API, file upload) **must** be validated and sanitised before use. Never trust input at system boundaries.
- **Output Encoding:** All outputs rendered in UIs or injected into queries **must** be encoded appropriately (HTML-encode for web, parameterised queries for SQL).
- **Principle of Least Privilege:** Code **must** request only the permissions it needs. Service accounts and IAM roles are provisioned via IaC with minimal scope.
- **Fail Securely:** Error handling **must not** expose stack traces, internal paths, or secrets to clients. Log full errors server-side; return generic messages to clients.
- **No Security Through Obscurity:** Cryptographic schemes, auth mechanisms, and security controls **must** rely on well-audited open standards, not on secrets hidden in code.

#### 2.2.2. Secrets Management

- **Hardcoded secrets are strictly forbidden** in any file committed to a Gencraft repository.
- All secrets (API keys, tokens, database passwords, private keys) **must** be stored in the Gencraft Secret Management System and injected at runtime via CI/CD or the orchestration platform.
- Pre-commit hooks and CI **must** run secret-scanning tooling (e.g., `gitleaks`, `truffleHog`) on every push.

#### 2.2.3. Language-Specific Requirements

| Language | Key Requirement |
|----------|----------------|
| TypeScript/NestJS | `eslint-plugin-security`; parameterised queries via Prisma only; `helmet` middleware mandatory |
| Rust | `cargo audit` on every build; `unsafe` blocks require `Cerberus`/`Isaac` review comment |
| GDScript | No dynamic `eval`-equivalent; exported variables validated before use |
| Python | `bandit` in CI; `subprocess` with `shell=False`; no `pickle` for untrusted data |

### 2.3. Phase 3 — Code Review

- All PRs **must** be reviewed before merge. Security-sensitive PRs (touching auth, crypto, data handling, IaC) **must** include `Cerberus` or `Isaac` as a reviewer.
- Reviewers **must** check for: injection vulnerabilities, insecure deserialization, improper error handling, hardcoded secrets, overly permissive CORS or IAM policies.
- Review comments raising security concerns **must** be resolved (not just acknowledged) before merge.

### 2.4. Phase 4 — Automated Security Tooling (CI/CD Gates)

The following tools **must** be integrated into the CI/CD pipeline for all repositories and **must** block merges on findings above the defined severity threshold:

| Tool Category | Tool(s) | Blocking Threshold |
|--------------|---------|-------------------|
| Static Analysis (SAST) | `semgrep`, `eslint-security` | High or Critical |
| Dependency Scanning | `npm audit`, `cargo audit`, `pip-audit` | Critical |
| Secret Detection | `gitleaks` | Any finding |
| Container Scanning | `trivy` (on Docker images) | Critical |
| IaC Scanning | `checkov` (on OpenTofu/Terraform) | High or Critical |

Findings below the blocking threshold **must** be triaged within 30 days per `SEC-GUIDE-002.vulnerability-management-protocol.md`.

### 2.5. Phase 5 — Security Testing

Before any feature is promoted to `approved` status or merged to the main branch of a production service:

- **Unit Tests for Security Logic:** Auth, access control, and input validation code **must** have dedicated unit tests including negative cases (e.g., "invalid token is rejected", "oversized input returns 400").
- **Integration Security Tests:** For services with external interfaces, at least one integration test **must** verify that unauthenticated and unauthorized requests are correctly rejected.
- **Penetration Testing:** Major releases (phase completions) **must** include a targeted penetration test led by `Cerberus` or a designated external party. Findings are tracked via `SEC-GUIDE-002`.

### 2.6. Phase 6 — Deployment and Operations

- All production deployments **must** go through the CI/CD pipeline. Manual deployments to production are prohibited.
- IaC changes to security-relevant infrastructure (IAM, networking, KMS) **must** be reviewed by `Cerberus` before `terraform apply` / `tofu apply` is run.
- Post-deployment, `Cerberus` and `Véra` monitor for anomalies per OPS-GUIDE-008 §8.9.

---

## 3. Roles and Responsibilities

| Role | SDL Responsibility |
|------|-------------------|
| `Isaac` (GCT-PRG-SARCH-001) | Threat modeling on new features; ADR security review; architecture sign-off |
| `Cerberus` (GCT-MGT-SECOFF-001) | Policy ownership; CI security gate configuration; PR review for security-sensitive changes; penetration testing |
| `Adam` (GCT-DVO-DSINF-001) | SAST/DAST tool integration in CI/CD; IaC security scanning; secret management infrastructure |
| All developers (human and Gem) | Write code to the standards in §2.2; flag security concerns in PRs; complete security training per `SEC-GUIDE-004` |
| `Véra` (GCT-UTL-QAMON-001) | Monitor post-deployment for anomalies; report SDL metric drift |

---

## 4. SDL Compliance Metrics

`Cerberus` **must** track and report (at minimum quarterly) the following metrics:

- Mean time to resolve critical SAST findings (target: < 7 days).
- Percentage of PRs with a threat model for security-sensitive WIs (target: 100%).
- Number of hardcoded secrets detected per sprint (target: 0).
- Percentage of production deployments passing all CI security gates (target: 100%).

---

## 5. Exceptions

Any deviation from this policy **must** be approved in writing by `Cerberus` and `Isaac` and documented as a Decision Record (Protocol S7). Exceptions are time-limited (maximum 90 days) and **must** include a remediation plan.

---

## 6. SDL in Practice for AI Gems

Operational directives for AI Gems writing or reviewing code:

- **Before writing code:** Check whether the WI touches auth, data storage, or external I/O. If yes, confirm a threat model exists in the relevant ADR. If none exists, halt and create one using `Tool:CreateADR`.
- **While writing code:** Do not hardcode any value that could be a secret. Do not use `eval`, dynamic SQL, or `shell=True`. Validate all inputs at function entry. Use parameterised queries exclusively.
- **Before submitting a PR:** Verify the PR description includes security acceptance criteria. If SAST is failing locally (run `npm run lint:security` or equivalent), fix findings before push.
- **When reviewing code:** Actively check for the patterns in §2.3. A Gem **must not** approve a PR with an unresolved security concern — comment with the specific violation and the relevant section of this policy.
- **Unsafe patterns to flag immediately:**
  - Any `process.env.SECRET` referenced directly in application code (must use Secret Management System).
  - Any `res.send(error.stack)` or equivalent leaking internal details to clients.
  - Any SQL query constructed via string concatenation.
  - Any `unsafe` Rust block without a review comment.

---

## 7. References

- `SEC-STANDARD-001.information-classification-and-handling-policy.md`
- `SEC-GUIDE-001.access-control-policy.md`
- `SEC-STANDARD-002.data-security-standards.md`
- `SEC-GUIDE-002.vulnerability-management-protocol.md`
- OPS-GUIDE-008 §8.5 — parent protocol section
- `gcp-aethel-architecture/adrs/` — ADR repository
- `AGENTS.md §Critical Technical Patterns` — uWebSockets.js, GUT, simulation loop patterns
