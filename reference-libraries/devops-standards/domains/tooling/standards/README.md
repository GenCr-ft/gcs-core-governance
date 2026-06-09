## Index of Contents

### Standards & Specifications

- [DEV-SPEC-001 · Markdown Linting Standard](DEV-SPEC-001.markdown-linting-standard.md): Establishes `markdownlint`/`markdownlint-cli` as the required tooling (with the VS Code extension and shared config) to enforce structure, readability, and CI enforcement for every Markdown file in the studio SSoT.
- [DEV-SPEC-002 · VS Code Recommendations](DEV-SPEC-002.vs-code-recommendations.md): Lists the required VS Code extensions and baseline `settings.json` configuration to guarantee a consistent development environment across contributors.
- [DEV-SPEC-003 · Environment Variables Standard](DEV-SPEC-003.environment-variables-standard.md): Defines the `GFT_<SERVICE>_<NAME>` naming convention plus storage guidance for environment variables across local, CI/CD, and production contexts.
- [DEV-SPEC-006 · Tool 004 Git Hooks Standard](DEV-SPEC-006.tool-004-git-hooks-standard.md): Mandates the `pre-commit` framework, the studio SSoT hook template, and required hooks (commitlint, sanity checks, markdown linting, secrets scanning, etc.) for every repository.
- [DEV-SPEC-007 · Tool 005 GitHub CLI Standard](DEV-SPEC-007.tool-005-github-cli-standard.md): Covers installation, authentication, token hygiene, scripting practices, and helper expectations for using the `gh` CLI in both human and automated workflows.
- [DEV-SPEC-008 · Tool 006 jq Usage Standard](DEV-SPEC-008.tool-006-jq-usage-standard.md): Documents how `jq` must be installed and invoked in scripts, including quoting, error handling, reusable patterns, and security considerations for JSON processing.
- [DEV-SPEC-010 · Specification: GenCr@ft Studio CLI (gft-cli)](DEV-SPEC-010.specification-gencrft-studio-cli-gft-cli.md): Serves as the full product spec for the `gft-cli`, detailing its principles, architecture, command groups, SSoT integrations, and acceptance criteria.
- [DEV-SPEC-012 · Conventional Commits Standard](DEV-SPEC-012.conventional-commits-standard.md): Implements Conventional Commits v1.0.0 as the mandatory commit format and publishes the machine-readable list of allowed `type` values for tooling.
- [DEV-SPEC-013 · Tool 003 Code Style and Formatting](DEV-SPEC-013.tool-003-code-style-and-formatting.md): Sets the studio-wide requirements for `.editorconfig`, mandatory formatters/linters, and CI enforcement of automated formatting across languages.
- [DEV-SPEC-014 · Tool 002 Language Specific Tooling Standards](DEV-SPEC-014.tool-002-language-specific-tooling-standards.md): Enumerates the approved linters, formatters, package managers, scanners, and testing stacks for TypeScript, C#, Go, Rust, and Python projects.
- [TOO-STAN-001 · SSoT Quality Gate: Automated Documentation Linting](TOO-STAN-001.ssot-quality-gate-automated-documentation-linting.md): Defines the documentation quality gate that validates docId conventions, frontmatter schema, and internal links via pre-commit hooks and GitHub Actions.

### Templates

- [`template/`](template): Shared scaffolding (e.g., `.editorconfig_standard`) referenced by multiple tooling standards.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
