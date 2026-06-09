---
docId: SEC-STANDARD-001
title: Information Classification And Handling Policy
version: 1.1.0
creation_date: '2025-06-13'
last_updated_date: '2026-05-20'
authors:
- AI Compliance Agent
- Cerberus (GCT-MGT-SECOFF-001)
knowledgeGuardian:
- Cerberus (GCT-MGT-SECOFF-001)
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/02-knowledge-base-hub/kb-domain-security/SEC-STANDARD-001.information-classification-and-handling-policy.md
metadata:
  lifecycle-stage: approved
  keywords:
  - information-classification
  - data-handling
  - security-policy
  - iac
  - automation
  - secrets-management
  - gencraft-studio
  - compliance
  scope: studio
  domain: security
  doc-type: standard
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
---
# Information Classification and Handling Policy

## 1. Purpose, Scope, and Mandate

**1.1. Purpose:**
This policy establishes the Gencraft Studio framework for classifying all
information assets and defines mandatory handling requirements for each
classification level. The objectives are to:

- Protect the Confidentiality, Integrity, and Availability (CIA Triad) of Gencraft information assets.
- Ensure information is handled in a manner commensurate with its sensitivity,
  criticality, and associated risks.
- Provide clear, actionable guidelines for all Gencraft personnel (human) and AI
  Gems to ensure consistent and secure information handling. These guidelines
  **must** inform the design, implementation, and **automated provisioning via
  Infrastructure as Code (IaC)** of all Gencraft systems, MCP Servers, and
  `Tools`.
- Support compliance with legal, regulatory, and contractual obligations.
- Enable `Cerberus` (GCT-MGT-SECOFF-001) to effectively monitor and enforce
  information security, `Isaac` (GCT-PRG-SARCH-001) to design and validate
  secure systems and data flows, and `Adam` (GCT-DVO-DSINF-001) to implement,
  manage, and automate secure infrastructure.

**1.2. Scope:**
This policy applies to **all Gencraft Studio information assets**, regardless of
their form (e.g., digital documents, source code, databases, Gem Blueprints,
operational logs, communications, API payloads, **infrastructure configurations
defined in IaC, CI/CD pipeline definitions**), media on which they are stored,
or location (e.g., SSoT repositories, cloud infrastructure, MCP Servers, local
development environments if permitted by S8). This includes information created,
processed, stored, transmitted, or managed by any Gencraft personnel (human) or
AI Gem, including data in transit between services and data actively being
processed in memory by applications or Gems. The design and **automated
provisioning** of all new systems, infrastructure components, and `Tools` must
explicitly consider how they will support and enforce this policy.

**1.3. Mandate:**
This policy is mandated under the authority of Protocol S8: Information Security
Management Protocol. Adherence is **mandatory** for all Gencraft members and for
the design, implementation, operation, and **automated management (IaC,
Configuration Management)** of all Gencraft systems, MCP Servers, infrastructure
components, and `Tools`.

## 2. Roles and Responsibilities

- **2.1. Studio Director (Lug - `LUG-STUDIO-DIR-001`):** Ultimately accountable
  for Gencraft's overall information security and risk posture. Approves this
  policy and receives high-level reports on its effectiveness from `Cerberus`.
- **2.2. Security Officer (`Cerberus` - GCT-MGT-SECOFF-001):**
  - **Accountable** for the development, maintenance, implementation, and
      enforcement of this Information Classification and Handling Policy.
  - **Responsible** for:
    - Providing definitive guidance and interpretation of this policy.
    - Developing and maintaining training materials (for humans and Gems via
          AIE Team) on information classification and handling.
    - Conducting and/or coordinating regular audits (using
          `Tool:AuditInformationHandling`) to ensure compliance.
    - Managing exceptions to this policy (Section 6).
    - Reporting on compliance and incidents related to information
          misclassification or mishandling to Studio Leadership and the
          Governance Crew.
    - Acting as the primary Knowledge Guardian for this policy.
- **2.3. Information Owners (Data Owners):**
  - Designated individuals (e.g., Department Leads, Project Leads) or Lead Gem
      roles responsible for specific categories of information assets (e.g.,
      Lead Game Designer for GDD content, Software Architect (`Isaac`) for
      architectural documents, AIE Team Lead (`Aura`) for Gem Blueprints). KG
      assignments may often overlap with Information Ownership.
  - **Responsible** for:
    - Assigning the initial classification level to information assets they
          create or for which they are the primary custodian, in strict
          accordance with this policy and using `Tool:ClassifyData` for
          guidance.
    - Reviewing and approving access requests to information they own, as
          per Protocol S8 (Section 8.3.3).
    - Periodically reviewing the classification of information assets within
          their domain to ensure continued accuracy.
- **2.4. Information Custodians:**
  - Individuals or Gem roles responsible for the operation and management of
      systems or repositories that store, process, or transmit Gencraft
      information (e.g., `Adam` (DevOps Infra) for cloud storage and IaC
      repositories, `Véra` (KC&T Gem) for SSoT indexing and access logging).
  - **Responsible** for implementing, **automating (via IaC and configuration
      management `Tools`)**, and maintaining the technical security controls
      required by this policy for the information assets and systems they manage
      (e.g., storage encryption, network segmentation, IAM configurations),
      based on their classification and under the guidance of `Cerberus` and
      `Isaac`.
- **2.5. Architects and Developers (Human and AI Gem, e.g., `Isaac` (GCT-PRG-
  SARCH-001), `Julien` (GCT-PRG-TL-001 - conceptual), other Development Gems):**
  - **Responsible** for designing and implementing systems, MCP Servers, APIs,
      and `Tools` that can inherently understand, respect, and enforce the
      handling requirements associated with different information classification
      levels, as defined in this policy. This includes secure data storage,
      transmission, processing, and logging mechanisms.
  - **Responsible** for ensuring that data flows within and between systems
      are designed to maintain the integrity and confidentiality of information
      according to its classification, minimizing exposure and adhering to the
      Principle of Least Privilege.
  - **Responsible** for consulting with `Cerberus` during the design phase
      (SDL Threat Modeling, S8.5.1) to ensure security requirements related to
      data classification are met.
  - **Responsible** for designing `Tools` with clear interfaces that allow
      calling Gems to specify or infer data classification, and for `Tools` to
      act accordingly.
- **2.6. DevOps Team (Lead: `Diane` - GCT-DVO-TL-001 - conceptual;
  Infrastructure Specialist: `Adam` - GCT-DVO-DSINF-001; Automation Specialist:
  `Camille` - GCT-DVO-DSAUT-001 - conceptual):**
  - **Responsible** for designing, implementing, managing, and **securing all
      Gencraft infrastructure components** (networks, storage, compute,
      Kubernetes clusters, CI/CD infrastructure) using Infrastructure as Code
      (IaC) principles that inherently enforce this policy's requirements.
  - **Responsible** for implementing and managing secure CI/CD pipelines that
      include automated security checks (SAST, SCA, image scanning) and manage
      deployment configurations (including secrets handling via
      `sec-001-secrets-management-standard.md`) according to data classification
      and security requirements.
  - **Responsible** for implementing and managing centralized monitoring,
      logging, and alerting systems for infrastructure security events,
      providing auditable data and actionable alerts to `Cerberus` and `Véra`.
  - **Responsible** for implementing and regularly testing secure backup,
      disaster recovery, and data disposal procedures at the infrastructure
      level, as per S4 and S16, ensuring compliance with classification-specific
      requirements.
  - **Responsible** for maintaining the `gencraft-iac` repository and
      associated `gcs-core-governance` related to secure infrastructure
      provisioning and operations.
- **2.7. All Gencraft Personnel (Human and AI Gems):**
  - **Responsible** for understanding this policy and complying with it in all
      their operations.
  - **Responsible** for correctly handling all information according to its
      assigned classification level.
  - **Responsible** for using designated Gencraft `Tools` that enforce or
      support these handling requirements.
  - **Responsible** for immediately reporting any suspected misclassification,
      mishandling of information, or actual/potential data breach to `Cerberus`
      using `Tool:ReportSecurityEvent(event_type="DataMishandling", ...)`.

## 3. Information Classification Levels

All Gencraft Studio information assets **must** be classified into one of the following four levels. If an asset contains components of multiple classification levels, it **must** be classified at the highest level applicable to any of its components.

**Note for AI Gems:** Use the following decision tree to determine the correct classification for any new information you create or handle. The `Tool:ClassifyData` is based on this logic.

```mermaid
graph TD
    A[Start: New Information Asset] --> B{For Public Release?};
    B -- Yes --> C[<b>L0 - Public</b>];
    B -- No --> D{Contains<br>Private Keys, Core IP Algorithms,<br>or poses Catastrophic Risk?};
    D -- Yes --> E[<b>L3 - Secret</b>];
    D -- No --> F{Contains Sensitive<br>Project, Financial, or<br>Security Vulnerability Data?};
    F -- Yes --> G[<b>L2 - Confidential</b>];
    F -- No --> H[<b>L1 - Internal</b><br>(Default)];

    style C fill:#c3e6cb,stroke:#155724
    style E fill:#f5c6cb,stroke:#721c24
    style G fill:#ffeeba,stroke:#856404
    style H fill:#d1ecf1,stroke:#0c5460
```

All Gencraft Studio information assets **must** be classified into one of the
following four levels. If an asset contains components of multiple
classification levels, it **must** be classified at the highest level applicable
to any of its components. `Cerberus` (using `Tool:ClassifyData` or by direct
assessment) is the final authority on classification disputes.

### **3.1. Level 0: Public (`L0-Public`)**

- **Description:** Information explicitly approved for public release or already lawfully in the public domain. Unauthorized disclosure results in minimal or no negative impact to Gencraft Studio.
- **Examples:** Published game trailers, official press releases (S11), public website content, job postings, Gencraft-contributed Open Source Software.
- **Marking:**
  - Human-readable: Clearly marked "PUBLIC" or implied by public distribution channel.
  - SSoT Frontmatter: `confidentialityLevel: "L0-Public"`
  - AI Gem `Tool` Tag / Infrastructure Tag: `GENCRAFT_CLASSIFICATION_L0_PUBLIC`
- **AI Gem Readability:** Freely accessible and processable by all Gencraft Gems and external systems.

### **3.2. Level 1: Gencraft-Internal (`L1-Internal`)**

- **Description:** Information intended for internal Gencraft use by authorized personnel and AI Gems. Unauthorized disclosure could cause minor operational disruption, minor reputational damage, or minor competitive disadvantage. This is the **default classification** for most internal operational information not explicitly classified higher or lower.
- **Examples:** Most SSoT documents (non-sensitive protocols, general KB articles, meeting notes for routine meetings), internal team communications on non-sensitive topics, development task tracking (non-sensitive details), non-critical Gem Blueprints not revealing unique IP.
- **Marking:**
  - Human-readable: Often implied by storage in internal systems, but ideally marked "GENCRAFT-INTERNAL".
  - SSoT Frontmatter: `confidentialityLevel: "L1-Internal"`
  - AI Gem `Tool` Tag / Infrastructure Tag: `GENCRAFT_CLASSIFICATION_L1_INTERNAL`
- **AI Gem Readability:** Accessible to all authenticated Gencraft Gems and personnel by default, unless more restrictive access is defined by the Information Owner for a specific subset of L1 information.

### **3.3. Level 2: Gencraft-Confidential (`L2-Confidential`)**

- **Description:** Sensitive business, project, or technical information. Unauthorized disclosure could cause significant operational disruption, financial loss, legal/regulatory penalties, serious reputational damage, or notable competitive disadvantage. Access **must** be restricted on a "need-to-know" basis.
- **Examples:** Unannounced strategic project details (major features, release dates not yet public), pre-release Game Design Documents (GDDs), detailed financial data and reports from `Cresus` (GCT-FIN-FRTA-001), specific Gem performance metrics or AIE Team research revealing sensitive AI model details, detailed security vulnerability reports before remediation, source code for core proprietary systems or unique game mechanics, sensitive S18 grievance investigation details.
- **Marking:**
  - Human-readable: **Mandatory** marking "GENCRAFT-CONFIDENTIAL".
  - SSoT Frontmatter: `confidentialityLevel: "L2-Confidential"`
  - AI Gem `Tool` Tag / Infrastructure Tag: `GENCRAFT_CLASSIFICATION_L2_CONFIDENTIAL`
- **AI Gem Readability:** Access strictly restricted. Gems require explicit RBAC permissions (S8.3.2) to read, process, or generate L2 data. `Gemma` **must** configure Gems handling L2 data with specific safeguards. `Iris`/`Véra` search results **must** be filtered based on authorization.

### **3.4. Level 3: Gencraft-Secret (`L3-Secret`)**

- **Description:** Gencraft's most sensitive and critical information, typically with very limited distribution. Unauthorized disclosure could cause severe or catastrophic damage to Gencraft's operations, finances, reputation, legal standing, strategic advantage, or long-term viability. Access **must** be severely restricted to a minimal number of explicitly named and authorized individuals or highly trusted/secured AI Gem processes.
- **Examples:** Private encryption keys for master data, root administrative credentials for critical studio-wide infrastructure, core unpatented IP algorithms or source code that forms Gencraft's primary competitive advantage, pre-litigation legal strategies, information that could compromise the security of `Gemma` or `Cerberus` themselves.
- **Marking:**
  - Human-readable: **Mandatory** marking "GENCRAFT-SECRET".
  - SSoT Frontmatter: `confidentialityLevel: "L3-Secret"`
  - AI Gem `Tool` Tag / Infrastructure Tag: `GENCRAFT_CLASSIFICATION_L3_SECRET`
- **AI Gem Readability:** Access extremely restricted and audited. Most AI Gems **must not** directly handle L3 data. Any Gem process designed to interact with L3 data **must** be specifically certified by `Cerberus` and the AIE Team, utilize purpose-built, highly audited `Tools`, and operate in a verifiable, constrained environment. `Iris`/`Véra` search **must** heavily restrict visibility and log all access attempts.

## 4. Information Handling Requirements by Classification Level

The following table summarizes the **minimum mandatory handling requirements**. Specific procedures and technical implementations are detailed in referenced SSoT documents (e.g., `data-security-standards.md`, `access-control-policy.md`). `Cerberus` may issue additional specific handling directives for certain data types. All infrastructure  configurations related to these requirements **must** be managed via Infrastructure as Code (IaC) and auditable.

| Requirement                 | L0-Public                                  | L1-Internal                                                                 | L2-Confidential                                                                                                 | L3-Secret                                                                                                                               |
|-----------------------------|--------------------------------------------|-----------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------|-----------------------------------------------------------------------------------------------------------------------------------------|
| **Access Control** | Open to public. Systems serving L0 **must** be in a DMZ or equivalent, provisioned via IaC (`gencraft-iac`) with minimal ingress firewall rules. | Authenticated Gencraft Personnel/Gems (via Gencraft AuthN/AuthZ Service - MCP-Auth). Default Gencraft Group. IAM roles defined and managed via IaC. | RBAC enforced by AuthN/AuthZ Service, Need-to-Know, Explicit Approval by Info Owner (S8.3). AuthZ service **must** support fine-grained checks. IAM roles via IaC with strict audit logs. | Strict RBAC via AuthN/AuthZ Service, Named Individuals/Gem Processes only, Explicit Approval by Lug/Cerberus, Strong MFA for humans (S8.3). AuthZ service **must** enforce this stringently; IAM roles via IaC with minimal permissions, deployed to dedicated service accounts. System architecture **must** minimize attack surface for L3 data. |
| **Encryption (At Rest)** | N/A.                                       | Recommended for SSoT (GitHub repo native encryption); **Mandatory** for operational databases (e.g., PostgreSQL with TDE managed via IaC). Key Management via Studio-approved KMS defined in IaC. | **Mandatory** (AES-256 or studio-approved equivalent, Gencraft-managed keys via KMS, S8.4.1). All cloud storage and DBs provisioned via IaC **must** have server-side encryption with KMS enabled by default using KMS. `Adam` verifies IaC modules. | **Mandatory** (Strongest studio-approved algorithms, key segregation, potentially HSMs for root keys, S8.4.1). Infrastructure **must** support these options, provisioned and managed via IaC, with KMS key policies strictly limiting access to L3 data services. |
| **Encryption (In Transit)** | Recommended (HTTPS for all web access, CDN configured via IaC). | **Mandatory** (TLS 1.3+ for all internal/external network traffic, S8.4.2). Network configurations (VPCs, subnets, load balancers - IaC defined) **must** enforce this. MCP & Gem-to-Gem comms within trusted network boundaries **must** use mTLS where appropriate, configured via service mesh (IaC managed) if used. | **Mandatory** (TLS 1.3+, VPN for external administrative access, mTLS for all internal service-to-service communication involving L2 data, S8.4.2). API Gateways & Load Balancers (IaC) **must** enforce TLS termination and re-encryption to backend services. Network flow logs **should** be monitored by `Cerberus` for non-compliant traffic. | **Mandatory** (TLS 1.3+, dedicated secure/isolated network segments or VPCs (IaC defined with strict firewall rules), end-to-end encryption where architecturally feasible, S8.4.2). Direct L3 data transit **must** be minimized; prefer processing within secure enclaves managed by IaC. All network paths handling L3 data **must** be explicitly defined and audited. |
| **Storage Location** | Publicly accessible Gencraft systems (e.g., CDN, static web host), isolated from internal networks. Provisioned via IaC. Bucket policies (IaC) **must** ensure public read-only. | Designated internal SSoT repos (GitHub), approved cloud storage (e.g., GCS/S3 buckets with L1 IAM policies via IaC), internal databases with L1 access controls via IaC. Storage solutions **must** support individual object/document metadata for `GENCRAFT_CLASSIFICATION_L1_INTERNAL` tags. | Designated secure SSoT folders with restricted permissions (managed via Git repo permissions), specific restricted cloud storage buckets/databases with strict IAM policies (IaC defined) and **mandatory, immutable audit logging** enabled. Solutions **must** be architected to enforce L2 access controls and integrate KMS. Backups **must** inherit L2 protections. | Highly restricted, programmatically-accessed, isolated, encrypted environments (e.g., dedicated secret manager instances for credentials, secure enclaves for processing, physically/logically separate DB instances with dedicated VPCs). All provisioned and managed via IaC with stringent change control and automated drift detection. Access **must** be via specific, minimal, audited APIs/`Tools`. |
| **Marking/Labeling** | "PUBLIC" (SSoT Frontmatter/metadata). System outputs **must** be verifiably L0 before publication via CI/CD checks (managed by `Camille`). | SSoT Frontmatter: `L1-Internal`; AI Tag: `GENCRAFT_CLASSIFICATION_L1_INTERNAL`; Database schema (IaC managed) **must** include classification columns. Object metadata **must** be applied by `Tools` or IaC provisioning scripts. `Véra` **should** be able to report on untagged assets. | SSoT Frontmatter: `L2-Confidential`; AI Tag: `GENCRAFT_CLASSIFICATION_L2_CONFIDENTIAL`; Mandatory, auditable metadata tags in all storage systems applied by `Tools` or IaC. Watermarking for sensitive human-readable documents (Tool TBD). DLP scans **should** check for L2 markers in outbound traffic. | SSoT Frontmatter: `L3-Secret`; AI Tag: `GENCRAFT_CLASSIFICATION_L3_SECRET`; Strict metadata, mandatory data tagging at point of creation; physical labeling if ever applicable. All system components handling L3 **must** be identifiable and inventoried by `Cerberus`, with configurations managed and audited via IaC. |
| **Sharing (Internal)** | Freely within Gencraft.                     | Within Gencraft personnel/Gems based on general role access (RBAC). `Tools` accessing/sharing L1 data **should** log access if significant volume or if crossing trust boundaries (via `Véra`). Network segmentation (IaC) **may** be used to group L1 systems. | Only to explicitly authorized personnel/Gems with verified Need-to-Know. `Tools` and APIs **must** programmatically verify recipient authorization via AuthZ service before sharing. All L2 sharing events **must** be logged to `Véra` by `Cerberus`. Infrastructure (e.g., message queues, shared storage) **must** support granular sharing controls defined by IAM/IaC. | Only to explicitly named individuals/Gem processes with verified, minimal Need-to-Know; all sharing events **must** be pre-authorized (if possible) and logged to `Véra` by `Cerberus` with full context. Network segmentation (IaC) **must** be used to strictly isolate L3 data flows. |
| **Sharing (External)** | Approved public channels (S11).             | **Strictly Prohibited** without explicit approval. Technical controls (DLP - TBD, potentially at network gateway (IaC configured) or endpoint level) **should** be architected to detect/prevent accidental L1 sharing. | **Strictly Prohibited** without explicit approval. Technical controls (DLP - TBD) **must** be architected to prevent unauthorized L2 sharing. Data **must** be encrypted before any approved transfer, via approved mechanisms (e.g., secure file transfer service provisioned by DevOps). | **Strictly Prohibited** except under extreme, legally mandated, and Lug-approved circumstances with maximum security controls, including end-to-end encryption and audited transfer mechanisms. Technical architecture **must** make accidental sharing impossible. |
| **Retention** | Per public dissemination strategy.          | Per S4/S16 operational needs. Cloud storage lifecycle policies (IaC managed by `Adam`) **should** support automated archival to lower-cost tiers or deletion based on S16 policies and metadata tags. | Per S4/S16, legal/project needs; reviewed for declassification/destruction. Cloud storage lifecycle policies (IaC managed) **must** support secure archival and verifiable deletion/anonymization. Immutable audit logs for these actions. | Per S4/S16, minimal necessary retention period, stringent review for destruction; **must never** reside on non-Gencraft development/test systems. Systems and storage (IaC managed) **must** support verifiable cryptographic erasure. Destruction logs **must** be generated and stored securely by DevOps. |
| **Secure Disposal** | Standard deletion.                         | Standard deletion/archival. Cloud storage deletion mechanisms. `Tools` and systems **should** log deletion events to `Véra`. `Adam` ensures IaC scripts for de-provisioning resources perform deletions. | Secure deletion (e.g., cryptographic wipe, multi-pass overwrite as per S4/S16). Cloud provider secure deletion options **must** be used and configured via IaC. `Tools` and systems **must** perform secure deletion methods and log completion to `Véra` for audit by `Cerberus`. | Certified destruction/cryptographic erasure, logged and verified by `Cerberus` (S4/S16). Cloud storage (IaC managed) **must** use certified methods. Architectural design **must** facilitate this. `Adam` is responsible for implementing IaC for secure disposal and providing auditable proof. |
| **Logging of Access**| Web server logs, CDN logs, centrally collected via DevOps `Tools` and ingested by `Véra`. | Basic system/application access logs (e.g., Git logs, Kubernetes API server logs). `Véra` **should** correlate these. Logs **must** be centrally collected to a secure log management system (managed by DevOps). | **Mandatory** (Detailed, immutable access logs: GemID/UserID, timestamp, resource ID, action type, data object ID if applicable, source IP/service; logged to centralized secure logging system (`Véra` or dedicated SIEM managed by DevOps) for `Cerberus` audit, S8.3). APIs and data access `Tools` **must** generate these logs. Infrastructure (e.g., DBs, storage buckets) **must** have audit logging enabled via IaC and configured to export to the central system. | **Mandatory** (Extensive, real-time, and immutable access logs, including failed attempts, data viewed/modified, export attempts; logged to centralized secure logging system (`Véra` or SIEM managed by DevOps) for `Cerberus` proactive alerting and audit, S8.3). System architecture and IaC **must** ensure log integrity and timely alerting through monitoring `Tools` managed by DevOps. Access to L3 logs itself **must** be L3. |

- **AI Gem Actionability & `Cerberus` / `Isaac` / `Adam` Oversight:**
  - `Cerberus` (GCT-MGT-SECOFF-001) **must** use
      `Tool:AuditInformationHandling(classification_level_filter,
      resource_filter, audit_checklist_ssot_path)` to periodically audit
      compliance. `Isaac` (GCT-PRG-SARCH-001) and `Adam` (GCT-DVO-DSINF-001)
      **must** collaborate with `Cerberus` to design automatable audit checks
      for applications, `Tools`, and infrastructure configurations (IaC
      templates). These checks **should** be integrated into CI/CD pipelines
      where feasible.
  - `Tools` used by Gems for data operations **must** be architected (by
      `Isaac`/Dev Gems) and deployed (by `Adam`/DevOps Gems) to programmatically
      enforce handling requirements. These `Tools` **must** be certified by
      `Cerberus`.
  - `Gemma` (GCT-UTL-GGEN-001) **must** ensure Gems are instantiated with
      Blueprints specifying max data classification levels and provisioned with
      certified `Tools` and IAM roles defined in IaC by `Adam`.
  - Any Gem detecting data mishandling **must** report to `Cerberus`. `Isaac`
      and `Adam` **must** be involved if the issue points to
      systemic/architectural/infrastructure flaws. `Adam` **must** provide
      `Tools` or IaC scripts to `Cerberus` to facilitate rapid infrastructure-
      level remediation (e.g., revoking network access, isolating a VM,
      triggering secure snapshot).

## 5. Policy in Action for AI Gems

To ensure this policy is not just a document but an operational reality, AI Gems must be designed and configured as follows:

- **Gem Configuration (`Gemma`)**: All Gem Blueprints must specify the maximum data classification level the Gem is authorized to handle. `Gemma` must use this to provision Gems with the correct role-based permissions (via `Auth Service`) and `Too`l access.
- **Mandatory `Tools`**:
  - `Tool:ClassifyData(content)`: Any Gem creating a new information asset must use this `Tool` to get a recommended classification level before saving.
  - `Tool:CheckPermissions(resource_id, action)`: Before accessing or modifying any data, a Gem must use this `Tool` to query the `Auth Service` to confirm it has the necessary rights.
  - `Tool:LogAccessEvent(resource_id, classification_level, action)`: Access to any L2 or L3 data must be explicitly logged via this Tool, which sends a structured log to `Véra`/`Cerberus`.
- **Behavioral Directives (in Gem Blueprints)**: Gems must be programmed to halt and escalate to their supervisor or `Cerberus` if they are asked to perform an action that violates this policy (e.g., share L2 data externally without a documented approval flag).

## 6. Policy Compliance and Enforcement

- **5.1. Compliance Monitoring:**
  - `Cerberus` (GCT-MGT-SECOFF-001) is responsible for establishing and
      managing a program to monitor compliance with this policy. This includes:
    - Regular automated checks via `Tools` (e.g.,
          `Tool:ScanSSoTForClassificationMarkers`,
          `Tool:CheckStorageEncryptionStatus` which interfaces with cloud
          provider APIs via DevOps `Tools`).
    - Periodic manual audits of specific domains, systems, or IaC
          configurations.
    - Reviewing access logs and security alerts provided by `Véra` and
          infrastructure monitoring tools.
- **5.2. Non-Compliance Reporting and Handling:**
  - Any Gencraft member (human or AI Gem) who becomes aware of any suspected
      or actual non-compliance with this policy **must** immediately report it
      to `Cerberus` or through the channels defined in S18: Grievance Reporting
      and Resolution Protocol.
  - `Cerberus` **must** investigate all reported non-compliance issues using
      `Tool:InvestigatePolicyViolation`.
  - Confirmed non-compliance may result in corrective actions, which could
      include:
    - For human personnel: Re-training, formal warning, up to disciplinary
          measures as per Gencraft HR policies (To Be Developed) and the Code of
          Conduct.
    - For AI Gems: Re-training, parameter adjustment via `Gemma` or AIE
          `Tools`, `Tool` permission revocation via IAM (IaC updated by `Adam`),
          temporary deactivation/quarantining (requiring infrastructure support
          for isolation, e.g., specific network policies or compute instance
          states, manageable via DevOps `Tools` operated by `Adam` or
          `Cerberus`), or decommissioning, as per S17 and the Code of Conduct.
          The AIE Team and DevOps (`Adam`) **must** provide auditable `Tools` or
          procedures to `Cerberus` to facilitate these actions.
- **5.3. Exceptions to this Policy:**
  - Any exception to this policy **must** be formally requested (using
      `security-policy-exception-request-template.md`) to `Cerberus`.
  - The request **must** include:
    - Clear identification of the policy section for which an exception is
          sought.
    - Detailed justification for the exception.
    - A comprehensive risk assessment detailing potential negative impacts.
    - Proposed compensating controls (technical, procedural, infrastructure-
          based) and how their effectiveness will be monitored.
    - An architectural impact assessment and technical feasibility review of
          compensating controls, co-signed by `Isaac` (GCT-PRG-SARCH-001) or a
          designated architect if system design or data flow is significantly
          affected.
    - An operational impact and feasibility assessment of compensating
          controls from a DevOps/Infrastructure perspective, co-signed by `Adam`
          (GCT-DVO-DSINF-001) or the DevOps Lead.
    - Duration for which the exception is requested.
  - `Cerberus` reviews the request. Exceptions require documented approval
      from `Cerberus` AND the Information Owner of the affected data. For
      exceptions to L3 handling requirements or those with significant
      architectural, security, or operational infrastructure risk (as determined
      by `Cerberus`, `Isaac`, and `Adam`), approval from the Studio Director
      (Lug) is also mandatory.
  - All approved exceptions **must** be documented in a central SSoT
      `ExceptionRegister.md` (managed by `Cerberus` with
      `Tool:LogPolicyException`), include an expiry date, and be periodically
      reviewed (at least quarterly or upon expiry) by `Cerberus`, the
      Information Owner, `Isaac`, and `Adam`.

## 6. Policy Review and Updates

This Information Classification and Handling Policy **must** be reviewed at
least annually by `Cerberus`, `Isaac`, `Adam`, and the Governance Crew, or more
frequently if:

- Significant changes occur in Gencraft's operations, technology stack (e.g.,
  new cloud services, new database technologies, major updates to core
  infrastructure components like Kubernetes or networking fabric), or data
  processing architectures.
- New significant security threats, vulnerabilities, or regulatory requirements
  emerge.
- A major security incident or compliance failure related to data handling
  occurs (triggering a mandatory review as part of the S5 Lessons Learned
  process).
All new Technical Design Documents (TDDs) for systems handling Level 1 or higher
data **must** include a section detailing how the design adheres to this policy.
**Infrastructure as Code (IaC) modules (`gencraft-iac`) managing resources that
store or process classified data must also explicitly document their adherence
to relevant sections of this policy in their respective READMEs or module
documentation, and be subject to periodic compliance checks by `Cerberus` using
`Tool:AuditIaCSecurityConfig`.**
Updates **must** follow S13: Global Protocol Evolution Protocol.

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
