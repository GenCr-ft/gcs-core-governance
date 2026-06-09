## **Chapter 6: Game System Architecture (Templates and Examples)**

* **Objective:** Provide concrete, reusable, and **scalable** architectural blueprints for the most common game systems. These templates are designed to ensure robustness, testability, and clear separation of concerns, speeding up initial development and long-term maintenance.
* **Detailed Plan:**
  * **6.1. Player Controller (Composition & State-Driven)**
    * **Philosophy:** The "Player" is not one giant script. It's an *assembly* of components coordinated by a central "brain." This applies the **Composition over Inheritance** pattern (Chapter 4).
    * **Input Management:**
      * Use the InputMap exclusively. **Never** hard-code key checks (e.g., Input.is\_key\_pressed(KEY\_W)).
      * **Why:** This allows for easy remapping in an options menu.
      * **Contextual Input:** The Player.gd "brain" script should be responsible for enabling/disabling \_process\_input() on its components. For example, when a UI menu is open, the PlayerMovementComponent's input processing should be disabled, but the PlayerMenuComponent's should be enabled.
    * **Architecture (State Machine \+ Components):**
      * **Player.gd (The "Brain" \- e.g., on a CharacterBody3D):**
        * Manages the State Machine (from Chapter 4).
        * Holds references to its components (e.g., @export var movement: PlayerMovementComponent).
        * Reads input from the InputMap (e.g., Input.get\_vector(...)).
        * Passes "intent" (like a desired move vector) to the relevant component. It *commands* its components.
      * **PlayerMovementComponent.gd (The "Muscles" \- Node):**
        * A component script (e.g., on a child Node).
        * **Does NOT** read input. It only has public functions like move(vector: Vector3).
        * Contains all move\_and\_slide() logic, gravity calculations, jump physics, etc.
        * Can be tested in isolation by just calling move().
      * **PlayerAnimationComponent.gd (The "Face" \- Node):**
        * A component script that holds the AnimationPlayer node.
        * **Does NOT** know about input or physics.
        * Listens for signals from the "Brain" or State Machine (e.g., state\_machine.state\_changed) to play the correct animations.
    * **Code Template (Conceptual):**
      \# Player.gd (The Brain)
      @export var movement\_component: PlayerMovementComponent
      @export var state\_machine: StateMachine

      func \_physics\_process(delta):
          \# 1\. Let the current state handle logic (like input)
          state\_machine.update(delta)

          \# 2\. Get intent from the state
          var move\_intent \= state\_machine.get\_move\_intent()

          \# 3\. Command the "muscles"
          movement\_component.move(move\_intent)

      \# PlayerMovementComponent.gd (The Muscles)
      var velocity: Vector3
      func move(move\_intent: Vector3):
          \# Apply gravity, handle physics
          velocity.x \= move\_intent.x \* speed
          \# ...
          move\_and\_slide()

  * **6.2. Inventory System (Resource-Based & Decoupled)**
    * **Resource\-Based Architecture (The "Why"):**
      * We define items as Resource files (.tres).
      * **Why:** Resources are serializable (easy to save/load), shareable (multiple enemies can drop the *exact same* "Health Potion" resource), and lightweight data containers.
      * **ItemData.gd (extends Resource):**
        * @export var name: String
        * @export var description: String
        * @export var texture: Texture2D
        * @export var stackable: bool \= false
        * @export var max\_stack\_size: int \= 1
    * **Separation of Data / Logic / UI (Model-View-Controller):**
      * **Inventory.gd (The "Model" \- extends Resource):**
        * This is the *data*. It's a Resource itself, so it can be saved/loaded as one file.
        * @export var slots: Array\[ItemData\]
        * Contains no logic, just the data.
      * **InventoryManager.gd (The "Controller" \- Autoload/Singleton):**
        * This is the *logic*. It's the only script allowed to *modify* the Inventory resource.
        * var player\_inventory: Inventory (loads the resource)
        * signal inventory\_updated
        * func add\_item(item: ItemData)
        * func remove\_item\_from\_slot(slot\_index: int)
        * **Why:** By centralizing logic here, no other script can illegally add an item. All UI elements just call InventoryManager.add\_item(...).
      * **InventoryUI.gd (The "View" \- Scene):**
        * This is the *presentation*. It's a Control node.
        * It knows *nothing* about how to add/remove items.
        * **On \_ready():** InventoryManager.inventory\_updated.connect(redraw\_ui)
        * **redraw\_ui():** Reads the data from InventoryManager.player\_inventory and instances/updates the InventorySlotUI scenes.
        * **When a slot is clicked:** slot.gui\_input.connect(\_on\_slot\_clicked)
        * **\_on\_slot\_clicked():** InventoryManager.use\_item\_in\_slot(slot\_index)
    * **Code Example:** Provide scripts for these three key components, demonstrating the signal-based connection.
  * **6.3. Artificial Intelligence (AI) (FSM vs. Behavior Trees)**
    * **Comparison of Approaches:**
      * **Finite State Machines (FSM):**
        * **Best For:** Simple, *reactive* AI. (e.g., Zombie: Idle \-\> Sees player \-\> Chase \-\> In range \-\> Attack).
        * **Pros:** Very easy to implement (see Chapter 4), easy to debug.
        * **Cons:** Becomes "state spaghetti" very quickly. Does not scale to complex logic (e.g., a guard who needs to patrol, check doors, sound an alarm, *and* attack).
      * **Behavior Trees (BT):**
        * **Best For:** Complex, *goal-oriented* AI.
        * **Pros:** Extremely scalable and reusable. You can build complex behaviors from simple "leaf" nodes.
        * **Cons:** Harder to implement from scratch. Less intuitive at first.
    * **FSM Template:**
      * Show the BaseState.gd pattern again.
      * Provide PatrolState.gd (moves between Path3D points, checks a detection Area3D), ChaseState.gd (uses NavigationAgent3D to move to player.global\_position), and AttackState.gd (stops moving, plays animation, triggers a HitboxComponent).
    * **Behavior Tree Template:**
      * Explain the core node types:
        * Selector (?: "OR"): Tries each child in order until one *succeeds*. (e.g., Attack Player? OR Chase Player? OR Patrol?)
        * Sequence (-\>: "AND"): Runs each child in order. If *any* fail, the whole sequence fails. (e.g., Is Player in Range? \-\> Is Attack Cooldown Ready? \-\> Perform Attack)
        * Action: A "leaf" node that performs an action (e.g., MoveToPlayer.gd).
        * Condition: A "leaf" node that checks a condition (e.g., IsPlayerInRange.gd).
    * **Navigation:** Clarify that both FSM and BT are *decision-making* systems. The *movement* itself should almost always be handled by NavigationServer and NavigationAgent3D / NavigationAgent2D. The decision-making layer *sets the destination* for the navigation agent.
  * **6.4. User Interface (UI) Management (Decoupled & Stack-Based)**
    * **Themes:**
      * Define a single, master Theme resource (.tres).
      * Set this theme in **Project \> Project Settings \> GUI \> Theme \> Custom**.
      * **Why:** This ensures *every* Button, Label, and Panel in the entire game is styled identically by default. Avoids styling nodes one-by-one.
    * **Menu Architecture (The "Scene Stack Manager"):**
      * **The Problem:** get\_tree().change\_scene\_to\_file() is slow, reloads everything, and is a poor way to manage "pop-up" menus (like a pause screen).
      * **The Solution:** An Autoload singleton (UIManager.gd).
      * **UIManager.gd:**
        * var scene\_stack: Array \= \[\]
        * var current\_scene \= null
        * func push\_screen(scene\_path: String):
          1. Instances the new UI scene (e.g., options\_menu.tscn).
          2. Adds it as a child of the UIManager (which is in the root viewport).
          3. If current\_scene exists, call current\_scene.hide().
          4. Set current\_scene \= new\_scene and push it to the stack.
        * func pop\_screen():
          1. Call current\_scene.queue\_free().
          2. Pop it from the stack.
          3. current\_scene \= scene\_stack.back()
          4. If current\_scene is not null, call current\_scene.show().
      * **Why:** This allows you to stack menus (e.g., MainMenu \-\> OptionsMenu \-\> RemapKeyMenu) and just "pop" back, or to show a PauseMenu "on top" of the GameScene without breaking it.
    * **Decoupling (The SignalBus):**
      * The UI must **never** directly access game nodes (e.g., get\_node("/root/Game/Player")).
      * **BAD:** PauseButton.gd \-\> get\_tree().paused \= true and get\_node("Player").set\_physics\_process(false).
      * **GOOD (Announce, Don't Command):**
        * PauseButton.gd \-\> SignalBus.emit\_signal("game\_paused").
        * Player.gd \-\> SignalBus.game\_paused.connect(\_on\_game\_paused) \-\> set\_physics\_process(false).
        * GameWorld.gd \-\> SignalBus.game\_paused.connect(\_on\_game\_paused) \-\> get\_tree().paused \= true.
      * **Why:** The UI *announces* that the pause button was pressed. It doesn't know *what* happens. This allows you to test the UI scene completely separately from the game.
