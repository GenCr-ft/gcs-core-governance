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

1. This repo has no `ssot-compliance.yml` caller workflow — on `origin/main`, `.github/workflows/`
   holds `agent-context-parity.yml` and `governance-integrity.yml`, and neither invokes the reusable
   SSoT linter (`governance-integrity.yml` runs a vendored `verify_governed_paths.py` that globs
   paths). So the reusable SSoT linter never runs here at all. *(I originally wrote "contains only
   `agent-context-parity.yml`" — true on this branch's base, false on the merge target.)*
2. `reusable-ssot-linter.yml@v1.3.2` contains **zero** occurrences of `planning`.
3. This repo's `.pre-commit-config.yaml` **excludes** `.planning/` from all four SSoT linters — three
   via the `&ssot_exclude` anchor (defined line 128, aliased at 142 and 149) and the naming-linter at
   line 135 via an **inlined literal copy** of the same pattern rather than the anchor. All four do
   exclude it; the mechanism is not uniform, which matters if someone edits the anchor expecting all
   four to follow.

The decision is still right, for a different reason: `.planning/` holds **tracked** files (6,
including this plan), so ignoring it would break the tracked-plan convention. The workspace
convention question remains open in gcs-project-management#533.

## Verification

| AC | Check | Result |
|---|---|---|
| AC-1 | `__pycache__` is ignored | `scripts/__pycache__/x.pyc` → `.gitignore:39:__pycache__/` ✓ |
| AC-1 | a `.pyc` inside it is ignored | matched by the same rule ✓ |
| AC-2 | `git status` no longer lists it | with the directory and a `.pyc` present, `git status --porcelain` shows only `?? .gitignore` ✓ |
| AC-3 | **no currently-tracked file becomes ignored** | `git ls-files \| git check-ignore --no-index --stdin` → empty, exit 1, across all **341** tracked files — re-run against the canonical template ✓ (the `--no-index` is load-bearing; see below) |
| — | governed `.env` MUSTs satisfied | `.env` → `:180`, `.env.local` → `:181`, `.env.production.local` → `:182` ✓ |
| — | canonical block unmodified | sha256 of the embedded template matches `gct-repo-template-standard/.gitignore` ✓ |
| — | markdownlint (this plan file) | `markdownlint-cli@0.45.0 --config .markdownlint.yaml` → clean ✓ |

### The AC-3 check I originally ran could not fail

`git check-ignore` consults the index by default and **never reports a tracked path**. So
`git ls-files | git check-ignore --stdin` — feeding it exactly and only tracked files — is
guaranteed to return empty with exit 1 no matter what `.gitignore` contains. It would have passed
against a `.gitignore` consisting of `*`.

Demonstrated in a scratch repo with three tracked files that all match ignore patterns:

```console
$ printf 'lib/\ndocs/_build/\n*.log\n' > .gitignore   # all three files below match
$ git ls-files | git check-ignore --stdin -v
EXIT=1                                                  # ← reports nothing
$ git ls-files | git check-ignore --no-index --stdin -v
.gitignore:2:docs/_build/   docs/_build/a.html
.gitignore:1:lib/           lib/foo.py
.gitignore:3:*.log          tracked.log
EXIT=0                                                  # ← reports all three
```

**The AC-3 property still holds** — re-run with `--no-index` on this branch: empty, exit 1, across
all 341 tracked files. But it had been certified by a test incapable of failing, which is worse than
not testing it, because it reads as verified.

Worth being precise about how I got this wrong, since it was not carelessness but mis-aimed rigour:
I *did* probe for vacuity, and probed the wrong axis. I tested whether directory patterns match
nested paths through `--stdin` (`lib/` → `lib/foo.py`, `docs/_build/` → `docs/_build/a.html`) — true,
and worth knowing — and concluded from it that AC-3 was trustworthy. Pattern matching was never the
risk. **Index consultation was, and it went unprobed.** So the earlier claim in this plan that
"AC-3 was genuinely well-tested" was inverted for its own headline example.

Also recorded, from the first attempt: **`git check-ignore` false-negatives on bare directories.** I
ran the AC-1 check before creating the directory and it reported "not ignored" — a trailing-slash
pattern cannot match a path git cannot see is a directory. The *check* was invalid, not the rule, and
that failure mode reads exactly like a broken rule.

The lesson generalising from both: for any verification whose pass condition is "no output",
construct a case that **must** produce output and confirm it does, before trusting the empty result.

## Governance-scope note

Per `GOV-STANDARD-008` **§6.1 "Linter Deployment: Centralized Reusable Workflow"**, item 3 (line 132):
*"The linter **MUST** parse and respect the `.gitignore` file located at the root of any repository it
scans. Any file or directory matching a pattern in `.gitignore` is considered out of scope for SSoT
validation."*

I first cited this as "§3", which is wrong: §3 is "Core Principles" (line 54) and says nothing about
`.gitignore`. The `3` I read as a section number is the **list ordinal** at the start of line 132,
inside §6.1 (heading at line 115, under §6 "Enforcement by Automation" at line 107). A citation error
of exactly the kind this repo exists to prevent, committed into this repo — and it had already been
exported into `gct-repo-template-standard#45`, which is corrected too.

So a `.gitignore` pattern here is not housekeeping — it **will define** SSoT validation scope, and
adding one is a governance change. Recorded in the file's own header.

**One honest qualification.** That de-scoping is **prospective in this repo, not yet operative.**
Nothing currently running here reads `.gitignore`: there is no `ssot-compliance.yml` caller workflow,
`governance-integrity.yml` runs a vendored `verify_governed_paths.py` that uses `glob.glob` rather
than gitignore semantics, and the pre-commit `gft verify` hooks receive staged paths directly. The
standard also scopes the linter's caller to *"every other studio repository"*. Stating the de-scoping
as already live would be the same over-claiming that produced the `@v1.3.2` error this PR already
fixed once.

One residual risk, accepted rather than fixed: the canonical template's directory patterns are
unanchored, so they match at any depth, and `reference-libraries/` is vendored upstream content
synced wholesale. A future sync containing a matching path segment would be silently untracked *and*
(prospectively) de-scoped from SSoT validation.

I originally named four such patterns. **Measured, the exposure is wider** — of 14 plausible future
`reference-libraries/` paths, **12** would match: `lib/`, `build/`, `target/`, `var/`, `dist/`,
`env/`, `instance/`, `htmlcov/`, `*.log`, `MANIFEST`, `override.tf`, `*.tfvars`. Only `docs/_build/`
(needs a literal `docs/` parent) and `/site` (root-anchored) fall outside. Nothing matches today.

Root-anchoring would remove the risk but would stop those patterns matching legitimately nested build
output — a genuine trade-off, raised in gct-repo-template-standard#45 rather than resolved
unilaterally, since anchoring here alone recreates the divergence HIGH 3 objected to.

**But "anchor or don't" was a false binary.** An *assertion* is not a divergence: a pre-commit or CI
check that `git ls-files | git check-ignore --no-index --stdin` is empty closes this permanently
without touching a single pattern, and would additionally have caught the tautological-verification
defect above. Neither my plan nor #45 considered it. Added to #45 as the recommended remedy.

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
- [x] Adversary PR review round 2 — 0 CRITICAL / 2 HIGH / 4 LOW, both HIGHs introduced by round 1's fix
- [x] R2 HIGH → `GOV-STANDARD-008` §3 corrected to §6.1 item 3, in all 3 files + #45
- [x] R2 HIGH → AC-3's verification needed `--no-index`; the original form could not fail
- [x] R2 LOW → re-sync instruction no longer destroys the header it lives in
- [x] R2 LOW → exposure re-measured (12 of 14, not 4); repo-local assertion option added to #45
- [x] R2 LOW → `.pre-commit-config.yaml` anchor vs inlined copy; `.github/workflows/` count on `origin/main`
- [x] R2 LOW → governance de-scoping marked prospective, not operative
- [ ] Adversary PR review round 3; **human merge**

## What two review rounds changed about how I work here

Six HIGH findings across two rounds. The pattern in round 1 was verifying the *implementation* while
leaving *justifications* unverified — HIGH 4 cited a mechanism that does not exist in this repo, HIGH 3
mirrored a downstream consumer while claiming canonical status.

**Round 2 sharpened that, and corrected my own account of it.** I had written here that "AC-3 was
genuinely well-tested". It was not: the command certifying it could not fail. So the honest version is
worse than the original diagnosis — it was not that I verified the implementation and skipped the
prose, it was that I verified the implementation *with a tautology* and skipped the prose. Both of
round 2's HIGHs were introduced by round 1's remediation, which matches the sibling PR
(`gcs-security-core#53`) where every round found defects in the previous round's corrections.

Three concrete practices, all earned:

1. **For any check whose pass condition is "no output", first construct a case that must produce
   output** and confirm it does. Otherwise "empty" is indistinguishable from "broken".
2. **Run the repo's own pinned gate before committing.** HIGH 1 was a `markdownlint-cli@0.45.0` MD040
   failure in a repo that pins and runs exactly that; its presence is evidence I did not run it.
3. **A citation's section number needs the same grep as its text.** The `GOV-STANDARD-008` text was
   byte-exact; the `§3` was a list ordinal I read as a heading. Byte-exactness of the quote gave false
   confidence about its location.
