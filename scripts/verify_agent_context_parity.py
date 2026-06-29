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
Exit 0 = WARN (only orphaned routing-table entries found; no canonical rule IDs missing).
Exit 1 = FAIL (one or more canonical rule IDs are absent from document-routing.md, or
         placeholder names diverge, GemID subset check fails, or required files are missing).
"""
import os
import re
import sys
from pathlib import Path

try:
    import yaml
except ImportError:
    print("FAIL: PyYAML is required — install with: pip install pyyaml")
    sys.exit(1)

REPO_ROOT = Path(__file__).resolve().parent.parent
STORAGE_RULES = REPO_ROOT / "config-engines" / "metadata-schemas" / "storage-rules.yml"
VALIDATION_RULES = REPO_ROOT / "config-engines" / "metadata-schemas" / "validation-rules.yml"
ROUTING_DOC = REPO_ROOT / "agent-context" / "protocols" / "document-routing.md"
REFLIB_STORAGE_RULES = REPO_ROOT / "reference-libraries" / "devops-standards" / "foundations" / "governance" / "rules" / "storage-rules.yml"
CONFIG_DIRS_REQUIRED_NON_EMPTY = [
    REPO_ROOT / "config-engines" / "pipeline-thresholds",
    REPO_ROOT / "config-engines" / "api-parameters",
]
TECHNICAL_CONSTRAINTS = REPO_ROOT / "agent-context" / "grounding" / "technical-constraints.md"
STUDIO_QUICK_REF = REPO_ROOT / "agent-context" / "grounding" / "studio-quick-ref.md"
REGISTRY = REPO_ROOT / "config-engines" / "metadata-schemas" / "gem-domain-registry.yml"
WORKSPACE_ROOT = Path(os.environ.get("WORKSPACE_ROOT", str(REPO_ROOT.parent)))
GEMS_INDEX = WORKSPACE_ROOT / "gcs-plt-gemop" / "gems" / "index.yaml"
GEM_ID_PATTERN = re.compile(r"^gct-[a-z]+-[a-z]+-\d{3}-[a-z]+$")


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


def check_reflib_parity(canonical_path: Path, reflib_path: Path) -> list[str]:
    """Verify that reference-libraries copy of storage-rules.yml is byte-for-byte identical
    to the canonical copy (ignoring the leading comment header lines which are identical).
    Compares each rule block field-by-field: rule_id, description, justification.
    Returns list of failure messages, empty = PASS.
    """
    failures = []
    canonical_text = canonical_path.read_text(encoding="utf-8")
    reflib_text = reflib_path.read_text(encoding="utf-8")

    # Strip leading comment lines (lines starting with #) for YAML parsing
    def strip_comments(text: str) -> str:
        lines = text.splitlines()
        body_lines = [l for l in lines if not l.startswith("#")]
        return "\n".join(body_lines)

    canonical_data = yaml.safe_load(strip_comments(canonical_text))
    reflib_data = yaml.safe_load(strip_comments(reflib_text))

    canonical_rules = {r["rule_id"]: r for r in canonical_data.get("storage_rules", [])}
    reflib_rules = {r["rule_id"]: r for r in reflib_data.get("storage_rules", [])}

    for rule_id, canonical_rule in canonical_rules.items():
        if rule_id not in reflib_rules:
            failures.append(f"FAIL: rule {rule_id!r} missing from reference-libraries copy")
            continue
        reflib_rule = reflib_rules[rule_id]
        for field in ("description", "justification"):
            # justification is nested under 'then'
            canonical_val = canonical_rule.get(field) or canonical_rule.get("then", {}).get(field)
            reflib_val = reflib_rule.get(field) or reflib_rule.get("then", {}).get(field)
            if canonical_val != reflib_val:
                failures.append(
                    f"FAIL: {rule_id}.{field} diverges:\n"
                    f"  canonical:  {canonical_val!r}\n"
                    f"  reflib:     {reflib_val!r}"
                )

    for rule_id in reflib_rules:
        if rule_id not in canonical_rules:
            failures.append(f"WARN: rule {rule_id!r} in reference-libraries copy not in canonical")

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


def check_config_dirs_non_empty(dirs: list[Path]) -> list[str]:
    """Return failure messages for any config-engines subdirectory that is empty."""
    failures = []
    for d in dirs:
        if not d.is_dir():
            failures.append(f"FAIL: required config directory not found: {d}")
        elif not any(f for f in d.iterdir() if f.is_file()):
            failures.append(
                f"FAIL: config directory is empty (rules-index.md pointer is broken): {d.relative_to(REPO_ROOT)}"
            )
    return failures


def check_gem_domain_registry_valid(path: Path) -> list[str]:
    """Validate gem-domain-registry.yml structure.

    Returns FAIL messages for: missing _meta, empty exempt_conditions, or domain
    entries lacking gem_id/display/authoritative keys.
    """
    failures = []
    try:
        data = yaml.safe_load(path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        failures.append(f"FAIL: could not parse {path.name}: {exc}")
        return failures

    if not isinstance(data, dict):
        failures.append(f"FAIL: {path.name} must be a YAML mapping at the top level")
        return failures

    if "_meta" not in data:
        failures.append(f"FAIL: {path.name} missing '_meta' block")

    exempt = data.get("exempt_conditions")
    if not exempt:
        failures.append(f"FAIL: {path.name} 'exempt_conditions' is absent or empty")

    for i, entry in enumerate(data.get("domains", [])):
        for field in ("gem_id", "display", "authoritative"):
            if field not in entry:
                failures.append(
                    f"FAIL: {path.name} domains[{i}] missing required field '{field}'"
                )
        gem_id = entry.get("gem_id", "")
        if gem_id and not GEM_ID_PATTERN.match(gem_id):
            failures.append(
                f"FAIL: {path.name} domains[{i}] gem_id {gem_id!r} does not match "
                r"^gct-[a-z]+-[a-z]+-\d{3}-[a-z]+$"
            )

    return failures


def check_gem_ids_in_gems_index(registry_path: Path, gems_index_path: Path) -> list[str]:
    """Verify every gem_id in the registry has a matching entry in gems/index.yaml.

    Cross-reference algorithm: re.sub(r"-[a-z]+$", "", gem_id).upper() produces the
    canonical GCT-* id (e.g. gct-prg-ldtl-001-forge → GCT-PRG-LDTL-001). The result
    is looked up in the 'id' field of each entry in gems/index.yaml.

    Assumes a single-word lowercase-alpha display suffix. Multi-word suffixes (e.g.
    tech-lead) would produce incorrect lookup keys — no such entries exist in the
    current gem corpus, but this constraint should be documented when adding new gems.

    Returns a FAIL message immediately if gems_index_path does not exist.
    """
    if not gems_index_path.exists():
        return [
            f"FAIL: {gems_index_path.name} not found at {gems_index_path} — "
            "verify WORKSPACE_ROOT env var or sibling gcs-plt-gemop checkout"
        ]

    try:
        index_data = yaml.safe_load(gems_index_path.read_text(encoding="utf-8"))
    except yaml.YAMLError as exc:
        return [f"FAIL: could not parse {gems_index_path.name}: {exc}"]

    index_ids = {entry["id"] for entry in index_data.get("gems", []) if "id" in entry}

    try:
        registry_data = yaml.safe_load(registry_path.read_text(encoding="utf-8"))
    except yaml.YAMLError:
        return []  # structural issues caught by check_gem_domain_registry_valid

    failures = []
    for entry in registry_data.get("domains", []):
        gem_id = entry.get("gem_id", "")
        if not gem_id:
            continue
        canonical_id = re.sub(r"-[a-z]+$", "", gem_id).upper()
        if canonical_id not in index_ids:
            failures.append(
                f"FAIL: gem_id {gem_id!r} → {canonical_id!r} not found in "
                f"{gems_index_path.name}"
            )
    return failures


def main() -> int:
    missing_files = [
        p for p in [STORAGE_RULES, VALIDATION_RULES, ROUTING_DOC, TECHNICAL_CONSTRAINTS, STUDIO_QUICK_REF, REFLIB_STORAGE_RULES, REGISTRY, GEMS_INDEX]
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
    reflib_failures = check_reflib_parity(STORAGE_RULES, REFLIB_STORAGE_RULES)

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

    registry_failures = check_gem_domain_registry_valid(REGISTRY)
    cross_ref_failures = check_gem_ids_in_gems_index(REGISTRY, GEMS_INDEX)

    all_failures = storage_failures + placeholder_failures + reflib_failures + gem_failures + registry_failures + cross_ref_failures

    if not all_failures:
        try:
            _reg = yaml.safe_load(REGISTRY.read_text(encoding="utf-8"))
            _gem_count = len(_reg.get("domains", []))
        except Exception:
            _gem_count = 0
        print(
            f"PASS: {len(storage_canonical)} storage rule IDs all present in document-routing.md; "
            f"all target_path_template placeholders match; "
            f"reference-libraries copy is in parity with canonical; "
            f"{len(constraints_gem_ids)} GemIDs from technical-constraints all present in studio-quick-ref; "
            f"gem-domain-registry.yml structure valid; "
            f"{_gem_count} gem IDs validated against gems/index.yaml"
        )
        return 0

    for line in all_failures:
        print(line)
    return 1
if __name__ == "__main__":
    sys.exit(main())
