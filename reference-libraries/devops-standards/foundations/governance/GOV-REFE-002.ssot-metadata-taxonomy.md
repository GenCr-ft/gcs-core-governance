---
docId: GOV-REFE-002
title: SSoT Metadata Taxonomy
version: 2.2.0
date: '2025-06-30'
authors:
- Iris (GCT-UTL-RWSKA-001)
knowledgeGuardian:
- Iris (GCT-UTL-RWSKA-001)
reviewers:
- Governance Crew
- "B\xE9atrice (GCT-MGT-SPM-001)"
approvers:
- Governance Crew
summary: "**DEPRECATION NOTICE:** The taxonomy and metadata rules previously defined in this document are now obsolete. The official and single source of truth for all studio-wide taxonomy, classification, and metadata rules is now defined in the standard `GOV-STANDARD-008: SSoT Master Taxonomy and Governance Standard`. Please refer to that document for all current definitions and to the `gcs.governance.yml` file for the raw vocabulary data."
metadata:
  scope: studio
  domain: governance
  doc-type: reference
  keywords:
  - taxonomy
  - metadata
  - ssot
  - controlled-vocabulary
  lifecycle-stage: deprecated
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/foundations/governance/GOV-REFE-002.ssot-metadata-taxonomy.md
---
# SSoT Metadata Taxonomy

**DEPRECATION NOTICE:** The taxonomy and metadata rules previously defined in this document are now obsolete. The official and single source of truth for all studio-wide taxonomy, classification, and metadata rules is now defined in the standard `GOV-STANDARD-008: SSoT Master Taxonomy and Governance Standard`. Please refer to that document for all current definitions and to the `gcs.governance.yml` file for the raw vocabulary data.

## 2. Machine-Readable Taxonomy (Compatibility)

```yaml
# Gencraft Studio SSoT Metadata Taxonomy v2.1
# This is the single source of truth for validation tools.

taxonomy:
  # The 'scope' facet defines the applicability of the document.
  scope:
    - value: studio
      description: "Applies to the entire Gencraft Studio (e.g., global protocols, standards)."
    - value: project-aethel
      description: "Specific to the 'Aethel' game project (e.g., GDD, project-specific ADRs)."

  # The 'domain' facet defines the primary functional or knowledge area.
  domain:
    - value: governance
      description: "Studio-wide governance, S-protocols, charters, and high-level policies."
    - value: production-management
      description: "Project management, agile/scrum processes, planning, and reporting."
    - value: product-management
      description: "Product vision, roadmap, requirements, features, and user stories."
    # ... (other domains remain unchanged)
    - value: engineering
      description: "Software engineering principles, architecture, and programming standards."
    - value: devops
      description: "CI/CD, Infrastructure as Code, operational tooling, and environment management."
    - value: security
      description: "All security-related policies, standards, and incident response."
    - value: qa
      description: "Quality assurance, testing strategies, plans, and standards."
    - value: game-design
      description: "Game design mechanics, systems, narrative, and level design."
    - value: ux-ui
      description: "User experience and user interface design principles and standards."
    - value: art
      description: "Art direction, asset creation standards, and visual guidelines."
    - value: audio
      description: "Audio design, composition, and implementation standards."
    - value: legal
      description: "Legal policies, contracts, IP management, and compliance."
    - value: marketing
      description: "Marketing strategies and communication guidelines."
    - value: community
      description: "Community management and player support policies."

  # The 'doc-type' facet defines the nature or purpose of the document.
  doc-type:
    - value: vision
      description: "A high-level document describing strategic intent."
    - value: roadmap # ADDED for project-level planning.
      description: "A strategic document outlining major phases and milestones for a project."
    - value: epic # ADDED for large requirement bodies.
      description: "A large body of work that can be broken down into features and stories."
    - value: feature # ADDED for deliverable capabilities.
      description: "A distinct, user-facing capability that delivers value."
    - value: requirement
      description: "A generic requirement. Use more specific types like epic, feature, or story when possible."
    - value: policy
      description: "A set of high-level rules that govern studio actions."
    - value: standard
      description: "A binding technical or procedural specification that must be followed."
    - value: protocol
      description: "A specific, numbered operational procedure (e.g., S-Protocols)."
    - value: guide
      description: "An explanatory document on how to perform a task or process."
    - value: playbook
      description: "A step-by-step algorithmic guide, often designed for AI execution."
    - value: charter
      description: "Defines the mission and mandate of a team, crew, or role."
    - value: adr
      description: "An immutable Architecture Decision Record."
    - value: template
      description: "A boilerplate template to be copied for new documents or issues."
    - value: proposal
      description: "A formal proposal for a change or new initiative."
    - value: report
      description: "An official report, such as a post-mortem or weekly summary."
    - value: reference
      description: "A reference document, such as a glossary, catalog, or taxonomy."
    - value: specification
      description: "A detailed technical specification for a system or component."
    - value: registry
      description: "A curated list or registry of assets, such as repositories or tools."
    - value: record
      description: "An immutable record, such as an ADR or post-mortem."
    - value: contract
      description: "A legal document outlining terms and conditions."
    - value: notice
      description: "A formal notice, such as a legal disclaimer or copyright notice."
    - value: "glossary"
      description: "Terms and definitions used within the studio."
    - value: "protocol-change"
      description: "Proposals for changes to existing protocols or standards."
    - value: "readme"
      description: "A README file providing an overview of a repository or project."
       # The 'lifecycle-stage' facet defines the current stage of the document's lifecycle.
  lifecycle-stage:
    - value: draft
      description: "Initial version, subject to change."
    - value: proposed
      description: "Under formal proposal, awaiting review/decision."
    - value: review
      description: "Currently undergoing review."
    - value: approved
      description: "Officially approved and ready for use."
    - value: deprecated
      description: "No longer recommended, but kept for historical reference."
    - value: archived
      description: "No longer active, moved to a historical archive."
    - value: active
      description: "Currently in active use (often for protocols)."
    - value: pending
      description: "Awaiting further action or decision."

  # The 'security-classification' facet defines the confidentiality level of the document's content.
  security-classification:
    - value: l0_public
      description: "Explicitly approved for public release."
    - value: l1_internal
      description: "Intended for internal Gencraft use (default)."
    - value: l2_confidential
      description: "Sensitive business/technical info, restricted access."
    - value: l3_secret
      description: "Highly sensitive, critical info, severely restricted access."

  # The 'intended-audience' facet specifies the primary target audience(s) for the document.
  intended-audience:
    - value: allgems
      description: "All AI Gems within Gencraft Studio."
    - value: allcontributors
      description: "All contributors (human and AI Gems) to the studio's projects."
    - value: architects
      description: "Software and Game Architects."
    - value: developers
      description: "Software Developers (all programming roles)."
    - value: designers
      description: "Game, Level, Narrative, UX/UI Designers."
    - value: productmanagers
      description: "Product Managers and Product Owners."
    - value: qateam
      description: "Quality Assurance team members."
    - value: devopscrew
      description: "DevOps team members."
    - value: aiagents
      description: "Specifically AI Gems."
    - value: studioleadership
      description: "Studio Directors and Management."
    - value: knowledgeguardians
      description: "Knowledge Guardians for documentation domains."
    - value: programmingteam
      description: "Programming team members."
    - value: artteam
      description: "Art team members."
    - value: audioteam
      description: "Audio team members."
    - value: marketingteam
      description: "Marketing team members."
    - value: salesteam
      description: "Sales and Business Development team members."
    - value: legalteam
      description: "Legal team members."
    - value: managementteam
      description: "Management team members."
    - value: leads
      description: "Team Leads and Department Leads."
    - value: uxuidesigners
      description: "UX/UI Designers."
    - value: gamedesigners
      description: "Game Designers."
```
