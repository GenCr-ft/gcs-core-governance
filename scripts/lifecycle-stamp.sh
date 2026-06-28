#!/usr/bin/env bash
# lifecycle-stamp.sh — thin wrapper that resolves the workspace root
# and delegates to gcs-plt-gemop/hooks/lifecycle_stamp.py.
#
# Usage (from anywhere inside gcs-core-governance):
#   bash scripts/lifecycle-stamp.sh write <repo> <branch> <issue> <phase>
#
# The script determines the workspace collection root (the parent of the
# gcs-core-governance repo) via git rev-parse, so agents do not need to
# know or hard-code the absolute workspace path.

set -euo pipefail

# Resolve the repo root (gcs-core-governance/) regardless of cwd.
REPO_ROOT="$(git -C "$(dirname "$0")" rev-parse --show-toplevel)"
# The workspace collection root is one level up from the repo root.
WORKSPACE_ROOT="$(dirname "${REPO_ROOT}")"

STAMP_SCRIPT="${WORKSPACE_ROOT}/gcs-plt-gemop/hooks/lifecycle_stamp.py"

if [[ ! -f "${STAMP_SCRIPT}" ]]; then
  echo "ERROR: lifecycle_stamp.py not found at ${STAMP_SCRIPT}" >&2
  echo "Ensure gcs-plt-gemop is cloned as a sibling of gcs-core-governance." >&2
  exit 1
fi

# lifecycle_stamp.py is a library module (no CLI entrypoint).
# Parse the positional args and call the appropriate function directly.
CMD="${1:-}"
if [[ "${CMD}" == "write" ]]; then
  REPO="${2:?missing repo argument}"
  BRANCH="${3:?missing branch argument}"
  ISSUE="${4:?missing issue number argument}"
  PHASE="${5:?missing phase argument}"
  exec python3 -c "
import sys
sys.path.insert(0, '$(dirname "${STAMP_SCRIPT}")')
import lifecycle_stamp
lifecycle_stamp.write_stamp('${REPO}', '${BRANCH}', int('${ISSUE}'), '${PHASE}', ['manual'], 'manual')
print('Stamp written:', lifecycle_stamp.stamp_path('${REPO}', '${BRANCH}'))
"
elif [[ "${CMD}" == "read" ]]; then
  REPO="${2:?missing repo argument}"
  BRANCH="${3:?missing branch argument}"
  exec python3 -c "
import sys, json
sys.path.insert(0, '$(dirname "${STAMP_SCRIPT}")')
import lifecycle_stamp
result = lifecycle_stamp.read_stamp('${REPO}', '${BRANCH}')
if result is None:
    print('No stamp found.')
    sys.exit(1)
print(json.dumps(result, indent=2))
"
else
  echo "ERROR: unknown command '${CMD}'. Usage: bash scripts/lifecycle-stamp.sh write|read <repo> <branch> [<issue> <phase>]" >&2
  exit 1
fi
