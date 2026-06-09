## **Chapter 1: Naming and Style Conventions**

* **Objective:** To establish a common language and strict, non-negotiable rules to ensure the readability, consistency, and long-term maintainability of all project code and assets.
* **Detailed Plan:**
  * **1.1. Introduction: The Importance of Consistency**
    * **Why a strict convention is non-negotiable:** Consistency directly reduces cognitive load. A developer's mental energy should be spent solving complex problems (game logic, algorithms), not deciphering *how* a variable is named or *where* a file might be located.
    * **The "Broken Windows" Effect:** A project without clear conventions quickly accumulates "code smells." One developer uses camelCase, another uses snake\_case, and a third uses no convention at all. This creates a high-friction environment where code becomes intimidating to modify, leading to bugs and technical debt.
    * **Impact on Onboarding:** A new team member can become productive within days, not weeks. The conventions act as a map, allowing them to navigate the project and understand its architecture "at a glance" instead of having to learn the personal idiosyncrasies of each original developer.
    * **Impact on Code Reviews:** Code reviews must focus on high-level concerns: logic, architecture, performance, and potential bugs. They must *not* be polluted by trivial, time-wasting comments like "Please rename this variable to snake\_case" or "This file is in the wrong folder." Adhering to this guide makes our review process efficient and valuable.
    * **Impact on Debugging:** Inconsistent naming can directly cause or hide bugs (e.g., PlayerHealth (a class property) and player\_health (a local variable) being used in the same function). A strict convention makes search tools (Ctrl+F, "Find in Files") 100% reliable.
  * **1.2. Conventions for GDScript**
    * **Classes and Files:** PascalCase (e.g., PlayerController.gd, EnemyAI.gd, InventorySystem.gd).
      * **Reason:** The filename *must* match the class\_name declared inside the script (e.g., class\_name PlayerController). This creates a clear 1:1 link between the file on disk and the type in the engine.
      * **class\_name Usage:** Use class\_name liberally. It registers your script as a global type within Godot, enabling you to use it for type hints in other scripts (e.g., var player: PlayerController).
    * **Variables and Properties:** snake\_case (e.g., move\_speed, current\_health, target\_node).
      * **Example (Good):** var max\_stamina: float \= 100.0
      * **Example (Bad):** var MaxStamina: float \= 100.0 (PascalCase is for types)
      * **Example (Bad):** var maxStamina: float \= 100.0 (camelCase is not used in GDScript)
      * **Example (Bad):** var f\_max\_stamina: float \= 100.0 (Hungarian notation is forbidden)
    * **Constants:** SCREAMING\_SNAKE\_CASE (e.g., MAX\_JUMP\_HEIGHT, GRAVITY\_FORCE, STATS\_FILE\_PATH).
      * **Reason:** This visually separates immutable, global-scope values from variables that can change state. When you see a SCREAMING\_CASE variable, you know it's safe to read from anywhere and that its value will not change during runtime.
    * **Functions and Methods:** snake\_case (e.g., calculate\_damage(), play\_animation(), update\_state()).
      * **Signal Callbacks:** Must *always* start with \_on\_ followed by the Node name and the signal name. Godot's editor helps with this when connecting signals via the UI.
      * **Example (Good):** \_on\_player\_hitbox\_body\_entered(body: Node3D)
      * **Example (Good):** \_on\_attack\_timer\_timeout()
      * **Reason:** This convention makes it immediately obvious that a function is an "entry point" that is called by the engine's signal system, not called manually within your own code.
    * **"Private" Functions and Variables:** \_ prefix (e.g., \_internal\_state, \_update\_ui(), \_target\_position).
      * **Important:** GDScript does not have true "private" methods. The \_ is a universal and respected convention that signals: "This property or method is an internal implementation detail of this class. It **must not** be called or modified from outside. It can change or be removed at any time without warning."
      * **Reason:** This promotes encapsulation (designing classes as "black boxes") and makes the public API (functions without \_) clean and easy to understand.
    * **Signals:** Named in the past tense, describing the event that *just occurred*.
      * **Example (Good):** signal health\_changed(old\_value: int, new\_value: int)
      * **Example (Good):** signal player\_died
      * **Example (Bad):** signal change\_health (This sounds like a command or function)
      * **Example (Bad):** signal on\_death (Ambiguous)
      * **Reason:** A signal is a *notification*, not a *command*. Naming it in the past tense makes its purpose clear. Other objects *listen* for player\_died; they do not *tell* the player to die.
    * **Static Typing:** **Mandatory for all code.**
      * **Reason:** Static typing is our primary line of defense against bugs. It allows the editor to detect type-mismatch errors before the game even runs. It enables far superior auto-completion and makes the code self-documenting (you know what a function expects without reading its source). In Godot 4, it also allows the compiler to generate more optimized code.
      * **Example (Bad \- Dynamic):**
        \# This code is fragile. What is 'target'? A Node? A Vector?
        \# What does this function return?
        var speed \= 100
        func set\_target(target):
            var new\_pos \= target.global\_position
            return new\_pos

      * **Example (Good \- Static):**
        \# This code is robust. We know 'target' must be a Node3D.
        \# We know the function returns a Vector3.
        \# The editor will warn us if we pass a string or an int.
        var speed: int \= 100
        func set\_target(target: Node3D) \-\> Vector3:
            var new\_pos: Vector3 \= target.global\_position
            return new\_pos

  * **1.3. Conventions for Scenes and Nodes**
    * **Scene Files (.tscn):** snake\_case (e.g., main\_menu.tscn, level\_01.tscn, player.tscn, goblin\_enemy.tscn).
      * **Reason:** Scene files are *resources*. They are assets on disk, just like textures (.png) or materials (.tres). We name all resources in snake\_case to clearly distinguish them from PascalCase *classes* and *nodes*.
    * **Nodes in the Scene Tree:** PascalCase (e.g., Player, UserInterface, TileMap, CameraPivot, HitboxArea).
      * **Reason:** Nodes are instances of Classes (whether built-in like MeshInstance3D or scripted like PlayerController). Naming them in PascalCase reinforces this concept.
      * **The % Operator:** This convention makes the "Unique Node" (%) operator incredibly powerful and readable.
      * **Example (Good \- Robust):** var player\_node \= %Player
      * **Example (Bad \- Fragile):** var player\_node \= get\_node("Player")
      * **Benefit:** If you rename the Player node to MyPlayer in the scene tree, the %Player reference will be *automatically updated* by the editor. The get\_node("Player") reference will *break* and cause a runtime crash. **Always prefer % references.**
  * **1.4. Conventions for Resources**
    * **Folder Structure:** We will use a **"Group by Feature" (Principle of Locality)** structure, *not* a "Group by Type" structure.
      * **Example (Bad \- Group by Type):**
        /textures/player\_albedo.png
        /models/player.glb
        /scripts/player.gd
        /scenes/player.tscn

        (This is bad because a single feature, "Player", is scattered across four different folders.)
      * **Example (Good \- Group by Feature):**
        /features/player/player.tscn
        /features/player/player.gd
        /features/player/player\_albedo.png
        /features/player/player\_model.glb
        /features/enemy\_goblin/goblin.tscn
        /features/enemy\_goblin/goblin.gd

        (This is good because all files related to the "Player" are in one place. It is much easier to work on, maintain, and version control.)
    * **File Naming:** type\_name\_variant.ext. Use prefixes to identify file types at a glance in the file system.
      * **tex\_**: Textures (tex\_player\_albedo.png, tex\_rock\_normal.png)
      * **mat\_**: Materials (mat\_water\_surface.tres, mat\_enemy\_goblin.tres)
      * **mdl\_**: 3D Models (mdl\_player\_rig.glb, mdl\_sword.glb)
      * **scn\_**: Scenes (scn\_player.tscn, scn\_level\_01.tscn) (Optional, but useful if a "feature" folder contains many scenes)
      * **sfx\_**: Sound Effects (sfx\_jump.wav, sfx\_weapon\_fire.ogg)
      * **mus\_**: Music (mus\_main\_menu.ogg)
      * **fnt\_**: Fonts (fnt\_ui\_main.ttf)
      * **anim\_**: Animation Libraries (anim\_player\_locomotion.tres)
      * **Reason:** Prevents ambiguity. player.png and player.tscn could be confusing. tex\_player.png and scn\_player.tscn are perfectly clear.
  * **1.5. Code Formatting**
    * **Maximum Line Length:** **120 characters.**
      * **Reason:** This ensures that code is readable on a single monitor without horizontal scrolling. It is essential for side-by-side code diffs during code reviews.
    * **Comments and Docstrings:**
      * Use \#\# (double hash) for multi-line docstrings that describe *what* a function does, its parameters, and what it returns. This is read by the editor for tooltips.
      * Use \# (single hash) for single-line comments *inside* a function to explain *why* a specific piece of logic exists.
      * **Example:**
        \#\# Plays the attack animation and enables the hitbox.
        \#\# \[param attack\_name\] The string name of the animation to play.
        func perform\_attack(attack\_name: String):
            \# We must reset the hitbox first, otherwise 'body\_entered'
            \# might not fire again for a persistent body.
            %Hitbox.disable()
            $AnimationPlayer.play(attack\_name)
            %Hitbox.enable()

    * **Indentation:** **Use tabs, not spaces.**
      * **Reason:** This is the default setting for Godot and ensures consistency. It also allows developers to set their own tab-width visually without changing the file's content.
    * **Vertical Whitespace:** Use single blank lines to separate logical blocks of code inside a function. Do not use multiple blank lines.
