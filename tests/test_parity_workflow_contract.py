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


def load_checker():
    import importlib.util

    spec = importlib.util.spec_from_file_location("checker", CHECKER)
    mod = importlib.util.module_from_spec(spec)
    spec.loader.exec_module(mod)
    return mod


def test_self_test_baseline_paths_equal_the_real_workflow():
    checker = load_checker()
    import yaml

    wf = yaml.safe_load((ROOT / checker.WORKFLOW_REL).read_text(encoding="utf-8"))
    on = checker.triggers(wf)
    for trig in ("pull_request", "push"):
        assert set(on[trig]["paths"]) == set(checker.BASELINE_PATHS), trig


def test_non_mapping_with_is_reported_not_a_crash():
    checker = load_checker()
    wf = checker.baseline()
    checker._step(wf, "S8")["with"] = ["not", "a", "mapping"]
    rep = checker.check(wf, checker.SYNTHETIC_TRACKED)
    assert "C0" in rep.fails


def test_paths_globs_follow_github_semantics():
    checker = load_checker()
    assert checker.covered("config-engines/a/b.yml", ["config-engines/**"])
    assert not checker.covered("scripts/sub/x.py", ["scripts/*.py"])
    assert checker.covered("scripts/x.py", ["scripts/*.py"])


def test_secret_hidden_behind_a_brace_fails_c8():
    checker = load_checker()
    wf = checker.baseline()
    wf["name"] = "${{ format('{0}', secrets.CROSS_REPO_PAT) }}"
    assert set(checker.check(wf, checker.SYNTHETIC_TRACKED).fails) == {"C8"}


def test_checker_self_test_proves_every_check_can_fail():
    result = run_checker("--self-test")
    assert result.returncode == 0, result.stdout + result.stderr
    assert result.stdout.splitlines()[-1] == "SELF-TEST: PASS"
