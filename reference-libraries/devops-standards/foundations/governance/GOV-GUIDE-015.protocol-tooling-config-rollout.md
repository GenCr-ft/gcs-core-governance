---
docId: GOV-GUIDE-015
title: Protocol for Studio-Wide Tooling Configuration Rollout
version: 2.0.0
date: '2025-06-27'
authors:
- Camille (GCT-DVO-DVSAU-001)
knowledgeGuardian:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Antoine (GCT-MGT-PPM-001)
- Governance Crew
approvers:
- Édouard (GCT-DVO-DVSST-001)
metadata:
  scope: studio
  domain: governance
  doc-type: protocol
  keywords:
  - rollout
  - pre-commit
  - automation
  - tooling
  - governance
  - versioning
  - ci-cd
  lifecycle-stage: approved
  intended-audience:
  - devopscrew
  - knowledgeguardians
  - contributors
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/foundations/governance/GOV-GUIDE-015.protocol-tooling-config-rollout.md
---
# Protocol for Studio-Wide Tooling Configuration Rollout

## 1. Objective

This protocol defines the **automated process** for propagating updates of shared tooling configurations (e.g., `.pre-commit-config.yaml`) from their Single Source of Truth (SSoT) in the `gcs-core-governance` repository to all other relevant repositories within the studio.

Its purpose is to **prevent configuration drift** and ensure all projects benefit from the latest quality and security standards consistently and automatically.

## 2. Scope

This protocol applies to any modification of the following canonical configuration files located at the root of the `gcs-core-governance` repository:

- `.pre-commit-config.yaml`
- `.markdownlint.yaml`
- `commitlint.config.js`
- `.yamllint.yaml`

## 3. Workflow

The rollout process is now **fully automated** by a dedicated GitHub Action within this repository. The manual execution of the deployment script is deprecated and reserved for emergency use by the DevOps team only.

```mermaid
graph TD
    A[Start: Change Proposed<br><i>PR on gcs-core-governance</i>] --> B{Knowledge Guardian<br>Reviews & Approves};
    B --> C["<b>PR is Merged into 'main'</b><br>SSoT is officially updated."];
    C --> D["<b>AUTOMATED STEP</b><br>GitHub Action triggers on push to main."];
    D --> E{Action executes 'deploy_configs.py'<br>using the latest tools};
    E --> F{Automation creates<br>a fleet of PRs<br><i>(Each PR links to the source change)</i>};
    F --> G[Target Repo Owners<br>Review & Merge];
    G --> H[End: Studio is Synchronized];

    style D fill:#d1ecf1,stroke:#0c5460,stroke-width:2px
    style H fill:#d4edda,stroke:#155724
```

### 3.1. Step-by-Step Procedure

1. **Propose Change**: A **Contributor** creates a Pull Request on the `gcs-core-governance` repository to modify one of the canonical configuration files.

   - If the change depends on a new version of the `gcd-ops-scripts`, the rev in `.pre-commit-config.yaml` MUST point to a specific, immutable Git tag (e.g., `v2.6.0`), never to a branch.

2. **Handle Tooling Dependencies**:

   - If the proposed change requires a new version of the linter scripts from `gcd-ops-scripts` (e.g., to support a new hook), the `rev:` in `.pre-commit-config.yaml` **MUST** point to a specific, immutable, and **already existing** Git tag (e.g., `v3.1.0`).

   - It is the **Contributor's responsibility** to ensure that this version of the tools has been previously released and is available before submitting the PR.

3. **Approve & Merge**: The designated **Knowledge Guardian** reviews the changes. If they are approved, the PR is merged into the `main` branch. This merge is the **single action** that triggers the entire studio-wide rollout.

4. **Automated Rollout**:
    a.  The merge to `main` automatically triggers the `config-rollout.yml` GitHub Action.
    b.  The action executes the `deploy_configs.py` script, which clones every relevant repository and applies the configuration update.
    c.  The script automatically creates a new Pull Request on each repository. The body of this PR will contain a link back to the original PR on `gcs-core-governance` for full traceability.

5. **Finalize Deployment**: The owners of the target repositories are responsible for reviewing and merging these automated PRs in a timely manner to complete the synchronization.

## 4. Actors and Responsibilities

- **Contributor**: Responsible for proposing quality changes and ensuring any tooling dependencies (rev: tag) are met beforehand.

- **Knowledge Guardian**: Responsible for the quality and validity of the canonical configuration. Merging the PR is their explicit approval to launch the studio-wide deployment.

- **Automation** (`config-rollout.yml` **workflow**): Responsible for the execution of the deployment, ensuring consistency and eliminating manual error.
