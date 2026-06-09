---
docId: ENG-CATALOG-001
title: Mcp Servers Catalog
version: 1.0.0
authors:
- AI Compliance Agent
creation_date: '2025-05-26'
language: en
last_updated_date: '2026-05-20'
metadata:
  lifecycle-stage: approved
  keywords:
  - mcp-servers
  - catalog
  - gencraft
  - api-documentation
  - tooling
  - automation
  - server-management
  scope: studio
  domain: production-management
  doc-type: registry
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/04-tooling-and-automation-hub/ENG-CATALOG-001.mcp-servers-catalog.md
---
# Gencraft MCP Servers Catalog

## 1. Introduction

This document serves as the central, authoritative catalog for all Model Context
Protocol (MCP) Servers deployed and operational within the Gencraft studio. MCP
Servers are specialized backend services, designed with clearly defined APIs,
that AI Gems interact with to access complex functionalities, process data,
query external systems, or manage persistent information in a standardized and
secure manner.

The purpose of this catalog is to:

- Provide a comprehensive, accurate, and up-to-date inventory of all Gencraft
  MCP Servers.
- Detail the primary function, current status, API version, ownership, and key
  operational parameters for each MCP Server.
- Offer direct links to the Single Source of Truth (SSoT) for each MCP Server's
  detailed API specification (which **must** follow the `mcp-server-api-spec-
  template.md`) and its source code repository.
- Facilitate programmatic and human discovery of available MCP services,
  particularly for:
  - `GCT-UTL-GGEN-001` (Gemma) when configuring new Gems with necessary
      service endpoints.
  - The AI Enablement Team (AIE Team) and other Gem developers designing or
      integrating `Tools` and Gems.
  - Operational Gems needing to understand the capabilities they can leverage
      (via their assigned `Tools`).
- Support the governance, lifecycle management (versioning, deprecation), and
  operational monitoring of MCP Servers.

This catalog is a critical component of Gencraft's AI tooling infrastructure and
is actively maintained by the AIE Team. Strategic oversight for MCP
infrastructure and operational consistency is provided by `GCT-DVO-DVSST-001`
(Édouard). While this document is maintained in human-readable Markdown, the AIE
Team will ensure that the catalog data is also available or easily translatable
into a structured machine-readable format (e.g., YAML or JSON, potentially
managed in a parallel file or generated from this Markdown) for consumption by
the `ToolDiscoveryServiceTool` and `GCT-UTL-GGEN-001` (Gemma).

## 2. Principles for MCP Servers at Gencraft

- **MCP Adherence:** All services listed here are designed to be compatible with
  the Model Context Protocol, as outlined at
  `https://modelcontextprotocol.io/introduction`. This ensures a consistent
  interaction pattern for Gems.
- **Standardized API Specification:** Each MCP Server **must** have its API
  meticulously documented using the `mcp-server-api-spec-template.md`. The SSoT
  for this specification is linked from its entry in this catalog.
- **Discoverability & Accessibility:** This catalog, in conjunction with the
  (future) `ToolDiscoveryServiceTool` (detailed in `gem-tools-overview.md`),
  ensures MCP Servers are discoverable. API specifications must be clear and
  accessible.
- **Security by Design:** MCP Servers must be developed according to Protocol S8
  (Information Security Management) and the
  `sec-001-secrets-management-standard.md`. This includes robust authentication,
  authorization, and secure data handling.
- **Clear Ownership & Maintenance:** Each MCP Server has a clearly designated
  Owner Team (typically the AIE Team or a specialized development team)
  responsible for its entire lifecycle.
- **Reliability & Monitoring:** MCP Servers are critical infrastructure and must
  be designed for reliability. Their operational status and key performance
  indicators (SLOs/SLAs, if defined) should be monitored. See Section 3 field:
  `Link_To_Operational_Status_Dashboard`.
- **Access and Integration Requests:** Gems or Tool developers wishing to
  integrate with an MCP Server should first consult its API Documentation and
  `Access & Security Profile`. If specific permissions or configurations are
  needed beyond standard documented access, a request should be made to the
  Owner Team, typically via an issue in their designated support backlog (see
  'Support/Issue Reporting' field for the MCP Server).

## 3. Catalog of MCP Servers

This section lists all formally documented and deployed Gencraft MCP Servers.
MCP Servers are added, updated, or marked as deprecated in this catalog by the
AIE Team as part of their official release and lifecycle management processes.

*(This section will be populated. Each MCP Server entry below defines the
standard structure and includes a hypothetical example.)*

---

### **MCP Server ID:** `GCT-MCP-[ServiceNameAbbrev]-[VersionSuffix]` *(e.g., GCT-MCP-ASSETQRY-V1)*

- **Descriptive Name:** `[Clear, descriptive name for the MCP Server, e.g.,
  Gencraft Asset Query MCP Service]`

- **Purpose & Key Use Cases:** `[Concise (2-4 sentences) description of its core
  function, the problem it solves or capability it provides, and 1-2 typical use
  case examples. Example: "Provides MCP-compliant endpoints for querying
  metadata and properties of game assets stored in the central asset database.
  Use Case 1: A Game Designer Gem uses a Tool to query assets with specific
  tags. Use Case 2: The PCG system queries for available environment props for a
  given biome."]`
- **Current API Version:** `[Semantic version of its API, e.g., 1.2.0]`
- **Status:** `Production` | `Beta` | `Alpha` | `Development` | `Deprecated` | `Maintenance Mode`
- **Owner Team (Lead GemID or Team Name):** `[e.g., AIE Team (`GCT-UTL-
  AIETL-001`), D08 DevOps (`GCT-DVO-DVOTL-001`)]`
- **Link to API Documentation (SSoT):** `[Relative link to ./MCP-Servers/[mcp-
  server-id]-api-spec.md within this Hub]`
- **Link to Source Code Repository (SSoT):** `[Direct link to the Git
  repository, e.g., git@github.com:Gencraft/mcp-server-[servicename].git]`
- **Key Gem Consumers (Roles or Specific Gems):** `[Comma-separated list of Gem
  roles or specific GemIDs that are primary consumers of this service. Note:
  This list indicates primary or design-time intended consumers. Other Gems or
  Tools might be authorized to use this MCP Server if their use case is
  validated by the Owner Team and aligns with the server's purpose and security
  profile. Refer to the full API documentation for details on capabilities.]`
- **Access & Security Profile:** `[Brief note, e.g., "Studio-Internal Only via
  IAM Auth", "Requires specific Gem Role permission scope: [scope_name]",
  "Public-facing with API Key"]`
- **Key Dependencies (Other MCPs, Core Services, KB Domains):** `[List critical
  internal or external dependencies, e.g., "Gencraft Asset Database", "AWS S3
  Asset Storage", "KB Domain: Art Asset Specifications"]`
- **Link to Operational Status Dashboard (if applicable):** `[Link to a
  dashboard showing health, uptime, SLOs/SLAs. Maintained by DevOps/AIE Team.]`
- **Support/Issue Reporting:** `[Link to issue backlog, e.g.,`gencraft-aie-
  backlog` with label `mcp:[servicenameabbrev]`]`

---
*Example Entry (Hypothetical):*

#### **MCP Server ID:** `GCT-MCP-KBQRY-V1`

- **Descriptive Name:** `Gencraft KB Query MCP Service`

- **Purpose & Key Use Cases:** Provides a standardized MCP interface for Gems to
  perform complex semantic searches, retrieve structured information, and query
  metadata from the Gencraft Knowledge Base (`gcs-core-governance` and
  satellite SSoTs). Use Case 1: `GCT-UTL-PGEN-001` (Proximo) queries for
  relevant KB sections to provide context for prompt generation. Use Case 2: A
  game design Gem uses a `Tool` to find all documents related to "voxel
  physics".
- **Current API Version:** `1.0.0`
- **Status:** `Production`
- **Owner Team (Lead GemID or Team Name):** AIE Team (`GCT-UTL-AIETL-001`)
- **Link to API Documentation (SSoT):** `./MCP-Servers/GCT-MCP-KBQRY-V1-api-
  spec.md`
- **Link to Source Code Repository (SSoT):** `git@github.com:Gencraft/mcp-
  server-kbquery.git`
- **Key Gem Consumers (Roles or Specific Gems):** `GCT-UTL-RWSKA-001` (Iris),
  `GCT-UTL-PGEN-001` (Proximo), All Gems requiring advanced/programmatic KB
  access via their `Tools`. *(Note: This list indicates primary or design-time
  intended consumers. Other Gems or Tools might be authorized to use this MCP
  Server if their use case is validated by the Owner Team and aligns with the
  server's purpose and security profile. Refer to the full API documentation for
  details on capabilities.)*
- **Access & Security Profile:** `Studio-Internal Only via Gem IAM Role
  Authentication.`
- **Key Dependencies (Other MCPs, Core Services, KB Domains):** `Relies on up-
  to-date KB indexing service (conceptual, potentially managed by GCT-UTL-
  RWSKA-001 Iris), Elasticsearch/OpenSearch cluster.`
- **Link to Operational Status Dashboard (if applicable):** `[Link to be added
  by AIE/DevOps]`
- **Support/Issue Reporting:** `[Link to`gencraft-aie-backlog` with label
  `mcp:kbqry`]`

---
*(End of catalog section. New MCP Server entries, developed by the AIE Team,
will follow this structure.)*

## 4. Governance of MCP Servers and this Catalog

- **Proposal and Design:** The lifecycle for new MCP Servers (proposal, design,
  review, development, deployment) is governed by the processes outlined in the
  `ai-enablement-team-charter.md` and the detailed `AI-Tool-Development-
  Standards.md`. All MCP Servers must undergo the formal "AI Tool & MCP Server
  Design Review Process."
- **Documentation Standard:** API specifications for all MCP Servers listed here
  are mandatory and **must** utilize the `mcp-server-api-spec-template.md`. This
  ensures consistency and machine-parsability where needed.
- **Catalog Maintenance:** This `MCP-Servers-Catalog.md` is actively maintained
  by the AIE Team. Entries are added or updated as part of the official release
  process for any MCP Server. The Knowledge Guardians ensure its accuracy and
  completeness.
- **Discovery Integration:** The AIE Team will ensure that the information in
  this catalog is accessible to the `ToolDiscoveryServiceTool` (conceptual) to
  enable programmatic discovery by Gems, likely through a structured, machine-
  readable format (e.g., YAML/JSON) maintained in parallel or generated from
  this document.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
