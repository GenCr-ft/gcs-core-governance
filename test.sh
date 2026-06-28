#!/usr/bin/env bash
# Governance repo validation suite — runs all parity scripts.
# Exit 0 = all checks pass. Exit 1 = at least one check failed.
set -uo pipefail

REPO_ROOT="$(cd "$(dirname "${BASH_SOURCE[0]}")" && pwd)"
EXIT=0

run_check() {
  local label="$1"
  shift
  if "$@" > /tmp/gov_check_out 2>&1; then
    echo "[PASS] $label"
  else
    echo "[FAIL] $label"
    sed 's/^/       /' /tmp/gov_check_out
    EXIT=1
  fi
}

run_check "agent-context parity"   python3 "${REPO_ROOT}/scripts/verify_agent_context_parity.py"
run_check "lifecycle gate parity"  python3 "${REPO_ROOT}/scripts/verify_lifecycle_gate_parity.py"
run_check "taxonomy parity"        python3 "${REPO_ROOT}/scripts/verify_taxonomy_parity.py"
run_check "AGENTS.md parity"       python3 "${REPO_ROOT}/scripts/verify_agents_md_parity.py"

exit $EXIT
