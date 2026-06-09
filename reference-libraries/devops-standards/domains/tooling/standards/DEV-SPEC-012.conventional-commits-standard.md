---
docId: DEV-SPEC-012
title: Conventional Commits Standard
version: 1.1.0
authors:
- Gem-BB (Camille)
reviewers:
- Gem-AA (Lead)
- Gem-D (Strategy)
creation_date: '2025-06-11'
language: en
summary: This document defines the studio's mandatory standard for formatting Git
  commit messages based on the Conventional Commits v1.0.0 specification. Includes
  machine-readable data for tooling.
last_updated_date: '2026-05-20'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: approved
  keywords:
  - tooling
  - standard
  - git
  - conventional-commits
  - commitlint
  scope: studio
  domain: devops
  doc-type: specification
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/tooling/standards/DEV-SPEC-012.conventional-commits-standard.md
---
# Conventional Commits Standard

## 1. Purpose

This document establishes the mandatory standard for writing Git commit messages at GenCr@t Studio. Adherence to this standard is critical for maintaining a clean, readable, and navigable version history.

It enables automated changelog generation, simplifies semantic versioning, and allows for better collaboration between humans and AI agents.

This standard is a strict implementation of the **[Conventional Commits v1.0.0 specification](https://www.conventionalcommits.org/en/v1.0.0/)**.

## 2. Specification

A commit message consists of a header, an optional body, and an optional footer.

```cmd
  <type>[optional scope]: <description>

  [optional body]

  [optional footer(s)]
```

### 2.1. Header

The header is the only mandatory part of the message.

- **`<type>`**: Must be one of the types defined in the Machine-Readable Data section below. This describes the kind of change you're committing.
- **`[optional scope]`**: A noun in parentheses describing the part of the codebase affected (e.g., `auth`, `ui`, `player-inventory`).
- **`<description>`**: A short, imperative-mood description of the change, starting with a lowercase letter.

### 2.2. Body (Optional)

The body is used to provide additional context, explaining the "what" and "why" of the change. It must be separated from the header by one blank line.

### 2.3. Footer (Optional)

The footer is used for metadata.

- **Breaking Changes**: Must start with `BREAKING CHANGE:` followed by a description of the change.
- **Referencing Issues**: Used to link to GitHub issues (e.g., `Refs: #13`, `Closes: #42`).

## 3. Machine-Readable SSoT Data

To enable automation, the definitive list of allowed `type`s is defined in the YAML block below. This data **must** be used by tools like `commitlint` and the `gft-cli`.

```yaml
# SSoT data for Conventional Commits
# This list is used by gft-cli to generate interactive prompts
# and by the commitlint.config.js for validation.

commit_types:
  - name: "feat"
    description: "A new feature for the user."
  - name: "fix"
    description: "A bug fix for the user."
  - name: "docs"
    description: "Documentation only changes."
  - name: "style"
    description: "Code style changes (formatting, etc)."
  - name: "refactor"
    description: "A code change that neither fixes a bug nor adds a feature."
  - name: "perf"
    description: "A code change that improves performance."
  - name: "test"
    description: "Adding or correcting tests."
  - name: "build"
    description: "Changes to the build system or external dependencies."
  - name: "ci"
    description: "Changes to our CI configuration and scripts."
  - name: "chore"
    description: "Other changes that don't modify src or test files."
  - name: "revert"
    description: "Reverts a previous commit."
```

## 4. Examples

### Good Commit Message

```cmd
feat(api): add endpoint for user profiles

This new endpoint allows fetching user profiles by their unique ID.
It includes pagination and returns a limited set of public fields
to ensure privacy.

Closes: #78
```

### Commit Message with a Breaking Change

```cmd
  refactor(auth): rename User model to StudioMember

  BREAKING CHANGE: The `User` model has been renamed to `StudioMember`
  to better reflect its purpose. All services interacting with the
  authentication API must update their data models accordingly.
```

## 5. Enforcement & Tooling

This standard is not just a guideline; it is enforced automatically.

- **`pre-commit` Hook:** Our standard `.pre-commit-config.yaml` includes a hook that runs `commitlint` on every commit message. Commits that do not comply with this standard will be rejected.
- **`gft-cli` Assistant:** The `gft-cli git commit` command provides an interactive, guided experience to help all studio members create compliant commit messages easily and without errors.

---

## IA Instructions

- **Purpose for AI Agents:** This document is the SSoT for Git commit message formatting. Use the YAML data block under `commit_types` to populate interactive choices when assisting a user with a commit.
- When validating a commit message, ensure the `type` is one of the `name` values in the YAML block.
