---
docId: GOV-PLAN-308
title: "[CODE] Update canonical pre-commit configuration for graceful gft verification"
issue-id: "GenCr-ft/gcs-core-governance#308"
created: 2026-06-11
status: approved
---

# [CODE] Task Plan — Update canonical pre-commit configuration (#308)

## Goal

Update canonical `.pre-commit-config.yaml` to fail gracefully if `gft` is missing, printing clear onboarding instructions.

## Files changed

- `.pre-commit-config.yaml` — Refactor SSoT custom hooks block
