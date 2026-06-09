---
docId: DEV-SPEC-014
title: Tool 002 Language Specific Tooling Standards
version: 1.2.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This document defines standard tooling for G@FT.ai Studio development, including
  linters, formatters, and package managers, across various languages (TypeScript,
  C#, Go, Rust, Python). It emphasizes code quality, consistency, security, and efficient
  CI/CD pipelines.
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - technical-writing
  - tooling-standards
  - code-quality
  - devops
  - typescript
  - csharp
  - go
  - rust
  - python
  - ci-cd
  - standards
  scope: studio
  domain: devops
  doc-type: specification
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/tooling/standards/DEV-SPEC-014.tool-002-language-specific-tooling-standards.md
---
## 1. Purpose

This document defines the standard set of development tools, including linters, formatters, package
managers, and vulnerability scanners, for each primary programming language used within <G@FT.ai> Studio.
Adherence to these standards is crucial for:

- **Code Quality & Consistency:** Ensuring a uniform code style and identifying potential issues early.
- **Developer Experience (DevEx):** Providing a consistent and predictable development environment.
- **Security:** Integrating automated checks for known vulnerabilities in dependencies.
- **CI/CD Efficiency:** Enabling standardized checks and validations within automated pipelines.
- **Maintainability:** Making codebases easier to understand, review, and maintain across teams.

All recommended tools strongly prefer **Open Source and/or Free** solutions. Configuration files for these
tools should be version-controlled within each repository, ideally based on centrally managed templates or
base configurations.

## 2. General Tooling Principles

- **`.editorconfig`:** All repositories containing text-based source code **MUST** include a standard `.
editorconfig` file at the root to enforce basic coding styles (indentation, line endings, charset). A
  studio-wide standard `.editorconfig` file is provided in `template/.editorconfig_standard`.
- **Automation:** Linting, formatting checks, and vulnerability scans **MUST** be integrated into
  pre-commit hooks (e.g., via Husky) and CI/CD pipelines for all code repositories.
- **Configuration:** Standard configurations for linters and formatters should be established and stored
  (e.g., in `gcs-core-governance/tooling/configs/`) to be referenced or copied into new projects.
- **Dependency Management:** Use lockfiles (`../package-lock.json`, `pnpm-lock.yaml`, `poetry.lock`, `go.
sum`, `Cargo.lock`, etc.) for all projects to ensure reproducible builds. These lockfiles **MUST** be
  committed to version control.

## 3. Tooling Standards by Language

### 3.1. TypeScript / JavaScript (Client, UI, some Backend Services)

- **Package Manager (Mandatory):**
  - **`pnpm`**: Recommended and preferred for its efficiency in terms of speed and disk space usage, and
    robust lockfile (`pnpm-lock.yaml`).
  - _Alternative:_ `npm` (with `../package-lock.json`) or `yarn` (v2+ with `yarn.lock`) are acceptable
    if a strong project-specific reason exists.
- **Linter (Mandatory):**
  - **`ESLint`**: For identifying and reporting on patterns in JavaScript/TypeScript.
  - _Configuration:_ Use a shared ESLint configuration (e.g., extending `eslint:recommended`,
    `plugin:@typescript-eslint/recommended`, `plugin:import/typescript`) with Prettier integration
    (`eslint-config-prettier`).
- **Formatter (Mandatory):**
  - **`Prettier`**: For consistent code formatting.
  - _Configuration:_ Use a shared Prettier configuration (`.prettierrc.js` or `.prettierrc.json`).
- **Type Checker (Mandatory for TypeScript):**
  - **`TypeScript Compiler (tsc)`**: Using `tsc --noEmit` to perform type checking without generating
    JavaScript output.
- **Testing Frameworks (Mandatory):**
  - **NestJS Backend Services**: **`Jest`**. Mandatory for all NestJS microservices.
    - _Context:_ `@nestjs/testing` integrates exclusively with Jest.
    - _Coverage:_ ARC-ADR-203 mandates a **minimum 80% unit test coverage**.
  - **Web / UI Components**: **`Vitest`**. Preferred for Vite-based apps and libraries.
    - _Benefits:_ Native ESM support and faster reload performance.
  - **E2E Testing**: **`Playwright`**. Preferred for cross-browser automation.
- **Vulnerability Scanner (Mandatory CI Step):**
  - `pnpm audit --prod --audit-level <level>` (or `npm audit`, `yarn audit`). The `<level>` (e.g.,
    `high`, `critical`) should be defined based on security policy.
  - _Consider:_ `Socket.dev` or `Snyk` (free tier) for enhanced open-source vulnerability management integrated into PRs.

### 3.2. C# / .NET (Game Server Core, some Backend Services)

- **Build Tool / Package Manager (Mandatory):**
  - **`.NET SDK CLI (dotnet)`**: For building, testing, packing, and managing NuGet packages.
- **Linter / Analyzer (Mandatory):**
  - **Roslyn Analyzers**: Integrated with the .NET SDK. Configure via `.editorconfig` and project files.
    Treat warnings as errors in CI builds (`/warnaserror` or `<>true</
TreatWarningsAsErrors>`).
  - _Consider:_ StyleCop.Analyzers for additional style enforcement.
- **Formatter (Mandatory):**
  - **`dotnet format`**: Integrated with the .NET SDK. Configure via `.editorconfig`.
- **Testing Frameworks (Recommended):**
  - `NUnit`, `xUnit`, or `MSTest` for unit and integration tests.
- **Vulnerability Scanner (Mandatory CI Step):**
  - `dotnet list package --vulnerable --include-transitive`

### 3.3. Go (Game Server Core option, some Backend Services)

- **Package Manager (Mandatory):**
  - **Go Modules (`go mod`)**: Managed with `go.mod` and `go.sum` files.
- **Linter (Mandatory):**
  - **`golangci-lint`**: A fast, comprehensive Go linters runner.
  - _Configuration:_ Use a shared `.golangci.yml` configuration file.
- **Formatter (Mandatory):**
  - **`gofmt`** or **`goimports`** (which also manages imports). Enforce in CI.
- **Testing Frameworks (Recommended):**
  - Built-in `testing` package for unit tests.
  - _Consider:_ `testify/assert` and `testify/require` for assertions.
- **Vulnerability Scanner (Mandatory CI Step):**
  - **`govulncheck`**: Official Go vulnerability scanner.

### 3.4. Rust (Game Server Core option, PCG option)

- **Build Tool / Package Manager (Mandatory):**
  - **`Cargo`**: Managed with `Cargo.toml` and `Cargo.lock` files.
- **Linter (Mandatory):**
  - **`Clippy` (`cargo clippy`)**: Extensive linter for Rust. Configure via `clippy.toml` or in-code
    attributes. Treat warnings as errors in CI (`-D warnings`).
- **Formatter (Mandatory):**
  - **`rustfmt` (`cargo fmt`)**: Official Rust code formatter. Configure via `rustfmt.toml` or `.
rustfmt.toml`.
- **Testing Frameworks (Recommended):**
  - Built-in testing framework (`cargo test`).
  - _Consider:_ `proptest` for property-based testing, `criterion` for benchmarking.
- **Vulnerability Scanner (Mandatory CI Step):**
  - **`cargo audit`**: Checks `Cargo.lock` for dependencies with known security vulnerabilities.

### 3.5. Python (PCG, Backend Services, Scripting)

> **Canonical standard per ENG-ADR-069 (2026-05-12).** All three active Python repos
> (`gcd-ops-scripts`, `gcs-plt-tools`, `gcp-aethel-pcg`) have been migrated to this stack.
> New repos MUST use this stack; no alternatives are permitted.

- **Package & Environment Manager (Mandatory):**
  - **`Poetry`** — sole mandated tool. `pyproject.toml` + `poetry.lock`. No `requirements.txt`,
    no `pip install -r`, no raw `venv`. The `poetry.lock` file MUST be committed.

- **Linter + Formatter (Mandatory):**
  - **`Ruff`** — replaces Flake8, isort, Black, and Pylint. Single tool for both lint and format.
  - Run in CI as two separate steps: `ruff check .` (lint) and `ruff format --check .` (format).
  - Canonical `pyproject.toml` config block:
    ```toml
    [tool.ruff]
    line-length = 120
    # E/F/W = pycodestyle + pyflakes; I = isort; B = flake8-bugbear; PL = Pylint
    select = ["E", "F", "W", "I", "B", "PL"]
    ```

- **Type Checker (Mandatory):**
  - **`Mypy`** — gradual adoption schedule tied to wave milestones (ENG-ADR-069):
    - **Phase A (immediate):** lenient config — `ignore_missing_imports`, `warn_return_any`, `warn_unused_configs`
    - **Phase B (after Wave 1 Stream 5 complete):** add `disallow_untyped_defs = true`
    - **Phase C (before Phase 6 WI authoring):** `strict = true`
  - Canonical Phase A `pyproject.toml` config block:
    ```toml
    [tool.mypy]
    python_version = "3.11"
    ignore_missing_imports = true
    warn_return_any = true
    warn_unused_configs = true
    ```

- **Testing (Mandatory):**
  - **`pytest`** — all tests in `tests/` or `src/**/tests/`. Run via `poetry run pytest`.
  - `./test.sh` entry point MUST exist at repo root (calls `poetry run pytest`).

- **Vulnerability Scanner (Mandatory CI Step):**
  - **`pip-audit`** — run as `poetry run pip-audit` in a dedicated `security` CI job.
  - No alternative (`safety` is deprecated for studio use).

## 4. Configuration and CI Integration

- **Configuration Files:** Standardized base configuration files for these tools (e.g., `.eslintrc.js`, `.prettierrc.js`, `.golangci.yml`, `clippy.toml`, `../formatting/configs/pyproject.toml` for Ruff/Black/Mypy settings) **SHOULD** be maintained in a central location (e.g., `gcs-core-governance/tooling/configs/`) and referenced or used as templates for new projects.
- **CI Integration:** All linting, formatting checks (verify no changes needed), type checks, and vulnerability scans **MUST** be integrated as mandatory checks in the CI pipelines for Pull Requests. Refer to `../cicd/cicd-001-baseline-workflow-guidance.md`.
- **Pre-commit Hooks (Highly Recommended):** Use tools like `husky` (for JS/TS projects) or `pre-commit` (language-agnostic, good for Python and others) to run linters, formatters, and other checks locally before commits are made. This speeds up the feedback loop for developers.

## 5. Review and Updates

This standard will be reviewed periodically (e.g., annually or as significant new tooling emerges) by the
DevOps Team and relevant stakeholders (Architects, Lead Developers) to ensure it remains current and
effective. Proposed changes should follow the contribution process for the `GenCr-ft/devops-standards`
repository.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
