## **Chapter 3: Version Control with Git**

* **Objective:** Standardize the use of Git to enable smooth, asynchronous collaboration. This is not just a backup system; it is our primary tool for quality assurance, conflict avoidance, and maintaining a clean, understandable project history.
* **Detailed Plan:**
  * **3.1. The .gitignore File for Godot**
    * Provide a standard .gitignore template for Godot projects. This file is **not optional** and must be the first thing added to the repository.
    * **Template:**
      \# Godot 4+ project-specific files
      .godot/

      \# Sensitive information \- NEVER commit this
      export\_presets.cfg

      \# Exported builds \- We only version source code
      \*.pck
      \*.exe
      \*.dmg
      \*.html

    * **Explanation of Key Files:**
      * .godot/: This is the local project cache. It stores imported versions of assets specific to your machine. Committing this **will** cause constant, unresolvable merge conflicts. It must be ignored.
      * export\_presets.cfg: This file often contains sensitive API keys, keystore passwords, and other credentials. Committing this is a **major security breach**.
      * \*.pck, \*.exe: These are "built" products, not source code. Our repository stores the *source* that *creates* these files, not the files themselves.
  * **3.2. Git LFS (Large File Storage) \- NON-NEGOTIABLE**
    * **The Problem:** Git is designed for text (code). It performs *terribly* when tracking large binary files (textures, models, audio). Without LFS, our repository will become gigabytes in size, and cloning/pulling will take hours.
    * **The Solution:** We **must** use Git LFS to track large assets. LFS stores the large files on a separate server and places small text "pointers" in the Git repository.
    * **Procedure:**
      * Install Git LFS locally (git lfs install).
      * Define which files to track using .gitattributes. This file *must* be committed.
    * **.gitattributes Template:**
      \# Textures
      \*.png filter=lfs diff=lfs merge=lfs \-text
      \*.jpg filter=lfs diff=lfs merge=lfs \-text
      \*.exr filter=lfs diff=lfs merge=lfs \-text

      \# 3D Models
      \*.glb filter=lfs diff=lfs merge=lfs \-text
      \*.gltf filter=lfs diff=lfs merge=lfs \-text

      \# Audio
      \*.wav filter=lfs diff=lfs merge=lfs \-text
      \*.ogg filter=lfs diff=lfs merge=lfs \-text

  * **3.3. Branching Strategy (GitHub Flow)**
    * **main:** This branch is **always** stable and deployable. Direct commits are **forbidden**. Every merge into main is a potential release.
    * **feature/feature-name:** (e.g., feature/player-inventory, feature/quest-system)
      * All new development happens here.
      * Branched *from* main.
      * Merged *into* main via a Pull Request when complete and reviewed.
    * **fix/bug-name:** (e.g., fix/inventory-crash, fix/typo-main-menu)
      * For fixing bugs.
      * Branched *from* main, merged *into* main via a Pull Request.
    * *(Note: GitHub Flow replaces the earlier Simplified GitFlow used in this guide. The studio standard — GCS-ARCH-001 §1, GCS-GUIDE-201 §2.1 — mandates GitHub Flow for all projects, including Godot game clients.)*
  * **3.4. The Pull Request (PR) & Code Review Process**
    * **Rule:** No one merges their own code directly into main.
    * **Workflow:**
      1. You finish work on your feature/player-inventory branch.
      2. You open a **Pull Request (PR)** (or Merge Request) to merge your branch *into* main.
      3. You assign at least **one other team member** to review your code.
      4. The reviewer checks for bugs, logic errors, and (critically) adherence to the Style Guide (Chapter 1 & 2).
      5. Once the PR is approved, it can be merged into main.
    * **Why:** This is our single most important quality gate. It prevents broken code from entering main and forces knowledge sharing.
  * **3.5. Commit Message Conventions**
    * We **must** use the "Conventional Commits" format. This is not for fun; it allows us to auto-generate changelogs and makes the project history readable.
    * **Format:** type(scope): message
    * **Types:** feat (new feature), fix (bug fix), refactor (code change, no behavior change), style (formatting, no code change), docs (documentation), test (adding tests).
    * **Examples (Good):**
      * feat(player): Add jump functionality and coyote time
      * fix(ui): Correct inventory button alignment on 16:10 screens
      * refactor(physics): Optimize all player raycasts into a single function
      * docs(git): Update branching strategy in the bible
    * **Examples (Bad):**
      * fix bug (Useless. What bug?)
      * wip (Doesn't say what work was done)
      * player stuff (Not specific, no type)
  * **3.6. Conflict Management (Especially .tscn Files)**
    * **The Problem:** Scene files (.tscn) are text, but they are not human-readable. They contain auto-generated IDs and complex resource links. A merge conflict in a .tscn file is **extremely difficult** and dangerous to resolve in a text editor.
    * **Rule 1: Communicate.** The best way to fix a conflict is to *prevent* it. Announce in Slack/Discord: "**I am now editing level\_01.tscn**."
    * **Rule 2: Small, Frequent Commits.** Do not "hold" changes to a shared scene for days. Commit and push your changes often so others can git pull.
    * **Procedure for Resolving a .tscn Conflict:**
      1. **NEVER** try to fix it in your text editor. You will break the scene.
      2. Abort the merge immediately: git merge \--abort.
      3. Communicate with the team member you are conflicting with.
      4. **Decide who merges.** One person will be responsible.
      5. That person will git pull (or git checkout their-branch \-- their-file.tscn) to get the other person's version, *overwriting their own*.
      6. Then, they must *manually re-apply their own changes* inside the Godot editor.
      7. Finally, they commit the (now manually merged) .tscn file.
