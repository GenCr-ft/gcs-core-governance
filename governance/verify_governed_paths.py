#!/usr/bin/env python3
"""verify_governed_paths.py — reusable advisory governance-integrity check.

Self-contained (no cross-repo imports) so any repo can run it. Checksums every DRIFT-BLOCK
governed file listed in <root>/governance/governed-paths.yaml against the committed baseline
<root>/governance/governed-paths.sha256. Root = $GOVERNANCE_REPO_ROOT (or cwd). `--update`
regenerates the baseline.

Published by gcd-shared-actions#101 (pattern from gcs-plt-gemop#347). ADVISORY: meant to run in
CI and fail VISIBLY on drift; whether it is a required/blocking check is each repo's branch-
protection decision (unavailable on the current plan → advisory, per gcs-plt-gemop#356).

Only DRIFT-BLOCK rows are checksummed. revert-lock rows are a local-hook concern (auto-revert),
and their bare workspace-root globs would collide with a repo's own same-named files
(gcs-plt-gemop#354 adversary F2).
"""

from __future__ import annotations

import glob as globlib
import hashlib
import os
import sys
from pathlib import Path


def _root() -> Path:
    return Path(os.environ.get("GOVERNANCE_REPO_ROOT", ".")).resolve()


def _drift_block_globs(root: Path) -> list[str]:
    manifest = root / "governance" / "governed-paths.yaml"
    try:
        import yaml
        data = yaml.safe_load(manifest.read_text(encoding="utf-8"))
        rows = data.get("paths", []) if isinstance(data, dict) else []
    except Exception:
        return []
    return [r["glob"] for r in rows
            if isinstance(r, dict) and r.get("glob") and r.get("mode") == "drift-block"]


def current_checksums(root: Path) -> dict:
    root = root.resolve()
    out: dict[str, str] = {}
    for g in _drift_block_globs(root):
        for match in globlib.glob(str(root / g), recursive=True):
            p = Path(match)
            if "__pycache__" in p.parts or p.suffix == ".pyc":
                continue
            if not p.is_file():
                continue
            try:
                rel = p.resolve().relative_to(root).as_posix()  # skip anything a ../ glob pulls outside root
            except ValueError:
                continue
            out[rel] = hashlib.sha256(p.read_bytes()).hexdigest()
    return out


def _baseline_path(root: Path) -> Path:
    return root / "governance" / "governed-paths.sha256"


def read_baseline(root: Path) -> dict:
    bp = _baseline_path(root)
    if not bp.is_file():
        return {}
    out = {}
    for line in bp.read_text(encoding="utf-8").splitlines():
        line = line.strip()
        if not line or line.startswith("#"):
            continue
        h, _, path = line.partition("  ")
        if h and path:
            out[path] = h
    return out


def update(root: Path) -> int:
    cur = current_checksums(root)
    body = ("# governance-integrity baseline (gcd-shared-actions#101). ADVISORY.\n"
            "# Regenerate: GOVERNANCE_REPO_ROOT=<root> python scripts/verify_governed_paths.py --update\n")
    body += "".join(f"{h}  {p}\n" for p, h in sorted(cur.items()))
    _baseline_path(root).write_text(body, encoding="utf-8")
    print(f"baseline updated: {len(cur)} governed files")
    return 0


def verify(root: Path) -> tuple[int, list]:
    cur = current_checksums(root)
    base = read_baseline(root)
    drift = []
    for p, h in sorted(cur.items()):
        if p not in base:
            drift.append(("new", p))
        elif base[p] != h:
            drift.append(("changed", p))
    for p in sorted(base):
        if p not in cur:
            drift.append(("removed", p))
    return (1 if drift else 0), drift


def main(argv) -> int:
    root = _root()
    if "--update" in argv:
        return update(root)
    code, drift = verify(root)
    if drift:
        print("❌ governance-integrity: governed files drifted from the baseline:")
        for kind, p in drift:
            print(f"   {kind}: {p}")
        print("If intended: GOVERNANCE_REPO_ROOT=<root> python scripts/verify_governed_paths.py --update")
    else:
        print(f"✅ governance-integrity: {len(read_baseline(root))} governed files match the baseline.")
    return code


if __name__ == "__main__":
    sys.exit(main(sys.argv[1:]))
