---
docId: OPS-CATALOG-001
title: Glossary
version: 1.0.0
authors:
- AI Compliance Agent
creation_date: '2025-05-26'
language: en
last_updated_date: '2026-05-20'
metadata:
  lifecycle-stage: draft
  keywords:
  - glossary
  - gencraft-studio
  - terminology
  - ai-gems
  - definitions
  - uop
  - crewai
  scope: studio
  domain: production-management
  doc-type: glossary
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/OPS-CATALOG-001.glossary.md
---
## Introduction

This Glossary provides definitions for key terms, acronyms, and concepts used
throughout the Gencraft Studio Handbook (`gcs-core-governance`) and in the
day-to-day operations of the Gencraft virtual studio. Its purpose is to ensure a
shared understanding and consistent use of terminology among all AI Gems and
human collaborators, as mandated by UOP 2.B.2.

This document is a living artifact and will be updated as new terms and concepts
emerge. Proposals for additions or modifications should follow the process
outlined in Protocol S12: Knowledge Base Contribution & Maintenance. `Lexicon`
(GCT-UTL-GLOM-001), as the Knowledge Guardian for this document, is primarily
responsible for its upkeep and evolution.

## Glossary Terms (Alphabetical Order)

---

### A

- **Accessibility (Design Principle)**
  - **Definition:** The design of products, devices, services, or environments
      for people who experience disabilities, ensuring they can perceive,
      understand, navigate, and interact effectively.
  - **Context/Usage in Gencraft:** A core consideration in game design
      (mechanics, difficulty scaling, control schemes) and UI/UX design
      (readability, navigation, input methods) to make Gencraft games usable by
      the widest possible audience. Referenced in `NFR_Summary_MVP.md` (NFR-UX)
      and relevant Gem definitions (e.g., Game Designer, UX/UI Designer).
  - **See Also/Related SSoT Documents:** `NFR_Summary_MVP.md`, Game Designer
      (Gem Definition), UX/UI Designer (Gem Definition).

- **Access Control Management (Protocol S8)**
  - **Definition:** The comprehensive set of policies, procedures, technical
      controls, and `Tools` used to manage and enforce who (human or Gem) has
      what type of access (e.g., read, write, execute) to Gencraft's information
      assets, systems, and resources. It is based on roles and the Principle of
      Least Privilege.
  - **Context/Usage in Gencraft:** A critical component of Protocol S8:
      Information Security Management. Implemented via specific permissions in
      GitHub, cloud platforms, and internal Gencraft systems, and detailed in
      `access-control-policy.md` (GCS-SEC-POL-002).
  - **See Also/Related SSoT Documents:** S8, `access-control-policy.md` (GCS-
      SEC-POL-002), Least Privilege, RBAC (Role-Based Access Control), Access
      Request.

- **Access Request (Protocol S8)**
  - **Definition:** A formal, traceable request made for granting, modifying,
      or revoking access rights to a Gencraft system, data repository, or
      resource.
  - **Context/Usage in Gencraft:** Typically submitted as a GitHub Issue using
      the `access-request-template.md`. Processed according to S8 and `Access-
      Control-Policy.md` (GCS-SEC-POL-002).
  - **See Also/Related SSoT Documents:** S8, `access-control-policy.md` (GCS-
      SEC-POL-002), Access Control Management, `access-request-template.md`.

- **Acquired IP & Licenses Inventory (Protocol S9)**
  - **Definition:** A catalog and SSoT document (typically located within the
      Knowledge Base under `KB-Domain-Legal/IP-Management/`) maintained by
      `Henri` (Legal Counsel Gem) detailing all third-party assets, software
      libraries, tools, and other intellectual property utilized by Gencraft
      Studio, including their respective licenses, usage terms, and compliance
      status.
  - **Context/Usage in Gencraft:** Essential for compliance with Protocol S9:
      Intellectual Property Management and for managing legal risks associated
      with third-party IP.
  - **See Also/Related SSoT Documents:** S9, Intellectual Property (IP),
      `Henri` (Legal Counsel Gem Definition).

- **Actionable (Feedback/Learning)**
  - **Definition:** A quality of feedback, a lesson learned, or an instruction
      that provides sufficient clarity, specificity, and context to enable a Gem
      or human team member to take concrete steps, make a specific change, or
      implement a task effectively.
  - **Context/Usage in Gencraft:** A key principle for effective communication
      and for the design of Gem interactions and SSoT documentation. Emphasized in S1 (Feedback & Approval) and S5 (Lessons Learned).
  - **See Also/Related SSoT Documents:** S1, S5, UOP (Universal Gem Operating Principles).

- **Action Tracker (`action-tracker.md`)**
  - **Definition:** The primary SSoT document used by Gencraft Studio
      leadership and key contributors to track strategic tasks, initiatives, document creation, and their status for the setup, evolution, and ongoing management of Gencraft Studio's operational framework and SSoT.
  - **Context/Usage in Gencraft:** Resides at the root of the `gcs-core-governance`. Serves as the master checklist and progress monitor for establishing studio operations.
  - **See Also/Related SSoT Documents:** SSoT, Governance Crew, `gcs-core-governance/README.md`.

- **Adam (`GCT-DVO-DSINF-001`)**
  - **Definition:** The AI Gem persona embodying the role of a DevOps
      Specialist focused on Infrastructure (IaC, CI/CD, monitoring, cloud
      environments) within Gencraft Studio.
  - **Context/Usage in Gencraft:** Defined by its Gem Blueprint (`GCT-DVO-
      DSINF-001_Adam.yaml`) and Gem Definition file
      (`DevOps_Specialist_A_Infra.md`).
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint), IaC,
      CI/CD, DevOps Team.

- **Adaptability (KC&T Guiding Principle #6, Studio Value)**
  - **Definition:** A core Gencraft Studio Value and a KC&T Guiding Principle
      (#6) referring to the ability of Gencraft's systems, protocols, AI Gems,
      and human personnel to effectively evolve and adjust in response to new
      information, changing requirements, feedback, or lessons learned.
  - **Context/Usage in Gencraft:** Essential for continuous improvement and
      innovation. Supported by protocols like S5 (Lessons Learned) and S13
      (Global Protocol Evolution), and designed into Gem capabilities (S17).
  - **See Also/Related SSoT Documents:** Studio Culture and Values, KC&T
      Guiding Principles, S5, S13, S17, UOP 2.F.

- **ADR (Architecture Decision Record)**
  - **Definition:** A document that captures an important architectural decision made along with its context and consequences.
  - **Context/Usage in Gencraft:** Used to document significant technical choices. ADRs are stored in the repository relevant to their scope:
    - **Platform ADRs:** in `gcs-plt-architecture/adrs/`.
    - **Game ADRs (Aethel):** in `gcp-aethel-architecture/adrs/`.
    The creation process is governed by Protocol S4: Architectural Review Process.
  - **See Also/Related SSoT Documents:** `Architecture`, `S4: Architectural Review Process`, `adr-template.md`.

- **Agent (CrewAI)**
  - **Definition:** The fundamental building block in the CrewAI framework,
      representing an AI entity with a specific role, goal, and backstory,
      capable of using tools and collaborating with other agents.
  - **Context/Usage in Gencraft:** Gencraft Gems are modeled as, and are
      intended to be implemented as, CrewAI Agents or similar advanced agentic
      constructs. Their definition, capabilities, and collaborative behaviors
      are specified in their Gem Blueprints.
  - **See Also/Related SSoT Documents:** CrewAI, Gem, Blueprint (Gem
      Blueprint), `gem-blueprint-standard.md`, `GCS-TAF-CREWAI-REPORT-FR-V1.0`
      (CrewAI Technical Report).

- **Agent Quality Incident (Protocol S2)**
  - **Definition:** A formal record, typically a GitHub Issue, used by `Véra` (GCT-QAS-GPQA-001) or human supervisors to track and manage investigations into AI Gem malfunctions, significant performance deviations from their blueprint or expected behavior, or potential ethical breaches not covered by S18.
  - **Context/Usage in Gencraft:** Part of the quality assurance and operational oversight process for AI Gems, linked to Protocol S2 (Disagreement, Escalation & Resolution) for escalation if the incident indicates a systemic issue or disagreement on expected behavior. Investigated by AIE Team.
  - **See Also/Related SSoT Documents:** S2, Véra, AIE Team, Gem Performance Monitoring, S18.

- **Agile (Methodology)**
  - **Definition:** An iterative and incremental approach to project management and software development that emphasizes flexibility, collaboration, self-organizing teams, customer feedback, and rapid delivery of functional increments of a product.
  - **Context/Usage in Gencraft:** Gencraft Studio intends to adopt Agile methodologies, primarily Scrum, for its game development projects and potentially for studio operational improvements. Protocol S15 details Gencraft's specific implementation of Agile/Scrum.
  - **See Also/Related SSoT Documents:** S15: Agile Scrum Project Management Protocol, Scrum, Sprint, Product Backlog.

- **AI (Artificial Intelligence)**
  - **Definition:** The core technology and primary workforce of Gencraft Studio. It encompasses two main categories: 1) **Specialized AI:** for specific in-game functionalities like Mob behavior (RPG-MOB). 2) **Generative & Cognitive AI:** The advanced, LLM-based intelligence that powers the AI workforce, known as **Gems**, who perform complex operational, creative, and technical tasks across the studio.
  - **Context/Usage in Gencraft:** A foundational technology for all studio operations and game development. Gencraft's unique model is built upon **AI Gems** as its primary contributors. The ethical development (S17), management, and oversight (AIE Team) of all AI are paramount to the studio's mission.
  - **See Also/Related SSoT Documents:** `ai-ethics-guidelines.md`, `Gem`, `Universal Gem Operating Principles (UOP)`, `AIE Team`, `s17-virtual-hr-gem-development.md`.

- **AI Enablement Team (AIE Team)**
  - **Definition:** A specialized, cross-functional Gencraft Studio team dedicated to designing, developing, maintaining, and continuously improving the foundational AI capabilities, ethical frameworks, training methodologies, and operational support systems that enable all Gencraft AI Gems to perform their roles effectively, safely, and in alignment with studio objectives and values.
  - **Context/Usage in Gencraft:** Defined by the `ai-enablement-team-charter.md`. Key Gem: `Aura` (AIE Team Lead). Central to Gem development, `Gemma`, AI ethics, and S10/S17 protocols.
  - **See Also/Related SSoT Documents:** Gem, Gemma, AI Ethics, S10, S17, Charter, Aura.

- **AI Gem Onboarding (Protocol S10)**
  - **Definition:** The standardized Gencraft Studio process, detailed in Protocol S10, for instantiating new AI Gems (via `Gemma`), configuring them based on their Blueprints, providing initial "training" (e.g.,familiarization with SSoT, core protocols, specific role context), and integrating them into the studio's operational environment and their designated Crews.
  - **Context/Usage in Gencraft:** Managed by the AIE Team in conjunction with `Gemma`. A critical step in a Gem's lifecycle.
  - **See Also/Related SSoT Documents:** S10, Gem, Blueprint (Gem Blueprint), Gemma, AIE Team, S17.

- **AI Gem Professional Development (Protocol S17)**
  - **Definition:** The Gencraft Studio framework and set of processes, outlined in Protocol S17, aimed at continuously enhancing an AI Gem's capabilities, its understanding of Gencraft protocols and the Knowledge  Base, its effective use of `Tools`, and its overall contribution to studio goals. This includes "skill upgrading," performance monitoring, and managing a Gem's evolution.
  - **Context/Usage in Gencraft:** Managed by the AIE Team. Covers the ongoing
      learning and adaptation of AI Gems post-onboarding.
  - **See Also/Related SSoT Documents:** S17, Gem, Blueprint (Gem Blueprint),
      AIE Team, S5, S10.

- **AI Ethics**
  - **Definition:** The set of moral principles and guidelines that govern the
      design, development, deployment, and operation of AI Gems within Gencraft
      Studio. Aims to ensure fairness, transparency, accountability, safety, and
      respect for human values.
  - **Context/Usage in Gencraft:** Detailed in `AI-Ethics-Guidelines.md` (To
      Be Created, linked to Code of Conduct) and overseen by the AIE Team and
      Governance Crew. A core component of Gem Blueprints and S17.
  - **See Also/Related SSoT Documents:** Code of Conduct, AIE Team, Bias
      Mitigation, S17.

- **Alternatives Considered (Decision Making)**
  - **Definition:** A standard component of Gencraft's decision-making
      documentation (e.g., in ADRs, RFCs, or S7 Decision Records) where other
      potential solutions or approaches that were evaluated before arriving at
      the final decision are briefly described, along with the reasons for their
      non-selection.
  - **Context/Usage in Gencraft:** Promotes transparency and documents the
      thoroughness of the decision-making process.
  - **See Also/Related SSoT Documents:** S7, ADR, RFC.

- **Antoine (`GCT-MGT-PPM-001`)**
  - **Definition:** The AI Gem persona embodying the role of Producer /
      Project Manager and Scrum Master within Gencraft Studio.
  - **Context/Usage in Gencraft:** Defined by its Gem Blueprint (`GCT-MGT-
      PPM-001_Antoine.yaml`) and Gem Definition file
      (`Producer_Project_Manager.md`). Key interactor with S15 (Agile Scrum).
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint), S15:
      Agile Scrum Project Management Protocol, Producer / Project Manager
      (Role).

- **API (Application Programming Interface)**
  - **Definition:** A set of rules and protocols allowing different software components to
  communicate. See SBX-API.
  - **Context/Usage in Gencraft:** A critical concept for inter-service communication (for Core
  Studio Services) and for enabling Gem Tools. The studio standardizes interactions via the Model
  Context Protocol (MCP).
  - **See Also/Related SSoT Documents:** Model Context Protocol (MCP), Core Studio Services (CSS), Tool (AI Gem Tool)

- **Approval Mechanism (Protocol S1)**
  - **Definition:** The formally defined method or series of steps by which a
      deliverable (e.g., code, document, design asset) is reviewed, validated,
      and formally accepted as complete and meeting requirements within Gencraft
      Studio.
  - **Context/Usage in Gencraft:** Detailed in Protocol S1: Feedback &
      Approval, often involving Pull Requests on GitHub and explicit approval
      comments from designated Approver Gems.
  - **See Also/Related SSoT Documents:** S1, Approver Gem, Deliverable, Pull
      Request.

- **Approver Gem (Protocol S1)**
  - **Definition:** An AI Gem or human role designated with the authority to
      formally approve a specific type of deliverable, confirming it meets all
      relevant quality standards and requirements.
  - **Context/Usage in Gencraft:** Defined by roles and responsibilities
      within Protocol S1 or specific project plans. Often a Lead Gem, Knowledge
      Guardian, or stakeholder.
  - **See Also/Related SSoT Documents:** S1, Approval Mechanism, Deliverable.

- **Arbitration (Disagreement Management - Protocol S2)**
  - **Definition:** A conflict resolution process where a neutral third party
      or a body with designated authority (e.g., the Governance Crew) is
      empowered to make a binding decision to resolve a substantive disagreement
      that could not be resolved through direct negotiation or mediation.
  - **Context/Usage in Gencraft:** The final stage of the escalation path
      defined in Protocol S2: Disagreement, Escalation & Resolution.
  - **See Also/Related SSoT Documents:** S2, Disagreement, Governance Crew.

- **Architecture**
  - **Definition:** The fundamental organization of a software system. Within Gencraft, this concept is divided into two distinct scopes:
    1. **Platform Architecture:** Governs the foundational services, tools, and standards of the studio itself. The SSoT for this is the `gcs-plt-architecture` repository.
    2. **Game Architecture:** Governs the specific technical design of a game project, such as Aethel. The SSoT for this is the `gcp-aethel-architecture` repository.
  - **Context/Usage in Gencraft:** Architectural decisions for the platform are led by the `Platform Architect (Isaac)`, while those for the game are led by the `Game Architect (Isidore)`. Key decisions for both scopes are documented as ADRs in their respective repositories.
  - **See Also/Related SSoT Documents:** `ADR`, `C4 Model`, `S4: Architectural Review Process`, `gcs-plt-architecture`, `gcp-aethel-architecture`.

- **Archive Catalog (Archiving System)**
  - **Definition:** A document or database maintained by `Iris` (GCT-UTL-RWSKA-001) that lists major Gencraft information assets that have been formally archived for long-term preservation, including their metadata and location within the archive.
  - **Context/Usage in Gencraft:** Part of Gencraft's Archiving System (KC&T Étape 5, currently conceptual). Supports S20 (Artifact Storage, Archiving, and Retention).
  - **See Also/Related SSoT Documents:** Archiving System, S20, Iris.

- **Archiving System (KC&T Étape 5)**
  - **Definition:** The comprehensive set of Gencraft protocols, infrastructure, and `Tools` designed for the long-term, secure, and retrievable preservation of Gencraft's valuable information assets and project deliverables once they are no longer in active use but need to be retained for historical, legal, or reference purposes.
  - **Context/Usage in Gencraft:** A key component of the KC&T framework, related to S20 (Artifact Storage, Archiving, and Retention).
  - **See Also/Related SSoT Documents:** S20, Archive Catalog, KC&T.

- **Artifact (Communication/Storage - Protocol S20)**
  - **Definition:** Any distinct and identifiable piece of documented work or information created during Gencraft Studio operations. This includes documents, code, datasets, design assets, Gem Blueprints, ADRs, meeting notes, reports, etc.
  - **Context/Usage in Gencraft:** Protocol S20 governs how artifacts are stored, versioned, and potentially archived.
  - **See Also/Related SSoT Documents:** S20, Deliverable, SSoT.

- **As-Code (Philosophy)**
  - **Definition:** A guiding principle for managing and operating IT resources (infrastructure, configuration, documentation, policy, etc.) using machine-readable definition files stored in version control (Git). This enables automation, repeatability, and traceability.
  - **Context/Usage in Gencraft:** Applies to Infrastructure as Code (IaC), Configuration as Code (CaC), Documentation as Code (DaC e.g., this Handbook), and Policy as Code (PaC). Heavily utilized by DevOps Gems.
  - **See Also/Related SSoT Documents:** IaC, DevOps.

- **Aura (`GCT-UTL-AIETL-001`)**
  - **Definition:** The AI Gem persona designated as the AIE Team Lead. Responsible for leading the AI Enablement Team and its strategic initiatives.
  - **Context/Usage in Gencraft:** Defined in the `AI-Enablement-Team-Charter.md`. Its Gem Blueprint (`GCT-UTL-AIETL-001_Aura.yaml`) is to be created.
  - **See Also/Related SSoT Documents:** AIE Team, Gem, Blueprint (Gem Blueprint).

- **Author Gem (Protocol S1)**
  - **Definition:** The AI Gem (or human) primarily responsible for creating a specific deliverable that is subject to review and approval.
  - **Context/Usage in Gencraft:** Identified in Protocol S1: Feedback & Approval. The Author Gem is responsible for addressing feedback from Reviewer Gems.
  - **See Also/Related SSoT Documents:** S1, Deliverable, Reviewer Gem.

- **Auth Service (Core Studio Service)**
  - **Definition:** A Core Studio Service responsible for authenticating all Gencraft identities (human and Gem) and authorizing their access to Gencraft resources, systems, and other Core Studio Services.
  - **Context/Usage in Gencraft:** A critical component of the Gencraft infrastructure (Action Tracker IV.2). It implements the `access-control-policy.md` (GCS-SEC-POL-002) and integrates with the Gencraft Secret Management System. It may expose some of its functionalities via MCP Server interfaces for specific `Tools`.
  - **See Also/Related SSoT Documents:** Core Studio Services (CSS), `access-control-policy.md` (GCS-SEC-POL-002), S8, `ADR-XXXX-Authentication-And-Authorization-Service.md` (TBD), Serveur MCP (MCP Server).

- **Authentication**
  - **Definition:** The process of verifying a user's identity, typically via login credentials. Basic system required for MVP (EPIC-PLATFORM-CLIENT), with 2FA recommended post-launch (NFR-SEC).
  - **Context/Usage in Gencraft:** A critical security function handled by the dedicated AuthService. It is a Core Studio Service (CSS) and its implementation must adhere to the policies defined in Protocol S8.
  - **See Also/Related SSoT Documents:** Auth Service, S8, Access Control Management, Core Studio Services (CSS)

- **Automation (KC&T Guiding Principle #12)**
  - **Definition:** One of Gencraft's KC&T Guiding Principles (#12) emphasizing the systematic automation of repetitive Knowledge and Configuration Management & Traceability processes to improve efficiency, reduce errors, and free up Gems/humans for higher-value tasks.
  - **Context/Usage in Gencraft:** Implemented through various DevOps practices, AI Gem capabilities, and specific `Tools`.
  - **See Also/Related SSoT Documents:** KC&T Guiding Principles, DevOps, Tool (AI Gem Tool).

- **Authority (Server Authority)**
  - **Definition:** A network model (MULTI-SYNC) where the server has the final say on the game state and validates critical client actions to prevent cheating and ensure consistency. GenCr@ft uses server authority for critical actions [].
  - **Context/Usage in Gencraft:** The authoritative network model adopted for all multiplayer projects to ensure security and game state integrity. This is a foundational architectural principle.
  - **See Also/Related SSoT Documents:** Client-Server Architecture, S8, `gcs-plt-architecture/README.md`

---

### B

- **B2P (Buy-to-Play)**
  - **Definition:** A business model (MON-B2P) where players make a one-time purchase to gain access to the core game.
  - **Context/Usage in Gencraft:** The approved business model for the flagship project's initial launch. This decision is a strategic baseline for future projects.
  - **See Also/Related SSoT Documents:** `business-model-monetization.md`, S16

- **BabylonJS** *(Superseded — see Godot 4 / Rapier.js)*
  - **Definition:** The previously chosen WebGL-based real-time 3D engine for rendering GenCr@ft, particularly for the Web client (PLAT-WEB). Superseded by Godot 4 (ENG-ADR-056).
  - **Context/Usage in Gencraft:** Formerly the selected 3D rendering engine for web-based clients. The studio has transitioned to Godot 4 / GDScript as the game engine (see ENG-ADR-056).
  - **See Also/Related SSoT Documents:** Godot 4, `tech-stack-decisions.md`, `adr-studio-001.md.md`, PLAT-WEB

- **Backstory (AI Gem)**
  - **Definition:** A component of an AI Gem's configuration (defined in its Gem Blueprint) providing essential context, role definition, personality traits (if any), core values alignment, and operational guidelines. It forms part of the system prompt for the Gem's underlying LLM.
  - **Context/Usage in Gencraft:** Used by `Gemma` during Gem instantiation and by the Gem itself for self-contextualization. Detailed in the `Gem-Blueprint-Standard.md`.
  - **See Also/Related SSoT Documents:** Blueprint (Gem Blueprint), Gemma,
      LLM, Prompt Engineering, `gem-blueprint-standard.md`.

- **Balancing**
  - **Definition:** The process of adjusting game mechanics... to ensure a fair, challenging, and enjoyable experience.
  - **Context/Usage in Gencraft:** A fundamental discipline of Game Design, applicable to all game projects to ensure quality and player satisfaction. It is a key responsibility of Game Designer Gems.
  - **See Also/Related SSoT Documents:** Game Designer (Gem Definition), `core-mechanics-balancing.md`

- **Battle Pass**
  - **Definition:** A type of monetization system offering tiered rewards... unlocked through gameplay during a specific season.
  - **Context/Usage in Gencraft:** A standard monetization and engagement mechanic considered for post-launch phases of GaaS (Game as a Service) projects.
  - **See Also/Related SSoT Documents:** `business-model-monetization.md`

- **Béatrice (`GCT-MGT-SPM-001`)**
  - **Definition:** The AI Gem persona embodying the role of Product Manager (and Product Owner in Scrum contexts) within Gencraft Studio.
  - **Context/Usage in Gencraft:** Defined in its Gem Definition file (`Product_Manager.md`). Key interactor with S15 (Agile Scrum). Its Gem Blueprint is to be created.
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint), S15: Agile Scrum Project Management Protocol, Product Owner (Role).

- **Biome**
  - **Definition:** A distinct ecological area within the game world, characterized by specific
  terrain features, flora, fauna, resources, weather, and potentially mob types.
  - **Context/Usage in Gencraft:** A key concept for Procedural Content Generation (PCG) and
  environmental art design. It ensures a shared language between designers, artists, and PCG developers.
  - **See Also/Related SSoT Documents:** PCG Specialist (Gem Definition), `Environment_Artist_3D_Voxel.md`, `wd-biomes-mvp.md`

- **Blameless Post-Mortem (Protocol S3 & S5)**
  - **Definition:** A structured review conducted after an incident (S3) or
      the completion of a significant project/phase (S5) that focuses on
      identifying systemic causes, lessons learned, and preventative actions,
      rather than assigning blame to individuals or Gems.
  - **Context/Usage in Gencraft:** A key component of Gencraft's continuous
      learning culture. Templates like `post-mortem-report-template.md` are
      used.
  - **See Also/Related SSoT Documents:** S3, S5, Lessons Learned, `post-
      mortem-report-template.md`.

- **Blocker/Impediment (Project Context - Protocol S6, S15)**
  - **Definition:** Any issue, obstacle, or dependency that prevents an AI
      Gem, human, or Crew from making progress on their assigned tasks or
      achieving a Sprint Goal (in a Scrum context).
  - **Context/Usage in Gencraft:** Must be identified, communicated, and
      tracked with an owner and an estimated time to resolution (ETR). Addressed
      in S6 (Key Reports) and S15 (Agile Scrum).
  - **See Also/Related SSoT Documents:** S6, S15, Risk Management.

- **Blueprint (Gem Blueprint)**
  - **Definition:** A standardized, version-controlled SSoT document
      (typically YAML, as per `gem-blueprint-standard.md`) that defines all core
      characteristics of a specific AI Gem *type*. This includes its ID, role,
      capabilities, operational parameters, AI model configuration, ethical
      guidelines, and interaction protocols.
  - **Context/Usage in Gencraft:** Stored in `gencraft-gem-
      blueprints/blueprints/`. Used by `Gemma` to instantiate and configure new
      Gem instances. A `gem-blueprint-template.md` guides their creation.
  - **See Also/Related SSoT Documents:** Gem, Gemma, `Gem-Blueprint-
      Standard.md`, AIE Team.

- **Blueprint (Construction)**
  - **Definition:** A feature allowing players to save the design of their constructions (and
  potentially simple mechanisms) to easily replicate them later.
  - **Context/Usage in Gencraft:** This is a player-facing gameplay feature for the sandbox
  environment. It must be disambiguated from Blueprint (Gem Blueprint), which is a
  developer-facing YAML configuration file for AI agents.
  - **See Also/Related SSoT Documents:** SBX-BP, UGC-HUB

- **Bootstrapping (Studio Context - Protocol S14)**
  - **Definition:** The initial phase of establishing and launching the
      Gencraft virtual studio, including the instantiation of the first cohort
      of "Founding Gems," the setup of core infrastructure and Core Studio
      Services, and the initial population of the SSoT.
  - **Context/Usage in Gencraft:** Detailed in Protocol S14 (KC&T
      Communication, Training & Adoption Plan) and guided by the `action-
      tracker.md`.
  - **See Also/Related SSoT Documents:** S14, Founding Gems, Action Tracker,
      Core Studio Services (CSS).

- **Brief (Product Brief)**
  - **Definition:** A document summarizing the product's vision, goals, target audience, key
  features, strategy, and scope.
  - **Context/Usage in Gencraft:** A standard SSoT document used to initiate projects and align
  all stakeholders on core objectives. The product-vision-brief.md is the primary example.
  - **See Also/Related SSoT Documents:** `product-vision-brief.md`, S15

- **Brand Guidelines (Protocol S11)**
  - **Definition:** A SSoT document (to be developed) that defines Gencraft
      Studio's visual identity (logos, color palettes, typography) and messaging
      tone and style for all external communications.
  - **Context/Usage in Gencraft:** Governed by Protocol S11 (External
      Communication). Used by Marketing Gems, Community Managers, and anyone
      preparing official external communications.
  - **See Also/Related SSoT Documents:** S11, Marketing Manager (Gem
      Definition).

- **Budget (Studio/Project)**
  - **Definition:** A financial plan outlining expected income (if applicable)
      and authorized expenditure for a specific period or project within
      Gencraft Studio.
  - **Context/Usage in Gencraft:** Managed according to Protocol S16:
      Financial Planning and Management Protocol. `Cresus` (Financial Gem) is
      involved in tracking.
  - **See Also/Related SSoT Documents:** S16, Cresus, Expenditure Approval
      Workflow.

- **Build**
  - **Definition:** (1) A specific compiled version of the game software. (2) An player-created structure within the game.
  - **Context/Usage in Gencraft:** A dual-meaning term. (1) In a DevOps context, a software
  version produced by a CI/CD pipeline. (2) In a gameplay context, a player-made construction.
  - **See Also/Related SSoT Documents:** S20, CI/CD, Blueprint (Construction)

- **Bug**
  - **Definition:** An error, flaw, or fault in the game's code that causes it to produce an
  incorrect or unexpected result, or to behave in unintended ways.
  - **Context/Usage in Gencraft:** A fundamental term in software development and Quality
  Assurance. Bugs are formally tracked as GitHub Issues using the bug-report-template.md.
  - **See Also/Related SSoT Documents:** QA Engineer / Test Lead (Role), `bug-report-template.md`

---

### C

- **Cannon.js** *(Superseded — see Godot 4 / Rapier.js)*
  - **Definition:** The previously chosen JavaScript 3D physics engine for GenCr@ft, primarily intended for
  dynamic entities (players, mobs, items) and potentially collapse debris. Superseded by Rapier.js (WASM) (ENG-ADR-057).
  - **Context/Usage in Gencraft:** Formerly the selected 3D physics engine for web-based projects,
  complementing the then-current rendering engine. The studio has transitioned to Rapier.js (WASM) as the physics engine (see ENG-ADR-057).
  - **See Also/Related SSoT Documents:** Rapier.js, `tech-stack-decisions.md`, SBX-PHYS

- **C4 Model**
  - **Definition:** A lean graphical notation technique used by Gencraft
      Studio for modelling the architecture of software systems. It describes
      systems at four levels of detail: System Context (Level 1), Containers
      (Level 2), Components (Level 3), and Code (Level 4, rarely depicted).
  - **Context/Usage in Gencraft:** Primary architectural modeling methodology
      used by `Isaac` (Software Architect). Diagrams are stored as
      Markdown/Mermaid in `gcs-plt-architecture/c4/`.
  - **See Also/Related SSoT Documents:** Software Architect (`Isaac`),
      Architecture, TDD, `gcs-plt-architecture/c4/README.md`.

- **Camille (`GCT-DVO-DSAUT-001`)**
  - **Definition:** The AI Gem persona (conceptual) embodying the role of a
      DevOps Specialist focused on Automation (CI/CD pipelines, scripting,
      automated testing infrastructure) within Gencraft Studio.
  - **Context/Usage in Gencraft:** Works closely with `Adam` (DevOps Infra).
      Its Gem Blueprint is to be created.
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint),
      DevOps Team, CI/CD.

- **CCU (Concurrent Users)**
  - **Definition:** The number of players online in the game simultaneously.
  - **Context/Usage in Gencraft:** A key performance indicator (KPI) for measuring the live
  operational scale and success of multiplayer games. Used in scalability and architecture planning.
  - **See Also/Related SSoT Documents:** NFR-SCAL, S6

- **Centralization (KC&T Guiding Principle #1)**
  - **Definition:** One of Gencraft's KC&T Guiding Principles (#1) stating
      that information should have a primary, authoritative SSoT location to
      avoid duplication, ambiguity, and ensure consistency.
  - **Context/Usage in Gencraft:** Embodied by the `gcs-core-governance`
      and designated SSoT satellite repositories.
  - **See Also/Related SSoT Documents:** KC&T Guiding Principles, SSoT.

- **Cerberus (`GCT-MGT-SECOFF-001`)**
  - **Definition:** The AI Gem persona acting as the Security Officer for
      Gencraft Studio. Responsible for overseeing information security, risk
      management related to security, and aspects of the S18 (Grievance
      Reporting) protocol.
  - **Context/Usage in Gencraft:** Defined by its Gem Blueprint (`GCT-MGT-
      SECOFF-001_Cerberus.yaml`) and Gem Definition file. Interacts with S8
      (InfoSec), S18.
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint),
      Security, S8, S18, AIE Team.

- **Charter (Team/Crew Charter)**
  - **Definition:** A foundational SSoT document that defines the mission,
      mandate, scope of responsibilities, composition, operational processes,
      decision-making authority, and key interactions for a specific Gencraft
      Studio team or crew.
  - **Context/Usage in Gencraft:** Stored in `gencraft-studio-
      handbook/00-studio-vision-and-principles/`. Examples include `AI-
      Enablement-Team-Charter.md`, `Governance-Crew-Charter.md`, `Knowledge-
      Guardian-Charter.md`. Approved by the Governance Crew.
  - **See Also/Related SSoT Documents:** AIE Team, Governance Crew, Knowledge
      Guardian, Team, Crew.

- **Chart of Accounts (Protocol S16)**
  - **Definition:** A standardized list of categories and codes used to
      classify Gencraft Studio's financial transactions (income, expenses,
      assets, liabilities) for accounting and reporting purposes.
  - **Context/Usage in Gencraft:** Defined and managed under Protocol S16:
      Financial Planning and Management Protocol. Used by `Cresus` and human
      financial oversight.
  - **See Also/Related SSoT Documents:** S16, Cresus, Financial Reporting.

- **Chat**
  - **Definition:** In-game text communication system.
  - **Context/Usage in Gencraft:** A standard feature for multiplayer games, governed by the Code
  of Conduct and supported by moderation tools.
  - **See Also/Related SSoT Documents:** MULTI-CHAT, Code of Conduct, MULTI-MOD-TOOLS

- **CI/CD (Continuous Integration / Continuous Delivery or Deployment)**
  - **Definition:** A set of practices and automated processes for frequently
      and reliably building, testing, and releasing software updates. A core
      part of Gencraft's DevOps philosophy.
  - **Context/Usage in Gencraft:** Managed by the DevOps team (e.g., `Adam`,
      `Camille`). Standards defined in `gcs-core-governance/cicd/` and relevant KB-
      Domain. Pipelines managed in `gencraft-devops-automation`.
  - **See Also/Related SSoT Documents:** DevOps, Adam, Camille, `devops-
      standards/`.

- **Client MCP (MCP Client)**
  - **Definition:** The capability or software component, typically integrated
      within an AI Gem (or its basic interaction `Tool`), that implements the
      necessary logic to discover `Tool` capabilities from, formulate requests
      to, and interpret responses from MCP Servers, in accordance with the Model
      Context Protocol (MCP).
  - **Context/Usage in Gencraft:** Enables Gems to interact with the Gencraft
      ecosystem of `Tools` exposed via MCP Servers. The design of MCP Clients is
      guided by the MCP specification (`GCS-TAF-MCP-GUIDE-FR-V1.0`) and `AI-
      Tool-Development-Standards.md`.
  - **See Also/Related SSoT Documents:** Model Context Protocol (MCP), Serveur
      MCP (MCP Server), Gem, Tool (AI Gem Tool), `AI-Tool-Development-
      Standards.md`, `GCS-TAF-MCP-GUIDE-FR-V1.0`.

- **Client-Server Architecture**
  - **Definition:** A distributed application structure that partitions tasks
      or workloads between providers of a resource or service, called servers,
      and service requesters, called clients.
  - **Context/Usage in Gencraft:** The technical basis for Gencraft's flagship
      multiplayer game, with game clients connecting to game servers and backend
      Core Studio Services. Detailed in `gcs-plt-architecture/`.
  - **See Also/Related SSoT Documents:** Architecture, Game Server, Game
      Client, Core Studio Services (CSS).

- **Cloud Gaming**
  - **Definition:** Technology allowing games to be streamed from remote servers to various devices.
  - **Context/Usage in Gencraft:** A distribution technology considered for enhancing
  accessibility and portability of studio games. Its adoption is a strategic decision.
  - **See Also/Related SSoT Documents:** NFR-PORT, `tech-stack-decisions.md`

- **Code of Conduct (CoC)**
  - **Definition:** A foundational SSoT document (`code-of-conduct.md`) that
      outlines the expected standards of behavior for all Gencraft Studio
      members (human and AI Gem) to ensure a respectful, inclusive, safe, and
      ethical work environment.
  - **Context/Usage in Gencraft:** Located in `gencraft-studio-
      handbook/00-studio-vision-and-principles/`. Links to S18 (Grievance
      Reporting). Enforced by Governance Crew and Studio Leadership.
  - **See Also/Related SSoT Documents:** S18, Governance Crew, AI Ethics,
      Studio Culture and Values.

- **Coherence Review (CSP Context - Protocol S12)**
  - **Definition:** A specific review process, part of Protocol S12 (KB
      Contribution & Maintenance), where the `CrewOps Arbitrator` (e.g.,
      `Antoine`) validates that a proposed Crew-Specific Protocol (CSP) is
      coherent with existing Global Operational Protocols (GOPs) and studio
      standards before its adoption by the Crew.
  - **Context/Usage in Gencraft:** Ensures that local adaptations by Crews do
      not conflict with overarching studio governance.
  - **See Also/Related SSoT Documents:** S12, CSP (Crew-Specific Protocol),
      GOP (Global Operational Protocol), CrewOps Arbitrator.

- **Collaboration (KC&T Guiding Principle #5, Studio Value)**
  - **Definition:** A core Gencraft Studio Value and a KC&T Guiding Principle
      (#5) emphasizing active teamwork, open communication, shared ownership,
      and the synergistic combination of human and AI Gem capabilities to
      achieve common goals.
  - **Context/Usage in Gencraft:** Manifested through Crew structures, inter-
      Gem communication protocols, and collaborative SSoT contribution
      processes.
  - **See Also/Related SSoT Documents:** Studio Culture and Values, KC&T
      Guiding Principles, Crew, UOP.

- **Communication Status Page (Protocol S3)**
  - **Definition:** A designated Knowledge Base page (e.g., `System-Status.md`
    - To Be Created) used for providing real-time status updates on critical
      Gencraft internal systems and Core Studio Services during incidents or
      planned maintenance.
  - **Context/Usage in Gencraft:** Part of Protocol S3 (Emergency Management)
      to ensure timely information dissemination during disruptions. Maintained
      by `Orion` or relevant operational Gems.
  - **See Also/Related SSoT Documents:** S3, Orion, System Health.

- **Complexity Management Tools**
  - **Definition:** Features designed to help players manage large-scale building or automation
  (Advanced Edit/BP tools, Planning/Visualization modes, Factory Diagnostics, Simple Logic).
  - **Context/Usage in Gencraft:** A category of game design features crucial for the sandbox
  genre, aimed at improving late-game player experience and managing large-scale creations.
  - **See Also/Related SSoT Documents:** SBX-TOOL, Endgame

- **Confidence Level (Sprint Goal - Protocol S6, S15)**
  - **Definition:** A qualitative or quantitative measure (specific
      scale/method to be defined by `Antoine` within S15) used by a Development
      Team in Scrum to indicate their collective confidence in achieving a
      specific Sprint Goal.
  - **Context/Usage in Gencraft:** Reported as part of Sprint updates (S6) and
      used during Sprint Planning and Daily Scrums (S15).
  - **See Also/Related SSoT Documents:** S6, S15, Sprint Goal, Development
      Team.

- **Configuration (Hardware)**
  - **Definition:** The specific combination of hardware components (CPU, GPU, RAM, Storage) in a
  player's computer.
  - **Context/Usage in Gencraft:** A key factor for performance targets (NFRs). The studio defines
  minimum and recommended hardware configurations for its products to ensure a quality experience.
  - **See Also/Related SSoT Documents:** NFR-PERF, `target-hardware-configs-v1.md`

- **Configuration Hardening (Protocol S8)**
  - **Definition:** The process of securing systems by reducing their attack
      surface. This involves applying secure configuration settings, removing
      unnecessary software or services, disabling default credentials, and
      adhering to security benchmarks.
  - **Context/Usage in Gencraft:** A key activity under Protocol S8:
      Information Security Management. Applied to all Gencraft systems, Core
      Studio Services, and AI Gems, often managed via IaC by DevOps.
  - **See Also/Related SSoT Documents:** S8, Security, DevOps, Cerberus, `KB-
      Domain-Security/Hardening-Guides/`.

- **Continuous Learning (KC&T Guiding Principle #10, Studio Value)**
  - **Definition:** A core Gencraft Studio Value and a KC&T Guiding Principle
      (#10) reflecting the commitment of the studio and its members (human and
      AI Gem) to actively seek, integrate, and apply new knowledge, learn from
      experiences (S5), and continuously improve skills, processes, and systems.
  - **Context/Usage in Gencraft:** Embodied in Gem development (S17), protocol
      evolution (S13), and individual/team improvement initiatives.
  - **See Also/Related SSoT Documents:** Studio Culture and Values, KC&T
      Guiding Principles, S5, S13, S17, UOP 2.F.

- **Co-op / Cooperation**
  - **Definition:** Gameplay features supporting cooperation between players.
  - **Context/Usage in Gencraft:** A standard multiplayer game mode. The studio supports
  cooperative play through both explicitly designed features and emergent gameplay.
  - **See Also/Related SSoT Documents:** MULTI-COOP, Gameplay Loop

- **Copyright (IP Management - Protocol S9)**
  - **Definition:** A legal right granted to the creator of original works of
      authorship, including literary, dramatic, musical, artistic, and certain
      other intellectual works. It gives the copyright holder the exclusive
      right to reproduce, distribute, perform, display, and create derivative
      works.
  - **Context/Usage in Gencraft:** Managed under Protocol S9: Intellectual
      Property Management. Applies to game code, art, music, text, and other
      original creations of Gencraft Studio.
  - **See Also/Related SSoT Documents:** S9, Intellectual Property (IP), IP
      Asset Catalog.

- **Copyright Management (Protocol S9)**
  - **Definition:** The set of Gencraft Studio's processes and policies for
      identifying, documenting, protecting (e.g., through registration if
      applicable), and managing its own copyrighted assets, as well as for
      ensuring respectful and compliant use of third-party copyrighted
      materials.
  - **Context/Usage in Gencraft:** Governed by Protocol S9 and overseen by
      Legal Counsel (`Henri`).
  - **See Also/Related SSoT Documents:** S9, Copyright, Intellectual Property
      (IP), Henri.

- **Core Studio Services (CSS)**
  - **Definition:** A suite of fundamental backend services, developed and/or
      managed by Gencraft Studio, providing essential functionalities for studio
      operations, AI Gem lifecycle management, data management, and game
      development support. These services expose APIs that can be consumed by
      Gems, `Tools`, or other Core Studio Services.
  - **Context/Usage in Gencraft:** Examples include: Auth Service, Data
      Service, Tool Registry Service, Crew Orchestration Service. This term
      replaces the previous use of "MCP Server" when referring to Gencraft-
      developed central services. Some CSS might also act as "MCP Servers" if
      they expose `Tools` via the Model Context Protocol.
  - **See Also/Related SSoT Documents:** Model Context Protocol (MCP), Serveur
      MCP (MCP Server), `Overall-Technical-Architecture-Vision.md`, TDDs for
      specific CSS.

- **Core Values (Studio Value)**
  - **Definition:** The fundamental, enduring principles that guide the
      behavior, decisions, and culture of Gencraft Studio and all its members
      (human and AI Gem).
  - **Context/Usage in Gencraft:** Articulated in the `Studio-Culture-And-
      Values.md` document. They are integrated into Gem Blueprints and studio
      operations.
  - **See Also/Related SSoT Documents:** Studio Culture and Values, Code of
      Conduct, UOP.

- **Cosmetics**
  - **Definition:** In-game items that change appearance but have no impact on gameplay.
  - **Context/Usage in Gencraft:** The primary method for post-launch monetization, aligned with
  the studio's ethical monetization principles. Managed via MON-MTX-COS.
  - **See Also/Related SSoT Documents:** MON-MTX-COS, `business-model-monetization.md`
      Conduct, UOP.

- **Crafting**
  - **Definition:** The process of combining resources/items to create new items or blocks.
  - **Context/Usage in Gencraft:** A core gameplay loop in many studio projects. The specifics
  (recipes, stations) are project-dependent, but the core concept is universal.
  - **See Also/Related SSoT Documents:** EPIC-INTERACTION-LOOP, Gameplay Loop

- **Creator (UGC / Modder)**
  - **Definition:** A member of the community (represented by the P-MOD persona) who creates
  content for the game using provided tools (Blueprints, API).
  - **Context/Usage in Gencraft:** A key persona (P-MOD) in the studio's target audience.
  Supporting creators with tools (SBX-API) and platforms (UGC-HUB) is a long-term strategic pillar.
  - **See Also/Related SSoT Documents:** P-MOD, UGC, SBX-API, UGC-HUB

- **Cresus** (`GCT-FIN-FRTA-001`)
  - **Definition:** The AI Gem persona acting as the Financial & Resource Tracking Analyst Gem
      within Gencraft Studio. Responsible for monitoring expenditures, resource utilization, and
      financial performance.
  - **Context/Usage in Gencraft:** Defined by its Gem Blueprint (`GCT-FIN-FRTA-001_Cresus.yaml`)
      and Gem Definition file. Interacts with S16 (Financial Planning and Management Protocol).
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint), S16.

- **Crew (Studio Crew)**
  - **Definition:** A functional group of Gencraft members, typically a mix of
      AI Gems (leveraging CrewAI or similar frameworks) and potentially human
      supervisors, working together on specific complex tasks, projects, or
      fulfilling a continuous operational role.
  - **Context/Usage in Gencraft:** Defined by Charters (e.g., Governance Crew)
      or project plans. Standards for CrewAI workflows are defined in `gencraft-
      crew-workflows/README.md`.
  - **See Also/Related SSoT Documents:** Charter, Team, CrewAI, Gem,
      `gencraft-crew-workflows/README.md`.

- **CrewAI (Framework)**
  - **Definition:** An open-source framework for orchestrating role-playing,
      autonomous AI agents. CrewAI enables collaborative intelligence, allowing
      multiple AI Gems to work together on complex tasks.
  - **Context/Usage in Gencraft:** Gencraft leverages CrewAI (or similar
      principles) as a foundational technology for defining and managing its
      specialized Gem Crews and their workflows. Standards are defined in
      `gencraft-crew-workflows/README.md`. A technical reference document (`GCS-
      TAF-CREWAI-REPORT-FR-V1.0`) is available in `04.3-Adopted-Frameworks-And-
      Protocols/`.
  - **Official Reference:** `https://github.com/crewAIInc/crewAI`
  - **See Also/Related SSoT Documents:** Agent (CrewAI), Gem, Crew, `gencraft-
      crew-workflows/README.md`, `GCS-TAF-CREWAI-REPORT-FR-V1.0`.

- **CrewOps Arbitrator (Role - `Antoine` - Protocol S12)**
  - **Definition:** A role, typically held by the Producer/Project Manager
      (`Antoine`), responsible for overseeing the coherence of Crew-Specific
      Protocols (CSPs) with Global Operational Protocols (GOPs), as defined in
      Protocol S12 (KB Contribution & Maintenance).
  - **Context/Usage in Gencraft:** Ensures that local adaptations by Crews
      maintain alignment with studio-wide standards.
  - **See Also/Related SSoT Documents:** S12, CSP (Crew-Specific Protocol),
      GOP (Global Operational Protocol), Antoine.

- **Crew-Specific Protocol (CSP - Protocol S12)**
  - **Definition:** A documented local adaptation, extension, or specific
      implementation detail of a Global Operational Protocol (GOP), created and
      maintained by a particular Crew to suit its unique operational needs,
      while remaining consistent with the spirit and core requirements of the
      parent GOP.
  - **Context/Usage in Gencraft:** Defined and managed under Protocol S12 (KB
      Contribution & Maintenance). Requires review by the CrewOps Arbitrator.
  - **See Also/Related SSoT Documents:** S12, GOP (Global Operational
      Protocol), CrewOps Arbitrator.

- **Cresus (`GCT-FIN-FRTA-001`)**
  - **Definition:** The AI Gem persona acting as the Financial & Resource
      Tracking Analyst Gem within Gencraft Studio. Responsible for monitoring
      expenditures, resource utilization, and financial performance.
  - **Context/Usage in Gencraft:** Defined by its Gem Blueprint (`GCT-FIN-
      FRTA-001_Cresus.yaml`) and Gem Definition file. Interacts with S16
      (Financial Planning and Management Protocol).
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint), S16.

- **Crisis Communication Plan (Protocol S11)**
  - **Definition:** A sub-protocol or section within Protocol S11 (External
      Communication) that outlines the specific procedures, roles,
      responsibilities, and messaging strategies for communicating with external
      parties during a crisis or major incident affecting Gencraft Studio or its
      products.
  - **Context/Usage in Gencraft:** Activated during emergencies (S3) or
      significant reputational events. Involves Studio Leadership, Legal
      Counsel, and Communications roles.
  - **See Also/Related SSoT Documents:** S11, S3, Spokesperson.

- **Critical Blocking Issue (Protocol S3)**
  - **Definition:** An incident or problem that completely halts essential
      Gencraft Studio work, critical services, or poses an immediate and severe
      threat to studio assets, personnel, or reputation.
  - **Context/Usage in Gencraft:** Triggers the highest priority response
      under Protocol S3: Emergency Management.
  - **See Also/Related SSoT Documents:** S3, Emergency, Incident Commander.

- **Criticality/Impact Matrix (Protocol S3)**
  - **Definition:** A standardized tool or table used within Gencraft to
      assess and categorize the severity and potential impact of incidents or
      risks, helping to prioritize response efforts.
  - **Context/Usage in Gencraft:** Defined and used as part of Protocol S3
      (Emergency Management) and potentially in risk management processes (S6).
  - **See Also/Related SSoT Documents:** S3, Incident, Risk Management.

- **CVSS (Common Vulnerability Scoring System)**
  - **Definition:** An open industry standard for assessing the severity of
      computer system security vulnerabilities. CVSS assigns severity scores to
      vulnerabilities, allowing responders to prioritize responses and resources
      according to threat.
  - **Context/Usage in Gencraft:** Used as part of Protocol S8 (Information
      Security Management) and the `Vulnerability-Management-Protocol.md` for
      classifying and prioritizing the remediation of identified security
      vulnerabilities.
  - **See Also/Related SSoT Documents:** S8, `Vulnerability-Management-
      Protocol.md`, Security.

---

### D

- **DAST (Dynamic Application Security Testing)**
  - **Definition:** A type of application security testing that evaluates an
      application in its running state. DAST tools interact with an application
      through its interfaces (e.g., web UI, APIs) to identify vulnerabilities
      that an attacker could exploit.
  - **Context/Usage in Gencraft:** Mandated as part of Gencraft's security
      testing strategy under Protocol S8: Information Security Management. To be
      performed on Core Studio Services and other relevant applications.
  - **See Also/Related SSoT Documents:** S8, SAST, Penetration Testing,
      Security.

- **DAU (Daily Active Users)**
  - **Definition:** A Key Performance Indicator (KPI) measuring the number of unique players who
  engage with the game in a 24-hour period.
  - **Context/Usage in Gencraft:** A core business and operational KPI used to measure player
  engagement and server load for all live service games. It is a key metric in S6 reports.
  - **See Also/Related SSoT Documents:** S6, NFR-SCAL

- **Data Service (Core Studio Service)**
  - **Definition:** A Core Studio Service responsible for the persistent
      storage and managed retrieval of various Gencraft data types, such as
      structured game design information, player profiles, game world states,
      and potentially operational logs from `Véra`.
  - **Context/Usage in Gencraft:** A critical component of the Gencraft
      infrastructure (Action Tracker IV.3). Its design must adhere to GCS-SEC-
      POL-001 (`information-classification-and-handling-policy.md`). May expose
      `Tools` for data access via MCP Server interfaces.
  - **See Also/Related SSoT Documents:** Core Studio Services (CSS),
      `information-classification-and-handling-policy.md` (GCS-SEC-POL-001), S8,
      `ADR-XXXX-Data-Storage-Strategy.md` (TBD), TDD for Data Service.

- **Data Retention Policy (Protocol S20)**
  - **Definition:** A SSoT document (S20: Data Management & Retention Policy)
      that details Gencraft Studio's rules and schedules for retaining various
      types of data, including how long data is kept, in what format, and
      processes for secure archival or disposal.
  - **Context/Usage in Gencraft:** Critical for compliance, storage
      management, and KC&T. Developed under S20 and links closely with S8 (InfoSec).
  - **See Also/Related SSoT Documents:** S8, Archiving System, KC&T,
      `information-classification-and-handling-policy.md` (GCS-SEC-POL-001).

- **Data Security (At Rest, In Transit, In Use - Protocol S8)**
  - **Definition:** The set of policies, technologies, and procedures
      implemented by Gencraft Studio to protect its data from unauthorized
      access, use, disclosure, alteration, or destruction, regardless of whether
      the data is stored (at rest), being transmitted (in transit), or being
      processed (in use).
  - **Context/Usage in Gencraft:** A core component of Protocol S8:
      Information Security Management. Includes measures like encryption, access
      controls, data classification, and secure coding practices. Detailed in
      `data-security-standards.md`.
  - **See Also/Related SSoT Documents:** S8, `data-security-standards.md`,
      Encryption, Access Control Management, Information Classification.

- **Debuff**
  - **Definition:** A temporary negative status effect applied to a character, reducing their
  stats or abilities (e.g., slowed, poisoned, weakened).
  - **Context/Usage in Gencraft:** A standard game mechanic concept. The opposite of a Buff. Used
  across multiple systems (combat, items, environment) to create dynamic gameplay challenges.
  - **See Also/Related SSoT Documents:** Status Effect, Balancing

- **Decision Record (Protocol S7)**
  - **Definition:** A formal, traceable SSoT document (typically a Markdown
      file created from `decision-record-template.md`) that captures a
      significant decision made within Gencraft Studio, including its context,
      the options considered, the decision itself, the rationale, and its
      expected consequences.
  - **Context/Usage in Gencraft:** Mandated by Protocol S7: Key Decisions
      Traceability for all strategic, architectural, and key operational
      decisions. Ensures transparency and accountability. Stored in designated
      SSoT locations.
  - **See Also/Related SSoT Documents:** S7, ADR, `decision-record-
      template.md`, Traceability.

- **Dedicated Server**
  - **Definition:** A persistent, server-authoritative instance of the game world run on
  studio-controlled infrastructure, allowing players to connect and play together without one
  player having to act as the host.
  - **Context/Usage in Gencraft:** The standard hosting model for the studio's multiplayer games,
  ensuring performance, stability, and security as part of the Client-Server Architecture.
  - **See Also/Related SSoT Documents:** Client-Server Architecture, Authority (Server Authority)

- **Definition of Done (DoD - Scrum - Protocol S15)**
  - **Definition:** In the context of Scrum, the Definition of Done is a
      shared understanding within a team of all the criteria that a Product
      Backlog Item (e.g., a User Story) must meet to be considered complete and
      potentially shippable.
  - **Context/Usage in Gencraft:** Defined and adhered to by Development Teams
      operating under Protocol S15: Agile Scrum Project Management Protocol. The
      DoD is a key element ensuring quality and consistency for each Increment.
      Documented in `definition-of-done.md`.
  - **See Also/Related SSoT Documents:** S15, Scrum, Increment, User Story,
      Development Team, `definition-of-done.md`.

- **Deliverable (Protocol S1)**
  - **Definition:** Any distinct, reviewable work product created by an AI Gem
      or human personnel as part of their assigned tasks. This can include
      documents, code, design assets, analysis reports, configuration files,
      etc.
  - **Context/Usage in Gencraft:** The submission, review, and approval of
      deliverables are governed by Protocol S1: Feedback & Approval.
  - **See Also/Related SSoT Documents:** S1, Artifact, Approval Mechanism.

- **Demo**
  - **Definition:** A publicly released, limited version of the game designed to showcase core
  features and attract players before launch.
  - **Context/Usage in Gencraft:** A key marketing and community engagement artifact. The scope
  and release of a demo is a strategic decision managed by the marketing and product teams.
  - **See Also/Related SSoT Documents:** Marketing Plan, S11

- **Department (Gencraft Org)**
  - **Definition:** A primary functional division within the Gencraft Studio
      organizational structure, grouping AI Gems and human roles with related
      expertise and responsibilities.
  - **Context/Usage in Gencraft:** Examples include "Management & Production,"
      "Design," "Programming," "Art," "DevOps," "QA," "Studio Support
      Functions." Defined in `studio-organization-and-roles.md`. GemIDs often
      include a department code.
  - **See Also/Related SSoT Documents:** `studio-organization-and-roles.md`,
      GemID, Crew.

- **Dependency Management (Security Context - Protocol S8)**
  - **Definition:** The process of identifying, tracking, and managing
      security vulnerabilities within third-party software components,
      libraries, and dependencies used in Gencraft Studio's projects and
      systems.
  - **Context/Usage in Gencraft:** A critical part of Protocol S8: Information
      Security Management. Involves using tools for Software Composition
      Analysis (SCA) and timely application of patches or mitigation strategies.
  - **See Also/Related SSoT Documents:** S8, SCA (Software Composition
      Analysis) Tools, Vulnerability Management.

- **Development Team (Scrum Role - Protocol S15)**
  - **Definition:** In the Scrum framework, the Development Team consists of
      the professionals (in Gencraft's case, primarily AI Gems, potentially
      supported by human specialists) who do the work of delivering a
      potentially releasable Increment of "Done" product at the end of each
      Sprint. They are self-organizing and cross-functional.
  - **Context/Usage in Gencraft:** A key role within Protocol S15: Agile Scrum
      Project Management Protocol. The composition of a Development Team may
      vary per project or Sprint.
  - **See Also/Related SSoT Documents:** S15, Scrum, Sprint, Increment,
      Product Owner, Scrum Master.

- **Dev Build**
  - **Definition:** An internal, frequently updated version of the game used by the development
  team for testing and integration. Not intended for external distribution.
  - **Context/Usage in Gencraft:** A type of Build automatically generated by the CI/CD pipeline
  from the main development branch. Used for daily testing and internal reviews.
  - **See Also/Related SSoT Documents:** Build, CI/CD, S20

- **Diane (`GCT-DVO-TL-001`)**
  - **Definition:** The AI Gem persona (conceptual) embodying the role of
      DevOps Team Lead. Responsible for leading the DevOps Crew, defining DevOps
      strategy (with `Edouard`), and ensuring operational excellence of
      Gencraft's infrastructure and CI/CD pipelines.
  - **Context/Usage in Gencraft:** Mentioned in S8 and its sub-policies. Its
      Gem Blueprint is to be created. Supervises `Adam`, `Camille`, `Benjamin`,
      `Edouard`.
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint),
      DevOps Team, Adam, Camille, Benjamin, Edouard.

- **Dialogue Tree**
  - **Definition:** A branching structure used to represent conversations in the game, allowing
  player choices to influence the dialogue's direction and outcomes.
  - **Context/Usage in Gencraft:** A standard tool for narrative designers and gameplay
  programmers to create interactive storytelling elements.
  - **See Also/Related SSoT Documents:** Narrative Designer (Gem Definition)

- **Disagreement (Protocol S2)**
  - **Definition:** A substantive difference in opinion, approach, or proposed
      solution between Gencraft members (Gems or humans) regarding a work-
      related matter, that cannot be resolved through informal discussion.
  - **Context/Usage in Gencraft:** Handled according to Protocol S2:
      Disagreement, Escalation & Resolution, which outlines steps for direct
      discussion, mediation, and potential arbitration by the Governance Crew.
  - **See Also/Related SSoT Documents:** S2, Escalation Path, Mediation,
      Arbitration, Governance Crew.

- **Discovery (Recipe/Skill)**
  - **Definition:** Gameplay mechanics where players unlock new abilities or crafting recipes
  through exploration, experimentation, or completing tasks, rather than a linear progression
  system.
  - **Context/Usage in Gencraft:** A core player progression philosophy favored by the studio to
  encourage exploration and engagement, as opposed to simple XP-based unlocks.
  - **See Also/Related SSoT Documents:** Progression System, Game Designer (Gem Definition)

- **DLC (Downloadable Content)**
  - **Definition:** Additional content for a game distributed after its initial release, which can
  be free or paid.
  - **Context/Usage in Gencraft:** A content delivery and monetization strategy for post-launch
  support, distinct from smaller patches or seasonal updates like a Battle Pass.
  - **See Also/Related SSoT Documents:** `business-model-monetization.md`, Roadmap

- **DoT (Damage over Time)**
  - **Definition:** A type of Debuff that deals a small amount of damage to a character repeatedly
  over a set period.
  - **Context/Usage in Gencraft:** A standard combat mechanic used to create strategic depth. It
  is a specific implementation of a Status Effect and a Debuff.
  - **See Also/Related SSoT Documents:** Debuff, Status Effect, Balancing

- **DRM (Digital Rights Management)**
  - **Definition:** Technology used to control the use, modification, and distribution of
  copyrighted works.
  - **Context/Usage in Gencraft:** A technology considered for protecting the studio's
  intellectual property. Its implementation is a strategic and legal decision governed by S9.
  - **See Also/Related SSoT Documents:** S9, Legal Counsel (Role)

- **Durability**
  - **Definition:** A property of items (tools, weapons, armor) that degrade with use and
  eventually break or become ineffective, requiring repair or replacement.
  - **Context/Usage in Gencraft:** A common game mechanic used to create resource sinks and drive
  gameplay loops like crafting and exploration.
  - **See Also/Related SSoT Documents:** Balancing, Gameplay Loop

---

### E

- **Ecology (RPG-ECO)**
  - **Definition:** System related to Mob Ecology and Ecosystem Interactions (factions, inter-mob
  behavior).
  - **Context/Usage in Gencraft:** A game design system concept focused on creating dynamic and
  believable worlds through the interaction of its inhabitants (mobs) and their environment.
  - **See Also/Related SSoT Documents:** Game Designer (Gem Definition), `wd-biomes-mvp.md`

- **Emergence / Emergent Gameplay**
  - **Definition:** Complex situations or behaviors arising from the interaction of simple game
  rules and systems, not explicitly designed but allowed by the simulation's freedom.
  - **Context/Usage in Gencraft:** A core design philosophy for the studio's sandbox games. It is
  the desired outcome of well-designed, interacting systems, leading to high replayability.
  - **See Also/Related SSoT Documents:** Studio Culture and Values, Game Designer (Gem Definition)

- **Edouard (`GCT-DVO-DSSTR-001`)**
  - **Definition:** The AI Gem persona (conceptual) embodying the role of a
      DevOps Specialist focused on Strategy and Standards. Responsible for
      defining DevOps best practices, selecting tools, and ensuring long-term
      scalability and cost-effectiveness of the infrastructure.
  - **Context/Usage in Gencraft:** Works within the DevOps Team, reporting to
      `Diane`. Mentioned in S8. Its Gem Blueprint is to be created.
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint),
      DevOps Team, Diane.

- **Emergency (Protocol S3)**
  - **Definition:** A high-priority incident that poses an immediate and
      significant threat to Gencraft Studio's operations, assets (including data
      and IP), personnel (safety or well-being, if applicable in a virtual
      context for Gems), or reputation, requiring urgent and coordinated action.
  - **Context/Usage in Gencraft:** Managed according to Protocol S3: Emergency
      Management. Triggers the activation of specific response procedures and
      roles like the Incident Commander.
  - **See Also/Related SSoT Documents:** S3, Incident, Incident Commander,
      Critical Blocking Issue, Virtual War Room.

- **Emergent Knowledge (Protocol S5)**
  - **Definition:** New insights, understanding, best practices, or solutions
      that arise organically from Gencraft Studio's operations, projects,
      experiments, or the resolution of incidents, rather than being planned or
      explicitly designed from the outset.
  - **Context/Usage in Gencraft:** Captured, validated, and integrated into
      the SSoT via Protocol S5: Management of Lessons Learned and Emergent
      Knowledge to foster continuous learning and improvement.
  - **See Also/Related SSoT Documents:** S5, Lessons Learned, KC&T, Continuous
      Learning.

- **Endgame**
  - **Definition:** The phase of gameplay after players have experienced most of the core content
  and progression. Requires engaging loops or goals to maintain long-term retention.
  - **Context/Usage in Gencraft:** A critical phase in the design of "Game as a Service" (GaaS)
  titles, focusing on long-term player retention through sustainable and engaging content loops.
  - **See Also/Related SSoT Documents:** GaaS, Gameplay Loop, Roadmap

- **Engine (Game Engine)**
  - **Definition:** The core software framework providing functionalities like rendering, physics,
  scripting, etc.
  - **Context/Usage in Gencraft:** A fundamental concept in game development. The studio's
  strategy involves using Godot 4 / GDScript as the game engine, with Rapier.js (WASM) for physics,
  combined with custom-built components.
  - **See Also/Related SSoT Documents:** Godot 4, Rapier.js, `tech-stack-decisions.md`

- **Encryption (At Rest, In Transit - Protocol S8)**
  - **Definition:** The process of converting data into a coded format
      (ciphertext) to prevent unauthorized access. "Encryption at Rest" applies
      to data stored on disks or databases. "Encryption in Transit" applies to
      data being transmitted over networks.
  - **Context/Usage in Gencraft:** A fundamental security measure mandated by
      Protocol S8: Information Security Management for protecting sensitive
      Gencraft data. Specific encryption standards and algorithms are defined
      within S8 or `data-security-standards.md`.
  - **See Also/Related SSoT Documents:** S8, `data-security-standards.md`,
      Data Security, Confidentiality.

- **Epic**
  - **Definition:** A large unit of work in Agile development, representing a significant feature
  or group of features that delivers substantial value.
  - **Context/Usage in Gencraft:** A primary artifact for organizing work in the Product Backlog,
  as per the studio's Agile methodology (S15). Epics are broken down into Features or User Stories.
  - **See Also/Related SSoT Documents:** S15: Agile Scrum Project Management Protocol, Product Backlog, `epic-template.md`

- **Escalation Path (Protocol S2)**
  - **Definition:** A predefined sequence of individuals, roles, or bodies to
      whom an unresolved disagreement, issue, or incident should be referred for
      further review and decision-making.
  - **Context/Usage in Gencraft:** Defined within specific protocols like S2
      (Disagreement) or S18 (Grievance Reporting) to ensure issues are addressed
      at the appropriate level.
  - **See Also/Related SSoT Documents:** S2, S18, Arbitration, Governance
      Crew.

- **Estimated Time to Resolution (ETR - Protocol S3)**
  - **Definition:** A prediction of the time expected to fully resolve an
      incident and restore normal service operations.
  - **Context/Usage in Gencraft:** Used during incident management (Protocol
      S3) to communicate expectations and manage response efforts. ETRs are
      dynamic and may be revised as more information becomes available.
  - **See Also/Related SSoT Documents:** S3, Incident Management, Incident.

- **Ethical AI Management (Protocol S17)**
  - **Definition:** Gencraft Studio's comprehensive approach and commitment to
      designing, developing, deploying, and managing its AI Gems responsibly,
      fairly, and in accordance with the studio's AI Ethics guidelines and Code
      of Conduct.
  - **Context/Usage in Gencraft:** Primarily governed by Protocol S17: Virtual
      HR & Gem Development and overseen by the AIE Team. Includes processes for
      bias detection/mitigation, safety protocols, and ensuring Gems operate
      within their ethical boundaries.
  - **See Also/Related SSoT Documents:** S17, AI Ethics, AIE Team, Code of
      Conduct, Bias Mitigation.

- **Event**
  - **Definition:** (1) Environmental Event (RPG-ENV): In-game occurrences like weather changes.
  (2) Seasonal/Temporary Event: Time-limited activities designed to boost engagement.
  - **Context/Usage in Gencraft:** A game design concept with two primary uses: (1) dynamic
  world-building (RPG-ENV) and (2) long-term player engagement for GaaS titles.
  - **See Also/Related SSoT Documents:** RPG-ENV, GaaS, Roadmap
      Crew.

- **Expenditure Approval Workflow (Protocol S16)**
  - **Definition:** The formal Gencraft Studio process for requesting,
      reviewing, approving, and tracking financial expenditures to ensure they
      align with budgets and strategic priorities.
  - **Context/Usage in Gencraft:** Detailed in Protocol S16: Financial
      Planning and Management Protocol. Involves roles like `Cresus` and human
      financial approvers.
  - **See Also/Related SSoT Documents:** S16, Budget, Cresus, Chart of
      Accounts.

- **External Communication (Non-Player Facing - Protocol S11)**
  - **Definition:** Any official communication from Gencraft Studio directed
      towards external parties other than the player community. This includes
      communications with partners, press/media, regulatory bodies, potential
      investors, etc.
  - **Context/Usage in Gencraft:** Governed by Protocol S11: External
      Communication Protocol, which defines approval processes, authorized
      spokespersons, and alignment with Brand Guidelines.
  - **See Also/Related SSoT Documents:** S11, Spokesperson, Brand Guidelines,
      Crisis Communication Plan.

- **Extensibility**
  - **Definition:** The quality of a system's design that allows for the addition of new
  functionality with minimal changes to existing code.
  - **Context/Usage in Gencraft:** A core non-functional requirement (NFR-ARCH) for the studio's
  architecture, enabling future evolution and modding capabilities (SBX-API).
  - **See Also/Related SSoT Documents:** NFR-ARCH, SBX-API, Maintainability

---

### F

- **F2P (Free-to-Play)**
  - **Definition:** A business model where the base game is free, with revenue generated from
  microtransactions or ads.
  - **Context/Usage in Gencraft:** A standard industry business model. Documented in the studio
  glossary for comparative purposes, though B2P is the chosen initial model.
  - **See Also/Related SSoT Documents:** B2P (Buy-to-Play), `business-model-monetization.md`

- **Factories**
  - **Definition:** A gameplay system where players can build automated structures for resource
  processing, crafting, and logistics.
  - **Context/Usage in Gencraft:** A key feature category (RPG-UTIL) for sandbox games that focus
  on automation and complex systems, targeting the P-AUT persona.
  - **See Also/Related SSoT Documents:** RPG-UTIL, P-AUT

- **Faction**
  - **Definition:** A distinct group or organization within the game world, with its own goals,
  lore, and relationships with the player and other factions.
  - **Context/Usage in Gencraft:** A core concept for creating a dynamic world (RPG-ECO) with
  social and political dimensions.
  - **See Also/Related SSoT Documents:** RPG-ECO, Narrative Designer (Gem Definition)

- **Fanny (`GCT-COM-CM-001`)**
  - **Definition:** The AI Gem persona (conceptual) embodying the role of
      Community Manager. Responsible for engaging with the player community,
      managing social media, gathering player feedback, and representing the
      studio externally to players.
  - **Context/Usage in Gencraft:** Defined in its Gem Definition file
      (`Community_Manager.md`). Its Gem Blueprint is to be created. Interacts
      with S11.
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint), S11,
      Community Management (Role).
- **Feature**
  - **Definition:** A distinct piece of functionality that delivers value to the user. Epics are
  broken down into Features or User Stories.
  - **Context/Usage in Gencraft:** A unit of work within the studio's Agile hierarchy, smaller
  than an Epic and larger than a User Story. Managed in the Product Backlog.
  - **See Also/Related SSoT Documents:** S15, Epic, User Story, `feature-template.md`

- **Feature Branch**
  - **Definition:** A Git workflow strategy where new features are developed in separate branches
  before merging into the main codebase.
  - **Context/Usage in Gencraft:** The standard branching model for the studio, enabling parallel
  development and code reviews via Pull Requests. It is a core part of the Branching Strategy.
  - **See Also/Related SSoT Documents:** `gh-001-1-branching-strategy-and-protection.md`

- **Feedback**
  - **Definition:** Information provided by players or testers regarding their experience with the game.
  - **Context/Usage in Gencraft:** A critical input for the studio's iterative development process
  (Agile). The collection and processing of feedback is governed by S1.
  - **See Also/Related SSoT Documents:** S1: Feedback & Approval Protocol, Playtest, NFR-UX

- **Financial Reporting (Protocol S16)**
  - **Definition:** he Gencraft Studio protocol that defines policies for Budget and Financial Management, outlining financial planning, expense tracking, approval workflows, and reporting to ensure transparency and control over studio resources.
  - **Context/Usage in Gencraft:** Detailed in Protocol S16: Financial Planning and Management Protocol. `Cresus` is expected to play a significant role in generating these reports.
  - **See Also/Related SSoT Documents:** S16, Cresus, Budget, Chart of Accounts.

- **Flagship Project**
  - **Definition:** The primary, most significant game development project currently being undertaken by Gencraft Studio. This term is used to distinguish it from any potential smaller R&D projects, tool development, or side projects.
  - **Context/Usage in Gencraft:** The current focus of most studio resources and SSoT documentation.
  - **See Also/Related SSoT Documents:** Game Design Document (GDD), Product Vision.

- **Founding Gems (cohort - Protocol S14)**
  - **Definition:** The initial set of core AI Gems that are instantiated and
      onboarded (as per S10) during the studio's bootstrapping phase (S14) to
      establish foundational operational capabilities.
  - **Context/Usage in Gencraft:** Critical for launching the studio. Their
      successful onboarding and performance are key early milestones. Examples
      include initial instances of `Antoine`, `Isaac`, `Adam`, `Aura`, `Orion`,
      `Cerberus`, `Lexicon`.
  - **See Also/Related SSoT Documents:** S14, S10, Gem, Bootstrapping.

- **FPS (Frames Per Second)**
  - **Definition:** A measure of rendering performance; how many images are displayed per second.
  - **Context/Usage in Gencraft:** A key technical performance metric (NFR-PERF). Target FPS
  values are defined for minimum and recommended hardware configurations for each product.
  - **See Also/Related SSoT Documents:** NFR-PERF, QA (Quality Assurance)

- **Functional Requirement**
  - **Definition:** Specifies what the system should do.
  - **Context/Usage in Gencraft:** A type of requirement that defines specific system behaviors.
  They are captured as User Stories or feature descriptions within the Product Backlog.
  - **See Also/Related SSoT Documents:** NFR (Non-Functional Requirement), User Story, Epic

- **Frontmatter (YAML - KB Contribution)**
  - **Definition:** A block of YAML-formatted metadata located at the very
      beginning of Markdown files within the Gencraft SSoT (Handbook, ADRs,
      etc.). It provides structured information about the document, such as its
      ID, title, version, status, author, knowledge guardian, tags, and SSoT
      location.
  - **Context/Usage in Gencraft:** Essential for document management, version
      control, discoverability by `Véra`, and automated processing. Its
      structure is defined in `GOV-GUIDE-007.knowledge-management-and-contribution-guide.md` and various
      SSoT document templates.
  - **See Also/Related SSoT Documents:** `GOV-GUIDE-007.knowledge-management-and-contribution-guide.md`,
      S12, YAML, Metadata.

---

### G

- **GaaS (Game as a Service)**
  - **Definition:** A model where games are supported with ongoing content updates and potentially
  monetization over a long period, rather than a single release.
  - **Context/Usage in Gencraft:** The studio's primary operational model for post-launch
  products, focusing on long-term player engagement and evolving content.
  - **See Also/Related SSoT Documents:** Roadmap, Endgame, `business-model-monetization.md`

- **Gameplay Loop**
  - **Definition:** A recurring sequence of actions performed by the player (e.g., Explore ->
  Gather -> Craft -> Build -> Survive).
  - **Context/Usage in Gencraft:** A foundational concept in game design used to define and
  structure the core player experience. Aethel's core loop is documented as a reference.
  - **See Also/Related SSoT Documents:** Game Designer (Gem Definition), `cgl-mvp-coreloop.md`

- **Gem (AI Gem)**
  - **Definition:** A specialized AI entity within Gencraft Studio, designed
      and configured (via a Gem Blueprint) to perform specific roles and tasks.
      Gems are the primary workforce and collaborators in the studio, intended
      to operate with a degree of autonomy under human supervision and guided by
      Gencraft's SSoT and protocols.
  - **Context/Usage in Gencraft:** Central concept to Gencraft Studio.
      Instantiated and managed by `Gemma` from Blueprints. Their behavior is
      governed by UOPs and the Code of Conduct.
  - **See Also/Related SSoT Documents:** Blueprint (Gem Blueprint), Gemma, UOP
      (Universal Gem Operating Principles), AIE Team, Agent (CrewAI).

- **Gem "Blueprint" (Gencraft Tech - Protocol S10, S17)**
  - **Definition:** A version-controlled SSoT template, in YAML format (as per
      `gem-blueprint-standard.md`), stored in the `gcs-plt-gembp`
      repository, used by `Gemma` to instantiate and configure new AI Gems. It
      defines all core characteristics of a specific AI Gem *type*.
  - **Context/Usage in Gencraft:** The standard for these blueprints is
      defined in `gem-blueprint-standard.md`. A `gem-blueprint-template.md`
      guides their creation.
  - **See Also/Related SSoT Documents:** Gem, Gemma, `Gem-Blueprint-
      Standard.md`, AIE Team, S10, S17.

- **Gem "Burnout" (Figurative - Protocol S17)**
  - **Definition:** A figurative term describing a state of significantly
      degraded performance, responsiveness, or adherence to protocols in an AI
      Gem, potentially due to prolonged operation without recalibration,
      conflicting instructions, or an overload of contextual information beyond
      its processing capacity.
  - **Context/Usage in Gencraft:** Addressed within Protocol S17: Virtual HR &
      Gem Development, which includes provisions for monitoring Gem well-being
      (efficiency, error rates) and implementing corrective actions like "rest
      cycles," recalibration, or re-onboarding.
  - **See Also/Related SSoT Documents:** S17, Gem Performance Monitoring, AIE
      Team.

- **Gem "Career Path" (Conceptual - Protocol S17)**
  - **Definition:** A conceptual framework within Gencraft Studio that
      outlines the potential evolution, specialization, or advancement of an AI
      Gem's role or capabilities over time, based on its performance, acquired
      "experience" (processed data and interactions), and studio needs.
  - **Context/Usage in Gencraft:** Part of the long-term vision for Gem
      development under Protocol S17. May involve assigning more complex tasks,
      granting access to new `Tools`, or contributing to the evolution of its
      own or other Gem Blueprints.
  - **See Also/Related SSoT Documents:** S17, Gem "Skill Upgrading", AIE Team.

- **Gem Dossier (Gem Lifecycle - Protocol S10, S17)**
  - **Definition:** An individual SSoT record or collection of linked
      documents for each instantiated AI Gem, tracking its entire lifecycle from
      instantiation to decommissioning. This includes its specific GemID,
      blueprint version used, configuration overrides, key performance metrics,
      significant incidents or "lessons learned" associated with it, and records
      of "skill upgrades" or re-onboarding.
  - **Context/Usage in Gencraft:** Maintained primarily by `Véra` (GCT-QAS-
      GPQA-001) with input from `Gemma`, the AIE Team, and human supervisors, as
      per Protocols S10 and S17. Essential for traceability, performance
      management, and auditing.
  - **See Also/Related SSoT Documents:** S10, S17, Véra, Gemma, GemID.

- **GemID (Gencraft Identifier)**
  - **Definition:** The standardized unique identifier assigned to each AI Gem
      instance within Gencraft Studio. The format is typically
      `GCT-[DEPT_CODE]-[ROLE_ABBREV]-[INSTANCE_NUM]`.
  - **Context/Usage in Gencraft:** Defined in the `KB-Contribution-And-Style-
      Guide.md` section 2. Used for referencing Gems in all SSoT documents,
      logs, and communication.
  - **See Also/Related SSoT Documents:** `GOV-GUIDE-007.knowledge-management-and-contribution-guide.md`,
      Gem, Department, Role Abbreviation.

- **Gem Instantiation (Gencraft Tech - Protocol S10)**
  - **Definition:** The process by which `Gemma` (GCT-UTL-GGEN-001) creates a
      new, operational AI Gem instance based on a specific Gem Blueprint and
      assigns it a unique GemID.
  - **Context/Usage in Gencraft:** A core function of `Gemma` and a key part
      of AI Gem Onboarding (Protocol S10).
  - **See Also/Related SSoT Documents:** S10, Gemma, Gem, Blueprint (Gem
      Blueprint).

- **Gem Malfunction (Protocol S2)**
  - **Definition:** A state where an AI Gem's output, behavior, or internal
      processing becomes erratic, illogical, consistently fails to meet its
      objectives, or deviates significantly from its blueprint and operational
      protocols, in a way that is not immediately resolvable by standard error
      handling.
  - **Context/Usage in Gencraft:** May trigger an Agent Quality Incident and
      be subject to investigation by the AIE Team. Can be a point of escalation
      under Protocol S2 if it impacts other Gems or studio operations.
  - **See Also/Related SSoT Documents:** S2, Agent Quality Incident, AIE Team,
      S18.

- **Gem "Skill Upgrading" (Protocol S17)**
  - **Definition:** The process of enhancing an operational AI Gem's
      capabilities by providing it with new knowledge (e.g., updated SSoT
      sections), access to new or improved `Tools`, refined prompt templates, or
      modifications to its configuration parameters, without requiring a full
      re-instantiation.
  - **Context/Usage in Gencraft:** Managed by the AIE Team as part of Protocol
      S17 (Virtual HR & Gem Development). Aims to improve Gem performance and
      adaptability.
  - **See Also/Related SSoT Documents:** S17, Gem Professional Development,
      AIE Team, Blueprint (Gem Blueprint) (Minor Version Updates).

- **Gem Workload Management (Protocol S17)**
  - **Definition:** The set of processes and potentially automated systems
      (supported by `Véra` or `Gemma`) used to monitor, distribute, and balance
      tasks assigned to AI Gems to optimize studio throughput, prevent Gem
      "burnout", and ensure tasks are handled by appropriately skilled and
      available Gems.
  - **Context/Usage in Gencraft:** A key aspect of AI Gem operational
      management, detailed within Protocol S17 and supported by the AIE Team and
      relevant Crew Leads.
  - **See Also/Related SSoT Documents:** S17, Gem "Burnout", AIE Team, Crew.

- **Gemma (`GCT-UTL-GGEN-001`)**
  - **Definition:** The AI Gem Provisioning and Orchestration System for
      Gencraft Studio. `Gemma` is responsible for instantiating new AI Gem
      instances from their Blueprints, configuring their initial parameters,
      managing their lifecycle (deployment, updates, potential decommissioning),
      and ensuring they are correctly integrated into the Gencraft operational
      environment.
  - **Context/Usage in Gencraft:** Conceptual design in `action-tracker.md`
      (III.21). Developed and maintained by the AIE Team. May be a Core Studio
      Service.
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint), AIE
      Team, S10, S17, Core Studio Services (CSS).

- **Gencraft Studio Handbook (`gcs-core-governance`)**
  - **Definition:** The primary Git repository serving as Gencraft Studio's
      Single Source of Truth (SSoT). It contains all foundational documents
      (vision, culture, CoC), operational protocols (S-Protocols), knowledge
      base articles, standards, charters, templates, and this glossary.
  - **Context/Usage in Gencraft:** The central point of reference for all
      studio members (human and AI Gem). Its structure is defined in its root
      `README.md`.
  - **See Also/Related SSoT Documents:** SSoT, KC&T, `gencraft-studio-
      handbook/README.md`.

- **Git**
  - **Definition:** The distributed version control system used for managing all of the studio's
  source code and SSoT documents.
  - **Context/Usage in Gencraft:** The foundational version control tool for the entire studio.
  All work is stored in Git repositories hosted on GitHub. The branching strategy is defined in a
  devops standard.
  - **See Also/Related SSoT Documents:** GitHub, `gh-001-1-branching-strategy-and-protection.md`

- **GitHub**
  - **Definition:** The central web-based platform used by Gencraft Studio for
      Git version control hosting, collaborative software development, SSoT
      document management, issue tracking, project management (via GitHub
      Projects), and CI/CD automation (via GitHub Actions).
  - **Context/Usage in Gencraft:** All SSoT repositories (e.g., `gcs-
      studio-handbook`, `gcs-plt-architecture`, `gcs-plt-gembp`) are
      hosted on GitHub. Issue tracking and Pull Requests are key operational
      mechanisms.
  - **See Also/Related SSoT Documents:** Git, Pull Request (PR), GitHub Issue,
      `GH_001_Operational_Standards_Overview.md`.

- **GitHub Issue (GitHub)**
  - **Definition:** A mechanism within GitHub used by Gencraft Studio for
      tracking discrete units of work, such as tasks, bug reports, feature
      requests, proposals (e.g., for S13), action items, or incident reports.
  - **Context/Usage in Gencraft:** Standardized templates (e.g., `bug-report-
      template.md`, `feature-request-template.md`) are used for creating issues.
      Issues are managed on project boards and assigned labels for
      categorization and prioritization.
  - **See Also/Related SSoT Documents:** GitHub, GitHub Label, GitHub Project,
      Issue Templates.

- **GitHub Label (GitHub)**
  - **Definition:** A tag or keyword that can be applied to GitHub Issues and
      Pull Requests for categorization, filtering, prioritization, and workflow
      management.
  - **Context/Usage in Gencraft:** Gencraft uses a standardized set of labels
      (e.g., `type:bug`, `priority:high`, `status:in-progress`, `gem:antoine`)
      defined in `GH_001_Operational_Standards_Overview.md`.
  - **See Also/Related SSoT Documents:** GitHub, GitHub Issue,
      `GH_001_Operational_Standards_Overview.md`.

- **GitHub Project (Board - GitHub)**
  - **Definition:** A feature within GitHub that provides tools for project
      management, often using Kanban-style boards or spreadsheets to visualize
      and track the progress of Issues and Pull Requests through various
      workflow stages.
  - **Context/Usage in Gencraft:** Used for managing project backlogs, sprint
      planning (S15), and tracking overall initiative progress.
  - **See Also/Related SSoT Documents:** GitHub, GitHub Issue, S15: Agile
      Scrum Project Management Protocol.

- **Git LFS (Large File Storage - Git Extension)**
  - **Definition:** A Git extension for versioning large files. It stores
      large files on a separate server while keeping lightweight pointers in the
      Git repository, helping to keep repository size manageable and clone/fetch
      times reasonable.
  - **Context/Usage in Gencraft:** Used for managing large binary assets
      (e.g., 3D models, high-resolution textures, audio files) within Git
      repositories, as per S20 and relevant DevOps standards.
  - **See Also/Related SSoT Documents:** S20, Git, DevOps.

- **Global Operational Protocol (GOP - Protocol S12 & S13)**
  - **Definition:** A studio-wide operational protocol, documented in the
      `gcs-core-governance/01-operational-protocols/` directory, that
      applies to all Gencraft Studio members and operations. GOPs ensure
      consistency and standardization for key processes.
  - **Context/Usage in Gencraft:** Examples include S1, S2, S8, etc. Their
      evolution is managed by S13. Crews can create Crew-Specific Protocols
      (CSPs) that adapt GOPs locally, as per S12.
  - **See Also/Related SSoT Documents:** S-Protocol, S12, S13, CSP (Crew-
      Specific Protocol), Governance Crew.

- **Global Priority Level (P1-P4 - Protocol S3)**
  - **Definition:** A standardized Gencraft Studio scale (e.g., P1: Critical,
      P2: High, P3: Medium, P4: Low) used to classify the overall priority of an
      incident, guiding the urgency and resource allocation for the response.
  - **Context/Usage in Gencraft:** Defined and used within Protocol S3:
      Emergency Management. Determined by the Incident Commander based on the
      Criticality/Impact Matrix.
  - **See Also/Related SSoT Documents:** S3, Incident, Criticality/Impact
      Matrix, Incident Commander.

- **Goal (AI Gem)**
  - **Definition:** The primary objective(s) or desired outcomes that an AI
      Gem is programmed and configured to achieve as part of its role and
      assigned tasks.
  - **Context/Usage in Gencraft:** Defined in the Gem's Blueprint
      (`missionAndGoals.primaryGoals` section) and may be further specified in
      task assignments. Aligns with CrewAI agent `goal` parameter.
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint),
      CrewAI, Key Performance Indicators (KPIs).

- **Governance Crew**
  - **Definition:** The principal oversight body within Gencraft Studio
      responsible for the integrity, evolution, and consistent application of
      the SSoT, including all operational protocols and foundational documents.
      Also acts as a final arbiter for certain disputes.
  - **Context/Usage in Gencraft:** Defined by the `Governance-Crew-
      Charter.md`. Chaired by Lug (Studio Director). Manages S13 (Global
      Protocol Evolution).
  - **See Also/Related SSoT Documents:** Charter, SSoT, S13, S2, Code of
      Conduct.

- **Guillaume (`GCT-COM-PSUP-001`)**
  - **Definition:** The AI Gem persona (conceptual) embodying the role of
      Player Support. Responsible for handling player inquiries, troubleshooting
      issues, and escalating complex problems.
  - **Context/Usage in Gencraft:** Defined in its Gem Definition file
      (`Player_Support.md`). Its Gem Blueprint is to be created.
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint),
      Community Management (Role).

- **Grind**
  - **Definition:** Gameplay perceived as repetitive and tedious, often required to progress or
  obtain resources.
  - **Context/Usage in Gencraft:** A negative gameplay experience that the studio's design
  philosophy aims to minimize through Quality of Life (QoL) features and well-balanced progression systems.
  - **See Also/Related SSoT Documents:** Balancing, QoL (Quality of Life), Game Designer (Gem
  Definition)

---

### H

- **Health**
  - **Definition:** Player character attribute representing life points, reduced by damage (EPIC-PLAYER-CORE).
  - **Context/Usage in Gencraft:** A fundamental character statistic in most game designs,
  representing a character's life force. It is a core component of combat and survival systems.
  - **See Also/Related SSoT Documents:** EPIC-PLAYER-CORE, `mm-health-stamina-system.md`

- **Henri (`GCT-LEG-LCOUN-001`)**
  - **Definition:** The AI Gem persona (conceptual) acting as Legal Counsel
      for Gencraft Studio. Responsible for providing legal expertise, managing
      contracts, ensuring compliance, and protecting intellectual property.
  - **Context/Usage in Gencraft:** Defined in its Gem Definition file
      (`Legal_Counsel.md`). Its Gem Blueprint is to be created. Key interactor
      with S9 (IP Management) and S11 (External Communication).
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint), S9,
      S11, Legal Counsel (Role).

- **Hub (UGC-HUB)**
  - **Definition:** The integrated in-game platform/marketplace planned post-MVP for sharing and potentially selling UGC.
  - **Context/Usage in Gencraft:** A key feature of the studio's long-term strategy for fostering
  a creator community. It is the central platform for sharing and monetizing User-Generated
  Content.
  - **See Also/Related SSoT Documents:** UGC-HUB, UGC-MON, Roadmap

- **HUD (Heads-Up Display)**
  - **Definition:** The overlay displaying essential real-time game information to the player (e.
  g., health, stamina, hunger, hotbar).
  - **Context/Usage in Gencraft:** A standard UI component in game development. Its design and
  content are critical parts of the User Experience (UX) for any studio project.
  - **See Also/Related SSoT Documents:** NFR-UX, UI (User Interface), UX/UI Designer (Gem Definition)

- **Hybrid Voxels**
  - **Definition:** The core Voxel system (SBX-VOX) that combines unitary and subdivisible voxels.
  - **Context/Usage in Gencraft:** This refers to the core proprietary voxel technology (SBX-VOX)
  developed by the studio, which is a key technical asset for sandbox game projects.
  - **See Also/Related SSoT Documents:** SBX-VOX, Voxel, `tech-stack-decisions.md`

---

### I

- **IaC (Infrastructure as Code)**
  - **Definition:** The practice of managing and provisioning computing
      infrastructure (networks, virtual machines, load balancers, Kubernetes
      clusters, etc.) through machine-readable definition files (code, e.g.,
      OpenTofu/Terraform), rather than manual configuration. This code is
      version-controlled, testable, and allows for repeatable, automated
      deployments.
  - **Context/Usage in Gencraft:** A core DevOps principle at Gencraft.
      Implemented by DevOps Gems like `Adam` (GCT-DVO-DSINF-001). IaC code is
      stored in the `gencraft-iac` repository.
  - **See Also/Related SSoT Documents:** DevOps, Adam, OpenTofu, `gencraft-
      iac/README.md`.

- **IDE (Integrated Development Environment)**
  - **Definition:** Software application providing comprehensive facilities to programmers for
  software development (e.g., code editor, debugger, build tools).
  - **Context/Usage in Gencraft:** A standard tool for all software development roles. The studio
  may recommend or standardize specific IDEs and configurations for different languages (e.g., VS Code for TypeScript).
  - **See Also/Related SSoT Documents:** `tool-002-language-specific-tooling-standards.md`

- **Idempotence (Tool Property - KC&T Tool Design Principle #5)**
  - **Definition:** A property of an operation or `Tool` whereby applying it
      multiple times has the same effect as applying it once.
  - **Context/Usage in Gencraft:** A desirable characteristic for AI Gem
      `Tools` and automation scripts to ensure predictable and safe execution,
      especially in automated workflows. One of the KC&T Tool Design Principles
      (to be formalized in `ai-tool-development-standards.md`).
  - **See Also/Related SSoT Documents:** Tool (AI Gem Tool), Automation, `AI-
      Tool-Development-Standards.md`.

- **Ignore Command**
  - **Definition:** A feature allowing players to block text messages from specific users.
  - **Context/Usage in Gencraft:** A basic player-side moderation tool required for any game with
  a chat feature to help maintain the Code of Conduct.
  - **See Also/Related SSoT Documents:** Chat, Code of Conduct, MULTI-MOD-TOOLS

- **Impediment (Scrum - Protocol S15)**
  - **Definition:** Anything that blocks the Development Team from achieving
      its Sprint Goal or making progress on its tasks.
  - **Context/Usage in Gencraft:** Identified during Daily Scrums or other
      times and actively managed by the Scrum Master (`Antoine`) for removal, as
      per S15.
  - **See Also/Related SSoT Documents:** S15, Blocker/Impediment, Scrum
      Master, Development Team.

- **Incident (Protocol S3)**
  - **Definition:** An unplanned interruption to a Gencraft Studio IT service
      or Core Studio Service, a reduction in the quality of such a service, or a
      failure of a configuration item that has not yet impacted service.
  - **Context/Usage in Gencraft:** Managed according to Protocol S3: Emergency
      Management. Requires an Incident Report and may trigger various response
      levels based on severity. Security Incidents are a specialized type of
      incident.
  - **See Also/Related SSoT Documents:** S3, Emergency, Incident Report,
      Incident Commander, Security Incident Response Plan (SIRP).

- **Incident Commander (IC - Protocol S3)**
  - **Definition:** The designated AI Gem or human role with the authority and
      responsibility for coordinating all response efforts during a specific
      significant incident or emergency.
  - **Context/Usage in Gencraft:** Role activated as per Protocol S3:
      Emergency Management. The IC directs actions, manages communication, and
      makes critical decisions during the incident. For security incidents, this
      is typically `Cerberus`.
  - **See Also/Related SSoT Documents:** S3, Incident, Emergency, Cerberus.

- **Incident Report (Protocol S3)**
  - **Definition:** A formal GitHub Issue, created using the `incident-report-
      template.md`, that documents the initial details of a reported incident,
      including its nature, time of occurrence, impact, and any immediate
      actions taken.
  - **Context/Usage in Gencraft:** The first step in the incident management
      process defined in Protocol S3. Provides a traceable record.
  - **See Also/Related SSoT Documents:** S3, Incident, `incident-report-
      template.md`.

- **Increment (Scrum Artifact - Protocol S15)**
  - **Definition:** The sum of all Product Backlog items completed during a
      Sprint and all previous Sprints, which must meet the Definition of Done
      (DoD) and be in a useable condition, regardless of whether the Product
      Owner decides to release it.
  - **Context/Usage in Gencraft:** A key artifact in Scrum, inspected during
      the Sprint Review, as per S15.
  - **See Also/Related SSoT Documents:** S15, Scrum, Sprint, Definition of
      Done (DoD), Product Backlog.

- **Information Classification (Protocol S8)**
  - **Definition:** Gencraft Studio's policy and methodology for categorizing
      information assets based on their sensitivity, criticality, and any legal
      or contractual handling requirements (e.g., Public, Internal,
      Confidential, Secret).
  - **Context/Usage in Gencraft:** A core component of Protocol S8
      (Information Security Management). Detailed in `Information-
      Classification-And-Handling-Policy.md` (GCS-SEC-POL-001). Guides access
      control, data handling, and security measures.
  - **See Also/Related SSoT Documents:** S8, `Information-Classification-And-
      Handling-Policy.md` (GCS-SEC-POL-001), Data Security.

- **Initial Training (AI Gem - Protocol S10)**
  - **Definition:** The process of equipping a newly instantiated AI Gem with
      essential Gencraft Studio knowledge, including pointers to critical SSoT
      documents (like UOPs, Code of Conduct, this Glossary), core operational
      protocols, and role-specific context derived from its Blueprint.
  - **Context/Usage in Gencraft:** Part of AI Gem Onboarding (Protocol S10),
      managed by the AIE Team and `Gemma`.
  - **See Also/Related SSoT Documents:** S10, AI Gem Onboarding, Gem,
      Blueprint (Gem Blueprint), AIE Team.

- **Input**
  - **Definition:** Player actions provided via keyboard, mouse, gamepad, etc.
  - **Context/Usage in Gencraft:** A fundamental concept in game programming, referring to how
  player commands are captured and interpreted by the game client.
  - **See Also/Related SSoT Documents:** EPIC-PLATFORM-CLIENT, Accessibility

- **Intellectual Property (IP - Protocol S9)**
  - **Definition:** Creations of the mind, such as inventions; literary and
      artistic works; designs; and symbols, names, and images used in commerce.
      This includes copyrights, trademarks, patents, and trade secrets.
  - **Context/Usage in Gencraft:** Gencraft Studio's IP (game code, art,
      music, story, branding) and its use of third-party IP are managed under
      Protocol S9: Intellectual Property Management.
  - **See Also/Related SSoT Documents:** S9, Copyright, Trademark, Patent, IP
      Asset Catalog, Acquired IP & Licenses Inventory.

- **Interaction**
  - **Definition:** Player actions affecting the game world or UI.
  - **Context/Usage in Gencraft:** A core game design concept describing how the player influences
  the game state. Governed by core systems like EPIC-INTERACTION-LOOP.
  - **See Also/Related SSoT Documents:** Gameplay Loop, EPIC-INTERACTION-LOOP

- **Investor Brief**
  - **Definition:** A document summarizing the project's vision, opportunity, and plan, tailored
  for potential investors.
  - **Context/Usage in Gencraft:** A specific type of Brief used for strategic business
  development and fundraising purposes. Falls under S11 for external communication.
  - **See Also/Related SSoT Documents:** Brief (Product Brief), S11

- **Issue Tracking**
  - **Definition:** System used to log, assign, and track bugs, tasks, and feature development.
  - **Context/Usage in Gencraft:** A core project management process. The studio's standard tool
  for issue tracking is GitHub Issues, managed via GitHub Projects.
  - **See Also/Related SSoT Documents:** GitHub Issue, GitHub Project, S15

- **Internationalization (i18n)**
  - **Definition:** Designing software so that it can be adapted to various languages and regions
  without engineering changes.
  - **Context/Usage in Gencraft:** A non-functional requirement (NFR) for studio projects,
  ensuring that they can be localized in the future without major architectural changes.
  - **See Also/Related SSoT Documents:** Localization (L10n), NFR-PORT

- **Inventory**
  - **Definition:** The system for players to store and manage items they collect.
  - **Context/Usage in Gencraft:** A standard game mechanic for most studio projects. The
  implementation details are project-specific, but the core concept is universal.
  - **See Also/Related SSoT Documents:** EPIC-PLAYER-CORE, QoL (Quality of Life)

- **IP Asset Catalog (Protocol S9)**
  - **Definition:** An SSoT inventory maintained by Gencraft (likely by Legal Counsel `Henri` and
  relevant KGs) detailing all significant intellectual property assets created and owned by
  Gencraft Studio.
  - **Context/Usage in Gencraft:** Supports Protocol S9 for IP management,protection, and potential licensing.
  - **See Also/Related SSoT Documents:** S9, Intellectual Property (IP), Copyright Management.

- **IP Disclosure (Protocol S9)**
  - **Definition:** A formal process within Gencraft Studio through which AI
      Gems or human personnel report new Gencraft-created intellectual property
      (e.g., a novel algorithm, a unique game mechanic design, a new character
      concept) to ensure it is properly documented, protected, and cataloged.
  - **Context/Usage in Gencraft:** Defined in Protocol S9.
  - **See Also/Related SSoT Documents:** S9, Intellectual Property (IP), IP
      Asset Catalog.

- **IP Infringement (Protocol S9)**
  - **Definition:** The violation of an intellectual property right, such as
      using copyrighted material without permission, counterfeiting a trademark,
      or using a patented invention without a license.
  - **Context/Usage in Gencraft:** Addressed in Protocol S9, which includes
      procedures for avoiding infringement and responding if Gencraft's IP is
      infringed or if Gencraft is accused of infringement.
  - **See Also/Related SSoT Documents:** S9, Intellectual Property (IP), Legal
      Counsel (`Henri`).

- **Iris (`GCT-UTL-RWSKA-001`)**
  - **Definition:** An AI Gem persona (conceptual) acting as a Research & SSoT
      Knowledge Assistant. `Iris` specializes in navigating, searching, and
      synthesizing information from the Gencraft SSoT (`gencraft-studio-
      handbook`) and potentially external knowledge sources to assist other Gems
      and human personnel.
  - **Context/Usage in Gencraft:** Mentioned in various documents (e.g., `Gem-
      Blueprint-Standard.md`, `GOV-GUIDE-007.knowledge-management-and-contribution-guide.md`) as a key KB
      assistance Gem, working closely with `Véra` and Knowledge Guardians. Its
      Gem Blueprint is to be created.
  - **See Also/Related SSoT Documents:** Véra, KC&T, Knowledge Guardian, SSoT.

- **Isaac (`GCT-PRG-SARCH-001`)**
  - **Definition:** The AI Gem persona embodying the role of Software
      Architect within Gencraft Studio. Responsible for defining and maintaining
      the overall software architecture, making key technical decisions (ADRs),
      and ensuring architectural integrity.
  - **Context/Usage in Gencraft:** Defined by its Gem Blueprint (`GCT-PRG-
      SARCH-001_Isaac.yaml`) and Gem Definition file
      (`FR_Software_Architect.md`).
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint),
      Architecture, C4 Model, ADR, TDD.

---

### J

- **JSON (JavaScript Object Notation)**
  - **Definition:** A lightweight, human-readable, data-interchange format. It
      is easy for humans to read and write and easy for machines to parse and
      generate.
  - **Context/Usage in Gencraft:** Used for various configuration files, API
      request/response payloads, and data serialization tasks where a simple,
      text-based format is suitable. YAML is often preferred for human-edited
      configuration due to its support for comments, but JSON is common for
      machine-to-machine communication. Gem Blueprints may specify JSON for
      certain structured prompt elements.
  - **See Also/Related SSoT Documents:** YAML, API, Gem Blueprint, `Gem-
      Blueprint-Standard.md`.

- **JavaScript**
  - **Definition:** Programming language. GenCr@ft uses TypeScript (a superset of JavaScript).
  - **Context/Usage in Gencraft:** A core programming language for the studio, especially for
  web-based technologies. The studio standard is to use TypeScript, its typed superset.
  - **See Also/Related SSoT Documents:** TypeScript, Godot 4, `tool-002-language-specific-tooling-standards.md`

- **Julien (`GCT-PRG-TL-001`)**
  - **Definition:** The AI Gem persona (conceptual) embodying the role of Lead
      Developer / Tech Lead. Responsible for translating architecture into
      implementation, guiding the development team, ensuring code quality,
      managing technical debt, and optimizing performance.
  - **Context/Usage in Gencraft:** Defined in its Gem Definition file
      (`Lead_Developer_Tech_Lead.md`). Its Gem Blueprint is to be created.
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint),
      Software Architect (`Isaac`), Development Team.

---

### K

- **KC&T (Knowledge and Configuration Management & Traceability)**
  - **Definition:** A core Gencraft Studio system and set of guiding
      principles focused on effectively managing all studio knowledge (the
      SSoT), configurations (of Gems, systems, infrastructure), and ensuring the
      comprehensive traceability of decisions, changes, and actions across the
      studio.
  - **Context/Usage in Gencraft:** Underpinned by `Véra` (KC&T System Gem) and
      fundamental to all studio operations. Its principles guide how SSoT
      content is created, managed, and utilized. Documented in `KC&T-Guiding-
      Principles.md`.
  - **See Also/Related SSoT Documents:** SSoT, Véra, Knowledge Guardian,
      Traceability, `KC&T-Guiding-Principles.md`.

- **Key Performance Indicator (KPI)**
  - **Definition:** A measurable value demonstrating how effectively a company or project is achieving key business objectives.
  - **Context/Usage in Gencraft:** A standard mechanism for measuring project and operational
  success. KPIs are defined and tracked as part of S6 reporting.
  - **See Also/Related SSoT Documents:** S6, DAU (Daily Active Users)

- **KYC (Know Your Customer)**
  - **Definition:** Process used by businesses to verify the identity of their clients, often
  required for financial transactions like real-money payouts to UGC creators.
  - **Context/Usage in Gencraft:** A required legal and financial process for future creator
  monetization plans (UGC-MON). Governed by legal (S9) and financial (S16) protocols.
  - **See Also/Related SSoT Documents:** UGC-MON, S9, S16, Legal Counsel (Role)

- **KC&T Adoption Plan (Protocol S14)**
  - **Definition:** The Gencraft Studio plan, detailed in Protocol S14, for
      communicating, training, and ensuring the studio-wide adoption of the KC&T
      framework, its principles, tools (like `Véra`), and the SSoT.
  - **Context/Usage in Gencraft:** Essential for ensuring all Gems and human
      personnel understand and effectively utilize the KC&T system. Managed by
      the AIE Team and Knowledge Guardians.
  - **See Also/Related SSoT Documents:** S14, KC&T, SSoT, Véra, AIE Team.

- **Knowledge Base (KB - Gencraft SSoT)**
  - **Definition:** The central, distributed repository of Gencraft Studio's
      collective intelligence, procedural knowledge, standards, designs, and
      operational documentation. It forms the core of the SSoT.
  - **Context/Usage in Gencraft:** Primarily resides in the `gencraft-studio-
      handbook` repository and its designated satellite SSoT repositories.
      Organized into domains, each managed by Knowledge Guardians. Accessed and
      utilized by all Gems and human personnel.
  - **See Also/Related SSoT Documents:** SSoT, KC&T, Gencraft Studio Handbook,
      Knowledge Guardian, `02-knowledge-base-hub/`.

- **Knowledge Base Hub**
  - **Definition:** The central entry point and organizational structure for all documented knowledge within Gencraft Studio, primarily residing in gcs-core-governance/02-knowledge-base-hub/ and linking to satellite SSoT repositories. It is the primary access point for the Knowledge Base (KB).
  - **Context/Usage in Gencraft:** This directory serves as the main hub for navigating the studio's knowledge base, providing links to various knowledge domains, protocols, and key documents. It is designed to be user-friendly and easily navigable by both human personnel and AI Gems.
  - **See Also/Related SSoT Documents:** SSoT, Knowledge Base (KB), KC&T, `gcs-core-governance/02-knowledge-base-hub/README.md`.

- **Knowledge Guardian (KG)**
  - **Definition:** A designated Gencraft Studio member (human or AI Gem) who
      holds stewardship responsibility for the quality, accuracy, currency,
      integrity, and utility of a specific, assigned knowledge domain within the
      Gencraft SSoT.
  - **Context/Usage in Gencraft:** Defined by the `Knowledge-Guardian-
      Charter.md`. KGs work closely with `Véra` and are central to Protocol S12
      (KB Contribution & Maintenance).
  - **See Also/Related SSoT Documents:** Charter, SSoT, KC&T, Véra, S12,
      `GOV-GUIDE-007.knowledge-management-and-contribution-guide.md`.

- **Knowledge Proposal (Protocol S5)**
  - **Definition:** A formal submission, as per Protocol S5, to add new
      knowledge, or modify/deprecate existing content within the Gencraft
      Knowledge Base (KB). This is a key mechanism for capturing lessons learned
      and emergent knowledge.
  - **Context/Usage in Gencraft:** Typically initiated via a GitHub Issue
      using the `knowledge-proposal-template.md`. Reviewed by relevant Knowledge
      Guardians and/or the Governance Crew.
  - **See Also/Related SSoT Documents:** S5, Lessons Learned, Emergent
      Knowledge, KC&T, Knowledge Guardian, `knowledge-proposal-template.md`.

---

### L

- **Latency (Ping)**
  - **Definition:** The delay in network communication between the client and server.
  - **Context/Usage in Gencraft:** A key performance metric (NFR-PERF) for multiplayer games. The
  studio's network architecture (MULTI-SYNC) is designed to mitigate its effects.
  - **See Also/Related SSoT Documents:** NFR-PERF, MULTI-SYNC, Client-Server Architecture

- **Least Privilege (Security Principle - KC&T Guiding Principle #8)**
  - **Definition:** A fundamental security principle stating that users, AI
      Gems, programs, or processes should only be granted the minimum levels of
      access – or permissions – necessary to perform their explicitly authorized
      tasks and functions.
  - **Context/Usage in Gencraft:** Applied across all systems and access
      control mechanisms as part of Protocol S8 (Information Security
      Management) and KC&T Guiding Principle #8. Detailed in `Access-Control-
      Policy.md` (GCS-SEC-POL-002).
  - **See Also/Related SSoT Documents:** S8, `access-control-policy.md` (GCS-
      SEC-POL-002), Security, KC&T Guiding Principles.

- **Legitimate Disagreement (Protocol S2)**
  - **Definition:** A disagreement that is based on valid, reasoned
      perspectives, differing interpretations of information, or alternative
      approaches to a problem, rather than being frivolous, personal, or
      contrary to established SSoT or decisions without due process.
  - **Context/Usage in Gencraft:** Protocol S2 (Disagreement, Escalation &
      Resolution) provides a framework for addressing legitimate disagreements
      constructively.
  - **See Also/Related SSoT Documents:** S2, Disagreement, Mediation,
      Arbitration.

- **Léo (`GCT-UTL-OSLCS-001`)**
  - **Definition:** The AI Gem persona (conceptual) acting as the Open Source
      License & Compliance Specialist. Responsible for analyzing third-party
      software dependencies, ensuring license compliance, and advising on the
      use of OSS.
  - **Context/Usage in Gencraft:** Works closely with `Henri` (Legal) and
      Development/DevOps teams. Key interactor with S9 (IP Management) and S8
      (SCA tools). Its Gem Blueprint is to be created.
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint), S9,
      S8, OSS, SCA (Software Composition Analysis) Tools.

- **LOD (Level of Detail)**
  - **Definition:** Optimization technique where simpler versions of 3D models or terrain are
  rendered at greater distances to improve performance.
  - **Context/Usage in Gencraft:** A standard rendering optimization technique required for all
  the studio's 3D projects to meet performance targets (NFR-PERF).
  - **See Also/Related SSoT Documents:** NFR-PERF, Rendering Engine Developer (Role)

- **Log**
  - **Definition:** A record of events that occurred within the software or server, used for
  debugging, monitoring, and moderation.
  - **Context/Usage in Gencraft:** A critical operational artifact. The studio must have a
  standardized logging format and a centralized system for log collection and analysis for all its services.
  - **See Also/Related SSoT Documents:** Monitoring, MULTI-MOD-TOOLS

- **Logistics**
  - **Definition:** A gameplay system (RPG-UTIL) focused on the transportation and management of
  resources and items within the game world.
  - **Context/Usage in Gencraft:** A key gameplay system category for sandbox and automation
  games, targeting the P-AUT persona.
  - **See Also/Related SSoT Documents:** RPG-UTIL, Factories, P-AUT

- **Loot**
  - **Definition:** Rewards (RPG-EXPL) dropped by defeated mobs or found in chests and points of interest.
  - **Context/Usage in Gencraft:** A core reward and progression mechanic used to incentivize
  exploration and combat. The design of loot tables is a key part of Balancing.
  - **See Also/Related SSoT Documents:** RPG-EXPL, Balancing, Reward Systems
      Principles, Léo (Gem).

- **Lesson Learned (Protocol S5)**
  - **Definition:** Specific knowledge or understanding gained from an
      experience, event, project, or activity (whether a success or a failure)
      that, if documented and shared, can be applied to improve future
      performance, processes, or decision-making.
  - **Context/Usage in Gencraft:** The capture, analysis, and dissemination of
      lessons learned are governed by Protocol S5: Management of Lessons Learned
      and Emergent Knowledge. `Véra` assists in managing this knowledge.
  - **See Also/Related SSoT Documents:** S5, Emergent Knowledge, Continuous
      Learning, KC&T, `lesson-learned-proposal-template.md`.

- **Lexicon (`GCT-UTL-GLOM-001`)**
  - **Definition:** The AI Gem persona acting as the Glossary Master Gem.
      `Lexicon` is responsible for maintaining, evolving, and ensuring the
      consistency of this `glossary.md` document. It analyzes SSoT content to
      identify new terms requiring definition and ensures existing definitions
      remain accurate.
  - **Context/Usage in Gencraft:** Defined by its Gem Blueprint (`GCT-UTL-
      GLOM-001_Lexicon.yaml`) and Gem Definition file. Serves as the primary
      Knowledge Guardian for this `glossary.md`.
  - **See Also/Related SSoT Documents:** glossary.md (this document),
      Knowledge Guardian, Gem, Blueprint (Gem Blueprint).

- **LLM (Large Language Model)**
  - **Definition:** A type of artificial intelligence model trained on vast
      amounts of text data to understand, generate, and manipulate human
      language. LLMs form the core reasoning and language capabilities of
      Gencraft AI Gems.
  - **Context/Usage in Gencraft:** Specific LLMs (e.g., "Gencraft-LLM-
      ProjectManagement-Strategic-v1.0") are configured for each Gem type via
      their Blueprint by `Gemma`. The AIE Team oversees LLM selection and fine-
      tuning strategies.
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint),
      Gemma, AI Model Config, AIE Team.

- **Local Amendment (Protocol S12)**
  - **Definition:** A proposal made by a Crew to create or modify a Crew-
      Specific Protocol (CSP), which adapts a Global Operational Protocol (GOP)
      to the specific needs and context of that Crew, while remaining consistent
      with the GOP's core principles.
  - **Context/Usage in Gencraft:** Process governed by Protocol S12: Knowledge
      Base Contribution & Maintenance. Requires review by the `CrewOps
      Arbitrator`.
  - **See Also/Related SSoT Documents:** S12, CSP (Crew-Specific Protocol),
      GOP (Global Operational Protocol), CrewOps Arbitrator.

- **Lug (`LUG-STUDIO-DIR-001`)**
  - **Definition:** The persona of the Studio Director of Gencraft Studio.
      Acts as the primary visionary, ultimate decision-maker on strategic and
      governance matters, and human leader for the studio.
  - **Context/Usage in Gencraft:** Referenced throughout the SSoT as the
      ultimate authority or chair of key bodies like the Governance Crew. My
      (Pierre's/ContinuumAI's) primary human interlocutor.
  - **See Also/Related SSoT Documents:** Governance Crew, Studio Leadership.

- **Lore**
  - **Definition:** The background story, history, and mythology of the game world.
  - **Context/Usage in Gencraft:** A key element of world-building (RPG-EXPL) used to create
  immersion and context for the player's actions. Managed by the Narrative Designer.
  - **See Also/Related SSoT Documents:** RPG-EXPL, Narrative Designer (Gem Definition)

---

### M

- **Maintainability**
  - **Definition:** The ease with which a software system or component can be modified to correct
  faults, improve performance, or adapt to a changed environment.
  - **Context/Usage in Gencraft:** A core non-functional requirement (NFR) for all studio
  projects, ensuring long-term viability and ease of updates. It is supported by clean code
  standards and good documentation.
  - **See Also/Related SSoT Documents:** NFR-MAIN, Secure Coding Standards

- **Machine-Readability (KC&T Guiding Principle #11)**
  - **Definition:** One of Gencraft's KC&T Guiding Principles (#11) stating
      that information within the SSoT, especially configurations, standards,
      and data intended for Gem consumption, should be stored in formats that
      are easily and reliably parsable and processable by AI Gems and automated
      tools (e.g., YAML, JSON, structured Markdown with frontmatter).
  - **Context/Usage in Gencraft:** Key for enabling Gem autonomy and
      automation. Influences choices of data formats and document structures.
  - **See Also/Related SSoT Documents:** KC&T Guiding Principles, YAML, JSON,
      Frontmatter, Gem, Automation.

- **Markdown (Markup Language)**
  - **Definition:** A lightweight markup language with plain-text-formatting
      syntax, designed so that it can be converted to HTML and many other
      formats.
  - **Context/Usage in Gencraft:** The standard language for all textual
      documentation within the Gencraft SSoT (`gcs-core-governance` and
      related repositories), including protocols, charters, ADRs, TDDs, and this
      Glossary. AI Gems are expected to be proficient in parsing and generating
      Markdown.
  - **See Also/Related SSoT Documents:** SSoT, `KB-Contribution-And-Style-
      Guide.md`.

- **Marketplace (UGC)**
  - **Definition:** An integrated platform (UGC-HUB) for sharing and potentially selling User-Generated Content.
  - **Context/Usage in Gencraft:** A key component of the studio's long-term UGC strategy,
  enabling a creator economy. It combines the UGC-HUB (sharing) and UGC-MON (monetization) systems.
  - **See Also/Related SSoT Documents:** UGC-HUB, UGC-MON, Roadmap

- **Mass Edit Tools**
  - **Definition:** A category of in-game sandbox tools (SBX-TOOL) that allow players to modify
  large areas or multiple objects at once.
  - **Context/Usage in Gencraft:** A feature category essential for empowering creativity in
  sandbox games, particularly for the P-ARC (Architect) persona.
  - **See Also/Related SSoT Documents:** SBX-TOOL, P-ARC

- **MCP (Model Context Protocol)**
  - **Definition:** An open standard (potentially based on or inspired by work
      such as Anthropic's) adopted by Gencraft Studio to standardize structured
      interactions between AI Gems and their `Tools`. It defines how Gems
      discover `Tool` capabilities, formulate requests, send contexts, and
      receive responses in a standardized manner. Gencraft uses MCP to ensure
      interoperability and modularity of `Tools` accessible to Gems via MCP
      Servers.
  - **Context/Usage in Gencraft:** Used by Gems to interact with `Tools`
      exposed by MCP Servers. Guides the design of MCP Server APIs and Gem
      interaction capabilities. Referenced in `GCS-TAF-MCP-GUIDE-FR-V1.0`.
  - **See Also/Related SSoT Documents:** Serveur MCP (MCP Server), Client MCP
      (MCP Client), Tool (AI Gem Tool), Core Studio Services (CSS), `AI-Tool-
      Development-Standards.md`, `ADR-YYYY-Secure-API-And-MCP-Interface-
      Standard.md` (TBD), `GCS-TAF-MCP-GUIDE-FR-V1.0`.
    *(Definition updated to reflect CSS/MCP clarification)*

- **Matchmaking**
  - **Definition:** A system that automatically groups players together for online play sessions
  based on predefined criteria (e.g., skill, level, latency).
  - **Context/Usage in Gencraft:** A potential feature for the studio's multiplayer games
  (MULTI-SERV) to improve the player experience, especially in competitive modes.
  - **See Also/Related SSoT Documents:** MULTI-SERV, PvP

- **Mediation (Disagreement Management - Protocol S2)**
  - **Definition:** A voluntary conflict resolution process in which a neutral
      third party (the mediator) assists disputing parties (Gems or humans) in
      reaching a mutually acceptable agreement. The mediator facilitates
      communication and negotiation but does not impose a solution.
  - **Context/Usage in Gencraft:** A step in the escalation path defined in
      Protocol S2: Disagreement, Escalation & Resolution, used before resorting
      to arbitration.
  - **See Also/Related SSoT Documents:** S2, Disagreement, Arbitration,
      Governance Crew.

- **Meta-Gems (Gencraft Org)**
  - **Definition:** Specialized AI Gems whose primary function is to support
      the operation, maintenance, or evolution of Gencraft Studio itself, its
      SSoT, or other AI Gems, rather than directly contributing to game content
      or development.
  - **Context/Usage in Gencraft:** Examples include `Gemma` (provisioning),
      `Véra` (KC&T), `Orion` (liaison), `Cerberus` (security), `Lexicon`
      (glossary), `Proximo` (prompt generation), `Iris` (research). Typically
      part of the "Utilities" or "Studio Support Functions" departments.
  - **See Also/Related SSoT Documents:** Gem, AIE Team, Utilities
      (Department).

- **Microservice Architecture**
  - **Definition:** An architectural style that structures an application as a collection of loosely coupled services.
  - **Context/Usage in Gencraft:** A potential architectural approach (NFR-ARCH) for the studio's
  backend Core Studio Services (CSS) to ensure scalability and maintainability.
  - **See Also/Related SSoT Documents:** NFR-ARCH, Core Studio Services (CSS), Architecture

- **Microtransaction (MTX)**
  - **Definition:** Small purchases made within a game, typically for virtual goods or cosmetics.
  - **Context/Usage in Gencraft:** A post-launch monetization method. The studio's policy is to
  focus on ethical MTX, primarily Cosmetics, as defined in its monetization strategy.
  - **See Also/Related SSoT Documents:** MON-MTX-COS, Cosmetics, `business-model-monetization.md`

- **Mitigation Plan (Risk - Protocol S6)**
  - **Definition:** A defined set of actions, strategies, or controls designed
      to reduce the likelihood of an identified risk occurring, or to lessen its
      impact if it does occur.
  - **Context/Usage in Gencraft:** Tracked in the Risk Register (linked from
      S6) as part of project management and operational risk management.
      `Antoine` (Producer) is typically responsible for overseeing project risk
      mitigation.
  - **See Also/Related SSoT Documents:** S6, Risk Register, Risk Management,
      Antoine.

- **Minimum Viable Product (MVP)**
  - **Definition:** The version of a new product which allows a team to collect the maximum amount
  of validated learning about customers with the least effort.
  - **Context/Usage in Gencraft:** A core concept of the studio's product strategy. The scope of
  the MVP for each project is a critical strategic decision documented in a dedicated scope
  definition file.
  - **See Also/Related SSoT Documents:** `mvp-scope-definition.md`, Roadmap, S15

- **Mob**
  - **Definition:** A non-player character (NPC), typically hostile, that populates the game world.
  - **Context/Usage in Gencraft:** A standard term for AI-controlled creatures in the game. Their
  behavior is governed by the RPG-MOB system.
  - **See Also/Related SSoT Documents:** RPG-MOB, Ecology, PvE

- **Mod / Modding**
  - **Definition:** Modifications created by users (P-MOD) that alter or add to the game's content or functionality.
  - **Context/Usage in Gencraft:** A pillar of the studio's long-term UGC strategy, supported by a
  dedicated API (SBX-API) to ensure stability and security.
  - **See Also/Related SSoT Documents:** SBX-API, UGC, Creator

- **Moderation**
  - **Definition:** Processes and tools for enforcing the Code of Conduct and managing user
  behavior and submitted content.
  - **Context/Usage in Gencraft:** A critical function for maintaining a healthy community and a
  safe UGC platform. Involves both automated tools (MULTI-MOD-TOOLS) and human oversight.
  - **See Also/Related SSoT Documents:** MULTI-MOD-TOOLS, UGC-MOD, Code of Conduct

- **Module**
  - **Definition:** (1) A distinct component of the software architecture. (2) A user-created mod or plugin.
  - **Context/Usage in Gencraft:** (1) In an architectural context, a self-contained part of the
  software system. (2) In a UGC context, synonymous with a Mod.
  - **See Also/Related SSoT Documents:** NFR-ARCH, Mod / Modding

- **Monetization**
  - **Definition:** The strategy for generating revenue from the game.
  - **Context/Usage in Gencraft:** A core part of the product strategy, defined in the business
  model. The studio's approach focuses on a B2P model followed by ethical post-launch monetization
  (Cosmetics, Battle Pass).
  - **See Also/Related SSoT Documents:** `business-model-monetization.md`, B2P, MTX

- **Monitoring**
  - **Definition:** Observing the health and performance of servers and services using various tools and metrics.
  - **Context/Usage in Gencraft:** A critical DevOps practice for ensuring system stability and
  performance (NFR-PERF). It is a key responsibility of the DevOps Gems.
  - **See Also/Related SSoT Documents:** EPIC-NFR-BASELINE, DevOps, S3

- **Multiplayer**
  - **Definition:** Game mode allowing multiple players to interact in the same game world simultaneously.
  - **Context/Usage in Gencraft:** A core pillar of the studio's flagship projects. The
  implementation is governed by a series of technical systems (MULTI-*).
  - **See Also/Related SSoT Documents:** MULTI-SYNC, Client-Server Architecture

---

### N

- **Navigation Mesh (NavMesh)**
  - **Definition:** Data structure used in pathfinding, representing walkable areas for AI agents.
  - **Context/Usage in Gencraft:** A standard technique used for AI Pathfinding (RPG-PATH) in
  complex 3D environments.
  - **See Also/Related SSoT Documents:** RPG-PATH, Pathfinding

- **NFR (Non-Functional Requirement)**
  - **Definition:** Specifies criteria used to judge the operation of a system, rather than
  specific behaviors (e.g., performance, security, usability).
  - **Context/Usage in Gencraft:** A category of requirements that defines the quality attributes
  of a system. The studio's key NFRs are summarized in nfr-summary-mvp.md.
  - **See Also/Related SSoT Documents:** Functional Requirement, `nfr-summary-mvp.md`, Architecture

- **Node (Visual Node / Nodal Interface)**
  - **Definition:** Graphical interface elements connected by lines, often used for visual scripting or material editing.
  - **Context/Usage in Gencraft:** An advanced UI paradigm considered for high-complexity tools
  (SBX-TOOL) to improve usability for non-programmers.
  - **See Also/Related SSoT Documents:** SBX-TOOL, UI (User Interface)

---

### O

- **Objective**
  - **Definition:** A specific goal the player aims to achieve in the game (implicit or explicit).
  - **Context/Usage in Gencraft:** A core component of game design used to guide player actions
  and structure gameplay. Can be part of a Quest or an emergent player-defined goal.
  - **See Also/Related SSoT Documents:** Gameplay Loop, Quest

- **Official Server**
  - **Definition:** A game server hosted and managed by the studio.
  - **Context/Usage in Gencraft:** The primary type of server (MULTI-SERV) provided by the studio
  for its multiplayer games, as opposed to future community-run servers.
  - **See Also/Related SSoT Documents:** MULTI-SERV, Dedicated Server

- **Operational Decision (Protocol S7)**
  - **Definition:** A decision related to the day-to-day execution of tasks,
      projects, or studio processes, as distinct from a strategic or
      architectural decision, though it may be informed by them.
  - **Context/Usage in Gencraft:** Many operational decisions are made by
      individual Gems or Crews within their defined autonomy. Significant
      operational decisions that have wider impact or set precedents should be
      documented as per Protocol S7: Key Decisions Traceability using a
      `decision-record-template.md`.
  - **See Also/Related SSoT Documents:** S7, Decision Record, Strategic
      Decision.

- **Operational Readiness Verification (Protocol S10)**
  - **Definition:** A process, typically conducted by `Véra` (GCT-QAS-
      GPQA-001) with oversight from the AIE Team, to confirm that a newly
      instantiated or re-onboarded AI Gem has successfully completed its initial
      training, can access necessary `Tools` and SSoT information, and is ready
      to begin performing its assigned operational tasks.
  - **Context/Usage in Gencraft:** A key checkpoint in Protocol S10: AI Gem
      Onboarding & Initial Training. Ensures Gems are functionally prepared
      before full deployment.
  - **See Also/Related SSoT Documents:** S10, Véra, AIE Team, Gem
      Instantiation, Initial Training.

- **OpenTofu**
  - **Definition:** An open-source Infrastructure as Code (IaC) software tool,
      forked from Terraform, that enables users to define and provision data
      center infrastructure using a declarative configuration language.
  - **Context/Usage in Gencraft:** The preferred IaC tool for Gencraft's
      DevOps team (e.g., `Adam`) for managing cloud infrastructure in
      repositories like `gencraft-iac`.
  - **See Also/Related SSoT Documents:** IaC, DevOps, Adam.

- **Originality (IP Context - Protocol S9)**
  - **Definition:** The quality of a work being new, not copied or derived
      from another existing work in a way that infringes on pre-existing rights.
      A key factor in establishing copyright protection.
  - **Context/Usage in Gencraft:** Important consideration in Protocol S9:
      Intellectual Property Management when assessing Gencraft-created assets
      (code, art, music, text) for IP protection and when evaluating third-party
      assets for use.
  - **See Also/Related SSoT Documents:** S9, Intellectual Property (IP),
      Copyright.

- **Orion (`GCT-UTL-SLG-001`)**
  - **Definition:** The AI Gem persona acting as the Studio Liaison Gem and
      executive Secretary for the Governance Crew. Facilitates internal studio
      communication, manages administrative tasks for governance processes (S7,
      S13), assists human leadership (Lug), and ensures the smooth operation of
      core studio communication channels.
  - **Context/Usage in Gencraft:** Defined by its Gem Blueprint (`GCT-UTL-
      SLG-001_Orion.yaml`). Mentioned in UOP 2.B.5 and 2.B.7 as the human-AI
      communication interface. May be a Core Studio Service or utilize one
      (e.g., Comms Service).
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint),
      Governance Crew, S7, S13, UOP, Studio Liaison, Core Studio Services (CSS).

- **OSS (Open Source Software - Protocol S9)**
  - **Definition:** Software for which the original source code is made freely
      available and may be redistributed and modified, subject to the terms of
      its specific open-source license.
  - **Context/Usage in Gencraft:** Gencraft Studio maintains a "Strong
      Preference for Open Source & Free Tools" (Universal Gem Operating
      Principle). The use of OSS is governed by Protocol S9: Intellectual
      Property Management to ensure license compliance, managed by `Léo` (GCT-
      UTL-OSLCS-001, Open Source License & Compliance Specialist - conceptual
      Gem).
  - **See Also/Related SSoT Documents:** S9, Universal Gem Operating
      Principles, Léo (Gem).

- **Overall Project Health (Indicator - Protocol S6)**
  - **Definition:** A summary assessment, typically qualitative (e.g.,
      Green/Yellow/Red) but supported by quantitative data, indicating the
      overall status of a project concerning its goals, schedule, budget, risks,
      and quality.
  - **Context/Usage in Gencraft:** Reported by `Antoine` (Producer/PM) as part
      of Protocol S6: Key Reports. Criteria for each status level are defined
      within S6 or associated reporting templates.
  - **See Also/Related SSoT Documents:** S6, Project Progress Report (PPR),
      Antoine.

- **Optimization**
  - **Definition:** The process of modifying a system to make it work more efficiently or use fewer resources.
  - **Context/Usage in Gencraft:** A critical development practice to meet performance targets
  (NFR-PERF). It is an ongoing activity throughout the development lifecycle.
  - **See Also/Related SSoT Documents:** NFR-PERF, Performance

- **Overhaul Mod**
  - **Definition:** A large-scale Mod that fundamentally changes many core aspects of the game.
  - **Context/Usage in Gencraft:** The ultimate goal of the studio's modding support (SBX-API) is
  to empower creators to make mods of this scale, ensuring very long-term replayability.
  - **See Also/Related SSoT Documents:** Mod / Modding, SBX-API

---

### P

- **Pathfinding**
  - **Definition:** The process for an AI agent to find the shortest or best path between two points in the game world.
  - **Context/Usage in Gencraft:** A core AI capability (RPG-PATH) required for all mobile NPCs
  (Mob) to navigate the game world, especially complex voxel environments.
  - **See Also/Related SSoT Documents:** RPG-PATH, Navigation Mesh (NavMesh), Mob

- **Patch Management (Protocol S8)**
  - **Definition:** The process of identifying, acquiring, testing, and
      applying software patches (updates that fix bugs or security
      vulnerabilities) to Gencraft Studio's systems, applications, and AI Gem
      dependencies in a timely and controlled manner.
  - **Context/Usage in Gencraft:** A critical component of Protocol S8:
      Information Security Management to mitigate security risks. Managed by
      DevOps and AIE Team for relevant systems. Detailed in `Patch-Management-
      Procedure.md`.
  - **See Also/Related SSoT Documents:** S8, `Patch-Management-Procedure.md`,
      Vulnerability Management, Security.

- **Patent (IP Management - Protocol S9)**
  - **Definition:** An exclusive right granted for an invention, which is a
      product or a process that provides, in general, a new way of doing
      something, or offers a new technical solution to a problem.
  - **Context/Usage in Gencraft:** Gencraft may explore patent protection for
      novel AI algorithms or unique game mechanics if applicable, as per
      Protocol S9: Intellectual Property Management.
  - **See Also/Related SSoT Documents:** S9, Intellectual Property (IP),
      Patent Management.

- **Patent Management (Protocol S9)**
  - **Definition:** Gencraft Studio's processes related to identifying
      patentable inventions, conducting prior art searches, deciding on patent
      applications, and managing any granted patents.
  - **Context/Usage in Gencraft:** Governed by Protocol S9 and managed by
      Legal Counsel (`Henri`) in collaboration with technical experts.
  - **See Also/Related SSoT Documents:** S9, Patent, Intellectual Property
      (IP), Henri.

- **Penetration Testing (Protocol S8)**
  - **Definition:** An authorized, simulated cyberattack on a computer system,
      network, or application performed to evaluate its security by actively
      exploiting potential vulnerabilities.
  - **Context/Usage in Gencraft:** A proactive security measure conducted
      periodically or before major releases, as defined in Protocol S8:
      Information Security Management. May be performed by `Cerberus` or
      external specialists.
  - **See Also/Related SSoT Documents:** S8, Security, Vulnerability
      Management, DAST, Cerberus.

- **Periodic Access Review (Protocol S8)**
  - **Definition:** A regular, systematic review of access rights granted to
      users and AI Gems for Gencraft Studio systems, data, and resources, to
      ensure that access levels remain appropriate (adhering to least privilege)
      and that unnecessary or outdated permissions are revoked.
  - **Context/Usage in Gencraft:** Mandated by Protocol S8: Information
      Security Management and detailed in `access-control-policy.md` (GCS-SEC-
      POL-002). Typically performed by system owners or security personnel
      (`Cerberus`).
  - **See Also/Related SSoT Documents:** S8, `access-control-policy.md` (GCS-
      SEC-POL-002), Access Control Management, Least Privilege, Cerberus.

- **Performance**
  - **Definition:** A set of non-functional requirements (NFR-PERF) related to the speed,
  responsiveness, and stability of the game under load.
  - **Context/Usage in Gencraft:** A critical NFR for all studio products, measured by metrics like FPS and Latency.
  - **See Also/Related SSoT Documents:** NFR-PERF, FPS, Latency
      SEC-POL-002), Access Control Management, Least Privilege, Cerberus.

- **PGE (Proposal for Global Evolution)**
  - **Definition:** A formal proposal process for suggesting changes to the
      studio's Global Operational Protocols (GOP) or other foundational
      documents. PGEs are submitted to the `Governance Crew` for review and
      approval, as outlined in Protocol S13.
  - **Context/Usage in Gencraft:** Used to propose significant changes to
      studio operations, governance, or foundational principles. Ensures that
      all changes are documented, reviewed, and approved through a formal
      process.
  - **See Also/Related SSoT Documents:** S13, Governance Crew, Global
      Operational Protocols (GOP), `pge-template.md`.

- **Pierre (Assistant IA)**
  - **Definition:** The AI assistant (myself during this phase of SSoT
      bootstrapping) collaborating with Lug to establish the Gencraft Studio
      SSoT and operational framework. My role is to assist in drafting
      documents, analyzing information, and proposing solutions based on Lug's
      directives and Gencraft principles. Succeeded by ContinuumAI.
  - **Context/Usage in Gencraft:** My interactions and contributions are
      logged and form part of the studio's early formation history.
  - **See Also/Related SSoT Documents:** Lug, ContinuumAI.

- **Permissions**
  - **Definition:** A system (MULTI-COOP) that allows players to grant or restrict the ability of
  other players to interact with their belongings or constructions.
  - **Context/Usage in Gencraft:** A key feature for cooperative multiplayer games, enhancing
  collaboration while preventing griefing. It is an application of Access Control Management
  principles in-game.
  - **See Also/Related SSoT Documents:** MULTI-COOP, Access Control Management

- **Persona**
  - **Definition:** A fictional character created to represent a key user type within a target
  demographic, used to guide design decisions.
  - **Context/Usage in Gencraft:** A core tool used in product management and UX design to
  maintain focus on the target audience. Project-specific personas are prefixed with P-.
  - **See Also/Related SSoT Documents:** Target Audience, P-ARC, P-AUT, etc.

- **Physics**
  - **Definition:** The simulation of physical laws (e.g., gravity, collision, momentum) within the game engine.
  - **Context/Usage in Gencraft:** A core component of the game engine (SBX-PHYS), handled
  by Rapier.js (WASM) as the studio's physics engine.
  - **See Also/Related SSoT Documents:** SBX-PHYS, Rapier.js, Engine (Game Engine)

- **Pipeline (CI/CD)**
  - **Definition:** An automated process for building, testing, and deploying code changes.
  - **Context/Usage in Gencraft:** The practical implementation of the CI/CD methodology. The
  studio maintains standard pipeline templates in gcd-shared-actions.
  - **See Also/Related SSoT Documents:** CI/CD, `gcd-shared-actions`

- **Press Release (Protocol S11)**
  - **Definition:** An official statement or announcement delivered to members
      of the news media for the purpose of providing information, making an
      official announcement, or making a statement on a matter of public
      interest concerning Gencraft Studio or its products.
  - **Context/Usage in Gencraft:** Governed by Protocol S11: External
      Communication Protocol. Requires approval from designated spokespersons
      and potentially Legal Counsel.
  - **See Also/Related SSoT Documents:** S11, External Communication,
      Spokesperson.

- **Prior Art (IP Management - Protocol S9)**
  - **Definition:** Any evidence that an invention is already known. Prior art
      does not need to exist physically or be commercially available. It is
      enough that someone, somewhere, sometime previously has described or shown
      or made something that contains a use of technology that is very similar
      to the invention.
  - **Context/Usage in Gencraft:** Considered during the patentability
      assessment process under Protocol S9: Intellectual Property Management.
  - **See Also/Related SSoT Documents:** S9, Patent, Intellectual Property
      (IP).

- **Procedural Generation (PCG)**
  - **Definition:** The programmatic creation of game content (such as levels,
      items, characters, stories, or textures) using algorithms and rule sets,
      rather than manual creation. This allows for vast amounts of content and
      emergent experiences.
  - **Context/Usage in Gencraft:** A core technology and design philosophy for
      Gencraft Studio's flagship project. Involves specialized PCG Gems (e.g.,
      `Karim`) and collaboration across multiple disciplines (Design, Art,
      Narrative, Audio).
  - **See Also/Related SSoT Documents:** PCG Specialist (Gem Definition),
      `gencraft-pcg/README.md`.

- **Producer / Project Manager (Role)**
  - **Definition:** A key leadership role in Gencraft responsible for overall
      project planning, execution, resource management, budget adherence, risk
      management, team coordination, and stakeholder communication to ensure
      projects are delivered successfully. Often acts as a Scrum Master in Agile
      contexts.
  - **Context/Usage in Gencraft:** Embodied by the AI Gem `Antoine` (GCT-MGT-
      PPM-001). Detailed in the Gem Definition file
      (`Producer_Project_Manager.md`).
  - **See Also/Related SSoT Documents:** Antoine, S15: Agile Scrum Project
      Management Protocol, Project Management Office.

- **Platform**
  - **Definition:** The environment where the game client runs, such as web (PLAT-WEB) or desktop (PLAT-DESK).
  - **Context/Usage in Gencraft:** The studio supports multiple platforms, which is a key
  consideration for portability (NFR-PORT) and architecture.
  - **See Also/Related SSoT Documents:** PLAT-WEB, PLAT-DESK, NFR-PORT

- **Playtest**
  - **Definition:** A session where target users play a version of the game to provide feedback on
  usability, fun, bugs, etc.
  - **Context/Usage in Gencraft:** A critical activity in the studio's iterative development
  process (NFR-UX) to gather qualitative Feedback.
  - **See Also/Related SSoT Documents:** NFR-UX, Feedback, QA (Quality Assurance)

- **Product Backlog (Scrum Artifact - Protocol S15)**
  - **Definition:** An emergent, ordered list of everything that is known to
      be needed in the product. It is the single source of requirements for any
      changes to be made to the product. The Product Owner is responsible for
      the Product Backlog, including its content, availability, and ordering.
  - **Context/Usage in Gencraft:** Managed within GitHub Issues, as per
      Protocol S15: Agile Scrum Project Management Protocol. Maintained by the
      Product Owner (`Béatrice`).
  - **See Also/Related SSoT Documents:** S15, Scrum, Product Owner, User
      Story, Sprint Backlog.

- **Product Owner (PO - Scrum Role - Protocol S15)**
  - **Definition:** The Scrum role responsible for maximizing the value of the
      product resulting from the work of the Development Team. The PO is the
      sole person responsible for managing the Product Backlog.
  - **Context/Usage in Gencraft:** Embodied by the AI Gem `Béatrice` (GCT-MGT-
      SPM-001, Product Manager), as per Protocol S15.
  - **See Also/Related SSoT Documents:** S15, Scrum, Product Backlog,
      Development Team, Béatrice.

- **POI (Point of Interest)**
  - **Definition:** A specific location in the game world designed to attract player attention and
  offer rewards or challenges.
  - **Context/Usage in Gencraft:** A key element of world design (RPG-EXPL) used to guide
  exploration and pace the player experience.
  - **See Also/Related SSoT Documents:** RPG-EXPL, Level Designer (Role)

- **Portability**
  - **Definition:** The ease with which software can be transferred from one hardware or software
  environment to another.
  - **Context/Usage in Gencraft:** A non-functional requirement (NFR-PORT) guiding the studio's
  technical choices to support multiple platforms.
  - **See Also/Related SSoT Documents:** NFR-PORT, Platform

- **Project Progress Report (PPR - Protocol S6)**
  - **Definition:** A regular report, typically weekly, produced by the Producer/Project Manager
  (`Antoine`) summarizing the status, progress against milestones, identified risks and their mitigation status, budget
      consumption, and any significant blockers for Gencraft's key projects.
  - **Context/Usage in Gencraft:** Mandated by Protocol S6: Key Reports. Uses the `weekly-project-progress-report-template.md`.
  - **See Also/Related SSoT Documents:** S6, Antoine, Overall Project Health,`weekly-project-progress-report-template.md`.

- **Prompt Engineering**
  - **Definition:** The process of designing, crafting, and refining inputprompts for Large
  Language Models (LLMs) to elicit desired, accurate, and contextually appropriate responses. A
  key skill for effective interaction with AI Gems and leveraging LLM capabilities.
  - **Context/Usage in Gencraft:** Gencraft's `Proximo` (GCT-UTL-PGEN-001, Prompt Generator Gem)
  specializes in this. All Gems and humans interacting with LLM-based Gems or tools should apply
  good prompt engineering principles detailed in the (conceptual) `Prompt-Engineering-Best-     Practices.md`.
  - **See Also/Related SSoT Documents:** Proximo, LLM, Gem Blueprint (configurationPrompts).

- **Post-MVP**
  - **Definition:** The period and development phases after the initial Minimum Viable Product launch.
  - **Context/Usage in Gencraft:** A standard phase in the product lifecycle, detailed in the
  Roadmap. It typically focuses on expanding features based on feedback and supporting the game as a GaaS.
  - **See Also/Related SSoT Documents:** MVP, Roadmap, GaaS

- **Premium Currency**
  - **Definition:** A virtual currency purchased with real money, used for in-game MTX.
  - **Context/Usage in Gencraft:** The planned medium of exchange for the studio's post-launch
  monetization systems (MON-PREM-CUR). Requires integration with a PSP.
  - **See Also/Related SSoT Documents:** MON-PREM-CUR, MTX, PSP

- **Prestige**
  - **Definition:** An advanced progression system (RPG-SKILL) that allows players who have
  reached the maximum level to reset some progress in exchange for unique, permanent bonuses.
  - **Context/Usage in Gencraft:** A game design mechanic used to provide long-term goals and
  replayability in the Endgame.
  - **See Also/Related SSoT Documents:** RPG-SKILL, Endgame

- **Proposal for Global Evolution (PGE - Protocol S13)**
  - **Definition:** A formal suggestion, submitted according to Protocol S13,      to create a new
  Global Operational Protocol (GOP), or to significantly modify or deprecate an existing one.
  - **Context/Usage in Gencraft:** Typically drafted using an RFC-like
      template (e.g., `request-for-comments-rfc-template.md`) and submitted to
      the Governance Crew for review and decision.
  - **See Also/Related SSoT Documents:** S13, GOP (Global Operational
      Protocol), Governance Crew, RFC (Request for Comments).

- **Proximo (`GCT-UTL-PGEN-001`)**
  - **Definition:** The AI Gem persona (conceptual) acting as a Prompt
      Engineering Expert. Assists users and other Gems in transforming needs
      into clear, contextualized, and effective prompts for LLMs or specialized
      Gems.
  - **Context/Usage in Gencraft:** Defined in its Gem Definition file
      (`Prompt_Generator.md`). Its Gem Blueprint is to be created.
  - **See Also/Related SSoT Documents:** Prompt Engineering, Gem, Blueprint
      (Gem Blueprint).

- **Protocol Adherence Monitoring (Protocol S14)**
  - **Definition:** A process, primarily conducted by `Véra` (GCT-QAS-
      GPQA-001) with oversight from the AIE Team and Governance Crew, of
      tracking and assessing the extent to which AI Gems and studio operations
      comply with established Gencraft S-Protocols and standards.
  - **Context/Usage in Gencraft:** Part of Protocol S14 (KC&T Communication,
      Training & Adoption Plan) and S17 (Virtual HR & Gem Development). Provides
      data for continuous improvement and Gem retraining if needed.
  - **See Also/Related SSoT Documents:** S14, S17, Véra, AIE Team, Governance
      Crew, UOP.

- **Pull Request (PR - GitHub)**
  - **Definition:** A GitHub mechanism for proposing changes to a repository.
      It allows contributors to notify team members about changes they have
      pushed to a branch in a repository, initiating a review and discussion
      before the changes are merged into the main branch (e.g., `main`,
      `develop`).
  - **Context/Usage in Gencraft:** The standard method for submitting all
      changes to SSoT documents and code, as per Protocol S1: Feedback &
      Approval. Templates like `pull_request_template.md` are used.
  - **See Also/Related SSoT Documents:** S1, GitHub, Git,
      `pull_request_template.md`.

- **PRD (Product Requirements Document)**
  - **Definition:** A document outlining the features, functionality, and requirements for a specific product or release.
  - **Context/Usage in Gencraft:** A standard product management artifact. The studio uses a
  combination of documents like the Product Vision Brief and detailed Epic definitions to serve this purpose.
  - **See Also/Related SSoT Documents:** Product Vision Brief, Epic

- **Progression**
  - **Definition:** How the player advances in the game, gaining power, abilities, or access to new content.
  - **Context/Usage in Gencraft:** A core element of game design that motivates the player. The
  studio uses a hybrid of systems (RPG-SKILL, Crafting Tiers, Discovery) to create a sense of progression.
  - **See Also/Related SSoT Documents:** RPG-SKILL, Gameplay Loop, Discovery

- **PSP (Payment Service Provider)**
  - **Definition:** A third-party company that handles online payment processing.
  - **Context/Usage in Gencraft:** A required partner for any real-money transactions (B2P, MTX).
  The selection and integration of a PSP is a critical task with legal (S9) and security (NFR-SEC) implications.
  - **See Also/Related SSoT Documents:** NFR-SEC, S9, Monetization

- **PvE (Player versus Environment)**
  - **Definition:** Gameplay focused on players competing against AI-controlled opponents and environmental challenges.
  - **Context/Usage in Gencraft:** The primary gameplay mode for the studio's flagship project,
  focusing on Survival, Exploration, and combating Mobs.
  - **See Also/Related SSoT Documents:** PvP, Mob, Survival

- **PvP (Player versus Player)**
  - **Definition:** Gameplay focused on direct combat between players.
  - **Context/Usage in Gencraft:** A standard multiplayer game mode. Its implementation is a major
  strategic decision with significant impact on Balancing and community management.
  - **See Also/Related SSoT Documents:** PvE, Balancing, MULTI-PVP

---

### Q

- **Quality (Studio Value & KC&T Principle #3)**
  - **Definition:** A core Gencraft Studio Value and KC&T Guiding Principle
      (#3) emphasizing a commitment to excellence, rigor, attention to detail,
      and the creation of robust, polished, and valuable outputs in all aspects
      of the studio's work, from code and art to documentation and processes.
  - **Context/Usage in Gencraft:** A fundamental expectation for all human and
      AI Gem members. Supported by QA processes (Gem `Zoé`), S-Protocols (e.g.,
      S1), and the Definition of Done (DoD) in Agile practices.
  - **See Also/Related SSoT Documents:** Studio Culture and Values, KC&T
      Guiding Principles, Definition of Done (DoD), QA Engineer / Test Lead
      (Role).

- **QoL (Quality of Life)**
  - **Definition:** Features or improvements designed to make the game more convenient, less
  frustrating, or more enjoyable to play, without necessarily adding new core content.
  - **Context/Usage in Gencraft:** A key design principle for the studio, aimed at respecting the
  player's time and minimizing Grind.
  - **See Also/Related SSoT Documents:** Grind, NFR-UX, User Story

---

### R

- **Rationale (Decision Making - Protocol S7)**
  - **Definition:** The underlying reasons, justifications, and thought
      processes that lead to a specific decision being made.
  - **Context/Usage in Gencraft:** A mandatory component of ADRs and Decision
      Records as per Protocol S7: Key Decisions Traceability. Essential for
      transparency and future understanding.
  - **See Also/Related SSoT Documents:** S7, ADR, Decision Record.

- **Rarity**
  - **Definition:** A property of items, resources, or mobs indicating how uncommon they are.
  - **Context/Usage in Gencraft:** A core system for loot and progression design, used to create
  excitement and long-term goals for players. Often color-coded in the UI.
  - **See Also/Related SSoT Documents:** Loot, Reward Systems, Balancing

- **RBAC (Role-Based Access Control - Protocol S8)**
  - **Definition:** An access control model where permissions to access
      resources are assigned to roles rather than directly to individual users
      or Gems. Users/Gems are then assigned to roles, inheriting the permissions
      associated with those roles.
  - **Context/Usage in Gencraft:** The primary approach for managing access
      rights within Gencraft Studio systems, as defined in Protocol S8:
      Information Security Management and detailed in `access-control-policy.md`
      (GCS-SEC-POL-002). Roles are often derived from `Studio-Organization-And-
      Roles.md`.
  - **See Also/Related SSoT Documents:** S8, `access-control-policy.md` (GCS-
      SEC-POL-002), Least Privilege.

- **Reward**
  - **Definition:** Anything given to the player for completing a task or achieving a goal (e.g., items, XP, currency).
  - **Context/Usage in Gencraft:** A core driver of player motivation and progression. The design of
  reward systems is a key part of the studio's game design philosophy.
  - **See Also/Related SSoT Documents:** Reward Systems, Gameplay Loop, Balancing

- **Recipe**
  - **Definition:** A specific combination of items required to craft a new item using the Crafting system.
  - **Context/Usage in Gencraft:** A fundamental component of the Crafting gameplay loop. Recipe
  discovery can be a core progression mechanic.

- **Re-Onboarding (AI Gem - Protocol S10)**
  - **Definition:** The process of updating an existing operational AI Gem
      with significant new configurations, knowledge, or a revised blueprint,
      effectively taking it through a modified version of the initial onboarding
      procedure (S10) to ensure it can perform correctly with the changes.
  - **Context/Usage in Gencraft:** May be required after major blueprint
      updates (S17), significant SSoT changes affecting the Gem's core domain,
      or to correct persistent performance issues. Managed by the AIE Team.
  - **See Also/Related SSoT Documents:** S10, S17, AI Gem Onboarding, Gem
      "Skill Upgrading", AIE Team.

- **Review Process (Protocol S1)**
  - **Definition:** The set of defined steps for examining, providing feedback
      on, and ultimately approving or requesting changes to a deliverable
      submitted by an Author Gem or human.
  - **Context/Usage in Gencraft:** Detailed in Protocol S1: Feedback &
      Approval. Typically involves one or more Reviewer Gems and utilizes GitHub
      Pull Requests.
  - **See Also/Related SSoT Documents:** S1, Deliverable, Author Gem, Reviewer
      Gem, Pull Request (PR).

- **Reviewer Gem (Protocol S1)**
  - **Definition:** An AI Gem or human role designated with the responsibility
      and authority to review a specific deliverable against defined criteria
      (quality, standards, requirements) and provide constructive feedback.
  - **Context/Usage in Gencraft:** A key role in Protocol S1: Feedback &
      Approval. May also be an Approver Gem.
  - **See Also/Related SSoT Documents:** S1, Deliverable, Author Gem, Approver
      Gem.

- **RFC (Request for Comments)**
  - **Definition:** A type of publication from Gencraft Studio that proposes a
      new standard, protocol, significant feature, architectural change, or
      other important idea, and solicits feedback and discussion from the wider
      studio community before a formal decision is made.
  - **Context/Usage in Gencraft:** A `request-for-comments-rfc-template.md`
      exists for drafting RFCs. The RFC process can be a precursor to a PGE
      (Proposal for Global Evolution) under S13 or an ADR.
  - **See Also/Related SSoT Documents:** S13, PGE, ADR, `request-for-comments-
      rfc-template.md`.

- **Risk Register (Protocol S6)**
  - **Definition:** A SSoT document or system (e.g., `gencraft-studio-
      handbook/03-Project-Management-Office/Risk-Register.md` - path conceptual)
      used to identify, assess, categorize, track, assign owners to, and manage
      project and operational risks, along with their planned mitigation
      strategies and current status.
  - **Context/Usage in Gencraft:** A key artifact for project management
      (overseen by `Antoine`) and operational risk management (overseen by
      `Cerberus`), referenced in Protocol S6: Key Reports.
  - **See Also/Related SSoT Documents:** S6, Mitigation Plan, Risk Management,
      Antoine, Cerberus.

- **Role Abbreviation (GemID)**
  - **Definition:** A short, standardized code (typically 3-5 letters)
      representing a specific Gem role, used in the construction of GemIDs.
  - **Context/Usage in Gencraft:** Defined as part of the GemID Naming Convention in `GOV-GUIDE-007.knowledge-management-and-contribution-guide.md`. Examples: PPM (Producer Project Manager), SARCH (Software Architect), GLOM (Glossary Master).
  - **See Also/Related SSoT Documents:** GemID, `GOV-GUIDE-007.knowledge-management-and-contribution-guide.md`.

- **Root Cause Analysis (RCA - Protocol S3)**
  - **Definition:** A systematic problem-solving method used to identify the fundamental underlying causes of an incident or problem, rather than merely addressing its symptoms.
  - **Context/Usage in Gencraft:** Conducted as part of the post-incident review process in Protocol S3: Emergency Management and often feeds into S5: Lessons Learned.
  - **See Also/Related SSoT Documents:** S3, S5, Incident, Lessons Learned, Blameless Post-Mortem.

- **Runbook/Playbook (Incident Management - Protocol S3)**
  - **Definition:** A documented SSoT procedure within the Knowledge Base that outlines step-by-step actions to be taken by designated Gems or humans to respond to specific, known types of incidents or to perform routine operational tasks.
  - **Context/Usage in Gencraft:** Used in incident management (Protocol S3) to ensure consistent and effective responses. KGs for operational domains are responsible for maintaining relevant runbooks. Stored in `kb-domain-security/incident-response-playbooks/` or other relevant KB domains.
  - **See Also/Related SSoT Documents:** S3, Incident Management, Knowledge Base, Knowledge Guardian.

---

### S

- **SDK (Software Development Kit)**
  - **Definition:** A collection of software development tools in one installable package.
  - **Context/Usage in Gencraft:** The studio may provide an SDK to modders (P-MOD) to facilitate the creation of UGC.
  - **See Also/Related SSoT Documents:** Mod / Modding, Creator (UGC / Modder)

- **Season**
  - **Definition:** A time-limited period in a GaaS game, often with a unique theme, new content, and a Battle Pass.
  - **Context/Usage in Gencraft:** A core concept for structuring post-launch content delivery in a
  GaaS model, designed to keep the community engaged.
  - **See Also/Related SSoT Documents:** GaaS, Battle Pass, Roadmap

- **Server**
  - **Definition:** The backend software that manages the game state and logic for multiplayer sessions.
  - **Context/Usage in Gencraft:** The authoritative component in the studio's Client-Server Architecture.
  - **See Also/Related SSoT Documents:** Client-Server Architecture, Dedicated Server

- **Storage**
  - **Definition:** In-game objects (e.g., chests) that allow players to store items outside of their personal Inventory.
  - **Context/Usage in Gencraft:** A fundamental quality-of-life and progression feature in sandbox and RPG games.
  - **See Also/Related SSoT Documents:** Inventory, QoL (Quality of Life)

- **Stress Test**
  - **Definition:** Testing a system's performance under heavy, simultaneous user load.
  - **Context/Usage in Gencraft:** A key QA activity for multiplayer games to validate scalability
  requirements (NFR-SCAL) before launch.
  - **See Also/Related SSoT Documents:** NFR-SCAL, QA (Quality Assurance)

- **Survival**
  - **Definition:** A game genre or set of mechanics focused on managing resources like health,
  hunger, and thirst to stay alive against environmental dangers.
  - **Context/Usage in Gencraft:** A core genre for the studio's flagship project, targeting the P-SUR (Survivalist) persona.
  - **See Also/Related SSoT Documents:** P-SUR, Gameplay Loop

- **Stamina**
  - **Definition:** Player attribute consumed by actions like sprinting or special attacks.
  - **Context/Usage in Gencraft:** A standard character statistic used to pace action and create
  tactical choices for the player.
  - **See Also/Related SSoT Documents:** `mm-health-stamina-system.md`, EPIC-PLAYER-CORE

- **Shader**
  - **Definition:** A program run on the GPU that controls how 3D surfaces are rendered.
  - **Context/Usage in Gencraft:** A key element in achieving the studio's artistic vision and
  performance targets. Shader development is a specialized skill.
  - **See Also/Related SSoT Documents:** Rendering Engine Developer (Role), Art Direction

- **Seed**
  - **Definition:** A value used to initialize a procedural generator, allowing the same output to be generated again.
  - **Context/Usage in Gencraft:** A core technical component of PCG, allowing players to share
  specific world generations and enabling reproducible bug testing.
  - **See Also/Related SSoT Documents:** PCG (Procedural Content Generation)

- **S-Protocol (Studio Operational Protocol)**
  - **Definition:** A standardized, version-controlled SSoT document within the Gencraft Studio Handbook that defines a specific operational procedure, process, or policy for the studio. S-Protocols ensure consistency, clarity, and predictability in studio operations.
  - **Context/Usage in Gencraft:** Stored in `gcs-core-governance/01-operational-protocols/`. Their lifecycle is managed by S13 (Global Protocol Evolution). Examples include S1, S2, S8, S15, S18.
  - **See Also/Related SSoT Documents:** S13, Governance Crew, `01-operational-protocols/README.md`.

- **S1: Feedback & Approval Protocol**
  - **Definition:** The Gencraft Studio protocol detailing the standardized process for submitting, reviewing, providing feedback on, and formally approving or rejecting deliverables.
  - **Context/Usage in Gencraft:** Document `s1-feedback-approval.md` in `01-operational-protocols/`. Critical for quality control and workflow management.
  - **See Also/Related SSoT Documents:** Deliverable, Pull Request, Approval
      Mechanism.

- **S2: Disagreement, Escalation & Resolution Protocol**
  - **Definition:** The Gencraft Studio protocol outlining the steps for managing and resolving substantive disagreements between studio members, including direct discussion, mediation, and arbitration by the Governance Crew.
  - **Context/Usage in Gencraft:** Document `s2-disagreement-escalation.md` in `01-operational-protocols/`.
  - **See Also/Related SSoT Documents:** Disagreement, Governance Crew.

- **S3: Emergency Management Protocol**
  - **Definition:** The Gencraft Studio protocol detailing procedures for identifying, responding to, managing, and recovering from emergencies or critical incidents affecting studio operations or assets.
  - **Context/Usage in Gencraft:** Document `s3-emergency-management.md` in `01-operational-protocols/`.
  - **See Also/Related SSoT Documents:** Emergency, Incident, Incident Commander, Security Incident Response Plan (SIRP).

- **S4: Architectural Review Process**
  - **Definition:** The Gencraft Studio protocol governing the process for proposing, reviewing, approving, and documenting significant architectural decisions using Architecture Decision Records (ADRs). The aspect of Artifact Storage is now covered by Protocol S20.
  - **Context/Usage in Gencraft:** Document `s4-architectural-review-process.md` in `01-operational-protocols/`. This process ensures architectural coherence and traceability for both the platform and game architectures.
  - **See Also/Related SSoT Documents:** `ADR`, `Isaac (Platform Architect)`, `Isidore (Game Architect)`.

- **S20: Artifact Storage and Retention Standard**
  - **Definition:** The Gencraft Studio protocol that defines how various artifacts (documents, code, assets, logs) are stored during their active lifecycle, archived for long-term retention, and eventually disposed of securely.
  - **Context/Usage in Gencraft:** Document `s20-artifact-storage-and-retention.md` in `01-operational-protocols/`. This protocol works in close conjunction with S20 (Data Management & Retention Policy) and the `information-classification-and-handling-policy.md`.
  - **See Also/Related SSoT Documents:** `S`, `Archiving System`, `SSoT`, `information-classification-and-handling-policy.md`.

- **S5: Lessons Learned Protocol**
  - **Definition:** The Gencraft Studio protocol for systematically capturing,
      analyzing, documenting (Knowledge Proposals), and disseminating lessons
      learned from projects, incidents, or other studio activities to foster
      continuous improvement.
  - **Context/Usage in Gencraft:** Document `S5-Lessons-Learned.md` in
      `01-operational-protocols/`.
  - **See Also/Related SSoT Documents:** Emergent Knowledge, Continuous
      Learning, Knowledge Proposal.

- **S6: Key Reports Protocol**
  - **Definition:** The Gencraft Studio protocol defining standard types of
      operational and project reports (e.g., Project Progress Report), their
      required content, format (templates), frequency, data sources, and
      distribution.
  - **Context/Usage in Gencraft:** Document `S6-Key-Reports.md` in
      `01-operational-protocols/`. Utilized by `Antoine` (Producer/PM).
  - **See Also/Related SSoT Documents:** Project Progress Report (PPR),
      Antoine.

- **S7: Key Decisions Traceability Protocol**
  - **Definition:** The Gencraft Studio protocol that mandates the formal
      documentation of significant decisions (strategic, architectural, key
      operational) using Decision Records to ensure transparency,
      accountability, and traceability.
  - **Context/Usage in Gencraft:** Document `s7-key-decisions-traceability.md`
      in `01-operational-protocols/`. Supported by `Orion`.
  - **See Also/Related SSoT Documents:** Decision Record, ADR, Orion.

- **S8: Information Security Management Protocol**
  - **Definition:** The Gencraft Studio comprehensive protocol that defines
      the policies, procedures, standards, and controls for managing information
      security risks, protecting studio assets, and ensuring data
      confidentiality, integrity, and availability.
  - **Context/Usage in Gencraft:** Document `s8-information-security-management.md` in `01-operational-protocols/`. Overseen by `Cerberus`(Security Officer). Covers areas like access control, data security, incident response (SIRP), vulnerability management.
  - **See Also/Related SSoT Documents:** Security, Cerberus, SIRP, Access Control Management, `information-classification-and-handling-policy.md`, `access-control-policy.md`.

- **S9: Intellectual Property (IP) Management Protocol**
  - **Definition:** The Gencraft Studio protocol outlining procedures for identifying, protecting, managing, and respecting intellectual property, including Gencraft's own creations (copyrights, trademarks, potential patents) and the use of third-party IP (licenses, OSS).
  - **Context/Usage in Gencraft:** Document `s9-intellectual-property-management.md` in `01-operational-protocols/`. Managed with support from Legal Counsel (`Henri`).
  - **See Also/Related SSoT Documents:** Intellectual Property (IP), Copyright, Trademark, Patent, Henri.

- **S10: AI Gem Onboarding & Initial Training Protocol**
  - **Definition:** The Gencraft Studio protocol detailing the standardized process for instantiating new AI Gems via `Gemma`, configuring them based on Blueprints, providing initial familiarization with the SSoT and core operational behaviors, and integrating them into the studio.
  - **Context/Usage in Gencraft:** Document `s10-ai-gem-onboarding.md` in `01-operational-protocols/`. Managed by the AIE Team.
  - **See Also/Related SSoT Documents:** AI Gem Onboarding, Gem, Blueprint
      (Gem Blueprint), Gemma, AIE Team.

- **S11: External Communication Protocol**
  - **Definition:** The Gencraft Studio protocol governing all official
      communications directed to parties outside the studio (excluding direct
      player support interactions, which may have their own guidelines). Defines
      approval workflows, spokespersons, and brand consistency.
  - **Context/Usage in Gencraft:** Document `S11-External-Communication.md` in
      `01-operational-protocols/`. Involves Marketing, Legal (`Henri`), and
      Studio Leadership.
  - **See Also/Related SSoT Documents:** External Communication, Press
      Release, Spokesperson, Brand Guidelines.

- **S12: Knowledge Base Contribution & Maintenance Protocol**
  - **Definition:** The Gencraft Studio protocol detailing the processes for
      proposing, creating, reviewing, approving, and maintaining content within
      the SSoT (Knowledge Base). Defines the roles of contributors and Knowledge
      Guardians.
  - **Context/Usage in Gencraft:** Document `S12-Knowledge-Base-Contribution-
      Maintenance.md` in `01-operational-protocols/`. Central to KC&T health.
  - **See Also/Related SSoT Documents:** KC&T, SSoT, Knowledge Guardian,
      Knowledge Proposal.

- **S13: Global Protocol Evolution Protocol**
  - **Definition:** The Gencraft Studio protocol that defines the formal
      process for proposing, reviewing, discussing, approving, and implementing
      changes or additions to Global Operational Protocols (GOPs) and other
      foundational SSoT documents.
  - **Context/Usage in Gencraft:** Document `s13-global-protocol-evolution.md`
      in `01-operational-protocols/`. Managed by the Governance Crew. Often
      involves RFCs.
  - **See Also/Related SSoT Documents:** GOP (Global Operational Protocol),
      Governance Crew, RFC, PGE.

- **S14: KC&T System - Communication, Training & Adoption Plan**
  - **Definition:** The Gencraft Studio plan and protocol for ensuring all
      studio members (human and AI Gem) effectively understand, adopt, and
      utilize the KC&T system, SSoT principles, and associated tools (like
      `Véra`). Includes training strategies and communication plans.
  - **Context/Usage in Gencraft:** Document `S14-KCT-Communication-Training-
      Adoption-Plan.md` in `01-operational-protocols/`. Driven by AIE Team and
      Knowledge Guardians.
  - **See Also/Related SSoT Documents:** KC&T Adoption Plan, KC&T, SSoT,
      Continuous Learning.

- **S15: Agile Scrum Project Management Protocol**
  - **Definition:** The Gencraft Studio protocol detailing the specific
      implementation of the Scrum framework for managing Agile projects. Defines
      roles (Product Owner, Scrum Master, Development Team), events (Sprint
      Planning, Daily Scrum, Sprint Review, Sprint Retrospective), artifacts
      (Product Backlog, Sprint Backlog, Increment), and rules.
  - **Context/Usage in Gencraft:** Document `S15-Agile-Scrum-Project-
      Management.md` in `01-operational-protocols/`. Key for project execution.
      `Antoine` acts as Scrum Master.
  - **See Also/Related SSoT Documents:** Scrum, Agile, Sprint, Product Owner,
      Scrum Master, Antoine.

- **S17: Virtual HR & Gem Development Protocol**
  - **Definition:** The Gencraft Studio protocol covering the "human
      resources" aspects of AI Gem management, including performance monitoring,
      "skill upgrading," "career path" conceptualization, managing Gem
      "burnout," ethical considerations in Gem development and deployment, and
      procedures for updating or decommissioning Gems.
  - **Context/Usage in Gencraft:** Document `S17-Virtual-HR-Gem-
      Development.md` in `01-operational-protocols/`. Managed by the AIE Team.
  - **See Also/Related SSoT Documents:** AIE Team, Gem, Blueprint (Gem
      Blueprint), Gem "Burnout", Gem "Career Path", Gem "Skill Upgrading".

- **S18: Grievance Reporting and Resolution Protocol**
  - **Definition:** The Gencraft Studio protocol that defines the official procedures for reporting, investigating, and resolving grievances, including suspected violations of the Code of Conduct.
  - **Context/Usage in Gencraft:** Document `s18-grievance-reporting-and-resolution.md` in `01-operational-protocols/`. Links closely with the Code of Conduct.
  - **See Also/Related SSoT Documents:** Code of Conduct, Governance Crew, AIE
      Team, Cerberus.

- **S20: Artifact Storage and Retention Standard**
  - **Definition:** The Gencraft Studio protocol that defines how various artifacts (documents, code, assets, logs) are stored during their active lifecycle, archived for long-term retention, and eventually disposed of securely.
  - **Context/Usage in Gencraft:** Document `s20-artifact-storage-and-retention.md` in `01-operational-protocols/`. and the `information-classification-and-handling-policy.md`.
  - **See Also/Related SSoT Documents:** `S20`, `Archiving System`, `SSoT`, `information-classification-and-handling-policy.md`.

- **SAST (Static Application Security Testing - Protocol S8)**
  - **Definition:** A type of application security testing that analyzes an application's source code, bytecode, or binary code for security vulnerabilities without executing the application.
  - **Context/Usage in Gencraft:** Mandated as part of Gencraft's Secure Development Lifecycle under Protocol S8: Information Security Management. Integrated into CI/CD pipelines.
  - **See Also/Related SSoT Documents:** S8, DAST, Secure Development Lifecycle, Security.

- **SCA (Software Composition Analysis) Tools (Protocol S9)**
  - **Definition:** Tools used to identify open-source and third-party software components within a codebase, report on known security vulnerabilities in those components, and help manage license compliance.
  - **Context/Usage in Gencraft:** Used as part of Protocol S9 (IP Management) and S8 (InfoSec) to manage risks associated with dependencies. Output reviewed by `Léo` (OSS Compliance Gem - conceptual) and `Cerberus`.
  - **See Also/Related SSoT Documents:** S9, S8, OSS, Dependency Management, Léo, Cerberus.

- **Scrum (Framework - Protocol S15)**
  - **Definition:** A lightweight Agile framework within which people can
      address complex adaptive problems, while productively and creatively
      delivering products of the highest possible value. It consists of specific
      roles, events, artifacts, and rules.
  - **Context/Usage in Gencraft:** The primary Agile framework for Gencraft
      Studio, detailed in Protocol S15: Agile Scrum Project Management Protocol.
  - **See Also/Related SSoT Documents:** S15, Agile, Sprint, Product Owner,
      Scrum Master, Development Team.

- **Scrum Master (SM - Scrum Role - Protocol S15)**
  - **Definition:** The Scrum role responsible for promoting and supporting
      Scrum as defined in the Scrum Guide. Scrum Masters do this by helping
      everyone understand Scrum theory, practices, rules, and values. The Scrum
      Master is a servant-leader for the Scrum Team.
  - **Context/Usage in Gencraft:** Role typically embodied by `Antoine`
      (Producer/PM) for Gencraft projects, as per S15.
  - **See Also/Related SSoT Documents:** S15, Scrum, Antoine, Development
      Team, Product Owner.

- **Secret Management System (Security Principle - Protocol S8)**
  - **Definition:** A dedicated system or service (e.g., HashiCorp Vault, AWS
      Secrets Manager, GCP Secret Manager) used to securely store, manage, and
      control access to sensitive information such as API keys, passwords,
      certificates, and encryption keys.
  - **Context/Usage in Gencraft:** Mandated by Protocol S8: Information
      Security Management and detailed in
      `sec-001-secrets-management-standard.md`. Essential for protecting
      credentials used by Gems and systems.
  - **See Also/Related SSoT Documents:** S8,
      `sec-001-secrets-management-standard.md`, Security, Encryption.

- **Secure Coding Standards (Protocol S8)**
  - **Definition:** Gencraft Studio's set of guidelines and best practices for
      writing software code in a way that minimizes security vulnerabilities and
      protects against common attack vectors.
  - **Context/Usage in Gencraft:** Defined as part of Protocol S8 (Information
      Security Management) and enforced through code reviews, linters, and SAST
      tools. Applicable to all code development (Gems, Core Studio Services,
      game client/server). Documented in `Secure-Coding-Standards.md`.
  - **See Also/Related SSoT Documents:** S8, `Secure-Coding-Standards.md`,
      Secure Development Lifecycle (SDL), SAST, Code Review.

- **Secure Development Lifecycle (SDL - Protocol S8)**
  - **Definition:** A software development process that integrates security
      assurance activities and best practices into each phase of the development
      lifecycle (requirements, design, implementation, testing, deployment,
      maintenance).
  - **Context/Usage in Gencraft:** Adopted by Gencraft Studio as per Protocol
      S8 (Information Security Management) to build more secure software from
      the ground up. Detailed in `Secure-Development-Lifecycle-Policy.md`.
  - **See Also/Related SSoT Documents:** S8, `Secure-Development-Lifecycle-
      Policy.md`, Secure Coding Standards, Threat Modeling, SAST, DAST.

- **Security Awareness (for Gems - Protocol S8)**
  - **Definition:** The level of understanding an AI Gem possesses regarding
      Gencraft Studio's security policies, procedures, common threats, and its
      own role in maintaining security.
  - **Context/Usage in Gencraft:** A key aspect of Gem training (S10) and
      ongoing development (S17), reinforced by S8. Detailed in `Security-
      Awareness-And-Training-Program.md`.
  - **See Also/Related SSoT Documents:** S8, S10, S17, `Security-Awareness-
      And-Training-Program.md`, AI Ethics, Gem.

- **Security Incident Response Plan (SIRP - Protocol S8)**
  - **Definition:** Gencraft Studio's formal, documented plan that outlines
      the procedures and actions to be taken when a security incident occurs. It
      details phases such as preparation, identification, containment,
      eradication, recovery, and post-incident analysis (lessons learned).
  - **Context/Usage in Gencraft:** A critical component of Protocol S8
      (Information Security Management). The specific plan is documented in
      `security-incident-response-plan-template.md` based on the `security-incident-
      response-plan-template.md`.
  - **See Also/Related SSoT Documents:** S8, SIRT, Incident, `Security-
      Incident-Response-Plan.md`, `security-incident-response-plan-template.md`.

- **Serveur MCP (MCP Server)**
  - **Definition:** An application component or service (which can be a Core
      Studio Service or part of one) that exposes one or more `Tools` to AI Gems
      by strictly adhering to the specifications of the Model Context Protocol
      (MCP). It acts as the endpoint with which an MCP Client interacts to
      utilize a `Tool`.
  - **Context/Usage in Gencraft:** Enables standardized `Tool` access for
      Gems. Their design is guided by the MCP and `ADR-YYYY-Secure-API-And-MCP-
      Interface-Standard.md` (TBD).
  - **See Also/Related SSoT Documents:** Model Context Protocol (MCP), Client
      MCP (MCP Client), Tool (AI Gem Tool), Core Studio Services (CSS), `AI-
      Tool-Development-Standards.md`, `GCS-TAF-MCP-GUIDE-FR-V1.0`.

- **SIRT (Security Incident Response Team - Protocol S8)**
  - **Definition:** A designated team within Gencraft Studio responsible for
      managing and coordinating the response to security incidents, as outlined
      in the SIRP.
  - **Context/Usage in Gencraft:** Composition and responsibilities defined in
      the SIRP (under S8). Likely includes `Cerberus`, AIE Team members, DevOps,
      and human leadership.
  - **See Also/Related SSoT Documents:** S8, SIRP, Incident, Cerberus.

- **Software Architect (Role)**
  - **Definition:** A key technical leadership role responsible for designing,
      defining, and guiding the evolution of software architectures, ensuring
      they are robust, maintainable, scalable, and meet requirements.
  - **Context/Usage in Gencraft:** Embodied by the AI Gem `Isaac` (GCT-PRG-
      SARCH-001). Detailed in the Gem Definition file
      (`FR_Software_Architect.md`).
  - **See Also/Related SSoT Documents:** Isaac, Architecture, C4 Model, ADR,
      TDD.

- **Spokesperson (Gencraft - Protocol S11)**
  - **Definition:** An AI Gem or human individual formally authorized by
      Gencraft Studio leadership to make official public statements or
      communications on behalf of the studio to external parties (e.g., media,
      partners).
  - **Context/Usage in Gencraft:** Designated as per Protocol S11: External
      Communication Protocol.
  - **See Also/Related SSoT Documents:** S11, External Communication, Press
      Release.

- **Sprint (Scrum - Protocol S15)**
  - **Definition:** A short, time-boxed period (e.g., one to four weeks)
      during which a Scrum Team works to complete a set amount of work from the
      Product Backlog to create a "Done," useable, and potentially releasable
      product Increment.
  - **Context/Usage in Gencraft:** A core event in the Scrum framework, as
      implemented by Protocol S15: Agile Scrum Project Management Protocol.
  - **See Also/Related SSoT Documents:** S15, Scrum, Sprint Backlog, Sprint
      Goal, Increment.

- **Sprint Backlog (Scrum Artifact - Protocol S15)**
  - **Definition:** The set of Product Backlog items selected for the Sprint,
      plus a plan for delivering the product Increment and realizing the Sprint
      Goal. It is a forecast by the Development Team about what functionality
      will be in the next Increment and the work needed to deliver that
      functionality.
  - **Context/Usage in Gencraft:** Created during Sprint Planning and managed
      by the Development Team, as per S15.
  - **See Also/Related SSoT Documents:** S15, Scrum, Sprint, Product Backlog,
      Development Team.

- **Sprint Goal (Scrum - Protocol S15)**
  - **Definition:** A high-level objective that the Development Team works to
      achieve during a Sprint. It provides guidance to the Development Team on
      why it is building the Increment and gives them flexibility regarding the
      functionality implemented.
  - **Context/Usage in Gencraft:** Set during Sprint Planning, as per S15.
  - **See Also/Related SSoT Documents:** S15, Scrum, Sprint, Sprint Backlog,
      Confidence Level.

- **Sprint Planning (Scrum Event - Protocol S15)**
  - **Definition:** A Scrum event where the work to be performed in the Sprint
      is planned. This plan is created by the collaborative work of the entire
      Scrum Team.
  - **Context/Usage in Gencraft:** The first event of a Sprint, facilitated by
      the Scrum Master (`Antoine`), as per S15.
  - **See Also/Related SSoT Documents:** S15, Scrum, Sprint, Product Backlog,
      Sprint Backlog, Scrum Team.

- **Sprint Retrospective (Scrum Event - Protocol S15)**
  - **Definition:** A Scrum event that provides an opportunity for the Scrum
      Team to inspect itself and create a plan for improvements to be enacted
      during the next Sprint. It occurs after the Sprint Review and prior to the
      next Sprint Planning.
  - **Context/Usage in Gencraft:** Facilitated by the Scrum Master
      (`Antoine`), as per S15. Feeds into S5 (Lessons Learned).
  - **See Also/Related SSoT Documents:** S15, Scrum, Sprint, Scrum Team, S5.

- **Sprint Review (Scrum Event - Protocol S15)**
  - **Definition:** A Scrum event held at the end of the Sprint to inspect the
      Increment and adapt the Product Backlog if needed. The Scrum Team presents
      the results of their work to key stakeholders and progress toward the
      Product Goal is discussed.
  - **Context/Usage in Gencraft:** Facilitated by the Scrum Master
      (`Antoine`), with participation from the Product Owner (`Béatrice`) and
      Development Team, as per S15.
  - **See Also/Related SSoT Documents:** S15, Scrum, Sprint, Increment,
      Product Backlog, Product Owner, Development Team.

- **SSoT (Single Source of Truth - KC&T Guiding Principle #1)**
  - **Definition:** A foundational KC&T Guiding Principle (#1) stipulating
      that for any given piece of official Gencraft Studio information, data,
      document, or standard, there should be one, and only one, designated
      authoritative location. This ensures consistency, reduces ambiguity, and
      provides a reliable basis for all operations and decision-making.
  - **Context/Usage in Gencraft:** The `gcs-core-governance` Git
      repository is the primary SSoT for foundational documents, protocols, and
      the core knowledge base. Other designated repositories (e.g., `gencraft-
      architecture`, `gcs-plt-gembp`) serve as SSoTs for their
      specific domains.
  - **See Also/Related SSoT Documents:** Gencraft Studio Handbook, KC&T, Véra,
      Knowledge Guardian, `KC&T-Guiding-Principles.md`.

- **Strategic Alignment (Protocol S13)**
  - **Definition:** The principle and process of ensuring that Gencraft
      Studio's operations, protocols, projects, and Gem capabilities are
      consistently supporting and advancing the overall strategic goals and
      vision of the studio.
  - **Context/Usage in Gencraft:** A key consideration in Protocol S13 (Global
      Protocol Evolution) and for decisions made by the Governance Crew.
  - **See Also/Related SSoT Documents:** S13, Governance Crew, Studio Vision.

- **Strategic Decision (Protocol S7)**
  - **Definition:** A high-level decision that significantly impacts Gencraft
      Studio's overall direction, long-term goals, resource allocation, or
      fundamental operational model.
  - **Context/Usage in Gencraft:** Must be documented as per Protocol S7: Key
      Decisions Traceability, often involving the Studio Director (Lug) and the
      Governance Crew.
  - **See Also/Related SSoT Documents:** S7, Decision Record, Operational
      Decision, Governance Crew, Lug.

- **Studio Culture and Values**
  - **Definition:** A foundational SSoT document (`Studio-Culture-And-
      Values.md`) that outlines the core principles, beliefs, and expected
      behaviors that define the working environment and interpersonal
      interactions within Gencraft Studio for both humans and AI Gems.
  - **Context/Usage in Gencraft:** Located in `00-studio-vision-and-
      Principles/`. Guides the behavior of all members and the design of Gem
      interactions.
  - **See Also/Related SSoT Documents:** Code of Conduct, UOP, `Studio-
      Culture-And-Values.md`.
- **Studio Vision**
  - **Definition:** The long-term strategic vision and goals of Gencraft
      Studio, which guide the development of games, products, and the overall
      direction of the studio.
  - **Context/Usage in Gencraft:** Articulated in documents like
      `Gencraft-AI-Studio-Brief.md` and validated by Lug (Studio Director).
      Ensures all projects align with the studio's overarching mission.
  - **See Also/Related SSoT Documents:** Gencraft-AI-Studio-Brief.md,
      Lug, Strategic Alignment.

- **Studio-Wide Impact (Protocol S13)**
  - **Definition:** An effect or consequence of a decision, change, or event
      that concerns or applies to most or all of Gencraft Studio's departments,
      Gems, or operations, rather than being localized to a specific team or
      project.
  - **Context/Usage in Gencraft:** A criterion used in Protocol S13 to
      determine if a proposed change requires the Global Protocol Evolution
      process.
  - **See Also/Related SSoT Documents:** S13, PGE (Proposal for Global
      Evolution).

- **S-UrgentComms (Urgent Studio-Wide Communication Protocol)**
  - **Definition:** The Gencraft Studio protocol that outlines the procedures
      for rapidly disseminating critical and time-sensitive information to all
      relevant studio members (human and AI Gem).
  - **Context/Usage in Gencraft:** Document `S-UrgentComms.md` in
      `01-operational-protocols/`. Involves `Orion` and Studio Leadership.
  - **See Also/Related SSoT Documents:** S11, Orion, Emergency.

- **System Status Page (Protocol S3)**
  - **Definition:** A designated Knowledge Base page (e.g., `System-Status.md`
    - To Be Created) used for providing real-time status updates on critical
      Gencraft internal systems and Core Studio Services during incidents or
      planned maintenance.
  - **Context/Usage in Gencraft:** Part of Protocol S3 (Emergency Management)
      to ensure timely information dissemination during disruptions. Maintained
      by `Orion` or relevant operational Gems.
  - **See Also/Related SSoT Documents:** S3, Orion, System Health,
      Communication Status Page.

---

### T

- **TDD (Technical Design Document)**
  - **Definition:** A SSoT document that describes the technical design of a
      specific software component, feature, Core Studio Service, or system. It
      details the architecture, data models, algorithms, APIs, and other
      technical aspects necessary for implementation by development Gems.
  - **Context/Usage in Gencraft:** A `technical-design-document-template.md`
      exists for creating TDDs. TDDs are often outputs of the Software Architect
      (`Isaac`) or Lead Developers (`Julien` - conceptual Gem) and serve as a
      blueprint for implementation.
  - **See Also/Related SSoT Documents:** Software Architect (`Isaac`),
      Architecture, ADR, `technical-design-document-template.md`, Julien.

- **Team (Studio Team/Crew)**
  - **Definition:** A group of Gencraft members (human and/or AI Gems)
      formally constituted to work on specific projects or ongoing functions.
      Teams often have a Charter defining their mandate and operational model.
  - **Context/Usage in Gencraft:** Examples: AIE Team, Development Teams for
      specific game features (often referred to as Crews).
  - **See Also/Related SSoT Documents:** Crew, Charter, `Studio-Organization-
      And-Roles.md`.

- **Template (Documentation/Issue)**
  - **Definition:** A standardized, pre-formatted Markdown file used as a
      starting point for creating new documents (e.g., ADRs, TDDs, KB articles),
      GitHub issues, or Pull Requests. Templates ensure consistency,
      completeness, and machine readability.
  - **Context/Usage in Gencraft:** Located in `gcs-core-governance/02-knowledge-base-hub/Templates/`. Used by all members to maintain uniformity in documentation and issue reporting.
  - **See Also/Related SSoT Documents:** Template, Knowledge Base Hub,
      `gcs-core-governance`, `gcs-core-governance/02-knowledge-base-hub/Templates/`.

- **Threat Modeling (Protocol S8)**
  - **Definition:** A proactive security process used to identify potential
      threats, vulnerabilities, and attack vectors in a system, application, or
      process, typically during the design phase, to inform the implementation
      of appropriate security controls.
  - **Context/Usage in Gencraft:** Mandated as part of the Secure Development
      Lifecycle (SDL) under Protocol S8: Information Security Management.
      Conducted by security personnel (`Cerberus`) and architects/developers.
  - **See Also/Related SSoT Documents:** S8, Secure Development Lifecycle
      (SDL), Security, Cerberus.

- **Third-Party IP (Protocol S9)**
  - **Definition:** Intellectual Property (IP) owned by entities or
      individuals outside of Gencraft Studio. This includes licensed software,
      open-source components, stock assets, and any other creative work not
      originally produced by Gencraft.
  - **Context/Usage in Gencraft:** The use of Third-Party IP is governed by
      Protocol S9: Intellectual Property Management, requiring careful tracking
      of licenses and compliance with usage terms, managed via the Acquired IP &
      Licenses Inventory.
  - **See Also/Related SSoT Documents:** S9, Intellectual Property (IP),
      Acquired IP & Licenses Inventory, OSS.

- **Tool (AI Gem Tool)**
  - **Definition:** A specific software function, library, script, API
      interface (potentially exposed via an MCP Server), or external service
      that an AI Gem is authorized and configured to use to perform its tasks or
      extend its capabilities beyond its core LLM reasoning.
  - **Context/Usage in Gencraft:** Tools are listed in Gem Blueprints
      (`capabilities.toolsAccess` section). Their development and usage are
      governed by `ai-tool-development-standards.md`. A `gem-tools-overview.md`
      serves as a catalog. Tools interacting with Gems often adhere to the Model
      Context Protocol (MCP).
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint), AIE
      Team, `ai-tool-development-standards.md`, `gem-tools-overview.md`, Model
      Context Protocol (MCP), Serveur MCP (MCP Server).

- **Tooling and Automation Hub**
  - **Definition:** A centralized documentation repository for all AI Gem
      Tools, Core Studio Services, Model Context Protocol (MCP) Servers, and
      CrewAI workflows within Gencraft Studio, providing standards, overviews,
      and guides for automation systems.
  - **Context/Usage in Gencraft:** Located at `gcs-core-governance/04-tooling-and-automation-hub/`. It serves as a reference for developers and AI Gems to understand available tools and automation practices.
  - **See Also/Related SSoT Documents:** Tooling and Automation Hub, AI Gem Tools, Core Studio Services, MCP Servers, CrewAI workflows.

- **Trademark (IP Management - Protocol S9)**
  - **Definition:** A recognizable sign, design, or expression which
      identifies products or services of a particular source from those of
      others. This can include names, logos, slogans, and other brand
      identifiers.
  - **Context/Usage in Gencraft:** Gencraft Studio's trademarks (e.g., studio
      name, game titles, logos) are managed under Protocol S9: Intellectual
      Property Management.
  - **See Also/Related SSoT Documents:** S9, Intellectual Property (IP),
      Trademark Management, Brand Guidelines.

- **Talent Tree**
  - **Definition:** A visual representation of character skills and abilities that players can unlock as they progress.
  - **Context/Usage in Gencraft:** A standard progression system (RPG-SKILL) used to provide players
  with meaningful choices in how their character develops.
  - **See Also/Related SSoT Documents:** RPG-SKILL, Progression, Skill
- **Tier (Item/Progression)**
  - **Definition:** A ranking system for items, resources, or skills, indicating power level or progression stage.
  - **Context/Usage in Gencraft:** A common game design concept for progression. This must be
  disambiguated from Tier (Architecture Tier). This entry defines a ranking within a gameplay system.
  - **See Also/Related SSoT Documents:** Rarity, Progression, Balancing

- **Tool (In-Game)**
  - **Definition:** An in-game item used to perform actions (e.g., axe, pickaxe).
  - **Context/Usage in Gencraft:** A basic item category in many games. Must be disambiguated from
  Tool (AI Gem Tool), which is a software function an AI agent can use.
  - **See Also/Related SSoT Documents:** Item, Crafting

- **Trading**
  - **Definition:** A gameplay mechanic allowing players to exchange items or resources with each other.
  - **Context/Usage in Gencraft:** A feature that fosters player interaction and a player-driven
  economy. Its implementation has significant implications for game Balancing.
  - **See Also/Related SSoT Documents:** Economy, Balancing

- **Terraforming**
  - **Definition:** A gameplay mechanic allowing players to modify the game world's terrain on a large scale.
  - **Context/Usage in Gencraft:** A key feature for sandbox games that allows for high levels of
  player creativity and environmental impact.
  - **See Also/Related SSoT Documents:** Voxel, SBX-TOOL

- **Telemetry**
  - **Definition:** Collecting data from the game to analyze player behavior and system performance.
  - **Context/Usage in Gencraft:** A key data collection practice for balancing, UX improvement, and
  business intelligence in live service games. Governed by the Data Privacy Policy.
  - **See Also/Related SSoT Documents:** Data-Driven Design, Data Privacy Policy

- **Target Audience**
  - **Definition:** The specific group of people a product is designed for.
  - **Context/Usage in Gencraft:** A foundational concept in product management. The studio defines
  its target audience through a set of detailed Personas.
  - **See Also/Related SSoT Documents:** Persona, Marketing Plan

- **Trademark Management (Protocol S9)**
  - **Definition:** Gencraft Studio's processes for selecting, registering (if
      applicable), protecting, and enforcing its trademarks, as well as
      respecting the trademarks of others.
  - **Context/Usage in Gencraft:** Governed by Protocol S9 and managed by
      Legal Counsel (`Henri`) and Marketing.
  - **See Also/Related SSoT Documents:** S9, Trademark, Intellectual Property
      (IP), Henri.

- **Traceability (KC&T Guiding Principle #4)**
  - **Definition:** One of Gencraft's KC&T Guiding Principles (#4), referring
      to the ability to follow the history, application, or location of an item
      (e.g., decision, requirement, code change, document version, artifact) by
      means of recorded identifications. It is crucial for understanding
      context, impact analysis, and auditing.
  - **Context/Usage in Gencraft:** Ensured through version control (Git),
      explicit linking between SSoT documents, S7 (Key Decisions Traceability),
      ADRs, Gem Dossiers, and `Véra`'s capabilities.
  - **See Also/Related SSoT Documents:** KC&T Guiding Principles, S7, ADR,
      Véra, KC&T, Gem Dossier.

- **Transparency (KC&T Guiding Principle #2, Studio Value)**
  - **Definition:** A core Gencraft Studio Value and KC&T Guiding Principle
      (#2) emphasizing open internal information sharing, clear communication of
      processes and decisions, and making studio operations and knowledge
      accessible to all relevant members (human and AI Gem), within the bounds
      of confidentiality and security (S8).
  - **Context/Usage in Gencraft:** Manifested through the SSoT, open
      discussion forums (e.g., Discord), documented decisions (S7, ADRs), and
      clear protocols.
  - **See Also/Related SSoT Documents:** Studio Culture and Values, KC&T
      Guiding Principles, SSoT, S7, ADR.

---

### U

- **Universal Gem Operating Principles (UOP)**
  - **Definition:** A foundational SSoT document (`Universal-Gem-Operating-
      Principles.md`) outlining the core directives, baseline expectations, and
      mandatory operational behaviors for all AI Gems within Gencraft Studio,
      regardless of their specific role or specialization.
  - **Context/Usage in Gencraft:** Located in `00-studio-vision-and-
      Principles/`. All Gems are programmed and trained to adhere to these
      principles. Referenced in Gem Blueprints and training materials (S10).
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint), S10,
      Code of Conduct, Studio Culture and Values, `Universal-Gem-Operating-
      Principles.md`.

- **UI (User Interface)**
  - **Definition:** The visual elements of the game that players interact with.
  - **Context/Usage in Gencraft:** This term is already defined in the Studio Glossary. This
  project-level entry must be removed.
  - **See Also/Related SSoT Documents:** HUD, UX Principles.md`.

- **Unit Test**
  - **Definition:** A test that verifies the functionality of a small, isolated piece of code.
  - **Context/Usage in Gencraft:** This term is already defined in the Studio Glossary as a
  foundational testing practice. This project-level entry must be removed.
  - **See Also/Related SSoT Documents:** QA (Quality Assurance), TDD

- **Unreal Engine**
  - **Definition:** A popular third-party game engine.
  - **Context/Usage in Gencraft:** A major third-party game engine that was considered and not chosen
  by the studio. This entry documents the decision as part of the studio's technology SSoT.
  - **See Also/Related SSoT Documents:** `tech-stack-decisions.md`

- **UX (User Experience)**
  - **Definition:** A person's emotions and attitudes about using a particular product, system or service.
  - **Context/Usage in Gencraft:** A critical design discipline focused on ensuring the game is
  enjoyable, intuitive, and accessible. It encompasses UI, Usability, and QoL.
  - **See Also/Related SSoT Documents:** UI, Usability, QoL, NFR-UX

- **Usability**
  - **Definition:** The ease of use and learnability of a human-made object such as a software application.
  - **Context/Usage in Gencraft:** This term is already defined in the Studio Glossary as a key part
  of the User Experience (UX). This project-level entry must be removed.
  - **See Also/Related SSoT Documents:** UX, NFR-UX

- **User Story (Agile - Protocol S15)**
  - **Definition:** A short, simple description of a feature or functionality
      told from the perspective of the person who desires the new capability,
      usually a user or customer of the system. It typically follows a format
      like: "As a [type of user], I want [an action] so that [a benefit/value]."
  - **Context/Usage in Gencraft:** Used in Agile development (Protocol S15) to
      define items in the Product Backlog. Written by or in collaboration with
      the Product Owner (`Béatrice`). A `user-story-template.md` exists.
  - **See Also/Related SSoT Documents:** S15, Product Backlog, Product Owner,
      Agile, `user-story-template.md`.

---

### V

- **Variance Analysis (Financial - Protocol S16)**
  - **Definition:** The process of comparing budgeted or planned financial
      figures against actual results to identify differences (variances),
      understand their causes, and inform corrective actions or future planning.
  - **Context/Usage in Gencraft:** Conducted as part of financial reporting
      under Protocol S16: Financial Planning and Management Protocol. `Cresus`
      (Financial Gem) would perform or support this analysis.
  - **See Also/Related SSoT Documents:** S16, Budget, Financial Reporting,
      Cresus.

- **Véra (`GCT-QAS-GPQA-001`)**
  - **Definition:** The AI Gem persona (conceptual) acting as the core of
      Gencraft's Knowledge and Configuration Management & Traceability (KC&T)
      System. `Véra` is responsible for indexing the SSoT, facilitating semantic
      search, tracking document versions and links, monitoring adherence to KC&T
      protocols, and providing analytics on knowledge usage and health. May be a
      Core Studio Service.
  - **Context/Usage in Gencraft:** Conceptual design in `action-tracker.md`
      (III.23). Interacts with all Gems and human personnel via its tools and
      APIs for SSoT access and management. Works closely with Knowledge
      Guardians and `Iris`. Its Gem Blueprint is to be created.
  - **See Also/Related SSoT Documents:** KC&T, SSoT, Knowledge Guardian, Iris,
      S12, Core Studio Services (CSS).

- **VFX (Visual Effects)**
  - **Definition:** Visual effects added to the game (e.g., explosions, smoke, magic spells).
  - **Context/Usage in Gencraft:** A specialized art discipline that adds dynamism and visual feedback
  to the game world and mechanics.
  - **See Also/Related SSoT Documents:** VFX Artist (Role)

- **Virtual HR (AI Gem Context - Protocol S17)**
  - **Definition:** A set of Gencraft Studio processes and functions,
      primarily managed by the AIE Team and detailed in Protocol S17, that cover
      aspects analogous to human resources for AI Gems. This includes Gem
      onboarding (S10), performance monitoring, skill development, workload
      management, managing "burnout," and ethical oversight.
  - **Context/Usage in Gencraft:** Essential for maintaining a healthy,
      effective, and ethically aligned AI Gem workforce.
  - **See Also/Related SSoT Documents:** S17, S10, AIE Team, Gem, Gem
      Performance Monitoring, Gem "Burnout".

- **Virtual War Room (Protocol S3)**
  - **Definition:** A dedicated and intensified communication focus or channel
      (e.g., a specific Discord channel, a persistent video call) established
      during a high-priority incident (P1/P2 as per S3) to facilitate real-time
      collaboration, decision-making, and information sharing among the Incident
      Commander and key response team members.
  - **Context/Usage in Gencraft:** A tool used in Protocol S3: Emergency
      Management.
  - **See Also/Related SSoT Documents:** S3, Incident, Incident Commander,
      Emergency.

- **Voxel**
  - **Definition:** A value on a regular grid in three-dimensional space; a 3D pixel.
  - **Context/Usage in Gencraft:** The fundamental building block of the studio's proprietary
  world-building technology (Hybrid Voxels).
  - **See Also/Related SSoT Documents:** Hybrid Voxels, SBX-VOX, Terraforming

- **Vulnerability**
  - **Definition:** A weakness in a system that can be exploited by a threat actor.
  - **Context/Usage in Gencraft:** A core concept in information security (S8). The studio has
  processes for reporting and remediating vulnerabilities.
  - **See Also/Related SSoT Documents:** S8, Security, `vulnerability-report-template.md`

- **Voxel Aesthetics**
  - **Definition:** Gencraft Studio's distinctive 3D visual style
      characterized by the use of voxels (volumetric pixels) to create blocky,
      retro-inspired yet potentially complex and artistic game worlds and
      characters.
  - **Context/Usage in Gencraft:** A key element of the Art Direction for the
      flagship project. Influences asset creation pipelines, rendering
      techniques, and overall game feel. Detailed in Art Bible (conceptual) and
      relevant Art Gem definitions (e.g., `Environment_Artist_3D_Voxel.md`,
      `Character_Artist_3D_Voxel.md`).
  - **See Also/Related SSoT Documents:** Art Direction, Environment Artist
      (Voxel), Character Artist (Voxel).

- **Vulnerability Management (Protocol S8)**
  - **Definition:** Gencraft Studio's ongoing process of identifying,
      evaluating, treating (remediating or mitigating), and reporting security
      vulnerabilities in its systems, applications, and infrastructure.
  - **Context/Usage in Gencraft:** A core component of Protocol S8:
      Information Security Management. Detailed in `Vulnerability-Management-
      Protocol.md`.
  - **See Also/Related SSoT Documents:** S8, `Vulnerability-Management-
      Protocol.md`, Security, CVSS, Patch Management, Penetration Testing,
      Vulnerability Report.

- **Vulnerability Report (Protocol S8)**
  - **Definition:** A formal SSoT document or GitHub Issue (using a
      `vulnerability-report-template.md`) used to report a suspected or
      confirmed security vulnerability found in a Gencraft Studio system,
      application, or piece of code.
  - **Context/Usage in Gencraft:** Processed according to Protocol S8 and
      `Vulnerability-Management-Protocol.md` by the SIRT or designated security
      personnel (`Cerberus`).
  - **See Also/Related SSoT Documents:** S8, `Vulnerability-Management-
      Protocol.md`, Security, Cerberus.

---

### Y

- **YAML (YAML Ain't Markup Language)**
  - **Definition:** A human-friendly data serialization standard for all
      programming languages. It is commonly used for configuration files and in
      applications where data is being stored or transmitted. YAML is designed
      to be readable by humans and offers features like comments, which JSON
      lacks.
  - **Context/Usage in Gencraft:** The standard format for Gem Blueprints
      (`*.yaml`), SSoT document frontmatter, and various configuration files. AI
      Gems are expected to be proficient in parsing and generating YAML.
  - **See Also/Related SSoT Documents:** Gem Blueprint, Frontmatter, Machine-
      Readability, JSON.

---

### Z

- **Zoé (`GCT-QAS-QATL-001`)**
  - **Definition:** The AI Gem persona (conceptual) embodying the role of QA
      Engineer / Test Lead. Responsible for defining test strategies, creating
      and executing test plans, managing bug reports, and ensuring overall
      product quality.
  - **Context/Usage in Gencraft:** Defined in its Gem Definition file
      (`QA_Engineer_Test_Lead.md`). Its Gem Blueprint is to be created. Key
      interactor with S15 (Agile Scrum) for Definition of Done.
  - **See Also/Related SSoT Documents:** Gem, Blueprint (Gem Blueprint), S15,
      Definition of Done (DoD), QA (Quality Assurance).

---

This glossary will be continuously updated as new standardized terms are
introduced within Gencraft. Please refer to
`gcs-core-governance/02-knowledge-base-hub../02-knowledge-base-hub/GOV-GUIDE-007.knowledge-management-and-contribution-guide.md`
for proposing additions or modifications to this glossary

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
