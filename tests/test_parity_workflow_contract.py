"""WI-325: the parity workflow meets its static contract (design #386 v6)."""

import subprocess
import sys
from pathlib import Path

ROOT = Path(__file__).resolve().parent.parent
CHECKER = ROOT / "tests" / "check_parity_workflow_contract.py"


def run_checker(*args):
    return subprocess.run(
        [sys.executable, str(CHECKER), *args],
        capture_output=True,
        text=True,
        cwd=ROOT,
        check=False,
    )


def test_parity_workflow_meets_contract():
    result = run_checker()
    assert result.returncode != 2, (
        result.stdout + result.stderr
    )  # never a checker crash
    assert result.stdout.splitlines()[-1] == "RESULT: PASS"


def test_checker_self_test_proves_every_check_can_fail():
    result = run_checker("--self-test")
    assert result.returncode == 0, result.stdout + result.stderr
    assert result.stdout.splitlines()[-1] == "SELF-TEST: PASS"
