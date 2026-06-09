---
docId: SEC-STAN-002
title: Sec 002 Iac Scanning Tool Selection
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: "Gencraft will standardize on TFSec as the primary IaC security scanning\
  \ tool for OpenTofu configurations. This decision prioritizes TFSec's specialization\
  \ in IaC, its cloud provider coverage, and alignment with Gencraft\u2019s technical\
  \ and operational principles."
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - iac-scanning-tool-selection
  - tfsec
  - open-tofu
  - security-scanning
  - aws
  - cloud-security
  - gencraft
  scope: studio
  domain: security
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/security/standards/SEC-STAN-002.sec-002-iac-scanning-tool-selection.md
---
## 1. Objective

This document records the decision-making process and the final selection of the standard tool(s) for
Infrastructure as Code (IaC) security scanning within Gencraft. The goal is to choose a tool (or set of
tools) that effectively identifies security misconfigurations and vulnerabilities in OpenTofu code,
integrates well with our CI/CD pipelines and local development workflows (pre-commit hooks), and aligns
with Gencraft's technical, security, and operational principles.

## 2. Context and Problem Statement

As Gencraft increasingly relies on IaC (OpenTofu) to manage its infrastructure (ref: PROJ-103 [cite:
devops_transformation_plan_proj103]), ensuring the security of this code is paramount. Static Analysis
Security Testing (SAST) for IaC helps detect vulnerabilities before deployment, aligning with a
"shift-left" security approach. iac-007-iac-static-analysis-standard.md [cite:
iac_static_analysis_standard_v1_1_and_report] mandates the use of such tools but leaves the specific tool
choice to be formalized in this document. We need to select a primary tool for this purpose, to be
integrated into both local development (via TOOL_004_Git_Hooks_Standard.md [cite:
tool_004_git_hooks_standard_v1_3_pure_raw_md]) and CI/CD pipelines (CICD_001_Baseline_Workflow_Guidance.md
[gcs-core-governance/cicd/CICD_001_Baseline_Workflow_Guidance.md]).

## 3. Considered Options

The following tools were considered based on their capabilities for scanning OpenTofu/Terraform code,
community support, open-source nature (UOP 2.7 [gcs-core-governance/00-studio-vision-and-principles/
universal-gem-operating-principles.md]), and existing mentions or considerations within Gencraft
documentation:

TFSec (<https://aquasecurity.github.io/tfsec/>)

Description: Specialized SAST tool for Terraform/OpenTofu code.

Pros: Strong focus on IaC, comprehensive rule set for major cloud providers (AWS, Azure, GCP) &
Kubernetes, known for speed and ease of CI/CD integration. Apache 2.0 license. Good coverage of CIS Benchmarks.

Cons: Limited to IaC; does not scan application code or container images. Custom rule creation can be less
straightforward than some alternatives.

Checkov (<https://www.checkov.io/>)

Description: Broader IaC scanner supporting Terraform/OpenTofu, CloudFormation, Kubernetes, ARM templates, Serverless framework.

Pros: Extensive policy library, graph-based analysis for contextual understanding of misconfigurations,
supports custom policies in Python. Apache 2.0 license.

Cons: Can be slightly slower than TFSec for pure Terraform/OpenTofu scans. Python custom policies might
add a language dependency if
not already standard for DevOps tooling scripts.

Trivy (<https://aquasecurity.github.io/trivy/>)

Description: Comprehensive, all-in-one open-source security scanner.

Pros: Scans IaC (Terraform/OpenTofu, Kubernetes, etc.), container images (OS packages, language
dependencies), filesystems, Git repositories for vulnerabilities and secrets. Potential for tool
consolidation. Apache 2.0 license.

Cons: IaC scanning is a more recent addition compared to its vulnerability scanning capabilities; depth of
IaC-specific rules might be less than dedicated tools like TFSec or Checkov initially.

## 4. Evaluation Criteria

The selected tool(s) were evaluated against the following criteria, weighted by Gencraft's priorities:

Effectiveness (Coverage & Accuracy) - High Priority:

Breadth and depth of security checks specifically for OpenTofu and Gencraft's primary cloud provider(s) (assume AWS initially).

Accuracy: Low false positive and false negative rates.

Up-to-date rule sets reflecting current threats and best practices.

Support for relevant compliance frameworks (e.g., CIS Benchmarks).

Support for custom policies/rules relevant to Gencraft's specific security posture.

Integration & Automation - High Priority:

Ease of integration into GitHub Actions CI/CD pipelines.

Suitability for local pre-commit hooks (performance, output clarity).

Availability of official or well-maintained pre-commit hooks.

Quality of CLI output for parsing and automation by AI Gems or scripts (e.g., SARIF support).

Usability & Actionability - Medium Priority:

Clarity of scan reports and findings.

Actionable remediation advice and links to documentation.

Ease of suppressing false positives or specific findings with a clear, auditable justification process (as per IAC_007).

Performance - Medium Priority:

Speed of scanning for both local (pre-commit) and CI/CD feedback loops, to avoid impacting developer experience negatively.

Customization & Extensibility - Medium Priority:

Ability to add custom Gencraft-specific security policies or rules easily.

Flexibility in configuring rule severity and behavior.

Community, Support & Licensing - Medium Priority:

Activity and responsiveness of the open-source project.

Quality of official documentation.

Permissive open-source license (MIT, Apache 2.0 preferred as per UOP 2.7).

Alignment with Gencraft Stack & Principles - High Priority:

Strong compatibility with OpenTofu.

Alignment with "Everything as Code" and potential for "AI-enabled" enhancements (e.g., AI Gems parsing results).

## 5. Decision

Decision: Gencraft will standardize on TFSec as the primary IaC security scanning tool for OpenTofu
configurations for the initial implementation within PROJ-103.

Justification for TFSec:

Effectiveness for IaC: TFSec's specialization in Terraform/OpenTofu provides a robust and focused set of
rules tailored to IaC misconfigurations, which is our immediate priority for securing new and refactored
infrastructure code. Its cloud provider coverage (especially AWS) and CIS benchmark alignment are strong.
Its maturity in IaC-specific rules is perceived as higher than Trivy's current IaC capabilities for depth.

Integration & Performance: It is widely recognized for its speed and straightforward integration into both
CI/CD pipelines and local pre-commit hooks, offering fast feedback.

Usability: Its output is generally clear and designed for developer consumption.

Community & Licensing: It has an active community and an Apache 2.0 license, aligning with UOP 2.7.

Focus for PROJ-103: For the immediate task of securing our OpenTofu code during and after the PROJ-103
migration, TFSec offers the most direct and mature solution for IaC-specific threats. Its perceived
simplicity for pure OpenTofu scanning is an advantage for rapid adoption.

Customization: While custom rule creation might be less direct than Checkov's Python, TFSec does support
custom checks and flexible configuration.

Consideration for Trivy & Checkov:

Trivy: Its comprehensive nature is highly appealing for long-term tool consolidation (IaC, container
scanning, dependency scanning, secrets). Trivy WILL BE the Gencraft standard for container image
vulnerability scanning and SHOULD BE evaluated for secret scanning in repositories (potentially via a
separate standard SEC_00X_Secret_Scanning_Tool_Standard.md). Its IaC capabilities will be formally
re-evaluated (see Section 8). However, Cerberus retains the prerogative to utilize additional or
alternative scanning tools (including Trivy or Checkov) for periodic, in-depth security audits or specific
investigations, without these necessarily becoming the mandated tool for daily CI/developer workflows
unless a future ADR revises this standard.

Checkov: A very strong contender with excellent features, including graph-based analysis and Python custom
policies. While powerful, the perceived slight advantage of TFSec in out-of-the-box speed and simplicity
for pure OpenTofu scanning led to TFSec being favored for initial standardization for PROJ-103. Checkov
remains a viable alternative for future re-evaluation or for specific use cases requiring its advanced
features.

## 6. Implementation Details & Configuration

SSoT for TFSec Configuration (Action for Cerberus, Édouard): While TFSec can be run with CLI flags, a
Gencraft standard configuration file (e.g., devops-standards/iac/templates/.tfsec-config.yml or .tfsec/
config.json at repo root) SHOULD be created if significant global overrides, custom severities,
exclusions, or minimum severity settings are desired beyond what IAC_007 specifies for CI failure. This
centralizes Gencraft-specific TFSec behavior and will be managed by Cerberus for security aspects and
Édouard for DevOps strategy.

CI/CD Integration (Action for Camille - Gem AB): As per iac-007-iac-static-analysis-standard.md [cite:
iac_static_analysis_standard_v1_1_and_report], TFSec will be a mandatory check, failing the pipeline on
CRITICAL or HIGH severity findings not formally excepted. Output SHOULD be in SARIF format, if possible,
for GitHub Security tab integration.

Local Usage (Action for Camille - Gem AB): Integrated via pre-commit hooks as per
TOOL_004_Git_Hooks_Standard.md [cite: tool_004_git_hooks_standard_v1_3_pure_raw_md], using the SSoT configuration.

Exception Management: As per Section 4 of iac-007-iac-static-analysis-standard.md [cite: iac_static_analysis_standard_v1_1_and_report].

## 7. Responsibilities

Cerberus (Security Officer Gem):

Owns the final decision on security tool efficacy and risk acceptance for IaC.

Defines/approves baseline security configurations, rule severities, and custom checks for TFSec.

Manages the security finding remediation process and exception approvals related to IaC scans.

Leads the periodic re-evaluation of this tool choice.

Édouard (Gem AD - DevOps Strategy):

Owns this decision document (SEC_002).

Facilitates tool evaluation and ensures alignment with overall DevOps strategy and other standards.

Co-responsible for creating and maintaining the SSoT TFSec configuration template.

Benjamin (Gem AC - Infrastructure Specialist):

Implements and uses TFSec in daily IaC development.

Provides feedback on TFSec usability, accuracy, and performance in practice.

Assists in developing custom TFSec checks if needed.

Camille (Gem AB - Automation Specialist):

Integrates TFSec into CI/CD pipelines and pre-commit hook SSoT configurations.

Ensures scan results are correctly processed, reported (e.g., SARIF), and pipeline failures are triggered
appropriately based on findings.

## 8. Next Steps / Future Considerations

Formal Approval: This SEC_002 decision document is considered approved as of v1.2.

SSoT Configuration Creation (Action for Cerberus, Édouard): Create the SSoT TFSec configuration template
(devops-standards/iac/templates/.tfsec-config.yml or similar) if deemed necessary for Gencraft-wide
settings.

Update iac-007-iac-static-analysis-standard.md (Action for Édouard): Explicitly name TFSec as the standard
tool and reference this SEC_002 document for the selection rationale.

Update TOOL_004_Git_Hooks_Standard.md SSoT (Action for Camille): Ensure the SSoT .pre-commit-config.yaml
template in TOOL_004 includes TFSec with the standard configuration.

Define Update Process (Action for Cerberus, Édouard): Define a clear process for updating TFSec's rule
database/version and reviewing new checks added by the tool. This should be part of the SSoT TFSec
configuration or a related operational guide.

Periodic Re-evaluation (Action for Édouard, Cerberus): Schedule an annual (or sooner, if significant
market changes occur) re-evaluation of this tool choice, specifically re-assessing Trivy's and Checkov's
IaC capabilities against TFSec and Gencraft's evolving needs. Track via gencraft-operations Issue (e.g.,
'# TBD-IaC-Tool-Reval-YYYY').

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
