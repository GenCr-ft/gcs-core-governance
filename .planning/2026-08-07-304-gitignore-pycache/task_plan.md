---
docId: GOV-PLAN-304
title: Add a .gitignore so generated artifacts stop appearing as untracked noise
issue-id: 'GenCr-ft/gcs-core-governance#304'
created: 2026-08-07
status: approved
---

# [CODE] Add a .gitignore so generated artifacts stop appearing as untracked noise

## Objective

`scripts/__pycache__/` appears as untracked in every `git status` on this repo. That matters more
than tidiness: `git status` is how both humans and agents decide whether a tree is clean before
starting work, and permanent noise trains people to ignore it. It also risks a stray `git add -A`
committing bytecode.

## Premise correction

The issue said "**add** `__pycache__/` to `.gitignore`", implying an existing file to amend.
Verified at implementation: **this repo has no `.gitignore` at all.**

```console
$ git ls-files | grep -iE 'gitignore|gitattributes'
(empty)
$ ls -la .gitignore
ls: cannot access '.gitignore': No such file or directory
```

So the change is to **create** one. That is a larger decision than appending a line — a new
`.gitignore` can silently stop tracking things — so the "nothing tracked becomes ignored" property
is asserted rather than assumed.

## Scope — adopt the canonical template, do not mint a variant

**Revised after the round-1 adversary review (HIGH 3).** My first version was a hand-written 30-line
file tailored to this repo, mirroring `gcs-plt-gemop/.gitignore:17` for the bytecode rule. That was
wrong on principle: `gct-repo-template-standard/.gitignore` exists and says it *"should be the base
for all new repositories"*, and `gcs-plt-gemop` is a **consumer** of that template, not its source.
Minting a bespoke divergent config — in the repo whose entire purpose is preventing config drift,
under a header reading `SSoT Path: gcs-core-governance/.gitignore` — asserted an SSoT status the
file did not hold.

It also had a concrete consequence, which is the real argument: the hand-written version **omitted
`.env`**, and two standards this repo governs make that a MUST:

- `SEC-STAN-001` §3.3 (line 107): *"These files **MUST** be listed in the project's `.gitignore`
  file and **NEVER** committed"*
- `DEV-SPEC-003` §3 (line 57): *"This `.env` file MUST be included in the project's `.gitignore`
  file."*

This PR creates the repo's first and only `.gitignore` — the sole place those MUSTs can be
satisfied. Hand-rolling missed them; the canonical template satisfies both by construction. That is
the general case for adopting a template over curating a subset.

So `.gitignore` is now the canonical template **byte-identical** (sha256 `049729bc…`), preceded by a
provenance header and followed by a clearly-marked addendum holding one addition (`Thumbs.db`),
upstreamed as GenCr-ft/gct-repo-template-standard#45 so the addendum can eventually be dropped.

**No content path is ignored.** `reference-libraries/`, `.planning/` and every Markdown document
remain fully tracked — re-verified against the larger template (AC-3 below).

### Why `.planning/` is not ignored — corrected

My original justification said *"the reusable SSoT linter at `@v1.3.2` lints it"*. That is **false
on three independently checkable counts**, and it was sitting in a `status: approved` governance
document:

1. This repo has no `ssot-compliance.yml` caller workflow — `.github/workflows/` contains only
   `agent-context-parity.yml`, so the reusable SSoT linter never runs here at all.
2. `reusable-ssot-linter.yml@v1.3.2` contains **zero** occurrences of `planning`.
3. This repo's `.pre-commit-config.yaml` explicitly **excludes** `.planning/` from all four SSoT
   linters via the `ssot_exclude` anchor (line 128).

The decision is still right, for a different reason: `.planning/` holds **tracked** files (6,
including this plan), so ignoring it would break the tracked-plan convention. The workspace
convention question remains open in gcs-project-management#533.

## Verification

| AC | Check | Result |
|---|---|---|
| AC-1 | `__pycache__` is ignored | `scripts/__pycache__/x.pyc` → `.gitignore:39:__pycache__/` ✓ |
| AC-1 | a `.pyc` inside it is ignored | matched by the same rule ✓ |
| AC-2 | `git status` no longer lists it | with the directory and a `.pyc` present, `git status --porcelain` shows only `?? .gitignore` ✓ |
| AC-3 | **no currently-tracked file becomes ignored** | `git ls-files \| git check-ignore --stdin` → empty, exit 1, across all tracked files — **re-run against the canonical template** ✓ |
| — | governed `.env` MUSTs satisfied | `.env` → `:180`, `.env.local` → `:181`, `.env.production.local` → `:182` ✓ |
| — | canonical block unmodified | sha256 of the embedded template matches `gct-repo-template-standard/.gitignore` ✓ |
| — | markdownlint (this plan file) | `markdownlint-cli@0.45.0 --config .markdownlint.yaml` → clean ✓ |

Two `git check-ignore` behaviours worth recording, because one is a false negative and the other is
the reason the AC-3 check is trustworthy:

- **False negative on bare directories.** I first ran the AC-1 check *before* creating the directory
  and it reported "not ignored". `git check-ignore` cannot match a trailing-slash pattern against a
  path it cannot see is a directory, so the *check* was invalid, not the rule. That failure mode
  reads exactly like a broken rule.
- **Directory patterns *do* match nested paths through `--stdin`** — verified explicitly (`lib/`
  matches `lib/foo.py`, `docs/_build/` matches `docs/_build/a.html`). This matters because AC-3
  depends on it: if `--stdin` silently failed to match directory patterns, AC-3's empty result would
  be vacuous rather than reassuring. Given the canonical template is ~200 lines with many
  directory patterns, that had to be probed rather than assumed.

## Governance-scope note

Per `GOV-STANDARD-008` §3 (line 132): *"The linter **MUST** parse and respect the `.gitignore` file
located at the root of any repository it scans. Any file or directory matching a pattern in
`.gitignore` is considered out of scope for SSoT validation."*

So in this repo a `.gitignore` pattern is not housekeeping — it **defines SSoT validation scope**.
Recorded in the file's own header so a future editor knows adding a line is a governance change.

One residual risk, accepted rather than fixed: the canonical template's directory patterns are
unanchored, so they match at any depth, and `reference-libraries/` is vendored upstream content
synced wholesale. A future sync containing a path segment named `lib/`, `var/`, `target/` or
`htmlcov/` would be silently untracked *and* silently de-scoped from SSoT validation. Nothing matches
today. Root-anchoring would remove the risk but would stop those patterns matching legitimately
nested build output, so it is a genuine trade-off — raised for decision in
gct-repo-template-standard#45 rather than resolved unilaterally here, since anchoring in this repo
alone would recreate exactly the divergence HIGH 3 objected to.

## Isolation

This repo had 5 dirty paths from in-flight WI-288 work (3 modified governance docs, 2 untracked).
None were touched; the work was done in a separate worktree so the working tree is left as found.

`gft branch create` branches from the repo's **current HEAD**, which here was
`feat/issue-288-gem-domain-registry` rather than `main`. Checked rather than assumed:
`git merge-base --is-ancestor 9d41ac1 origin/main` → true, and `git log origin/main..9d41ac1` → 0
commits, so the base is clean. In a repo whose checked-out branch is *not* already merged, that same
command would silently drag another WI's commits into the PR.

## Steps

- [x] Confirm the gap and the `gcs-plt-gemop` asymmetry still hold
- [x] Discover the repo has no `.gitignore` — correct the issue's premise
- [x] Verify the branch base is an ancestor of `origin/main`
- [x] Create a `.gitignore`; assert no tracked file becomes ignored (AC-3)
- [x] Prove the rule works with the directory actually present
- [x] Adversary PR review round 1 (mandatory §4.1) — 0 CRITICAL / 4 HIGH / 4 LOW
- [x] HIGH 3 → replace the bespoke file with the canonical template + marked addendum
- [x] HIGH 2 → `.env` MUSTs now satisfied (a consequence of HIGH 3's fix, not a separate patch)
- [x] HIGH 4 → replace the false `.planning/` justification with the real one
- [x] HIGH 1 → fix MD040 in this file; run the repo's pinned markdownlint before committing
- [x] LOW → CHANGELOG entry, plan frontmatter `title`/`created`, `.active_plan` pointer
- [x] LOW → unanchored-pattern risk recorded and routed upstream (#45)
- [ ] Adversary PR review round 2; **human merge**

## What the round-1 review changed about how I work here

Four HIGH findings, and the pattern across them is that I verified my *implementation* carefully
(AC-3 was genuinely well-tested) while leaving my *justifications* unverified. HIGH 4 was a citation
to a mechanism that does not exist in this repo; HIGH 3 mirrored a downstream consumer while claiming
canonical status. Both would have read as authoritative to the next person.

HIGH 1 is the plainest lesson: the repo pins `markdownlint-cli@0.45.0` in `.pre-commit-config.yaml`
and lints `.planning/**`, and I committed a file that fails it. Running the repo's own pinned gate
before committing would have caught it in seconds. Its presence is evidence I did not.
