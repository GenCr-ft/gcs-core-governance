---
docId: GOV-PROTO-GOP-IDX-001
title: GOP S-Number Index — Global Operational Protocols Lookup
version: 1.0.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: reference
  intended-audience: [ai-agents]
  security-classification: l2_confidential
  source_version: "1.0.0"
  last_verified: "2026-06-27"
---
# GOP S-Number Index

Distilled from `reference-libraries/studio-handbook/01-operational-protocols/` (OPS-GUIDE-002 through OPS-GUIDE-021).
Use this table to resolve any S-number reference encountered in agent-context/ without reading reference-libraries/.

## S-Number Lookup Table

| S-Number | Protocol Name | Algorithm | Full source |
|----------|--------------|-----------|-------------|
| S1 | Feedback Approval | Algorithm 1 (Contribution & Review) | OPS-GUIDE-021 |
| S2 | Disagreement, Escalation, and Resolution | Algorithm 2 (Disagreement & Escalation) | OPS-GUIDE-002 |
| S3 | Emergency Management | Algorithm 5 (Incident Management Quick Response) | OPS-GUIDE-003 |
| S4 | Architectural Review Process | — | OPS-GUIDE-004 |
| S5 | Lessons Learned | — | OPS-GUIDE-005 |
| S6 | Key Reports | — | OPS-GUIDE-006 |
| S7 | Key Decisions Traceability | Algorithm 3 (Decision Traceability) | OPS-GUIDE-007 |
| S8 | Information Security Management | — | OPS-GUIDE-008 |
| S9 | Intellectual Property Management | — | OPS-GUIDE-009 |
| S10 | AI Gem Onboarding | — | OPS-GUIDE-010 |
| S11 | External Communication | — | OPS-GUIDE-011 |
| S12 | Crew-Specific Amendments | Algorithm 6 (Protocol Evolution — crew level) | OPS-GUIDE-012 |
| S13 | Global Protocol Evolution | Algorithm 6 (Protocol Evolution — studio level) | OPS-GUIDE-013 |
| S14 | KCT Communication Training Adoption Plan | — | OPS-GUIDE-014 |
| S15 | Agile Scrum Project Management | Algorithm 4 (Agile/Scrum Task Loop) | OPS-GUIDE-015 |
| S16 | Budget Financial Management | Algorithm 7 (Epic & Task Hierarchy) | OPS-GUIDE-016 |
| S17 | Virtual HR Gem Development | — | OPS-GUIDE-017 |
| S18 | Grievance Reporting and Resolution | — | OPS-GUIDE-018 |
| S19 | Action Item Management Protocol | — | OPS-GUIDE-019 |
| S20 | Artifact Storage and Retention | — | OPS-GUIDE-020 |

## Quick-Reference: S-Numbers in agent-context

The following S-numbers appear in agent-context/ files. Use the table above to confirm what each covers:

- **S2** — `agent-bootstrap.md` line 53, line 67: Disagreement & Escalation
- **S3** — `agent-bootstrap.md` line 44, line 68: Emergency Management / Incident Reporting
- **S7** — `collaboration-algorithms.md` Algorithm 3: Key Decisions Traceability
- **S8** — `strategic-context.md` line 46: Information Security Management
- **S12** — `collaboration-algorithms.md` Algorithm 6: Crew-Specific Amendments
- **S13** — `agent-bootstrap.md` line 71, `collaboration-algorithms.md` Algorithm 6: Global Protocol Evolution
- **S15** — `collaboration-algorithms.md` Algorithm 4: Agile Scrum Project Management
- **S16** — `collaboration-algorithms.md` Algorithm 7: Budget Financial Management / Epic Hierarchy

## Notes

- S-numbers S1–S20 are all studio-wide (GOP scope). For Crew-Specific Protocol (CSP) adaptations, see S12.
- Algorithm numbers in `collaboration-algorithms.md` map to the S-numbers shown in the table above.
- Full narrative for each protocol is in `reference-libraries/studio-handbook/01-operational-protocols/` — read only when deep protocol detail is needed.
