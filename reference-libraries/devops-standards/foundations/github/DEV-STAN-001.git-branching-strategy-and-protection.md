---
docId: DEV-STAN-001
title: Git Branching Strategy and Protection
version: 2.0.2
date: '2026-06-02'
authors:
- Lug (Studio Lead)
- Claude Sonnet 4.6 (AI)
knowledgeGuardian:
- Vector (GCT-DVO-DSSTR-001)
reviewers:
- Isaac (GCT-PRG-SARCH-001)
- Antoine (GCT-MGT-PPM-001)
- Forge (GCT-PRG-LDTL-001)
approvers:
- Governance Crew
relatedDocuments:
- gcs-core-governance/domains/tooling/standards/DEV-SPEC-012.conventional-commits-standard.md
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/foundations/github/DEV-STAN-001.git-branching-strategy-and-protection.md
metadata:
  lifecycle-stage: approved
  keywords:
  - git-branching
  - devops
  - standard
  - gencraft
  - github-flow
  - worktree
  - ai-commits
  scope: studio
  domain: devops
  doc-type: standard
  intended-audience:
  - contributors
  - ai-agents
  - governance-team
  - project-leads
  security-classification: l2_confidential
changelog:
  - version: 2.0.2
    date: '2026-06-02'
    summary: >
      Patch: add workspace exception clause to §5.3 Co-Authored-By mandate.
      Workspaces where AGENTS.md declares an administrative block on
      Co-Authored-By are exempt; the AGENTS.md entry takes precedence.
  - version: 2.0.1
    date: '2026-05-07'
    summary: >
      Patch: fix relatedDocuments (remove self-ref, correct DEV-SPEC-012 path).
      Add style/, build/, revert/ to §4.2 branch type table. Restructure §4.3
      and §5.2 examples to explicitly separate WI and non-WI cases. Fix §5.1
      doc reference to DEV-SPEC-012. Add §6.2 note on spec-ref PR titles.
      Fix §8 force-with-lease logging to say "PR comment" not "commit message".
  - version: 2.0.0
    date: '2026-05-07'
    summary: >
      Breaking change. Promotes GitHub Flow to Tier 1 (default for all repos).
      Renames prior Tier 1 Hybrid Flow to Tier 2 (opt-in, must be declared).
      Adds AI commit conventions (Co-Authored-By trailer), WI-X.Y branch and PR
      naming, one-PR-per-WI rule, worktree pattern for parallel work, and PR
      title format. Branch prefix vocabulary aligned with Conventional Commits
      type list. Removes develop/release/hotfix as default expectations.
  - version: 1.0.0
    date: '2025-06-13'
    summary: Initial standard. Defined Gencraft Hybrid Flow as default.
---

# Git Branching Strategy and Protection

## 1. Objective

This standard defines the mandatory Git branching strategy for all GenCr@ft repositories. It ensures a consistent, automatable workflow for code integration and delivery across Studio Meta-Project and Game Project repositories, understandable and enforceable by both human contributors and AI Gems.

**v2.0.0 change:** GitHub Flow is now the default (Tier 1). The Hybrid Flow (main + develop + release/\* + hotfix/\*) defined in v1.0.0 is available as opt-in Tier 2 for repositories that require it. Every repository not explicitly declared Tier 2 operates as Tier 1.

---

## 2. Scope

Applies to all Git repositories in the `GenCr-ft` GitHub organisation containing version-controlled artefacts: source code, IaC, as-code configurations, and documentation repositories.

---

## 3. Branching Tiers

### Tier 1 — GitHub Flow (Default)

**All repositories are Tier 1 unless explicitly declared otherwise in their README.**

Model: `main` + short-lived type branches. All work branches merge into `main` via Pull Request. No `develop` branch. No `release/*` branches.

- `main` is always deployable.
- Every branch is cut from `main` and merged back to `main`.
- Releases are tagged directly on `main` after merge.
- Hotfixes follow the same pattern as features: branch from `main`, PR to `main`, tag.

### Tier 2 — Gencraft Hybrid Flow (Opt-in)

For repositories with distinct release cycles requiring a stabilisation gate between feature integration and production (e.g., a game client with coordinated milestone releases).

**To operate as Tier 2:** declare `branching-tier: 2` in the repository `README.md` with a reference to the governance approval (ADR or governance ticket). Absent this declaration, the repo is Tier 1.

Tier 2 adds: `develop` as the integration target, `release/vX.Y.Z` stabilisation branches, `hotfix/vX.Y.Z-*` emergency patches. See Appendix A for the full Tier 2 workflow.

---

## 4. Branch Naming (Tier 1 Default)

Branch names use the **Conventional Commit type** as the prefix, followed by an optional WI reference and a kebab-case description.

### 4.1 Format

```
<type>/<wi-reference>-<kebab-case-description>
<type>/<kebab-case-description>          ← when no WI applies
```

### 4.2 Allowed Types

| Type | When to use |
|---|---|
| `feat/` | New feature or capability |
| `fix/` | Bug fix |
| `docs/` | Documentation only |
| `chore/` | Tooling, config, maintenance — no production code |
| `test/` | Adding or correcting tests |
| `refactor/` | Restructuring without behaviour change |
| `perf/` | Performance improvement |
| `ci/` | CI/CD workflow changes |
| `style/` | Formatting, whitespace — no logic change |
| `build/` | Build system or dependency changes |
| `revert/` | Reverting a previous commit |

### 4.3 WI Reference (Recommended)

When work corresponds to a tracked Work Item (`WI-X.Y`), include the reference immediately after the type prefix:

```
feat/wi-4.1-chunk-wire-format        ← WI-tracked work
fix/wi-5.2-voxel-transposition       ← WI-tracked work
```

When no WI applies, omit it — the type prefix alone is sufficient:

```
chore/3-file-paradigm-revamp         ← no WI, doc-ref slug used
docs/gam-spec-033-pcg-gameplay-goals ← no WI, spec reference used
```

### 4.4 Rules

- All lowercase. Kebab-case only. No underscores.
- Concise: prefer `feat/wi-4.3-jwt-validation` over `feat/wi-4.3-implement-jwt-validation-service-for-websocket`.
- Maximum 72 characters.

---

## 5. Commit Message Standard

All commits MUST follow the Conventional Commits specification as defined in `DEV-SPEC-012.conventional-commits-standard.md` and enforced by `commitlint`.

### 5.1 Format

```
<type>(<scope>): <subject>

[optional body]

[optional footer]
```

Header maximum 100 characters. Subject does not end with a period.

### 5.2 WI Reference in Subject

When work corresponds to a tracked Work Item, include the WI reference in the subject using an em dash:

```
feat(server): WI-4.3 — JwtValidationService (RS256 JWT validation)
fix(pcg): WI-5.2 — correct voxel index transposition in lib.rs
```

Format: `WI-X.Y — <description>` (em dash `—`, not hyphen `-`).

When no WI applies, omit the reference entirely:

```
chore(gemop): migrate 9 gems to 3-file schema (GCS-STD-003 v2.0.0)
docs(gdd): GAM-SPEC-033 — PCG gameplay goals contract
```

### 5.3 Co-Authored-By Trailer (AI Commits)

All commits produced with AI assistance (including commits authored by Claude Code or any AI Gem acting as the committing agent) MUST include a `Co-Authored-By` trailer identifying the AI model:

```
Co-Authored-By: Claude Sonnet 4.6 <noreply@anthropic.com>
```

Update the model name when the active model changes. This is a studio attribution requirement, not a technical enforcement; omitting it on a commit does not fail CI but is a standard violation.

> **Workspace exception:** This trailer is suspended in workspaces where `AGENTS.md` declares an administrative block on Co-Authored-By. The `AGENTS.md` entry takes precedence.

### 5.4 Allowed Commit Types

As defined in `commitlint.config.js`: `feat`, `fix`, `docs`, `style`, `refactor`, `perf`, `test`, `build`, `ci`, `chore`, `revert`.

---

## 6. Pull Requests

### 6.1 One PR per Work Item

Each Work Item produces exactly one PR. Multiple commits may be pushed to the same branch and PR. Do not combine unrelated WIs into one PR.

### 6.2 PR Title Format

```
type(scope): WI-X.Y — <short description>   ← WI-tracked work
type(scope): <short description>             ← no WI
```

Examples:
```
feat(server): WI-4.3 — JwtValidationService (RS256 JWT validation)
chore(gemop): migrate Wave 1 gems to 3-file persona schema
docs(gdd): GAM-SPEC-033 — update PCG gameplay goals contract
```

The third example uses a spec reference (`GAM-SPEC-033`) in place of a WI reference; this is acceptable when the work traces to a spec rather than a backlog WI.

Rules:
- Title follows Conventional Commits format.
- Include WI reference when the work is tracked in the backlog.
- Maximum 100 characters.
- No trailing period.

### 6.3 Linked Issue Requirement

Every PR MUST link to a GitHub Issue. Create the issue first if one does not exist. Link via the PR body using `Closes #NNN` or `Refs #NNN`.

### 6.4 Merge Strategy

- **Tier 1 (feature branches → `main`):** Squash and Merge is preferred to maintain a clean `main` history. The squashed commit message MUST be a well-formed Conventional Commit. Use merge commit only when preserving individual commit history has explicit value.
- **Tier 2 (see Appendix A):** merge strategies vary by target branch.

### 6.5 Review Comments

All review comments MUST be resolved before merge. After pushing fixes, reply to each thread citing the fixing commit SHA, then resolve the discussion. If the reviewer has not resolved their own thread, reply with the fix reference and resolve it as the author.

### 6.6 Branch Deletion

Feature branches MUST be deleted from the remote immediately after their PR is merged. Configure "Automatically delete head branches" in GitHub repository settings.

---

## 7. Parallel Work — Worktree Pattern

When two or more Work Items in the **same repository** must be developed concurrently, use `git worktree` to isolate each WI in its own directory. Do not develop multiple WIs on different branches in the same working tree.

```bash
# Add a worktree for WI-4.2 while WI-4.3 is in progress in the main tree
git worktree add /tmp/wi-4.2-worktree feat/wi-4.2-flat-terrain-generator
```

Each worktree operates independently: its own branch, its own working files, its own uncommitted changes. Changes in one worktree do not affect another.

Clean up after merge:
```bash
git worktree remove /tmp/wi-4.2-worktree
```

---

## 8. Destructive Operations — Safety Gates

The following operations require explicit confirmation from the Studio Lead or a human authorised to approve them before execution. An AI Gem MUST NOT perform these unilaterally:

| Operation | Gate |
|---|---|
| `git push --force` or `--force-with-lease` to `main` | Explicit human instruction in the current session |
| `git branch -D` (force-delete a branch with unmerged commits) | Explicit human instruction |
| `git reset --hard` on a shared branch | Explicit human instruction |
| `git push --force` to any branch with open PRs | Explicit human instruction |
| Closing or superseding a PR without merging | State intent and confirm before executing |

For `--force-with-lease` on **non-main** branches where the agent itself made all previous pushes (e.g., rebasing its own WI branch), no external confirmation is required — the agent may proceed and MUST log the operation in a PR comment.

---

## 9. Branch Protection Configuration

Managed as code via OpenTofu in `gencraft-iac`. The following rules apply to all Tier 1 repositories.

### 9.1 `main`

- Pull request required before merging: **enabled**.
- Minimum 1 approving review (human).
- Dismiss stale reviews on new push: **enabled**.
- Required status checks must pass before merge.
- Conversation resolution required before merge.
- Direct commits: **forbidden**.
- Force pushes: **disabled**.
- Deletions: **disabled**.

AI Gem approvals do not count towards the human approval requirement.

---

## 10. Tagging and Versioning

1. Tags are created on `main` on the merge commit that finalises a release.
2. Tag format: `vX.Y.Z` following Semantic Versioning 2.0.0.
3. Annotated tags preferred: `git tag -a vX.Y.Z -m "Release vX.Y.Z"`.
4. CI/CD triggers on tags matching `v*.*.*`.

---

## 11. Responsibilities

| Role | Responsibility |
|---|---|
| Vector (GCT-DVO-DSSTR-001) | Maintain and evolve this standard |
| Forge (GCT-PRG-LDTL-001) | Enforce within PRG team; approve PRs per §6.5 |
| Diane (GCT-DVO-DTL-001) | Implement branch protection rules via IaC |
| Pulse (GCT-DVO-DSAUT-001) | Automate branch deletion and CI enforcement |
| All contributors (Gems and humans) | Follow this standard on every branch, commit, and PR |

---

## 12. Exceptions

Exceptions require a GitHub Issue in `gcs-core-governance` documenting justification, scope, duration, risk, and mitigation. Approval required from Vector, Forge, Isaac, and the relevant Product Manager. Exceptions impacting multiple repos require a merged ADR.

---

## Appendix A — Tier 2 Hybrid Flow (Opt-in)

Repositories declared Tier 2 add the following to the Tier 1 rules:

**Additional perpetual branch:** `develop` — integration target for all feature/bugfix branches. Must always build, pass all tests, and be deployable to staging.

**Additional temporary branches:**
- `bugfix/<wi-reference>-<description>` — non-critical bugs fixed against `develop`
- `release/vX.Y.Z` — stabilisation branch cut from `develop` when feature-complete; merges to `main` and back to `develop`
- `hotfix/vX.Y.Z-<description>` — critical production fix branched from `main`; merges to `main`, `develop`, and any active `release/*`

**Merge strategies for Tier 2:**
- `feature/*` / `bugfix/*` → `develop`: Squash and Merge
- `release/*` → `main`: Merge Commit (`--no-ff`)
- `release/*` → `develop`: Merge Commit (`--no-ff`)
- `hotfix/*` → `main` and `develop`: Merge Commit (`--no-ff`)

**Branch protection additions:**
- `develop`: protected; minimum 1 approving review; direct commits forbidden.
- `release/v*`, `hotfix/v*`: protected; minimum 1 approving review from Release Manager or Tech Lead.
