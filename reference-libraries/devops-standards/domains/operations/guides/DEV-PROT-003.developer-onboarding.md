---
docId: DEV-PROT-003
title: Developer Onboarding
version: 1.1.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This document defines the current developer onboarding protocol for GenCr@ft Studio using the active gcd-onboarding-scripts entry points.
last_updated_date: '2026-06-01'
knowledgeGuardian:
- "Édouard (GCT-DVO-DVSST-001)"
metadata:
  lifecycle-stage: draft
  keywords:
  - developer-onboarding
  - gft
  - windows
  - linux
  - macos
  - wsl2
  - bash
  - scripts
  - development-environment
  scope: studio
  domain: devops
  doc-type: protocol
  intended-audience: [devops-team, all-engineers]
  security-classification: l2_confidential

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/domains/operations/guides/DEV-PROT-003.developer-onboarding.md
---

# Developer Onboarding

## 1. Purpose

This protocol defines the supported path for setting up a GenCr@ft Studio developer workstation. The active
onboarding automation lives in the `gcd-onboarding-scripts` repository and exposes two supported entry
points:

- `gcd-onboarding-scripts/gft-onboarding.sh` for Linux, macOS, and WSL2.
- `gcd-onboarding-scripts/onboarding-win.ps1` for Windows bootstrap before handing off to WSL2.

The scripts consume the role/tooling matrix from
`gcs-core-governance/foundations/governance/GOV-GUIDE-010.role-tooling--resource-matrix.md`.

## 2. Prerequisites

- Active GitHub account with access to the `GenCr-ft` organization.
- Internet access for package installation, repository cloning, and standards checkout.
- `sudo` access on Linux/macOS or Administrator rights on Windows.
- Git available locally, or permission for the onboarding script to install missing prerequisites.

## 3. Linux, macOS, and WSL2 Flow

Download and run the Bash orchestrator from `gcd-onboarding-scripts`:

```bash
curl -L https://raw.githubusercontent.com/GenCr-ft/gcd-onboarding-scripts/main/gft-onboarding.sh -o gft-onboarding.sh
curl -L https://raw.githubusercontent.com/GenCr-ft/gcd-onboarding-scripts/main/gft-onboarding.sh.sha256 -o gft-onboarding.sh.sha256
sha256sum --check gft-onboarding.sh.sha256
chmod +x gft-onboarding.sh
./gft-onboarding.sh
```

The script installs required tools, checks out the standards repository, resolves role-specific tools and
repositories, configures shell environment variables, and deploys workspace helper files.

## 4. Windows Flow

Run the Windows bootstrapper from an Administrator PowerShell session:

```powershell
curl -L https://raw.githubusercontent.com/GenCr-ft/gcd-onboarding-scripts/main/onboarding-win.ps1 -o onboarding-win.ps1
curl -L https://raw.githubusercontent.com/GenCr-ft/gcd-onboarding-scripts/main/onboarding-win.ps1.sha256 -o onboarding-win.ps1.sha256
Get-FileHash onboarding-win.ps1 -Algorithm SHA256 | ForEach-Object { "$($_.Hash)  onboarding-win.ps1" } | Select-String -Pattern (Get-Content onboarding-win.ps1.sha256)

Set-ExecutionPolicy -Scope Process -ExecutionPolicy Bypass -Force
.\onboarding-win.ps1
```

The Windows bootstrapper enables WSL2, installs or selects an Ubuntu distribution, copies `.env` into the
WSL2 home directory when present, and launches `gft-onboarding.sh` inside WSL2.

## 5. Optional Configuration

Create a `.env` file next to the downloaded script to override defaults before execution:

```env
# GitHub organization to clone from.
GFT_ORG_NAME="GenCr-ft"

# Parent directory for side-by-side workspace repositories.
GFT_PROJECTS_HOME="$HOME/gft_studio"

# Optional non-interactive role selection for repeatable setup.
GFT_ROLE="devops-specialist"

# Optional local override for the Gem operations repository.
GFT_SSOT_GEMOP_PATH="$HOME/gft_studio/gcs-plt-gemop"
```

If no `.env` file is present, the onboarding flow uses defaults and prompts interactively where needed.

## 6. Post-Onboarding Verification

After the script completes:

- Restart terminal sessions so shell profile updates are loaded.
- Open the generated workspace in VS Code if the script did not launch it automatically.
- Run the validation script from the cloned `gcd-onboarding-scripts` repository:

```bash
cd "$GFT_PROJECTS_HOME/gcd-onboarding-scripts"
./validate-environment.sh
```

- For DevOps roles, run the additional DevOps validation:

```bash
./validate-devops-environment.sh
```

- Verify standards hooks in at least one cloned repository:

```bash
cd "$GFT_PROJECTS_HOME/gcs-core-governance"
pre-commit run --all-files
```

## 7. Troubleshooting

- **Checksum mismatch:** Delete the downloaded script and checksum file, then download both again from
  `GenCr-ft/gcd-onboarding-scripts`.
- **WSL2 launch fails:** Re-run `onboarding-win.ps1` after rebooting, then confirm `wsl -l -v` shows an
  installed Ubuntu distribution.
- **GitHub authentication fails:** Run `gh auth login` and confirm SSH keys are present in GitHub account
  settings.
- **Role matrix cannot be loaded:** Confirm the workstation can clone
  `https://github.com/GenCr-ft/gcs-core-governance.git`.
- **A required tool is missing after onboarding:** Run `./validate-environment.sh`, capture the output, and
  open an issue in `GenCr-ft/gcd-onboarding-scripts` with the logs.

## 8. Ownership

- Source scripts: `GenCr-ft/gcd-onboarding-scripts`.
- Role/tooling matrix: `GenCr-ft/gcs-core-governance`.
- Operational support: `#devops-support` or a GitHub issue in `gcd-onboarding-scripts`.
