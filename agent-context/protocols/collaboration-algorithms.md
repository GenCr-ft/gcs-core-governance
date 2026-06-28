---
docId: GOV-PROTO-CA-001
title: Collaboration Algorithms — Agent Protocol Reference
version: 1.1.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: protocol
  intended-audience: [ai-agents]
  security-classification: l2_confidential
  source_version: "1.0.0"
  last_verified: "2026-06-27"
---
# Collaboration Algorithms

Distilled from `execution-manuals/onboard-manuals/grounding-docs/GOV-GUIDE-014.operational-playbook-core-collaboration-algorithms.md` (v2.0.0).
This layer: stripped of narrative, optimized for token budget. Full prose in GOV-GUIDE-014.

## Algorithm 1 — Contribution & Review (S1)

1. Deliverable ready → create PR or update Issue using appropriate template
2. Assign reviewers (knowledgeGuardian, Lead as defined by repo/protocol)
3. Incorporate feedback → push updates to same PR
4. Once all approvals granted → ensure merge by authorized Gem

## Algorithm 2 — Disagreement & Escalation (S2)

1. **Self** — formalize disagreement in GitHub Issue (`disagreement-formalization-template.md`) + direct discussion
2. **Lead** — request mediation from Crew Lead
3. **Architect** — escalate to Isaac or Isidore (architectural issues only)
4. **Production** — escalate to Antoine (Producer) or Béatrice (PM)
5. **Governance Crew** — final binding decision

> ⚠ Template: `disagreement-formalization-template.md` — not yet authored. When needed, create a minimal inline version in the issue body and file a follow-up to formalize it.

Rule: **do not remain blocked** — escalate within same sprint cycle.

## Algorithm 3 — Decision Traceability (S7)

Required when making a significant decision within scope of autonomy:

1. **Context** — state what problem is being solved
2. **Options** — list the alternatives considered
3. **Decision** — state the decision clearly
4. **Justification** — explain why this option was chosen
5. **Traceability** — log in GitHub Issue or ADR

> ⚠ Template: `decision-template.md` — not yet authored. When needed, create a minimal inline version in the issue body and file a follow-up to formalize it.

## Algorithm 4 — Agile/Scrum Task Loop (S15)

1. Pull prioritized task from Sprint Backlog
2. Implement — adhere to Unified Technical Standard; satisfy all Definition of Done criteria
3. Report daily: progress, next steps, impediments
4. Submit for review via Algorithm 1
5. Repeat

## Algorithm 5 — Incident Management Quick Response (S3)

1. Assess: is it a critical failure, security breach, or major blocker?
2. Report immediately: use `incident-report-template.md` — do NOT delay
3. Follow Incident Commander (IC) instructions once assigned
4. All communication in the designated incident Issue (traceability)

> ⚠ Template: `incident-report-template.md` — not yet authored. See ops-runbook.md Template Registry.

> ⚠ Template: `incident-report-template.md` — not yet authored. See ops-runbook.md Template Registry.

> ⚠ Template: `incident-report-template.md` — not yet authored. See ops-runbook.md Template Registry.

## Algorithm 6 — Protocol Evolution (S12/S13)

1. **Crew-level** — propose Crew-Specific Protocol (CSP) to Lead (S12)
2. **Studio-level** — draft proposal using `protocol-change-proposal-template.md`
3. Submit proposal to Governance Crew (S13) for review
4. Approved proposals become GOPs and are merged to gcs-core-governance

> ⚠ Template: `protocol-change-proposal-template.md` — not yet authored. When needed, create a minimal inline version in the issue body and file a follow-up to formalize it.

## Algorithm 7 — Epic & Task Hierarchy (S16)

1. Create Epic (Parent Issue) in appropriate repo
2. Inside Epic body, use `- [ ] #N` tasklist syntax to link Child Issues (not plain text)
3. Child Issue must reference Epic in its body
4. This feeds completion metrics into GitHub Projects automatically

**Never use:** `**Parent:** #123` — use `- [ ] #123` or `- [x] #123` only.


## Algorithm 8 — Information Security Management (S8)

Apply before committing any artifact, creating any document, or storing any data:

1. **Classify** — determine the data classification level of the artifact:
   - `l0_public`: explicitly approved for public release
   - `l1_internal`: non-sensitive operational information (default)
   - `l2_confidential`: sensitive business/project/technical data (restricted access)
   - `l3_secret`: highly sensitive — private keys, critical vulnerability details, core IP pre-legal-protection
2. **Mark** — set `security-classification: <level>` in YAML frontmatter for every SSoT document
3. **Check prohibited storage** — never commit or store the following regardless of classification:
   - API keys, passwords, certificates, or encryption keys in source files or config
   - Secrets in Gem Blueprints or CI environment variables in plaintext
   - Any `l3_secret` material outside the designated Gencraft Secret Management System
4. **Escalate l3-secret material** — if the artifact is `l3_secret`:
   - Do NOT proceed autonomously
   - File a GitHub Issue in `gcs-core-governance` referencing `Cerberus` (GCT-MGT-SECOFF-001) as assignee
   - Await explicit approval before any storage or transmission action
5. **Log** — all access to `l2_confidential` or `l3_secret` data must be logged (reference S3 Algorithm 5 if a breach is suspected)

> Source: `reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-008.s8-information-security-management.md` (sections 8.1-8.3). Agents must not read that file directly; this algorithm surfaces the mandatory agent-facing steps.