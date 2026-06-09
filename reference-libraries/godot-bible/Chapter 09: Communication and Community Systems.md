## **Chapter 9: Communication and Community Systems**

* **Objective:** Define and standardize the architectures for in-game communication tools to foster a robust social experience and streamline studio-to-community interaction, with a strong emphasis on security and moderation.
* **Detailed Plan:**
  * **9.1. Player-to-Player Communication (Core Social Loop)**
    * **Text Chat System (RPC-Based Architecture):**
      * **The Flow:**
        1. **Client:** Player types message in LineEdit. On submit, the client *does not* send it to other players. It sends *one* RPC to the server: Messages.rpc\_id(1, message\_text, channel\_id).
        2. **Server (Authority):** Receives the Messages RPC.
        3. **Validation (Mandatory):**
           * **Security:** Sanitize the input string (remove malicious characters).
           * **Rate Limit:** Check if this player peer\_id has sent a message in the last X seconds. If too fast, discard the message and send a system message back to the sender ("You are chatting too fast.").
           * **Moderation:** Check if the player is muted. Run the message through the profanity filter (see 9.1.3).
        4. **Distribution:** Based on channel\_id:
           * CHANNEL\_GENERAL: Loop through *all* connected peers and receive\_chat\_message.rpc(peer\_id, sender\_name, message\_text).
           * CHANNEL\_TEAM: Get the sender's team, loop through peers *on that team*, and send the RPC.
           * CHANNEL\_PRIVATE: Send the RPC to the single, specific peer\_id for the whisper.
      * **Code Example (Conceptual):**
        \# Client.gd
        func \_on\_chat\_box\_submitted(text):
            \# Only send to server (peer ID 1\)
            send\_chat\_message.rpc\_id(1, text, CURRENT\_CHANNEL)

        @rpc("any\_peer") \# Server can call this on us
        func receive\_chat\_message(sender\_name, message):
            chat\_ui.add\_message(sender\_name, message)

        \# Server.gd
        @rpc("authority") \# Only server can execute this
        func send\_chat\_message(message, channel):
            var peer\_id \= multiplayer.get\_remote\_sender\_id()
            if not is\_rate\_limited(peer\_id) and not is\_muted(peer\_id):
                var sanitized\_message \= sanitize(message)
                var filtered\_message \= profanity\_filter(sanitized\_message)
                \# ... logic to find target\_peers based on channel ...
                for id in target\_peers:
                    receive\_chat\_message.rpc\_id(id, get\_player\_name(peer\_id), filtered\_message)

    * **Emote/Ping System (Non-Verbal):**
      * **Purpose:** Fast, non-verbal, language-independent communication. Critical for fast-paced team games.
      * **Architecture (Similar to Chat):**
        1. **Client:** Player holds "Ping" key, clicks on ground.
        2. A raycast gets the global\_position of the ping.
        3. Client sends send\_ping.rpc\_id(1, ping\_type\_enum, ping\_position).
        4. **Server:** Receives, validates (rate limit is *critical* here to prevent visual spam).
        5. **Server:** Re-broadcasts to all *other* teammates: show\_ping.rpc(ping\_type\_enum, ping\_position).
        6. **Clients:** show\_ping function instances a PingMarker.tscn at the ping\_position. The scene self-destructs after 5 seconds.
    * **Moderation and User Safety:**
      * **Profanity Filter:**
        * **Implementation:** A profanity\_list.json file loaded *by the server*.
        * **Action:** Server-side string replacement (e.g., word.replace("\*\*\*\*", 4)) *before* rebroadcasting the message.
        * **Security:** *Never* do this client-side. It's trivial to bypass.
      * **Report Function:**
        * **UI:** A "Report" button next to a player's name or chat message.
        * **Flow:** Client sends report\_player.rpc\_id(1, reported\_peer\_id, reason\_enum, chat\_log\_snippet).
        * **Server:** Receives this, adds metadata (timestamp, server ID), and sends it to a secure *external* webhook (see 9.2.2) for human review. **Do not store this in the game server.**
      * **Mute/Block Function:**
        * This is a *client-side* feature.
        * When Client A blocks Client B, Client A simply adds Client B's peer\_id to a local blocked\_list array.
        * In receive\_chat\_message, Client A checks: if sender\_peer\_id in blocked\_list: return. The server still sends the message; the client just chooses to ignore it.
  * **9.2. Studio-to-Player Communication (Live Ops)**
    * **MOTD (Message of the Day) / News Feed:**
      * **Architecture:**
        1. The Main Menu scene contains an HTTPRequest node.
        2. On \_ready(), it calls http\_request.request(YOUR\_NEWS\_API\_URL).
        3. The API returns a simple JSON blob: {"title": "New Patch\!", "body": "...", "image\_url": "..."}.
        4. Connect the request\_completed signal.
        5. \_on\_request\_completed(result, response\_code, headers, body):
           * Check response\_code \== 200\.
           * Parse the body as JSON: var data \= JSON.parse\_string(body.get\_string\_from\_utf8()).
           * Populate UI: title\_label.text \= data.title, body\_label.text \= data.body.
           * Use *another* HTTPRequest node to fetch the image\_url and display it in a TextureRect.
      * **Caching (Critical):**
        * Store the ETag header from the server response in user://cache.cfg.
        * On the *next* request, add the header: http\_request.request(URL, \["If-None-Match: " \+ cached\_etag\]).
        * If the server returns 304 Not Modified, the content hasn't changed. Load the *last* response from a local cache file instead of re-parsing.
    * **In-Game Feedback Collection:**
      * **UI:** A simple form with an OptionButton (Type: Bug, Feedback) and a TextEdit (Body).
      * **Security Vulnerability:** A simple HTTPRequest from the client to a Discord/Slack webhook URL is a *massive security hole*. The URL can be stolen and spammed.
      * **Secure Architecture (Server Relay):**
        1. **Client:** "Submit" button packs the form data into a Dictionary.
        2. Client sends submit\_feedback.rpc\_id(1, feedback\_data).
        3. **Game Server (Trusted):** Receives the RPC. It *has* the secure webhook URL.
        4. Game Server creates a new HTTPRequest node, formats the feedback\_data into the Discord JSON payload, and request(WEBHOOK\_URL, ...)
        5. This hides the webhook URL from all clients and allows the server to rate-limit feedback submissions.
  * **9.3. Back-end Infrastructure (The Persistent World)**
    * **The "Why":** A game server (Godot instance) is *ephemeral*. It exists for one match. We need a *persistent database* for data that lives *between* matches.
    * **Identity Service (Profiles / Auth):**
      * **Purpose:** Handles player accounts (username/password or platform auth like Steam/Epic), persistent stats (K/D, XP), and persistent inventory.
      * **Flow:** Game client HTTPRequests this service *before* connecting to a game server.
    * **Social Service (Friends / Presence):**
      * **Purpose:** Handles friend lists, party invites, and "Presence" (e.g., "Online," "In-Menu," "In-Match").
      * **Architecture:** Requires more than simple HTTP. This is often a WebSocket connection to a dedicated service that can push real-time updates (e.g., "Your friend just came online").
    * **Matchmaking Service:**
      * **Purpose:** The "switchboard" that groups players together.
      * **Flow:**
        1. Client HTTPRequests Matchmaker: "I want to play."
        2. Matchmaker puts player in a queue.
        3. When a lobby is full, Matchmaker *tells a new Game Server to spin up*.
        4. Matchmaker sends all 10 players the *same* IP/Port: "Connect to 123.45.6.78:9000."
        5. All 10 players then connect to that Godot server, and the match begins.
    * **Our Scope:** We will not implement these. We *must* define the API requirements (the JSON payloads and HTTP endpoints) that the game client and server will use to communicate with them.
