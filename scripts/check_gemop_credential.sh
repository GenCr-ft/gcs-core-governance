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
set -u

classify() {
  # RED STUB (WI-325.2): replaced at green.
  echo unknown
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
  echo "RED STUB (WI-325.2): live probe not implemented" >&2
  exit 2
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
