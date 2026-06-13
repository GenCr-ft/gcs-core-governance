#!/usr/bin/env bash
# verify-compression.sh — AC acceptance script for WI-14 (gcs-core-governance#14)
# Usage:
#   --workspace --claude <path>   check CLAUDE.md: ≤200 nb lines, no absolute paths
#   --repo <agents-path>          check AGENTS.md: no absolute paths, warn if >150 nb lines
# Exit 0 = all checks PASS/WARN; exit 1 = at least one FAIL
set -euo pipefail

CLAUDE_MAX_NB=200
AGENTS_WARN_NB=150
ABS_PATH_PATTERN='/home/[a-zA-Z0-9_]+'

FAIL=0

emit() { printf '[%s] %s\n' "$1" "$2"; }

check_workspace() {
    local claude_path="$1"

    if [ ! -f "$claude_path" ]; then
        emit FAIL "workspace — CLAUDE.md not found: $claude_path"
        FAIL=$((FAIL+1)); return
    fi

    local nb
    nb=$(grep -cv '^\s*$' "$claude_path" || true)

    if [ "$nb" -le "$CLAUDE_MAX_NB" ]; then
        emit PASS "workspace — CLAUDE.md $nb/$CLAUDE_MAX_NB non-blank lines"
    else
        emit FAIL "workspace — CLAUDE.md $nb non-blank lines exceeds budget of $CLAUDE_MAX_NB"
        FAIL=$((FAIL+1))
    fi

    local abs_matches
    abs_matches=$(grep -oE "$ABS_PATH_PATTERN" "$claude_path" | sort -u || true)
    if [ -z "$abs_matches" ]; then
        emit PASS "workspace — CLAUDE.md no absolute paths"
    else
        emit FAIL "workspace — CLAUDE.md contains absolute paths: $(echo "$abs_matches" | tr '\n' ' ')"
        FAIL=$((FAIL+1))
    fi
}

check_repo() {
    local agents_path="$1"

    if [ ! -f "$agents_path" ]; then
        emit FAIL "repo — AGENTS.md not found: $agents_path"
        FAIL=$((FAIL+1)); return
    fi

    local abs_matches
    abs_matches=$(grep -oE "$ABS_PATH_PATTERN" "$agents_path" | sort -u || true)
    if [ -z "$abs_matches" ]; then
        emit PASS "repo — AGENTS.md no absolute paths"
    else
        emit FAIL "repo — AGENTS.md contains absolute paths: $(echo "$abs_matches" | tr '\n' ' ')"
        FAIL=$((FAIL+1))
    fi

    local nb
    nb=$(grep -cv '^\s*$' "$agents_path" || true)
    if [ "$nb" -le "$AGENTS_WARN_NB" ]; then
        emit PASS "repo — AGENTS.md $nb/$AGENTS_WARN_NB non-blank lines"
    else
        emit WARN "repo — AGENTS.md $nb non-blank lines exceeds soft limit of $AGENTS_WARN_NB"
    fi
}

# --- argument parsing ---
MODE=""
CLAUDE_PATH=""
AGENTS_PATH=""

while [[ $# -gt 0 ]]; do
    case "$1" in
        --workspace) MODE="workspace" ;;
        --claude)    CLAUDE_PATH="${2:?--claude requires a path argument}"; shift ;;
        --repo)      MODE="repo"; AGENTS_PATH="${2:?--repo requires a path argument}"; shift ;;
        *) echo "Unknown argument: $1" >&2; exit 2 ;;
    esac
    shift
done

case "$MODE" in
    workspace) check_workspace "$CLAUDE_PATH" ;;
    repo)      check_repo "$AGENTS_PATH" ;;
    *)
        echo "Usage: $0 --workspace --claude <path> | --repo <agents-path>" >&2
        exit 2
        ;;
esac

[ "$FAIL" -eq 0 ]
