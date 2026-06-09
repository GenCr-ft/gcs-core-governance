---
docId: DEV-SPEC-013
title: Tool 003 Code Style And Formatting
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This standard defines the required code style and formatting practices for
  G@FT.ai Studio, ensuring consistent code across all projects. Automated tools, including
  formatters and linters, are mandatory, alongside adherence to specific naming conventions
  and language idioms.
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - code-style
  - formatting
  - standards
  - devops
  - gft-ai
  - tooling
  - coding-guidelines
  scope: studio
  domain: devops
  doc-type: specification
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/tooling/standards/DEV-SPEC-013.tool-003-code-style-and-formatting.md
---
## 1. Purpose

This standard defines the principles and practices for code style and automated code formatting within
<G@FT.ai> Studio. Consistent code style and formatting are essential for:

- **Readability & Maintainability:** Making code easier to read, understand, and maintain by all team members.
- **Reduced Cognitive Load:** Minimizing style-related distractions during code reviews and development.
- **Collaboration Efficiency:** Ensuring a uniform appearance of code regardless of who wrote it.
- **Preventing Style Debates:** Establishing an objective standard enforced by tools.
- **Onboarding:** Helping new developers adapt quickly to the codebase.

## 2. Core Principles

1. **Automated Formatting First:** Code formatting **MUST** be primarily managed by automated tools.
   Manual formatting that deviates from the configured tool's output is discouraged. 2.**Consistency Over Preference:** The chosen automated formatter's style is the standard, even if
   individual developers have different personal preferences. 3.**IDE Integration:** Developers **SHOULD** configure their Integrated Development Environments (IDEs)
   to use the project's defined formatter and `.editorconfig` settings, ideally formatting on save. 4.**CI Enforcement:** Code formatting **MUST** be checked in Continuous Integration (CI) pipelines. Pull
   Requests with formatting violations that are not auto-fixable by the CI (or that require manual
   intervention) **SHOULD NOT** be merged until fixed. 5.**Language-Specific Standards:** While this document sets general principles, specific formatter tools
   and configurations are defined in `tool-002-language-specific-tooling-standards.md`.

## 3. Standard Tooling and Configuration

### 3.1. `.editorconfig` (Mandatory)

- All repositories containing text-based source code, configuration files, or documentation **MUST**
  include a standard `.editorconfig` file at the root.
- This file helps maintain consistent basic coding styles (indentation style, indent size, line endings,
  charset, trim trailing whitespace, insert final newline) across different editors and IDEs.
- A studio-wide standard `.editorconfig` template **MUST** be used as a base. This template is located in
  `template/.editorconfig_standard`. It defines sensible defaults:

```editorconfig
    # EditorConfig is awesome: [https://EditorConfig.org](https://EditorConfig.org)

    # top-most EditorConfig file
    root = true

    [*]
    end_of_line = lf
    insert_final_newline = true
    charset = utf-8
    trim_trailing_whitespace = true
    indent_style = space
    indent_size = 2 # Default, can be overridden by language-specific sections

    [*.{js,jsx,ts,tsx,json,yaml,yml}]
    indent_size = 2

    [*.py]
    indent_size = 4

    [*.cs]
    indent_size = 4

    [*.go]
    indent_style = tab # Go standard

    [*.rs]
    indent_size = 4

    [*.md]
    trim_trailing_whitespace = false # Often desirable for markdown
```

- Project-specific overrides within the project's `.editorconfig` are allowed if justified and documented,
  but the base settings for line endings, final newline, and charset should be maintained.

### 3.2. Language-Specific Formatters (Mandatory)

- Each programming language **MUST** use its designated automated code formatter as specified in
  `tool-002-language-specific-tooling-standards.md`. Examples include:
  - **TypeScript/JavaScript:** Prettier
  - **C# / .NET:** `dotnet format`
  - **Go:** `gofmt` or `goimports`
  - **Rust:** `rustfmt`
  - **Python:** Ruff (`ruff format`) or Black
- Configuration files for these formatters (e.g., `.prettierrc.js`, `.rustfmt.toml`, `../formatting/
configs/pyproject.toml` for Black/Ruff) **MUST** be included in the repository and version-controlled.
- Shared base configurations for these tools are maintained in `gcs-core-governance/tooling/configs/` and
  should be used as starting points for projects.

### 3.3. Linters for Style (Mandatory)

- Linters specified in `tool-002-language-specific-tooling-standards.md` (e.g., ESLint, Roslyn Analyzers,
  golangci-lint, Clippy, Ruff/Flake8) also contribute to code style and consistency.
- Their configurations often include style-related rules that complement the primary formatter. These
  **MUST** be enabled and configured to align with the overall <G@FT.ai> code style philosophy.

## 4. Workflow Integration

### 4.1. Local Development Environment

- **IDE Configuration:** Developers **MUST** configure their IDEs to:
  - Respect the project's `.editorconfig` file.
  - Use the project's designated formatter, ideally with format-on-save enabled.
  - Integrate the project's linter for real-time feedback.
- **Pre-commit Hooks (Highly Recommended):**
  - Use tools like `husky` (for Node.js based projects) or `pre-commit` (language-agnostic) to
    automatically run formatters and linters on staged files before a commit is created.
  - This helps catch formatting and style issues locally, reducing CI failures and review friction.
  - Standard configurations for these hooks will be provided.

### 4.2. Continuous Integration (CI) Pipeline

- CI pipelines for all code repositories **MUST** include a **formatting check stage**.
  - This stage runs the designated formatter in a "check" or "verify" mode (e.g., `prettier --check .`,
    `dotnet format --verify-no-changes`, `cargo fmt -- --check`, `black --check .`).
  - The CI build **MUST** fail if the formatter detects files that are not correctly formatted.
- CI pipelines **MUST** also include a **linting stage** that runs the configured linters.
  - The CI build **MUST** fail if linters report errors (and potentially configurable levels of warnings).

## 5. Style Guides & Naming Conventions (Beyond Auto-Formatting)

While automated formatters handle most syntactic style, other aspects require conscious effort and
adherence to established conventions:

- **Naming Conventions:** Variables, functions, classes, modules, files, etc., **MUST** follow consistent
  naming conventions appropriate for the language (e.g., `camelCase` for JavaScript/TypeScript variables and
  functions, `PascalCase` for classes, `snake_case` for Python functions and variables, `PascalCase` for C#
  classes and methods). Language-specific style guides referenced in `TOOL_002` or separate <G@FT.ai> coding
  guidelines will detail these.
- **Readability:** Prioritize clear, readable, and self-documenting code. Use comments judiciously to
  explain complex logic or "why" something is done, not just "what" it does.
- **Language Idioms:** Write idiomatic code that aligns with the common practices and paradigms of the
  specific programming language being used.
- **Simplicity (KISS - Keep It Simple, Stupid):** Prefer simple, straightforward solutions over overly
  complex or clever ones.
- **DRY (Don't Repeat Yourself):** Avoid unnecessary code duplication. Utilize functions, classes,
  modules, and shared libraries appropriately.

Detailed language-specific coding style guides (beyond what formatters enforce) may be developed and will
reside in `gcs-core-governance/tooling/language-style-guides/`.

## 6. Review and Updates

This standard, along with the specific formatter configurations and language style guides, will be
reviewed periodically (e.g., annually) by the DevOps Team, Architects, and Lead Developers to ensure they
remain relevant and effective.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
