---
docId: ENG-STAN-004
title: Changelog and Release Notes Standard
version: 1.0.0
authors: [Studio Lead]
reviewers: [Studio Lead]
creation_date: '2026-10-20'
last_updated_date: '2026-10-20'
language: en
summary: Mandatory format, scope and length rules for CHANGELOG.md entries and release notes in
  every GenCr@ft repository. Approved via GenCr-ft/gcs-project-management#613.
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: engineering-and-architecture
  doc-type: standard
  intended-audience: [contributors, ai-agents, devops-team]
  security-classification: l2_confidential
  keywords: [changelog, release-notes, keep-a-changelog, semver, traceability]
---

# ENG-STAN-004 — Changelog and Release Notes Standard

A changelog is written for the people who **use** a repository, not for its reviewers. It says
*what changed for them*. The *why* and the *how* go in the PR body and the issue. Keywords
MUST/SHOULD/MAY follow RFC 2119.

Baseline: [Keep a Changelog 1.0.0](https://keepachangelog.com/en/1.0.0/) and
[SemVer 2.0.0](https://semver.org/spec/v2.0.0.html). Release-note practice follows
[How to write great release notes](https://releaseglow.com/blog/how-to-write-great-release-notes).

## 1. File

1. Every governed repository MUST have a root `CHANGELOG.md`.
2. `## [Unreleased]` MUST be the first version section. Released versions follow it, newest first.
3. A version heading MUST read `## [X.Y.Z] - YYYY-MM-DD`, with the date in ISO 8601. An em dash
   in place of the hyphen is accepted, since released headings are not rewritten. A pulled
   version keeps its heading with `[YANKED]` appended after the date.
4. Version headings SHOULD link to their tag compare range (link references at the end of the file).

## 2. Sections

1. Only these six type headings are allowed, in this order: `Added`, `Changed`, `Deprecated`,
   `Removed`, `Fixed`, `Security`.
2. Each type heading MUST appear **at most once** per version section. Add to the existing heading.
   Never open a second one.
3. A version section MUST NOT contain an empty type heading.

## 3. Which changes get an entry

An entry is REQUIRED for a **consumer-visible** change: behaviour, public API, CLI commands and
flags, configuration or schema, documented content that readers act on, deprecations, removals,
security fixes, and anything breaking.

An entry MUST NOT be written for: CI/workflow pins, refactors, tests, formatting, planning or
memory files, generated re-renders, and dependency bumps with no behaviour change (security
bumps excepted).

A PR with no consumer-visible change declares it in one of two ways. Its Conventional Commit
type is `ci`, `test`, `refactor`, `style`, `build` or `chore`, or the PR carries the
`changelog:skip` label. `gft pr preflight` accepts either as a pass of its changelog check.

## 4. Entry format

```text
- <What changed, in the user's terms>. (#<PR>, @<author>)
```

1. One entry per PR at most. A follow-up PR to an unreleased feature edits that entry; it does
   not add a new one.
2. The description, excluding the suffix, MUST be a single line of **at most 200 characters**.
   The suffix is exactly `(#<PR>, @<author>)`. Issue, design and impl references go in the PR
   body, which the PR number links.
3. Describe the outcome, not the implementation. For a fix, describe the symptom the user saw,
   not the cause.
4. The entry MUST NOT contain rationale, measurements, investigation history, file lists, chains
   of issue references, or markdown emphasis. Put those in the PR body.
5. A breaking change starts with `BREAKING:` and names the required action.

Bad: an actual fleet entry of 880 characters, opening with markdown emphasis.

```text
- **`gft doctor` now emits the `skills-duplicates` row its docstring has promised since
  ENG-ADR-088 §6: one skill name, one definition.** Nothing verified the deployed library, so …
  (#1129, issue #1122, design #1124, impl #1125, @loigallain)
```

Good:

```text
- `gft doctor` reports skills that are defined more than once. (#1129, @loigallain)
```

A re-pin of a CI workflow to a new shared-actions tag gets **no entry**. It is a `ci:` change
and its readers are the pipeline, not the repository's users.

## 5. Release

1. On release, `[Unreleased]` is renamed to the new version and date, and an empty
   `## [Unreleased]` is opened above it. Commit-log dumps MUST NOT replace the curated section.
2. The bump follows SemVer from the Conventional Commit range (`feat` → MINOR, `fix` → PATCH,
   `BREAKING CHANGE` → MAJOR). Automation is GenCr-ft/gcd-shared-actions#223.

## 6. Release notes

Release notes (the GitHub Release body) are a curated summary of **one** version's changelog
section, for readers who will not open the diff.

1. Title: `<repo> vX.Y.Z — YYYY-MM-DD`.
2. A MAJOR or MINOR release with `Added` entries MUST open with a summary of **at most 3
   sentences and 60 words**. The summary gives the headline improvement, the problem it solves,
   and where to try it. A PATCH release MAY omit it.
3. Breaking changes, deprecations and removals come **first**. Each states the required action
   and any deadline, and says when no action is needed.
4. Then group the rest as **New** (`Added`), **Improved** (`Changed`), **Fixed**, **Security**.
   Lead with the user benefit. Minor fixes MAY be grouped into one line.
5. One or two sentences per item. A reader must be able to scan the notes in under two minutes.
6. Release notes MUST NOT contain commit-log dumps, internal-only changes, or AI attribution
   footers.

## 7. Enforcement

| Rule | Enforced by |
|---|---|
| §1–§2, §4.2, §4.4 (emphasis) | `changelog-linter` pre-commit hook (`gcd-ops-scripts`), on `[Unreleased]`; §1 on the whole file |
| §3 entry present or declared exempt | `gft pr preflight` changelog check |
| §4.1, §4.3, §4.4 (content), §6 | PR review |

Released sections written before this standard are not rewritten.
