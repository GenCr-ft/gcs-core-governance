---
docId: GOV-IMPL-325
title: WI-325 — implementation plan (agent-context parity job runs)
issue-id: GenCr-ft/gcs-core-governance#325
status: in_progress
---

# WI-325 implementation plan

- **Design:** [DESIGN] #386 v6, `status:approved` (setter `loigallain`, 2026-11-23T17:58:27Z).
- **Branch:** `fix/issue-325-parity-job-runs`.
- **Lane:**
  - `.github/workflows/agent-context-parity.yml`
  - `tests/check_parity_workflow_contract.py` (new)
  - `scripts/check_gemop_credential.sh` (new)
  - `CHANGELOG.md`
  - `.planning/`
- **Not touched:** the three `scripts/verify_*.py` files, and `test.sh` (PR #286 rewrites it; deferred as OQ-6).

## Files

| File | Change |
|---|---|
| `tests/check_parity_workflow_contract.py` | **New.** Stdlib plus PyYAML. Implements STEPS and the ids C0, C1, C2, C3, C5, C6, C7, C8, C11, C13 and C14, with the per-id FAIL/SKIP/PASS outcome and precedence. `--self-test` runs mutations with exact expected FAIL and SKIP sets, plus positive controls. Exit codes: 0 holds, 1 violated, 2 usage or parse error, including a `git ls-files` failure. |
| `scripts/check_gemop_credential.sh` | **New.** Runs the empty-token check first, then probe 1 (contents of `gems/index.yaml`), then probe 2 only after a 404. The header goes over stdin (`-H @-`), with `--proto '=https'`, and `-D` writes to a 0600 mktemp file. There is one `classify` function, behind `--classify` and `--self-test`. It has 9 classes, and only the code and class reach `::error::`. |
| `.github/workflows/agent-context-parity.yml` | **Rewritten** to the S1–S11 STEPS. Changes: `paths` gain 5 entries in both triggers, `workflow_dispatch` is added, `permissions: {contents: read}`, `persist-credentials: false` on both checkouts, and the PyYAML install is pinned to `PyYAML==6.0.3` (an exact release with a cp312 manylinux wheel; the newest, 6.0.4, was avoided as too fresh to verify). The dead post-checkout assert is removed and replaced by S7. |
| `CHANGELOG.md` | One `### Fixed` line under `[Unreleased]`, at most 200 characters. |

## TDD cycles (commit format `WI-325.N`)

1. **Cycle 1: the contract checker proves the current workflow non-compliant.**
   - Red: add the checker. Running it on the base workflow must give exactly FAIL {C0, C1, C3, C5, C11, C14} and SKIP {C7, C8, C13}. The exit-1 output is recorded verbatim in progress.md, and the commit message names that set.
   - Green: rewrite the workflow to STEPS. The checker exits 0, and `--self-test` exits 0.
2. **Cycle 2: the credential classifier maps every status class to its remedy.**
   - Red: add `scripts/check_gemop_credential.sh` with the `--self-test` table and a stub `classify` that returns `unknown`. `--self-test` exits 1.
   - Green: implement `classify`, the probes and the capture. `--self-test` exits 0. The local empty-token run gives `absent`, and an invalid-token run gives `rejected` 401.
3. **Cycle 3 (blue): tidy-up.** Comments that cite #386, C-id docstrings and the CHANGELOG line. No behaviour change. The checker, both self-tests, the `.yamllint` pass and `pre-commit run --from-ref origin/main --to-ref HEAD` all stay green.

Ordering: cycle 1's green needs `scripts/check_gemop_credential.sh` to exist, because C3 requires it to be a tracked file in `paths`. So cycle 2's red lands **before** cycle 1's green. The commit order is red-1, red-2, green-2, green-1, blue.

## Verification

- **Local:**
  - checker exit 0;
  - `--self-test` exit 0 for both files;
  - all three verifiers PASS under PyYAML 6.0.3 in a clean venv;
  - `yamllint -c .yamllint.yaml`;
  - pre-commit from-ref.
- **CI proof:**
  - *AC-3 rejected:* the PR's first run, before the SD's a1 action. S7 must give `rejected` (HTTP 401) and S8 to S11 must be skipped.
  - *AC-1:* after a1, a rerun with S7 to S11 `success`.
  - *AC-2:* five one-file scratch PRs with base = the fix branch.
  - *AC-4:* a scratch PR changing `gct-dvo-dtl-001-diane` to `gct-dvo-dtl-999-diane`, which must fail at S9.
  - Each PR run's per-step conclusions are tabulated, cancelled runs included.

## Risks

- PR #286 merges first: it changes the verifier logic, and the job then exercises it. Re-run, and report any new FAIL as #286's.
- PyYAML 6.0.3 has no transitive dependencies.
- Hosted-runner curl differences are covered by the HTTP/2 header fixtures.

## Rollback

Revert the PR. The job returns to its never-passing state, and nothing else depends on it.
