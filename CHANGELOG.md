# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Added

- Add the `intended_audience` term `investors` to the SSoT taxonomy and bump `ssot_version` to 1.6.0, implementing Decision 3 of the #320 ruling. All 21 pre-existing audience terms denote an internal studio audience, so an externally-addressed document had nowhere to map without misstating its readership; the other three unknown terms in that ruling are near-misses and are mapped rather than added. MINOR rather than PATCH per ENG-STAN-001 §3.1 — an added vocabulary term is backward-compatible added functionality, matching the 1.4.0 → 1.5.0 precedent set by #321 for the same change class. Verified additive-only across all ten vocabularies (nothing removed, with a synthetic-removal control), and functionally in both directions — a probe declaring `intended-audience: [investors]` is rejected under v1.5.0 and scans clean under the patched Law. `governance/governed-paths.sha256` re-baselined, exactly one hash changed. (#338)

- Add the repository's first `.gitignore`, adopted byte-identically from the canonical `gct-repo-template-standard` template plus a marked addendum, so locally-generated artifacts (notably `scripts/__pycache__/`) no longer appear as untracked noise. It is the first place the `.env` exclusions mandated by SEC-STAN-001 §3.3 and DEV-SPEC-003 §3 are satisfied in this repo. Per GOV-STANDARD-008 §6.1 (item 3) the SSoT linter must respect `.gitignore`, so patterns here will define SSoT validation scope once a caller workflow exists — prospective rather than operative today. No previously-tracked file becomes ignored (verified with `git check-ignore --no-index` across all 341 tracked files). (#304)

### Changed

- Update canonical .pre-commit-config.yaml to run SSoT linters locally via gft verify with graceful fallback instructions. (#308, @Antigravity)

### Fixed

- Remediate adversarial PR review findings, correcting pre-commit portability, resolving the split-brain amendment log, enforcing metadata validation on active taxonomy configurations, and correcting playbook tasklist instructions. (#1, @antigravity)
- Allow optional skos:definition and alternative skos:broader category mapping in taxonomy schema to resolve test suite drift checks. (#3, @antigravity)
