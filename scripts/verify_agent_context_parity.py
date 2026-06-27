#!/usr/bin/env python3
"""
verify_agent_context_parity.py — Agent-context/storage-rules parity check.

Compares rule_ids in config-engines/metadata-schemas/storage-rules.yml against
the Rule ID column in agent-context/protocols/document-routing.md.

Exit 0 = PASS (all rule_ids present in routing table).
Exit 1 = FAIL (details printed to stdout).
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STORAGE_RULES = REPO_ROOT / "config-engines" / "metadata-schemas" / "storage-rules.yml"
ROUTING_DOC = REPO_ROOT / "agent-context" / "protocols" / "document-routing.md"


def extract_rule_ids_from_yaml(path: Path) -> list[str]:
    """Parse rule_id: values from storage-rules.yml."""
    pattern = re.compile(r'^\s*-\s*rule_id:\s*"?([A-Z_]+)"?', re.MULTILINE)
    return pattern.findall(path.read_text(encoding="utf-8"))


def extract_rule_ids_from_routing_table(path: Path) -> list[str]:
    """Parse backtick-quoted RULE_IDs from the routing table in document-routing.md."""
    pattern = re.compile(r'`([A-Z_]+)`')
    return pattern.findall(path.read_text(encoding="utf-8"))


def main() -> int:
    if not STORAGE_RULES.exists():
        print(f"FAIL: storage-rules.yml not found at {STORAGE_RULES}")
        return 1
    if not ROUTING_DOC.exists():
        print(f"FAIL: document-routing.md not found at {ROUTING_DOC}")
        return 1

    canonical_ids = set(extract_rule_ids_from_yaml(STORAGE_RULES))
    routing_ids = set(extract_rule_ids_from_routing_table(ROUTING_DOC))

    missing_from_routing = canonical_ids - routing_ids
    orphaned_in_routing = routing_ids - canonical_ids

    if not missing_from_routing and not orphaned_in_routing:
        print(f"PASS: {len(canonical_ids)} rule IDs match between storage-rules.yml and document-routing.md")
        return 0

    if missing_from_routing:
        print("FAIL: rule IDs in storage-rules.yml missing from document-routing.md:")
        for rid in sorted(missing_from_routing):
            print(f"  - {rid}")
    if orphaned_in_routing:
        print("WARN: rule IDs in document-routing.md not found in storage-rules.yml:")
        for rid in sorted(orphaned_in_routing):
            print(f"  - {rid}")

    return 1


if __name__ == "__main__":
    sys.exit(main())
