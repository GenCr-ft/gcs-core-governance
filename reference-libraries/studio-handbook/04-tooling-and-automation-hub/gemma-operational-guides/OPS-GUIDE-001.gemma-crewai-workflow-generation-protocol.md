---
docId: OPS-GUIDE-001
title: Gemma Crewai Workflow Generation Protocol
version: 1.0.1
authors:
- AI Compliance Agent
creation_date: '2025-05-26'
language: en
last_updated_date: '2026-05-20'
metadata:
  lifecycle-stage: approved
  keywords:
  - gemma-workflow-generation
  - crewai
  - gencraft
  - automation
  - python-script
  - workflow-definition
  scope: studio
  domain: production-management
  doc-type: protocol
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  security-classification: l2_confidential
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/04-tooling-and-automation-hub/gemma-operational-guides/OPS-GUIDE-001.gemma-crewai-workflow-generation-protocol.md
---
# Gemma Operational Protocol: CrewAI Workflow Generation

## 1. Purpose

This protocol outlines the steps `Gemma` (GCT-UTL-GGEN-001) MUST follow to
generate a new Gencraft CrewAI workflow. This includes the creation of a Python
workflow definition script (`.py`) and its corresponding Markdown documentation
file (`.md`), based on input specifications and standard Gencraft templates.

## 2. Inputs Required by Gemma

Gemma requires the following structured inputs to initiate workflow generation:

1. **`workflow_creation_request` (Structured Data, e.g., JSON/YAML):**
    - `proposed_workflow_id`: (String) Suggested unique ID (e.g., `CW-PROJECTX-
      FEATUREY-V0.1`). Gemma will version this to `vX.Y.Z-draft`.
    - `workflow_purpose_description`: (String) High-level objective of the
      workflow.
    - `involved_gem_roles`: (List of Strings) List of Gencraft Gem Role Titles
      (e.g., ["Producer / Project Manager", "Software Architect"]).
    - `key_tasks_overview_structured`: (List of Objects) For each task:
        - `task_name`: (String) Short name for the task.
        - `task_description_brief`: (String) Brief description of the task's
          goal.
        - `assigned_gem_role`: (String) Role Title of the Gem to perform this
          task.
        - `task_dependencies`: (List of Strings, optional) Names of preceding
          tasks this task depends on.
    - `workflow_inputs_specification`: (List of Objects) For each workflow
      input:
        - `input_name`: (String)
        - `input_type`: (String, e.g., "String", "FilePath:SSoT", "JSON")
        - `input_description`: (String)
        - `is_required`: (Boolean)
    - `workflow_outputs_specification`: (List of Objects) For each workflow
      output:
        - `output_name`: (String)
        - `output_type`: (String, e.g., "MarkdownDocument:SSoT", "JSON_String",
          "StatusFlag")
        - `output_description`: (String)
    - `initiator_reference`: (String) GemID or Human Name of the requester.
    - `target_ssot_category_path`: (String) Path within `gencraft-crew-
      workflows/workflows/` where the workflow files should be stored (e.g.,
      `project_alpha/content_creation_crew`).

2. **Access to SSoT Repositories:**
    - `gcs-plt-gembp/blueprints/`: To retrieve specific Gem Blueprint
      YAML files.
    - `gencraft-gem/G-FT.ai/`: To retrieve Gem Definition Markdown files.
    - `gencraft-crew-workflows/templates/`: For workflow templates.
    - `gencraft-crew-workflows/common_tools_for_crews/` and `common_tasks/`: For
      potential re-use.
    - `Gencraft Studio Handbook` (especially `04-tooling-and-automation-hub/Gem-
      Tools-Overview.md` - conceptual).

## 3. Workflow Generation Process (To Be Executed by Gemma)

### Phase 1: Python Script (`.py`) Generation

1. **Determine File Paths & Version:**
    - Base filename: `{proposed_workflow_id}`. Initial version: `0.1.0-draft`.
    - Python file path: `gencraft-crew-
      workflows/workflows/{target_ssot_category_path}/{base_filename}_v0.1.0-draft.py`.
2. **Initialize Python File:**
    - Copy the content of `gencraft-crew-workflows/templates/crew-workflow-
      definition-template.py` to the new file path. This template is a
      structural outline.
    - Update the header comments in the new `.py` file:
        - `File:` (actual filename)
        - `Version:` 0.1.0-draft
        - `Date:` Current date (YYYY-MM-DD)
        - `Author:` `Gemma (GCT-UTL-GGEN-001)` based on request from
          `{initiator_reference}`.
        - `SSoT Location:` (actual path to this .py file).
3. **Populate Python Script Sections:**

    - **Section 1 (IMPORTS):**
        - Ensure `Agent`, `Crew`, `Process`, `Task` from `crewai` and `BaseTool`
          from `crewai_tools` are imported.
        - Add import for `GencraftLLM` (conceptual Gencraft LLM wrapper).
        - Identify required `Tools` based on `involved_gem_roles` (from their
          Blueprints' `capabilities.toolsAccess`) and
          `key_tasks_overview_structured`. Add import statements for these tools
          (from `common_tools_for_crews` or generate placeholders if custom).
    - **Section 2 (WORKFLOW CONFIGURATION):**
        - Set `WORKFLOW_ID` using the full versioned ID (e.g.,
          `"{proposed_workflow_id}_v0.1.0-draft"`).
        - Set `WORKFLOW_VERSION = "0.1.0-draft"`.
        - Define `GENCRAFT_LLM_INSTANCE` (placeholder for how Gemma
          accesses/configures the LLM).
    - **Section 3 (TOOL DEFINITIONS):**
        - For each unique `Tool` identified in step 3.1 that is not available in
          `common_tools_for_crews/`, generate a placeholder class structure
          using `gencraft-crew-workflows/templates/crew-tool-template.py` within
          this script or flag as a missing dependency. Instantiate all required
          tools.
    - **Section 4 (AGENT DEFINITIONS):**
        - For each Gem role in `involved_gem_roles`:
            1. Fetch the Gem's Blueprint YAML and Markdown Definition file.
            2. Extract `operationalParams.role` for CrewAI `role`.
            3. Synthesize CrewAI `goal` from Blueprint's
                `gemCoreInfo.description` and the specific role of this Gem
                *within this workflow* (derived from
                `key_tasks_overview_structured`).
            4. > ⚠️ **[PENDING: GEM-SPEC-STD-001 — gcs-core-governance issues #44, #51]**
               > This backstory synthesis step is superseded by `SYSTEM.md` (GCS-STD-003).
               > Once `personaFilesRef` is populated in the Gem's Blueprint, Gemma MUST
               > load `SYSTEM.md` as the system prompt instead of synthesizing from the
               > Gem Definition Markdown. Until then, Gemma continues to use the legacy
               > synthesis below.
               >
               > Synthesize CrewAI `backstory` from the Gem Definition Markdown
               > (Role & Mission, Core Principles) and relevant
               > `configurationPrompts.gemmaBackstoryElements_JSON` from the
               > Blueprint, tailored to the workflow's context.
            5. Configure the `llm` using `aiModelConfig.baseModel` from the
                Blueprint via `GENCRAFT_LLM_INSTANCE`.
            6. List `tools` by instantiating the `Tool` objects identified in
                Section 3 that are relevant to this Gem's role in *this
                workflow* (cross-reference with Blueprint's
                `capabilities.toolsAccess`).
            7. Set `allow_delegation` (e.g., from a new
                `operationalParams.defaultDelegation` field in Blueprint, or
                default to `True` for lead roles, `False` otherwise).
            8. Instantiate `Agent` and assign to a uniquely named variable
                (e.g., `agent_role_name_instance`).
    - **Section 5 (TASK DEFINITIONS):**
        - For each task in `key_tasks_overview_structured`:
            1. Generate a detailed `description` string. This description MUST
                clearly state the task's objective, any specific inputs it
                requires (referencing workflow inputs by their placeholder
                names, e.g., `{workflow_input_name_1}`, or outputs of antecedent
                tasks using `task.context`), and the PRECISE `expected_output`
                format.
            2. Assign the appropriate `agent` (variable name from Section 4).
            3. Define `context` by listing the variable names of prerequisite
                task instances.
            4. Instantiate `Task` and assign to a uniquely named variable
                (e.g., `task_name_instance`).
    - **Section 6 (CREW DEFINITION & INSTANTIATION):**
        - Populate `agents` list with agent instance variables.
        - Populate `tasks` list with task instance variables.
        - Set `process` (default to `Process.sequential`).
    - **Section 7 (WORKFLOW EXECUTION):**
        - Adapt the `run_workflow(inputs: dict)` function signature if
          `workflow_inputs_specification` defines specific typed inputs.
        - Populate the `workflow_inputs` dictionary within `run_workflow` to map
          function arguments to the placeholders used in `Task` descriptions.

### Phase 2: Markdown Documentation (`.md`) Generation

1. **Determine File Paths & Version:**
    - Markdown file path: `gencraft-crew-
      workflows/workflows/{target_ssot_category_path}/{base_filename}_v0.1.0-draft.md`.
2. **Initialize Markdown File:**
    - Copy the content of `gencraft-crew-workflows/templates/crew-workflow-
      documentation-template.md` to the new file path. This template is a
      structural outline.
3. **Populate Markdown Frontmatter:**
    - `workflowId`: Same as Python script (e.g.,
      `"{proposed_workflow_id}_v0.1.0-draft"`).
    - `workflowVersion`: "0.1.0-draft".
    - `status`: "Draft".
    - `dateCreated`: Current date.
    - `lastUpdated`: Current date.
    - `authors`: `["Gemma (GCT-UTL-GGEN-001)", "{initiator_reference}"]`.
    - `knowledgeGuardian`: (e.g., AIE Team Lead, or initiator for review).
    - `pythonImplementation`: Relative link to the generated `.py` file.
    - `tags`: (Generate relevant tags based on purpose and involved
      Gems/domains).
4. **Populate Markdown Sections:**
    - **Section 1 (Purpose & Objective):** Use `workflow_purpose_description`.
    - **Section 2 (Crew Composition):** List agents from Python script (Role
      Title, GemID placeholder if known), link to their Gem
      Definition/Blueprint, and summarize their responsibility *in this
      workflow*.
    - **Section 3 (Workflow Inputs):** Detail each input from
      `workflow_inputs_specification`.
    - **Section 4 (Workflow Process):**
        - **4.1 (Task List & Descriptions):** List each Task from Python script,
          assigned agent, and its `description` (or a summary).
        - **4.2 (Workflow Diagram):** Generate a basic Mermaid flowchart based
          on sequential task dependencies. Note that human refinement might be
          needed for complex flows.
    - **Section 5 (Workflow Outputs):** Detail each output from
      `workflow_outputs_specification`.
    - **Section 6 (Operational Parameters):** Document key CrewAI parameters
      (e.g., `process`, `max_iterations` if set).
    - **Section 7 (Dependencies):** List key Gem Blueprint versions and Tools
      referenced.
    - **Section 8 (Error Handling):** Add a standard placeholder statement about
      error logging and potential escalation to S3/S18.
    - **Section 9 (Security Considerations):** Add a standard placeholder
      statement about data sensitivity and tool permissions.
    - **Section 10 (Changelog):** Initialize with v0.1.0-draft.

### Phase 3: Output and Next Steps

1. **Output:** Gemma provides the paths to the generated `.py` and `.md` files.
2. **Action Required:** The generated files are in "Draft" status. They MUST be
    committed to a new branch in the `gencraft-crew-workflows` repository and a
    Pull Request opened for human review by the AIE Team and relevant
    stakeholders (e.g., initiator, KGs of involved Gem roles) as per Protocol
    S1. The review will focus on:
    - Correctness of logic in the Python script.
    - Clarity and completeness of task descriptions for LLM interpretation.
    - Accuracy and completeness of the Markdown documentation.
    - Adherence to all Gencraft standards.

This protocol ensures that `Gemma` can systematically generate the initial
structure and content for new CrewAI workflows, significantly accelerating their
development while maintaining consistency.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
