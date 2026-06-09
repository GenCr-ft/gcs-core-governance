## Chapter 9: Architecture and Urbanism

---

### 9.0 Introduction: Building the Habitable World

This chapter marks a critical transition, moving procedural generation from the realm of the *natural* to the **man-made**. In the previous chapters, we summoned chaotic, organic forms: mountains, forests, and creatures. Now, we apply our algorithms to a new challenge: **order, structure, and function**. This is the domain of **architecture** (the building) and **urbanism** (the city).

Here, the goals are different. A procedural building cannot just *look* interesting; it must be *functional*. A floorplan must be navigable. A city cannot just be a random collection of houses; it must be a *system* for habitation and transport, with logical road networks, distinct districts, and a sense of planned, human-driven history.

In this chapter, we will explore the techniques used to solve these complex spatial and logical problems. We will operate at two scales:
1.  **The Macro (Urbanism):** We will use agent-based models, graph theory, and partitioning algorithms to generate the "skeleton" of an entire city, from its branching road networks to its distinct districts.
2.  **The Micro (Architecture):** We will use powerful grammar-based systems (like Shape Grammars) and constraint-solvers (like WFC) to construct the "flesh" of the city—the infinite, stylistically-consistent, and functional buildings that fill the lots.

This is procedural generation as a tool for **spatial problem-solving**, a digital architect that can design not just a single asset, but a complete, emergent, and habitable world.

---

### 9.1 Procedural Urbanism (City & Town Layouts)
*This section focuses on the "macro" scale: generating the layout and systems of an entire urban area.*

* **9.1.1. Theoretical Explanation:**
    * **Concept:** Define the core problem of urbanism: generating a graph of roads (connectivity) and a set of valid lots (parcels) for buildings to occupy.
    * **Core Components:**
        1.  **Road Networks:** The "arteries" of the city, which dictate the flow of traffic and define the shape of the city blocks.
        2.  **Land Parcels:** The "organs" or "lots" created *between* the roads, where buildings will be placed.
        3.  **Zoning:** The (often implicit) rules that define *what* can be built on a parcel (e.g., residential, commercial, industrial).
    * **Constraints:** Generation must be constrained by the underlying terrain (e.g., roads avoid steep slopes, ports are on the coast) and by high-level goals (e.g., connecting a mine to a city center).

* **9.1.2. Implementation: Road Network Generation**
    * **Technique 1: Agent-Based Growth (Chapter 4):**
        * **Concept:** A bottom-up simulation that "grows" roads organically. Agents (representing "travelers" or "settlers") move between points of interest (POIs).
        * **Application:** Agents leave "pheromone" trails (desire lines). Over time, a "road building" agent follows the paths with the highest pheromone concentration, turning them into roads.
        * **Result:** Organic, winding, "medieval" or "ancient" style road networks that feel naturally evolved.
        * **Pseudo-Code (Conceptual Agent):**
            ```
            function updateTravelerAgent(agent, pheromone_map):
                // 1. Move
                target_poi = find_random_poi()
                path = A_Star_Pathfind(agent.pos, target_poi, terrain_cost)
                // 2. Deposit "desire"
                pheromone_map.add(path, 1)

            function updateRoadBuilder(pheromone_map, road_graph):
                // 1. Find highest pheromone path
                best_path = find_highest_pheromone_path(pheromone_map)
                // 2. Build it
                if best_path.strength > BUILD_THRESHOLD:
                    road_graph.addRoad(best_path)
                    pheromone_map.remove(best_path) // Pave it
            ```
    * **Technique 2: L-Systems (Chapter 3):**
        * **Concept:** A top-down, grammar-based approach for creating structured, hierarchical road networks.
        * **Application:** An axiom `H` ("Highway") is recursively replaced by rules that spawn smaller streets (e.g., `H -> H[+S][-S]H`, where `S` is a "Secondary" street).
        * **Result:** Highly structured, grid-like ("Manhattan") or fractal-branching ("suburban") road networks.
        * **Pseudo-Code (Rule definition):**
            ```
            // Axiom: "F" (Main Highway)
            // Rules:
            // 1. F -> F[+F]F[-F]F  (Grid-like)
            // 2. F -> F[+G][-G]   (Branching)
            // 3. G -> G[+H][-H]
            //
            // Turtle Interpretation:
            // F, G, H = Draw 4-lane, 2-lane, 1-lane road
            // [ ] = Push/Pop state (for intersection)
            // +,- = Turn 90 degrees
            ```
    * **Technique 3: Cost-Based Pathfinding (Chapter 3):**
        * **Concept:** Connects a pre-defined set of POIs (City Center, Harbor, Mine) using a pathfinding algorithm like A* or Dijkstra's.
        * **Application:** The terrain is treated as a cost graph. The `getMovementCost()` function heavily penalizes steep slopes, water, and dense forests. The algorithm finds the "cheapest" path for a road between two points.
        * **Result:** Efficient, logical, "Roman road" style networks that make sense with the underlying terrain.
        * **Pseudo-Code (Cost Function):**
            ```
            function getRoadCost(from_node, to_node):
                cost = distance(from_node, to_node)
                // 1. Add cost for slope
                cost += getSlope(to_node) * 100.0 // Heavily penalize steep slopes
                // 2. Add cost for biome
                if getBiome(to_node) == "Forest": cost += 20.0
                // 3. Make water-crossing almost impossible
                if getBiome(to_node) == "River": cost = 999999.0
                return cost
            ```
* **9.1.3. Implementation: Land Parcel & Lot Division**
    * **Concept:** Once roads exist, the "blocks" (empty spaces) between them must be subdivided into usable lots.
    * **Technique 1: Voronoi Tessellation (Chapter 3/5):**
        * **Concept:** A geometric partitioning based on seed points.
        * **Application:** Seed points are scattered (e.g., at road intersections or as "landmarks"). The resulting Voronoi cells define the irregular boundaries of city districts or large properties.
        * **Result:** Irregular, organic, "medieval" style city blocks.
    * **Technique 2: Recursive Subdivision (BSP / Quadtree) (Chapter 3):**
        * **Concept:** A top-down, recursive algorithm that excels at creating rectangular, grid-like layouts.
        * **Application:** The algorithm takes a (usually rectangular) city block defined by roads and recursively splits it (e.g., `splitBlock(rect)`) until the resulting "lots" are below a minimum size.
        * **Result:** Rectangular, grid-based lots, perfect for planned cities and suburbs.
    * **Technique 3: Shape Grammars (Chapter 5):**
        * **Concept:** A grammar is used to define the *style* of the subdivision.
        * **Application:** `Rule: Block -> splitX(Lot_A, Lot_B, Lot_C)` where `Lot_A` is a different *type* of lot than `Lot_B` (e.g., a "corner lot").
        * **Result:** A highly art-directable and stylistically consistent subdivision of city blocks.
* **9.1.4. Strengths and Limitations:**
    * **Strengths:** Can generate vast, functional cities that feel logical and provide clear navigation for players. Excellent for large-scale games and simulations.
    * **Limitations:** Can feel sterile, repetitive, or "top-down" if not combined with other techniques. High-level logic (e.g., zoning, function) can be difficult to enforce with simple geometric rules.
    * **Mitigations:** Use a hybrid approach. Use L-Systems or A* for main highways, then use Agent-Based Growth (9.1.2) for smaller streets to get a mix of planned and organic. Use WFC (9.1.6) to "fill" the lots with buildings that respect the zoning.
* **9.1.5. Use Cases for Generation:**
    * **Open-World Game Cities:** Generating the entire city layout for games like *Watch Dogs* or *Grand Theft Auto*.
    * **Real-time Strategy (RTS) Maps:** Generating random, balanced maps with clear paths and chokepoints.
    * **VFX Backgrounds:** Creating a massive, distant, and detailed city skyline for a film.
    * **Real-world Urban Planning:** Simulating traffic flow, population growth, or the impact of a new highway.
    * **Simulation Games:** Providing the core engine for games like *SimCity* or *Cities: Skylines*.
* **9.1.6. Algorithmic Variations:**
    * **Wave Function Collapse (WFC) (Chapter 5):**
        * **Concept:** WFC is used to *simultaneously* generate roads and lots. The tileset includes `[intersection]`, `[straight_road]`, `[house_lot]`, `[park_lot]`.
        * **Application:** The adjacency rules enforce logic (e.g., `[house_lot]` must be next to a `[road]`). WFC generates a dense, logical, and "finished" city grid in a single pass.
        * **Result:** Excellent for generating dense, detailed, and highly coherent urban or village grids.
    * **Constraint Satisfaction (CSP) (Chapter 5):**
        * **Concept:** A high-level logic solver. Used to define the *zoning* of the city.
        * **Application:** The variables are the districts. The constraints are the high-level rules: `[Industrial_Zone] must_be_downwind_of [Residential_Zone]`, `[Commercial_Zone] must_be_adjacent_to [Residential_Zone]`, `[Industrial_Zone] must_be_near [River]`.
        * **Result:** A logically planned, high-level city map that *makes sense* economically and environmentally, which can then be used to guide the low-level geometry generators.

---

### 9.2 Procedural Architecture (Building Generation)
*This section focuses on the "micro" scale: generating the 3D model and interior layout of a single building.*

* **9.2.1. Theoretical Explanation:**
    * **Concept:** Define the goal—generating a single, functional, and stylistically coherent building.
    * **The Grammar Approach:** The core concept is that buildings are *inherently hierarchical*. `Building -> Floors -> Rooms -> Walls -> Windows`. This structure makes them a perfect match for grammar-based algorithms.
* **9.2.2. Implementation: Shape Grammars (The Core Technique)**
    * **Concept:** A formal grammar (Chapter 5) that recursively replaces abstract *shapes* (like a "facade" polygon) with other, more concrete shapes. This is the gold standard for architectural generation.
    * **Application:** An `Axiom` (e.g., `Lot_Footprint`) is recursively subdivided. The rules can be simple (split a shape) or complex (extrude, inset, place mesh).
    * **Result:** Highly detailed, varied, and *stylistically consistent* buildings.
    * **Pseudo-Code (Facade Generation):**
        ```
        // Axiom: "Facade(width=30, height=50)"

        // Rule 1: Split the main facade into floors
        // (Recursive rule)
        Rule: Facade(w, h) -> if h > 5:
                                splitY( Floor(w, 4.0), Facade(w, h - 4.0) )
                            else:
                                Roof(w, h)

        // Rule 2: Define what a "Floor" is
        // (Stochastic/probabilistic rule)
        Rule: Floor(w, h) -> [
            { replacement: splitX(Wall(w*0.2), Window(w*0.6), Wall(w*0.2)), weight: 0.8 }, // 80%
            { replacement: splitX(Wall(w*0.4), Door(w*0.2), Wall(w*0.4)), weight: 0.2 }  // 20%
        ]

        // Rule 3: Define the terminal symbols
        Rule: Window(w, h) -> [Instantiate("window_mesh", w, h)]
        Rule: Wall(w, h)   -> [Instantiate("wall_mesh", w, h)]
        ```
* **9.2.3. Implementation: Floorplan Generation**
    * **Concept:** Generating the *interior* layout of a building, which is a 2D problem.
    * **Technique 1: BSP (Chapter 3):**
        * **Application:** `bspFloorplan(rect)` recursively splits the building's footprint into rectangles (rooms). Corridors are then added to connect the leaf nodes.
        * **Result:** Simple, fast, and functional, but very "boxy."
    * **Technique 2: WFC (Chapter 5):**
        * **Application:** Uses 2D tiles like `[wall_N]`, `[wall_E]`, `[door_S]`, `[floor]`. WFC "solves" the interior space, creating logical rooms and hallways based on adjacency rules.
        * **Result:** Highly detailed and logical layouts that can include furniture placement.
    * **Technique 3: Graph-based:**
        * **Application:** The designer defines a graph (`[Entry] -> [Hall] -> [Kitchen]`, `[Hall] -> [Living_Room]`). The algorithm then tries to *fit* these "room" nodes (with size constraints) into the building's footprint, solving a complex packing problem.
        * **Result:** A floorplan that is guaranteed to have a specific, logical *flow* for gameplay or simulation.
* **9.2.4. Strengths and Limitations:**
    * **Strengths:** Unmatched **stylistic control**. A single grammar can generate an *infinite* number of buildings in the *same* architectural style (e.t., "Gothic," "Sci-Fi," "Suburban").
    * **Limitations:** Very rigid and hierarchical. Designing the grammar is an extremely difficult, non-intuitive, expert task. Very poor at "messy," organic, or non-hierarchical structures (e.g., a "ruined" building).
    * **Mitigations:** Use **Stochastic Grammars** (9.2.6) for variety. For "ruins," generate a *perfect* building with a grammar, then apply a "destruction" filter (e.g., using 3D noise or physics simulation) as a post-process.
* **9.2.5. Use Cases for Generation:**
    * **Game Worlds:** Generating all the non-hero "filler" buildings in an open-world city.
    * **Film/VFX:** Creating massive, detailed cityscapes for background shots that would be impossible to model by hand.
    * **Real-World Architecture:** Used in tools like *CityEngine* for architects and urban planners to explore thousands of valid design variations for a new skyscraper or apartment complex.
    * **Destructible Buildings:** Generating the *internal structural elements* (beams, supports, floors) so that a building can be realistically destroyed by a physics engine.
    * **Virtual Reality:** Creating endless, non-repeating building interiors for VR exploration.
* **9.2.6. Algorithmic Variations:**
    * **Grammar Induction (Inverse Procedural Modeling):**
        * **Concept:** Using Machine Learning to *learn* a set of grammar rules by analyzing a 3D model of a real building.
        * **Pseudo-Code (Conceptual):**
            ```
            function learnGrammar(example_building_mesh):
                // 1. Analyze mesh to find repeating patterns (e.g., windows, floors)
                patterns = find_repeating_geometry(example_building_mesh)
                // 2. Cluster patterns into abstract symbols
                symbols = cluster_patterns(patterns) // e.g., ["window_A", "window_B"] -> "Window"
                // 3. Infer the hierarchical splitting rules
                rules = infer_recursive_splits(symbols)
                return new Grammar(rules)
            ```
    * **SDF-based Architecture (Chapter 5):**
        * **Concept:** Using boolean operations on SDF primitives to "sculpt" complex, futuristic, or "alien" architecture.
        * **Pseudo-Code:**
            ```
            function generateAlienTower(p):
                // A tall cylinder for the tower
                tower = sdf_Cylinder(p, 100)
                // A repeating torus shape for "rings"
                rings = sdf_RepeatingTorus(p, 5.0)
                // Combine them
                return sdf_Union(tower, rings)
            ```
    * **Agent-Based Architecture (Emergent Design):**
        * **Concept:** Simulating "agents" (e.g., "residents") that "build" their own homes, leading to emergent, unplanned structures.
        * **Pseudo-Code:**
            ```
            class ResidentAgent:
                function update(world):
                    if this.needsShelter:
                        // 1. Find a valid spot (e.g., flat ground)
                        spot = find_valid_spot(world)
                        // 2. "Build" a simple hut by adding voxels to the world
                        world.addVoxel(spot, "Wood_Wall")
                        world.addVoxel(spot.up(), "Wood_Roof")
                        this.needsShelter = false
            ```
    * **Split Grammars:**
        * **Concept:** A more advanced grammar where rules can be applied based on context or parameters, similar to Context-Sensitive L-Systems (8.1.5).
        * **Pseudo-Code:**
            ```
            // Rule with a conditional
            Rule: Floor(w, h, is_ground_floor) ->
                if is_ground_floor:
                    splitX(Wall, Door, Wall) // Must have a door
                else:
                    splitX(Wall, Window, Wall) // Only windows
            ```
