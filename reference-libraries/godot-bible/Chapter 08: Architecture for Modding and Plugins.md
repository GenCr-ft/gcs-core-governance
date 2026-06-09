## **Chapter 8: Architecture for Modding and Plugins**

* **Objective:** Define a clear, secure, and maintainable strategy and architecture to make our games moddable. This will increase the game's lifespan, foster community engagement, and allow for user-generated content, while protecting the core game and the user's system.
* **Detailed Plan:**
  * **8.1. Philosophy: Why Modding is a Core Feature, Not an Add-on**
    * **The Asset:** Modding creates longevity, community ownership, and a long tail of "free" content that keeps the game relevant. It must be planned from day one.
    * **Our Core Principle: "Expose, Isolate, and Validate"**
      * **Expose:** Provide a clear and stable API for modders.
      * **Isolate:** The mod must *never* be able to crash the core game or access the user's computer.
      * **Validate:** All data and code from a mod must be treated as untrusted and validated before use.
    * **Level 1: Data Mods (Safest)**
      * **What it is:** Replacing or adding simple data.
      * **Examples:** Modifying item stats via JSON/CSV files, replacing textures (.png), audio files (.ogg), or models (.glb).
      * **Risk:** Low. The game loads this data *as data*, not as code.
      * **Our Strategy:** The game's data (e.g., ItemDatabase) must load from res:// first, then scan user://mods/ for "override" files and merge them.
    * **Level 2: Content Mods (Medium Risk)**
      * **What it is:** Adding new, self-contained game entities.
      * **Examples:** A modder creates a new SuperSword.tscn scene. This scene can contain its own meshes, particles, and *can even reference core game scripts* (like BaseItem.gd).
      * **Risk:** Medium. If the modded scene contains a *new, custom* script, it becomes a Level 3 risk. We must clearly define what a "content-only" mod can contain.
    * **Level 3: Script Mods (High Risk)**
      * **What it is:** Adding *new logic* via GDScript files (.gd).
      * **Examples:** A mod that adds a new "weather system," "quest logic," or custom AI behavior.
      * **Risk:** High. An arbitrary GDScript has access to the OS class (filesystem, command execution) and get\_node("/root/") (can manipulate *any* part of the game, including singletons, to cheat or break things). **This is the primary security threat.**
  * **8.2. Designing a Stable and Secure Modding API**
    * **The ModAPI Autoload (The Façade Pattern):**
      * **Concept:** We will create *one* Autoload singleton (e.g., ModAPI.gd). This is the *only* "door" a mod should ever use to talk to the game.
      * **Why:** This is a "façade." It decouples the mod from the game's internal structure. We can completely refactor our InventoryManager or Player script, and the mod *will not break* as long as we maintain the public-facing functions in ModAPI.
    * **DOs and DON'Ts of API Design:**
      * **DO: Expose safe functions:**
        \# ModAPI.gd
        \# Safe: The function validates and processes the data.
        func register\_new\_item(item\_resource: ItemData):
            if not \_is\_item\_data\_valid(item\_resource): return
            CoreGame.ItemDatabase.register\_mod\_item(item\_resource)

      * **DON'T: Expose direct node access:**
        \# ModAPI.gd
        \# UNSAFE: This gives the mod total control over the player.
        func get\_player\_node() \-\> CharacterBody3D:
            \# NEVER DO THIS.
            return get\_tree().get\_node("/root/Game/Player")

    * **Using Signals (The Primary Interaction Method):**
      * The ModAPI will act as a *public signal bus* for all major game events.
      * **Example Flow:**
        1. **Internal Game:** Player.gd emits player\_took\_damage(10).
        2. **API Façade:** A core game script listens: Player.player\_took\_damage.connect(ModAPI.on\_player\_took\_damage).
        3. **Public Signal:** ModAPI.gd simply re-emits the signal: signal player\_took\_damage(player, amount).
        4. **Mod Script:** A mod can safely connect: ModAPI.player\_took\_damage.connect(my\_mod\_function).
      * **Why:** The mod *never* knows the Player.gd node exists. It only knows about ModAPI.
  * **8.3. Loading and Sandboxing Techniques**
    * **Loading Data/Content (The Loader):**
      * **Mod Folder:** All mods are loaded from user://mods/.
      * **Process:**
        1. On game start, scan user://mods/ for sub-directories.
        2. Each sub-directory *must* contain a mod.json (see 8.4).
        3. Parse mod.json to get mod info.
        4. Load any Level 1 data (e.g., item overrides).
        5. Load any Level 2 scenes (load(mod\_scene\_path)).
        6. Handle Level 3 scripts (see below).
    * **The Security Threat: Sandboxing GDScript (Level 3\)**
      * **The Problem:** Godot has *no* built-in sandbox. A load()-ed .gd script has *full access*.
      * **Forbidden Actions:** We must prevent mods from accessing:
        * OS class (file system, execute commands).
        * get\_node("/root") or get\_tree() (access to singletons, UI, etc.).
        * Networking classes (HTTPRequest, MultiplayerAPI).
      * **Strategy 1: Veto (Safest):** We disallow Level 3 (Script) mods entirely. Many successful games do this.
      * **Strategy 2: Curation:** Mods must be manually approved (e.g., Steam Workshop). Not scalable.
      * **Strategy 3: Static Analysis (Our Preferred Method):**
        1. When the ModLoader finds a script, it *does not* load() it immediately.
        2. It opens the .gd file as a FileAccess and reads its content as a String.
        3. It runs a "pre-parser" (e.g., Regex) to check for *forbidden keywords*:
           * "OS."
           * "get\_node(\\"/root")"
           * "get\_tree()"
           * "HTTPRequest"
        4. If any forbidden string is found, the mod is *rejected* and not loaded.
        5. If it passes, *then* we load() and execute its "main" function.
      * **Note:** This is not 100% foolproof (e.g., obfuscation like get\_node("/" \+ "root")) but stops 99.9% of accidental or low-effort malicious code.
  * **8.4. Structure and Distribution of a Mod**
    * **Standard Mod Folder Structure:** This must be documented for modders.
      /user://mods/
          /my\_cool\_mod/
              mod.json
              /scenes/
                  new\_sword.tscn
              /scripts/
                  sword\_logic.gd
              /textures/
                  new\_sword\_albedo.png

    * **The Manifest File (mod.json):**
      * **Purpose:** This file tells the ModLoader what the mod is, who made it, and what to load.
      * **Example mod.json:**
        {
          "name": "My Cool Mod",
          "version": "1.1.0",
          "author": "ModderName",
          "description": "Adds a cool new sword and a script that prints to the console.",
          "api\_version": "1.0", // Checks against our ModAPI version
          "level\_1\_overrides": {
            "items": "res://data/new\_items.json"
          },
          "level\_2\_scenes": \[
            "res://scenes/new\_sword.tscn"
          \],
          "level\_3\_script": "res://scripts/main.gd" // The \*one\* entry-point script to run
        }

    * **"Hello World" Mod Example (Tutorial for Modders):**
      1. Create the folder my\_first\_mod with mod.json (above).
      2. Create main.gd with the following content:
         \# main.gd
         \# This function is called by ModLoader after it passes static analysis
         func \_mod\_init():
             print("My First Mod is loading\!")
             \# Connect to the stable API
             ModAPI.player\_took\_damage.connect(\_on\_player\_hit)

         func \_on\_player\_hit(player\_node, amount):
             print("Mod detected player was hit for %s damage\!" % amount)

      3. (Game runs, ModLoader loads this, and the message will print when the player is hit).
