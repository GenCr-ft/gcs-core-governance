---
docId: ENG-AGEN-033
title: AGENTS.md - gcs-core-governance
version: 2.0.0
authors:
- Governance Crew
creation_date: '2026-06-13'
language: en
summary: Claude Code subagent entry point for gcs-core-governance. Surfaces agent-context/ and human-guides/ layers.
last_updated_date: '2026-06-27'
metadata:
  lifecycle-stage: approved
  scope: studio-governance
  domain: engineering
  doc-type: agent-instructions
  security-classification: l2_confidential
---

# AGENTS.md — gcs-core-governance

Canonical DevOps/tooling SSoT for GenCr@ft Studio. Read `agent-context/` for machine-readable protocols; read `human-guides/` for visual/narrative guides.

## Agent Context Layer (start here)

| Question | File |
|----------|------|
| How do I route a document? | [agent-context/protocols/document-routing.md](agent-context/protocols/document-routing.md) |
| What are the WI lifecycle gate requirements? | [agent-context/protocols/wi-lifecycle-gates.yml](agent-context/protocols/wi-lifecycle-gates.yml) |
| What collaboration algorithm applies? | [agent-context/protocols/collaboration-algorithms.md](agent-context/protocols/collaboration-algorithms.md) |
| What CLI commands and error paths do I need? | [agent-context/protocols/ops-runbook.md](agent-context/protocols/ops-runbook.md) |
| What is my identity and operational context? | [agent-context/grounding/agent-bootstrap.md](agent-context/grounding/agent-bootstrap.md) |
| What does this term mean? | [agent-context/grounding/lexicon.yml](agent-context/grounding/lexicon.yml) |
| What are the authoritative rule YAML files? | [agent-context/rules-index.md](agent-context/rules-index.md) |

## Human Guides Layer

| Guide | File |
|-------|------|
| Three-layer enforcement architecture | [human-guides/enforcement-architecture.md](human-guides/enforcement-architecture.md) |
| WI lifecycle visual flowchart | [human-guides/wi-lifecycle-flow.md](human-guides/wi-lifecycle-flow.md) |
| Document routing guide | [human-guides/document-routing.md](human-guides/document-routing.md) |

## Quick Commands

| Task | Command |
|------|---------|
| Run compression acceptance tests | `bash tools/tests/test_verify_compression.sh` |
| Run agent-context parity check | `python3 scripts/verify_agent_context_parity.py` |
| Write lifecycle stamp (REFINE) | `bash scripts/lifecycle-stamp.sh write gcs-core-governance <branch> <issue> refine` |
| File governance gap issue | `unset GH_TOKEN && gh issue create --repo GenCr-ft/gcs-core-governance --title "[GOV] ..."` |

## Critical Patterns

- All documents must have YAML frontmatter with `docId: DOMAIN-TYPE-CODE`.
- `tools/verify-compression.sh` — compression ACs for WI-14 (200 nb CLAUDE.md, 150 nb AGENTS.md).
- `agent-context/` is the machine-readable surfacing layer. Do not read `reference-libraries/` directly.
- Issue routing: `gh issue create --repo GenCr-ft/gcs-core-governance`.

## Commit & PR Conventions

- Conventional Commits v1.0.0. Branch: `feat/issue-ID-slug` or `fix/issue-ID-slug`.
- Every PR references a GitHub Issue. Co-author trailer: strictly prohibited.

## Three-Tier Judgment Boundaries

✅ **Always Do**
- Add frontmatter to every new Markdown document
- Use `agent-context/` as the first read target (not `reference-libraries/`)
- File gaps as GitHub issues in `gcs-core-governance` before proceeding

⚠️ **Ask First**
- Changing compression thresholds (200/150 nb line limits)
- Adding new governance standards that affect all repos

🚫 **Never Do**
- Commit without a GitHub Issue reference
- Delete existing governance standards without Studio Lead approval
- Modify `reference-libraries/` content (frozen pending restructure)
