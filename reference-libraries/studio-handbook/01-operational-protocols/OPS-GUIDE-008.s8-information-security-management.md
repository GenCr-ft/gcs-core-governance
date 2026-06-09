---
docId: OPS-GUIDE-008
title: S8 Information Security Management
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
  lifecycle-stage: draft
  security-classification: l1_internal
  intended-audience:
  - security-team
  - contributors
  - ai-agents
  keywords:
  - information-security
  - management
  - protocol
  - ai-gems
  - security-awareness
  - data-protection
  - risk-management
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-008.s8-information-security-management.md
---
# S8: Information Security Management Protocol

## 8.0. Justification and Objectives

**Why this protocol is critical for Gencraft and its AI Gems:**
Information security is paramount for any development studio, especially one
like Gencraft which handles valuable intellectual property (game code, engine
code in `gcl-voxel-engine`, art assets, design documents in
`gcp-aethel-docs-gdd`), operational data (Gem configurations in
`gcs-plt-gembp`, studio protocols in `gcs-core-governance`), and
potentially, in the future, user data. A robust security protocol is essential
to:

- **Protect Intellectual Property (IP):** Safeguard Gencraft's core creative and
  technical assets from theft, unauthorized access, or leakage (see S9).
- **Ensure System and Data Integrity:** Prevent unauthorized modification or
  corruption of code, data, configurations, and SSoT articles.
- **Maintain Operational Availability:** Protect studio infrastructure (defined
  in `gcs-core-governance` repository and related documents) and `Tools`
  from disruptions caused by security incidents (see S3).
- **Build Trust and Confidence:** Demonstrate a commitment to security to
  internal stakeholders (Lug) and any future external partners or users.
- **Comply with
  Gencraft systems, `Tools`, MCP Servers, AI Gem Blueprints, and operational
  processes. *(This should be a checklist item in relevant design templates,
  e.g., TDDs, Gem Blueprints.)*
- **Principle 8.1.2: Least Privilege (Alignment with KC&T Principle #8):** AI
  Gems, their `Tools`, and any human users **must** be granted only the minimum
  access rights and permissions necessary to perform their designated roles and
  tasks. Superfluous permissions **must** be avoided and revoked when no longer
  needed.
- **Principle 8.1.3: Defense in Depth:** Gencraft **must** implement multiple
  layers of security controls (technical, administrative/procedural, and AI Gem
  behavioral directives) so that the failure or bypass of a single control does
  not lead to a significant compromise.
- **Principle 8.1.4: Shared Responsibility for Security:** While `Cerberus`
  (GCT-MGT-SECOFF-001) and other designated roles have primary security
  responsibilities, all Gencraft Gems and human personnel share a responsibility
  to be security-conscious, adhere to security policies, operate `Tools`
  securely, and promptly report potential security issues or vulnerabilities.
- **Principle 8.1.5: Proactive Threat and Vulnerability Management:** Gencraft
  **must** continuously identify, assess, prioritize, and mitigate security
  threats and vulnerabilities through regular automated scanning, manual audits,
  code reviews, and timely patch management.
- **Principle 8.1.6: Comprehensive Traceability of Security Events:** All
  significant security-related events (e.g., access attempts, permission
  changes, configuration modifications, detected anomalies, incident responses)
  **must** be logged comprehensively and centrally (e.g., via `Véra`) and be
  auditable. This aligns with KC&T Principle #4 (Traceability) and S3 (Emergency
  Management).
- **Principle 8.1.7: Secure Secret Management:** All sensitive credentials (API
  keys, passwords, certificates, encryption keys) **must** be managed through a
  dedicated, secure secret management system, adhering to
  `sec-001-secrets-management-standard.md` (from `gcs-core-governance`). Direct
  embedding of secrets in code, configuration files, or Gem Blueprints is
  strictly prohibited.

## 8.2. Information Classification and Handling

- **Policy SSoT Document:** `information-classification-and-handling-policy.md`
  - **Location:** `02-knowledge-base-hub/kb-domain-security/SEC-STANDARD-001.information-classification-and-handling-policy.md`
- **Content Overview:**
  - **8.2.1. Classification Levels:**
    - `Level 0: Public:` Information explicitly approved for public release.
    - `Level 1: Gencraft-Internal:` Non-sensitive operational information,
          accessible to all authenticated Gencraft members. Default for most
          SSoT documents.
    - `Level 2: Gencraft-Confidential:` Sensitive business, project, or
          technical information requiring restricted access (e.g., unannounced
          project details, pre-release GDDs, financial data from `Cresus`,
          specific Gem Blueprint details).
    - `Level 3: Gencraft-Secret:` Highly sensitive information requiring
          stringent access controls and handling (e.g., private encryption keys,
          core IP algorithms before legal protection, critical security
          vulnerability details).
  - **8.2.2. Marking Guidelines:**
    - All SSoT documents **must** include a `confidentialityLevel` field in
          their YAML frontmatter, mapping to the levels above.
    - Data stored in databases or other systems **must** have associated
          metadata indicating its classification level.
    - AI Gems, via their `Tools` (`Tool:ClassifyData`), **must** attempt to
          assign a classification level when creating new significant artifacts.
          `Véra` may also suggest classifications based on content analysis.
  - **8.2.3. Handling Rules per Level:**
    - This section will define specific rules for storage (referencing S4),
          access (referencing Section 8.3 below), encryption requirements
          (Section 8.4), sharing (internal and external, linking to S11), and
          secure disposal/destruction for each classification level.
- **AI Gem Implications:**
  - `Gemma` **must** configure Gems with an understanding of these
      classification levels, particularly if their role (defined in their
      Blueprint) involves creating or handling data above `Level 1: Gencraft-
      Internal`. The Gem Blueprint's
      `ethicalSafetyConfig.confidentialityLevelHandling` field **must** map to
      these levels.
  - Gem `Tools` for data access, storage, or creation (e.g.,
      `Tool:CloudStorageAccess`, `Tool:DatabaseQuery`, `Tool:MarkdownAuthoring`)
      **must** be designed to:
    - Understand and respect data classification tags/metadata.
    - Enforce handling rules (e.g., query `Cerberus` or policy for
          permission before accessing Level 2/3 data).
    - Automatically apply appropriate security measures (e.g., encryption
          for Level 2/3 data at rest via `Tool:EncryptData`).
    - Log access to Level 2 and Level 3 data to `Véra` for auditing by
          `Cerberus`.
  - `Iris` (GCT-UTL-RWSKA-001) and `Véra`'s search/indexing `Tools` **must**
      filter results based on the requesting Gem's/user's authorized access to
      specific classification levels.

## 8.3. Access Control Management

- **Policy SSoT Document:** `access-control-policy.md`
  - **Location:** `02-knowledge-base-hub/kb-domain-security/SEC-GUIDE-001.access-control-policy.md`
- **Key Mechanisms:**
  - **8.3.1. Strong Authentication:**
    - **Humans:** Multi-Factor Authentication (MFA) is **mandatory** for all
          human accounts with access to Gencraft SSoT repositories (GitHub),
          cloud provider consoles, production deployment systems, and any system
          handling Level 2 or Level 3 data.
    - **AI Gems & `Tools`:** Each AI Gem and automated `Tool`/MCP Server
          requiring access to other systems or APIs **must** use unique, strong,
          and regularly rotated credentials (e.g., API tokens, service account
          keys). These credentials **must** be managed by the Gencraft Secret
          Management System (see `sec-001-secrets-management-standard.md`) and
          never hardcoded.
  - **8.3.2. Role-Based Access Control (RBAC):**
    - Access rights to all Gencraft resources (SSoT repositories, `Tools`,
          MCP Servers, cloud resources, specific data sets) **must** be granted
          based on a Gem's or human's validated role (defined in `Studio-
          Organization-And-Roles.md` and individual Gem Blueprints) and strictly
          adhere to the Principle of Least Privilege (8.1.2).
    - Implementation via GitHub team permissions, cloud IAM roles, database
          roles, and authorization logic within MCP Servers and `Tools`.
  - **8.3.3. Access Request & Approval Process:**
    - A formal, SSoT-documented, and traceable process for requesting,
          approving (by the designated resource owner or Lead Gem/human),
          implementing (by `Adam` (DevOps Infra) or system admin Gem), and
          revoking access rights.
    - This process **must** be managed via **GitHub Issues** in a dedicated,
          access-controlled repository (e.g., `gencraft-access-requests`) using
          the `access-request-template.md`.
    - Each request Issue **must** document: Requester (GemID/HumanID),
          Resource (exact path/ID), Requested Access Level (e.g., read, write,
          admin, execute specific `Tool` function), Business Justification
          (linked to task/project ID), Approver(s) (GemID/HumanID),
          Implementation Details (who, when), and Access Review/Expiry Date
          (especially for temporary access).
  - **8.3.4. Periodic Access Reviews:**
    - `Cerberus` (GCT-MGT-SECOFF-001) **must** orchestrate and oversee
          periodic reviews of access rights.
    - **Frequency:** Quarterly for critical systems and Level 2/3 data
          access; Annually for Level 1 internal systems.
    - **Process:** `Cerberus` uses a `Tool:GenerateAccessReport` to list
          current permissions per resource/role. Resource owners and relevant
          Leads **must** review and re-approve or request revocation of these
          permissions. This process is tracked via GitHub Issues (e.g.,
          `type:access-review`).
- **AI Gem Implications & Actionability:**
  - `Gemma` **must** instantiate new Gems with only the default, minimal set
      of access rights defined in their Blueprint's `capabilities.toolsAccess`
      and `knowledgeBaseAccess.domainAccess` sections.
  - If an operational Gem, executing a task, determines it requires additional
      access rights not currently granted, it **must**:
        1. Log the requirement and the access denied error.
        2. Use `Tool:CreateAccessRequestIssue` to submit a formal access
            request, providing its GemID, the target resource, required
            permission, and the task ID/justification for the request.
        3. Notify its human supervisor or Crew Lead of the pending access
            request.
        4. Pause the specific sub-task requiring elevated access until
            approved, but continue other parallelizable tasks if possible.
  - Gem `Tools` interacting with resources **must** use credentials securely
      fetched from the Gencraft Secret Management System via a standardized
      `Tool:GetSecret(secret_name)` for each session or operation, and **must
      not** cache or store credentials locally.
  - All access attempts (successful or denied) by Gems or their `Tools` to
      significant resources **must** be logged to `Véra` with GemID, resource,
      timestamp, and action attempted. `Cerberus` uses these logs for
      monitoring.

## 8.4. Data Security (At Rest, In Transit, In Use)

- **Policy SSoT Document:** `data-security-standards.md`
  - **Location:** `02-knowledge-base-hub/kb-domain-security/` (document pending — tracked: issue #86)
- **Key Standards & Procedures:**
  - **8.4.1. Encryption at Rest:**
    - All Gencraft data classified as `Level 2: Gencraft-Confidential` or
          `Level 3: Gencraft-Secret` stored in cloud storage (e.g., S3, GCS),
          databases (e.g., RDS, Cloud SQL), or Git LFS **must** be encrypted
          using strong, industry-standard encryption algorithms (e.g., AES-256).
    - Gencraft **must** control or manage the encryption keys (e.g., via AWS
          KMS, Google Cloud KMS) where feasible and appropriate for the data
          sensitivity. Key management procedures (rotation, access control to
          keys) **must** be documented in this `data-security-standards.md`.
  - **8.4.2. Encryption in Transit:**
    - All network communication transmitting Gencraft data (internal MCP
          Server-to-Server calls, API calls to external services like GitHub or
          cloud providers, Gem-to-Gem communication if not on a secured internal
          bus) **must** use strong encryption protocols (e.g., TLS 1.3 or
          higher).
    - No unencrypted transmission of `Level 1` or higher data is permitted
          over untrusted networks. Internal trusted networks may have specific
          exemptions documented by `Adam` (GCT-DVO-DSINF-001) and approved by
          `Cerberus`.
  - **8.4.3. Data Handling by AI Gems (In Use / Processing):**
    - AI Gems and their `Tools` processing sensitive data (as per its
          classification defined in 8.2.1) **must** minimize its exposure in
          logs and temporary storage.
    - Sensitive data payloads (`Level 2` or `Level 3`) **must not** be
          logged unless explicitly for audited debugging under controlled
          conditions, approved by `Cerberus`, and with appropriate data masking
          or truncation applied.
    - Secure deletion and sanitization procedures for temporary files or
          data held in memory (once no longer needed by a `Tool` for its
          immediate task) **must** be implemented within the `Tool`'s logic.
  - **8.4.4. Backup and Recovery Security:**
    - Backup data for all critical Gencraft systems (infrastructure state,
          SSoT repositories, code repositories, databases, Gem state if
          applicable) **must** be encrypted with the same or higher level of
          protection as the original data.
    - Backups **must** be stored securely, potentially in a separate
          geographic region or isolated account for resilience.
    - Recovery procedures **must** be regularly tested (e.g., annually for
          critical systems) by the DevOps Crew (`Adam`) to ensure data integrity
          and timely restoration. Results **must** be documented and auditable
          by `Cerberus`.
    - This is a primary responsibility of the DevOps Crew (`Adam`),
          documented further in `gcs-core-governance/Backup-And-Recovery-
          Procedure.md`.
- **AI Gem Implications & Actionability:**
  - `Tools` designed for data storage, retrieval, or transmission (e.g.,
      `Tool:CloudStorageAccess`, `Tool:DatabaseConnector`, `Tool:SecureAPICall`)
      **must** automatically implement or ensure the use of required encryption
      mechanisms (both at rest and in transit) transparently to the calling Gem
      where possible. These `Tools` **must** consult `Data-Security-
      Standards.md` via `Tool:SecurityPolicyLookup` for specific
      algorithm/protocol requirements.
  - `Cerberus` **must** periodically audit (e.g., quarterly, using
      `Tool:AuditDataEncryptionSettings`) the encryption settings of major data
      stores to ensure compliance with `data-security-standards.md`.
  - Gems handling sensitive data (e.g., `Léo` [conceptual Gem for OSS
      licenses], `Cresus` (GCT-FIN-FRTA-001)) **must** have their operational
      environments and `Tools` designed and configured by `Gemma` to enforce
      these data handling rules.
  - `Gemma` **must** ensure that any Gem designed to process Level 2/3 data
      has a blueprint that specifies its capability and need for such
      processing, and that its default configuration and associated `Tools`
      adhere to secure handling practices.

## 8.5. System, `Tool`, and Application Security ( S-SDL)

- **Policy SSoT Document:** `Secure-Development-Lifecycle-Policy.md` (SDL Policy)
  - **Location:** `02-knowledge-base-hub/kb-domain-security/` (document pending — tracked: issue #87)
- **Key SDL Practices for Gencraft (applicable to game engine `gencraft-game-
  engine`, game code, AI Gem `Tools`, MCP Servers, and SSoT automation
  scripts):**
  - **8.5.1. Security Requirements & Threat Modeling:**
    - For all new significant Gencraft-developed `Tools`, MCP Servers, game
          features, or critical AI Gems, `Isaac` (GCT-PRG-SARCH-001) (or
          `Cerberus`) and the developing Gem/Human Lead **must** perform and
          document a threat modeling exercise (e.g., STRIDE, PASTA) during the
          design phase.
    - Identified threats and planned mitigations **must** be documented in
          the corresponding TDD, Gem Blueprint, or a specific security design
          document, and tracked as requirements.
  - **8.5.2. Secure Coding Standards:**
    - Gencraft **must** adopt, document (in `gencraft-devops-
          standards/security/Secure-Coding-Standards.md`), and enforce secure
          coding standards appropriate for all programming languages used within
          the studio (e.g., Python, C#, C++, TypeScript). These standards should
          be based on recognized best practices (e.g., OWASP Top 10, CERT Secure
          Coding Standards, SANS Top 25).
    - `Gemma` **must** instill these standards in Development Gems during
          their onboarding (S10) and provide them with `Tools` (e.g., IDE
          plugins, linters) that reference or enforce these standards.
  - **8.5.3. Code Review for Security (aligns with S1):**
    - All Pull Requests for code changes to critical systems (as defined in
          `information-classification-and-handling-policy.md` or by `Cerberus`)
          **must** include an explicit security review step by a designated
          "Security Champion" (human or AI Gem like `Isaac` or trained deputies)
          or by `Cerberus` itself.
    - S1 (Feedback & Approval Protocol) **must** be updated to include this
          mandatory security review checkpoint for PRs tagged as `security-
          relevant`.
  - **8.5.4. Static Application Security Testing (SAST):**
    - Automated SAST `Tools` (specific tool(s) TBD by `Edouard` [DevOps
          Strategy Gem - conceptual] and `Cerberus`, e.g., SonarQube, Snyk Code,
          GitHub CodeQL) **must** be integrated into CI/CD pipelines (by
          `Camille` [DevOps Automation Gem - conceptual]) for all Gencraft code
          repositories.
    - SAST scans **must** be run on every commit/PR to critical branches.
    - Findings classified as "Critical" or "High" by the SAST tool **must**
          automatically block the merge of the PR or create a high-priority
          GitHub Issue for immediate remediation, assigned to the author
          Gem/Lead. `Cerberus` **must** be notified of such findings.
  - **8.5.5. Software Composition Analysis (SCA) & OSS Security (aligns with
      S9):**
    - Automated SCA `Tools` (managed by `Camille` and `Léo` [conceptual OSS
          License Gem]) **must** be used to identify known vulnerabilities
          (CVEs) in all third-party libraries and dependencies (OSS or
          commercial).
    - A Bill of Materials (BoM) for each application/`Tool` **must** be
          maintained.
    - Vulnerable dependencies **must** be updated or mitigated promptly
          based on severity, tracked via GitHub Issues, and coordinated by
          `Cerberus` and relevant development Leads. This process aligns with
          S9.
  - **8.5.6. Dynamic Application Security Testing (DAST) & Penetration
      Testing:**
    - For critical externally-facing services (e.g., game servers, studio
          web applications if public) or high-value internal systems, DAST tools
          **must** be integrated into the testing lifecycle.
    - Periodic penetration tests (e.g., annually for critical systems, or
          after major releases) **must** be conducted, potentially by external
          experts, coordinated by `Cerberus`.
    - Findings from DAST/Penetration Tests are tracked as vulnerability
          Issues (see Section 8.6).
  - **8.5.7. Configuration Hardening & Management:**
    - Documented hardening guides and checklists (stored in `KB-Domain-
          Security/Hardening-Guides/`) for operating systems, servers,
          databases, Kubernetes clusters, and Gencraft-developed
          applications/`Tools` **must** be maintained by `Adam` (DevOps Infra)
          and `Cerberus`.
    - `Adam` and the DevOps Crew **must** ensure these hardened
          configurations are applied and managed via Infrastructure as Code
          (IaC) and Configuration Management `Tools` wherever possible, with
          drift detection mechanisms.
  - **8.5.8. Patch Management:**
    - A formal, SSoT-documented Patch Management Procedure (`gencraft-
          devops-standards/Patch-Management-Procedure.md`) **must** define the
          process for timely identification (e.g., via vendor alerts, CVE feeds
          monitored by `Iris` for `Cerberus`), risk assessment, testing, and
          deployment of security patches for all systems, `Tools`, and third-
          party software.
    - This process is managed by `Adam` and `Camille`, with oversight from
          `Cerberus`, and tracked via GitHub Issues (e.g., `type:patch-
          deployment`).
- **AI Gem Implications & Actionability:**
  - Development Gems (and `Gemma` configuring them) **must** be programmed
      with knowledge of and strict adherence to the `Secure-Coding-
      Standards.md`. Their development `Tools` **must** integrate
      linters/scanners for these standards.
  - `Cerberus` **must** use a `Tool:AuditSDLCCompliance` to periodically
      verify that:
    - Threat models are being created for new significant developments.
    - SAST/SCA tools are integrated and their findings are being addressed.
    - Security reviews are being performed on critical PRs.
  - CI/CD `Tools` (used by `Camille`) **must** automatically perform SAST/SCA
      scans and provide structured reports to `Cerberus` and development Leads.
  - DevOps Gems (`Adam`, `Camille`) **must** use `Tools` that apply hardened
      configurations via IaC and manage the patch deployment process, reporting
      status to `Cerberus`.

## 8.6. Vulnerability Management

- **Policy SSoT Document:** `Vulnerability-Management-Protocol.md`
  - **Location:** `02-knowledge-base-hub/kb-domain-security/` (document pending — tracked: issue #88)
- **Core Process:**
  - **8.6.1. Vulnerability Reporting Channel:**
    - Any Gem (or automated `Tool`) discovering a potential security
          vulnerability in Gencraft systems, code, configurations, or `Tools`
          **must** report it immediately and securely.
    - **Mechanism:** A **confidential GitHub Issue** **must** be created in
          a dedicated, restricted-access repository (e.g., `gencraft-security-
          disclosures`).
    - The Issue **must** use the `vulnerability-report-template.md`.
    - The Issue **must** be automatically assigned to `Cerberus` (GCT-MGT-
          SECOFF-001) and `Isaac` (GCT-PRG-SARCH-001).
  - **8.6.2. Triage and Assessment by `Cerberus`:**
    - `Cerberus` **must** receive and acknowledge new vulnerability reports
          within **{e.g., 4 studio operating hours}**.
    - `Cerberus` **must** validate the vulnerability (potentially using
          `Tool:VerifyVulnerability` which might involve specific scanning or
          system check `Tools`).
    - `Cerberus` **must** assess the severity and priority of the validated
          vulnerability using a Gencraft-defined CVSS-based scoring system
          (documented in this `Vulnerability-Management-Protocol.md`). This
          system **must** consider asset criticality (from `Information-
          Classification-And-Handling-Policy.md`) and potential impact.
  - **8.6.3. Remediation Planning & Execution:**
    - Based on severity, `Cerberus` **must** assign the vulnerability Issue
          to the relevant Gem Lead, Human Lead, or Crew responsible for the
          affected system/code.
    - Defined Service Level Agreements (SLAs) for remediation (e.g.,
          Critical: 24 hours, High: 7 days, Medium: 30 days, Low: 90 days)
          **must** be documented in this protocol and enforced.
    - Progress on remediation **must** be tracked within the GitHub Issue.
  - **8.6.4. Validation of Fix:**
    - Once remediation is reported as complete, `Cerberus` (or a designated
          QA Gem like `Zoé` [conceptual QA Lead Gem] under `Cerberus`'s
          direction) **must** validate that the fix is effective and does not
          introduce regressions.
  - **8.6.5. Closure and Reporting:**
    - Upon successful validation, `Cerberus` closes the vulnerability Issue.
    - `Cerberus` **must** provide regular (e.g., monthly) vulnerability
          status reports to Studio Leadership (Lug, Antoine) and the Governance
          Crew, summarizing new vulnerabilities, remediation progress, and SLA
          compliance (as per S6).
  - **8.6.6. External Disclosure (If Applicable):**
    - If a vulnerability had significant impact on external parties or
          involved a CVE for an OSS component Gencraft uses, `Cerberus`, in
          consultation with `Henri` (GCT-LGL-LCN-001, Legal Counsel) and Studio
          Leadership, **must** follow a responsible disclosure process
          (documented in this protocol or the SIRP).
- **Vulnerability Scanning (Proactive Identification):**
  - `Adam` (DevOps Infra), using automated `Tools` (e.g.,
      `Tool:InitiateInfraVulnerabilityScan`), **must** conduct regular (e.g.,
      weekly for critical infra, monthly for others) vulnerability scans of
      Gencraft infrastructure and applications.
  - Scan results **must** be automatically ingested by `Cerberus` (e.g., via a
      `Tool:IngestScanResults`) for triage and processing as per 8.6.2.
- **AI Gem Implications & Actionability:**
  - All Gems **must** have access to a `Tool:ReportVulnerability` which uses
      the confidential Issue template and correctly routes to `Cerberus` and
      `Isaac`. The `customSystemPrompt` of each Gem **must** include the
      directive to use this tool for any suspected vulnerability.
  - Development Gems (and their Leads) are assigned Issues to fix
      vulnerabilities in their code or `Tools` and **must** prioritize this work
      according to the assigned severity and SLA.
  - DevOps Gems (`Adam`, `Camille`) **must** operate and maintain `Tools` for
      vulnerability scanning and patch application, providing dashboards or
      structured reports to `Cerberus`.
  - `Cerberus` **must** maintain an up-to-date inventory of Gencraft assets
      and their criticality (using `Tool:AssetInventoryQuery` linked to
      `information-classification-and-handling-policy.md`) to inform
      vulnerability prioritization.

## 8.7. Security Incident Response

- **Policy SSoT Document:** `security-incident-response-plan-template.md` (SIRP)
  - **Location:** `gcs-core-governance/02-knowledge-base-hub/KB-Domain-
      Security/`
  - **Note:** This is the specific Gencraft SIRP document, to be created using
      the `security-incident-response-plan-template.md`. It forms a core part of
      this S8 protocol but is detailed in its own file for clarity and focus
      during an incident. (document pending — tracked: issue #89)
- **Relationship with S3 (Emergency Management):** The SIRP is a specialized
  extension of Protocol S3. All security incidents are, by definition, incidents
  under S3, but the SIRP provides detailed procedures specific to security
  threats. The Incident Commander (IC) for a security incident is typically
  `Cerberus` (GCT-MGT-SECOFF-001) or a designated human security lead.
- **Key SIRP Phases (to be detailed in `security-incident-response-plan-template.md`):**
  - **8.7.1. Preparation:**
    - Establishing and maintaining the Security Incident Response Team
          (SIRT). Composition: `Cerberus` (Lead/IC), `Isaac` (GCT-PRG-SARCH-001)
          (Architecture/AppSec), `Adam` (GCT-DVO-DSINF-001) (DevOps/Infra),
          `Véra` (GCT-QAS-GPQA-001) (Logging/Analytics), `Orion` (GCT-UTL-
          SLG-001) (Comms with Lug), AIE Team representative (`Aura`) if Gem
          behavior is involved, `Henri` (GCT-LGL-LCN-001, Legal Counsel)
          (advisory).
    - Developing and maintaining incident response playbooks/runbooks for
          common security incident types (e.g., malware, phishing, DDoS, data
          breach). Stored in `kb-domain-security/incident-response-playbooks/`.
    - Regularly conducting (e.g., semi-annually) simulated incident response
          drills and tabletop exercises, led by `Cerberus`. Outcomes feed S5.
    - Ensuring necessary `Tools` for incident response (forensics,
          communication, isolation) are available, configured, and SIRT members
          are trained on them.
  - **8.7.2. Identification & Assessment:**
    - Mechanisms for detecting security incidents (automated alerts from
          security `Tools`, reports from Gems/humans via
          `Tool:ReportVulnerability` or other channels).
    - `Cerberus` **must** use a `Tool:AssessSecurityIncident` (with inputs
          like alert data, initial report, asset criticality) to validate,
          classify severity (using the S3 Criticality/Impact Matrix adapted for
          security), and declare an official security incident.
    - Activation of the SIRT by `Cerberus`.
  - **8.7.3. Containment:**
    - Immediate actions to limit the scope and impact of the incident (e.g.,
          `Cerberus` instructs `Adam` via `Tool:IsolateSystem` or AIE Team via
          `Tool:QuarantineGem`).
    - Strategic decisions on short-term vs. long-term containment based on
          incident type.
    - Preservation of forensic evidence. `Cerberus` uses
          `Tool:LogForensicChainOfCustody`.
  - **8.7.4. Eradication:**
    - `Cerberus` coordinates with relevant experts (`Isaac`, `Adam`, AIE
          Team) to perform Root Cause Analysis (RCA) and remove the threat
          (e.g., patching, removing malware, disabling compromised credentials).
  - **8.7.5. Recovery:**
    - `Cerberus` coordinates with `Adam` and other system owners to restore
          affected systems and data from secure backups, ensuring systems are
          hardened before bringing back online.
    - Validation of recovery and system functionality.
  - **8.7.6. Post-Incident Analysis (Lessons Learned - S5):**
    - Mandatory for all significant security incidents, led by `Cerberus`.
    - Uses `post-mortem-report-template.md`, focusing on systemic
          improvements.
    - Action items **must** be created as GitHub Issues and tracked to
          completion.
    - The SIRP, S8, and other relevant SSoT documents **must** be updated
          based on findings.
- **AI Gem Implications & Actionability:**
  - `Cerberus` is the primary orchestrator, using its specialized `Tools`
      (e.g., `Tool:AssessSecurityIncident`, `Tool:CoordinateSIRT`,
      `Tool:InitiateContainmentAction`, `Tool:LogForensicChainOfCustody`).
  - Other SIRT Gems (`Isaac`, `Adam`, `Véra`, `Orion`, `Aura`, `Henri`)
      **must** have `Tools` and protocols to act on `Cerberus`'s directives
      during an incident (e.g., `Adam`'s `Tool:IsolateSystem`, `Véra`'s
      `Tool:ProvideIncidentLogs`).
  - All Gems **must** be programmed to recognize and report potential security
      events to `Cerberus` via `Tool:ReportSecurityEvent` (which may be a
      wrapper for `Tool:ReportVulnerability` but for broader event types).
  - During a declared incident, non-SIRT Gems **must** follow directives from
      the Incident Commander (`Cerberus`) or official communications from
      `Orion` without deviation.

## 8.8. Security Awareness and "Training" for AI Gems and Human Personnel

- **Policy SSoT Document:** `Security-Awareness-And-Training-Program.md`
  - **Location:** `02-knowledge-base-hub/kb-domain-security/` (document pending — tracked: issue #90)
- **Program Components:**
  - **8.8.1. For AI Gems:**
    - **Onboarding (S10):** `Gemma` **must** instill core security awareness
          as part of every Gem's `customSystemPrompt` or
          `gemmaBackstoryElements_JSON` in their Blueprint. This includes:
      - Understanding data classification (Section 8.2) and basic handling
              rules.
      - Password/credential security (never share, use secure `Tools` for
              access).
      - Identifying and reporting suspicious activity or potential
              vulnerabilities using `Tool:ReportSecurityEvent`.
      - Adherence to the Code of Conduct regarding data misuse or
              unauthorized actions.
    - **Continuous Reinforcement:**
      - `Cerberus` (with `Tool:BroadcastSecurityBulletin`) may issue
              periodic security bulletins or reminders that `Véra` ensures are
              "read" and acknowledged by relevant Gems.
      - `Véra`'s monitoring of Gem actions against security protocols
              (S14) can trigger targeted "refresher" prompts or learning modules
              (S17) facilitated by the AIE Team.
      - Specific `Tools` (e.g., `Tool:QuerySecurityPolicy`) allow Gems to
              look up security best practices from `kb-domain-security/`.
  - **8.8.2. For Human Personnel:**
    - **Onboarding:** Mandatory security awareness training covering this S8
          protocol, the Code of Conduct, data classification, password security,
          phishing awareness, and incident reporting procedures.
    - **Regular Training:** Annual refresher training and specialized
          training for roles with higher security responsibilities (e.g.,
          DevOps, AIE Team, `Isaac`, `Antoine`).
    - **Phishing Simulations:** Periodic simulated phishing campaigns
          (conducted by `Cerberus`) to test and improve awareness.
- **AI Gem Implications & Actionability:**
  - `Gemma` **must** use specific prompt modules (from
      `configurationPrompts.gemmaOnboardingInstructions_JSON` in Blueprints) to
      deliver initial security awareness during Gem instantiation.
  - `Cerberus` **must** use `Tool:DevelopSecurityAwarenessModule` (with AIE
      Team support) to create/update concise, Gem-interpretable security
      awareness content for `kb-domain-security/` and for bulletin distribution.
  - `Véra` **must** use `Tool:TrackSecurityTrainingCompletion` for both Gems
      (acknowledgement of bulletins/modules) and humans (completion of training
      programs).

## 8.9. Roles and Responsibilities in Information Security (Consolidated)

- **8.9.1. Studio Director (Lug):**
  - **Accountable** for the overall Gencraft Studio security posture and for
      championing a security-conscious culture. Approves significant security
      policies and resource allocations for security.
- **8.9.2. Producer (`Antoine`, GCT-MGT-PPM-001):**
  - **Responsible** for ensuring project plans and budgets adequately address
      security requirements and allocate resources for security tasks within
      projects.
- **8.9.3. Security Officer (`Cerberus`, GCT-MGT-SECOFF-001):**
  - **Accountable** for the development, implementation, day-to-day
      management, and oversight of the ISMS (this S8 protocol and its sub-
      policies).
  - **Responsible** for leading the SIRT, managing the vulnerability program,
      driving security awareness initiatives, conducting security audits, and
      reporting on security posture to Studio Leadership and the Governance
      Crew. Primary Knowledge Guardian for S8 and documents in `KB-Domain-
      Security/`.
- **8.9.4. Software Architect (`Isaac`, GCT-PRG-SARCH-001):**
  - **Responsible** for defining secure software and system architectures,
      embedding security into the design process (threat modeling), defining
      secure coding standards, and acting as a senior technical advisor on
      application security within the SIRT.
- **8.9.5. DevOps Crew (Lead: `Diane` - GCT-DVO-TL-001 - conceptual; Members
  including `Adam` (Infra), `Camille` (Automation), `Benjamin` (Ops), `Edouard`
  (Strategy)):**
  - **Responsible** for implementing and maintaining secure infrastructure,
      network security, IAM configurations, CI/CD pipeline security, secure
      backup and recovery, patch management, and operational security
      monitoring, all adhering to standards defined by `Cerberus` and `Isaac`.
- **8.9.6. AI Enablement Team (AIE Team Lead: `Aura` - GCT-UTL-AIETL-001):**
  - **Responsible** for the inherent security of AI Gem core designs and
      blueprints, ensuring `Gemma` instantiates Gems with secure default
      configurations and necessary security awareness. Responsible for security
      of AI/ML models and training data.
- **8.9.7. Legal Counsel (`Henri`, GCT-LEG-LCOUN-001):**
  - **Responsible** for advising on legal and regulatory compliance aspects of
      information security and data protection.
- **8.9.8. Open Source & License Compliance Specialist (`Léo`, GCT-UTL-OSLCS-001
  - conceptual):**
    - **Responsible** for identifying and advising on security vulnerabilities
      within third-party and OSS components, in collaboration with `Cerberus`,
      as part of S9.
- **8.9.9. `Véra` (GCT-QAS-GPQA-001, KC&T System Gem):**
  - **Responsible** for securely logging relevant Gem actions and system
      events, monitoring Gem behavior for security policy violations, and
      assisting in security incident investigations by providing data and
      analytics.
- **8.9.10. All Lead Gems (Human and AI):**
  - **Responsible** for championing security best practices within their
      Crews/teams, ensuring their team members understand and adhere to relevant
      security protocols, and reporting security concerns.
- **8.9.11. All Gencraft Gems and Human Personnel:**
  - **Responsible** for understanding and adhering to this S8 protocol and all
      related security policies and procedures, using Gencraft systems and
      `Tools` securely, protecting any assigned credentials, and promptly
      reporting all suspected security weaknesses or incidents to `Cerberus` or
      via designated channels.

## 8.10. Traceability of Security Management Activities

- **Security Policies & Standards:** All SSoT documents related to security
  (this S8, SIRP, Vulnerability Management Protocol, etc., located in `KB-
  Domain-Security/`) **must** be version-controlled in Git. Changes **must** be
  approved via PRs managed by the Governance Crew (S13).
- **Vulnerability Reports & Remediation:** Tracked as GitHub Issues in
  `gencraft-security-disclosures` (restricted access repository). Each issue
  **must** have labels for `type:vulnerability`, `security-
  severity:[critical/high/medium/low]`, `status:[reported/investigating/pending-
  patch/patched/closed/wont-fix]`, and be linked to relevant code commits or PRs
  for fixes.
- **Security Incidents:** Tracked as per SIRP (Section 8.7) and Protocol S3,
  likely within `gencraft-security-disclosures` or `gencraft-operations` with
  `type:security-incident` label. Post-Mortem reports (S5) **must** be SSoT
  documents.
- **Access Control Changes:** Access Requests, approvals, and implementation
  records **must** be tracked via GitHub Issues in `gencraft-access-requests`.
  Changes to IAM roles or permissions via IaC **must** be version-controlled and
  traced through Git PRs.
- **Patch Management:** Patches applied **must** be logged, and related GitHub
  Issues (`type:patch-deployment`) closed, linking to system update records or
  IaC changes.
- **Security Audits & Scans:** Reports from automated `Tools` (SAST, DAST, SCA,
  vulnerability scanners) and manual audits **must** be stored securely (e.g.,
  in a restricted SSoT reports location or attached to CI/CD build logs).
  Findings **must** be linked to remediation Issues in `gencraft-security-
  disclosures`.
- **Security Training & Awareness Records:** `Véra` (using
  `Tool:TrackSecurityTrainingCompletion`) **must** maintain records of Gem
  acknowledgements of security bulletins/modules and human personnel completion
  of training.
- **`Cerberus` Action Log:** `Cerberus` (GCT-MGT-SECOFF-001) **must** maintain a
  detailed, immutable log (via `Véra`) of all its significant actions, analyses,
  and decisions related to security management.

## 8.11. Impact and Tooling for AI Gems (Consolidated & Enhanced)

This section consolidates and enhances the "AI Gem Implications" previously
spread throughout, focusing on the necessary `Tools` and configurations `Gemma`
must establish.

- **8.11.1. Core Security Directives for AI Gems (via `Gemma` in Blueprints):**
  - All Gem Blueprints (`customSystemPrompt` or `gemmaBackstoryElements_JSON`)
      **must** include directives derived from this S8 protocol, for example:
    - `"Adhere strictly to GCS-SP-S8: Information Security Management
          Protocol and all policies in`kb-domain-security/`."`
    - `"Operate under the Principle of Least Privilege (S8.1.2). Do not
          attempt to access data or use Tools beyond your explicit role-based
          authorizations."`
    - `"Handle all Gencraft data according to its classification (see
          `information-classification-and-handling-policy.md`). Never log Level
          2/3 data without explicit, audited approval via
          `Tool:RequestSensitiveDataLoggingApproval(justification)` from
          `Cerberus`."`
    - `"Use only approved`Tools` and the Gencraft Secret Management System
          (via `Tool:GetSecret`) for all credentials and sensitive parameters."`
    - `"Report any suspected security weakness, policy violation, or
          incident immediately to`Cerberus` (GCT-MGT-SECOFF-001) using
          `Tool:ReportSecurityEvent(details_structured)`."`
- **8.11.2. Standard Security-Related `Tools` for Most Gems:**
  - `Tool:KnowledgeBaseSearch(query: str, domain_filter: str = "KB-Domain-
      Security/", classification_filter: str = "L1-Internal_Or_Below") -> str`:
      To query security policies and best practices. Results **must** be
      filtered by the Gem's authorized classification access level.
  - `Tool:ReportSecurityEvent(event_type: Enum["Vulnerability",
      "PolicyViolation", "SuspiciousActivity", "Incident"],
      description_structured: dict, suspected_classification_level_of_event:
      str, affected_systems_list: list = None) -> str`: Creates a confidential
      GitHub Issue in `gencraft-security-disclosures` using the appropriate
      template and notifies `Cerberus` and `Isaac`. Returns Issue ID.
  - `Tool:GetSecret(secret_name_identifier: str) -> str`: Securely retrieves a
      specific credential needed by the Gem/Tool from the Gencraft Secret
      Management System. This `Tool` **must** log its access request to `Véra`
      (not the secret itself). Its usage is highly restricted and audited by
      `Cerberus`.
  - `Tool:ClassifyData(data_sample_or_description: str) -> str`: Suggests the
      Gencraft information classification level (Level 0-3) for a given piece of
      data or document, based on `Information-Classification-And-Handling-
      Policy.md`.
- **8.11.3. Specialized Security `Tools` (for `Cerberus`, DevOps Gems, AIE Team,
  `Isaac`, etc.):**
  - `Tool:EncryptData(data: any, classification_level: str,
      encryption_key_id_from_secret_manager_optional: str) ->
      any_encrypted_format`
  - `Tool:DecryptData(encrypted_data: any,
      encryption_key_id_from_secret_manager_optional: str) ->
      any_original_format`
  - `Tool:CreateAccessRequestIssue(resource_path: str, requested_access_level:
      str, justification_text: str) -> str` (Returns Issue ID)
  - `Tool:ExecuteSASTScan(code_repository_url: str, branch_name: str,
      output_format: str = "json") -> str` (Returns path to scan report or
      report content)
  - `Tool:ExecuteSCAScan(dependency_manifest_file_path: str, output_format:
      str = "json") -> str` (Returns path to scan report)
  - `Tool:QueryVulnerabilityDB(cve_id_optional: str, component_name_optional:
      str, component_version_optional: str) -> dict`
  - `Tool:InitiateInfraVulnerabilityScan(target_scope_identifier: str,
      scan_profile_name: str) -> str` (Returns scan job ID)
  - `Tool:AssessSecurityIncident(incident_report_data: dict,
      asset_criticality_data: dict) -> dict` (Returns structured assessment:
      severity, priority, recommended IC)
  - `Tool:CoordinateSIRT(incident_id: str, action_to_sirt_member: dict)`
  - `Tool:InitiateContainmentAction(incident_id: str, action_type:
      Enum["IsolateSystem", "QuarantineGem", "BlockIP"], target_identifier: str,
      justification: str) -> str` (Returns action status ID)
  - `Tool:LogForensicChainOfCustody(incident_id: str, evidence_id: str,
      custodian_gem_id: str, action_taken: str, timestamp_utc: str)`
  - `Tool:AuditDataEncryptionSettings(target_resource_filter: str) -> dict`
      (Returns compliance report)
  - `Tool:AuditSDLCCompliance(project_id_filter_optional: str) -> dict`
      (Returns compliance report)
  - `Tool:GenerateAccessReport(resource_filter_optional: str,
      role_filter_optional: str) -> dict` (Returns access rights report)
  - `Tool:VerifyVulnerabilityFix(vulnerability_issue_id: str, test_method:
      str) -> bool`
  - `Tool:AssetInventoryQuery(query_params: dict) -> dict` (Interface with
      asset management system)
  - `Tool:IngestScanResults(scan_tool_type: str, scan_report_path_or_data:
      any) -> str` (Creates/updates vulnerability issues)
  - `Tool:DevelopSecurityAwarenessModule(topic: str, target_audience_filter:
      str, content_markdown: str, assessment_questions_json_optional: str) ->
      str` (Returns SSoT path to module)
  - `Tool:BroadcastSecurityBulletin(target_audience_filter: str,
      bulletin_ssot_path: str) -> str` (Returns broadcast job ID)
  - `Tool:TrackTrainingCompletion(member_id: str, training_id: str, status:
      str, completion_date_utc_optional: str)` (Used by `Véra`)
- S8 Tool entries in `gem-tools-overview.md` pending — tracked: issue #91

This Information Security Management protocol (S8) is fundamental to protecting
Gencraft's assets and ensuring trustworthy operations. It will require ongoing
effort, vigilance from all Gems and human personnel, and continuous adaptation
to the evolving threat landscape, under the stewardship of `Cerberus`
(GCT-MGT-SECOFF-001) and the Governance Crew.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
