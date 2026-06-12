#!/usr/bin/env bash
# Tests for tools/verify-compression.sh
# Run: bash tools/tests/test_verify_compression.sh
set -euo pipefail

SCRIPT="$(cd "$(dirname "$0")/.." && pwd)/verify-compression.sh"
PASS=0; FAIL=0

assert_exit() {
    local desc="$1" expected="$2"
    shift 2
    local actual
    "$@" > /dev/null 2>&1 && actual=0 || actual=$?
    if [ "$actual" -eq "$expected" ]; then
        echo "  PASS: $desc"
        PASS=$((PASS+1))
    else
        echo "  FAIL: $desc — expected exit $expected, got $actual"
        FAIL=$((FAIL+1))
    fi
}

assert_output_contains() {
    local desc="$1" pattern="$2"
    shift 2
    local out
    out=$("$@" 2>&1 || true)
    if echo "$out" | grep -qE "$pattern"; then
        echo "  PASS: $desc"
        PASS=$((PASS+1))
    else
        echo "  FAIL: $desc — expected pattern '$pattern' in output"
        echo "        got: $out"
        FAIL=$((FAIL+1))
    fi
}

# --- fixtures ---
TMPDIR_FIXTURES=$(mktemp -d)
trap 'rm -rf "$TMPDIR_FIXTURES"' EXIT

# compliant CLAUDE.md: 10 non-blank lines, no absolute paths
COMPLIANT_CLAUDE="$TMPDIR_FIXTURES/compliant_claude.md"
printf '%s\n' \
    "# CLAUDE.md" "" \
    "## Section One" "Line one." "Line two." "" \
    "## Section Two" "Line three." "Line four." "" \
    "## Section Three" "Line five." "Line six." > "$COMPLIANT_CLAUDE"

# over-budget CLAUDE.md: 210 non-blank lines
OVERBUDGET_CLAUDE="$TMPDIR_FIXTURES/overbudget_claude.md"
{ printf '# CLAUDE.md\n'; for i in $(seq 1 210); do printf 'Line %d\n' "$i"; done; } > "$OVERBUDGET_CLAUDE"

# CLAUDE.md with absolute path
ABSPATH_CLAUDE="$TMPDIR_FIXTURES/abspath_claude.md"
printf '# CLAUDE.md\nSee /home/lgan/hxgn/dev/workspace for details.\n' > "$ABSPATH_CLAUDE"

# compliant AGENTS.md: 10 non-blank lines, no absolute paths
COMPLIANT_AGENTS="$TMPDIR_FIXTURES/compliant_agents.md"
printf '# AGENTS.md\n\n## Overview\nThis repo does X.\n\n## Permissions\n✅ Always Do\n- Edit files.\n⚠️ Ask First\n- Destructive ops.\n' > "$COMPLIANT_AGENTS"

# AGENTS.md with absolute path
ABSPATH_AGENTS="$TMPDIR_FIXTURES/abspath_agents.md"
printf '# AGENTS.md\nBinary at /home/lgan/tools/bin.\n' > "$ABSPATH_AGENTS"

# over-budget AGENTS.md: 160 non-blank lines (warn only)
OVERWARN_AGENTS="$TMPDIR_FIXTURES/overwarn_agents.md"
{ printf '# AGENTS.md\n'; for i in $(seq 1 160); do printf 'Line %d\n' "$i"; done; } > "$OVERWARN_AGENTS"

# --- workspace flag tests ---
echo "=== --workspace tests ==="

assert_exit "compliant CLAUDE.md exits 0" 0 \
    "$SCRIPT" --workspace --claude "$COMPLIANT_CLAUDE"

assert_exit "over-budget CLAUDE.md exits 1" 1 \
    "$SCRIPT" --workspace --claude "$OVERBUDGET_CLAUDE"

assert_output_contains "over-budget emits FAIL line" "FAIL" \
    "$SCRIPT" --workspace --claude "$OVERBUDGET_CLAUDE"

assert_exit "CLAUDE.md with absolute path exits 1" 1 \
    "$SCRIPT" --workspace --claude "$ABSPATH_CLAUDE"

assert_output_contains "absolute path emits FAIL with path pattern" "FAIL.*absolute" \
    "$SCRIPT" --workspace --claude "$ABSPATH_CLAUDE"

# --- repo flag tests ---
echo "=== --repo tests ==="

assert_exit "compliant AGENTS.md exits 0" 0 \
    "$SCRIPT" --repo "$COMPLIANT_AGENTS"

assert_exit "AGENTS.md with absolute path exits 1" 1 \
    "$SCRIPT" --repo "$ABSPATH_AGENTS"

assert_output_contains "AGENTS.md absolute path emits FAIL" "FAIL" \
    "$SCRIPT" --repo "$ABSPATH_AGENTS"

assert_exit "over-budget AGENTS.md still exits 0 (warn only)" 0 \
    "$SCRIPT" --repo "$OVERWARN_AGENTS"

assert_output_contains "over-budget AGENTS.md emits WARN" "WARN" \
    "$SCRIPT" --repo "$OVERWARN_AGENTS"

# --- summary ---
echo ""
echo "Results: $PASS passed, $FAIL failed"
[ "$FAIL" -eq 0 ] && exit 0 || exit 1
