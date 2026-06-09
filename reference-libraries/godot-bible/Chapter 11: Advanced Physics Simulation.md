## **Chapter 11: Advanced Physics Simulation**

* **Objective:** Go beyond the basic features of Godot's built-in physics engine to implement complex, custom, and performant physical behaviors.
* **Detailed Plan:**
  * **11.1. Customizing Physics Step (The "Godot Way")**
    * **The Need:** When you need to *alter* a body's behavior (e.g., gravity, custom thrust, magnetism) every single frame *before* the physics engine solves collisions.
    * **The \_integrate\_forces(state) Callback:**
      * **Concept:** This callback on RigidBody2D/3D runs *after* default forces (like gravity) are applied, but *before* the physics state is solved. It's the "pro" way to apply custom, continuous forces.
      * **How to enable:** You must call set\_integrate\_forces(true) in \_ready().
      * **PhysicsDirectBodyState (The state parameter):**
        * This object gives you direct access to the body's transform, linear/angular velocity, etc., *inside* the physics step.
        * **Crucial:** You must use state.transform (direct access) instead of self.transform (one frame behind).
    * **Use Case Example (Magnetic Force):**
      func \_ready():
          set\_integrate\_forces(true)

      func \_integrate\_forces(state: PhysicsDirectBodyState3D):
          var magnetic\_pull \= get\_magnetic\_force\_at(state.transform.origin)
          state.apply\_central\_force(magnetic\_pull)

          \# This is also where you'd apply custom damping, e.g., "water friction"
          var linear\_drag \= \-state.linear\_velocity \* DRAG\_COEFFICIENT
          state.apply\_force(linear\_drag)

    * **When this is *not* enough:** \_integrate\_forces is still running in GDScript. If your calculation is extremely heavy (e.g., simulating 1,000+ bodies or complex algorithms like SPH), you hit a bottleneck. This is when you move to GDExtension.
  * **11.2. Extending the Physics Engine (The "GDExtension Way")**
    * **The Need:** For truly heavy simulations like custom vehicle physics solvers, n-body simulations, or SPH fluid dynamics.
    * **The Strategy:** Re-implementing your \_integrate\_forces logic in C++ via GDExtension.
    * **The Benefit:** C++ can perform these raw calculations 10-100x faster than GDScript, allowing you to simulate *more* objects *more accurately* within the 16ms frame budget.
    * **This is *not*...** This is *not* about replacing Godot's *collision detection* (Jolt/GodotPhysics). It's about replacing the *force integration* part for specific, demanding objects.
  * **11.3. Custom Gravity**
    * **Problem:** Simulating gravity that isn't a single, global Vector3 (e.g., planetary, spherical, linear).
    * **Easy Solution: Area3D Gravity Zones:**
      * **How:** Create an Area3D, set its gravity\_point property to true (making it a spherical gravity field), set its gravity strength, and (optionally) gravity\_direction (for a "cylindrical" field).
      * **Pros:** Extremely simple, 0 code required.
      * **Cons:** Inflexible. No custom falloff (it's linear or constant), applies to *all* bodies in the area.
    * **Pro Solution: \_integrate\_forces Gravity:**
      * **How:** The *same* method as 11.1.
      * **Practical Example (Planetary Gravity):**
        const GRAVITY\_CONSTANT: float \= 6.674
        @export var planet\_center: Node3D
        @export var planet\_mass: float
        var my\_mass: float \= 10.0 \# From RigidBody

        func \_integrate\_forces(state: PhysicsDirectBodyState3D):
            var to\_planet: Vector3 \= planet\_center.global\_transform.origin \- state.transform.origin
            var distance\_sq: float \= to\_planet.length\_squared()

            \# F \= G \* (m1\*m2 / r^2)
            var force\_magnitude: float \= (GRAVITY\_CONSTANT \* my\_mass \* planet\_mass) / distance\_sq
            var force\_vector: Vector3 \= to\_planet.normalized() \* force\_magnitude

            state.apply\_central\_force(force\_vector)

  * **11.4. Materials and Friction**
    * **The Resource:** PhysicsMaterial. This resource defines how two colliding bodies *react* to each other.
    * **Key Properties:**
      * friction: How much surfaces "grip" each other. 0 \= ice, 1 \= standard. \>1 \= high friction (rubber).
      * bounce: How much energy is returned on impact. 0 \= no bounce (absorbent), 1 \= perfect bounce.
      * rough: If true, friction is applied even at rest (stacking).
      * absorbent: If true, the body "eats" all velocity from a colliding object.
    * **The "How it Works": PhysicsMaterialCombineMode**
      * **Problem:** Body A (Ice, friction 0.1) hits Body B (Rubber, friction 1.5). What is the *actual* friction?
      * **Solution:** The friction\_combine and bounce\_combine properties (default: Average).
        * Average: (0.1 \+ 1.5) / 2 \= 0.8
        * Min: min(0.1, 1.5) \= 0.1 (The "most slippery" surface wins)
        * Max: max(0.1, 1.5) \= 1.5 (The "grippiest" surface wins)
        * Multiply: 0.1 \* 1.5 \= 0.15
    * **Practical Example:**
      * **Ice Rink:** A StaticBody3D floor with a PhysicsMaterial (Friction: 0.05, Combine: Min). Anything that touches it will use its *own* friction or the ice's, whichever is lower.
      * **Sticky Wall:** A StaticBody3D wall (Friction: 2.0, Bounce: 0.0, Combine: Max).
  * **11.5. Fluid Simulation (Liquids, Gases)**
    * **Warning:** Real fluid simulation is *extremely* CPU-intensive and one of the most complex topics in gamedev physics.
    * **Approach 1: "Fake" Fluids (The 99% Solution)**
      * **Concept:** Use an Area3D to *simulate* fluid properties. This is purely visual and non-interactive.
      * **How:** Create an Area3D for your water volume.
      * **Buoyancy:** Area3D.gravity\_point \= true, gravity\_direction \= Vector3.UP, gravity \= (e.g., 10.0). This creates an "upward" gravity (buoyancy) *inside* the area.
      * **Viscosity (Drag):** Area3D.linear\_damp and Area3D.angular\_damp (e.g., 0.5). This makes any body that enters the area slow down, as if moving through water.
      * **Visuals:** Use a "water" shader on the MeshInstance3D of the area. This is purely cosmetic.
    * **Approach 2: "Real" Fluids (The 1% Solution)**
      * **Theoretical Introduction: SPH (Smoothed-particle hydrodynamics)**
        * **Concept:** You don't simulate the *volume* of water. You simulate *thousands* of individual particles.
        * Each particle has properties (mass, density, pressure, velocity).
        * In each physics step, each particle checks its "neighbors" within a small radius.
        * It calculates forces (pressure to push away, viscosity to "stick" together) based on the density of its neighbors.
      * **Implementation Strategy:** **GDExtension is mandatory.**
        * A GDScript for loop over 10,000 particles checking 10 neighbors each is 100,000 calculations. This will take *seconds* per frame.
        * A C++ implementation, ideally parallelized (multi-threaded), is the *only* way to run this in real-time.
        * This is a massive engineering task. **Always use the "Fake" approach first.**
  * **11.6. Soft Bodies and Cloth**
    * **The Node:** SoftBody3D.
    * **How it Works:** It's *not* a standard RigidBody. It's a *simulation mesh* where every *vertex* is a physics point, and every *edge* is a spring.
    * **Use Cases:** Flags, cloth, jelly, deformable objects (e.g., a "squashy" ball).
    * **Key Properties:**
      * simulation\_precision: The number of solver iterations. \>10 gets expensive fast.
      * damping: How quickly it stops "wiggling."
      * stiffness: How much the springs resist being stretched.
    * **Optimization Tip 1: The "Two Mesh" Strategy**
      * **Problem:** Simulating a high-poly, 10,000-vertex flag will destroy performance.
      * **Solution:**
        1. Create a SoftBody3D with a *very low-poly* mesh (e.g., a 10x10 grid plane for a flag). This is your *simulation mesh*.
        2. Create a *separate* MeshInstance3D node with your *high-poly* flag model.
        3. Use a Skin and Skeleton3D to "skin" the high-poly mesh to the low-poly SoftBody3D's vertices.
      * **Result:** The physics engine only simulates 100 vertices, but the player *sees* the 10,000-vertex mesh deforming realistically.
    * **Optimization Tip 2: Attaching to the World**
      * Use SoftBody3D.pin\_points\_to\_nodes() to "nail" specific vertices of the SoftBody to a Node3D (like a flagpole), so the rest of the cloth can be simulated.
