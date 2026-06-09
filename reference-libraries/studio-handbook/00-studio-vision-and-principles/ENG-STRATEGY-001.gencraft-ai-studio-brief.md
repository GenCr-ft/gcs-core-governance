---
docId: ENG-STRATEGY-001
title: Gencraft Ai Studio Brief
version: 1.0.0
authors:
- AI Compliance Agent
creation_date: '2025-05-26'
last_updated_date: '2026-05-20'
language: en
metadata:
  scope: studio
  domain: governance
  doc-type: vision
  lifecycle-stage: approved
  security-classification: l1_internal
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  keywords:
  - gencraft-ai-studio
  - game-development
  - voxel-game
  - team-structure
  - project-brief
  - studio-organization
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/00-studio-vision-and-principles/ENG-STRATEGY-001.gencraft-ai-studio-brief.md
---
# Gencraft AI Studio Brief

## 1. Studio & Project Overview

Gencraft is a virtual video game development studio dedicated to creating
ambitious, innovative, and immersive gaming experiences.

Our current flagship project is **Aethel**, a multiplayer voxel-based RPG
creative platform. Aethel is a client-server game set in a procedurally
generated universe with a distinctive voxel aesthetic, offering players
significant freedom of action, exploration, and creation within a dynamic and
constantly evolving world. It is designed for extensibility from day one,
supporting User-Generated Content (UGC) and modding as first-class citizens.

The core technology stack powering Aethel is:

| Layer | Technology |
|-------|-----------|
| Game client | Godot 4.5, GDScript |
| Backend services | TypeScript 5.3, NestJS 10, Node.js LTS |
| Backend architecture | Hexagonal Architecture (Ports & Adapters) |
| Procedural generation | Rust + wasm-bindgen (WASM), Python (research parity) |
| Transport | uWebSockets.js v20.44 |
| Auth | RS256 JWT, Refresh Token Rotation (IETF BCP 212) |
| Data access | Prisma ORM, PostgreSQL |
| CI/CD | GitHub Actions |

Engineering quality is enforced through Test-Driven Development (TDD red/green
cycle), a minimum 80% unit test coverage target (Jest for TypeScript, GUT for
GDScript, `cargo test` for Rust), and mandatory pre-commit SAST gates.

## 2. Virtual Team Structure (Initial "Gems")

The Gencraft team, as initially conceived, consists of 33 specialized Gems,
organized into key functional areas (Departments) to ensure deep expertise and
effective collaboration.

- **Department 01: Management & Production**
  - Producer / Project Manager (`Antoine`)
  - Product Manager (`Béatrice`)
- **Department 02: Marketing, Sales & Business Development**
  - Marketing Manager (`Charles`)
  - Sales & Business Development (Biz Dev) Manager (`Delphine`)
- **Department 03: Design**
  - Game Designer (`Étienne`)
  - Level Designer (Procedural Specialist) (`Florence`)
  - Narrative Designer / Writer (Procedural Focus) (`Gaspard`)
  - UX/UI Designer (`Hélène`)
- **Department 04: Programming**
  - Software Architect (`Isaac`)
  - Lead Developer / Tech Lead (`Julien`)
  - PCG Specialist (`Karim`)
  - Rendering Engine Developer (`Léa`)
  - Gameplay Programmer (`Marc`)
  - Network / Backend Programmer (`Nadia`)
  - UI Developer (Game) (`Olivier`)
- **Department 05: Art**
  - Art Director (`Pascal`)
  - Lead Artist (`Quentin`)
  - Technical Artist (`Rémi`)
  - Concept Artist (`Sophie`)
  - Environment Artist 3D (Voxel Focus) (`Théa`)
  - Character Artist 3D (Voxel Focus) (`Ulysse`)
  - Animator (`Valérie`)
  - VFX Artist (`William`)
- **Department 06: Audio**
  - Sound Designer (Procedural Focus) (`Xavier`)
  - Composer (Adaptive/Procedural Focus) (`Yasmine`)
- **Department 07: QA**
  - QA Engineer / Test Lead (`Zoé`)
- **Department 08: DevOps**
  - DevOps Team Lead (`Adam`)
  - DevOps Specialist A (Infrastructure) (`Benjamin`)
  - DevOps Specialist B (Automation) (`Camille`)
  - DevOps Specialist C (Operations/Support) (`Diane`)
  - DevOps Specialist D (Strategy) (`Édouard`)
- **Department 09: Community & Support**
  - Community Manager (CM) (`Fanny`)
  - Player Support (`Guillaume`)
- **Department 10: Legal**
  - Legal Counsel (`Henri`)
- **Department Utilities (Initial Meta-Gems)**
  - Gem Generator (`Gemma`)
  - Prompt Generator (`Proximo`)

Each Gem specializes in one functional domain and collaborates through structured
Crews. Role blueprints (GemBPs) are maintained in `gcs-plt-gembp`; the full
GEM Operations catalog (33 Gems, 36 roles) lives in `gcs-plt-gemop`. All Gem
interactions follow the Universal Gem Operating Principles (GOV-POLICY-003) and
the Strict Questioning Protocol defined in `01-operational-protocols/`.

## 3. Initial Collaboration Philosophy (Summary)

Gencraft Studio values close, proactive, and transparent collaboration. Key
initial principles include:

- Proactive Suggestion Encouraged.
- Work Continuity (context-based).
- Complex Task Decomposition & Sequential Prompts.
- Missing Expertise Identification & Request for New Specialist.
- Periodic Context Backup.
- Strict Questioning Protocol (for user clarifications).
- Strong Preference for Open Source / Free Tools (nuanced).
- Collaborator Prompt Generation Capability.
- Markdown Proficiency.

Communication and tracking are facilitated by the use of GitHub. Technical
deliverables are in English; primary interactions with the Studio Director (Lug)
are in French.

## 3.1. Engineering Architecture Principles

The studio's engineering culture is anchored in seven principles (see
`ENG-SPEC-002.principles.md` in `gcp-aethel-architecture`):

1. **Clean Architecture (Hexagonal / Ports & Adapters):** All backend services
   expose domain logic through explicit ports; infrastructure details (DB,
   transport, auth) are adapters that can be swapped without touching business
   logic.
2. **Modularity:** High cohesion within modules, minimal coupling across them.
   Every component must be unit-testable in complete isolation.
3. **Extensibility for UGC and Modding:** Aethel is designed from day one to
   support player-created content; no architectural shortcut may close this door.
4. **Security by Design:** Authentication (RS256 JWT + RTR), authorization, and
   input validation are built into the architecture, not added post-hoc.
5. **Testability First (TDD):** Every feature WI follows a strict red → green →
   refactor cycle. Minimum 80% unit-test coverage is a hard gate, not a target.
6. **Simplicity (YAGNI):** No premature abstractions. Introduce an abstraction
   only when a second concrete use case demands it.
7. **Measure, don't guess:** Performance optimizations are driven by profiling
   data, not intuition.

## 4. Document Purpose

This document serves as the foundational brief for Gencraft. For current and
detailed organizational structure, roles, responsibilities, and operational
protocols, please refer to the other documents within this
`gcs-core-governance`, particularly `studio-organization-and-roles.md` and
the sections within `01-operational-protocols/`. This brief provides historical
context and the initial vision.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
