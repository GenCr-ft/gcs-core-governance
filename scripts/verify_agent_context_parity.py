#!/usr/bin/env python3
"""
verify_agent_context_parity.py — Agent-context parity check.

Checks three invariants:
  1. rule_ids in storage-rules.yml all appear in the routing table of document-routing.md.
  2. target_path_template placeholder variable names in storage-rules.yml match those used
     in the corresponding rows of document-routing.md (prevents silent naming divergence).
  3. Every GemID row in technical-constraints.md §Key Agents Referenced also appears in
     studio-quick-ref.md §Key Gem Contacts for Escalation.
     (studio-quick-ref.md may list additional contacts — that is expected and not an error.)

Note: Invariant 2 from the original four (validation rule IDs present in document-routing.md)
was removed.  As of commit 6925a39, document-routing.md intentionally uses a pointer-only
§Validation Rules section — it no longer mirrors the GOV_RULE_NNN rows that live in
validation-rules.yml.  The canonical source for those rules is validation-rules.yml itself.

Exit 0 = PASS (all invariants satisfied).
Exit 1 = FAIL (details printed to stdout).
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
STORAGE_RULES = REPO_ROOT / "config-engines" / "metadata-schemas" / "storage-rules.yml"
VALIDATION_RULES = REPO_ROOT / "config-engines" / "metadata-schemas" / "validation-rules.yml"
ROUTING_DOC = REPO_ROOT / "agent-context" / "protocols" / "document-routing.md"
TECHNICAL_CONSTRAINTS = REPO_ROOT / "agent-context" / "grounding" / "technical-constraints.md"
STUDIO_QUICK_REF = REPO_ROOT / "agent-context" / "grounding" / "studio-quick-ref.md"


def extract_rule_ids_from_yaml(path: Path) -> list[str]:
    """Parse rule_id: values from a rules YAML file."""
    pattern = re.compile(r'^\s*-\s*rule_id:\s*"?([A-Z_0-9]+)"?', re.MULTILINE)
    return pattern.findall(path.read_text(encoding="utf-8"))


def extract_storage_rule_ids_from_routing_table(path: Path) -> list[str]:
    """Parse backtick-quoted STORAGE rule IDs (ALL_CAPS_STORAGE/RULE) from document-routing.md."""
    pattern = re.compile(r'`([A-Z][A-Z_]*(?:STORAGE|RULE)[A-Z_]*)`')
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


def check_subset(
    required_ids: set[str],
    superset_ids: set[str],
    required_label: str,
    superset_label: str,
) -> list[str]:
    """Check that required_ids is a subset of superset_ids (one-way; extra entries in superset are fine).

    Returns FAIL messages only for IDs missing from superset_ids.
    """
    failures = []
    missing = required_ids - superset_ids
    if missing:
        failures.append(f"FAIL: GemIDs in {required_label} missing from {superset_label}:")
        for rid in sorted(missing):
            failures.append(f"  - {rid}")
    return failures


def extract_template_placeholders_from_yaml(path: Path) -> dict[str, set[str]]:
    """Return {rule_id: set_of_placeholder_names} for rules that have target_path_template."""
    text = path.read_text(encoding="utf-8")
    rule_id_pattern = re.compile(r'-\s*rule_id:\s*"?([A-Z_0-9]+)"?')
    template_pattern = re.compile(r'target_path_template:\s*"([^"]+)"')
    placeholder_pattern = re.compile(r'\{([^}]+)\}')

    result: dict[str, set[str]] = {}
    # Split on rule blocks using the rule_id as a delimiter
    blocks = re.split(r'(?=-\s*rule_id:)', text)
    for block in blocks:
        rid_match = rule_id_pattern.search(block)
        tpl_match = template_pattern.search(block)
        if rid_match and tpl_match:
            rid = rid_match.group(1)
            placeholders = set(placeholder_pattern.findall(tpl_match.group(1)))
            result[rid] = placeholders
    return result


def extract_template_placeholders_from_routing_table(path: Path) -> dict[str, set[str]]:
    """Return {rule_id: set_of_placeholder_names} from path strings in document-routing.md table rows."""
    text = path.read_text(encoding="utf-8")
    placeholder_pattern = re.compile(r'\{([^}]+)\}')
    result: dict[str, set[str]] = {}
    for line in text.splitlines():
        # Match table rows that contain a backtick-quoted rule_id and a path fragment
        rid_match = re.search(r'`([A-Z][A-Z_]*(?:STORAGE|RULE)[A-Z_]*)`', line)
        if rid_match:
            rid = rid_match.group(1)
            placeholders = set(placeholder_pattern.findall(line))
            if placeholders:
                result[rid] = placeholders
    return result


def check_placeholder_parity(
    yaml_templates: dict[str, set[str]],
    routing_templates: dict[str, set[str]],
) -> list[str]:
    """Return failure messages for any rule whose placeholder sets diverge."""
    failures = []
    for rid, yaml_placeholders in yaml_templates.items():
        routing_placeholders = routing_templates.get(rid)
        if routing_placeholders is None:
            # Rule not in routing table — caught by rule_id parity check; skip here
            continue
        if yaml_placeholders != routing_placeholders:
            failures.append(
                f"FAIL: placeholder mismatch for rule {rid}:\n"
                f"  storage-rules.yml  : {sorted(yaml_placeholders)}\n"
                f"  document-routing.md: {sorted(routing_placeholders)}"
            )
    return failures


def extract_gem_ids_from_technical_constraints(path: Path) -> list[str]:
    """Parse GemID values from the Key Agents Referenced table in technical-constraints.md."""
    pattern = re.compile(r'\|\s*[^|]+\|\s*(GCT-[A-Z0-9]+-[A-Z0-9]+-\d+)')
    return pattern.findall(path.read_text(encoding="utf-8"))


def extract_gem_ids_from_quick_ref_escalation_table(path: Path) -> list[str]:
    """Parse GemID values from the Key Gem Contacts for Escalation table in studio-quick-ref.md."""
    pattern = re.compile(r'\|\s*[^|]+\|\s*(GCT-[A-Z0-9]+-[A-Z0-9]+-\d+)')
    return pattern.findall(path.read_text(encoding="utf-8"))


def main() -> int:
    missing_files = [
        p for p in [STORAGE_RULES, VALIDATION_RULES, ROUTING_DOC, TECHNICAL_CONSTRAINTS, STUDIO_QUICK_REF]
        if not p.exists()
    ]
    if missing_files:
        for p in missing_files:
            print(f"FAIL: required file not found: {p}")
        return 1

    storage_canonical = set(extract_rule_ids_from_yaml(STORAGE_RULES))
    routing_storage_ids = set(extract_storage_rule_ids_from_routing_table(ROUTING_DOC))

    yaml_templates = extract_template_placeholders_from_yaml(STORAGE_RULES)
    routing_templates = extract_template_placeholders_from_routing_table(ROUTING_DOC)

    storage_failures = check_parity(
        storage_canonical, routing_storage_ids, "storage-rules.yml", "document-routing.md routing table"
    )
    placeholder_failures = check_placeholder_parity(yaml_templates, routing_templates)

    # Invariant 3: every GemID in technical-constraints.md Key Agents Referenced must appear
    # in studio-quick-ref.md Key Gem Contacts for Escalation.
    # studio-quick-ref.md is the escalation table and may list additional contacts — that is
    # expected and is NOT a failure condition.
    constraints_gem_ids = set(extract_gem_ids_from_technical_constraints(TECHNICAL_CONSTRAINTS))
    quick_ref_gem_ids = set(extract_gem_ids_from_quick_ref_escalation_table(STUDIO_QUICK_REF))
    gem_failures = check_subset(
        constraints_gem_ids,
        quick_ref_gem_ids,
        "technical-constraints.md Key Agents Referenced",
        "studio-quick-ref.md Key Gem Contacts for Escalation",
    )

    all_failures = storage_failures + placeholder_failures + gem_failures

    if not all_failures:
        print(
            f"PASS: {len(storage_canonical)} storage rule IDs all present in document-routing.md; "
            f"all target_path_template placeholders match; "
            f"{len(constraints_gem_ids)} GemIDs from technical-constraints all present in studio-quick-ref"
        )
        return 0

    for line in all_failures:
        print(line)
    return 1


if __name__ == "__main__":
    sys.exit(main())
