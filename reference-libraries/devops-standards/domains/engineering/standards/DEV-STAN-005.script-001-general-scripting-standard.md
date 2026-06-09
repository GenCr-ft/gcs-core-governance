---
docId: DEV-STAN-005
title: Script 001 General Scripting Standard
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This standard establishes mandatory guidelines for writing, deploying, and
  maintaining scripts within the Gencraft studio, focusing on consistency, readability,
  maintainability, security, and reliability.
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - scripting-standards
  - automation
  - gencraft
  - devops
  - coding-guidelines
  - shell-scripting
  - python-scripting
  scope: studio
  domain: devops
  doc-type: standard
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/engineering/standards/DEV-STAN-005.script-001-general-scripting-standard.md
---
## 1. Objective

This standard establishes mandatory guidelines for writing, deploying, and maintaining scripts within the
Gencraft studio. The objectives are to ensure all scripts are:

- **Consistent:** Adhering to common style and structure.
- **Readable & Understandable:** Easy for both humans and AI Gems to comprehend.
- **Maintainable:** Designed for long-term viability and ease of modification.
- **Secure:** Minimizing security risks in development and execution.
- **Reliable:** Incorporating robust error handling and logging.
- **Efficient:** Using resources responsibly.
- **Actionable by AI Gems:** Designed for non-interactive execution with clear inputs, outputs, and status
  reporting when intended for AI Gem use.

## 2. Scope

This standard applies to ALL scripts developed or used within Gencraft, including but not limited to:

- Shell scripts (Bash, sh).
- Python scripts.
- PowerShell scripts (if adopted for specific use cases).
- Scripts embedded in CI/CD pipelines (e.g., GitHub Actions workflow steps).
- Automation scripts stored in `gencraft-devops-automation` or other designated SSoT locations.
- Local utility scripts intended for shared use among Gems.
- Scripts developed by or for AI Gems.

This standard complements language-specific best practices and `../tooling/tool-003-code-style-and-formatting.md`.

## 3. Standard

### 3.1. Language Choice Guidelines

- **Bash/Shell (`.sh`):** Preferred for simple command sequences, CLI tool wrappers, file system
  manipulation, or when broad POSIX compatibility is paramount and external libraries are minimal.
- **Python (`.py`):** Preferred for scripts requiring complex logic, data manipulation, API interactions,
  extensive error handling, or when leveraging a rich ecosystem of third-party libraries. It is the default
  choice for new complex automation.
- **PowerShell (`.ps1`):** May be used for automation tasks specifically targeting Windows environments or
  requiring deep integration with Microsoft products (e.g., Azure, Exchange), subject to approval by DevOps
  leadership (`Adam`, `Édouard`).

### 3.2. File Structure and Naming Conventions

- **File Extension:** Use standard extensions: `.sh` for Bash/shell, `.py` for Python, `.ps1` for
  PowerShell.
- **Naming:** Script names MUST be in `snake_case` (e.g., `my_utility_script.sh`) or `kebab-case` (e.g.,
  `my-utility-script.sh`). Be descriptive and consistent within a project or functional area.
- **Shebang (for executable Unix scripts):**
  - Bash: `#!/usr/bin/env bash` (preferred for portability).
  - Python: `#!/usr/bin/env python3`.
- **Permissions:** Scripts intended to be executed directly MUST have execute permissions set (`chmod +x scriptname.sh`).

### 3.3. Script Header and Metadata

All scripts SHOULD include a header comment block providing essential metadata.

- **Bash/Shell & Python Example:**

```bash
  #!/usr/bin/env bash
  #
  # ID: SCRIPT_XYZ (If applicable, e.g., for SSoT scripts in gencraft-devops-automation)
  # Title: Brief description of script purpose
  # Author(s): GemID (Name), GemID (Name)
  # Creation Date: YYYY-MM-DD
  # Last Modified Date: YYYY-MM-DD
  # Version: X.Y.Z (Semantic Versioning if applicable for complex scripts)
  #
  # Description:
  #   More detailed explanation of what the script does, its inputs, outputs,
  #   and any important assumptions or dependencies.
  #
  # Usage:
  #   ./scriptname.sh [options] <arguments>
  #   (Provide clear usage examples)
  #
  # Dependencies:
  #   - jq (version >= X.Y)
  #   - aws-cli (version >= X.Y)
  #
  # Exit Codes:
  #   0 - Success
  #   1 - General error
  #   2 - Invalid input
  #   (Define others as needed)
```

- **PowerShell Example:** Use comment-based help: <https://learn.microsoft.com/en-us/powershell/module/>
  microsoft.powershell.core/about/about_comment_based_help?view=powershell-7.4

### 3.4. Readability, Style, and Formatting

- **Adherence to `TOOL_003`:** All scripts MUST adhere to `../tooling/tool-003-code-style-and-formatting.
md` and utilize specified linters/formatters. These SHOULD be integrated into local development workflows
  via pre-commit hooks as defined in `../tooling/tool-004-git-hooks-standard.md`.
  - **Bash:** - Linting: `shellcheck` (configuration SSoT: `gcs-core-governance/linting/configs/.shellcheckrc` -
    _si ce fichier SSoT est créé_). - Formatting: `shfmt` using the following recommended CLI arguments: `shfmt -w -i 2 -ci -s`
    (Write, Indent 2 spaces, Case Indent, Simplify). (Référence: `gcs-core-governance/formatting/
configs/` pour la discussion sur les options `shfmt`).
  - **Python:** - Formatting: `black` (configuration SSoT: `../formatting/configs/pyproject.toml` under `[tool.
black]` section). - Linting: `flake8` or `pylint` (configurations SSoT: `gcs-core-governance/linting/configs/.
flake8` or `gcs-core-governance/linting/configs/.pylintrc` - _si ces fichiers SSoT sont créés_).
  - **PowerShell:**
    - Linting & Formatting: `PSScriptAnalyzer` (configuration via un fichier de settings PowerShell,
      SSoT: `gcs-core-governance/linting/configs/PSScriptAnalyzerSettings.psd1` - _si ce fichier SSoT est créé_).
- **Comments:** Use comments to explain non-obvious logic, complex regular expressions, or critical
  decision points. Avoid commenting on obvious code.
- **Naming Conventions (Variables, Functions):**
  - **Bash:** `UPPER_CASE_SNAKE` for global constants/environment variables, `lower_case_snake` for
    local variables and functions.
  - **Python:** `UPPER_CASE_SNAKE` for constants, `lower_case_snake` for variables and functions (PEP 8).
  - **PowerShell:** `PascalCase` for functions and cmdlets, `PascalCase` or `$camelCase` for variables
    (consistent with community practices).
- **Modularity:** Break down complex scripts into functions. For Python, consider creating reusable
  modules if logic is shared across multiple scripts. Scripts in `gencraft-devops-automation/
scripts/libs/` (To Be Created) could house such shared functions.
- **Line Length:** Adhere to line length recommendations (e.g., 80-120 characters) as per `../tooling/
tool-003-code-style-and-formatting.md` to enhance readability.

### 3.5. Error Handling

- **Exit Codes:** Scripts MUST exit with `0` on success and a non-zero integer (`1-255`) on failure.
  - `1`: General/unspecified error.
  - `2`: Invalid input, arguments, or missing dependencies.
  - Define other specific exit codes in the script header if they provide actionable distinctions for AI
    Gems or calling processes. (e.g., `3`: Prerequisite condition not met, `4`: External service error).
- **Bash Best Practices:**
  - `set -e`: Exit immediately if a command exits with a non-zero status.
  - `set -u`: Treat unset variables as an error when substituting.
  - `set -o pipefail`: The return value of a pipeline is the status of the last command to exit with a
    non-zero status, or zero if no command exited with a non-zero status.
  - Use explicit checks for command success: `if ! command_that_might_fail; then echo "Error:
'command_that_might_fail' failed with exit code $?." >&2; exit 1; fi`.
- **Python Best Practices:** Use `try...except...finally` blocks for error handling. Catch specific
  exceptions rather than generic `Exception`. Log errors appropriately using the `logging` module. Use `sys.
exit(code)` for exiting.
- **PowerShell Best Practices:** Use `try...catch...finally` blocks and `trap` statements. Set
  `$ErrorActionPreference = "Stop"` for critical sections where you want scripts to halt on terminating
  errors. Use `Write-Error` for error messages.
- **Error Messages:** MUST be clear, concise, and written to `stderr`. They SHOULD indicate the script
  name (or ScriptID if applicable), the function where the error occurred (if applicable), the nature of the
  error, and any relevant context (e.g., filename, line number) without exposing sensitive information. For
  AI actionability, consider prefixing error messages with a structured error code if not using distinct
  exit codes (e.g., `ERR_SCRIPT_XYZ_FILE_NOT_FOUND: Specific_file.txt could not be accessed.`).

### 3.6. Logging

- **Purpose:** Provide visibility into script execution, aid in debugging, and create an audit trail for
  critical operations.
- **Levels (minimum suggested, align with any studio-wide logging standard e.g., `LOG_001_Logging_Standard.md` - To Be Created):**
  - `INFO`: General operational messages indicating progress or key actions.
  - `WARNING`: Potential issues, recoverable errors, or deprecated usage.
  - `ERROR`: Failures that prevent normal completion (usually precedes a non-zero exit).
  - `DEBUG`: Verbose information for troubleshooting (SHOULD be disabled by default and controllable via
    a flag like `--debug` or an environment variable like `GFT_SCRIPT_DEBUG=true` or
    `GFT_LOG_LEVEL=DEBUG`).
- **Format (Recommended for AI Parsability, align with `LOG_001`):** `YYYY-MM-DDTHH:MM:SSZ LEVEL [ScriptID|
ScriptName:PID:FunctionName] MessageBody (JSON_Payload_If_Applicable)`
  - Example: `2025-05-22T08:30:00Z INFO [SCRIPT_XYZ:12345:main] User validation successful. {"user": "gem_id"}`
- **Output:**
  - `INFO` and `DEBUG` messages typically to `stdout` (or a configured log file/stream, as per `LOG_001`).
  - `WARNING` and `ERROR` messages to `stderr` (or a configured error log file/stream, as per `LOG_001`).
- **Sensitive Data:** Scripts MUST NEVER log secrets, tokens, passwords, PII, or other sensitive data as
  defined by `../../gcs-core-governance/02-knowledge-base-hub/kb-domain-security/
information-classification-and-handling-policy.md`. Sanitize or omit such data from logs. Refer to `../../
gencraft-operations/docs/ops-001-iac-scan-exception-log-standard.md` for handling sensitive scan results
  if scripts report such.
- **Python:** Use the `logging` module, configured to output in the standard format and levels.
- **Bash:** Use `echo` to `stdout`/`stderr` with manually formatted messages or a dedicated logging helper
  function (from `gencraft-devops-automation/scripts/libs/bash_logging_utils.sh` - To Be Created) to ensure
  consistency.
- **PowerShell:** Use `Write-Output`, `Write-Warning`, `Write-Error`, `Write-Verbose`, `Write-Debug`.
  Consider wrapping these in functions for standardized formatting and level control.

### 3.7. Input Parameters and Arguments

- **Clear Definition:** All accepted inputs (arguments, options, environment variables) MUST be documented
  in the script header (Usage section), including data type (string, integer, boolean, enum with allowed
  values), whether mandatory/optional, and default values if any.
- **Validation:** Scripts MUST validate critical input parameters for presence, type, and allowed values/
  patterns (e.g., regex for string formats). Exit with an error (and appropriate exit code `2`) if
  validation fails.
- **Help Message:** Provide a `--help` or `-h` option that displays the usage information from the header.
  This should be auto-generated by the argument parsing tool where possible.
- **Argument Parsing Tools:**
  - **Bash:** `getopts` (for simple POSIX-style options). For more complex needs or GNU-style long
    options, consider a more robust solution or a Python wrapper. Avoid manual parsing for more than 1-2
    arguments.
  - **Python:** `argparse` module from the standard library is PREFERRED. `click` or `typer` are
    acceptable alternatives for more complex CLIs.
  - **PowerShell:** Use `param()` blocks with strongly typed parameters, mandatory checks (`[Parameter
(Mandatory=$true)]`), and validation attributes (e.g., `[ValidateSet(...)]`, `[ValidatePattern(...)]`, `[ValidateRange(...)]`).

### 3.8. Security Considerations

- **Secrets Management:**
  - Adhere strictly to `../security/sec-001-secrets-management-standard.md`. Secrets MUST NOT be hardcoded.
  - Retrieve secrets from approved Gencraft secret management solutions (e.g., HashiCorp Vault, GitHub
    encrypted secrets) at runtime. Scripts SHOULD NOT have direct access to Vault tokens if possible;
    prefer mechanisms like Vault Agent injection or short-lived credentials.
  - If secrets are passed via environment variables (e.g., `GH_TOKEN` for `gh`), the script MUST ensure
    they are not inadvertently logged (e.g., by unsetting them after use if possible, or careful use of
    `set +x` in Bash). Use `add-mask` in GitHub Actions.
- **Input Validation:** Sanitize and validate ALL external inputs rigorously, especially if they are used
  to construct file paths, commands to be executed (see "Command Usage" below), or queries to APIs, to
  prevent injection attacks, path traversal, or unintended operations.
- **Principle of Least Privilege:** Scripts SHOULD run with the minimum necessary permissions, both in
  terms of filesystem access and any credentials they use. File permissions on the script itself should be
  restrictive (e.g., `rwxr-x---` or `rwx------`). For CI/CD, tokens used by scripts must have minimal scopes.
- **Command Usage & Execution:**

  - **Avoid `eval` or direct shell execution of constructed strings:** In Bash, avoid `eval
"$COMMAND_STRING"`. In Python, avoid `os.system()` with formatted strings or `subprocess.call(..., shell=True)`.
  - **Safe Command Construction:** When calling external commands, pass arguments as separate elements
    in an array or list to prevent shell injection.
    - Bash: `local_var="some value"; my_command "fixed_arg" "$local_var"`
    - Python: `subprocess.run(["my_command", "fixed_arg", local_var], check=True)`
  - Be extremely cautious with commands like `rm -rf`, or those that execute arbitrary code or modify
    critical system state. Limit their use, ensure paths/inputs are strictly controlled and validated.
    Consider adding a `--dry-run` mode and/or interactive confirmation (`--force` to override) for

    heavily scrutinized.

- **Temporary Files:** If temporary files or directories are used, create them securely using `mktemp -d`
  or `mktemp` in Bash (with appropriate umask), or the `tempfile` module in Python. Ensure they are cleaned
  up using traps (e.g., `trap "rm -rf '$TEMP_DIR'" EXIT INT TERM HUP`) or `finally` blocks, even if the
  script errors.
- **External Calls (Network):** Validate SSL/TLS certificates for HTTPS calls by default. Be cautious with
  `--insecure` or equivalent flags; require explicit justification and approval from `Cerberus` if used.
- **Regular Review:** Security-critical scripts (e.g., those handling production secrets, performing
  wide-ranging infrastructure changes, exposed to external input, or running with elevated privileges) MUST
  be subject to periodic security review by `Cerberus` or designated security personnel.
- **Secret Scanning:** All scripts committed to repositories MUST pass secret scanning checks as per `../
security/sec-003-secret-scanning-standard.md`.

### 3.9. Dependencies

- **Declaration:** External command-line tools (e.g., `jq`, `aws`, `gh`) or libraries required by a script
  MUST be explicitly listed in its header metadata, including version constraints where compatibility is
  critical (e.g., `jq >= 1.6`). Reference `../../gcd-onboarding-scripts/validations-scripts/
validate-gft-devops-environment.sh` or specific project setup documentation for ensuring availability.
- **Python:** Use `requirements.txt` (with pinned versions, e.g., `package==X.Y.Z` or `package>=X.Y,<X.Z`)
  for Python script dependencies. These should be installed into and run from a virtual environment (`venv`).
- **Bash/PowerShell:** For less common tools not part of a standard OS build or the Gencraft CI runner
  image, the script header must clearly specify them. The execution environment (developer machine, CI
  runner) MUST ensure their availability in the correct versions.
- **Avoid Bundling:** Do not commit library code or vendored dependencies directly into script
  repositories unless absolutely unavoidable, explicitly justified, and approved by DevOps leadership
  (`Adam`, `Édouard`) and `Cerberus`. Prefer standard package management and artifact repositories (see `../
cicd/cicd-002-artifact-management-standard.md`).

### 3.10. Testing

- While extensive unit testing may be overkill for very simple utility scripts (e.g., < 20 lines of simple
  commands), important, complex, or critical scripts (especially Python and PowerShell, and non-trivial Bash
  scripts) SHOULD have automated tests.
- **Strategy Reference:** Refer to `../iac/iac-006-iac-testing-strategy.md` for analogous principles on
  testing levels, where applicable. A specific `SCRIPT_00X_Script_Testing_Strategy.md` may be developed if
  needed.
- **Types of Tests:**
  - **Python:** `unittest` or `pytest` for functions and classes. Aim for good test coverage of core logic.
  - **Bash:** Consider `Bats` (Bash Automated Testing System) or `shellcheck -x` (to check sourced files
    and execution paths) for testing core logic and ensuring robustness. Test individual functions if the
    script is well-structured.
  - **PowerShell:** `Pester` for testing functions and modules.
- **Test Cases:** Should cover normal operational paths, expected failure modes (e.g., invalid input,
  missing dependencies, external service errors), edge cases, and input validation logic.
- **Environment:** For scripts interacting with external services, use mocks, stubs, or dedicated test
  instances/sandboxes. Avoid running tests directly against production services.
- **CI/CD Integration:** Automated tests for scripts stored in SSoT locations like
  `gencraft-devops-automation` MUST be integrated into CI/CD pipelines. PRs modifying these scripts should trigger these tests.

### 3.11. Actionability for AI Gems

Scripts designed to be called by or interact with AI Gems (either for execution by an AI, or for an AI to
analyze/generate such scripts) MUST prioritize:

- **Non-Interactivity:** No interactive prompts. All input MUST be via command-line arguments/options or
  environment variables. Default values should be sensible.
- **Clear, Parseable Output:**
  - For data output, **JSON is the MANDATORY format** if the output is complex or structured. Use `jq`
    or native JSON capabilities to structure output.
  - For status or simple string outputs, ensure they are predictable, concise, and easily parsable (e.
    g., avoid unstructured human-readable sentences if a simple status string like `SUCCESS` or `FAILURE:reason_code` suffices).
- **Standard and Specific Exit Codes:** Crucial for AI to determine success, failure, or specific error
  states unambiguously. Document all custom exit codes and their meanings in the script header.
- **Idempotency:** If a script modifies state (filesystem, cloud resources, configuration), it SHOULD be
  designed to be idempotent where feasible (i.e., running it multiple times with the same inputs results in
  the same state without unintended side effects). If not fully idempotent, its side-effects on re-run MUST
  be clearly documented in the header.
- **Comprehensive and Structured Documentation:** The script's header/metadata (see section 3.3) MUST be
  accurate, complete, and ideally machine-readable to some extent. This includes:
  - Purpose and brief description.
  - All input parameters: name, data type (string, int, bool, enum, path), mandatory/optional, default
    value, description, validation rules/constraints.
  - All primary outputs: format (e.g., JSON, plain text lines), structure/schema if JSON, description.
  - All defined exit codes and their meanings.
  - Key dependencies and their expected versions.
- **Logging Standards:** Adherence to structured logging (section 3.6) helps AI Gems monitor script
  progress and diagnose issues programmatically.
- **Example Scripts:** Well-commented example scripts in `gencraft-devops-automation` that fully adhere to
  this standard (e.g., `../../gcd-onboarding-scripts/onboarding/gftai-onboarding.sh` and `../../
gcd-onboarding-scripts/validations-scripts/validate-gft-devops-environment.sh` should be updated to serve
  as such) are invaluable for AI Gems learning to generate or use Gencraft scripts.

## 4. Responsibilities

- **Script Authors (All Gems):**
  - Adherence to this standard for any new or significantly modified scripts.
  - Documenting their scripts as per section 3.3.
  - Ensuring appropriate security measures are taken (section 3.8).
  - Writing tests for critical or complex scripts (section 3.10).
- **`Camille` (Gem AB - Automation Specialist):**
  - Co-Knowledge Guardian of this standard.
  - Championing best practices in scripting and automation.
  - Maintaining SSoT scripts and shared libraries (e.g., `gencraft-devops-automation/scripts/libs/`)
    within `gencraft-devops-automation`.
  - Assisting other Gems in writing complex or critical automation scripts.
- **`Édouard` (Gem AD - DevOps Strategy Specialist):**
  - Co-Knowledge Guardian of this standard.
  - Ensuring alignment with overall DevOps strategy and other tooling/IaC standards.
  - Maintaining SSoT for linter/formatter configurations (in `gcs-core-governance/formatting/configs/`
    and `gcs-core-governance/linting/configs/`).
- **`Cerberus` (Security Officer Gem):**
  - Reviewing security-critical scripts and security-related aspects of this standard.
  - Providing guidance on secure scripting practices, secret management, and input validation.
- **DevOps Team (`Adam`, `Benjamin`, `Camille`, `Diane`, `Édouard`):**
  - Reviewing scripts used in CI/CD and core DevOps automation for compliance with this standard.
  - Promoting the use of linters, formatters, and testing for scripts.
- **Code Reviewers (as per S1):**
  - Checking for adherence to this standard during PR reviews of scripts.

## 5. SSoT Locations for Scripts

- **General DevOps Automation & Reusable Studio Scripts:** `gencraft-devops-automation/scripts/`
  (organized by function/tool, e.g., `gencraft-devops-automation/scripts/onboarding/`). Shared libraries in
  `gencraft-devops-automation/scripts/libs/` (To Be Created).
- **IaC Related Utility Scripts (if not directly part of IaC code):** `gencraft-studio-iac/scripts/` or
  `gencraft-game-aethel-iac/scripts/` (or future `gencraft-iac-[project]/scripts/`).
- **Project-Specific Scripts:** Within the project's repository, typically in a `/scripts` or `/tools`
  directory. These should still adhere to the standard if intended for more than trivial, one-off use by a
  single developer.
- **Validation Scripts:** `gencraft-devops-automation/validations-scripts/`.

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
