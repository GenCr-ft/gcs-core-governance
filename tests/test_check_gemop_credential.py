"""WI-325: the gemop credential precondition classifies every status (design #386 v6)."""

import os
import subprocess
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
PROBE = ROOT / "scripts" / "check_gemop_credential.sh"


def run_probe(*args, token=None):
    env = {k: v for k, v in os.environ.items() if k != "CROSS_REPO_PAT"}
    if token is not None:
        env["CROSS_REPO_PAT"] = token
    return subprocess.run(
        ["bash", str(PROBE), *args],
        capture_output=True,
        text=True,
        cwd=ROOT,
        env=env,
        check=False,
    )


def test_classify_maps_401_to_rejected():
    assert run_probe("--classify", "401").stdout.strip() == "rejected"


def test_empty_token_fails_as_absent():
    result = run_probe(token="")
    assert result.returncode == 1, result.stdout + result.stderr
    assert result.stdout.startswith("::error title=CROSS_REPO_PAT absent::")


def test_classifier_self_test_covers_every_class():
    result = run_probe("--self-test")
    assert result.returncode == 0, result.stdout + result.stderr
    assert result.stdout.splitlines()[-1] == "SELF-TEST: PASS"
