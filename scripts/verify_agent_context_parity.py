#!/usr/bin/env python3
"""
verify_agent_context_parity.py — Agent-context parity check.

Checks two invariants:
  1. rule_ids in storage-rules.yml all appear in the routing table of document-routing.md.
  2. rule_ids in validation-rules.yml all appear in the validation table of document-routing.md.

Exit 0 = PASS (all rule_ids present in respective tables).
Exit 1 = FAIL (details printed to stdout).
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STORAGE_RULES = REPO_ROOT / "config-engines" / "metadata-schemas" / "storage-rules.yml"
VALIDATION_RULES = REPO_ROOT / "config-engines" / "metadata-schemas" / "validation-rules.yml"
ROUTING_DOC = REPO_ROOT / "agent-context" / "protocols" / "document-routing.md"


def extract_rule_ids_from_yaml(path: Path) -> list[str]:
    """Parse rule_id: values from a rules YAML file."""
    pattern = re.compile(r'^\s*-\s*rule_id:\s*"?([A-Z_0-9]+)"?', re.MULTILINE)
    return pattern.findall(path.read_text(encoding="utf-8"))


def extract_storage_rule_ids_from_routing_table(path: Path) -> list[str]:
    """Parse backtick-quoted STORAGE rule IDs (ALL_CAPS_STORAGE/RULE) from document-routing.md."""
    pattern = re.compile(r'`([A-Z][A-Z_]*(?:STORAGE|RULE)[A-Z_]*)`')
    return pattern.findall(path.read_text(encoding="utf-8"))


def extract_validation_rule_ids_from_routing_table(path: Path) -> list[str]:
    """Parse backtick-quoted GOV_RULE_NNN IDs from document-routing.md."""
    pattern = re.compile(r'`(GOV_RULE_\d+)`')
    return pattern.findall(path.read_text(encoding="utf-8"))


def check_parity(
    canonical_ids: set[str],
    table_ids: set[str],
    source_label: str,
    table_label: str,
) -> list[str]:
    """Return list of failure messages, empty = PASS."""
    failures = []
    missing = canonical_ids - table_ids
    orphaned = table_ids - canonical_ids
    if missing:
        failures.append(f"FAIL: rule IDs in {source_label} missing from {table_label}:")
        for rid in sorted(missing):
            failures.append(f"  - {rid}")
    if orphaned:
        failures.append(f"WARN: rule IDs in {table_label} not found in {source_label}:")
        for rid in sorted(orphaned):
            failures.append(f"  - {rid}")
    return failures


def main() -> int:
    missing_files = [
        p for p in [STORAGE_RULES, VALIDATION_RULES, ROUTING_DOC] if not p.exists()
    ]
    if missing_files:
        for p in missing_files:
            print(f"FAIL: required file not found: {p}")
        return 1

    storage_canonical = set(extract_rule_ids_from_yaml(STORAGE_RULES))
    validation_canonical = set(extract_rule_ids_from_yaml(VALIDATION_RULES))
    routing_storage_ids = set(extract_storage_rule_ids_from_routing_table(ROUTING_DOC))
    routing_validation_ids = set(extract_validation_rule_ids_from_routing_table(ROUTING_DOC))

    storage_failures = check_parity(
        storage_canonical, routing_storage_ids, "storage-rules.yml", "document-routing.md routing table"
    )
    validation_failures = check_parity(
        validation_canonical, routing_validation_ids, "validation-rules.yml", "document-routing.md validation table"
    )

    all_failures = storage_failures + validation_failures

    if not all_failures:
        print(
            f"PASS: {len(storage_canonical)} storage rule IDs and "
            f"{len(validation_canonical)} validation rule IDs all present in document-routing.md"
        )
        return 0

    for line in all_failures:
        print(line)
    return 1


if __name__ == "__main__":
    sys.exit(main())
