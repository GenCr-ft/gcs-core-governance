#!/usr/bin/env python3
"""
verify_agents_md_parity.py — AGENTS.md parity check.

Checks two invariants:
  1. Every Markdown link target in AGENTS.md resolves to an existing file under
     the repo root.
  2. If AGENTS.md frontmatter has a `source_version:` field, it must match the
     `# Version:` header in config-engines/metadata-schemas/storage-rules.yml.
     (The document version: field is the AGENTS.md doc version, not a source pin.)

Exit 0 = PASS (all invariants satisfied or only WARNs).
Exit 1 = FAIL (one or more FAIL lines emitted).
"""
import re
import sys
from pathlib import Path

REPO_ROOT = Path(__file__).resolve().parent.parent
AGENTS_MD = REPO_ROOT / "AGENTS.md"
STORAGE_RULES = REPO_ROOT / "config-engines" / "metadata-schemas" / "storage-rules.yml"


def extract_md_link_targets(text: str) -> list[str]:
    return re.findall(r'\[(?:[^\]]+)\]\(([^)#]+)\)', text)


def check_link_targets(agents_text: str) -> list[str]:
    failures = []
    for target in extract_md_link_targets(agents_text):
        target = target.strip()
        if target.startswith(("http://", "https://", "mailto:")):
            continue
        if not (REPO_ROOT / target).exists():
            failures.append(f"FAIL: AGENTS.md link target missing: {target}")
    return failures


def check_source_version_sync(agents_text: str) -> list[str]:
    """If AGENTS.md has source_version: pin, verify it matches storage-rules.yml."""
    m = re.search(r"^\s+source_version:\s*['\"]?([\d.]+)['\"]?", agents_text, re.MULTILINE)
    if not m:
        return ["WARN: AGENTS.md has no source_version: pin — drift detection not wired (see #284)"]
    agents_src_ver = m.group(1)

    if not STORAGE_RULES.exists():
        return [f"FAIL: storage-rules.yml not found at {STORAGE_RULES}"]
    rv = re.search(r"^# Version:\s*([\d.]+)", STORAGE_RULES.read_text(encoding="utf-8"), re.MULTILINE)
    if not rv:
        return ["WARN: storage-rules.yml has no '# Version:' header — version sync skipped"]
    rules_ver = rv.group(1)

    if agents_src_ver != rules_ver:
        return [f"FAIL: AGENTS.md source_version ({agents_src_ver}) != storage-rules.yml version ({rules_ver})"]
    return []


def main() -> int:
    if not AGENTS_MD.exists():
        print(f"FAIL: AGENTS.md not found at {AGENTS_MD}", file=sys.stderr)
        return 1

    agents_text = AGENTS_MD.read_text(encoding="utf-8")
    findings = check_link_targets(agents_text) + check_source_version_sync(agents_text)

    hard_failures = [f for f in findings if f.startswith("FAIL:")]
    warnings = [f for f in findings if f.startswith("WARN:")]

    for w in warnings:
        print(w)
    for f in hard_failures:
        print(f, file=sys.stderr)

    if hard_failures:
        return 1

    link_count = sum(
        1 for t in extract_md_link_targets(agents_text)
        if not t.strip().startswith(("http://", "https://", "mailto:"))
    )
    print(f"PASS: {link_count} AGENTS.md link targets verified; source_version sync checked")
    return 0


if __name__ == "__main__":
    sys.exit(main())
