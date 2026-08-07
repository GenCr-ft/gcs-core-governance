---
docId: GOV-PLAN-304
issue-id: 'GenCr-ft/gcs-core-governance#304'
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

```
$ git ls-files | grep -iE 'gitignore|gitattributes'
(empty)
$ ls -la .gitignore
ls: cannot access '.gitignore': No such file or directory
```

So the change is to **create** one. That is a larger decision than appending a line — a new
`.gitignore` can silently stop tracking things — so the file is deliberately minimal and the
"nothing tracked becomes ignored" property is asserted rather than assumed.

## Scope

Creates `.gitignore` with rules for artifacts this repo actually produces: Python bytecode (from
`scripts/`), local virtualenvs, pytest/coverage output, and OS/editor cruft. Mirrors
`gcs-plt-gemop/.gitignore:17` for the bytecode rule, which is the asymmetry the issue reported.

**No content path is ignored.** `reference-libraries/`, `.planning/` and every Markdown document
remain fully tracked. `.planning/` is deliberately *not* ignored here — the reusable SSoT linter at
`@v1.3.2` lints it, and the workspace convention question is still open (gcs-project-management#533).

## Verification

| AC | Check | Result |
|---|---|---|
| AC-1 | `__pycache__` is ignored | `git check-ignore -v scripts/__pycache__` → `.gitignore:13:__pycache__/` ✓ |
| AC-1 | a `.pyc` inside it is ignored | `…/probe.cpython-312.pyc` → matched by the same rule ✓ |
| AC-2 | `git status` no longer lists it | with the directory and a `.pyc` present, `git status --porcelain` shows only `?? .gitignore` ✓ |
| AC-3 | **no currently-tracked file becomes ignored** | `git ls-files \| git check-ignore --stdin` → empty ✓ |

A false negative on the way: I first ran the AC-1 check *before* creating the directory and it
reported "not ignored". `git check-ignore` cannot match a trailing-slash pattern against a path it
cannot see is a directory, so the check was invalid rather than the rule. Re-run with the directory
present, both paths match. Worth recording — that failure mode reads exactly like a broken rule.

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
- [x] Create a minimal `.gitignore`; ignore only generated artifacts
- [x] Assert no tracked file becomes ignored (AC-3)
- [x] Prove the rule works with the directory actually present
- [ ] Adversary PR review (mandatory §4.1); PR; **human merge**
