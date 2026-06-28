---
docId: GOV-GRND-002
title: Studio Quick Reference — Key Facts for AI Agents
version: 1.0.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: governance
  doc-type: grounding
  intended-audience: [ai-agents]
  security-classification: l2_confidential
  source_version: "1.0.0"
  last_verified: "2026-06-27"
---
# Studio Quick Reference

Distilled from GOV-GUIDE-412 (Studio Reference v1.0.0) and CLAUDE.md workspace config.
Key facts for cold-start context. Full lexicon: `agent-context/grounding/lexicon.yml` (GOV-GUIDE-HG-AC-004).

## Core Terminology

> **Authoritative source:** `grounding/lexicon.yml` (GOV-GUIDE-HG-AC-004) is the canonical definition for all terms below. When a definition here conflicts with `lexicon.yml`, `lexicon.yml` takes precedence.

| Term | Definition |
|------|-----------|
| SSoT | Single Source of Truth — for any given piece of official information, there is one authoritative location, always a version-controlled document in a Gencraft Git repository |
| AI Gem | A specialized AI entity within Gencraft Studio, designed to perform specific roles and tasks. Also called 'Gem'. |
| GOP | Global Operational Protocol — studio-wide operational protocol in 01-operational-protocols/, applies to all Gencraft members (e.g., S1, S2, S8) |
| CSP | Crew-Specific Protocol — documented local adaptation of a GOP, applies only within a particular Crew, as defined in Protocol S12 |
| Knowledge Guardian (KG) | A designated Gem responsible for the quality, accuracy, and currency of a specific knowledge domain within the SSoT |
| ADR | Architecture Decision Record — document capturing an important architectural decision, its context, and consequences |
| WI | Work Item — a GitHub Issue tracking a single deliverable, governed by the 5-gate lifecycle in GOV-PROT-003 |
| GemID | Unique identifier for an AI Gem. Format: GCT-{DEPT}-{ROLE}-{NNN}. Example: GCT-PRG-SARCH-001 (Isaac, Senior Architect). |
| MCP | Model Context Protocol — open standard Gencraft uses to standardize all interactions between Gems (as MCP Clients) and their Tools (exposed via MCP Servers) |

## Repo Naming Convention

| Prefix | Layer |
|--------|-------|
| `gcd-` | DevOps / developer tooling |
| `gcl-` | Shared libraries and microservices |
| `gcp-` | Product (Aethel game) |
| `gcs-` | Studio-wide standards and handbooks |
| `gct-` | Templates (repo, service, SSoT) |
| `gce-` | Experimental (not yet production) |
| *(none — see `gencraft-iac`)* | Infrastructure as Code (predates prefix convention; actual repo is `gencraft-iac`) |

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
| Product Manager | GCT-MGT-PM-001 | Béatrice | Feature/roadmap decisions |
| Security Officer | GCT-MGT-SECOFF-001 | Cerberus | Security incidents, L3 access |
| Sr. Architect | GCT-PRG-SARCH-001 | Isaac | Architecture decisions, ADR veto |
| Sr. Architect | GCT-PRG-SARCH-002 | Isidore | Architecture decisions |
| QA Lead | GCT-QAS-QA-001 | Sentinel | Bug triage, severity assignment |
| AIE Team Lead | GCT-UTL-AIETL-001 | Aura | AI/Gem platform issues, identity injection failures |
| Studio Liaison & Governance Secretary | GCT-UTL-SLG-001 | Orion | WI lifecycle / governance protocol questions |
| GEM Instantiation Agent | GCT-UTL-GGEN-001 | Gemma | Identity injection failures (missing GemID or incomplete role at instantiation) |
