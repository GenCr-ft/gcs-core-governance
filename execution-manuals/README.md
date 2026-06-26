---
docId: GOV-READ-EM-001
title: execution-manuals — DEPRECATION NOTICE
version: 1.1.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: deprecated
  deprecation_justification: "Content migrating to agent-context/ (machine-readable protocols) per Option B architecture decision 2026-06-26. See gcs-core-governance#92 and migration issue #99."
  scope: studio
  domain: governance
  doc-type: readme
  intended-audience: [ai-agents, contributors]
  security-classification: l2_confidential
---
# execution-manuals/ — DEPRECATION NOTICE

> **This folder is being superseded.** Content is migrating to [`agent-context/`](../agent-context/) as part of the gcs-core-governance AI-native refactor (gcs-pm#300, Option B architecture decision 2026-06-26).

## Migration status

| Subfolder | Migration target | Status |
|-----------|-----------------|--------|
| `onboard-manuals/GOV-GUIDE-006.gasai-v2.0.md` | `agent-context/grounding/agent-bootstrap.md` | ✅ Extracted (distilled version available) |
| `onboard-manuals/grounding-docs/GOV-GUIDE-014.md` | `agent-context/protocols/collaboration-algorithms.md` | ✅ Extracted |
| `onboard-manuals/grounding-docs/GOV-GUIDE-012.md` | `agent-context/grounding/agent-bootstrap.md` | ✅ Extracted |
| `onboard-manuals/grounding-docs/` (full docs) | `agent-context/grounding/` | Pending migration issue [#99](https://github.com/GenCr-ft/gcs-core-governance/issues/99) |
| `security-checklists/` | `agent-context/protocols/` | Pending |
| `testing-playbooks/` | `agent-context/protocols/` | Pending |

## AI agents: use agent-context/ instead

- Document routing → [`agent-context/protocols/document-routing.md`](../agent-context/protocols/document-routing.md)
- WI lifecycle gates → [`agent-context/protocols/wi-lifecycle-gates.yml`](../agent-context/protocols/wi-lifecycle-gates.yml)
- Collaboration algorithms → [`agent-context/protocols/collaboration-algorithms.md`](../agent-context/protocols/collaboration-algorithms.md)
- Agent bootstrap / identity → [`agent-context/grounding/agent-bootstrap.md`](../agent-context/grounding/agent-bootstrap.md)
- Studio quick reference → [`agent-context/grounding/studio-quick-ref.md`](../agent-context/grounding/studio-quick-ref.md)

Full original documents remain here until migration is complete. Do not modify this folder.
