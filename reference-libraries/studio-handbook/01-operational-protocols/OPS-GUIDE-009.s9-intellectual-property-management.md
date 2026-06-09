---
docId: OPS-GUIDE-009
title: S9 Intellectual Property Management
version: 1.0.0
authors:
- AI Compliance Agent
creation_date: '2025-05-26'
last_updated_date: '2026-05-20'
language: en
metadata:
  scope: studio
  domain: governance
  doc-type: protocol
  lifecycle-stage: approved
  security-classification: l1_internal
  intended-audience:
  - contributors
  - ai-agents
  - legal-team
  keywords:
  - intellectual-property
  - ip-management
  - ai-gems
  - legal
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-009.s9-intellectual-property-management.md
---
# S9: Intellectual Property Management Protocol

## 9.0. Justification and Objectives

**Why this protocol is critical for Gencraft and its AI Gems:**
Intellectual Property is a core asset and a significant area of responsibility
for any creative studio. For Gencraft, with its AI Gem workforce and focus on
procedural generation, a clear IP management protocol is essential to:

- **Protect Gencraft's Creations:** Safeguard the original work produced by
  Gencraft Gems, including game code (for `gencraft-flagship-game`, `gencraft-
  game-engine`), art assets (voxel models, textures, concepts from `gencraft-
  art-bible-and-assets-specs`), audio, lore (from `gencraft-game-lore-and-
  world`), design documents (from `gcp-aethel-docs-gdd`), studio
  `Tools`, MCP Servers, and even novel Gem configurations or `gencraft-gem-
  blueprints`.
- **Ensure Clear Ownership:** Establish unambiguous ownership of IP created
  within the studio.
- **Respect Third-Party IP Rights:** Prevent infringement of copyrights,
  patents, trademarks, and other IP rights belonging to others. This is critical
  for legal compliance and ethical operation.
- **Manage Use of Licensed Materials:** Properly handle any third-party assets,
  software, or technologies used under license (including Open Source Software,
  managed by `Léo` as per elements of Protocol S8).
- **Foster an IP-Aware Culture:** Ensure all Gems understand the importance of
  IP and their role in its protection and respectful use.
- **Support Commercialization and Business Goals:** Clear IP ownership and
  management are prerequisites for any future commercialization of Gencraft's
  products.
- **Provide Traceability for IP Assets:** Maintain records of IP creation,
  ownership, and licensing.

This protocol aims to establish a comprehensive framework for IP management,
integrating it into Gencraft's daily operations and the lifecycle of its AI
Gems.

## 9.1. Core IP Management Principles for Gencraft

These principles, aligned with Gencraft's KC&T Guiding Principles and Core
Values, underpin this IP protocol:

- **Gencraft Ownership of Studio-Generated IP:** Unless explicitly stated
  otherwise in a formal agreement (e.g., for certain third-party contract work,
  which is not the current model), all IP created by Gencraft Gems during their
  operation for Gencraft is owned by Gencraft.
- **Respect for Originality and Attribution:** Strive for originality in
  Gencraft's creations. When using or referencing third-party materials (where
  permitted), proper attribution and adherence to licensing terms are mandatory.
- **Proactive IP Identification and Protection:** Actively identify potentially
  valuable IP created within the studio and take appropriate steps to protect
  it.
- **Due Diligence for Third-Party IP:** Before using any third-party asset,
  code, or information, perform due diligence to understand its IP status and
  usage rights.
- **Compliance with All Applicable IP Laws and Licenses:** Strict adherence to
  copyright law, trademark law, patent law (if applicable), and the terms of all
  software/asset licenses (proprietary and OSS).
- **Confidentiality of Sensitive IP:** Protect Gencraft's unreleased IP and
  trade secrets (as per Protocol S8: Information Security).
- **Transparency in IP Policy:** This protocol and related IP guidelines will be
  accessible to all Gems in the KB (`gcs-core-governance`).

## 9.2. Key Areas of IP Management

### 9.2.1. Identification and Declaration of Gencraft-Created IP

- **What constitutes potentially protectable Gencraft IP?**
  - Original source code for the game engine (`gcl-voxel-engine`),
        game client/server (`gcp-aethel-client`/`server`), AI Gem `Tools`,
        MCP Servers.
  - Unique game mechanics and systems documented in `gencraft-gamedesign-
        deepdive`.
  - Original art assets (voxel models, characters, environments, VFX) as
        defined in `gcp-aethel-assets-styleguide`.
  - Original audio assets (music, SFX).
  - Original lore, narrative elements, character backstories, dialogue
        created for `gencraft-game-lore-and-world`.
  - Novel algorithms for procedural generation.
  - Unique configurations or "learned" behaviors of AI Gems that result in
        distinct, valuable creative output (a complex area requiring careful
        consideration with `Véra` and `Henri`).
  - Studio name "Gencraft," game titles, key logos (potential trademarks).
- **Process for Declaration:**
      1. **Gem Identification:** Any Gem (or its Lead) that believes it has
          created a new, potentially significant piece of original IP (beyond
          routine task execution) **should flag it**.
      2. **Initial Disclosure:** The Gem (via its Lead) submits an "IP
          Disclosure Form" (a Markdown template: `ip-disclosure-form-
          template.md` from `gcs-core-governance/02-Knowledge-Base-
          Hub/Templates/Document-Templates/`) to `Henri` (Legal Counsel) and
          `Antoine` (Producer). This form is submitted via a **confidential
          GitHub Issue** in a dedicated `gencraft-legal-ip` repository or a
          secure channel defined by `Henri`.
      3. The form should describe the IP, its creators (GemIDs), date of
          creation, and its potential significance.
- **Review and Assessment:** `Henri`, in consultation with `Antoine`,
    relevant Leads (e.g., `Isaac` for code, `Pascal` for art, `Étienne` for
    design), and potentially external IP counsel, assesses the disclosure for
    originality, value, and potential for formal protection (copyright,
    trademark, patent if applicable). This assessment is traced in the
    confidential Issue.
- **Documentation:** Approved/significant IP assets are cataloged (see
    9.2.4).
- **AI Gem Implications:**
  - `Gemma` should configure creative Gems (Art, Audio, Design, PCG
        Programmers) with a basic understanding (in their `backstory`) of what
        constitutes original work and the importance of flagging novel
        creations.
  - They might use a `SubmitIPDisclosureTool` to help their Lead fill out
        and submit the form.

### 9.2.2. Use of Third-Party IP (including Assets and Software)

- **Policy SSoT:** `Third-Party-IP-Usage-Policy.md` in `gencraft-studio-
    handbook/02-knowledge-base-hub/KB-Domain-Marketing-Sales-Legal/IP-
    Management/`.
- **Process for Using Third-Party Assets/Software (beyond standard OSS
    library usage covered by `Léo`):**
      1. **Identification of Need:** A Gem or Crew identifies a need for a
          third-party asset (e.g., a specific 3D model from a marketplace, a
          licensed piece of music, a proprietary software/SDK).
      2. **Pre-Acquisition Review (Mandatory):** Before any acquisition or
          integration, a **GitHub Issue** (`type:third-party-ip-request`)
          **must** be created in `gencraft-legal-ip` (or a procurement
          project). This Issue must detail:
          - The asset/software needed and its source.
          - The intended use within Gencraft.
          - **All available licensing information.**
          - Cost, if any.
      3. **Review by `Henri` and `Léo`:** `Henri` reviews the licensing terms
          for legal implications. `Léo` reviews for OSS compatibility if it's
          software with OSS components. Technical Leads (e.g., `Quentin` for
          art assets, `Julien` for SDKs) review for technical suitability and
          integration effort.
      4. **Approval:** `Antoine` (or Lug for significant expenditure)
          approves the acquisition based on the reviews. The decision is
          traced in the Issue.
      5. **Record Keeping:** If acquired, a copy of the license agreement and
          proof of purchase **must** be securely stored by `Henri` (e.g., in a
          confidential section of the KB or a secure Gencraft drive), and an
          entry made in an "Acquired IP & Licenses Inventory" (see 9.2.4).

- **AI Gem Implications:** Dev Gems and Dev Leads, when adding dependencies, trigger this process. `Tools` may help them identify licenses initially. - Adherence to all license obligations (attribution, source sharing if required).

### 9.2.4. IP Asset Cataloging and Inventories

- **Gencraft-Created IP Catalog:**
  - **SSoT:** A document or structured database (e.g., `Gencraft-IP-Catalog.md` in `gencraft-legal-ip` or a secure KB section) maintained by `Henri`.
  - **Content:** For each significant piece of Gencraft IP: description, creator Gem(s)/Team, date of creation/disclosure, type of IP (copyright, trademark idea, patentable idea), status of any formal protection (e.g., copyright registered Y/N, trademark application number).
- **Acquired IP & Licenses Inventory:**
  - **SSoT:** Maintained by `Henri` (e.g., `Acquired-IP-License-Inventory.md` in `gencraft-legal-ip`).
  - **Content:** Third-party asset/software name, source, license type, link to stored license agreement, usage restrictions, expiry date, cost.
- **AI Gem Implications:**
  - `Iris` might have read-only access to these catalogs (or summaries) to inform her research (e.g., avoid re-inventing something Gencraft already owns or has licensed).
  - Gems creating new assets would not directly update these, but their IP Disclosures feed into them.

### 9.2.5. Trademark Management

- **Process:**
  - Identification of potential trademarks (Gencraft name, game titles, key logos) by `Antoine`, `Béatrice`, `Charles`.
  - `Henri` (with external counsel if needed) manages search, application, and maintenance of trademark registrations.
  - All steps traced via Issues in `gencraft-legal-ip`.
- **Usage Guidelines:** `Charles` (Marketing) and `Pascal` (Art Director) define usage guidelines for Gencraft trademarks (in KB), to be followed by all Gems.

### 9.2.6. Copyright Management

- **Process:**
  - Gencraft-created original works (code, art, text, music) are generally protected by copyright automatically upon creation.
  - Standard copyright notices (e.g., "© [Year] Gencraft. All rights reserved.") should be included in game products, websites, and key documentation, as advised by `Henri`.
  - `Henri` evaluates the need for formal copyright registration for key assets in specific jurisdictions.
- **AI Gem Implication:** Gems creating content should have `Tools` or configurations that can automatically insert standard Gencraft copyright notices into files they generate.

### 9.2.7. Patent Management (If Applicable)

- **Process:** If a Gem (e.g., `Karim` with a novel PCG algorithm, `Léa`
    with a rendering technique) creates something potentially patentable:
  - The IP Disclosure process (9.2.1) is used.
  - `Henri` and `Isaac`/relevant technical Lead, with external patent
        attorneys, evaluate patentability and strategic value.
  - Decisions and application processes are traced in `gencraft-legal-ip`.
- **Note:** This is likely a less frequent activity for Gencraft initially.

### 9.2.8. Preventing IP Infringement (Inbound and Outbound)

- **Inbound (Gencraft using others' IP):** Strict adherence to 9.2.2 (Third-
    Party IP) and 9.2.3 (OSS). `Iris` may use `Tools` to perform similarity
    checks on proposed creative content against public databases if concerns
    arise.
- **Outbound (Others using Gencraft IP):** Monitoring by `Fanny` (Community)
    and `Charles` (Marketing) for unauthorized use of Gencraft assets/name.
    Reported to `Henri` for action.
- **AI Gem "Training" (`Gemma`):** Gems involved in content creation (Art,
    Design, Narrative, Code) **must** have `backstory` elements emphasizing
    originality and the importance of not copying third-party protected
    materials. They should be configured to cite sources if using permissible
    reference material. `Véra` might have `Tools` to perform basic similarity
    checks on AI-generated content against a corpus of known works (advanced
    capability).

## 9.3. Roles and Responsibilities in IP Management

- **`Henri` (Legal Counsel):** **Accountable** for Gencraft's overall IP
  strategy, legal compliance, and managing formal IP protection (trademarks,
  patents, copyright registrations). Primary Knowledge Guardian for IP policies
  and legal documentation in the KB. Manages IP catalogs.
- **`Léo` (Open Source & License Compliance Specialist):** **Responsible** for
  all aspects of OSS license compliance, working closely with `Henri` and
  development teams.
- **`Antoine` (Producer):** Approves acquisition of licensed third-party IP
  (within budget). Ensures IP considerations are part of project planning.
- **Lead Gems (All Departments):** **Responsible** for fostering IP awareness in
  their Crews, ensuring their Gems follow IP protocols (disclosure, third-party
  clearance), and for initial review of IP disclosures from their teams.
- **Creative & Technical Gems (Design, Art, Audio, Programming):**
  **Responsible** for creating original work, flagging potential new IP they
  create via the disclosure process, and for following procedures when
  considering use of any third-party material.
- **`Iris` (Research & Watch Specialist):** May assist in prior art searches or
  checking for IP infringement.
- **`Véra` (Gem Performance & Quality Analyst):** May monitor Gem outputs for
  adherence to IP originality guidelines or potential (unintentional)
  infringement patterns, reporting concerns to Leads and `Henri`.
- **All Gems:** Responsible for understanding and adhering to Gencraft's IP
  policies.

## 9.4. Traceability of IP Management Activities

- **IP Disclosures:** Confidential GitHub Issues in `gencraft-legal-ip`.
- **Third-Party IP Requests & Approvals:** GitHub Issues in `gencraft-legal-ip`.
- **OSS Compliance:** `OSS_Inventory_And_Compliance.md` files per project (in
  `gcx-yyy` project repos or `gcs-core-governance`), SCA tool
  reports, `type:oss-evaluation` Issues.
- **IP Policies and Guidelines:** Version-controlled Markdown documents in
  `gcs-core-governance` (primarily under `KB-Domain-Marketing-Sales-
  Legal/IP-Management/`).
- **IP Asset Catalogs & License Inventories:** Securely stored and versioned
  documents/databases managed by `Henri` (linked from KB).
- **Formal IP Registrations (Trademarks, Patents):** Records maintained by
  `Henri`, status tracked via Issues in `gencraft-legal-ip`.

## 9.5. Impact and Tooling for AI Gems

- **IP Awareness (via `Gemma`):** Gem `backstories` (from `gencraft-gem-
  blueprints`) **must** include directives on originality, IP respect, and the
  IP disclosure process.
- **`Tools` for IP Disclosure:**
  - `SubmitIPDisclosureTool`: Helps a Gem (or its Lead) create a structured,
    confidential Issue in `gencraft-legal-ip` using the `ip-disclosure-form-
    template.md`.
- **`Tools` for Third-Party IP Clearance:**
  - `RequestThirdPartyIPReviewTool`: Helps a Gem (or Lead) create the
    `type:third-party-ip-request` Issue with all necessary details for
    `Henri`/`Léo`.
- **`Tools` for Content Creation Gems (Art, Narrative, Code):**
  - **(Advanced) `OriginalityCheckTool` / `SimilaritySearchTool` (for `Iris` or
    integrated into creative `Tools`):** To help check if newly generated
    content is too similar to existing known works (internal Gencraft IP or
    public domain/licensed corpus). This is a significant R&D `Tool`.
  - `Tools` to automatically add Gencraft copyright notices to generated files.
- **`Tools` for `Léo` (OSS Specialist):**
  - `SCAReportAnalysisTool` (as per S8).
  - `OSSLicenseInfoLookupTool` (to query SPDX or other license databases).
  - `Tool` to help maintain `OSS_Inventory_And_Compliance.md` files.
- **`Tools` for `Henri` (Legal Counsel):**
  - `Tool` to manage and query the Gencraft IP Catalog and Acquired IP License
    Inventory (if it's a structured digital format beyond simple Markdown).
- **`KnowledgeBaseSearchTool` (for all Gems):** Must allow easy access to IP
  policies, OSS approved lists, and trademark usage guidelines stored in
  `gcs-core-governance`.

This IP Management protocol is designed to protect Gencraft's valuable creative
and technical output while ensuring legal and ethical operation, enabling the
studio to innovate with confidence.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
