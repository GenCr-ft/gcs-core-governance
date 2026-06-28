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

exec python3 "${STAMP_SCRIPT}" "$@"
