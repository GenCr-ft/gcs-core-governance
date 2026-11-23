#!/usr/bin/env python3
"""Static contract for .github/workflows/agent-context-parity.yml.

GenCr-ft/gcs-core-governance#325, design #386 v6, [IMPL] #387.

Usage:
    check_parity_workflow_contract.py [WORKFLOW]   check a workflow file
    check_parity_workflow_contract.py --self-test  prove every check can fail alone

Exit codes: 0 the contract holds, 1 it is violated, 2 usage or parse error.

Each check id reports FAIL, SKIP or PASS. A SKIP means a check could not locate
the step it reads (a dependency failed), so it never hides a violation: the
dependency's own FAIL already makes the exit code 1.
"""

from __future__ import annotations

import copy
import fnmatch
import re
import subprocess
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FAIL: PyYAML is required to run the contract checker")
    sys.exit(2)

REPO_ROOT = Path(__file__).resolve().parent.parent
WORKFLOW_REL = ".github/workflows/agent-context-parity.yml"
GEMOP_REPO = "gencr-ft/gcs-plt-gemop"
SECRET_REF = "${{ secrets.CROSS_REPO_PAT }}"
ACTIVE_IDS = ("C0", "C1", "C2", "C3", "C5", "C6", "C7", "C8", "C11", "C13", "C14")

# The complete, ordered step list of job `parity` (design #386 v6, IMPL #387).
# `target` holds the compliant with/env values. C0 compares them only where the
# key is listed in `pinned`; the other values belong to C6, C7 and C11.
STEPS = [
    {
        "id": "S1",
        "name": "Checkout gcs-core-governance",
        "uses": "actions/checkout@v4",
        "with": {"persist-credentials": False},
        "pinned": (),
    },
    {
        "id": "S2",
        "name": "Set up Python",
        "uses": "actions/setup-python@v5",
        "with": {"python-version": "3.12"},
        "pinned": ("python-version",),
    },
    {
        "id": "S3",
        "name": "Install verifier dependencies",
        "run": "python -m pip install 'PyYAML==6.0.3'",
    },
    {
        "id": "S4",
        "name": "Verify the workflow contract",
        "run": "python3 tests/check_parity_workflow_contract.py",
    },
    {
        "id": "S5",
        "name": "Self-test the contract checker",
        "run": "python3 tests/check_parity_workflow_contract.py --self-test",
    },
    {
        "id": "S6",
        "name": "Self-test the credential classifier",
        "run": "bash scripts/check_gemop_credential.sh --self-test",
    },
    {
        "id": "S7",
        "name": "Verify CROSS_REPO_PAT can read gcs-plt-gemop/gems/index.yaml",
        "run": "bash scripts/check_gemop_credential.sh",
        "env": {"CROSS_REPO_PAT": SECRET_REF},
        "pinned": (),
    },
    {
        "id": "S8",
        "name": "Checkout gcs-plt-gemop for gem domain registry cross-reference",
        "uses": "actions/checkout@v4",
        "with": {
            "repository": "GenCr-ft/gcs-plt-gemop",
            "path": "gcs-plt-gemop",
            "token": SECRET_REF,
            "persist-credentials": False,
        },
        "pinned": (),
    },
    {
        "id": "S9",
        "name": (
            "Verify agent-context routing table matches storage-rules.yml "
            "and validation-rules.yml"
        ),
        "run": "python3 scripts/verify_agent_context_parity.py",
        "env": {"WORKSPACE_ROOT": "${{ github.workspace }}"},
        "pinned": ("WORKSPACE_ROOT",),
    },
    {
        "id": "S10",
        "name": "Verify wi-lifecycle-gates.yml gate phases match GOV-PROT-003",
        "run": "python3 scripts/verify_lifecycle_gate_parity.py",
    },
    {
        "id": "S11",
        "name": "Verify ssot-naming-cheatsheet.md type codes match taxonomy.yml",
        "run": "python3 scripts/verify_taxonomy_parity.py",
    },
]
STEP_BY_ID = {s["id"]: s for s in STEPS}
SECRETS_RE = re.compile(r"\$\{\{[^}]*\bsecrets\b")


class Report:
    """Per-id outcome: FAIL beats SKIP beats PASS."""

    def __init__(self) -> None:
        self.fails: dict[str, list[str]] = {}
        self.skips: dict[str, str] = {}

    def fail(self, cid: str, msg: str) -> None:
        self.fails.setdefault(cid, []).append(msg)
        self.skips.pop(cid, None)

    def skip(self, cid: str, reason: str) -> None:
        if cid not in self.fails:
            self.skips[cid] = reason

    def summary(self) -> str:
        if not self.fails and not self.skips:
            return "RESULT: PASS"
        return f"RESULT: FAIL {fmt(self.fails)} SKIP {fmt(self.skips)}"


def fmt(ids) -> str:
    order = {cid: i for i, cid in enumerate(ACTIVE_IDS)}
    return "{" + ", ".join(sorted(ids, key=lambda c: order.get(c, 99))) + "}"


def norm(text) -> str:
    return " ".join(str(text).split())


def triggers(wf: dict):
    """PyYAML reads the bare key `on` as boolean True; accept both forms."""
    return wf["on"] if "on" in wf else wf.get(True)


def key_names(mapping: dict) -> set:
    return {"on" if k is True else k for k in mapping}


def locate(steps: list) -> dict:
    """Map each STEPS id to its index, by pinned name. Absent or duplicated is unlocated."""
    names = [s.get("name") if isinstance(s, dict) else None for s in steps]
    return {
        spec["id"]: names.index(spec["name"])
        for spec in STEPS
        if names.count(spec["name"]) == 1
    }


def step_matches(step, spec: dict) -> list[str]:
    """C0's per-step comparison. Returns the mismatches."""
    if not isinstance(step, dict):
        return [f"{spec['id']}: not a mapping"]
    out = []
    if step.get("name") != spec["name"]:
        out.append(f"{spec['id']}: name {step.get('name')!r} != {spec['name']!r}")
    if "uses" in spec:
        want_keys, field = {"name", "uses", "with"}, "with"
        if step.get("uses") != spec["uses"]:
            out.append(f"{spec['id']}: uses {step.get('uses')!r} != {spec['uses']!r}")
    else:
        want_keys = {"name", "run"} | ({"env"} if "env" in spec else set())
        field = "env"
        if norm(step.get("run", "")) != norm(spec["run"]):
            out.append(f"{spec['id']}: run {step.get('run')!r} != {spec['run']!r}")
    if set(step) != want_keys:
        out.append(f"{spec['id']}: keys {sorted(step)} != {sorted(want_keys)}")
    if field in spec:
        got = step.get(field)
        if not isinstance(got, dict) or set(got) != set(spec[field]):
            got_keys = sorted(got) if isinstance(got, dict) else got
            out.append(
                f"{spec['id']}: {field} keys {got_keys} != {sorted(spec[field])}"
            )
        else:
            for key in spec.get("pinned", ()):
                if got[key] != spec[field][key]:
                    out.append(
                        f"{spec['id']}: {field}.{key} {got[key]!r} is not pinned value"
                    )
    return out


def walk_strings(node, path=()):
    """Yield (path, string) for every string key and value in the tree."""
    if isinstance(node, dict):
        for k, v in node.items():
            if isinstance(k, str):
                yield path + (k,), k
            yield from walk_strings(v, path + (k,))
    elif isinstance(node, list):
        for i, v in enumerate(node):
            yield from walk_strings(v, path + (i,))
    elif isinstance(node, str):
        yield path, node


def covered(path: str, patterns: list) -> bool:
    return any(path == p or fnmatch.fnmatch(path, p) for p in patterns)


def check(wf, tracked: set) -> Report:
    """Pure function of (workflow, tracked files): the whole contract."""
    rep = Report()
    if not isinstance(wf, dict):
        raise ValueError("workflow is not a mapping")
    on = triggers(wf) if isinstance(triggers(wf), dict) else {}
    jobs = wf.get("jobs") if isinstance(wf.get("jobs"), dict) else {}
    job = jobs.get("parity") if isinstance(jobs.get("parity"), dict) else {}
    steps = job.get("steps") if isinstance(job.get("steps"), list) else []
    pr = on.get("pull_request") if isinstance(on.get("pull_request"), dict) else {}
    push = on.get("push") if isinstance(on.get("push"), dict) else {}
    pr_paths, push_paths = pr.get("paths") or [], push.get("paths") or []

    # C14: workflow and job key allowlists.
    if key_names(wf) != {"name", "on", "permissions", "jobs"}:
        rep.fail("C14", f"top-level keys {sorted(map(str, key_names(wf)))}")
    if set(jobs) != {"parity"}:
        rep.fail("C14", f"jobs {sorted(jobs)} != ['parity']")
    if set(job) != {"runs-on", "steps"}:
        rep.fail("C14", f"job keys {sorted(job)} != ['runs-on', 'steps']")
    if job.get("runs-on") != "ubuntu-latest":
        rep.fail("C14", f"runs-on {job.get('runs-on')!r} != 'ubuntu-latest'")

    # C0: the complete, ordered step list.
    if len(steps) != len(STEPS):
        rep.fail("C0", f"{len(steps)} steps, expected {len(STEPS)}")
    for step, spec in zip(steps, STEPS):
        for msg in step_matches(step, spec):
            rep.fail("C0", msg)
    where = locate(steps)

    # C1, C2: trigger paths.
    for label, paths in (("pull_request", pr_paths), ("push", push_paths)):
        if WORKFLOW_REL not in paths:
            rep.fail("C1", f"{label}.paths lacks {WORKFLOW_REL}")
    if set(pr_paths) != set(push_paths):
        rep.fail("C2", "pull_request.paths != push.paths")
    if push.get("branches") != ["main"]:
        rep.fail("C2", f"push.branches {push.get('branches')!r} != ['main']")

    # C3: every tracked file a run: names is in both paths lists.
    for step in steps:
        run = step.get("run") if isinstance(step, dict) else None
        for token in str(run or "").split():
            if token in tracked:
                for label, paths in (("pull_request", pr_paths), ("push", push_paths)):
                    if not covered(token, paths):
                        rep.fail("C3", f"{token} not in {label}.paths")

    # C5: trigger names and their sub-key sets.
    if key_names(on) != {"pull_request", "push", "workflow_dispatch"}:
        rep.fail("C5", f"triggers {sorted(map(str, key_names(on)))}")
    if set(pr) != {"paths"}:
        rep.fail("C5", f"pull_request keys {sorted(pr)} != ['paths']")
    if set(push) != {"branches", "paths"}:
        rep.fail("C5", f"push keys {sorted(push)} != ['branches', 'paths']")
    if on.get("workflow_dispatch") not in (None, {}):
        rep.fail("C5", "workflow_dispatch must be empty")

    # C6: S8 values.
    if "S8" in where:
        w = steps[where["S8"]].get("with") or {}
        repo = str(w.get("repository", ""))
        if "${{" in repo or repo.lower() != GEMOP_REPO:
            rep.fail("C6", f"S8 repository {repo!r}")
        if w.get("token") != SECRET_REF:
            rep.fail("C6", "S8 token is not the CROSS_REPO_PAT secret")
        if w.get("path") != "gcs-plt-gemop":
            rep.fail("C6", f"S8 path {w.get('path')!r} != 'gcs-plt-gemop'")
    else:
        rep.skip("C6", "depends on C0 (S8 unlocated)")

    # C7: S7 env value.
    if "S7" in where:
        env = steps[where["S7"]].get("env") or {}
        if env.get("CROSS_REPO_PAT") != SECRET_REF:
            rep.fail("C7", "S7 env.CROSS_REPO_PAT is not the CROSS_REPO_PAT secret")
    else:
        rep.skip("C7", "depends on C0 (S7 unlocated)")

    # C8: the secrets context only at the two allowed sites.
    if "S7" in where and "S8" in where:
        allowed = {
            ("jobs", "parity", "steps", where["S7"], "env", "CROSS_REPO_PAT"),
            ("jobs", "parity", "steps", where["S8"], "with", "token"),
        }
        for path, text in walk_strings(wf):
            if SECRETS_RE.search(text) and path not in allowed:
                rep.fail("C8", f"secrets context at {'.'.join(map(str, path))}")
    else:
        rep.skip("C8", "depends on C0 (S7 or S8 unlocated)")

    # C11: persist-credentials false on both checkouts.
    sites = [sid for sid in ("S1", "S8") if sid in where]
    for sid in sites:
        w = steps[where[sid]].get("with") or {}
        if w.get("persist-credentials") is not False:
            rep.fail("C11", f"{sid} persist-credentials is not false")
    if not sites:
        rep.skip("C11", "depends on C0 (S1 and S8 unlocated)")

    # C13: permissions value.
    if "permissions" in wf:
        if wf["permissions"] != {"contents": "read"}:
            rep.fail("C13", f"permissions {wf['permissions']!r}")
    else:
        rep.skip("C13", "depends on C14 (no permissions key)")
    return rep


def tracked_files() -> set:
    proc = subprocess.run(
        ["git", "-C", str(REPO_ROOT), "ls-files", "-z"],
        capture_output=True,
        check=False,
    )
    if proc.returncode != 0:
        raise OSError(f"git ls-files exited {proc.returncode}")
    return {p for p in proc.stdout.decode().split("\0") if p}


# --- self-test ---------------------------------------------------------------

BASELINE_PATHS = [
    "config-engines/**",
    "agent-context/protocols/document-routing.md",
    "human-guides/validation-rules-summary.md",
    "agent-context/protocols/wi-lifecycle-gates.yml",
    "GOV-PROT-003.wi-lifecycle-contract.md",
    "human-guides/ssot-naming-cheatsheet.md",
    "agent-context/grounding/technical-constraints.md",
    "agent-context/grounding/studio-quick-ref.md",
    "scripts/verify_agent_context_parity.py",
    "reference-libraries/devops-standards/foundations/governance/rules/storage-rules.yml",
    WORKFLOW_REL,
    "scripts/verify_lifecycle_gate_parity.py",
    "scripts/verify_taxonomy_parity.py",
    "scripts/check_gemop_credential.sh",
    "tests/check_parity_workflow_contract.py",
]
SYNTHETIC_TRACKED = {
    WORKFLOW_REL,
    "scripts/verify_agent_context_parity.py",
    "scripts/verify_lifecycle_gate_parity.py",
    "scripts/verify_taxonomy_parity.py",
    "scripts/check_gemop_credential.sh",
    "tests/check_parity_workflow_contract.py",
}


def render(spec: dict) -> dict:
    step = {"name": spec["name"]}
    if "uses" in spec:
        step["uses"] = spec["uses"]
        step["with"] = dict(spec["with"])
    else:
        step["run"] = spec["run"]
        if "env" in spec:
            step["env"] = dict(spec["env"])
    return step


def baseline() -> dict:
    return {
        "name": "agent-context parity check",
        "on": {
            "pull_request": {"paths": list(BASELINE_PATHS)},
            "push": {"branches": ["main"], "paths": list(BASELINE_PATHS)},
            "workflow_dispatch": None,
        },
        "permissions": {"contents": "read"},
        "jobs": {
            "parity": {"runs-on": "ubuntu-latest", "steps": [render(s) for s in STEPS]}
        },
    }


def _step(wf, sid):
    return wf["jobs"]["parity"]["steps"][[s["id"] for s in STEPS].index(sid)]


def _drop_path(wf, path, which=("pull_request", "push")):
    for trig in which:
        wf["on"][trig]["paths"].remove(path)


def _mut(fn):
    def apply(wf):
        fn(wf)
        return wf

    return apply


MUTATIONS = [
    (
        "S10 run masked with || true",
        _mut(lambda w: _step(w, "S10").update(run=_step(w, "S10")["run"] + " || true")),
        {"C0"},
        set(),
    ),
    (
        "S11 removed",
        _mut(lambda w: w["jobs"]["parity"]["steps"].pop(10)),
        {"C0"},
        set(),
    ),
    (
        "extra step after S2",
        _mut(
            lambda w: w["jobs"]["parity"]["steps"].insert(
                2, {"name": "extra", "run": "echo hi"}
            )
        ),
        {"C0"},
        set(),
    ),
    (
        "S7 duplicated",
        _mut(
            lambda w: w["jobs"]["parity"]["steps"].insert(
                7, copy.deepcopy(_step(w, "S7"))
            )
        ),
        {"C0"},
        {"C7", "C8"},
    ),
    (
        "self path removed from both paths",
        _mut(lambda w: _drop_path(w, WORKFLOW_REL)),
        {"C1"},
        set(),
    ),
    (
        "config-engines/** removed from push only",
        _mut(lambda w: _drop_path(w, "config-engines/**", ("push",))),
        {"C2"},
        set(),
    ),
    (
        "push.branches widened",
        _mut(lambda w: w["on"]["push"].update(branches=["main", "dev"])),
        {"C2"},
        set(),
    ),
    (
        "taxonomy script removed from both paths",
        _mut(lambda w: _drop_path(w, "scripts/verify_taxonomy_parity.py")),
        {"C3"},
        set(),
    ),
    (
        "pull_request.branches added",
        _mut(lambda w: w["on"]["pull_request"].update(branches=["main"])),
        {"C5"},
        set(),
    ),
    (
        "pull_request_target added",
        _mut(lambda w: w["on"].update(pull_request_target=None)),
        {"C5"},
        set(),
    ),
    (
        "workflow_dispatch removed",
        _mut(lambda w: w["on"].pop("workflow_dispatch")),
        {"C5"},
        set(),
    ),
    (
        "S8 repository as an expression",
        _mut(
            lambda w: _step(w, "S8")["with"].update(
                repository="${{ github.repository_owner }}/gcs-plt-gemop"
            )
        ),
        {"C6"},
        set(),
    ),
    (
        "S7 env bound to another secret",
        _mut(
            lambda w: _step(w, "S7")["env"].update(
                CROSS_REPO_PAT="${{ secrets.OTHER }}"
            )
        ),
        {"C7"},
        set(),
    ),
    (
        "secret in the workflow name",
        _mut(lambda w: w.update(name="parity ${{ secrets.CROSS_REPO_PAT }}")),
        {"C8"},
        set(),
    ),
    (
        "S1 persist-credentials true",
        _mut(lambda w: _step(w, "S1")["with"].update({"persist-credentials": True})),
        {"C11"},
        set(),
    ),
    (
        "permissions widened",
        _mut(lambda w: w.update(permissions={"contents": "write"})),
        {"C13"},
        set(),
    ),
    ("top-level env added", _mut(lambda w: w.update(env={})), {"C14"}, set()),
    (
        "job if: false added",
        _mut(lambda w: w["jobs"]["parity"].update({"if": False})),
        {"C14"},
        set(),
    ),
    ("permissions removed", _mut(lambda w: w.pop("permissions")), {"C14"}, {"C13"}),
]

POSITIVE_CONTROLS = [
    ("baseline as built", _mut(lambda w: None)),
    (
        "S8 repository in lowercase",
        _mut(
            lambda w: _step(w, "S8")["with"].update(repository="gencr-ft/gcs-plt-gemop")
        ),
    ),
    (
        "S9 run reflowed",
        _mut(
            lambda w: _step(w, "S9").update(
                run="  python3   scripts/verify_agent_context_parity.py  "
            )
        ),
    ),
    ("on key read as PyYAML True", _mut(lambda w: w.update({True: w.pop("on")}))),
]


def self_test() -> int:
    bad = 0
    for label, apply, want_fail, want_skip in MUTATIONS:
        rep = check(apply(baseline()), SYNTHETIC_TRACKED)
        got_fail, got_skip = set(rep.fails), set(rep.skips)
        ok = (got_fail, got_skip) == (want_fail, want_skip)
        bad += not ok
        print(
            f"{'ok  ' if ok else 'BAD '} mutation {label}: FAIL {fmt(got_fail)} "
            f"SKIP {fmt(got_skip)} (want FAIL {fmt(want_fail)} SKIP {fmt(want_skip)})"
        )
    for label, apply in POSITIVE_CONTROLS:
        rep = check(apply(baseline()), SYNTHETIC_TRACKED)
        ok = not rep.fails and not rep.skips
        bad += not ok
        print(f"{'ok  ' if ok else 'BAD '} control {label}: {rep.summary()}")
    sole = {next(iter(f)) for _, _, f, _ in MUTATIONS if len(f) == 1}
    missing = set(ACTIVE_IDS) - sole
    if missing:
        bad += 1
        print(f"BAD  ids never the sole failure: {fmt(missing)}")
    print("SELF-TEST: PASS" if not bad else f"SELF-TEST: FAIL ({bad} bad)")
    return 0 if not bad else 1


def main(argv: list) -> int:
    if argv[1:] == ["--self-test"]:
        return self_test()
    if len(argv) > 2 or (len(argv) == 2 and argv[1].startswith("-")):
        print(__doc__)
        return 2
    target = Path(argv[1]) if len(argv) == 2 else REPO_ROOT / WORKFLOW_REL
    try:
        wf = yaml.safe_load(target.read_text(encoding="utf-8"))
        rep = check(wf, tracked_files())
    except (OSError, yaml.YAMLError, ValueError) as exc:
        print(f"ERROR: {exc}")
        return 2
    for cid in ACTIVE_IDS:
        for msg in rep.fails.get(cid, []):
            print(f"FAIL {cid}: {msg}")
        if cid in rep.skips:
            print(f"SKIP {cid}: {rep.skips[cid]}")
    print(rep.summary())
    return 1 if rep.fails else 0


if __name__ == "__main__":
    sys.exit(main(sys.argv))
