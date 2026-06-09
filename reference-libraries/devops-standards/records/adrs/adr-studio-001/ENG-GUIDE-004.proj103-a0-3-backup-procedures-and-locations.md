---
docId: ENG-GUIDE-004
title: Proj103 A0 3 Backup Procedures And Locations
version: 1.0.0
authors:
- Édouard (GCT-DVO-DVSST-001)
reviewers:
- Architecture Lead
creation_date: '2025-05-25'
language: en
summary: This document outlines the procedures for backing up critical GenCr@ft GitHub
  organization configurations and repository data before PROJ-103 Phase 1. The backup
  utilizes `gh` (GitHub CLI) to clone repositories and extract metadata, with a local
  hard drive backup managed by Lug.
last_updated_date: '2026-05-20'
metadata:
  lifecycle-stage: draft
  keywords:
  - technical-writing
  - github-backup
  - projek103
  - backup-procedures
  - data-recovery
  - git
  - cli
  - organization-settings
  scope: studio
  domain: devops
  doc-type: protocol
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
knowledgeGuardian:
- "\xC9douard (GCT-DVO-DVSST-001)"

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/records/adrs/adr-studio-001/ENG-GUIDE-004.proj103-a0-3-backup-procedures-and-locations.md
---
## 1. Purpose

This document outlines the procedures for backing up critical GenCr@ft GitHub organization configurations
and repository data before the execution of PROJ-103 Phase 1 (GitHub Structure Implementation). This is a
critical risk mitigation step, now leveraging `gh` (GitHub CLI) for comprehensive data extraction.

## 2. Scope of Backup

The following GitHub entities will be backed up:

- **Organization Settings (exported as JSON via `gh api`):**
  - List of organization members and their roles (Note: `gh` provides member list; roles might need
    specific queries or be part of organization audit logs).
  - List of teams, their members, and repository permissions per team.
  - General organization settings where accessible via API.
  - Organization-level webhooks.
- **Repository Data (for all repositories):**
  - **Git Repository:** Full mirror clone including all branches and tags (`gh repo clone --mirror`).
  - **Wikis:** Full mirror clone of the wiki repository (`gh repo clone ORG/REPO.wiki --mirror`).
  - **Issues & Comments:** Exported as JSON objects via `gh api`.
  - **Pull Requests & Comments/Reviews:** Exported as JSON objects via `gh api`.
  - **Milestones:** Exported as JSON objects via `gh api`.
  - **Labels:** Exported as JSON objects via `gh api`.
  - **Repository Settings:** General settings, collaborators, topics, etc., exported as JSON via `gh api`.
  - **Branch Protection Rules:** Exported as JSON objects via `gh api` for each protected branch.
  - **Repository Webhooks:** Exported as JSON objects via `gh api`.
  - **Releases & Assets:** Release metadata exported as JSON; release assets (binaries) downloaded.
- **Manual Backup (Screenshots/Notes):** For highly critical organization settings visible only in the UI
  and not easily extractable via API (e.g., SAML configuration details, Billing information summary).

## 3. Backup Tools and Scripts

- **Primary Tool:** `gh` (GitHub CLI - `cli/cli`)
  - `gh repo clone ORG/REPO --mirror`: For cloning main repositories and their wikis.
  - `gh api`: For all metadata extraction (issues, PRs, settings, teams, etc.). This will be driven by
    custom shell scripts.
- **Secondary Tool(s):**
  - `jq`: For processing JSON output from `gh api` if needed during scripting or verification.
  - Standard shell utilities (`bash`, `curl`, `tar`, `gzip`): For scripting, automation, and archiving.
- **Custom Scripts:** A collection of shell scripts will be developed by Gem-AA to automate:
  1. Listing all organization repositories.
     2.Iterating through repositories to perform mirror clones (code and wiki).
     3.Iterating through repositories to export all specified metadata items (issues, PRs, etc.) to
     structured JSON files.
     4.Exporting organization-level metadata (teams, members, org hooks).
     5.Downloading release assets.
     6.Organizing the backed-up data into a consistent directory structure.

**Example `gh api` calls to be scripted (non-exhaustive):**

- Get Repos: `gh repo list <ORG_NAME> --json name,owner --limit 2000 -q '.[] | .owner.login + "/" + .name'`
- Repo Settings: `gh api repos/<OWNER>/<REPO>`
- Issues: `gh api repos/<OWNER>/<REPO>/issues --state all --paginate`
- PRs: `gh api repos/<OWNER>/<REPO>/pulls --state all --paginate`
- PR Comments: `gh api repos/<OWNER>/<REPO>/pulls/<PR_NUM>/comments --paginate`
- PR Reviews: `gh api repos/<OWNER>/<REPO>/pulls/<PR_NUM>/reviews --paginate`
- Labels: `gh api repos/<OWNER>/<REPO>/labels --paginate`
- Milestones: `gh api repos/<OWNER>/<REPO>/milestones --state all --paginate`
- Releases: `gh api repos/<OWNER>/<REPO>/releases --paginate` (assets need separate download logic)
- Branch Protections: `gh api repos/<OWNER>/<REPO>/branches/<BRANCH>/protection`
- Teams: `gh api orgs/<ORG_NAME>/teams --paginate`
- Team Members: `gh api orgs/<ORG_NAME>/teams/<TEAM_SLUG>/members --paginate`
- Org Hooks: `gh api orgs/<ORG_NAME>/hooks --paginate`

## 4. Backup Location and Security

- **Storage Backend:** Lug's local hard drive.
- **Designated Path:** `/mnt/c/_DATAS` (Base path. A subdirectory like
  `GenCr@ft_GitHub_Backup_PROJ103_YYYYMMDD` will be created for each full backup run).
- **Security Considerations for Local Backup:**
  - **Responsibility:** The security and integrity of the backup on the local hard drive are under Lug's
    direct responsibility.
  - **Recommendations:** Encrypted local hard drive (BitLocker, FileVault, LUKS, VeraCrypt), physical
    security, optional multiple copies on separate local media, checksum verification (SHA256).
- **Data Transfer:** Local file copy operations from the machine executing the backup to Lug's local hard drive.

## 5. Backup Frequency and Retention

- **Frequency:** One full backup will be performed immediately before the start of PROJ-103 Phase 1.
- **Retention Policy:** Managed by Lug on the local hard drive. Recommendation: Retain at least one full,
  verified backup until PROJ-103 is fully validated and stable, plus one archive. Adherence to `../dr/
dr-001-backup-restore-strategy.md` principles for local archives is recommended.

## 6. Backup Execution Process

1. **Preparation:**
   - **Confirm Local Path:** Lug confirms the exact subdirectory within `/mnt/c/_DATAS` for this backup run (e.g., `/mnt/c/_DATAS/GenCr@ft_GitHub_Backup_PROJ103_20250522`).
   - **Environment Setup:** Ensure `gh` is installed, authenticated (`gh auth login` with sufficient scopes), and `jq` is available on the execution machine. Sufficient disk space on execution machine for temporary files and on `/mnt/c/_DATAS` for the final backup.
   - **PAT/Token:** `gh` will use its authenticated session. Ensure the token used for `gh auth login` has `repo`, `workflow`, `admin:org`, `read:user`, `project`, `read:org`, `admin:repo_hook`, `gist` scopes.
   - **Scripts:** Prepare and test the custom backup scripts (responsibility of Gem-AA). 2.**Pre-Backup Communication:** Announce a brief maintenance window or code freeze if deemed necessary, coordinated with the Communication Plan (`communication-pal.md`). Given the "now" directive, this step is expedited. 3.**Execution:**
   - Create the target backup subdirectory (e.g., `/mnt/c/_DATAS/GenCr@ft_GitHub_Backup_PROJ103_20250522/`).
   - Run the master backup script which will:
     - Fetch the list of all organization repositories.
     - For each repository:
       - Create a dedicated subdirectory within the backup target.
       - Execute `gh repo clone <ORG_NAME>/<REPO_NAME> --mirror` into `REPO_NAME.git`.
       - Execute `gh repo clone <ORG_NAME>/<REPO_NAME>.wiki --mirror` into `REPO_NAME.wiki.git` (if wiki exists).
       - Execute scripted `gh api` calls to download issues, PRs, labels, milestones, releases (and
         assets), settings, branch protections, hooks into respective JSON files within the
         repository's backup subdirectory.
     - Execute scripted `gh api` calls to download organization-level data (teams, org members, org
       hooks) into a dedicated "ORG_Backup" subdirectory.
   - Perform manual screenshots/notes for UI-only settings. 4.**Verification:**
   - Check script execution logs for any errors.
   - Verify that the target directory on `/mnt/c/_DATAS` contains the expected structure (git mirrors,
     JSON files, downloaded assets).
   - Perform spot checks: clone a mirrored repo to a new location and check its integrity; validate JSON
     file content for a few key items.
   - Generate and record checksums (SHA256) for key archive files or the entire backup directory if feasible. 5.**Post-Backup:**
   - Securely store any logs or reports (can be included with the backup data).
   - Confirm completion and successful storage to stakeholders (Lug).

## 7. Restoration Procedure (Principles)

This backup is primarily a disaster recovery measure for PROJ-103.

- **Priority:** Restore Git repository data (code), then critical metadata (issues, PRs).
- **Process Outline:**
  1. **Assess:** Determine what needs restoration. 2.**Retrieve:** Access data from Lug's local hard drive. 3.**Repository Code/Wiki Restoration:**
     - Create a new empty repository on GitHub.
     - Push the mirrored Git data (`git push --mirror NEW_REMOTE_URL`). 4.**Metadata Restoration:**
     - This is more complex and may require custom scripting using the GitHub API to re-create issues,
       PRs (preserving authorship and timestamps as much as possible is hard), labels, milestones from
       the backed-up JSON files. This is a best-effort process for metadata.
     - Some settings might need manual re-application via UI or `gh api` based on backed-up JSON. 5.**Teams/Permissions:** Re-establish via GitHub UI or, ideally, future IaC (Terraform/OpenTofu) as
       per adr-studio-001.md, using backed-up data as reference.

## 8. Test of Backup and Restoration (Summary)

- **Test Plan:** Prior to full execution, Gem-AA will:
  - Test backup scripts on a small subset of 2-3 non-critical repositories.
  - Verify data integrity for these test repos (clones and JSON metadata).
  - Simulate restoration steps for one test repository's code and a sample of its issues/PRs from JSON
    to assess feasibility and script requirements.
- **Conclusion (Anticipated):** The `gh`-based approach provides comprehensive data capture. Code
  restoration is straightforward. Metadata restoration requires significant scripting effort and is
  best-effort for fidelity. This procedure is deemed adequate for the PROJ-103 pre-migration backup given
  `gh`'s reliability.

## 9. Responsibilities

- **Development & Execution of Backup Scripts:** Gem-AA (DevOps Team Lead) and DevOps Crew.
- **Secure Storage of Local Backup:** Lug.
- **Approval of this Plan:** Lug (Supervisor).
- **Maintenance of Scripts:** DevOps Crew.

## 10. Next Steps (Pre-Phase 1)

1. **Script Development & Testing:** Gem-AA finalizes and tests the `gh`-based backup scripts. 2.**PAT/Token:** Ensure `gh auth login` uses a token with all necessary scopes. 3.**Confirmation of Local Path & Space:** Lug confirms the exact local hard drive path and sufficient space. 4.**Schedule Execution:** (Currently "now" as per Lug's directive, pending this document's approval).

## 11. Document Control

- **Version:** 1.2
- **Status:** Review
- **Last Updated:** 2025-05-22
- **Owner:** Gem-AA (DevOps Team Lead)
- **Review Cycle:** N/A (specific to PROJ-103 migration).

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
