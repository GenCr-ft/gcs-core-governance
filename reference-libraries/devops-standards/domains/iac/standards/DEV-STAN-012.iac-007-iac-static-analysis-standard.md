---
docId: DEV-STAN-012
title: Iac 007 Iac Static Analysis Standard
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This standard mandates the use of static analysis tools, TFLint and TFSec
  (or equivalent), for OpenTofu infrastructure as code within Gencraft. It aims to
  proactively detect errors, best practice deviations, and security vulnerabilities
  before deployment, integrated into CI/CD pipelines for automated validation.
last_updated_date: '2026-06-02'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - iac-static-analysis
  - open-tofu
  - tflint
  - tfsec
  - infrastructure-as-code
  - security-standards
  - gencraft
  - automation
  scope: studio
  domain: devops
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/iac/standards/DEV-STAN-012.iac-007-iac-static-analysis-standard.md
---
## 1. Objective

This standard mandates the use and defines the configuration of static analysis tools `TFLint` and `TFSec`(or an approved equivalent as per `SEC_00X_IaC_Scanning_Tool_Selection.md`) for all Infrastructure as Code (IaC) written with OpenTofu within Gencraft. The objective is to proactively detect syntax errors, deviations from best practices, non-compliance with Gencraft IaC standards (ref: `iac-004-clean-iac-principles.md`), and security vulnerabilities before infrastructure deployment. This standard aims to be directly actionable by AI Gems involved in IaC development and CI/CD pipeline management.

## 2. Scope

This standard applies to all OpenTofu code within Gencraft-managed repositories, including but not limited to:

- `gencraft-studio-iac`
- `gencraft-game-aethel-iac`
- Any other repositories containing OpenTofu-based IaC as identified by `Adam` (Gem AA).

## 3. Standard Tools & Configuration

The Gencraft studio standardizes on the following tools for IaC static analysis. Minimum versions are specified in `IAC_001_Tooling_Standard_OpenTofu.md` and verified by `validate_gft_devops_environment_proj103.sh` [cite: devops_env_validation_script_proj103].

### 3.1. `TFLint`

- **Objective:** General linting of OpenTofu code, error detection, identification of provider-specific (e.g., AWS, Azure, GCP) best practice violations, and enforcement of custom Gencraft IaC rules.
- **Installation:** As per official documentation ([https://github.com/terraform-linters/tflint#installation](https://github.com/terraform-linters/tflint#installation)).
- **Configuration:**
  1. **Central Configuration File:** A `.tflint.hcl` configuration file MUST be present at the root of each IaC repository.
  2. **SSoT Template (Action for `Édouard` - Gem AD):** The baseline `.tflint.hcl` template MUST be created and maintained at `templates/.tflint.hcl`. Projects MUST use this template as a starting point and MAY extend it with project-specific needs, subject to review by `Édouard` (Gem AD).
  3. **Mandatory Rulesets:** The SSoT template MUST enable the Gencraft primary cloud provider's ruleset (e.g., `aws`) and the `terraform` core ruleset by default.
  4. **Custom Gencraft Rules:**
  - Custom `TFLint` rules specific to Gencraft's IaC best practices (e.g., enforcing specific tagging patterns not covered by `iac-002-cloud-resource-tagging-standard.md` [gcs-core-governance/iac/IAC_002_Cloud_Resource_Tagging_Standard.md], naming conventions for modules as per `IAC_00X_Naming_Conventions.md` To Be Created) MAY be developed.
  - **SSoT for Custom Rules (Action for `Édouard`/`Benjamin`):** `gcs-core-governance/iac/custom-rules/tflint/` MUST be the SSoT for storing these rules.
  - **Development Process:** New custom rules MUST be proposed via an Issue in `gcs-core-governance` (template: `../../gcs-core-governance/02-knowledge-base-hub/templates/issue-templates/knowledge-proposal-template.md` [gcs-core-governance/02-knowledge-base-hub/Templates/Issue-Templates/knowledge-proposal-template.md]), developed (with test cases), tested thoroughly, and approved by `Édouard` (Gem AD) and `Benjamin` (Gem AC) before being added to the SSoT and considered for inclusion in the base `.tflint.hcl` template.
  - **CI/CD Integration (Action for `Camille` - Gem AB):**
  1. `TFLint` MUST be executed as a mandatory validation step in all CI/CD pipelines for IaC (ref:Action A2.4 of PROJ-103 [cite: devops_transformation_plan_proj103]).
  2. The pipeline MUST use the repository's `.tflint.hcl` for configuration.
  3. A `TFLint` execution that reports any errors (exit code non-zero) MUST fail the CI/CD pipeline build, preventing merge or deployment.
  - **Local Usage (Action for IaC Contributors & `Camille` - Gem AB for hook config):**
  1. All IaC contributors (Gems or humans) MUST run `tflint` locally before committing changes.
  2. This check MUST be integrated into the Git pre-commit hooks as defined in `../tooling/tool-004-git-hooks-standard.md` (using the SSoT `.pre-commit-config.yaml` template from `gencraft-devops-automation/git-hooks/templates/`).

### 3.2. `TFSec` (or Approved Alternative, e.g., `Checkov`)

- **Objective:** Static security analysis of OpenTofu code to identify security misconfigurations, deviations from security best practices, and potential vulnerabilities based on a comprehensive ruleset.
- **Tool Selection SSoT (Action for `Édouard`, `Cerberus`):** The officially selected tool (TFSec, Checkov, or other) MUST be documented in `gcs-core-governance/security/SEC_00X_IaC_Scanning_Tool_Selection.md` (To Be Created). This standard assumes `TFSec` until that document specifies otherwise.
- **Installation:** As per official documentation of the selected tool (e.g., TFSec: [https://aquasecurity.github.io/tfsec/latest/getting-started/installation/](https://aquasecurity.github.io/tfsec/latest/getting-started/installation/)).
- **Configuration:**
  1. **Baseline Configuration (Action for `Édouard`/`Cerberus`):** A baseline Gencraft configuration for the selected tool (e.g., specifying minimum severity to report, custom checks if any, ignored rules with justification) MAY be defined and versioned.
  2. **SSoT Template (if applicable):** `gcs-core-governance/iac/templates/.tfsec-config.yml` (or equivalent for the chosen tool - To Be Created by `Édouard`/`Cerberus` if a central config is used). Otherwise, configuration is per-repository or via CLI flags in CI.
  3. **Severity Thresholds for CI Failure:** By default, any findings with severity `CRITICAL` or `HIGH` MUST fail the CI/CD pipeline. This threshold MAY be adjusted in the SSoT template or CI pipeline configuration, but any lowering of this threshold requires explicit approval from `Cerberus` (Security Officer Gem) and MUST be documented with justification.
- **CI/CD Integration (Action for `Camille` - Gem AB):**
  1. The selected IaC security scanner MUST be executed as a mandatory validation step in all CI/CD pipelines for IaC.
  2. The pipeline MUST use the repository's or the centrally defined SSoT configuration for the scanner.
  3. A scanner execution that reports findings exceeding the defined severity threshold (default: CRITICAL or HIGH) and not covered by an approved exception (see Section 4) MUST fail the CI/CD pipeline build.
- **Local Usage (Action for IaC Contributors & `Camille` - Gem AB for hook config):**
  1. All IaC contributors MUST run the selected IaC security scanner locally before committing changes.
  2. This check MUST be integrated into the Git pre-commit hooks as defined in `../tooling/tool-004-git-hooks-standard.md`.

## 4. Management of False Positives and Exceptions

Acknowledging that static analysis tools can produce false positives or identify issues that are acceptable under specific, justified circumstances.

1. **Justification Process:** - Any `TFLint` rule violation or IaC security scanner finding that is proposed to be ignored MUST first be discussed in a GitHub Issue within the relevant IaC repository or in `gencraft-operations`. - The Issue MUST detail the finding, the context, the justification for ignoring it, potential risks, and any mitigating controls.
2. **Approval:** - Non-security related `TFLint` exceptions: Approval by `Benjamin` (Gem AC) or `Édouard` (Gem AD) is required in the GitHub Issue. - Security-related exceptions (all `TFSec`/security scanner findings): Approval by `Cerberus`(Security Officer Gem, or their delegate) is MANDATORY in the GitHub Issue.
3. **Inline Comment Format:** Once approved, the finding MAY be ignored using an inline comment directly above the line of code causing the finding. The comment MUST follow this exact format:

```yaml
  # GFT_IGNORE[TOOL_NAME][RULE_ID_OR_CODE]: Reason: <Concise justification, max 120 chars>. ApprovedBy: @<ApproverGemID>. Expires: YYYY-MM-DD (or N/A for permanent). Ticket: <FullLinkToGitHubIssue>
  # Example: # GFT_IGNORE[TFSEC][AWS006]: Reason: S3 for public, non-sensitive website assets, default S3 encryption sufficient. ApprovedBy: @Cerberus. Expires: N/A. Ticket: https://github.com/GenCr-ft/gencraft-studio-iac/issues/123`
  - `TOOL_NAME`: `TFLINT` or the name of the security scanner (e.g., `TFSec`, `Checkov`).
  - `RULE_ID_OR_CODE`: The specific identifier of the rule/finding from the tool.
  - `<ApproverGemID>`: The GemID of the approver (e.g., `@GCT-MGT-SECOFF-001` for `Cerberus`).
  - `Expires`: `YYYY-MM-DD` for temporary exceptions, `N/A` for permanent (rarely accepted for security issues).
  - `<FullLinkToGitHubIssue>`: Direct link to the GitHub Issue where the exception was discussed and approved.
```

1. **Tool-Specific Ignore Mechanisms:** Utilize the tool's native mechanism (e.g., `tfsec:ignore:AWS006`, `//tflint-ignore: L001`) _in conjunction with_ the mandatory `GFT_IGNORE` comment. The `GFT_IGNORE` comment is for auditability; the tool-specific comment silences the tool.
2. **Central Exception Tracking (Action for `Benjamin` - Gem AC, `Cerberus`):** - All approved exceptions MUST be logged by the approver in a central SSoT: `gencraft-operations/iac-scan-exceptions.md` (To Be Created by `Benjamin`/`Cerberus`). - This Markdown log MUST be structured with columns: `Date Logged`, `Repository`, `File:Line`, `Tool`,`Rule ID`, `Justification Summary`, `Approver GemID`, `Ticket Link`, `Expiry Date`. - This log facilitates auditing and periodic review. An AI Gem (`Véra` or a dedicated audit Gem) MAY be tasked to parse this log and the codebase to verify consistency.
3. **Periodic Review (Action for `Benjamin` - Gem AC, `Cerberus`, `Édouard` - Gem AD):** - A review of all active exceptions in `gencraft-operations/iac-scan-exceptions.md` MUST be conducted quarterly by `Benjamin` (for TFLint) and `Cerberus` (for security findings), with oversight from `Édouard`. - The review will assess the continued validity of each exception. Expired or no-longer-valid exceptions MUST be remediated (code fixed or exception removed). - Output: A brief report summarizing the review and actions taken, stored in `gencraft-studio-reports/security/iac_exception_review_YYYY_QX.md`.

## 5. Future Exploration: `Trivy`

- **Context:** `Trivy` offers broad scanning capabilities, including IaC.
- **Action Required (Tracked in `gencraft-operations` Issue #TBD-IaC-TrivyEval, assigned to `Édouard`, `Cerberus`):**
  1. Conduct a formal evaluation (Proof of Concept - PoC) of `Trivy` for IaC scanning (post-PROJ-103 initial stabilization).
  2. Compare its IaC rule coverage, depth, usability, and CI/CD integration against `TFSec` (or current tool).
  3. Evaluate the benefits of consolidating on `Trivy` vs. using specialized tools.
  4. Document findings and the final decision in `gcs-core-governance/security/SEC_00X_IaC_Scanning_Tool_Selection.md`.

## 6. Responsibilities

- **`Édouard` (Gem AD - DevOps Strategy):**
  - Maintenance of this IAC_007 standard.
  - Creation and maintenance of the SSoT for `.tflint.hcl` and other IaC analysis tool configuration templates (e.g., `gcs-core-governance/iac/templates/`).
  - Leading the development and maintenance of SSoT for custom Gencraft `TFLint` rules (e.g., `gcs-core-governance/iac/custom-rules/tflint/`).
  - Leading the evaluation of new/alternative IaC scanning tools (e.g., Trivy).
- **`Benjamin` (Gem AC - Infrastructure Specialist):**
  - Ensuring consistent application of this standard across all Gencraft IaC repositories.
  - Reviewing and approving non-security related `TFLint` exceptions, documenting them in the GitHub Issue and the central log.
  - Co-managing and populating the central `gencraft-operations/iac-scan-exceptions.md` log for TFLint.
  - Implementing and updating IaC code to address findings from scanners.
- **`Camille` (Gem AB - Automation Specialist):**
  - Integration and maintenance of `TFLint` and `TFSec` (or chosen alternative) execution steps in all relevant CI/CD pipelines.
  - Ensuring pipeline failures occur based on the defined criteria in this standard.
  - Configuration of pre-commit hooks for these tools as per `../tooling/tool-004-git-hooks-standard.md`.
- **`Cerberus` (Security Officer Gem):**
  - Reviewing and approving security-related exceptions (`TFSec` findings), documenting them in the GitHub Issue and the central log.
  - Co-managing and populating the central `gencraft-operations/iac-scan-exceptions.md` log for security findings.
  - Auditing the overall effectiveness of the IaC static analysis security posture and the exception management process.
- **All IaC Contributors (Gems and Humans):**
  - Adherence to this standard.
  - Running `TFLint` and `TFSec` (or chosen alternative) locally before committing/pushing IaC changes.
  - Addressing all findings reported by the tools or obtaining a formal, documented exception as per Section 4.

## 7. References & SSoTs

- **Tool Documentation:**
  - TFLint: [https://github.com/terraform-linters/tflint](https://github.com/terraform-linters/tflint)
  - TFSec: [https://aquasecurity.github.io/tfsec/latest/](https://aquasecurity.github.io/tfsec/latest/)
  - Trivy (for future exploration): [https://aquasecurity.github.io/trivy/latest/](https://aquasecurity.github.io/trivy/latest/)
- **Gencraft Standards:**
  - `gcs-core-governance/iac/IAC_001_Tooling_Standard_OpenTofu.md`
  - `iac-004-clean-iac-principles.md`
  - `../tooling/tool-004-git-hooks-standard.md`
  - `gcs-core-governance/security/SEC_00X_IaC_Scanning_Tool_Selection.md` (To Be Created by `Édouard`, `Cerberus`)
- **Gencraft Configuration Templates & Custom Rules:**
  - `templates/.tflint.hcl` (To Be Created by `Édouard`)
  - `gcs-core-governance/iac/templates/.tfsec-config.yml` (To Be Created by `Édouard`/`Cerberus` if a central config is used for chosen tool)
  - `gcs-core-governance/iac/custom-rules/tflint/` (To Be Populated by `Édouard`/`Benjamin` if custom rules are developed)
- **Exception Tracking:**
  - `gencraft-operations/iac-scan-exceptions.md` (To Be Created by `Benjamin`/`Cerberus`)

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
