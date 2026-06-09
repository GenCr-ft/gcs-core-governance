## **Chapter 7: Networked Multiplayer Architecture**

* **Objective:** Define the core concepts, mandatory architectures, and standard patterns required to build stable, secure, performant, and responsive multiplayer games with Godot. This chapter is critical for avoiding common pitfalls that can doom a project.
* **Detailed Plan:**
  * **7.1. Core Concepts of Godot's Multiplayer API**
    * **The MultiplayerAPI Interface:**
      * This is Godot's high-level, abstract interface for networking.
      * Explain its role: It provides a unified way to manage connections, peers, and RPCs, regardless of the underlying protocol.
      * Mention MultiplayerPeer (the low-level implementation) and ENetMultiplayerPeer (Godot's default, reliable UDP-based implementation).
    * **RPC (Remote Procedure Call):**
      * This is the "verb" of networking: *telling* another machine to *do something*.
      * **The @rpc Annotation (Godot 4+):** This is the modern, mandatory way to designate a function as callable over the network.
      * **RPC Modes (Authority, AnyPeer):**
        * @rpc(call\_local, authority): **The most common.** Only the "authority" (usually the server) can execute this. call\_local means it runs on the caller's machine as well.
        * @rpc(any\_peer): **Use with extreme caution.** *Any* client can call this function on *any* other client. This is a massive security hole and should almost never be used.
      * **Reliability:**
        * reliable: TCP-like. Guarantees the packet will arrive, and in the correct order. Use for critical events: fire\_weapon, take\_damage, player\_joined.
        * unreliable: UDP-like. Packet may be lost or arrive out of order. **Use for high-frequency, non-critical data:** player *aim vector*, etc.
      * **Clear Code Example:**
        \# Player.gd (on the Client)
        func \_process\_input():
            if Input.is\_action\_just\_pressed("fire"):
                \# Tell the server we fired.
                \# We don't spawn the bullet. We ask the server to.
                fire\_weapon.rpc(global\_position, get\_global\_mouse\_position())

        \# Player.gd (on the Server)
        @rpc(authority)
        func fire\_weapon(fire\_pos: Vector3, target\_pos: Vector3):
            \# Server validates the request (e.g., check ammo, fire rate)
            if not can\_fire(): return

            \# Server instances the \*real\* bullet
            var bullet \= BulletScene.instantiate()
            bullet.global\_position \= fire\_pos
            bullet.look\_at(target\_pos)
            get\_tree().get\_root().add\_child(bullet)

    * **MultiplayerSpawner and MultiplayerSynchronizer:**
      * These are the "nouns" of networking: *keeping things in sync*.
      * **MultiplayerSpawner:**
        * **Problem:** Server spawns an enemy. How do clients know *what* scene to spawn and *when*?
        * **Solution:** The spawner acts as a network-aware "factory." When the server calls spawner.spawn(enemy\_scene), the spawner sends a reliable RPC to all clients telling *them* to also call spawn() with the same scene.
      * **MultiplayerSynchronizer:**
        * **The most important node for state syncing.** This node *replaces* thousands of manual RPCs.
        * **Purpose:** Automatically synchronizes properties (e.g., position, rotation, current\_health) from the authority (server) to the replicas (clients).
        * **How it works:** You configure it to watch properties. It automatically detects changes, compresses them, and sends them to clients at a fixed interval.
        * **Use This For:** position, rotation, velocity, health, ammo.
        * **Do NOT Use This For:** One-shot events. Use an RPC for that.
  * **7.2. Architecture Models: Client-Server vs. Peer-to-Peer**
    * **Authoritative Server (Client-Server):**
      * **Concept:** One "peer" (the server) is the ultimate source of truth. The server *owns* the game state, the physics, and the simulation.
      * **Client's Role:** Clients are "dumb terminals." They send *intent* to the server (e.g., "I am pressing the 'forward' key") and receive *state* back from the server (e.g., "Your new position is X").
      * **Why it's the standard:**
        * **Security (Anti-Cheat):** The *only* way to prevent cheating. A client cannot rpc("set\_health", 9999\) because the server is the authority. It owns the health variable.
        * **Consistency:** Prevents desyncs. Since one machine calculates all physics, all players see the same result.
      * **Consequences:** Requires a dedicated server (higher cost) and introduces latency (all actions have a round-trip time).
    * **Peer-to-Peer (P2P):**
      * **Concept:** Everyone is a "server." All peers talk to all other peers directly. One peer is often the "host" (who owns the lobby), but game logic is shared.
      * **When to Use:**
        * **2-Player Co-op:** For small, non-competitive games among trusted friends (e.g., Steam friends).
        * **Fighting Games (Rollback):** A *very* advanced form of P2P that requires deterministic simulation, but provides the lowest possible latency.
      * **Risks (Why we avoid it):**
        * **Security:** Non-existent. Anyone can cheat.
        * **NAT Traversal:** The \#1 killer of P2P projects. Peers often can't connect directly due to firewalls/routers.
        * **Desyncs:** Tiny differences in physics or float precision will cause game states to diverge, leading to "I see him, but he doesn't see me."
    * **Our Standard:** **Authoritative Client-Server is mandatory** for any project that is competitive, has persistent player data, or involves more than 4 players.
  * **7.3. Lobby and Connection Flow (Template)**
    * **Connection Flow:**
      1. **Host (Server):** peer \= ENetMultiplayerPeer.new(). peer.create\_server(PORT). multiplayer.multiplayer\_peer \= peer.
      2. **Client:** peer \= ENetMultiplayerPeer.new(). peer.create\_client(IP, PORT). multiplayer.multiplayer\_peer \= peer.
    * **Player Management (Server-Side):**
      1. Connect signals: multiplayer.peer\_connected.connect(\_on\_peer\_connected) and multiplayer.peer\_disconnected.connect(\_on\_peer\_disconnected).
      2. \_on\_peer\_connected(id): A new player (with id) joined.
      3. The *server* instances a PlayerInfo scene/data for them.
      4. The *server* sends an RPC *to all clients* (including the new one) with the *entire* current player list.
      5. The new client sends an RPC *to the server* with their info (e.g., set\_my\_name.rpc\_id(1, "PlayerName")).
      6. The server receives this, updates its PlayerInfo data, and broadcasts the change to *all* peers.
    * **Game Start:** The Host (Server) is the only one with a "Start Game" button. When pressed, it calls start\_game.rpc().
    * **@rpc(call\_local) func start\_game():** This function, called on all peers, simply does get\_tree().change\_scene\_to\_file("res://game\_level.tscn").
  * **7.4. Synchronization Strategies**
    * **What to synchronize?**
      * **Sync Inputs/Events (RPCs):** jump\_pressed, fire\_weapon, use\_item, chat\_message\_sent. These are discrete, one-time events.
      * **Sync State (Synchronizer):** position, rotation, velocity, current\_health. These are continuous values that define the "state" of an object.
    * **What NOT to synchronize?**
      * **Raw Physics Results:** Never. Let the server run the *entire* physics sim.
      * **Animation Frames:** Don't send animation\_player.play("run") 60 times a second. Send *state* (e.g., is\_running \= true) and let a local AnimationTree handle the blending.
    * **Bandwidth Optimization:**
      * **Tick Rate:** Do not send updates every physics frame. Use a Timer to send updates at a fixed "tick rate" (e.g., 20 times/sec). This is what MultiplayerSynchronizer does automatically.
      * **Unreliable:** Use unreliable RPCs or MultiplayerSynchronizer's "unreliable" mode for data that is sent *constantly* and where one lost packet doesn't matter (e.g., rotation, aim\_vector).
      * **Compression/Quantization:** Don't send a Vector3 if you only need a float. Don't send a float if an int8 (0-255) will do (e.t., health\_percentage).
  * **7.5. Handling Latency (The "Feel" of the Game)**
    * **Client-Side Prediction (For the Local Player):**
      * **Problem:** Player presses "W". The *input* is sent to the server. The *server* moves the player. The *new position* is sent back. Total time: 100ms. The game feels sluggish and unresponsive.
      * **Solution:** On the client, when "W" is pressed, *immediately* move the *local player's* "ghost" or "visual."
      * **Reconciliation:** When the server's *authoritative* position arrives 100ms later, the client must check if it matches their predicted position. If not (e.g., they hit a wall on the server), *snap* the local player back to the server's position. This is the "rubber-band" effect, and the goal is to make it minimal.
    * **Entity Interpolation (For Remote Players):**
      * **Problem:** Remote player positions arrive 20 times/sec. If you just set proxy.global\_position \= new\_pos, the remote player will be *stuttering* and *jerking* across the screen.
      * **Solution:** Create a *buffer*. Always render the remote player slightly *in the past* (e.g., 100ms). When a new position arrives, don't *set* it. lerp (interpolate) from the *current* visual position to this *new* target position over the next 100ms. This guarantees smooth motion at the cost of a slight, unnoticeable delay.
    * **Lag Compensation (For "Hitscan" Weapons):**
      * **Problem:** The "Shooter's Paradox."
        1. Player A (ping 50ms) sees Player B, aims perfectly, and fires. fire\_weapon.rpc() is sent.
        2. Packet arrives at Server 50ms later.
        3. In that 50ms, Player B (ping 50ms) *has already moved* on the server.
        4. Server checks: "Did the bullet hit?" \-\> "No." The shot misses. Player A is furious.
      * **Solution (Server-Side):**
        1. Server receives fire\_weapon.rpc() from Player A (ping 50ms).
        2. Server *rewinds time* by 50ms.
        3. It moves *all other players* (Player B) back to where they *were* 50ms ago (based on its stored history of past positions).
        4. *Then* it performs the raycast for the shot.
        5. It correctly registers the hit that Player A saw on their screen.
