#!/usr/bin/env python3
"""
verify_lifecycle_gate_parity.py — WI lifecycle gate parity check.

Checks that agent-context/protocols/wi-lifecycle-gates.yml is consistent
with GOV-PROT-003.wi-lifecycle-contract.md:

  1. metadata.source_version in wi-lifecycle-gates.yml is a parseable YAML
     field (not a comment) — exits non-zero with named failure if absent.
  2. Every phase name in wi-lifecycle-gates.yml[gates] that maps to a numbered
     GOV-PROT-003 gate (create, refine, implement, close) has its required
     sections present in GOV-PROT-003.
  3. The design phase in wi-lifecycle-gates.yml is flagged as an extension
     phase (no numbered gate in GOV-PROT-003) — exits non-zero if it is
     presented as a canonical gate with no annotation.

Exit 0 = PASS. Exit 1 = FAIL (details printed to stdout).
"""
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FAIL: PyYAML is required — install with: pip install pyyaml")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
GATES_YML = REPO_ROOT / "agent-context" / "protocols" / "wi-lifecycle-gates.yml"
GOV_PROT_003 = REPO_ROOT / "GOV-PROT-003.wi-lifecycle-contract.md"

# Phases in wi-lifecycle-gates.yml that correspond to numbered gates in GOV-PROT-003.
# The `design` phase is an extension not numbered in GOV-PROT-003 — it must be
# annotated as such in the YAML (presence of `extension_phase: true`).
CANONICAL_GATE_PHASES = {"create", "refine", "implement", "close"}
EXTENSION_PHASES = {"design"}

# Required sections per GOV-PROT-003 (Gate 1 = create, Gate 2 = refine,
# Gate 3 = implement, Gate 4 = close).
GOV_PROT_003_REQUIRED_SECTIONS = {
    "create": ["## Summary", "## Acceptance Criteria", "## Architecture Impact", "## Out of Scope"],
    "refine": ["## Acceptance Criteria", "## Testability Notes", "## Sub-issues"],
    "implement": [
        "## Relations", "## Desired Outcome", "## AC Coverage Map",
        "## Technical Scope", "## TDD Cycles", "## Integration & E2E Verification",
        "## Risk Register", "## External Dependencies", "## Rollback Plan",
        "## Definition of Done",
    ],
    "close": [],  # Gate 4 checks are condition-based, not section-based
}


def load_gates_yml(path: Path) -> dict:
    """Load and parse wi-lifecycle-gates.yml, returning the parsed dict."""
    text = path.read_text(encoding="utf-8")
    return yaml.safe_load(text)


def check_metadata_fields(data: dict) -> list[str]:
    """Verify metadata.source_version and metadata.last_verified are real YAML fields.

    The file uses the studio _meta SSoT convention: fields live under
    _meta.metadata (not at the top level). Fall back to a bare top-level
    'metadata' key for forward-compatibility.
    """
    failures = []
    metadata = data.get("_meta", {}).get("metadata")
    if metadata is None:
        metadata = data.get("metadata")
    if not isinstance(metadata, dict):
        failures.append(
            "FAIL: wi-lifecycle-gates.yml missing '_meta.metadata' block — "
            "source_version and last_verified must be parseable YAML fields, not comments"
        )
        return failures
    if "source_version" not in metadata:
        failures.append(
            "FAIL: metadata.source_version absent from wi-lifecycle-gates.yml — "
            "must be a YAML field, not a comment"
        )
    if "last_verified" not in metadata:
        failures.append(
            "FAIL: metadata.last_verified absent from wi-lifecycle-gates.yml — "
            "must be a YAML field, not a comment"
        )
    return failures


def check_extension_phase_annotated(data: dict) -> list[str]:
    """Verify that phases not numbered in GOV-PROT-003 carry an extension annotation.

    Accepts either ``extension_phase: true`` or ``gate_number: null`` as
    equivalent markers — the latter is the canonical form used in
    wi-lifecycle-gates.yml where an inline comment further clarifies intent.
    """
    failures = []
    gates = data.get("gates", [])
    for gate in gates:
        phase = gate.get("phase", "")
        if phase not in EXTENSION_PHASES:
            continue
        annotated = gate.get("extension_phase") or (
            "gate_number" in gate and gate.get("gate_number") is None
        )
        if not annotated:
            failures.append(
                f"FAIL: phase '{phase}' in wi-lifecycle-gates.yml has no numbered gate in "
                f"GOV-PROT-003 but lacks an extension annotation — add either "
                f"'extension_phase: true' or 'gate_number: null' to clarify that this phase "
                f"is not a canonical GOV-PROT-003 gate"
            )
    return failures


def check_required_sections_present(data: dict) -> list[str]:
    """Verify canonical phases list at least the GOV-PROT-003 required sections."""
    failures = []
    gates = data.get("gates", [])
    phase_map = {g.get("phase"): g for g in gates}
    for phase, required in GOV_PROT_003_REQUIRED_SECTIONS.items():
        if not required:
            continue
        gate = phase_map.get(phase)
        if gate is None:
            failures.append(f"FAIL: GOV-PROT-003 canonical phase '{phase}' missing from wi-lifecycle-gates.yml")
            continue
        # Collect all section keys that could hold required sections
        declared = set()
        for key in ("required_sections", "required_sections_in_design_issue",
                    "required_sections_in_impl_issue"):
            for item in gate.get(key, []):
                declared.add(item)
        for section in required:
            if section not in declared:
                failures.append(
                    f"FAIL: GOV-PROT-003 required section '{section}' for phase '{phase}' "
                    f"is missing from wi-lifecycle-gates.yml — drift detected"
                )
    return failures


def check_gov_prot_003_readable(path: Path) -> list[str]:
    """Confirm GOV-PROT-003 can be read (basic existence/encoding check)."""
    failures = []
    if not path.exists():
        failures.append(f"FAIL: {path.name} not found at expected path {path}")
        return failures
    try:
        path.read_text(encoding="utf-8")
    except OSError as exc:
        failures.append(f"FAIL: cannot read {path.name}: {exc}")
    return failures


def main() -> int:
    missing = [p for p in [GATES_YML, GOV_PROT_003] if not p.exists()]
    if missing:
        for p in missing:
            print(f"FAIL: required file not found: {p}")
        return 1

    try:
        data = load_gates_yml(GATES_YML)
    except yaml.YAMLError as exc:
        print(f"FAIL: could not parse {GATES_YML.name}: {exc}")
        return 1

    all_failures = (
        check_metadata_fields(data)
        + check_extension_phase_annotated(data)
        + check_required_sections_present(data)
        + check_gov_prot_003_readable(GOV_PROT_003)
    )

    if not all_failures:
        print(
            "PASS: wi-lifecycle-gates.yml metadata fields are parseable YAML, "
            "extension phases are annotated, and all GOV-PROT-003 required sections "
            "are present for canonical phases"
        )
        return 0

    for line in all_failures:
        print(line)
    return 1


if __name__ == "__main__":
    sys.exit(main())
