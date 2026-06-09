---
docId: TOO-STAN-001
title: 'SSoT Quality Gate: Automated Documentation Linting'
version: 1.0.0
authors:
- Isaac (Architect)
- "\xC9douard (DevOps)"
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
language: en
summary: This standard defines the automated checks required to enforce compliance
  with Gencraft Studio's SSoT documentation standards, including naming conventions,
  frontmatter schema, and internal link integrity. It acts as a mandatory 'Quality
  Gate' to ensure the reliability and navigability of our knowledge base.
metadata:
  scope: studio
  domain: tooling
  doc-type: standard
  lifecycle-stage: approved
  security-classification: l1_internal
  intended-audience:
  - developers
  - devopscrew
  - aiagents
  - knowledgeguardians
  keywords:
  - quality
  - ssot
  - linting
  - automation
  - ci-cd
  - git-hooks
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/tooling/standards/TOO-STAN-001.ssot-quality-gate-automated-documentation-linting.md
---
# SSoT Quality Gate: Automated Documentation Linting

## 1. Objective

This standard defines the automated checks required to maintain the structural integrity, consistency, and quality of all documents within the GenCr@ft Studio Single Source of Truth (SSoT).

Its purpose is to create a "Quality Gate" that prevents common errors, such as broken links or incorrect metadata, from being introduced into our knowledge base. This guarantees that our SSoT remains reliable and navigable for both humans and AI agents.

## 2. The Quality Gate: A Two-Layered Approach

To enforce SSoT quality, we will implement automated validation at two critical stages of the development workflow. Both stages will run the same core validation script.

**Local Validation (Prevention):**

- **Mechanism:** A pre-commit Git hook.
- **Trigger:** Automatically runs on a developer's machine each time they execute `git commit`.
- **Behavior:** If any validation check fails, the commit is blocked, and a clear error message is displayed, guiding the user to fix the issue. This is our first line of defense.

**Server-Side Validation (Guarantee):**

- **Mechanism:** A mandatory GitHub Action workflow.
- **Trigger:** Automatically runs on the server for every push to a Pull Request branch.
- **Behavior:** If any validation check fails, the action will fail, and the Pull Request will be blocked from being merged. This is our ultimate guarantee of quality.

## 3. Mandatory Validation Checks

The SSoT Quality Gate script (`ssot-linter`) MUST perform the following three categories of checks on all modified Markdown (`.md`) files.

### 3.1. Check 1: Naming and docId Convention

The linter will enforce strict compliance with the **`GOV-STANDARD-005.ssot-document-id-convention.md`** [https://github.com/GenCr-ft/gcs-core-governance/blob/main/foundations/governance/GOV-STANDARD-005.ssot-document-id-convention.md].

- It MUST read the `docId` from the YAML frontmatter.
- It MUST validate that the `docId` structure (DOMAIN-TYPE-CODE) and casing (UPPERCASE) are correct, as defined in `GOV-STANDARD-005`.
- It MUST validate that the filename matches the `docId` and follows the pattern `<docId>.<description-in-kebab-case>.md`, as defined in `GOV-STANDARD-005`.

### 3.2. Check 2: Frontmatter Schema

The linter will validate the presence and structure of mandatory fields in the YAML frontmatter of the document, as well as the validity of their values.

- The complete schema for mandatory and recommended frontmatter fields, including the structure of the `metadata:` block and the deprecation of the `tags:` field, is defined in **`GOV-STANDARD-006.metadata-and-tagging-policy.md`** [https://github.com/GenCr-ft/gcs-core-governance/blob/main/foundations/governance/GOV-STANDARD-006.metadata-and-tagging-policy.md].
- The allowed values for all controlled facets (e.g., `scope`, `domain`, `doc-type`, `lifecycle-stage`, `security-classification`, `intended-audience`) are strictly defined in the official SSoT Taxonomy document: **`GOV-TAXONOMY-001.ssot-metadata-taxonomy.md`** [https://github.com/GenCr-ft/gcs-core-governance/blob/main/foundations/governance/GOV-TAXONOMY-001.ssot-metadata-taxonomy.md].
- The linter MUST verify that all fields mandated by `GOV-STANDARD-006` (including `language` and `summary`, which are also validated by this Quality Gate) are present and non-empty.
- The linter MUST ensure that the values used for controlled facets conform to the definitions in `GOV-TAXONOMY-001`.
- The `tags:` field is explicitly disallowed and will cause validation to fail.

### 3.3. Check 3: Internal Link Integrity

To prevent a "dead" SSoT, the linter MUST validate all internal links.

- It will parse the document content and extract all relative Markdown links (e.g., a link to a local file, or a link to a parent directory document).
- It will ignore absolute URLs and internal page anchors (`#section-link`).
- For each relative link, it will resolve the path and verify that the target file or directory actually exists on the filesystem.
- If a link is broken, the linter will fail and report the broken link's path and the source file containing it.

## 4. Implementation Plan

- A new Python script, `ssot-linter`, will be developed and stored in the `gcd-ops-scripts` repository.
- The `.pre-commit-config.yaml` file in our repository templates will be updated to include a hook that runs this linter.
- A new reusable GitHub Action, `ssot-linter-action`, will be created and added as a required status check for all SSoT repositories.
