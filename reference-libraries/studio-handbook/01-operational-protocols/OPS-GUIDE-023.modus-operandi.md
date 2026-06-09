---
docId: OPS-GUIDE-023
title: Studio Modus Operandi (Hybrid Workflow)
version: 1.0.1
authors:
- Gemini CLI
creation_date: '2026-05-16'
last_updated_date: '2026-06-02'
language: en
metadata:
  scope: studio
  domain: governance
  doc-type: protocol
  lifecycle-stage: approved
  security-classification: l1-internal
  intended-audience:
  - all-contributors
  keywords:
  - modus-operandi
  - hybrid-workflow
  - collaboration
  - tdd
  - planning-with-files
knowledgeGuardian:
- Architecture Lead

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/01-operational-protocols/OPS-GUIDE-023.modus-operandi.md
---

# OPS-GUIDE-023: Studio Modus Operandi

## 1. Objective
This protocol defines the canonical workflow for all contributors—Human or AI—within the GenCr@ft Studio ecosystem. It ensures technical integrity, traceability, and seamless collaboration across ~30 repositories.

## 2. Core Principles
1. **SSoT or GTFO**: Every document must follow the SSoT standard (docId, Frontmatter, English-only). If it's not in the SSoT, it doesn't exist.
   *   *Note: Ephemeral planning files in `.planning/` are exempt from full SSoT metadata requirements to reduce overhead.*
2. **Atomic TDD**: Production code changes without a corresponding (and originally failing) test are prohibited. We aim for high coverage, but mandate 100% pass rate for all executed suites.
3. **Planning Persistence**: Context is volatile; the filesystem is permanent. Complex tasks must be documented in situ.

## 3. The Execution Loop (Plan-Act-Validate)

### 3.1. Phase: Research & Planning
For any task involving more than 3 tool calls or 2 files, the contributor MUST:
- Initialize planning files in `.planning/YYYY-MM-DD-<slug>/`.
- Use `task_plan.md` for phase tracking.
- Use `findings.md` for raw data and research results.
- Use `progress.md` for a chronological session log.

### 3.2. Phase: Implementation (TDD)
- **Act 1: Red**: Write a test that fails.
- **Act 2: Green**: Write the minimal code to pass the test.
- **Act 3: Refactor**: Clean the code while maintaining green status.

### 3.3. Phase: Validation
- Run `pre-commit run --all-files` to ensure SSoT compliance.
- Run repo-local `./test.sh`.
- Run root `./test-all.sh` if cross-repo dependencies exist.

## 4. Collaboration & Handoffs

### 4.1. Issues & PRs
- Every change MUST reference a GitHub Issue.
- PRs must use Conventional Commits (e.g., `feat(auth): ...`).

### 4.2. Human-Agent Protocol
- **Humans** provide high-level intent and approve critical plans.
- **Agents** execute the technical "ironification" and SSoT remediation.
- Gaps in requirements found by Agents must be immediately captured as GitHub Issues with the `type:requirement-gap` label.

## 5. Tooling Mandates
- **Onboarding**: All contributors must use `gft-onboarding.sh` (Linux/macOS) or `onboarding-win.ps1` (Windows) to set up their environment.
- **Verification**: `gft doctor` is the authoritative health check. It must pass 100% before starting work.
- **Freshness**: Use the `check-freshness.sh` script to ensure documentation is not stale.

### 5.1 Documentation Freshness Script
```bash
#!/usr/bin/env bash
# check-freshness.sh - Detects documents that haven't been updated recently.
set -euo pipefail

MAX_DAYS_STALE=30
CURRENT_SECS=$(date +%s)

find . -name "*.md" -not -path "*/.*" | while read -r doc; do
    # Extract date using more robust sed
    LAST_UPDATED=$(grep "last_updated_date:" "$doc" | head -n 1 | sed 's/last_updated_date: //;s/["'\'']//g;s/ //g')

    if [[ -n "$LAST_UPDATED" ]]; then
        # Try GNU date then BSD date
        DOC_SECS=$(date -d "$LAST_UPDATED" +%s 2>/dev/null || date -jf "%Y-%m-%d" "$LAST_UPDATED" +%s 2>/dev/null || echo "")

        if [[ -n "$DOC_SECS" ]]; then
            DIFF_DAYS=$(( (CURRENT_SECS - DOC_SECS) / 86400 ))
            if [ "$DIFF_DAYS" -gt "$MAX_DAYS_STALE" ]; then
                echo "[WARN] $doc is stale ($DIFF_DAYS days old). Review and update."
            fi
        fi
    fi
done
```
