## **Chapter 16: Test-Driven Development (TDD) with Godot**

* **Objective:** Implement a testing culture to ensure that the game's business logic is correct, robust, and does not regress over time. TDD isn't just about finding bugs; it's a design methodology that forces you to write small, modular, and decoupled code that is inherently testable. This process builds a "safety net" of tests, allowing you to refactor and add features aggressively without fear of breaking existing functionality.
* **Detailed Plan:**
  * **16.1. The Principles of TDD: Red-Green-Refactor**
    * **Explain the cycle:** This is the core loop of TDD. It provides a simple, repeatable, and powerful process for writing high-quality, proven-correct code. It's a discipline.
    * **1\. RED:** Write a small test for a *single piece* of functionality that *doesn't exist yet*. For example, test\_player\_cannot\_jump\_twice\_in\_mid\_air. Run your test suite. The test *must* fail (turn "Red"). This step is crucial: it validates that your test is *actually testing something*. If you write a test for new functionality and it passes, your test is broken or you're testing the wrong thing. A "Red" test proves the system is in the "broken" state you expect, and that your test is correctly wired up to detect it.
    * **2\. GREEN:** Write the *absolute minimum* amount of code necessary to make this one specific test pass (turn "Green"). This code might be "ugly," inefficient, or incomplete. For instance, to pass test\_player\_cannot\_jump\_twice\_in\_mid\_air, you might just add a simple if not is\_on\_floor(): return check at the start of your jump() function. The goal is *not* to write perfect code. The goal is to get back to a "passing" state as quickly as possible, proving your small piece of logic works. This is not the time to optimize or add bells and whistles.
    * **3\. REFACTOR:** Now that your tests are all passing, you have a safety net. You can confidently improve the code you just wrote, or the surrounding code, without fear of breaking existing functionality. This is where you clean up. You might look at the if not is\_on\_floor() check and decide to refactor it into a more robust State Machine. You can rename variables, extract a complex block of code into its own function, or optimize an algorithm. After each small refactor, you run the *entire test suite* again. If it stays "Green," you proceed. If it turns "Red," you know the *exact* change you just made broke something, and you can undo it and rethink, rather than introducing a bug you'll only find days later.
  * **16.2. Setting up Godot Unit Test (GUT)**
    * **Install and Configure:** GUT is the de-facto standard for testing in Godot. It's a plugin available from the Godot AssetLib or GitHub. You install it, enable it under Project \-\> Project Settings \-\> Plugins, and it adds a new "GUT" dock to your editor, which becomes your main testing control panel.
    * **Test Folder Structure:** A common practice is to create a top-level test/ directory in your project, parallel to res://. Inside this, you should mirror your main project structure. For example, a script at res://player/player\_stats.gd would have a corresponding test at test/unit/player/test\_player\_stats.gd. This makes it incredibly easy to find the test for any given script. Test scripts *must* be classes that inherit from gut.Test (or just Test if you use @tool).
    * **Configuration:** GUT provides a gut\_config.json file for project-wide settings. Here you can specify where your tests live, what directories to "shadow" (letting you right-click a script in res:// and jump to its test in test://), and define preload\_scripts that should be loaded before any tests run. This is also where you can configure command-line options, which is essential for integrating your tests into a CI/CD pipeline (e.g., GitHub Actions) to automatically run all tests whenever new code is pushed.
  * **16.3. What and How to Test?**
    * **Unit Tests vs. Integration Tests:** This is the most important distinction in testing.
      * A **Unit Test** tests a *single script or function* in total isolation. It should be "pure." It should not depend on the scene tree, other nodes, or even Godot's physics engine. You should test it by creating a .new() instance of the script, not by instancing a scene. These tests are extremely fast, 100% reliable, and easy to write.
      * An **Integration Test** tests *how multiple nodes or scenes work together*. It tests the "seams" and "wiring" of your game. For example, does the Player's health\_changed signal correctly connect to the HUD's update\_health\_bar function? These tests are necessary but are slower, harder to write, and can be "brittle" (they break if you refactor your scene, even if the logic is still correct).
    * **MUST Test (Unit Tests):** Pure logic, algorithms, and data management. These have no dependencies on the SceneTree and can be tested without instancing any scenes. They are fast, reliable, and easy to write.
      * **Examples:**
        * PlayerStats.calculate\_damage(base\_damage, defense)
        * PlayerStats.is\_critical\_hit(crit\_chance)
        * Inventory.add\_item(item): Does it add? What if it's full? What if the item is invalid?
        * Inventory.has\_required\_items(crafting\_recipe)
        * StateMachine.can\_transition\_to(new\_state): Given the current state, is this new state a valid transition?
        * SaveGameData.serialize(): Does the dictionary output match the expected JSON format?
        * Utils.format\_time(total\_seconds): Does 62 correctly return "1:02"?
    * **Test WITH CAUTION (Integration Tests):** Interactions between nodes.
      * **The Problem:** Your Player.gd script's logic in \_physics\_process might depend on is\_on\_floor(), which is a result of move\_and\_slide(). This is an *integration* of physics, signals, and code.
      * **How to Test:** GUT allows you to instance *scenes* for your tests. You can load() a scene, add\_child\_gut(scene\_instance) it to the test's scene tree, and then yield() to simulate time or wait for signals.
      * **Example:** yield(get\_tree().create\_timer(0.1), "timeout") to wait for 0.1 seconds of physics. yield(my\_node, "my\_signal") to pause the test until a signal is emitted. This is powerful but can make tests slow.
    * **How to Mock Objects:** "Mocking" is creating a fake, lightweight version of an object to satisfy a dependency. If your Player script needs to call SoundManager.play\_sound("jump"), your *test* doesn't want to actually hear a sound.
      * **The Solution:** Use GUT's mock() function. You can create a fake SoundManager and pass it to your Player. The test then *asserts* that sound\_manager.play\_sound was *called* with the argument "jump". This proves the *interaction* is correct without testing the SoundManager itself.
      * **Stubs:** You can also stub a mock's functions. For example, if a Player script needs to check if inventory.has\_item("key"), you can create a mock\_inventory, stub(mock\_inventory, "has\_item").and\_return(true), and pass it to the Player. Now you can test the "player has key" logic *without* needing a real inventory or a real key item.
  * **16.4. Concrete Test Examples (GDScript-style pseudo-code)**
    * **Test a Damage Calculation Function (Unit Test):**
      \# test/unit/player/test\_player\_stats.gd
      extends gut.Test
      var stats

      func before\_each():
          \# .new() is fast and isolated. No scenes needed.
          stats \= load("res://player/player\_stats.gd").new()

      func test\_calculate\_damage\_with\_no\_defense():
          assert\_eq(stats.calculate\_damage(50, 0), 50, "Damage should be unchanged with 0 defense")

      func test\_calculate\_damage\_with\_defense():
          assert\_eq(stats.calculate\_damage(50, 20), 30, "Damage should be reduced by defense")

      func test\_damage\_cannot\_go\_below\_one():
          assert\_eq(stats.calculate\_damage(50, 100), 1, "Damage should always be at least 1")

      func test\_calculate\_damage\_with\_vulnerability():
          \# Assumes the function is: calculate\_damage(base, defense, vulnerability\_mod)
          \# stats.vulnerability \= 1.5 \# Set up state
          \# assert\_eq(stats.calculate\_damage(50, 10), 60\) \# (50 \- 10\) \* 1.5
          pass \# Example of expanding the test suite

    * **Test the Inventory System (Unit Test):**
      \# test/unit/inventory/test\_inventory.gd
      extends gut.Test
      var inventory

      func before\_each():
          inventory \= load("res://inventory/inventory.gd").new()
          inventory.max\_slots \= 2

      func test\_add\_item\_succeeds():
          assert\_true(inventory.add\_item("potion"), "Should be able to add to empty inventory")
          assert\_eq(inventory.get\_item\_count("potion"), 1, "Item count should be 1")

      func test\_add\_item\_fails\_when\_full():
          inventory.add\_item("potion")
          inventory.add\_item("sword")
          \# Try to add a third item
          assert\_false(inventory.add\_item("shield"), "Should not add item when full")
          assert\_eq(inventory.items.size(), 2, "Inventory size should remain 2")

      func test\_remove\_item\_succeeds():
          inventory.add\_item("potion")
          assert\_true(inventory.remove\_item("potion"), "Should return true on successful removal")
          assert\_eq(inventory.get\_item\_count("potion"), 0, "Item count should be 0 after removal")

      func test\_remove\_item\_that\_doesnt\_exist():
          assert\_false(inventory.remove\_item("key"), "Should return false when removing non-existent item")

    * **Test a State Machine (Integration Test):**
      \# test/integration/player/test\_player\_states.gd
      extends gut.Test
      var player\_scene \= load("res://player/player.tscn")
      var player

      func before\_each():
          player \= player\_scene.instance()
          add\_child\_gut(player) \# Adds to test's scene tree

      func after\_each():
          \# Clean up the mocked input
          Input.action\_release("move\_right")
          Input.action\_release("jump")

      func test\_player\_starts\_in\_idle\_state():
          assert\_eq(player.state\_machine.current\_state.name, "Idle", "Player should start in Idle state")

      func test\_player\_moves\_to\_walk\_state\_on\_input():
          \# Mock input
          Input.action\_press("move\_right")
          \# Wait one physics frame for the \_physics\_process to run
          yield(get\_tree(), "physics\_frame")

          assert\_eq(player.state\_machine.current\_state.name, "Walk", "Player should be in Walk state after move input")

      func test\_player\_moves\_to\_jump\_state():
          \# Player starts on floor in "Idle"
          Input.action\_press("jump")
          yield(get\_tree(), "physics\_frame")

          assert\_eq(player.state\_machine.current\_state.name, "Jump", "Player should be in Jump state")
