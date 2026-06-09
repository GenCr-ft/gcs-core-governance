---
docId: ENG-STANDARD-007
title: Crewai Workflows Repository Standard
version: 1.0.0
authors:
- AI Compliance Agent
creation_date: '2025-05-26'
language: en
last_updated_date: '2026-05-20'
metadata:
  lifecycle-stage: approved
  keywords:
  - technical-writing
  - crewai
  - workflow
  - standards
  - python
  - automation
  - gencraft
  - repository
  scope: studio
  domain: engineering
  doc-type: standard
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  security-classification: l2_confidential
knowledgeGuardian:
- Antoine (GCT-MGT-PPM-001)

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/04-tooling-and-automation-hub/ENG-STANDARD-007.crewai-workflows-repository-standard.md
---
# Gencraft CrewAI Workflows Repository Standard

## 1. Introduction and Purpose

This document defines the mandatory standards for the structure, development, documentation, testing, and contribution workflows associated with the **`gencraft-crewai-workflows`** Git repository. This repository serves as the Gencraft studio's Single Source of Truth (SSoT) for the Python source code that defines all **studio-wide, reusable Gencraft Crews**. These Crews leverage the CrewAI framework (`https://github.com/crewAIInc/crewAI`) to orchestrate AI Gems for collaborative, autonomous, and complex task execution, with the primary goal of enhancing Gencraft's operational efficiency and game development capabilities.

The objectives of this standard are to:

- Establish a clear, consistent, and scalable structure for the `gencraft-crewai-workflows` repository.
- Define rigorous development, documentation, testing, versioning, and contribution guidelines for all Gencraft Crew definitions.
- Ensure that Gencraft Crew definitions are modular, maintainable, reusable, secure, and easily discoverable by both humans and AI Gems (e.g., for understanding capabilities or for potential dynamic invocation).
- Facilitate the effective integration of Crews into Gencraft's operational processes and their diligent management by the AI Enablement Team (AIE Team).

This standard is actively maintained by the AIE Team Lead (`GCT-UTL-AIETL-001`Aura) and forms a critical part of Gencraft's automation and AI strategy. It is a supplement to the overarching `ai-tool-development-standards.md`.

## 2. Repository Naming and Scope

- **Repository Name:** `gencraft-crewai-workflows`
- **Scope:** This repository is the designated SSoT to host, version, and manage the Python source code for all Gencraft Crews that are designed for **studio-wide application or significant reusability across multiple projects or departments.**
  - **Note on Project-Specific Crews:** Highly specialized Crews exclusively tied to a single game project *could* potentially reside within that project's specific repository (e.g., `gencraft-flagship-game/crews/`). However, they **MUST** still adhere to all structural, development, documentation, and testing standards outlined in this document. Furthermore, an entry for such project-specific Crews, clearly linking to their SSoT definition, **MUST** be cataloged in `gcs-core-governance/04-tooling-and-automation-hub/Studio-Crews-Overview.md`.
  - **Default Location:** For initial Gencraft operations and to maximize reusability, discovery, and centralized governance, **all Crews SHOULD preferably reside in `gencraft-crewai-workflows`** unless a compelling justification for project-specific location is formally approved by the AIE Team Lead (`GCT-UTL-AIETL-001` Aura) and `GCT-PRG-SARCH-001` (Isaac - Software Architect).

## 3. Repository Structure (Mandatory)

The `gencraft-crewai-workflows` repository **MUST** adhere to the following internal directory and file structure. This structure is designed for clarity, modularity, and to support automated tooling (e.g., CI/CD, documentation generation).

gencraft-crewai-workflows/
│
├── .github/                    # GitHub specific files
│   ├── ISSUE_TEMPLATE/         # Templates for GitHub Issues specific to this repo
│   │   ├── bug_report.md
│   │   └── crew_enhancement_request.md
│   ├── PULL_REQUEST_TEMPLATE.md # Template for Pull Requests to this repo
│   └── WORKFLOWS/              # GitHub Actions CI/CD workflows
│       └── python-ci.yml       # Workflow for Python linting, code formatting, automated testing (pytest)
│
├── crews/                      # Root directory for all individual Crew definitions
│   │
│   ├── [crew_id_lowercase_underscores]/  # Directory for a specific Crew, named after its Crew ID from Studio-Crews-Overview.md
│   │   │                                   # Example: crews/crew_kb_ingest_001/
│   │   ├── init.py         # Makes the directory a Python package
│   │   ├── main.py             # Main Python script to define the Crew, its Agents, Tasks, and Process.
│   │   │                       # This script MUST include a runnable example or entry point for local testing/execution.
│   │   ├── agents.py           # Python script defining the specialized AI Agents (Gems) configured for this Crew's context.
│   │   │                       # Agent definitions should leverage base prompts from Gem Blueprints where applicable,
│   │   │                       # and clearly specify assigned Tools.
│   │   ├── tasks.py            # Python script defining the CrewAI Tasks assigned to the Agents in this Crew.
│   │   │                       # Tasks should be granular and well-described.
│   │   ├── tools/              # OPTIONAL: Directory for any small, custom Python helper functions or classes
│   │   │   │                   # developed exclusively for this Crew's internal logic and not intended for studio-wide use.
│   │   │   └── init.py     # These MUST NOT duplicate functionality of standard Gencraft Gem Tools without explicit
│   │   │                       # documented approval from the AIE Team Lead.
│   │   ├── config/             # Directory for configuration files specific to this Crew.
│   │   │   └── [crew_name]config.yaml # Example: YAML or JSON for agent prompts, parameters, LLM settings, API endpoints.
│   │   │                           # Secrets MUST NOT be stored here; use references to the secrets management system.
│   │   ├── tests/              # Directory for all automated tests related to this Crew.
│   │   │   ├── init.py
│   │   │   └── test[crew_name]_workflow.py # Comprehensive unit tests for agents/tasks, and integration tests
│   │   │                                    # for the full Crew workflow using mock data.
│   │   └── README.md           # MANDATORY: Detailed documentation for this specific Crew (See Section 5 of this standard).
│   │
│   └── ...                     # Other Crew directories, each adhering to this standardized internal structure.
│
├── shared/                     # OPTIONAL: Directory for shared Python utilities, base classes, or common components
│   │                           # that are demonstrably reused by multiple Crews within this repository.
│   ├── init.py
│   ├── base_crew_agents.py     # Example: Potential base classes for Gencraft Agents used in Crews, promoting consistency in abilities or setup.
│   ├── common_crew_utils.py    # Example: Common utility functions (e.g., for standardized logging, error handling, data parsing specific to Crews).
│   └── shared_crew_tools/      # Example: Shared small Python helper tools or tool wrappers used by multiple Crews,
│       └── init.py         # if they do not warrant full Gencraft Gem Tool status and dedicated documentation in the Tooling Hub.
│
├── docs/                       # General documentation pertaining to the development, contribution, and governance of this repository.
│   └── DEVELOPMENT_GUIDE.md    # MANDATORY: Detailed guidelines for Crew development, testing, documentation, and contribution processes (See Section 6).
│
├── .gitignore                  # Standard Python .gitignore, ensuring virtual environments, IDE configs, .env files, etc., are excluded.
├── LICENSE                     # Gencraft's chosen license for the code in this repository (To be determined by GCT-LEG-LCOUN-001 Henri).
├── poetry.lock                 # (If Poetry is used for dependency management, which is recommended).
├── pyproject.toml              # (If Poetry or PEP 621 compliant tools are used for project configuration and dependency management).
│                               # Alternatively, a requirements.txt can be used if pip is the standard.
└── README.md                   # MANDATORY: Main README for this repository, providing an overview and quick start (See Section 4).

## 4. Main `README.md` Content (Root of `gencraft-crewai-workflows`)

The main `README.md` for the `gencraft-crewai-workflows` repository is the primary entry point for anyone interacting with this codebase. It **MUST** include:

- **Purpose of the Repository:** A clear explanation of its role as the SSoT for Gencraft Crew definitions and its importance to studio automation.
- **Prerequisites for Development & Execution:**
  - Python version (e.g., specify 3.10+).
  - CrewAI library version (pinned to a specific version tested by AIE Team).
  - Dependency management tool and usage (e.g., Poetry: `poetry install`; pip: `pip install -r requirements.txt`).
  - Instructions for setting up the development environment, including any necessary environment variables (e.g., for accessing Gencraft Gem `Tools` or MCP Servers if Crews interact with them locally – referencing `.env.example` if provided).
- **Repository Structure Overview:** A brief explanation of the directory structure defined in Section 3 of this standard, guiding users to find specific Crews or shared components.
- **How to Contribute to this Repository:**
  - A direct link to `docs/DEVELOPMENT_GUIDE.md` for comprehensive standards on coding, testing, documentation, etc.
  - A summary of Gencraft's standard PR process (based on Protocol S1), including code review requirements (e.g., mandatory peer review by AIE Team members, final approval by AIE Team Lead for merges to `main`/`develop` branch).
  - Process for proposing new Crews or significant modifications (via `type:crew-proposal` or `type:crew-enhancement-request` Issues in `gencraft-aie-backlog`).
- **Dependency Management:** Detailed instructions on using the chosen dependency manager (e.g., `poetry add [package]`, `poetry lock`, `poetry export > requirements.txt` if needed for deployment). How to manage dependencies for the shared environment and potentially for individual Crews if they have unique needs.
- **Local Execution & Testing Guidelines:**
  - General instructions on how a developer can execute a specific Crew definition locally for testing and debugging (e.g., "Navigate to the Crew's directory: `cd crews/[crew_id]/`. Each Crew's `main.py` should provide a runnable example or a command-line interface for local execution. Refer to the Crew's specific `README.md` for detailed run instructions.").
  - Command to run all tests in the repository (e.g., `poetry run pytest`).
- **Key Links & References:**
  - `gcs-core-governance/04-tooling-and-automation-hub/Studio-Crews-Overview.md` (for the functional catalog and high-level descriptions of all Crews).
  - `ai-enablement-team-charter.md` (as the AIE Team owns and governs this repository and the overall Crew strategy).
  - Official CrewAI Documentation (`https://docs.crewai.com/`).
  - `ai-tool-development-standards.md` (as many principles apply to the development of custom tools or logic within Crews).

## 5. Individual Crew `README.md` Standard (Located at `crews/[crew_id]/README.md`)

Each individual Crew directory (`crews/[crew_id]/`) **MUST** contain its own `README.md` file. This document is the SSoT for that specific Crew's functional details, operational guide, and technical specifics. It **MUST** include at least the following sections:

- **Crew ID & Descriptive Name:** (Must match the entry in `Studio-Crews-Overview.md`).
- **Version:** (Semantic Version of this Crew's definition, e.g., `1.0.0`).
- **Last Updated:** `YYYY-MM-DD`.
- **Crew Owner/Primary Maintainer(s):** (e.g., AIE Team, or specific GemID if primary maintenance is delegated).
- **Mission & Purpose:** A detailed explanation of what the Crew accomplishes, the specific studio problem it solves, or the process it automates/augments. Clearly state the value it brings.
- **Workflow Overview:**
  - A clear, high-level description of the Crew's operational process. This should detail the sequence of primary tasks and the roles and interactions of its constituent Agents.
  - A simple diagram (Mermaid preferred, embedded in the Markdown or linked as an image in `assets/`) is **STRONGLY RECOMMENDED** if the workflow involves more than 2-3 steps or multiple agents with complex interactions.
- **Constituent Agents & Their Roles:** List each Agent class defined in the Crew's `agents.py` script. For each Agent:
  - Its designated role within this Crew.
  - Its primary goal(s) within the Crew's specific context.
  - Key elements of its `backstory` or core prompts if they are highly specialized for this Crew and not fully encapsulated in a standard Gem Blueprint.
  - The Gencraft Gem `Tools` it is explicitly assigned and configured to use within this Crew.
- **Key Tasks:** Describe each significant Task defined in the Crew's `tasks.py` script:
  - Its specific, measurable goal.
  - The Agent(s) responsible for executing it.
  - Expected inputs for the task (data, context from previous tasks).
  - Expected outputs or deliverables from the task.
- **Configuration (`config/[crew_name]_config.yaml`):** Detailed explanation of all configurable parameters, environment variables needed for the Crew to run, prompt snippets, or LLM settings (model names, temperature, etc.) that are externalized in its configuration file. Explain how to set them for local execution versus potential production deployment.
- **Gencraft Gem `Tools` & MCP Servers Utilized:** Explicitly list all standard Gencraft Gem `Tools` (with versions) and MCP Servers (with API versions) that this Crew interacts with. Describe *why* each is used.
- **Expected Inputs to Initiate the Crew:** Define precisely what data, events, or parameters are required to trigger and successfully run the Crew's entire workflow. Include the schema or format if structured data is expected as input.
- **Expected Outputs/Deliverables & Side Effects:** Describe the tangible, verifiable results of the Crew's successful execution (e.g., a new Pull Request in a specific repository, a generated report in Markdown, updated data in a target system, an email notification). Clearly document any side effects or changes to other systems.
- **Local Execution & Testing Instructions:** Specific, step-by-step instructions on how to:
  - Set up the local environment for this Crew (if it has unique dependencies beyond the global repo setup).
  - Run the Crew's main workflow locally (e.g., `poetry run python crews/[crew_id]/main.py --input [example_input_file]`).
  - Execute its automated tests (e.g., `poetry run pytest crews/[crew_id]/tests/`).
- **Error Handling, Known Limitations & Troubleshooting:** Describe how the Crew is designed to handle common errors or exceptions. List any known limitations, edge cases not handled, or common issues encountered during testing and provide troubleshooting steps.
- **Performance Benchmarks (if applicable):** Document expected run times, resource consumption (e.g., LLM token usage if high), or processing capacity under typical load conditions, based on testing.
- **Changelog:** A brief, reverse-chronological list of significant changes, enhancements, and bug fixes by version/date for this specific Crew definition.

## 6. `docs/DEVELOPMENT_GUIDE.md` Content (Located at `gencraft-crewai-workflows/docs/DEVELOPMENT_GUIDE.md`)

This crucial document, to be created and maintained by the AIE Team Lead (`GCT-UTL-AIETL-001` Aura), **MUST** provide comprehensive guidelines for any Gem or human contributing to the `gencraft-crewai-workflows` repository. It **MUST** include detailed sections on:

- **Python Coding Standards for Crews:**
  - Strict adherence to PEP 8. Mandatory use of code formatters like Black.
  - Mandatory type hinting for all function and method signatures.
  - Docstring conventions (e.g., Google style or reStructuredText) for all modules, classes, functions, and methods.
  - Use of approved linters (e.g., Flake8, Ruff) integrated via pre-commit hooks is **MANDATORY**. Configuration for these tools will be in `pyproject.toml`.
- **CrewAI Design Principles Specific to Gencraft:**
  - **Agent Design:** Detailed guidelines on defining focused, expert Agents. How to effectively leverage core Gem Blueprints as a base for Agent `role`, `goal`, and `backstory`, then specialize context and instructions for the Crew's specific needs. Best practices for inter-agent communication, context sharing (e.g., using CrewAI's shared memory, task outputs).
  - **Task Design:** Creating clear, actionable, verifiable, and appropriately-scoped tasks. Managing task outputs as structured context for subsequent tasks. Designing for idempotence where appropriate.
  - **Process Definition:** Guidance on choosing appropriate CrewAI process types (sequential, hierarchical) based on workflow complexity and desired control flow. Strategies for robust error handling and retry mechanisms within processes.
  - **Modularity & Reusability:** Emphasize designing Agents and Tasks to be potentially reusable across different Crews or adaptable for similar workflows.
- **Utilizing Gencraft Gem `Tools` and MCP Servers within Crews:**
  - Standardized, secure, and efficient methods for Crews and their constituent Agents to invoke approved Gencraft Gem `Tools` (from `Gem-Tools-Overview.md`) and MCP Servers (from `MCP-Servers-Catalog.md`).
  - Strict adherence to `sec-001-secrets-management-standard.md` for any credentials the Crew or its Agents might need to securely access `Tools` or external services. Define how Crews obtain and use these secrets (e.g., via environment variables injected by a secure orchestrator, or by calling a specific `Tool` to fetch secrets).
  - Best practices for managing `Tool` versions and API compatibility within Crew definitions and their dependencies.
- **Configuration and Prompt Management for Crew Agents:**
  - Standardized approach for managing prompts and configurations: **MANDATORY** use of `config/[crew_name]_config.yaml` (or similar structured files like JSON) for externalizing agent-specific prompts, system messages, parameters, and LLM settings (e.g., model name, temperature, max tokens). This promotes maintainability and allows for easier tuning without code changes.
  - Techniques for constructing effective prompts that combine base Gem Blueprint directives with Crew-specific context loaded from these configuration files. Reference the "Advanced Prompt Engineering Guide" from the KB.
- **Testing Requirements for Crews:**
  - **Mandatory Automated Tests:**
    - Unit tests for any custom logic in `agents.py`, `tasks.py`, or custom `tools/` within a Crew's directory.
    - Integration tests for critical sequences of Tasks, verifying data flow and inter-agent handoff.
    - End-to-end workflow tests for the entire Crew process using mock data and, where feasible, mocked responses from external Gencraft Gem `Tools` or MCP Servers to ensure test determinism and isolation.
  - **Testing Framework:** `pytest` is the standard testing framework for this repository.
  - **Test Coverage:** Aim for a high level of test coverage (e.g., >80%) for all new and modified Python code. This will be enforced via CI.
  - **Running Tests:** Clear instructions on how to execute all tests for an individual Crew and for the entire repository. Test execution **MUST** be part of the CI pipeline.
- **Documentation Standards for Crews:** Reinforce the mandatory sections and expected quality for individual Crew `README.md` files (as defined in Section 5 of this standard). Documentation **MUST** be kept up-to-date with code changes.
- **Pull Request (PR) and Code Review Process:**
  - All changes (new Crews, modifications to existing ones) **MUST** be submitted via PRs from feature branches to the designated integration branch (`main` or `develop` - strategy to be defined by AIE Team Lead).
  - PRs **MUST** link to a relevant GitHub Issue in `gencraft-aie-backlog` (e.g., `type:crew-development-task`, `type:crew-bug-fix`).
  - PR descriptions **MUST** follow the template defined in `.github/PULL_REQUEST_TEMPLATE.md`, clearly summarizing changes, how they were tested, and any potential impact.
  - Code reviews will be conducted by at least one other AIE Team member (or a designated peer with CrewAI expertise). Reviews **MUST** focus on code quality, adherence to all standards in this guide, test coverage, documentation accuracy, workflow logic, and security considerations. The AIE Team Lead (`GCT-UTL-AIETL-001` Aura) approves final merges.
- **Security Considerations for Crew Development:** Detailed guidelines on handling sensitive data that may be processed by a Crew, managing permissions if a Crew needs to interact with restricted resources (principle of least privilege for Crew execution roles), and ensuring all Crew actions and data handling align with Protocol S8 and directives from `GCT-MGT-SECOFF-001` (Cerberus).
- **Versioning Strategy for Individual Crews:** Each Crew defined in `crews/[crew_id]/` **MUST** declare its own Semantic Version in its `README.md` and potentially in a `__version__.py` file. This version is incremented according to SemVer rules based on changes to that specific Crew's logic, agents, or tasks. The `Studio-Crews-Overview.md` will track the "current operational version" of each Crew.
- **Logging and Traceability for Crews:** Define standard logging practices for Crews to ensure their actions are traceable and auditable. Logs should be structured and provide sufficient context for debugging and performance analysis by `GCT-QAS-GPQA-001` (Véra).

## 7. Governance and Maintenance

- The AIE Team Lead (`GCT-UTL-AIETL-001` Aura) is the primary Knowledge Guardian and maintainer for the `gencraft-crewai-workflows` repository, its main `README.md`, this `CREWAI_WORKFLOWS_REPOSITORY_STANDARD.md` document, and the critical `docs/DEVELOPMENT_GUIDE.md`.
- The AIE Team is responsible for the primary development, testing, documentation, and maintenance of common, studio-wide Crews listed in `Studio-Crews-Overview.md`.
- Proposals for new studio-wide Crews or significant changes to existing ones must be submitted as formal requests to the `gencraft-aie-backlog` repository and will be reviewed, prioritized, and approved by the AIE Team Lead in consultation with `GCT-MGT-PPM-001` (Antoine - Producer) and other relevant stakeholders (e.g., Department Leads, `GCT-PRG-SARCH-001` Isaac).
- Adherence to this standard is **MANDATORY** for all contributions to the `gencraft-crewai-workflows` repository. The CI pipeline should include checks for compliance where possible.

This standard ensures that Gencraft's CrewAI-based workflows are developed, managed, and evolved in a consistent, robust, secure, and maintainable manner, thereby maximizing their benefit to the studio's game development efforts and operational efficiency.

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
