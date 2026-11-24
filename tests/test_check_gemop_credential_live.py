"""WI-325: the credential probe's live path, driven through a stub curl (PR #389 review).

The stub stands in for curl on PATH. Each call takes the next canned (code, header block,
exit status) from a queue. It records its argv, and whether an Authorization header came in
on stdin, so the tests can assert the token never reaches argv (Cerberus M1).
"""

import os
import subprocess
from pathlib import Path

import pytest

ROOT = Path(__file__).resolve().parent.parent
PROBE = ROOT / "scripts" / "check_gemop_credential.sh"
TOKEN = "wi325-live-test-marker-token-0123456789"

STUB = r"""#!/usr/bin/env bash
# Stub curl for tests: pops one "code|headers|rc" entry per call from $STUB_QUEUE.
printf '%s\n' "$@" >> "$STUB_DIR/argv.log"
grep -c '^Authorization: Bearer ' >> "$STUB_DIR/stdin-auth.log"
n=$(( $(cat "$STUB_DIR/calls" 2>/dev/null || echo 0) + 1 )); echo "$n" > "$STUB_DIR/calls"
entry=$(sed -n "${n}p" "$STUB_DIR/queue")
code=${entry%%|*}; rest=${entry#*|}; hdr=${rest%%|*}; rc=${rest##*|}
out=""; prev=""
for a in "$@"; do [ "$prev" = "-D" ] && out="$a"; prev="$a"; done
[ -n "$out" ] && printf '%b' "$hdr" > "$out"
[ "$rc" != 0 ] && exit "$rc"
printf '%s' "$code"
"""


@pytest.fixture
def stub(tmp_path):
    bindir = tmp_path / "bin"
    bindir.mkdir()
    curl = bindir / "curl"
    curl.write_text(STUB)
    curl.chmod(0o755)
    temp = tmp_path / "tmp"
    temp.mkdir()

    def run(queue, temp_dir=temp):
        (tmp_path / "queue").write_text("".join(f"{q}\n" for q in queue))
        for name in ("argv.log", "stdin-auth.log", "calls"):
            (tmp_path / name).unlink(missing_ok=True)
        env = {k: v for k, v in os.environ.items() if k not in ("RUNNER_TEMP",)}
        env.update(
            PATH=f"{bindir}:{env['PATH']}",
            STUB_DIR=str(tmp_path),
            CROSS_REPO_PAT=TOKEN,
            TMPDIR=str(temp_dir),
        )
        result = subprocess.run(
            ["bash", str(PROBE)], capture_output=True, text=True, env=env, check=False
        )
        argv = (
            (tmp_path / "argv.log").read_text()
            if (tmp_path / "argv.log").exists()
            else ""
        )
        auth_log = tmp_path / "stdin-auth.log"
        auth = auth_log.read_text().split() if auth_log.exists() else []
        calls = (
            int((tmp_path / "calls").read_text())
            if (tmp_path / "calls").exists()
            else 0
        )
        return result, argv, auth, calls, sorted(os.listdir(temp_dir))

    return run


@pytest.mark.parametrize(
    "queue, rc, marker, calls",
    [
        (["200||0"], 0, "CROSS_REPO_PAT: OK", 1),
        (["401||0"], 1, "::error title=CROSS_REPO_PAT rejected::HTTP 401", 1),
        (
            ["404||0", "404||0"],
            1,
            "::error title=CROSS_REPO_PAT no-grant::HTTP 404 then HTTP 404",
            2,
        ),
        (
            ["404||0", "200||0"],
            1,
            "::error title=CROSS_REPO_PAT index-missing::HTTP 404 then HTTP 200",
            2,
        ),
        (
            [r"403|HTTP/2 403\r\nx-ratelimit-remaining: 0\r\n\r\n|0"],
            1,
            "::error title=CROSS_REPO_PAT rate-limited::HTTP 403",
            1,
        ),
        (
            ["000||6"],
            1,
            "::error title=CROSS_REPO_PAT api-fault::HTTP 000 (curl exit 6)",
            1,
        ),
    ],
)
def test_live_probe_classifies_and_never_puts_the_token_in_argv(
    stub, queue, rc, marker, calls
):
    result, argv, auth, n, left = stub(queue)
    assert result.returncode == rc, result.stdout + result.stderr
    assert result.stdout.startswith(marker), result.stdout
    assert n == calls
    assert TOKEN not in argv  # M1: the token never reaches curl's argv
    assert auth == ["1"] * calls  # ... it arrives on stdin, once per call
    assert TOKEN not in result.stdout + result.stderr
    assert left == []  # header temp files are removed by the EXIT trap


def test_unwritable_temp_dir_exits_2_before_any_curl_call(stub, tmp_path):
    locked = tmp_path / "locked"
    locked.mkdir()
    locked.chmod(0o500)
    try:
        if os.access(locked, os.W_OK):
            pytest.skip("running as a user that can write to a 0500 directory (root)")
        result, _argv, _auth, n, _left = stub(["200||0"], temp_dir=locked)
    finally:
        locked.chmod(0o700)
    assert result.returncode == 2, result.stdout + result.stderr
    assert n == 0  # refused before the token is sent
