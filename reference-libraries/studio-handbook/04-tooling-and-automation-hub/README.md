---
docId: ENG-READ-004
title: "Tooling and Automation Hub — Index"
version: 1.0.0
authors:
- Architecture Lead
creation_date: '2026-05-07'
last_updated_date: '2026-05-20'
language: en
knowledgeGuardian:
- Governance Crew
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/04-tooling-and-automation-hub/README.md
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: engineering
  doc-type: readme
  security-classification: l2_confidential
  intended-audience:
  - contributors
  - ai-agents
  keywords:
  - index
  - navigation
  - eng-read-001
---
# Readme

Welcome to the Gencraft Studio Tooling and Automation Hub. This central repository provides comprehensive documentation for all AI Gem Tools, Core Studio Services, Model Context Protocol (MCP) Servers, CrewAI workflows, and adopted frameworks that power our studio's operations.

This hub is designed to be the single source of truth for understanding, utilizing, and contributing to our automation systems. Here you will find development standards, overviews, catalogs, and operational guides to ensure efficient and consistent use of our tooling and automation capabilities. Please explore the index below to navigate to the specific resources you need.

---

## Index of Contents

### Subdirectories

- [04-3-adopted-frameworks-and-protocols/]
- [gemma-operational-guides/](./gemma-operational-guides)
- [mcp-servers/](./mcp-servers)
- [tools/](./tools)

### Files

- [Ai Tool Development Standards]: This document outlines the mandatory
Design Review process for new AI Tools and significant architectural changes to existing ones. It ensures
technical soundness, security, and alignment with Gencraft’s strategy, validating the tool’s need and
identifying potential risks early in the development lifecycle.
- [Automation Scripts Actions]: This document details the use of automation
scripts and GitHub Actions within Google Cloud Studio, outlining how to create and execute workflows for
managing and deploying applications. It provides guidance on integrating these tools for streamlined operations.
- [Crewai Workflows Repository Standard]: This document establishes
standards for the `gencraft-crewai-workflows` Git repository, defining a mandatory structure and development
workflow for Gencraft Crew definitions. It ensures consistency, reusability, and maintainability of Crews used
throughout the studio.
- [Gem Tools Overview]: This document provides a comprehensive overview of Gencraft’s
AI Gem Tool ecosystem. It outlines the philosophy, categories, and development standards for these tools,
emphasizing their modularity, reusability, and discoverability. The document details a strategy for Gems to
effectively utilize available tools, including a programmatic discovery service.
- [Mcp Servers Catalog]: This document serves as the central, authoritative catalog
for all Model Context Protocol (MCP) Servers deployed within the Gencraft studio. It details the purpose, API,
ownership, and operational parameters of each MCP Server, facilitating discovery and integration by Gems and
Tools.
- [Studio Crews Overview]: This document provides an overview of Gencraft "Crews,"
which are teams of AI Gems designed to automate studio processes. It details the principles, structure, and
catalog of these Crews, aiming to enhance efficiency and consistency across Gencraft operations.

## IA Instructions

This document serves as the main index for the Gencraft Studio "Tooling and Automation Hub".

**Purpose for AI Agents:**

- Use the `docId` (`GC04-README-IDX-006`) for direct reference to this index.
- Navigate to the individual documents or subdirectories listed under "Index of Contents" to access specific standards, overviews, catalogs, or guides related to AI Gem Tools, Core Studio Services, MCP Servers, CrewAI workflows, and adopted frameworks.
- This hub is critical for understanding the technical landscape of Gencraft's automation and tooling.
- When tasked with developing, integrating, or understanding a studio tool or automated process, consult this index to find relevant documentation and standards.
- The `summary` field in the frontmatter of this document and linked documents provides a concise overview of their content.
