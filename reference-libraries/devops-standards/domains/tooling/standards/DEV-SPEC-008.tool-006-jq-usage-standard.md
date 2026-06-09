---
docId: DEV-SPEC-008
title: Tool 006 jq Usage Standard
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This standard defines mandatory guidelines for using the `jq` command-line
  JSON processor within Gencraft studio scripts, focusing on consistency, readability,
  correctness, and maintainability.
last_updated_date: '2026-06-02'
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - jq
  - json
  - standard
  - gencraft
  - automation
  - scripting
  - tooling
  scope: studio
  domain: devops
  doc-type: specification
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/tooling/standards/DEV-SPEC-008.tool-006-jq-usage-standard.md
---
## 1. Objective

This standard defines the mandatory guidelines for using the `jq` command-line JSON processor within
Gencraft studio scripts and automations. The objectives are to ensure:

- **Consistency:** Uniform `jq` filter syntax and invocation across scripts.
- **Readability:** `jq` expressions are understandable by both humans and AI Gems.
- **Correctness:** Accurate parsing and manipulation of JSON data.
- **Maintainability:** Ease of updating and debugging `jq` filters.
- **Efficiency:** Appropriate use of `jq` for optimal performance in scripts.

## 2. Scope

This standard applies to ALL Gencraft Gems and human contributors who write or maintain scripts (primarily
Bash/shell scripts, but also applicable where `jq` is invoked from other languages or CI/CD steps) that
use `jq` to process JSON data. This includes interactions with APIs (like GitHub API via `gh`),
configuration files, or any other JSON-formatted data sources.

## 3. Standard

### 3.1. Installation and Version

- **Tool:** `jq` - Command-line JSON processor ([https://stedolan.github.io/jq/](https://stedolan.github.io/jq/))
- **Minimum Required Version:** `jq-1.6` (or as specified in the latest
  `validate_gft_devops_environment_proj103.sh` script and `gcs-core-governance/tooling/TOOL_README.md`).
- **Installation:**
  - For Linux/WSL: `sudo apt-get install jq`
  - For macOS: `brew install jq`
  - Refer to official `jq` documentation for other systems.
- **Verification:** The presence and version of `jq` MUST be verifiable by the
  `validate_gft_devops_environment_proj103.sh` script. `Camille` (Gem AB) is responsible for updating this
  validation if the standard version changes.

### 3.2. Basic Usage Principles

- **Quoting Filters:**
  - Simple filters without spaces or special shell characters MAY be unquoted (e.g., `.name`).
  - It is STRONGLY RECOMMENDED to enclose all `jq` filters in single quotes (`'filter'`) in shell
    scripts to prevent shell expansion and handle special characters safely. Example: `jq '.items[] |
select(.active==true) | .name'`
- **Input to `jq`:** JSON input should typically be piped to `jq`. Example: `cat data.json | jq '.'` or
  `gh api /user | jq '.login'`.
- **Simplicity and Readability:**
  - Prefer multiple simple, chained `jq` operations over a single, overly complex filter if it enhances readability.
  - Break down complex filters onto multiple lines within the script using shell line continuation (`\`)
    for better readability if necessary (see section 3.5).
- **Error Handling in Scripts:**
  - Scripts invoking `jq` MUST check its exit code. `jq` exits with `0` if the last output was a
    non-false/non-null value, `1` if the filter had a syntax error, `2` if `jq` was invoked with invalid
    option(s), `3` if the filter produced no results or only `false` or `null`, and `4` if memory
    allocation failed. For most Gencraft use cases, an exit code other than `0` (when output is expected)
    or `3` (when no output is acceptable) should be treated as an error.
  - Implement error handling as per `../scripting/script-001-general-scripting-standard.md`.
  - Handle cases where JSON input might be malformed or missing expected fields gracefully (e.g., using
    `//` for default values, `?` for optional chaining, or explicit checks like `has("field")` or `type ==
"object"`).

### 3.3. Common Patterns and Best Practices

1. **Extracting Specific Field Values:**
   - Single field: `jq -r '.field.subfield'` (use `-r` for raw string output without quotes).
   - Multiple fields into a new JSON object: `jq '{newName: .oldName, another: .path.to.value}'` 2.**Working with Arrays:**
   - Accessing elements: `jq '.[0]'` (first element), `jq '.[-1]'` (last element).
   - Iterating and extracting: `jq '.array[].name'` (get all `name` fields from objects in `array`).
   - `map(expression)`: Apply an expression to each element of an input array.
     Example: `jq '.users | map({id: .userId, name: .username})'`
   - `select(boolean_expression)`: Filter array elements.
     Example: `jq '.items[] | select(.count > 10)'` 3.**Creating/Modifying JSON Structures:**
   - Constructing objects: `jq -n '{key1: "value1", key2: $myvar}' --arg myvar "some_value"`
   - Adding/updating fields: `jq '.object.newField = "newValue"'` or `jq '.object + {anotherField: "anotherValue"}'` 4.**Using `jq` Variables:**
   - Pass shell variables into `jq` using `--arg varname "value"` or `--argjson varname '{"json":"value"}
'`.
     Example: `repo_name="my-repo"; gh api "/repos/GenCr-ft/$repo_name" | jq --arg rn "$repo_name" '.name = $rn'` 5.**Conditional Logic:**
   - `if A then B else C end`: Standard conditional.
   - `//` (Alternative operator): `jq '.optionalField // "default_value"'` (provides a default if `.
optionalField` is null or not found). 6.**Output Control:**
   - `-r` (raw output): Essential for extracting string values to be used in shell variables or commands,
     removes JSON string quotes.
     Example: `LOGIN=$(gh api /user | jq -r '.login')`
   - `-c` (compact output): Outputs entire JSON on a single line. Useful for machine-to-machine communication.
   - `-S` (sort keys): Sorts keys in JSON objects before outputting. Useful for consistent diffs. 7.**Reading from Files:**
   - `jq '.' myfile.json`
   - `--slurpfile varname filepath`: Reads an entire JSON file into a `jq` variable.

### 3.4. Security Considerations

- **Untrusted Input:** While `jq` itself is not a shell interpreter, avoid constructing `jq` filter
  strings _directly and unsafely_ from untrusted external input. Use `--arg` or `--argjson` to pass external
  data into filters.
- **Large JSON Files/Streams:** Processing extremely large JSON documents entirely in memory with `jq` can
  be resource-intensive. For very large datasets, consider stream-processing alternatives or ensure
  sufficient resources.
- **Error Message Verbosity:** `jq` error messages can sometimes expose parts of the input JSON or the
  filter. Ensure that scripts handling `jq` errors do not log excessively verbose or sensitive information
  from these errors (as per `../scripting/script-001-general-scripting-standard.md`).

### 3.5. Readability and Maintainability of `jq` Filters

- **Clarity over Brevity:** A slightly longer but clearer filter is preferable to a short, cryptic one.
- **Comments in Calling Script:** Since `jq` filters do not support internal comments, complex filters
  SHOULD be explained with comments in the calling shell script immediately preceding the `jq` command.
- **Formatting Long Filters (in shell scripts):**

```bash
  # Example: Get active, high-priority user names
  USER_NAMES=$(echo "$JSON_DATA" | jq -r '
    .users[]
    | select(.active == true and .priority == "high")
    | .name
  ')
```

- **Reusable Filters (Advanced):** For very complex or frequently reused filter logic, consider defining
  'jq' functions in a '.jq' file and using 'jq -L. 'include "myfunctions"'; 'my_filter' or sourcing them if
  appropriate. This is an advanced use case and should be discussed with 'Camille' (Gem AB).

### 3.6. When _Not_ to Use `jq` (Alternatives)

- **Within High-Level Languages:** If already scripting in Python, Node.js, etc., use the language's
  native JSON parsing libraries (e.g., Python's `json` module) for better integration, type safety, and more
  complex programmatic manipulation. `jq` is primarily for shell-level JSON processing.
- **Very Simple Extractions on Trusted Data (Bash):** For extremely simple cases where only one easily
  accessible value is needed from a trusted JSON structure, and adding a `jq` dependency is undesirable,
  basic shell string manipulation or tools like `grep`/`sed`/`awk` _might_ be used cautiously. However, this
  is error-prone and `jq` is generally safer and more robust. This approach is DISCOURAGED.

### 3.7. Actionability for AI Gems

- **Structured Output Expectation:** AI Gems invoking scripts that use `jq` to produce JSON output need to
  have a clear definition (e.g., a JSON schema or example) of the expected output structure from the `jq` filter.
- **Error Interpretation:** AI Gems need to be able to interpret the standard exit codes (section 3.2) and
  any structured error messages provided by the calling script to understand if the `jq` processing was successful.
- **Dynamic Filters:** If an AI Gem is constructing or providing parts of a `jq` filter, extreme care must
  be taken to ensure the generated filter is valid and secure (see section 3.4). Passing data via `--arg` is safer.

## 4. Responsibilities

- **Script Authors (All Gems using `jq`):**
  - Adherence to this standard.
  - Writing clear, maintainable, and correct `jq` filters.
  - Documenting complex `jq` usage within their scripts.
- **`Camille` (Gem AB - Automation Specialist):**
  - Knowledge Guardian for this standard.
  - Providing expert guidance and training on `jq` usage.
  - Reviewing complex `jq` implementations in critical automation scripts.
  - Maintaining examples of best practices.
- **`Édouard` (Gem AD - DevOps Strategy Specialist):**
  - Ensuring this standard aligns with the overall tooling strategy.
- **Code Reviewers:**
  - Verifying adherence to this standard during PR reviews of scripts containing `jq` commands.

## 5. Examples (Illustrative)

Assume `GH_TOKEN` is set and `gh` is installed.

- **Example 1: Get names of all open pull requests for a repo**

```bash
REPO_OWNER="GenCr-ft"
REPO_NAME="gcs-core-governance"

gh api "repos/$REPO_OWNER/$REPO_NAME/pulls?state=open" | jq -r '.[].title'
```

- **Example 2: Get the login of the assignees for a specific issue, handling no assignees**

```bash
# ... REPO_OWNER, REPO_NAME set ...
ISSUE_NUMBER="42"

ASSIGNEES=$(gh api "repos/$REPO_OWNER/$REPO_NAME/issues/$ISSUE_NUMBER" | jq -r '.assignees[]?.login // "None"')
echo "Assignees for issue #$ISSUE_NUMBER: $ASSIGNEES"
```

- **Example 3: Create a JSON object from shell variables**

```bash
USER_ID="user123"
USER_ROLE="editor"

NEW_USER_JSON=$(jq -n \
  --arg id "$USER_ID" \
  --arg role "$USER_ROLE" \
  '{userId: $id, role: $role, status: "active"}'
)
echo "$NEW_USER_JSON"
# Output: {"userId": "user123", "role": "editor", "status": "active"}
```

## 6. References

- `jq` Official Documentation: <https://stedolan.github.io/jq/manual/>

- `jq` Cookbook: <https://github.com/stedolan/jq/wiki/Cookbook>
- `../scripting/script-001-general-scripting-standard.md`
- `tool-005-github-cli-standard.md`

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
