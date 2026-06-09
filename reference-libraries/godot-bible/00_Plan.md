# **The Godot Bible \- Development Reference**

## **Introduction**

* **1\. Purpose of this Document**
  * Establish a Single Source of Truth for all Godot development practices within the team.
  * Accelerate onboarding for new members by providing them with a comprehensive guide.
  * Ensure the quality, maintainability, and long-term performance of our projects.
* **2\. How to Use This Guide**
  * This document is a living guide: it is intended to be updated as we discover better practices.
  * Use as a reference during Code Reviews to justify modification requests.
  * Consult before starting development on a new major system.
* **3\. Our Development Philosophy**
  * **Pragmatism First:** Use Godot's tools (nodes, signals) as a priority. Do not over-architect.
  * **Clarity \> Brevity:** Write readable code, even if it's more verbose.
  * **Performance by Design:** Think about optimization from the beginning, not at the end.
  * **Data-Oriented vs. Object-Oriented:** Understand when to use the node-based (OO) approach and when to switch to an ECS/Data-Oriented approach (for performance).

## **Part 1: Foundations and Best Practices**

* **Chapter 1: Naming and Style Conventions**
  * **Objective:** Make the code instantly readable and predictable.
  * **GDScript:**
    * Classes/Files: PascalCase (e.g., PlayerController.gd).
    * Variables & Functions: snake\_case (e.g., move\_speed, calculate\_damage()).
    * Constants: SCREAMING\_SNAKE\_CASE (e.g., MAX\_HEALTH).
    * Signals: Past Tense (e.g., health\_changed, player\_died).
    * "Private" Variables: \_ prefix (e.g., \_current\_target).
    * Exported Variables: @export var node\_name: NodeType.
    * **Mandatory Static Typing:** Enforce static typing for all variables, function arguments, and return types.
  * **Scenes & Nodes:**
    * Scene Files (.tscn): snake\_case (e.g., level\_01.tscn, main\_menu.tscn).
    * Node Names in the Tree: PascalCase (e.g., Player, CameraPivot, MainUI).
  * **Resources (.tres, .png, etc.):**
    * type\_name\_variant (e.g., tex\_player\_albedo.png, mat\_rock\_01.tres, sfx\_jump\_01.wav).
    *
* **Chapter 2: Project Structure**
  * **Objective:** Know where to find and where to place any file without thinking.
  * **Standard Directory Structure:**
    * /scenes/: .tscn scenes.
      * /scenes/levels/: Main level scenes.
      * /scenes/characters/: Player, enemy scenes.
      * /scenes/props/: Interactive objects, decor scenes.
      * /scenes/ui/: Menu screens, HUD scenes.
    * /scripts/: .gd scripts.
      * Mirror the /scenes/ structure or group by feature (e.g., /scripts/systems/inventory/).
    * /assets/: Raw imported resources.
      * /assets/graphics/ (3D models, textures, sprites).
      * /assets/audio/ (music, sound effects).
      * /assets/fonts/.
    * /addons/: Plugins and external tools.
    * /tests/: Unit test scripts (see Chapter 16).
  * **Principle of Locality:** Resources specific to one scene (e.g., scripts for a complex enemy) can be stored in the same folder as the scene.

* **Chapter 3: Version Control with Git**
  * **Objective:** Enable smooth and secure collaboration on code and assets.
  * **.gitignore File:** Provide the official template for Godot (ignore .godot/, export\_presets.cfg, etc.).
  * **Git LFS (Large File Storage):**
    * **Mandatory** for large binary assets (.png, .glb, .wav).
    * Define which file types to track (e.g., git lfs track "\*.png").
  * **Branching Strategy (GitHub Flow):**
    * main: Always stable and deployable. Direct commits are forbidden.
    * feature/feature-name: Branch for a new feature, branched from and merged back into main.
    * fix/bug-name: Branch for an urgent fix, branched from and merged back into main.
  * **Pull Request (PR) / Merge Request (MR) Process:**
    * Any change to develop or main must go through a PR.
    * Define the minimum number of required approvals (e.g., 1 or 2).
  * **Commit Messages:** Adopt Conventional Commits (e.g., feat(player): Add jump ability, fix(ui): Correct main menu button alignment).

## **Part 2: Design Patterns and Architecture**

* **Chapter 4: Fundamental Godot Patterns**
  * **Objective:** Use Godot's idiomatic patterns to solve common problems.
  * **The Signal Bus (Event Bus / Autoload Singleton):**
    * **Problem:** Decouple distant systems (e.g., the UI must react to the player's health).
    * **Solution:** An Autoload SignalBus.gd script that centralizes global signals.
    * **Anti-Pattern:** Don't overuse it. For local interactions, prefer classic node signals.
  * **State Machine:**
    * **Problem:** Manage complex behaviors (AI, player, menus).
    * **Solution:** A parent node (Player) that manages child nodes representing each state (IdleState, WalkState). Only the active state is in the tree (add\_child(new\_state)).
  * **Composition (Nodes as Components):**
    * **Problem:** Avoid complex inheritance.
    * **Solution:** A Player is composed of children: HealthComponent, InputComponent, SpriteManager.
  * **Object Pooling:**
    * **Problem:** Constantly instantiating and freeing scenes (bullets, explosions) is expensive.
    * **Solution:** Create a BulletPool that keeps bullet scenes in memory and reuses them (hide/show, move).
* **Chapter 5: The ECS (Entity Component System) Architecture**
  * **Objective:** Understand when and why to abandon the node-based architecture for performance.
  * **Philosophy:** Data-Oriented Design (DOD) vs. Object-Oriented Programming (OOP).
  * **ECS (Entity, Component, System):**
    * **Entity:** A simple ID.
    * **Component:** Pure data (e.g., PositionComponent { x, y }).
    * **System:** Pure logic that operates on sets of components (e.g., MovementSystem iterates over all PositionComponent and VelocityComponent).
  * **When to Use It?**
    * **YES:** For thousands of similar entities (RTS, bullet-hell, simulations).
    * **NO:** For general game logic, UI, or unique "hero" characters.
  * **Implementation:** Use a recognized library (e.g., Godot-ECS) or a lightweight framework.
* **Chapter 6: Game System Architecture (Templates and Examples)**
  * **Objective:** Provide "ready-to-use" blueprints for recurring systems.
  * **Player Controller:**
    * Separate input gathering (InputComponent that reads the InputMap) from action (MovementComponent that applies physics).
    * Use a State Machine (Chap. 4\) to manage states (Idle, Run, Jump).
  * **Inventory System (Based on Resource):**
    * **ItemData.tres (Resource):** Defines an item's properties (name, icon, description, stats).
    * **InventorySlot.gd (Node):** Manages an inventory slot (contains ItemData \+ quantity).
    * **Inventory.gd (Node):** Manages the collection of InventorySlots.
    * **Advantage:** Resources are easy to save, load, and share.
  * **Artificial Intelligence (AI):**
    * **State Machine:** Simple and effective for basic enemies (Patrol, Chase, Attack).
    * **Behavior Trees:** For complex and modular logic.
* **Chapter 07: Networked Multiplayer Architecture**
  * **Objective:** Build robust and secure multiplayer games.
  * **Godot's API:** MultiplayerAPI, MultiplayerSpawner, MultiplayerSynchronizer.
  * **RPCs (Remote Procedure Call):** Understand @rpc("authority", "call\_local"), etc.
  * **Architecture: Authoritative Server**
    * **The Golden Rule:** The client only sends its inputs. The server simulates the game and sends back the state. **NEVER TRUST THE CLIENT.**
    * **Advantages:** Secure against cheating.
    * **Disadvantages:** More complex, requires a dedicated server.
  * **Handling Latency:**
    * **Client-Side Prediction:** The client simulates its own actions immediately.
    * **Server Reconciliation:** The client corrects its position when the server state arrives, if there is a discrepancy.
    * **Interpolation:** Smooth the movement of other players to avoid jitter.
* **Chapter 08: Architecture for Modding and Plugins**
  * **Objective:** Allow the community to extend the game.
  * **Levels of Modding:**
    * Level 1: Data replacement (JSON, textures).
    * Level 2: Content addition (.tscn for new items, enemies).
    * Level 3: Logic addition (.gd for new behaviors).
  * **Creating a Modding API:**
    * Expose functions and signals via an ModdingAPI Autoload.
    * **Sandboxing:** Discuss the security risks of loading external scripts (.gd) and strategies to mitigate them.
  * **Loading System:** The game must scan a mods/ folder on startup and load the found resources and scripts.
* **Chapter 09: Communication and Community Systems**
  * **Objective:** Manage interaction between players and between the studio and players.
  * **Player-to-Player Communication:** Chat (via RPCs), ping/emote system.
  * **Studio-to-Player Communication:** Message of the Day (MOTD) loaded from a server, in-game feedback form.
  * **Backend Infrastructure:**
    * Discuss the need for a simple web API (e.g., Flask, FastAPI) or a service (Firebase, PlayFab, Ludiq) to manage player accounts, leaderboards, persistent inventories.

## **Part 3: Rendering, Physics, Animation, and Procedural Worlds**

* **Chapter 10: Voxel Worlds and Procedural Geometry**
  * **Objective:** Build large and dynamic worlds.
  * **Data Structures:**
    * Division into "Chunks" (pieces of the world).
    * Storage (3D Array, Octrees for optimization).
  * **"Meshing" Algorithms:**
    * Greedy Meshing (for Minecraft-style cubes).
    * Marching Cubes (for smooth, organic terrains).
  * **Generation and Streaming:**
    * **MANDATORY Threading:** World generation and meshing must be done in separate threads to avoid freezing the game.
    * Load/unload chunks around the player.
  * **Level of Detail (LoD) and Transvoxel:**
    * Techniques to display simplified versions of distant chunks and manage transitions without "seams."
* **Chapter 11: Advanced Physics Simulation**
  * **Objective:** Master and extend the physics engine.
  * **Raycasting:**
    * The most versatile tool: ground detection (is\_on\_floor()), line of sight for AI, shooting (hitscan).
  * **Custom Gravity:**
    * Use Area3D to create gravity zones (e.g., planetary gravity).
  * **Fluids and Complex Effects:**
    * Discuss 'simulated' (SPH, expensive) vs. 'stylized' (shaders, physics zones) approaches.
  * **Optimization:** When to use CharacterBody vs. RigidBody vs. StaticBody.
* **Chapter 12: Texture and Shader Management**
  * **Objective:** Optimize VRAM usage and create custom materials.
  * **Textures:**
    * **VRAM Compression:** Use Godot's importer to compress textures (reduces VRAM usage, not disk size).
    * **Atlases:** Group 2D sprites to reduce draw calls.
  * **Shaders:**
    * **Visual Shaders:** An excellent entry point for artists and beginners.
    * **Shader Language (GDShader):**
      * Syntax (similar to GLSL).
      * Shader types: spatial (3D), canvas\_item (2D), particle.
      * Key functions: vertex(), fragment(), light().
    * **uniform:** How to expose parameters (colors, textures, sliders) in the Inspector.
* **Chapter 13: Light and Shadow Management** *(file not yet created — [Chapter 13 — Pending])*
  * **Objective:** Create performant visual moods.
  * **Light Types:** DirectionalLight3D (sun), OmniLight3D (point), SpotLight3D (cone).
  * **Global Illumination (GI):**
    * **LightmapGI (Baked):** For static scenes. High quality, maximum performance.
    * **SDFGI / VoxelGI (Real-Time):** For dynamic scenes. More expensive, but reacts to changes.
  * **Shadow Optimization:**
    * Shadows are very expensive.
    * Use Cascades for the DirectionalLight.
    * Disable shadows for small or distant objects.
  * **Environments:** Role of WorldEnvironment, Sky, ReflectionProbe.
* **Chapter 14: Animation, Rigging, and Cinematics**
  * **14.1. Godot's Animation Tools:**
    * AnimationPlayer: The Swiss Army knife. Animate any property, call functions, play sounds.
    * AnimationTree: The brain. For characters, manages transitions, blending, and complex animation logic.
  * **14.2. Rigging and Skinning (2D and 3D):**
    * **3D Pipeline:** Best practices for exporting from Blender (glTF 2.0). Importance of "Apply All Transforms."
    * Importing: Check Skeleton3D and BoneAttachment3D (for attaching objects, like a sword, to a bone).
    * **2D Pipeline:** Using Skeleton2D and Bone2D to deform sprites (Cutout animation).
  * **14.3. Character Animation:**
    * **AnimationTree (State Machine):** Manage states (Idle, Walk, Run, Attack).
    * Smooth transitions: cross-fading between animations.
    * BlendSpace1D/2D: For movement (e.g., blending Walk and Run based on speed).
    * **Root Motion vs. In-Place:**
      * **In-Place (Recommended):** The animation plays on the spot, the CharacterBody3D handles movement.
      * **Root Motion:** The animation's movement displaces the character. Useful for very precise animations (e.g., climbing).
  * **14.4. Procedural Animation and Inverse Kinematics (IK):**
    * SkeletonIK3D: The node for implementing IK.
    * Use cases: Adjust feet to uneven ground, make a character aim at a target with their head or weapon.
  * **14.5. Creating Cinematics:**
    * Use a main AnimationPlayer to orchestrate the scene.
    * Animate tracks: camera properties, other characters' AnimationPlayers, and call method tracks (Call Method Tracks) to trigger events.

## **Part 4: Quality, Testing, and Optimization**

* **Chapter 15: Anti-Patterns (What to Avoid)**
  * **Objective:** Identify common "traps" that harm maintainability.
  * **The "Mega-Script":** A 2000-line script that does everything. **Solution:** Decompose into components (child nodes).
  * **The get\_node() Hell:** Using hard-coded paths (get\_node("../../../Player")). **Solution:** Use @export var, signals, or groups.
  * **The Overloaded \_process:** Putting heavy calculations or unnecessary checks in \_process or \_physics\_process. **Solution:** Use signals, Timers, or Threads.
  * **The Abusive Singleton:** Putting all game logic into Autoloads, creating a "big ball of mud."
  * **The UI That Thinks:** The UI should only display data and emit signals. It must not store game state (e.g., player health).
* **Chapter 16: Test-Driven Development (TDD) with Godot**
  * **Objective:** Write more reliable code and avoid regressions.
  * **Tool:** Use **GUT (Godot Unit Test)**, the standard testing framework.
  * **What to Test?**
    * **YES:** Pure logic (algorithms, stat calculations, inventory management). Classes that do not inherit from Node.
    * **NO:** The visual aspect, animation.
  * **Red-Green-Refactor Cycle:**
    * **Red:** Write a test that fails.
    * **Green:** Write the minimum code for the test to pass.
    * **Refactor:** Improve the code without breaking the test.
  * **Continuous Integration (CI):** Configure a CI (e.g., Gitlab CI, Github Actions) to run tests automatically on every push.
* **Chapter 17: General Debugging and Optimization**
  * **Objective:** Know how to identify and fix bugs and performance bottlenecks.
  * **Debugging Tools:**
    * The integrated debugger (breakpoints, variable inspection).
    * Remote Scene Monitor (inspect the scene tree of a running game).
  * **Profiling Tools (Optimization):**
    * **The Profiler:** To find the GDScript functions that take the most time.
    * **The Monitor:** To monitor draw calls, VRAM usage, and physics.
  * **Optimization Strategies:**
    * **Culling:** Frustum Culling (automatic), Occlusion Culling (manual, for 3D).
    * **Batching:** Use MultiMesh or RenderingServer to display thousands of identical objects.

## **Appendices**

* **A. Useful Code Snippets**
  * Complete SignalBus.gd example.
  * Basic StateMachine script example.
  * Basic save/load function.
* **B. Code Review Checklist**
  * Does the code follow naming conventions?
  * Is the code fully typed?
  * No get\_node() with hard-coded paths?
  * Is the logic decomposed, or is it a "Mega-Script"?
  * Are new systems covered by tests (if applicable)?
* **C. Glossary of Terms.**
  * Definition of: RPC, ECS, TDD, CI, Batching, Culling, etc.
* **D. External Links and Resources.**
  * Links to the official Godot documentation, best tutorials, and tools (GUT, etc.).
