---
docId: GCP-GCS-READ-001
title: gcs-engineering-handbook
version: 1.0.0
authors:
- Architecture Lead
reviewers:
- Architecture Lead
creation_date: '2026-05-10'
language: en
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: engineering
  doc-type: orientation-guide
  intended-audience:
  - contributors
  - ai-agents
  security-classification: l1_public

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/AGENTS.md
---
# AGENTS.md — gcs-engineering-handbook

## Project Overview

The cultural foundation and technical guidance repository for all engineering work at GenCr@ft Studio. Contains the Engineering Manifesto (ENG-REFE-001), architecture standards, development guides (feature flags, semantic versioning, scripting), advanced technical guides, process guides (onboarding, code review), governance documents, and specialised sections for Godot GDScript patterns and PCG. The manifesto establishes binding engineering philosophy for all technical work.

## Architecture & Key Directories

```
gcs-engineering-handbook/
  01-manifesto-and-culture/                   — Core philosophy (required reading)
    ENG-REFE-001.*                             — The Engineering Manifesto
  02-development-guides/                      — Feature flags, semantic versioning, scripting
  03-advanced-guides/                         — Complex technical topics
  04-process-guides/                          — Onboarding, code review, processes
  05-governance-and-organization/             — Legal compliance, roles, org structure
  Godot/                                      — Godot 4 GDScript patterns
  Procedural_Content_Generation/              — PCG guides
```

## Core Philosophy (from ENG-REFE-001 — MANDATORY READING)

Three pillars all engineering work must uphold:

1. **Simplicity is Ultimate Sophistication** — Complexity is a bug. Unix way: small, focused, composable.
2. **Rigor Before Results** — Dijkstra: readable, testable, provable code. Empty `catch` blocks are professional malpractice.
3. **Reliability is Not an Option** — Hamilton: design for failure. Defensive programming, not optimistic programming.

Core truths in practice: Brooks's Law (adding people to late projects makes them later), No Silver Bullet (no single technique solves complexity), Knuth's 97% rule (premature optimisation is the root of all evil — measure first).

## Linting & Formatting

```bash
pre-commit run --all-files   # markdownlint, yamllint, commitlint, gcd-ops-scripts SSoT linters
```

## CI/CD & Required Checks

- `.github/workflows/ssot-compliance.yml` — validates SSoT frontmatter.

## Commit & PR Conventions

- Conventional Commits v1.0.0.
- Branch naming: `docs/`, `feat/`, `fix/`, `chore/`.
- Co-author trailer: Strictly prohibited in this workspace due to administrative blocks. Do NOT write or push commits containing the `Co-Authored-By` trailer.

## Notes for Agents

- The manifesto (`01-manifesto-and-culture/ENG-REFE-001.*`) is **required reading** before making any architectural or coding-style decisions across the workspace.
- All technical decisions made by agents must be consistent with the three philosophy pillars (Simplicity, Rigor, Reliability).
- The Godot and PCG sections provide patterns that must be followed when writing `gcp-aethel-client` and `gcp-aethel-pcg` code.
- All Markdown files must carry valid SSoT YAML frontmatter.
- This is a documentation-only repo — do not add implementation code.
- **AI instruction file precedence:** `AGENTS.md` is the sole authoritative AI instruction source for every repository. `CLAUDE.md`, when present, is a human-readable companion only and MUST NOT contradict `AGENTS.md`. See `GCS-GUIDE-205` for the full policy.

## .planning/ Directory Policy

Task plan files in `.planning/` directories are **session-ephemeral artefacts**. The authoritative policy is:

> `04-process-guides/GCS-GUIDE-405.planning-directory-retention-policy.md`

Key rules (full details in GCS-GUIDE-405):
- Plans with `status: complete` MUST be deleted before or immediately after the PR merge that completes the work — never committed to `main`.
- Plans with `status: in_progress` or `approved` MAY be committed to the working branch so they survive across sessions; they must be deleted in the merge commit or in a follow-up commit on `main` immediately after merge.
- If you find a `.planning/` file with `status: complete` or all tasks checked, treat it as a stale artefact — do NOT re-execute its tasks.

## Gap Protocol

Any gap, defect, or action item found while working in this repo **must become a GitHub Issue before proceeding** — nothing lives only in conversation context or memory.

```bash
# Route: governance and studio-wide items → gcs-project-management
gh issue create --repo GenCr-ft/gcs-project-management \
  --title "[gcs-engineering-handbook] Short description of the gap" \
  --body "## Summary

## Evidence

## Ref
ENG-BACK-NNN (if known)"

# Immediately add to Project #16:
gh project item-add 16 --owner GenCr-ft --url <issue-url>
```

Full routing table: workspace `AGENTS.md §9 — Gap Identification Protocol`.
