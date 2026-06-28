---
docId: GOV-TMPL-IRT-001
title: Incident Report Template
version: 1.0.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: template
  intended-audience: [ai-agents]
  security-classification: l2_confidential
---
# Incident Report

> Use this template immediately when Algorithm 5 (Incident Management) step 2 is triggered.
> Do NOT delay — fill in what is known now and update as information becomes available.

## Incident Summary

**Severity:** [ ] Critical | [ ] High | [ ] Medium  
**Type:** [ ] Security Breach | [ ] Critical Failure | [ ] Major Blocker  
**Detected at:** <!-- ISO-8601 timestamp -->  
**Detected by:** <!-- agent name or human -->  
**Incident Commander:** <!-- assign once known -->  

## Description

<!-- One paragraph: what happened, what is currently known, what is NOT known -->

## Immediate Impact

<!-- Systems, users, or data affected. State "unknown" if not yet assessed. -->

## Actions Taken So Far

- <!-- timestamp: action taken -->

## Next Steps

- [ ] Assign Incident Commander
- [ ] Notify affected teams
- [ ] Contain / mitigate
- [ ] Root cause analysis
- [ ] Post-mortem schedule

## Communication Channel

All further communication must occur in this GitHub Issue. Reference issue number in all commits and PRs related to this incident.
