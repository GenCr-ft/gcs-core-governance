## **Chapter 2: Project Structure**

* **Objective:** Define a single, standardized folder structure so that every team member knows *exactly* where to find and place files. This is not just about "avoiding clutter"; it's about reducing cognitive load, improving scalability, and enabling efficient collaboration.
* **Detailed Plan:**
  * **2.1. The Two Philosophies: "Group by Type" vs. "Group by Feature"**
    * Before presenting a template, we must decide *how* we organize.
    * **"Group by Type" (Classic):** All scripts go in /scripts/, all scenes in /scenes/. This is simple to understand initially but scales poorly. As the project grows, /scripts/ becomes a "junk drawer" of 100+ unrelated files, and working on a single feature (e.g., the Player) requires editing files in 4 different folders.
    * **"Group by Feature" (Recommended):** All files related to a single feature (scene, script, model, textures) are co-located in the *same* folder. This is the **Principle of Locality**. It is far more scalable and maintainable.
  * **2.2. Template A: The "Group by Type" Structure (To Avoid)**
    * This is a common structure for small projects or game jams. **We will not use this** as it does not scale.
    * **Example:**
      /project.godot
      /assets/      \# Raw resources (models, textures, sounds)
      /scenes/      \# Game scenes (player.tscn, enemy.tscn, level\_01.tscn)
      /scripts/     \# GDScript scripts (player.gd, enemy.gd, level\_01.gd)
      /ui/          \# UI-specific scenes and resources
      /addons/      \# Plugins and addons

    * **Why we avoid it:** High friction. To work on the "Player", you must jump between /scenes, /scripts, and /assets. It's impossible to see all related files at once. Deleting a feature is a nightmare.
  * **2.3. Template B: The "Group by Feature" Structure (Our Standard)**
    * **This is our mandatory project structure.** It organizes the project vertically by feature, not horizontally by file type.
    * **Example:**
      /project.godot
      /features/        \# All self-contained game entities
        /player/
          player.tscn
          player.gd
          player\_model.glb
          mat\_player\_albedo.tres
          tex\_player\_albedo.png
        /enemy\_goblin/
          goblin.tscn
          goblin.gd
          goblin\_model.glb
        /item\_health\_potion/
          health\_potion.tscn
          health\_potion.gd
          ico\_health\_potion.png
      /systems/         \# Global managers (Autoloads)
        /inventory\_system/
          inventory\_system.gd
          inventory\_data.gd       (a Resource script)
        /signal\_bus/
          signal\_bus.gd
      /levels/          \# Scenes that assemble features (e.aws, level\_01.tscn)
      /ui/              \# Global UI elements (main\_menu.tscn, hud.tscn)
      /tests/           \# Unit and integration tests
      /addons/          \# Plugins and addons

    * **Justification:**
      * **Low Cognitive Load:** When you open /features/player/, *everything* related to the player is right there.
      * **Easy Refactoring:** Deleting a feature? Just delete its folder.
      * **Version Control:** Two developers working on different features (e.g., "Player" and "Goblin") will *never* have a Git conflict, as they are working in different directories. In Template A, they would both be editing the /scripts/ folder, causing potential conflicts.
  * **2.4. Scene Organization (The "Prefab" Principle)**
    * **"One Scene per Concept" (The Prefab Pattern):** This is the *most important* concept. A scene file (.tscn) is Godot's version of a "prefab."
      * **Example:** player.tscn is a scene. level\_01.tscn *instances* player.tscn. You do *not* build the player directly inside level\_01.tscn.
      * **Why:** If you update player.tscn (e.g., add a new attack animation), that change is *automatically* reflected in every level that instances it.
    * **"Level" Scenes vs. "Entity" Scenes:**
      * **Entity Scenes** (e.g., player.tscn, goblin.tscn, health\_potion.tscn) are the "building blocks." They are self-contained and should be runnable on their own for testing.
      * **Level Scenes** (e.g., main\_menu.tscn, level\_01.tscn) are the "assemblies." Their job is to instance and arrange the Entity scenes to build a playable experience.
    * **Scene Inheritance (Use Sparingly):**
      * **What it is:** You can create a new scene that *inherits* from a base scene (e.g., goblin.tscn inherits from base\_enemy.tscn).
      * **When to use it:** When you have many variations of a *very* similar thing.
      * **Example:** BaseEnemy.tscn has a HealthComponent and a StateMachine. Goblin.tscn inherits from it and just adds a specific model and stats.
      * **Warning:** Prefer *composition* (adding nodes as children) over inheritance where possible.
  * **2.5. Script Organization**
    * **If using Template B (Our Standard):** This is simple. **Scripts live in the feature folder they belong to.**
      * player.gd lives in /features/player/.
      * goblin.gd lives in /features/enemy\_goblin/.
    * **Global Scripts (Autoloads / Systems):**
      * Scripts that manage a global system (e.g., InventorySystem, SignalBus) should live in their own folder under /systems/.
      * These are typically registered as "Autoloads" in the Project Settings.
    * **class\_name:** As mentioned in Chapter 1, always use class\_name at the top of your script (e.g., class\_name PlayerController) to make it a globally accessible type.
