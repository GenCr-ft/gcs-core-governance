#!/usr/bin/env python3
"""
verify_taxonomy_parity.py — Taxonomy type-code parity check.

Checks that every Document Type Code row in human-guides/ssot-naming-cheatsheet.md
exists as a code in config-engines/metadata-schemas/taxonomy.yml
knowledge_classification_type[*].code.

Exit 0 = PASS (all cheatsheet codes present in taxonomy.yml).
Exit 1 = FAIL (details printed to stdout).
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
TAXONOMY = REPO_ROOT / "config-engines" / "metadata-schemas" / "taxonomy.yml"
CHEATSHEET = REPO_ROOT / "human-guides" / "ssot-naming-cheatsheet.md"


def extract_taxonomy_codes(path: Path) -> set[str]:
    """Extract all code values from knowledge_classification_type in taxonomy.yml."""
    text = path.read_text(encoding="utf-8")
    # Find knowledge_classification_type block and extract code values
    in_block = False
    codes: set[str] = set()
    for line in text.splitlines():
        if line.strip() == "knowledge_classification_type:":
            in_block = True
            continue
        if in_block:
            # Stop at next top-level key
            if re.match(r'^[a-z]', line) and not line.startswith(" ") and ":" in line:
                in_block = False
                continue
            m = re.match(r'\s+code:\s*"?([A-Z][A-Z0-9]*)"?', line)
            if m:
                codes.add(m.group(1))
    return codes


def extract_cheatsheet_codes(path: Path) -> set[str]:
    """Extract all type codes from the Document Type Codes table in the cheatsheet."""
    text = path.read_text(encoding="utf-8")
    in_table = False
    codes: set[str] = set()
    for line in text.splitlines():
        if "## Document Type Codes" in line:
            in_table = True
            continue
        if in_table:
            if line.startswith("## "):
                break
            m = re.match(r'\|\s*`([A-Z][A-Z0-9]*)`\s*\|', line)
            if m:
                codes.add(m.group(1))
    return codes


def check_uniqueness_in_cheatsheet(path: Path) -> list[str]:
    """Return failure messages for duplicate codes in the cheatsheet table."""
    text = path.read_text(encoding="utf-8")
    in_table = False
    seen: list[str] = []
    duplicates: list[str] = []
    for line in text.splitlines():
        if "## Document Type Codes" in line:
            in_table = True
            continue
        if in_table:
            if line.startswith("## "):
                break
            m = re.match(r'\|\s*`([A-Z][A-Z0-9]*)`\s*\|', line)
            if m:
                code = m.group(1)
                if code in seen:
                    duplicates.append(f"FAIL: duplicate code '{code}' in Document Type Codes table in {path.name}")
                else:
                    seen.append(code)
    return duplicates


def main() -> int:
    missing = [p for p in [TAXONOMY, CHEATSHEET] if not p.exists()]
    if missing:
        for p in missing:
            print(f"FAIL: required file not found: {p}")
        return 1

    failures: list[str] = []

    # AC-1 (broadened): all codes in the cheatsheet table must be unique
    failures.extend(check_uniqueness_in_cheatsheet(CHEATSHEET))

    # AC-2 (ASTRID): every cheatsheet code must exist in taxonomy.yml
    taxonomy_codes = extract_taxonomy_codes(TAXONOMY)
    cheatsheet_codes = extract_cheatsheet_codes(CHEATSHEET)
    missing_in_taxonomy = cheatsheet_codes - taxonomy_codes
    if missing_in_taxonomy:
        failures.append(
            f"FAIL: type codes in {CHEATSHEET.name} missing from taxonomy.yml knowledge_classification_type:"
        )
        for code in sorted(missing_in_taxonomy):
            failures.append(f"  - {code}")

    if not failures:
        print(
            f"PASS: {len(cheatsheet_codes)} type codes in ssot-naming-cheatsheet.md are unique "
            f"and all present in taxonomy.yml"
        )
        return 0

    for line in failures:
        print(line)
    return 1


if __name__ == "__main__":
    sys.exit(main())
