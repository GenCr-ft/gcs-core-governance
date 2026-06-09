---
docId: GOV-GUIDE-101
title: "SSoT Remediation Guide: From Error to Compliance"
version: 0.1.0
creation_date: '2025-07-11'
last_updated_date: '2026-05-20'
authors:
  - "Iris (GCT-UTL-RWSKA-001)"
knowledgeGuardian:
- Iris (GCT-UTL-RWSKA-001)
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/sections/governance/GOV-GUIDE-101.ssot-remediation-guide.md
metadata:
  domain: governance
  lifecycle-stage: draft
  security-classification: "l1_internal"
  intended-audience:
    - "all-contributors"
    - "developers"
  scope: studio
  doc-type: guide
---

# SSoT Remediation Guide: From Error to Compliance

## 1. Introduction: Why This Guide Exists?

### 1.1. Our Vision: Supervised Automation

The "End of Chaos" mission is a studio-wide initiative to transform our Single Source of Truth (SSoT) from a source of friction into a reliable, scalable foundation for all our work. A key part of this mission is ensuring that every artifact we produce is compliant with our shared governance standards.

This is where the **Global SSoT Linter** comes in. Its purpose is not to block your work, but to guide it. Think of the linter not as a gatekeeper that says "no," but as a collaborative partner that says, "Almost there, here's how to get it right." It automates the tedious task of compliance checking so you can focus on what matters most: creating great content.

This guide is the human-friendly companion to that automated system.

### 1.2. How to Use This Document

This guide is your practical playbook for resolving any SSoT compliance error reported by the linter. Each section is designed to help you quickly understand the problem and apply the correct solution.

When your Pull Request is flagged by the linter, follow this simple workflow:

1. **Identify the Error:** Check the linter's automated comment on your Pull Request. It will list the specific error codes (e.g., `DOC_ID_MISMATCH`, `INVALID_TAXONOMY_TERM`).

2. **Find the Solution:** Navigate to the corresponding section in this guide. We explain the root cause of each error.

3. **Apply the Fix:** Follow the clear "Before/After" examples to correct the issue in your local branch. The goal is not just to fix the problem, but to understand the "why" behind the rule.

4. **Submit with Confidence:** Once you've applied the fixes and validated them locally with `gft validate`, use the `gft pr submit` command to push your changes. The linter will automatically re-run, and your check should now pass.

---

## 2. Error Category 1: Structure and Parsing Errors (`parsing_error`)

### 2.1. Context: The Foundation of Your Document

This is the most critical category of errors. A `parsing_error` means that our automated tooling cannot even read the metadata (the frontmatter) of your document. The file is considered structurally unsound.

These errors must be fixed first, as no other validation can run until the linter can successfully parse the file.

---

### 2.2. Error Case: `YAML_SYNTAX_ERROR`

> **Linter Message:** `Error: Invalid YAML syntax in frontmatter.`

**Root Cause:** This error is typically caused by incorrect indentation, a missing colon (`:`), or unescaped special characters within a string. YAML is very sensitive to whitespace.

**Solution:** Carefully check the indentation and syntax of your frontmatter block.

#### **Example:**

- **BEFORE: Invalid Indentation**

```yaml
---
docId: GOV-STAN-001
title: "My Document"
metadata:
domain: "Governance" # <-- ERROR: Incorrect indentation
---
```

- **AFTER: Correct Indentation**

```yaml
---
docId: GOV-STAN-001
title: "My Document"
metadata:
  domain: governance # <-- CORRECT: Indented under 'metadata'
---
```

---

### 2.3. Error Case: `MISSING_FRONTMATTER`

> **Linter Message:** `Error: No YAML frontmatter block found.`

**Root Cause:** The document is missing the `---...---` block at the very beginning of the file, or the delimiters are not correctly placed on their own lines.

**Solution:** The most reliable way to create a new, compliant document is to use the `gft new document` command, which generates a valid frontmatter block automatically.

If you are adding frontmatter to an existing file, ensure you add the opening `---` and closing `---` delimiters on their own lines at the top of the file, with the YAML content in between

---

## 3. Error Category 2: Identity and Naming Errors (`naming_convention_error`)

### 3.1. Context: The Unique Identity of Your Contribution

Every artifact in our SSoT must have a unique and predictable identity. This is fundamental to our ability to track, link, and manage knowledge at scale. The **`docId`** is the artifact's permanent, immutable identifier, and the filename must always be synchronized with it.

These errors occur when that synchronization is broken or the `docId` itself is invalid.

---

### 3.2. Error Case: `DOC_ID_MISMATCH`

> **Linter Message:** `Error: The 'docId' (GOV-STAN-001) in the frontmatter does not match the filename (GOV-STAN-002.some-standard.md).`

**Root Cause:** This happens when a file is renamed manually, or its `docId` is copied and pasted from another document without being updated. The **`docId` inside the file is always considered the single source of truth.**

**Solution:** You must rename the file to match the `docId`. The linter often suggests the exact new filename in its resolution message.

**Example:**

Your file is named `a-new-policy.md`. Inside the file, you have:

```yaml
---
docId: GOV-POLI-105
title: "A New Policy"
# ...
---
```

To fix this, you must rename the file itself:

- **INCORRECT:** `a-new-policy.md`
- **CORRECT:** `GOV-POLI-105.a-new-policy.md`

---

### 3.3. Error Case: `DOC_ID_FORMAT_INVALID`

> **Linter Message:** `Error: The 'docId' (My-Doc-1) does not follow the required format (e.g., DOMAIN-TYPE-NNN).`

**Root Cause:** The `docId` was created manually and does not conform to the studio's standard format. This format is crucial for automated processing and discoverability.

**Solution:** The `docId` is a system-generated identifier and **must never be created manually.** The only supported method for creating a new document with a valid `docId` is by using the `gft new document` command.

If you have content in a document with an invalid ID, you should:

1. Run `gft new document` in your terminal to create a new, compliant file with a valid `docId`.
2. Copy your content into this newly created file.
3. Delete the old file that had the invalid ID.

---

## 4. Error Category 3: Semantic Classification Errors (`taxonomy_violation`)

### 4.1. Context: Speaking the Studio's Common Language

This category of error means you are using a classification term that does not exist in our shared dictionary, `taxonomy.yml`. Our SSoT is built on a controlled vocabulary to ensure that everyone describes concepts in the same way. Using official terms is essential for discoverability, automation, and clear communication.

---

### 4.2. Error Case: `INVALID_TAXONOMY_TERM`

> **Linter Message:** `Error: The value 'Game Development' for the 'domain' field is not a valid term. Did you mean 'Product & Game Design'?`

**Root Cause:** This error is usually caused by a simple typo, using a plural form instead of a singular one, incorrect capitalization, or using a legacy term that has since been updated.

**Solution:**

1. **Trust the Linter's Suggestion:** The linter uses fuzzy matching to provide the most likely correction. In most cases, accepting the suggestion is the right choice.
2. **Use the CLI to Explore:** If you are unsure, you can use the `gft-cli` to explore the valid terms for a specific field. *(Note: This command will be specified in the `gft-cli` user guide).*
3. **Consult the Source:** As a last resort, you can directly consult the `taxonomy.yml` file in the `gcs-core-governance` repository.

**Example:**

- **BEFORE: Incorrect Term**

```yaml
---
# ...
metadata:
  domain: "devops" # <-- ERROR: Incorrect capitalization and term
# ...
---
```

- **AFTER: Correct Term from Taxonomy**

```yaml
---
# ...
metadata:
  domain: "DevOps & Infrastructure" # <-- CORRECT
# ...
---
```

---

### 4.3. What If a Term is Genuinely Missing?

Our taxonomy is a living system. If you believe a new term is needed to accurately classify your work, you should propose an addition. **Do not invent a term in your document.** Instead, follow the official governance process:

1. **Create an Issue:** Open a new issue in the `gcs-core-governance` repository using the "Taxonomy Change Proposal" template.
2. **Justify Your Proposal:** Clearly explain why the new term is needed and provide a definition and examples.
3. **Assign for Review:** Assign the issue to the `knowledgeGuardian` of the relevant domain (e.g., the "DevOps Crew" for a term related to `DevOps & Infrastructure`).

Your change will be discussed, and if approved, it will be added to `taxonomy.yml` and become available for everyone to use.

---

## 5. Error Category 4: Governance Rule Errors (`governance_rule_violation`)

### 5.1. Context: Playing by the Studio's Rules

This category of error is more advanced. It means your document's metadata is structurally sound and semantically correct (i.e., it uses valid terms from the taxonomy), but it violates a specific process or ownership rule defined by the studio.

These rules are stored in `validation-rules.yml` and ensure that our processes remain consistent and that the right experts are involved at the right times.

---

### 5.2. Error Case: `MISSING_REQUIRED_REVIEWER`

> **Linter Message:** `Governance Rule Violation (GOV_RULE_001): Documents in the 'Legal' domain must include 'Henri (GCT-LEG-LCOUN-001)' in the 'reviewers' list.`

**Root Cause:** Certain types of documents require review and approval from specific subject matter experts or designated `knowledgeGuardians` to ensure quality and compliance. Your document meets the criteria for one of these rules but is missing the required reviewer in its frontmatter.

**Solution:** You must add the required person or crew to the `reviewers` list in your document's frontmatter. This will ensure they are automatically added to the Pull Request for their review.

**Example:**

Based on rule `GOV_RULE_001`, any document in the "Legal" domain must be reviewed by "Henri (GCT-LEG-LCOUN-001)".

- **BEFORE: Missing Required Reviewer**

```yaml
---
docId: LEG-POLI-005
title: "Data Privacy Policy Update"
reviewers:
  - "Iris (GCT-UTL-RWSKA-001)"
metadata:
  domain: "Legal"
  # ...
---
```

- **AFTER: Correct Reviewer Added**

```yaml
---
docId: LEG-POLI-005
title: "Data Privacy Policy Update"
reviewers:
  - "Iris (GCT-UTL-RWSKA-001)"
  - "Henri (GCT-LEG-LCOUN-001)" # <-- CORRECT: Required reviewer added
metadata:
  domain: "Legal"
  # ...
---
```

---

## 6. Appendix: The Full Remediation Workflow

### 6.1. Scenario: My Pull Request is Blocked by the Linter

You've worked hard on a new feature or documentation update. You create a Pull Request (PR), but a few moments later, a red 'X' appears next to the **`Global SSoT Linter`** check. A comment from a bot has been posted with a list of errors.

Don't worry, this is a normal part of the process designed to help, not to block. This section walks you through the exact steps to resolve the issues and get your PR approved.

### 6.2. Step-by-Step Resolution

1. **Read the Linter's Comment**
    Carefully read the automated comment on your PR. It will provide a list of all detected errors, including the filename, the error code (e.g., `TAXONOMY_VIOLATION`), and a descriptive message.

2. **Consult This Guide**
    For each error reported by the linter, use the error code to find the corresponding section in this guide. Take a moment to understand the root cause of the issue.

3. **Apply the Corrections**
    In your local development branch, edit the file(s) to apply the solutions described in this guide.

4. **Validate Locally (Highly Recommended)**
    Before pushing your changes, confirm your fixes locally. Run the following command in your terminal:

    ```bash
    gft validate path/to/your/corrected-file.md
    ```

    If the command runs silently and returns no errors, your file is now compliant.

5. **Submit Your Corrections**
    Once your local validation passes, use our standard CLI command to commit and push your changes. This single command ensures your commit message is standardized and that all necessary steps are performed correctly.

    ```bash
    gft pr submit
    ```

    This command will handle adding, committing, and pushing your changes. The CI/CD system will automatically re-run the `Global SSoT Linter` on your Pull Request, which should now pass.
