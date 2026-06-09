---
docId: DEV-SPEC-005
title: Gct Tool Mdlint V1
version: 1.0.0
authors:
- AI Compliance Agent
creation_date: '2025-05-26'
language: en
last_updated_date: '2026-05-20'
metadata:
  lifecycle-stage: approved
  keywords:
  - markdown-lint
  - tooling
  - markdown
  - consistency
  - gencraft-studio
  - documentation
  scope: studio
  domain: devops
  doc-type: specification
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/04-tooling-and-automation-hub/tools/DEV-SPEC-005.gct-tool-mdlint-v1.md
---
# Markdown Linting Tool - Tool Documentation

## 1. Overview and Purpose

- **Brief Description:** The `MarkdownLintingTool` is a utility designed to
  enforce Markdown syntax consistency and style guidelines across all Gencraft
  Studio repositories containing Markdown documentation. Its primary goal is to
  ensure readability, maintainability, and a uniform appearance for all Markdown
  files, particularly those within the `gcs-core-governance`.
- **Core Functionality:**
  - Scans specified Markdown files for syntax errors and style violations.
  - Reports violations with details (file, line number, rule, description).
  - Optionally, provides auto-fixing capabilities for certain rule violations.
- **Intended Users (Gems/Crews):**
  - All Gems contributing or modifying Markdown documents (e.g., during
      content creation for the handbook, drafting ADRs, writing documentation).
  - AI Enablement Team (AIE) for setup, configuration, and maintenance of the
      tool.
  - DevOps Team for integration into CI/CD pipelines.
  - Potentially automated KB maintenance Gems or processes.
- **Use Cases:**
  - Ensuring Markdown contributions adhere to Gencraft's defined styling rules
      before merging.
  - Maintaining a consistent and professional look and feel for all studio
      documentation.
  - Reducing cognitive load for readers by standardizing Markdown structure.
  - Assisting Gems in learning and applying correct Markdown syntax.
  - Automated quality checks in CI/CD pipelines to validate Pull Requests.
- **Relation to other Tools/MCPs:**
  - Configuration will align with principles from
      `tool-003-code-style-and-formatting.md` and `.editorconfig_standard`.
  - May be invoked by CI/CD pipeline tools (defined by DevOps).
  - Output might be consumed by review or notification tools in the future.

## 2. Technical Specifications

### 2.1. Architecture

- The tool will primarily be a wrapper or direct invocation of a robust,
  existing Markdown linting engine, such as `markdownlint-cli` (Node.js based).

- It will utilize a central or per-repository configuration file (e.g.,
  `.markdownlint.json`) to define the active ruleset.
- **Key technologies or libraries used:** `markdownlint-cli` (or a similar
  engine chosen by AIE Team), Node.js (if using `markdownlint-cli`).

### 2.2. Invocation / API

- **How to invoke the `Tool`:**
  - **Command-line interface (CLI) usage:**
    - `gencraft-lint-md <file_or_directory_path_to_lint...>`
    - `gencraft-lint-md --fix <file_or_directory_path_to_lint...>` (for
          auto-fixing)
    - `gencraft-lint-md --config <path_to_config_file>` (to specify a custom
          config)
  - The AIE team will determine the exact CLI command and may provide a
      wrapper script for ease of use.

- **Input Parameters / Arguments:**
  - `paths_to_lint`: (String/Array of Strings) One or more file paths or
      directory paths to lint. Required. Example: `"."`, `"./01-Operational-
      Protocols/"`, `"./00-studio-vision-and-principles/MyDocument.md"`.
  - `--fix`: (Boolean) If present, attempt to automatically fix linting
      violations. Optional. Default: `false`.
  - `--config`: (String) Path to the Markdown linter configuration file.
      Optional. Defaults to a predefined location (e.g., `.markdownlint.json` in
      the root of the scanned repository or a central SSoT).
  - `--output-format`: (String) Specify the output format (e.g., `text`,
      `json`, `checkstyle`). Optional. Default: `text` (for console).
- **Output / Return Value:**
  - **Console Output (`text` format):** Human-readable list of violations,
      including:
    - File path
    - Line number (and column, if applicable)
    - Violated Rule ID (e.g., `MD001`)
    - Rule description or error message
    - Example: `MyDocument.md:10 MD009/no-trailing-spaces Trailing spaces`
  - **JSON Output (`json` format):** Structured JSON array of violation
      objects, suitable for machine processing. Each object to contain similar
      details as text output.
  - **Checkstyle Output (`checkstyle` format):** XML format compatible with
      Checkstyle, for CI integration.
  - **Exit Codes:** `0` for success (no linting errors), non-zero for errors
      (e.g., `1` if linting errors are found).
- **Configuration:**
  - The primary configuration method will be via a ruleset file (e.g.,
      `.markdownlint.json` or `.markdownlint.yaml`).
  - This file will define which linting rules are enabled/disabled and any
      specific parameters for those rules.
  - **Principle:** Minimize Gencraft-specific rules; rely on widely accepted
      defaults from the chosen linter engine (e.g., `markdownlint-cli`'s default
      rules).
  - **SSoT for configuration files:** A base configuration file will be
      maintained by the AIE team (e.g., in `gcs-core-governance/tooling/configs/`
      or a dedicated `gencraft-linting-configs` repository). Repositories using
      Markdown should include this configuration file (e.g., as
      `.markdownlint.json` at their root) or reference a global one if
      technically feasible.

### 2.3. Dependencies

- **Software Dependencies:**
  - `markdownlint-cli` (or chosen linter engine).
  - Node.js and npm/yarn (if using `markdownlint-cli`).

- **System Dependencies:** OS-agnostic, capable of running Node.js or the chosen
  linter's runtime.
- **KB Dependencies:** None for basic operation, but rules might indirectly
  enforce conventions desired for KB readability.

### 2.4. Security Considerations

- The tool reads files from the filesystem. It should operate with the necessary
  read permissions for the target files.

- If `--fix` option is used, it will modify files. Users should ensure they have
  backups or use version control.
- No network access is required for core linting functionality.
- No direct handling of sensitive data or secrets beyond file content access.

## 3. Usage Guide

### 3.1. Prerequisites

- Installation of the chosen linter engine (e.g., `npm install -g markdownlint-
  cli` or as a dev dependency in projects).

- Access to the Gencraft standard Markdown linting configuration file.

### 3.2. Basic Usage Examples

- **Lint all Markdown files in the current directory and subdirectories:**

  ```bash
  gencraft-lint-md "**/*.md"
  ```

*(Assuming `gencraft-lint-md` is an alias or script set up by AIE Team for ease
of use. The actual command might directly use the chosen linter engine, e.g.,
`markdownlint`)*
  *Alternatively, using `markdownlint-cli` directly (if chosen as the engine):*

  ```bash
  markdownlint "**/*.md"
  ```

- **Lint a specific file:**

    ```bash
    markdownlint ./00-studio-vision-and-principles/studio-culture-and-values.md
    ```

- **Lint and attempt to auto-fix violations:**

    ```bash
    markdownlint --fix "**/*.md"
    ```

### 3.3. Advanced Usage (if applicable)

- **Using a specific configuration file (if not using the default
  `.markdownlint.json` in the repository root):**

  ```bash
  markdownlint --config /path/to/custom/.markdownlint.json "**/*.md"
  ```

- **Outputting results in JSON format (for scripting or CI consumption):**

```bash
markdownlint --json "**/*.md" > lint-report.json
```

- **Outputting results in Checkstyle XML format (for CI tools that support
  it):**

```bash
markdownlint --output-format checkstyle "**/*.md" > checkstyle-report.xml
```

- **Ignoring specific directories or files (via CLI, though .markdownlintignore
  or similar is preferred for persistent ignores):**

```bash
markdownlint "**/*.md" --ignore "node_modules/**" --ignore "archive/**"
```

### 3.4. Error Handling and Troubleshooting

- **Common error messages:**
  - `File not found: <path>`: The specified file or directory does not exist.
  - `Cannot read config file: <path_to_config>`: The specified configuration
      file is missing or unreadable.
  - `Invalid option: <option_name>`: An invalid command-line option was used.
  - Linter engine specific errors (e.g., rule implementation errors if custom
      rules were used, though we aim to avoid this).

- **Known issues or limitations:**
  - Auto-fix (`--fix`) functionality may not be available for all linting
      rules. Some violations require manual correction.
  - Performance might degrade on extremely large individual Markdown files
      (though this is generally not expected for handbook documents).
  - Complex or highly nested Markdown structures might occasionally lead to
      linter confusion, though this is rare with mature linters.
- **Troubleshooting steps:**
  - Ensure the linter engine (e.g., `markdownlint-cli` and its dependency
      Node.js) is correctly installed and accessible in the system's PATH.
  - Verify that the paths to the files/directories to be linted are correct.
  - Check the validity and location of the `.markdownlint.json` (or
      equivalent) configuration file.
  - Consult the documentation of the chosen linter engine for explanations of
      specific rule violations or error messages.
  - For CI/CD integration issues, check the DevOps team's CI logs and pipeline
      configuration.
- **How to report bugs or request support for this `Tool`:**
  - Submit an issue to the `gencraft-aie-backlog` repository (once created as
      per Action Tracker point AIE-Charter-Act-003).
  - Use the label `type:tool-bug` and `tool:GCT-TOOL-MDLINT-V1`.
  - Include the version of the tool/linter, the problematic Markdown snippet,
      the configuration used, and the observed vs. expected behavior.

## 4. Development and Maintenance

-(Primarily for AIE Team and contributors)-

### 4.1. Development Standards

- Refer to `gcs-core-governance/04-tooling-and-automation-hub/AI-Tool-
  Development-Standards.md`.

- The "Tool" itself for Gencraft primarily consists of:
    1. The chosen linter engine (e.g., `markdownlint-cli`).
    2. The centrally managed Gencraft Markdown linting ruleset configuration
        (e.g., `.markdownlint.json`).
    3. Optionally, simple wrapper scripts (`gencraft-lint-md`) for standardized
        invocation across the studio.
- Development will mostly focus on defining and maintaining the shared ruleset
  configuration. Wrapper scripts should be kept minimal.

### 4.2. Testing Strategy

- **Ruleset Configuration Testing:**
  - The Gencraft standard `.markdownlint.json` ruleset must be tested against
      a curated corpus of Markdown files.
  - This corpus should include:
    - Files that perfectly adhere to all enabled rules.
    - Files that demonstrate common violations for each important rule, to
          ensure they are correctly flagged.
    - Files where auto-fixable rules can be tested for correct modification.
  - This test corpus should be version-controlled.

- **Wrapper Script Testing (if developed):**
  - Unit tests for argument parsing, path handling, and correct invocation of
      the underlying linter.
  - Integration tests to ensure the script works with the linter engine and
      configuration file as expected.
- **CI Integration Testing:**
  - DevOps team will be responsible for testing the linting step within CI
      pipelines across various repositories to ensure it:
    - Correctly identifies non-compliant Markdown files.
    - Fails the build as expected upon detecting errors.
    - Correctly passes builds with compliant Markdown.

### 4.3. Contribution Guidelines

- **Changes to the Standard Ruleset Configuration:**
  - All proposed changes (enabling/disabling rules, modifying rule parameters)
      must be discussed via an Issue in the `gencraft-aie-backlog` (or the
      repository designated as SSoT for the linting configuration).
  - Rationale for changes must be provided, considering the "avoid specific
      rules" principle.
  - Approved changes should be submitted as a Pull Request to the SSoT of the
      configuration file, including updates to the test corpus if necessary.

- **Contributions to Wrapper Scripts (if any):**
  - Follow the standard Pull Request process defined in `AI-Tool-Development-
      Standards.md` to the script's SSoT code repository.

## 5. Version History (Changelog)

| Version | Date       | Author(s)                      | Summary of Changes                                                                 |
| :------ | :--------- | :----------------------------- | :--------------------------------------------------------------------------------- |
| `0.1.0` | `2025-05-15` | `[GCT-AIA-PIER-001 (Pierre)]`  | Initial draft specification based on Lug's requirements and `tool-documentation-template.md`. Focus on `markdownlint-cli` as the proposed engine. |
|         |            |                                |                                                                                    |

## 6. Roadmap (Future Enhancements)

- **IDE Integration Guides:** Develop and document specific setup instructions
  for commonly used IDEs within Gencraft (e.g., VS Code, JetBrains suite) to
  automatically use the Gencraft Markdown linting configuration on save or via
  IDE actions.

- **Pre-commit Hook Configuration:** Provide a standard pre-commit hook
  configuration (e.g., for `husky` in Node.js projects or `pre-commit` for
  broader use) that repositories can easily adopt to run linting locally before
  commits. This is highly recommended.
- **Centralized Configuration Distribution:** Investigate mechanisms for easier
  distribution and updating of the standard linting configuration file across
  all Gencraft repositories (e.g., via a shared DevOps utility or a versioned
  package).
- **Custom Rule Development (Strictly if Necessary and Approved):** Only if
  absolutely essential Gencraft-specific Markdown conventions cannot be
  addressed by existing `markdownlint-cli` rules, the AIE team might explore
  developing custom rules. This would be a significant undertaking and should be
  a last resort, adhering to the principle of minimizing specific rules.
- *(Links to relevant GitHub Issues in `gencraft-aie-backlog` will be added here
  as features are formally proposed and tracked).*

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
