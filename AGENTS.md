---
docId: ENG-AGEN-033
title: AGENTS.md - gcs-core-governance
version: 1.0.0
authors:
- Claude Sonnet 4.6
creation_date: '2026-06-13'
language: en
summary: Claude Code subagent instructions for the GenCr@ft Core Governance repo.
last_updated_date: '2026-06-13'
metadata:
  lifecycle-stage: approved
  scope: studio-governance
  domain: engineering
  doc-type: agent-instructions
  security-classification: l2_confidential
---

# AGENTS.md — gcs-core-governance

## Project Overview

Canonical DevOps/tooling SSoT for GenCr@ft Studio. Contains governance standards, compliance tools, and the `verify-compression.sh` acceptance script for Telegraphic Semantic Compression (WI-14).

**Scope:** Studio-wide governance documents, linting tools, and platform acceptance scripts.

## Quick Commands

| Task | Command |
|------|---------|
| Run compression acceptance tests | `bash tools/tests/test_verify_compression.sh` |
| Check workspace CLAUDE.md | `bash tools/verify-compression.sh --workspace --claude ../../CLAUDE.md` |
| Check a repo AGENTS.md | `bash tools/verify-compression.sh --repo <path>/AGENTS.md` |

## Critical Patterns

- All documents must have YAML frontmatter with `docId: DOMAIN-TYPE-CODE`.
- `tools/verify-compression.sh` is the acceptance script for WI-14 compression ACs — do not modify thresholds (200 nb for CLAUDE.md, 150 nb for AGENTS.md) without updating gcs-core-governance#14.
- Issue routing for governance gaps: `gh issue create --repo GenCr-ft/gcs-core-governance`.

## Commit & PR Conventions

- Conventional Commits v1.0.0. Branch: `feat/issue-ID-slug` or `fix/issue-ID-slug`.
- Every PR references a GitHub Issue.
- Co-author trailer: Strictly prohibited. Do NOT write or push commits with `Co-Authored-By` trailer.

## Three-Tier Judgment Boundaries

✅ **Always Do**
- Add frontmatter to every new Markdown document
- Use `tools/verify-compression.sh` to validate compression ACs before closing WI-14 sub-issues
- File gaps as GitHub issues in `gcs-core-governance` before proceeding

⚠️ **Ask First**
- Changing compression thresholds (200/150 nb line limits)
- Adding new governance standards that affect all repos
- Modifying `tools/verify-compression.sh` acceptance criteria

🚫 **Never Do**
- Commit without a GitHub Issue reference
- Delete existing governance standards without Studio Lead approval
- Modify the workspace root CLAUDE.md directly (it is deployed from `gcs-plt-gemop/templates/CLAUDE.md.template`)

## Orchestration

**Status:** ✅ Stage 2 — AGENTS.md created 2026-06-13 (WI-14)

This repo follows Software Factory routing (workspace `AGENTS.md §Orchestration Routing`).
Shared skills available via `~/.claude/skills/`.
