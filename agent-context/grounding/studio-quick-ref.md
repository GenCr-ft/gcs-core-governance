---
docId: GOV-REFE-003
title: Studio Quick Reference — Key Facts for AI Agents
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
# Studio Quick Reference

Distilled from GOV-GUIDE-412 (Studio Reference v1.0.0) and CLAUDE.md workspace config.
Key facts for cold-start context. Full lexicon in GOV-GUIDE-412.

## Core Terminology

| Term | Definition |
|------|-----------|
| SSoT | Single Source of Truth — one authoritative location per piece of info, always in a version-controlled Git repo |
| AI Gem | A specialized AI entity with a role, GemID, and SKILL.md persona definition |
| GOP | Global Operational Protocol — studio-wide, applies to all Gems (S1–S17) |
| CSP | Crew-Specific Protocol — local adaptation of a GOP, applies within one Crew only |
| Knowledge Guardian (KG) | Gem responsible for accuracy/currency of a knowledge domain |
| ADR | Architecture Decision Record — documents significant architectural choices |
| WI | Work Item — GitHub Issue following the REFINE→DESIGN→IMPLEMENT→CLOSE lifecycle |
| GemID | Unique Gem identifier, format: GCT-{DEPT}-{ROLE}-{SEQ} (e.g. GCT-PRG-SARCH-001) |
| MCP | Model Context Protocol — standard for Gem ↔ Tool interaction |

## Repo Naming Convention

| Prefix | Layer |
|--------|-------|
| `gcd-` | DevOps / developer tooling |
| `gcl-` | Shared libraries and microservices |
| `gcp-` | Product (Aethel game) |
| `gcs-` | Studio-wide standards and handbooks |
| `gct-` | Templates (repo, service, SSoT) |
| `gce-` | Experimental (not yet production) |
| `gci-` | Infrastructure as Code |

## Key Repositories

| Repo | Role |
|------|------|
| `gcs-core-governance` | Studio governance: schemas, rules, protocols, reference libraries |
| `gcs-plt-gemop` | GEM Operations: 33 gem personas, hooks, skills |
| `gcs-plt-gembp` | GEM Blueprint: 36 role definitions |
| `gcp-aethel-client` | Godot 4.5 game client |
| `gcp-aethel-server` | TypeScript/NestJS game server |
| `gcp-aethel-pcg` | Rust/WASM procedural generation |
| `gcs-project-management` | Project backlog, sprint plans, workspace STATUS.md |
| `gcd-shared-actions` | Reusable GitHub Actions workflows |
| `gcd-ops-scripts` | Python SSoT linters |

## Technology Stack

| Layer | Technology |
|-------|-----------|
| Game client | Godot 4.5, GDScript |
| Backend | TypeScript 5.3, NestJS 10, Node.js LTS |
| Architecture | Hexagonal (Ports & Adapters) |
| PCG | Rust + wasm-bindgen |
| Auth | RS256 JWT, Refresh Token Rotation (RTR) |
| Testing (TS) | Jest, ≥80% unit coverage |
| Testing (GDScript) | GUT v9.3.0 |
| Testing (Rust) | cargo test |
| CI/CD | GitHub Actions |

## Security Classification Levels

| Level | Label | Handling |
|-------|-------|---------|
| L0 | `l0_public` | Public — no restrictions |
| L1 | `l1_internal` | Internal to studio only |
| L2 | `l2_confidential` | Confidential — role-based access |
| L3 | `l3_secret` | Secret — security officer approval required |

## Key Gem Contacts for Escalation

| Role | GemID | Name | When to contact |
|------|-------|------|----------------|
| Studio Director | GCT-MGT-DIR-001 | Lug | Final authority |
| Producer | GCT-MGT-PPM-001 | Antoine | Scope/sprint decisions |
| Product Manager | GCT-MGT-SPM-001 | Béatrice | Feature/roadmap decisions |
| Security Officer | GCT-MGT-SECOFF-001 | Cerberus | Security incidents, L3 access |
| Sr. Architect | GCT-PRG-SARCH-001 | Isaac | Architecture decisions, ADR veto |
| Sr. Architect | GCT-PRG-SARCH-002 | Isidore | Architecture decisions |
| AIE Team Lead | GCT-UTL-AIETL-001 | Aura | AI/Gem platform issues |
