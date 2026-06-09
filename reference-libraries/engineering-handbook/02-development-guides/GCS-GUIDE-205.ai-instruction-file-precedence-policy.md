---
docId: GCS-GUIDE-205
title: "AI Instruction File Precedence Policy"
version: 1.0.0
status: Approved
date: 2026-06-02
authors:
  - "Engineering Lead"
knowledgeGuardian:
  - "Engineering Lead"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/02-development-guides/GCS-GUIDE-205.ai-instruction-file-precedence-policy.md
metadata:
  lifecycle-stage: approved
  domain: engineering
  doc-type: guide
  scope: studio-wide
  security-classification: l1_public
  keywords:
    - "agents"
    - "AGENTS.md"
    - "CLAUDE.md"
    - "ai-tooling"
    - "instruction-precedence"
    - "split-brain"
---

# AI Instruction File Precedence Policy

## 1. Objective

This policy resolves the dual-authority problem identified in the 2026-06-01 documentation audit
(ref: `gcp-aethel-backlog#500`, Pattern B). It establishes a single, unambiguous source of
truth for AI agent instructions across all GenCr@ft Studio repositories and defines the permitted
scope of the companion `CLAUDE.md` file.

## 2. Rule

**`AGENTS.md` is the sole authoritative AI instruction source for every GenCr@ft Studio
repository.**

Every repository that is expected to be worked on by an AI agent (Claude Code or any other
agent) MUST contain an `AGENTS.md` file at its root. `AGENTS.md` is the file that agents
MUST read and follow. Its authority cannot be overridden or supplemented by any other file.

## 3. Constraints on CLAUDE.md

`CLAUDE.md`, when present, is a **human-readable companion document only**. It MUST comply
with all of the following constraints:

1. **No agent-routing rules.** `CLAUDE.md` MUST NOT contain agent-routing tables, dispatch
   logic, or instructions that direct an AI agent to a specific persona, skill, or sub-agent.

2. **No commit or branching conventions.** `CLAUDE.md` MUST NOT specify commit message formats,
   branch naming rules, or PR conventions. These belong exclusively in `AGENTS.md`.

3. **No tool-call instructions.** `CLAUDE.md` MUST NOT contain instructions for how an AI agent
   should call tools (e.g., which shell commands to run, which GitHub Actions to invoke).

4. **No prohibited-behaviour directives.** `CLAUDE.md` MUST NOT instruct AI agents on
   prohibited behaviours (e.g., trailer suppression, force-push rules). Such directives belong
   in `AGENTS.md`.

5. **No duplication of AGENTS.md content.** `CLAUDE.md` MUST NOT duplicate content that
   already exists in `AGENTS.md`. Duplication creates drift and is itself a form of
   contradiction.

6. **Conflict resolution: `AGENTS.md` always wins.** When any statement in `CLAUDE.md`
   conflicts with a statement in `AGENTS.md` — on any topic — `AGENTS.md` takes precedence
   without exception.

## 4. Permitted Content for CLAUDE.md

`CLAUDE.md` MAY contain the following categories of human-oriented content:

| Permitted category | Examples |
|--------------------|---------|
| Project background | Elevator-pitch description, business context, key stakeholders |
| Local dev setup | OS-level prerequisites, IDE plugin recommendations, environment variable hints |
| Onboarding orientation | "Start by reading ENG-REFE-001", links to Confluence/Notion pages |
| Frequently asked questions | "Why do we use uWebSockets instead of Socket.IO?" |
| Links to external resources | Architecture ADRs, design documents, RFC links |
| Repo-level caveats | Known quirks, on-ice status, activation gates |

This content is addressed to human readers and is not authoritative for agents.

## 5. Deprecation Path

Repositories should be evaluated against the following criteria:

| Condition | Action |
|-----------|--------|
| `CLAUDE.md` content is 100% covered by `AGENTS.md` | Delete `CLAUDE.md` |
| `CLAUDE.md` contains unique human-context content that complies with §3 | Retain; ensure no conflicting instructions remain |
| `CLAUDE.md` contains instructions that violate §3 | Remove violating sections; move appropriate content to `AGENTS.md` |

The studio-wide sweep to apply these criteria is tracked in `gcp-aethel-backlog#505` (Pattern B
remediation). Priority targets identified in the audit: `gcd-shared-actions` and
`gcl-voxel-engine` (content 100% covered by `AGENTS.md`).

## 6. Rationale

The 2026-06-01 documentation audit found 20+ repositories with confirmed dual-authority
conflicts between `CLAUDE.md` and `AGENTS.md`. Agents reading both files received contradictory
instructions — a P0 systemic finding catalogued in `gcp-aethel-backlog#500`. Examples of the
observed conflicts:

- `CLAUDE.md` mandating a Co-Authored-By trailer; `AGENTS.md` prohibiting it.
- `CLAUDE.md` specifying a different branch naming pattern than `AGENTS.md`.
- `CLAUDE.md` routing agents to a legacy persona file that has been superseded.

A single authoritative source eliminates these conflicts and makes agent behaviour predictable
and auditable.

## 7. References

| Reference | Description |
|-----------|-------------|
| `gcp-aethel-backlog#500` | Master documentation audit (2026-06-01) — P0 findings |
| `gcp-aethel-backlog#505` | Pattern B remediation — batch CLAUDE.md sweep |
| `gcs-engineering-handbook#39` | Issue that triggered this policy |
| `ENG-REFE-001` | Engineering Manifesto — architecture and standards index; canonical source of studio philosophy (supersedes GCS-ARCH-001) |
