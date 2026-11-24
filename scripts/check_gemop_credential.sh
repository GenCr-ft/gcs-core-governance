#!/usr/bin/env bash
# Precondition for the gcs-plt-gemop checkout in agent-context-parity.yml.
# GenCr-ft/gcs-core-governance#325, design #386 v6, [IMPL] #387.
#
# Usage:
#   check_gemop_credential.sh                     probe with $CROSS_REPO_PAT (the workflow step)
#   check_gemop_credential.sh --classify C1 [C2] [HDR]   print the class for HTTP codes
#   check_gemop_credential.sh --self-test         run the classification table
#
# Exit: 0 ok, 1 any other class, 2 usage or temp-dir error.
#
# The token is read from the environment only and reaches curl on stdin (`-H @-`), never
# argv (Cerberus M1). The URLs are compile-time literals over https only (M2; probe 1 is a
# literal path under the ruled URL, recorded on #386). Response bodies are discarded unread,
# and only the HTTP code and class reach `::error::` (M3).
#
# NOT `set -e`: every outcome leaves through report(), which prints the diagnostic first.
set -u

CONTENTS_URL='https://api.github.com/repos/GenCr-ft/gcs-plt-gemop/contents/gems/index.yaml'
REPO_URL='https://api.github.com/repos/GenCr-ft/gcs-plt-gemop'

# has_header <file> <name>: the header is present, matched by name anchored at line start,
# case-insensitively, with CR stripped (HTTP/2 writes lowercase names and CRLF).
has_header() {
  [ -n "$1" ] && [ -r "$1" ] && tr -d '\r' < "$1" | grep -qiE "^$2:"
}

# rate_exhausted <file>: x-ratelimit-remaining is exactly 0.
rate_exhausted() {
  [ -n "$1" ] && [ -r "$1" ] && tr -d '\r' < "$1" | grep -qiE '^x-ratelimit-remaining:[[:space:]]*0[[:space:]]*$'
}

# classify <code1> [<code2>] [<probe-1 header file>]: one function for the live path and
# --classify (design #386 v6, round-2 N6). A curl failure arrives as code 000.
classify() {
  local c1="$1" c2="${2:-}" hdr="${3:-}"
  case "$c1" in
    200) echo ok ;;
    401) echo rejected ;;
    429) echo rate-limited ;;
    403)
      if rate_exhausted "$hdr" || has_header "$hdr" 'retry-after'; then
        echo rate-limited
      elif has_header "$hdr" 'x-github-sso'; then
        echo sso
      else
        echo forbidden
      fi
      ;;
    404)
      case "$c2" in
        404) echo no-grant ;;
        200) echo index-missing ;;
        *) echo api-fault ;;
      esac
      ;;
    *) echo api-fault ;;
  esac
}

remedy() {
  case "$1" in
    absent) echo "no CROSS_REPO_PAT reached this run. Fork and Dependabot pull requests never receive secrets (an accepted cost on this public repo); otherwise the gcs-core-governance repository secret CROSS_REPO_PAT is missing (#386 OQ-2 a1)." ;;
    rejected) echo "the token is dead. Re-set the gcs-core-governance repository secret CROSS_REPO_PAT per the GenCr-ft/gcs-project-management#528 runbook." ;;
    rate-limited) echo "rate limited (GenCr-ft/gcs-project-management#615). Wait and re-run; do not rotate." ;;
    sso) echo "the token needs SSO authorisation for GenCr-ft. Authorise it; do not rotate." ;;
    forbidden) echo "the token lacks a permission, probably Contents: read on gcs-plt-gemop. Fix the PAT's permissions; do not rotate." ;;
    no-grant) echo "the token cannot see gcs-plt-gemop. Add it to the PAT's repository grant; do not rotate." ;;
    index-missing) echo "gcs-plt-gemop has no gems/index.yaml. This is not a credential fault." ;;
    *) echo "network or GitHub API fault. This is not a credential fault; re-run." ;;
  esac
}

# report <class> <codes>: print the outcome; exit 0 only for ok.
report() {
  if [ "$1" = ok ]; then
    echo "CROSS_REPO_PAT: OK, gcs-plt-gemop/gems/index.yaml is readable"
    exit 0
  fi
  echo "::error title=CROSS_REPO_PAT $1::$2 — $(remedy "$1") This is a credential precondition of the parity job, not a parity finding."
  exit 1
}

# probe <url> <header file>: print the HTTP code, or 000 when curl itself fails.
probe() {
  local code rc
  code=$(curl --proto '=https' -sS --max-time 30 -o /dev/null -D "$2" -w '%{http_code}' \
    -H 'Accept: application/vnd.github+json' -H @- "$1" <<< "Authorization: Bearer ${CROSS_REPO_PAT}")
  rc=$?
  # A curl failure is code 000 (api-fault); keep curl's own exit status for the diagnostic.
  if [ "$rc" -ne 0 ]; then code="000 (curl exit $rc)"; fi
  printf '%s' "$code"
}

usage() {
  sed -n '2,10p' "$0" >&2
  exit 2
}

self_test() {
  local dir bad=0 got
  dir=$(mktemp -d) || exit 2
  # Header fixtures: HTTP/2 (lowercase names, CRLF) and HTTP/1.1 (mixed case).
  printf 'HTTP/2 403\r\nx-ratelimit-remaining: 0\r\n\r\n' > "$dir/h2-ratelimit0"
  printf 'HTTP/1.1 403 Forbidden\r\nRetry-After: 60\r\n\r\n' > "$dir/h1-retryafter"
  printf 'HTTP/2 403\r\nx-github-sso: required; url=https://example.invalid\r\n\r\n' > "$dir/h2-sso"
  printf 'HTTP/1.1 403 Forbidden\r\nX-RateLimit-Remaining: 4999\r\n\r\n' > "$dir/h1-plain"
  printf 'HTTP/2 403\r\nx-not-x-github-sso: 1\r\nx-other-ratelimit-remaining: 0\r\n\r\n' > "$dir/h2-unanchored"
  while read -r c1 c2 hdr want; do
    [ "$c2" = "-" ] && c2=""
    if [ "$hdr" = "-" ]; then hdr=""; else hdr="$dir/$hdr"; fi
    got=$(classify "$c1" "$c2" "$hdr")
    if [ "$got" = "$want" ]; then
      echo "ok   classify $c1 ${c2:--} ${hdr##*/}: $got"
    else
      echo "BAD  classify $c1 ${c2:--} ${hdr##*/}: $got (want $want)"
      bad=$((bad + 1))
    fi
  done <<'TABLE'
200 - - ok
401 - - rejected
429 - - rate-limited
403 - h2-ratelimit0 rate-limited
403 - h1-retryafter rate-limited
403 - h2-sso sso
403 - h1-plain forbidden
403 - h2-unanchored forbidden
404 404 - no-grant
404 200 - index-missing
404 500 - api-fault
000 - - api-fault
500 - - api-fault
TABLE
  # The absent path: an empty token must fail as `absent`, with no network call.
  got=$(CROSS_REPO_PAT='' bash "$0" 2>&1)
  if [ $? -eq 1 ] && printf '%s' "$got" | grep -q '^::error title=CROSS_REPO_PAT absent::'; then
    echo "ok   empty token: absent"
  else
    echo "BAD  empty token: not reported as absent"
    bad=$((bad + 1))
  fi
  rm -rf "$dir"
  if [ "$bad" -eq 0 ]; then echo "SELF-TEST: PASS"; return 0; fi
  echo "SELF-TEST: FAIL ($bad bad)"
  return 1
}

main() {
  local tmp hdr1 hdr2 c1 c2=""
  # Empty-token check first: the absent path touches no file and no network (round-3 D6).
  if [ -z "${CROSS_REPO_PAT:-}" ]; then report absent "no token"; fi
  tmp="${RUNNER_TEMP:-${TMPDIR:-/tmp}}"
  # A temp-dir failure exits 2 BEFORE the token is sent.
  hdr1=$(mktemp -p "$tmp" 2>/dev/null) || { echo "cannot create a temp file under '$tmp'; refusing to send the token" >&2; exit 2; }
  hdr2=$(mktemp -p "$tmp" 2>/dev/null) || { rm -f "$hdr1"; echo "cannot create a temp file under '$tmp'; refusing to send the token" >&2; exit 2; }
  trap 'rm -f "$hdr1" "$hdr2"' EXIT
  c1=$(probe "$CONTENTS_URL" "$hdr1")
  if [ "$c1" = 404 ]; then c2=$(probe "$REPO_URL" "$hdr2"); fi
  report "$(classify "$c1" "$c2" "$hdr1")" "HTTP ${c1}${c2:+ then HTTP $c2}"
}

case "${1:-}" in
  --self-test) [ "$#" -eq 1 ] || usage; self_test; exit $? ;;
  --classify)
    if [ "$#" -lt 2 ] || [ "$#" -gt 4 ]; then usage; fi
    shift
    classify "$@"
    exit 0
    ;;
  "") main ;;
  *) usage ;;
esac
