# Changelog

All notable changes to this project will be documented in this file.

The format is based on [Keep a Changelog](https://keepachangelog.com/en/1.0.0/),
and this project adheres to [Semantic Versioning](https://semver.org/spec/v2.0.0.html).

## [Unreleased]

### Changed

- Update canonical .pre-commit-config.yaml to run SSoT linters locally via gft verify with graceful fallback instructions. (#308, @Antigravity)

### Fixed

- Remediate adversarial PR review findings, correcting pre-commit portability, resolving the split-brain amendment log, enforcing metadata validation on active taxonomy configurations, and correcting playbook tasklist instructions. (#1, @antigravity)
- Allow optional skos:definition and alternative skos:broader category mapping in taxonomy schema to resolve test suite drift checks. (#3, @antigravity)
