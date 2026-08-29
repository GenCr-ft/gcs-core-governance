---
docId: GOV-PLAN-354
title: "[CODE] WI-354 — pin poetry in the tool-version SSoT"
issue-id: GenCr-ft/gcs-core-governance#354
status: complete
version: "1.0"
authors: [session-agent]
metadata:
  scope: workspace-ops
  domain: governance
  doc-type: plan
  lifecycle-stage: complete
---

# [CODE] WI-354 — pin poetry in the tool-version SSoT

Keystone of a five-part sweep. This WI adds the entry; the four consumers are separate issues,
because the entry alone changes nothing — see §4.

## 1. The measurement

`pip install poetry` on the self-hosted pool is a **no-op**:

```
Requirement already satisfied: poetry in
  /home/lgan/actions-runner/_work/_tool/Python/3.12.13/x64/lib/python3.12/site-packages (2.4.1)
```

Confirmed on disk in both tool-cache interpreters (`poetry-2.4.1.dist-info` under Python 3.11.16 and
3.12.13). So the version every Python job in the fleet runs is **ambient runner state nobody chose** —
the mechanism `gcs-plt-gemop#483` measured with PyYAML resolving to a 2019 build with known CVEs.

Three poetries exist on the developer workstation, at three versions:

| path | version | pinned by |
|---|---|---|
| `/usr/bin/poetry` — what `poetry` resolves to on PATH | 1.8.2 | Ubuntu distro package, Mar 2024 |
| `~/.gft-studio/.poetry/bin/poetry` | **2.1.3** | `gcs-plt-tools/onboard.sh:37`, hard-coded, with a `POETRY_MIN_MAJOR=2` floor that rejects the distro copy |
| CI runner tool-cache | **2.4.1** | nothing |

## 2. The version: 2.4.1, and why 2.1.3 was rejected on evidence

The first recommendation was 2.4.1 (zero CI delta). On finding `onboard.sh`'s deliberate 2.1.3 pin,
that was revised to 2.1.3 — align CI to the value a human had actually chosen — and approved.
**Testing then blocked it, before any code was written:**

```
$ ~/.gft-studio/.poetry/bin/poetry -C gcs-plt-tools install --dry-run --no-root
rc=1
pyproject.toml changed significantly since poetry.lock was last generated.
```

2.1.3 **cannot install `gcs-plt-tools`** — which holds **10 of the 13** call sites — while the ambient
2.4.1 installs it fine (that repo's `lint` job reaches step 9, so `Install dependencies` passes).

Root cause of the divergence, real rather than a version quirk: that repo's `poetry.lock` last changed
**2025-11-19** while its `pyproject.toml` changed **2026-06-12** — a **7-month-stale lock**. 2.1.3
refuses it; 2.4.1 is permissive enough to proceed. Pinning 2.1.3 would therefore require regenerating
that lock first, pulling 7 months of dependency updates into the platform CLI repo as a prerequisite.
Decision reverted to **2.4.1** with that measurement on the table, and re-approved.

**The probe was controlled**, which is why the result is trusted rather than suspected:

| control | result |
|---|---|
| must-pass — 2.1.3 against `gcd-ops-scripts` (`lock-version = "2.0"`) | `check --lock` rc=0 |
| must-fire — 2.1.3 against a pyproject mutated to add an unlocked dependency | rc=1, staleness detected |

Without the must-fire half, "2.1.3 rejects gcs-plt-tools" would have been equally consistent with a
broken probe.

## 3. The change

Two things in one file:

1. `poetry 2.4.1` appended to `tooling/ssot/.tool-versions-gft` — one added line among the pins.
2. **The header comment rewritten**, because adding poetry made it actively false. It said *"Read at
   runtime by gcd-onboarding-scripts get_ssot_tool_version()"* with no indication of **which** tools —
   so it reads as "this file governs the toolchain" when that function is called for exactly three
   entries (`02_installers.sh:414/422/430`). I made that inference myself earlier and published a
   wrong warning from it, since retracted. Leaving the comment would encode that error into the file
   for the next reader, so the new header names the consumer per tool and states plainly that poetry
   has none yet.

`.tool-versions-gft` is **not** a governed path — 0 occurrences in both
`governance/governed-paths.sha256` (32 entries) and `governed-paths.yaml` — so no baseline re-record is
needed. Checked rather than assumed, after `gcl-srv-authentication#171` where an edited file *was*
governed and produced drift that had to be separated from someone else's. Worth an observation on the
PR: the file whose whole purpose is to be the single authority for tool versions is not
integrity-protected while 32 policy documents are.

## 4. Why the entry alone changes nothing

Swept every repo: `.tool-versions-gft` is read only by `gcd-onboarding-scripts`
(`includes/01_helpers.sh` `get_ssot_tool_version`, called at `02_installers.sh:414/422/430` for
nodejs/python/opentofu) plus docs, plans and fixtures. **No CI workflow reads it, and no installer
requests poetry from it.** Inert on both sides until consumers exist:

| # | repo | issue | scope |
|---|---|---|---|
| 2 | `gcd-ops-scripts` | #175 | 1 CI call site |
| 3 | `gcs-plt-tools` | #976 | 10 CI call sites |
| 4 | `gct-service-template-py` | #49 | 3 CI call sites (template — propagates) |
| 5 | `gcd-ops-scripts` | #176 | linter rule asserting the copies agree |

Plus, folded in by the approved decision: **point `gcs-plt-tools/onboard.sh:37` at this entry** instead
of hard-coding, which moves developers 2.1.3 → 2.4.1 — a minor within Poetry 2.x, so no change to
`shell` / `export` / `--no-update` behaviour.

## 5. Acceptance

- The file contains `poetry 2.4.1`.
- The header names a consumer per tool and marks poetry as having none yet.
- No other pin is modified — the diff on the pin lines is exactly one added line.
- `test.sh`'s three parity verifiers still pass; none of them reads this file.

**Not claimed:** that anything now installs poetry 2.4.1. It does not, and §4 says so. Claiming
otherwise would be the "merged but inert" failure this studio keeps hitting, asserted rather than
avoided.

## 6. Related findings surfaced by this WI, all filed

- `gcs-plt-tools#977` — `poetry lock --no-update` ×3, removed in Poetry 2.0, **broken today**; plus
  `update_poetry_locks.sh` exists twice with diverged copies.
- `gcs-plt-architecture#92` — ENG-ADR-069 recommends `poetry shell`, removed from core in 2.0.
- `gcd-onboarding-scripts#269` — the tool-version SSoT does not govern poetry; two pins, two values.
- `gcs-plt-tools#978` — `gft self update` skips the reinstall when the repo is current but the install
  is stale, reporting success. Found while updating gft for this WI, and the reason gft was on 0.11.0
  against a tree declaring 0.13.2.
