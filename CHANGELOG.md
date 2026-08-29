# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Add `poetry 2.4.1` to `tooling/ssot/.tool-versions-gft`, and rewrite the file's header to name a consumer per tool. **The version was chosen by measurement, not preference:** `pip install poetry` on the self-hosted pool is a **no-op** — poetry is already in the runner's persistent site-packages (`Requirement already satisfied: poetry … (2.4.1)`, confirmed as `poetry-2.4.1.dist-info` under both tool-cache interpreters) — so every Python job in the fleet runs an ambient version nobody chose, the mechanism gcs-plt-gemop#483 measured with PyYAML resolving to a 2019 build with known CVEs. Pinning 2.4.1 is a zero-behaviour-delta change. **2.1.3 was approved first and rejected on evidence**: it is what `gcs-plt-tools/onboard.sh:37` deliberately pins for developers, but it **cannot install gcs-plt-tools** (`install --dry-run` rc=1, *pyproject.toml changed significantly since poetry.lock was last generated*) — that repo holds 10 of the 13 call sites, and its lock last changed 2025-11-19 against a pyproject changed 2026-06-12. The probe carried both controls: must-pass (2.1.3 reads `gcd-ops-scripts`' `lock-version = "2.0"`, rc=0) and must-fire (a pyproject mutated to add an unlocked dependency, rc=1). **The header rewrite is the load-bearing half.** It previously said *"Read at runtime by gcd-onboarding-scripts get_ssot_tool_version()"* with no indication of *which* tools, so it reads as governing the whole toolchain when that function is called for exactly three entries (`02_installers.sh:414/422/430`) — a misreading that produced a published, since-retracted claim that this change would bump every developer across a Poetry major. **This entry enforces nothing yet** and the header now says so: no CI workflow reads this file and no installer requests poetry from it, so consumers are tracked separately (gcd-ops-scripts#175/#176, gcs-plt-tools#976, gct-service-template-py#49). `.tool-versions-gft` is not a governed path (0 of 32 entries), verified rather than assumed, so no baseline was re-recorded. (#354)
- Add the `intended_audience` term `investors` to the SSoT taxonomy and bump `ssot_version` to 1.6.0, implementing Decision 3 of the #320 ruling. All 21 pre-existing audience terms denote an internal studio audience, so an externally-addressed document had nowhere to map without misstating its readership; the other three unknown terms in that ruling are near-misses and are mapped rather than added. MINOR rather than PATCH per ENG-STAN-001 §3.1 — an added vocabulary term is backward-compatible added functionality, matching the 1.4.0 → 1.5.0 precedent set by #321 for the same change class. Verified additive-only across all ten vocabularies (nothing removed, with a synthetic-removal control), and functionally in both directions — a probe declaring `intended-audience: [investors]` is rejected under v1.5.0 and scans clean under the patched Law. `governance/governed-paths.sha256` re-baselined, exactly one hash changed. (#338)

- Add the repository's first `.gitignore`, adopted byte-identically from the canonical `gct-repo-template-standard` template plus a marked addendum, so locally-generated artifacts (notably `scripts/__pycache__/`) no longer appear as untracked noise. It is the first place the `.env` exclusions mandated by SEC-STAN-001 §3.3 and DEV-SPEC-003 §3 are satisfied in this repo. Per GOV-STANDARD-008 §6.1 (item 3) the SSoT linter must respect `.gitignore`, so patterns here will define SSoT validation scope once a caller workflow exists — prospective rather than operative today. No previously-tracked file becomes ignored (verified with `git check-ignore --no-index` across all 341 tracked files). (#304)

### Changed

- Update canonical .pre-commit-config.yaml to run SSoT linters locally via gft verify with graceful fallback instructions. (#308, @Antigravity)

### Fixed

- Remediate adversarial PR review findings, correcting pre-commit portability, resolving the split-brain amendment log, enforcing metadata validation on active taxonomy configurations, and correcting playbook tasklist instructions. (#1, @antigravity)
- Allow optional skos:definition and alternative skos:broader category mapping in taxonomy schema to resolve test suite drift checks. (#3, @antigravity)
