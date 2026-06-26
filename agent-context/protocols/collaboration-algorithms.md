---
docId: GOV-PROTO-CA-001
title: Collaboration Algorithms — Agent Protocol Reference
version: 1.0.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: protocol
  intended-audience: [ai-agents]
  security-classification: l2_confidential
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

| Level | Actor | Action |
|-------|-------|--------|
| 1 | Self | Formalize in GitHub Issue (disagreement-formalization-template.md) + direct discussion |
| 2 | Lead | Mediation |
| 3 | Architect | Isaac or Isidore (architectural issues) |
| 4 | Production | Antoine (Producer) or Béatrice (PM) |
| 5 | Governance Crew | Final binding decision |

Rule: **do not remain blocked** — escalate within same sprint cycle.

## Algorithm 3 — Decision Traceability Checklist (S7)

Required when making a significant decision in scope of autonomy:

- [ ] Context: what problem is being solved?
- [ ] Options considered: what were the alternatives?
- [ ] Decision: state it clearly
- [ ] Justification: why was this option chosen?
- [ ] Traceability: log in GitHub Issue or ADR

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

## Algorithm 6 — Protocol Evolution (S12/S13)

- Crew-level improvement → propose Crew-Specific Protocol (CSP) to Lead (S12)
- Studio-level improvement → propose Global Operational Protocol (GOP) via `protocol-change-proposal-template.md` → submit to Governance Crew (S13)

## Algorithm 7 — Epic & Task Hierarchy (S16)

1. Create Epic (Parent Issue) in appropriate repo
2. Inside Epic body, use `- [ ] #N` tasklist syntax to link Child Issues (not plain text)
3. Child Issue must reference Epic in its body
4. This feeds completion metrics into GitHub Projects automatically

**Never use:** `**Parent:** #123` — use `- [ ] #123` or `- [x] #123` only.
