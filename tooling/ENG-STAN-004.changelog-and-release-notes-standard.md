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
This standard is what workspace `AGENTS.md` Traceability Rule 6 refers to. Where an older
statement of that rule differs, this standard governs. Related: `ENG-STAN-001` (versioning) and
`PRO-STAN-001` (Definition of Done: "CHANGELOG.md updated if the change is user-facing").

## 1. File

1. Every repository listed in the workspace `AGENTS.md` Repo Index MUST have a root `CHANGELOG.md`.
2. `## [Unreleased]` MUST be the first version section. Released versions follow it, newest first.
3. A version heading MUST read `## [X.Y.Z] - YYYY-MM-DD`, with the date in ISO 8601. An em dash
   is accepted as the separator, since released headings are not rewritten. A pulled version keeps
   its heading with `[YANKED]` appended after the date.
4. Version headings SHOULD link to their tag compare range (link references at the end of the file).

## 2. Sections

1. Only these six type headings are allowed, in this order: `Added`, `Changed`, `Deprecated`,
   `Removed`, `Fixed`, `Security`.
2. Each type heading MUST appear **at most once** per version section. Add to the existing heading.
   Never open a second one.
3. A type heading MUST NOT be empty. An `[Unreleased]` section with no type headings is valid.

## 3. Which changes get an entry

An entry is REQUIRED for a **consumer-visible** change: behaviour, public API, CLI commands and
flags, configuration or schema, documented content that readers act on, deprecations, removals,
security fixes (including security dependency bumps), and anything breaking.

An entry MUST NOT be written for: refactors, tests, formatting, planning or memory files,
generated re-renders, a repository's own CI configuration, and dependency bumps with no
behaviour change.

A PR with no consumer-visible change is exempt when its Conventional Commit type is `ci`, `test`,
`refactor`, `style`, `build` or `chore`, or when it carries the `changelog:skip` label. The type
exemption is a default and is void when the change is in fact consumer-visible. Two examples: a
`build(deps)` security bump, and a `ci` change in a repository whose product is CI workflows
(`gcd-shared-actions`). Those PRs MUST carry an entry. The author owns that judgement, and PR
review checks it.

## 4. Entry format

```text
- <What changed, in the user's terms>. (#<PR>, @<author>)
```

1. A PR adds at most one entry per type heading. A follow-up PR to an unreleased entry edits that
   entry and keeps its original suffix.
2. The description, excluding the suffix, MUST be a single line of **at most 200 characters**.
   The suffix is exactly `(#<PR>, @<author>)`, with one PR and one author (the PR author). Issue,
   design and impl references go in the PR body, which the PR number links.
3. The entry is added **after** the PR is opened, so the number is real and never predicted.
4. Describe the outcome, not the implementation. For a fix, describe the symptom the user saw,
   not the cause.
5. The entry MUST NOT contain rationale, measurements, investigation history, file lists, or
   emphasis (`*`, `_`, `**`). Code spans are allowed. Put the rest in the PR body.
6. A breaking change starts with `BREAKING:` and names the required action.

Bad: an actual fleet entry of 880 characters, opening with emphasis.

```text
- **`gft doctor` now emits the `skills-duplicates` row its docstring has promised since
  ENG-ADR-088 §6: one skill name, one definition.** Nothing verified the deployed library, so …
  (#1129, issue #1122, design #1124, impl #1125, @loigallain)
```

Good:

```text
- `gft doctor` reports skills that are defined more than once. (#1129, @loigallain)
```

A re-pin of a repository's own CI caller to a new shared-actions tag gets **no entry**. It is a
`ci:` change, and the readers of that repository are not affected by it.

## 5. Release

1. On release, `[Unreleased]` is renamed to the new version and date, and an empty
   `## [Unreleased]` is opened above it.
2. Output generated from commits is a draft. It MUST be curated to this standard and MUST NOT
   replace the section as a commit-log dump.
3. The bump follows SemVer from the Conventional Commit range: `feat` → MINOR; `fix` and `perf`
   → PATCH; `!` or `BREAKING CHANGE` → MAJOR. Below `1.0.0`, `ENG-STAN-001` §3.4 applies.
   Automation is GenCr-ft/gcd-shared-actions#223.

## 6. Release notes

Release notes (the GitHub Release body) are a curated summary of **one** version's changelog
section, for readers who will not open the diff.

1. Title: `<repo> vX.Y.Z - YYYY-MM-DD`.
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

| Rule | Enforced by | Status |
|---|---|---|
| §1–§2, §4.2, §4.5 (emphasis) | `changelog-linter` pre-commit hook: `[Unreleased]` fully, version headings file-wide | planned, GenCr-ft/gcd-ops-scripts#232 |
| §3 entry present or declared exempt | `gft pr preflight` changelog check | planned, GenCr-ft/gcs-plt-tools#1246 |
| §3 void exemptions, §4.1, §4.3–§4.6, §6 | PR review | in force |

Rollout: a repository enables `changelog-linter` only after its `[Unreleased]` conforms
(GenCr-ft/gcs-project-management#614). Released sections written before this standard are not
rewritten.
