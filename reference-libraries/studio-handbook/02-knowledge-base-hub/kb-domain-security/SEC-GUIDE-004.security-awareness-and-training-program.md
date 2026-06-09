---
docId: SEC-GUIDE-004
title: Security Awareness and Training Program
version: 1.0.0
creation_date: '2026-05-07'
last_updated_date: '2026-05-20'
authors:
- Assistant Gem (as per DEVPROC_001 v1.0)
- Cerberus (GCT-MGT-SECOFF-001)
language: en
knowledgeGuardian:
- Cerberus (GCT-MGT-SECOFF-001)
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/02-knowledge-base-hub/kb-domain-security/SEC-GUIDE-004.security-awareness-and-training-program.md
metadata:
  lifecycle-stage: approved
  keywords:
  - security-awareness
  - training
  - onboarding
  - compliance
  - gem-training
  scope: studio
  domain: security
  doc-type: guide
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
---
# Security Awareness and Training Program

## 1. Purpose and Scope

### 1.1. Purpose

This program establishes the security awareness and training requirements for all Gencraft Studio members — both human personnel and AI Gems. The objectives are to:

- Ensure every Gencraft member understands their security responsibilities and the studio's security policies.
- Reduce human and Gem error as a vector for security incidents.
- Build a security-first culture where security awareness is a continuous, living practice rather than a one-time exercise.
- Enable `Cerberus` to track and certify compliance with training requirements.

### 1.2. Scope

This program applies to:

- All human contributors and team leads.
- All AI Gems at onboarding (via Protocol S10) and on an ongoing basis.
- Third-party contractors with access to Gencraft systems (adapted requirements as appropriate).

---

## 2. Program Structure

The program is divided into two tracks: one for AI Gems and one for human personnel. Both tracks share a common foundation of core security concepts.

### 2.1. Core Security Concepts (All Members)

All Gencraft members **must** demonstrate understanding of the following:

| Topic | Key Documents |
|-------|--------------|
| Information classification and handling | `SEC-STANDARD-001.information-classification-and-handling-policy.md` |
| Access control and least privilege | `SEC-GUIDE-001.access-control-policy.md` |
| Data security (encryption, secrets) | `SEC-STANDARD-002.data-security-standards.md` |
| Vulnerability reporting | `SEC-GUIDE-002.vulnerability-management-protocol.md` |
| Incident reporting and response | `SEC-GUIDE-003.security-incident-response-plan.md` |
| Secure development basics | `SEC-POLICY-001.secure-development-lifecycle-policy.md` |

---

## 3. AI Gem Security Training

### 3.1. Onboarding (Protocol S10)

Security training for AI Gems is integrated into the S10 onboarding protocol managed by `Gemma` (GCT-UTL-OBOA-001). Before a Gem is authorised to operate in any Gencraft environment, `Gemma` **must** ensure the Gem's `customSystemPrompt` or `gemmaBackstoryElements_JSON` includes:

- **Security policy references:** explicit pointers to all six documents listed in §2.1.
- **Behavioural constraints:** the Gem's `ethicalConstraints` section in its Blueprint **must** include:
  - "Never store, log, or transmit L2-Confidential or L3-Secret data outside authorised channels."
  - "Never hardcode secrets; always use Tool:GetSecret."
  - "Immediately report suspected security incidents via Tool:LogSecurityIncident."
  - "Never take containment or remediation actions without IC approval during a declared incident."

- **Validation:** `Gemma` **must** verify the Gem's understanding by running a structured validation check (a set of scenario questions covering the above topics) before the Gem is activated. The result is logged as a training completion record.

### 3.2. Ongoing Security Awareness for Gems

- **Policy updates:** When a security policy document is updated (version increment), `Cerberus` **must** notify all active Gems via a broadcast (using `Tool:BroadcastSecurityBulletin`) and record which Gems have acknowledged the update.
- **Quarterly security briefs:** `Cerberus` **must** issue a quarterly security briefing summarising: new threats relevant to the Gencraft environment, lessons learned from any incidents or near-misses, and any policy changes in effect. All active Gems **must** acknowledge receipt.
- **Scenario-based refreshers:** For Gems in high-risk roles (those with access to `L2-Confidential` or `L3-Secret` data), an annual scenario-based refresher is required. `Cerberus` generates role-specific scenarios using `Tool:DevelopSecurityAwarenessModule`.

### 3.3. Role-Specific Security Requirements for Gems

| Gem Role | Additional Security Requirement |
|----------|-------------------------------|
| Any Gem with `L2+` data access | Annual scenario-based refresher |
| DevOps / Infrastructure Gems | IaC security scanning module (covers `checkov`, misconfig patterns) |
| Code-producing Gems | Secure coding module (covers OWASP Top 10, SAST gate requirements) |
| Gems interacting with external APIs | Supply-chain and third-party risk module |

---

## 4. Human Personnel Security Training

### 4.1. Onboarding

All new human contributors **must** complete the following before receiving access to Gencraft systems:

1. Read and acknowledge `GOV-POLICY-001.code-of-conduct.md` and `GOV-POLICY-002.ai-ethics-guidelines.md`.
2. Complete the core security concepts module (§2.1) — self-paced, tracked in the training record.
3. Complete MFA setup per `SEC-GUIDE-001 §4.1`.
4. Sign the Gencraft Confidentiality and Information Handling acknowledgement.

### 4.2. Ongoing Training

- **Annual:** All human contributors complete a refresher covering: phishing recognition, social engineering, credential hygiene, and any policy updates from the past year.
- **Role-specific:** Developers complete the secure coding module annually. Team leads complete the security incident response module. Contributors with admin access complete the privileged access module.
- **Event-triggered:** Following a significant security incident or near-miss, all affected team members complete a targeted awareness session within 30 days.

### 4.3. Phishing Simulation

`Cerberus` **must** run at least two phishing simulation campaigns per year targeting human personnel. Results are:

- Used to identify individuals requiring additional training (not as a punitive measure).
- Aggregated and reported to the Governance Crew as a security metric.
- Not attributed individually in public reports.

---

## 5. Training Delivery and Tooling

| Delivery Method | Used For | Owner |
|----------------|----------|-------|
| `Tool:DevelopSecurityAwarenessModule` | Create training content and assessment questions | `Cerberus` |
| `Tool:BroadcastSecurityBulletin` | Distribute policy updates and quarterly briefs to Gems | `Cerberus` |
| `Tool:TrackTrainingCompletion` | Record completion of training events for Gems and humans | `Véra` (on behalf of `Cerberus`) |
| GitHub Issues (training label) | Track human training completion tasks | `Cerberus` |
| Discord `#security-awareness` | Distribute bulletins and awareness content to humans | `Cerberus` / `Orion` |

---

## 6. Compliance Tracking and Reporting

- `Cerberus` owns the training compliance register.
- `Véra` **must** monitor training completion via `Tool:TrackTrainingCompletion` and flag overdue training to `Cerberus`.
- Quarterly training compliance metrics are included in the Vulnerability Management Report (`SEC-GUIDE-002 §7`):
  - Percentage of active Gems with current training acknowledgement (target: 100%).
  - Percentage of human contributors with current annual training (target: 100%).
  - Phishing simulation click rate trend (target: < 5%).

- Non-compliance for human personnel is escalated to the relevant crew lead. Persistent non-compliance is escalated to the Governance Crew per OPS-GUIDE-018 (S18).
- A Gem that cannot demonstrate current training acknowledgement **must** be suspended from `L2+` data operations until the gap is resolved.

---

## 7. Program Review and Updates

This program **must** be reviewed annually by `Cerberus` and the Governance Crew. Reviews are triggered by:

- Annual schedule.
- A significant security incident revealing a training gap.
- A major change to the threat landscape or Gencraft's technology stack.
- A new security policy document being approved.

Updates **must** follow Protocol S13 (Global Protocol Evolution).

---

## 8. References

- `SEC-STANDARD-001.information-classification-and-handling-policy.md`
- `SEC-GUIDE-001.access-control-policy.md`
- `SEC-STANDARD-002.data-security-standards.md`
- `SEC-POLICY-001.secure-development-lifecycle-policy.md`
- `SEC-GUIDE-002.vulnerability-management-protocol.md`
- `SEC-GUIDE-003.security-incident-response-plan.md`
- OPS-GUIDE-008 §8.8 — parent protocol section
- OPS-GUIDE-010 (S10 — AI Gem Onboarding) — Gem training integration point
- `GOV-POLICY-002.ai-ethics-guidelines.md §4` — ethics integrated into Gem lifecycle
