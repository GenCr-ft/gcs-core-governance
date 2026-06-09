## **Chapter 12: Texture and Shader Management**

* **Objective:** Establish best practices for managing graphics resources to optimize video memory (VRAM) usage, reduce draw calls, and create visually rich, performant materials.
* **Detailed Plan:**
  * **12.1. Best Practices for Textures (The Data)**
    * **12.1.1. The \#1 Misconception: Disk Size vs. VRAM Size**
      * **The Problem:** A 1024x1024 PNG might be 1MB on disk. Developers assume it uses 1MB of VRAM.
      * **The Reality:** The GPU cannot read PNG/JPG directly. It must be *decompressed* in VRAM. A 1024x1024 32-bit (RGBA8) texture *always* uses 1024 \* 1024 \* 4 bytes \= 4MB of VRAM, regardless of disk size.
      * **Our Rule:** Always check the VRAM usage, not the file size.
    * **12.1.2. VRAM Compression (The Solution)**
      * **Concept:** Use Godot's built-in texture import settings to apply a hardware-specific compression (like BCn/S3TC for desktop, ASTC for mobile). The GPU *can* read these formats directly.
      * **How:** In the Import dock, select a texture, choose VRAM Compressed mode.
      * **Trade-off:** Results in a *massive* VRAM saving (e.g., 4:1 or 6:1, turning 4MB into 1MB or less) at the cost of a *slight*, often imperceptible, loss in quality.
      * **Our Rule:** VRAM Compressed must be the default for all 3D/2D game assets. Lossless is only for UI elements where perfect pixel fidelity is required.
    * **12.1.3. Texture Atlases (The Draw Call Killer)**
      * **Problem:** A 3D model with 5 materials (wood, metal, cloth, leather, skin) requires 5 separate draw calls. This is slow.
      * **Solution:** A Texture Atlas (or "Trim Sheet") combines all these textures into *one larger texture* (e.g., one 2048x2048). The 3D model's UVs are laid out so that all parts map to different sections of this single texture.
      * **Result:** The model now uses *one material* and *one draw call*.
      * **2D Equivalent:** A Sprite Sheet (managed by Sprite2D's Animation \> Hframes/Vframes or AtlasTexture resource) is the same concept for 2D.
      * **Tools:** Provide links to tools like Materialize or internal scripts for packing.
    * **12.1.4. Mipmaps (The Performance/Quality Boost)**
      * **Concept:** A pre-calculated sequence of smaller versions of a texture.
      * **The Benefit (Performance):** When a 1024x1024 texture is far away and only covers 2x2 pixels, the GPU doesn't have to sample the entire 1024px texture. It samples the tiny 2x2 mipmap, which is *much* faster.
      * **The Benefit (Quality):** Prevents "shimmering" or "aliasing" on distant surfaces.
      * **The Cost:** Mipmaps add \~33% to the texture's VRAM cost.
      * **Our Rule:** **Always enable Mipmaps** for all 3D textures and any 2D textures that will be scaled down. Disable only for pixel-art UI or ViewportTextures that are 1:1.
    * **12.1.5. Power-of-Two (POT) Sizing**
      * **Concept:** Textures should have dimensions that are powers of two (e.g., 128, 256, 512, 1024, 2048).
      * **Why:** Required for VRAM compression (BCn/ASTC) and Mipmapping. Non-POT textures often cannot be compressed properly and may have performance hits.
      * **Our Rule:** All assets *must* be authored at POT resolutions.
  * **12.2. Shaders in Godot (The Logic)**
    * **When to create a custom shader?**
      * When StandardMaterial3D or CanvasItemMaterial are no longer sufficient.
      * **Examples:** Stylized water, wind-blown foliage, outline/cel-shading (NPR), tri-planar mapping for terrain, procedural noise, or any effect that needs to react to game state (e.g., a "hit flash").
    * **The Godot Shader Language (GDShader)**
      * **Concept:** A simple, GLSL-like language. shader\_type(spatial) for 3D, shader\_type(canvas\_item) for 2D, shader\_type(sky) for skies.
      * **Core Functions (Spatial):**
        * vertex(): Runs *once per vertex*. Use this to modify VERTEX (position), NORMAL, UV. This is where you do procedural geometry or wind sway.
        * fragment(): Runs *once per pixel*. Use this to set ALBEDO (color), ROUGHNESS, METALLIC, ALPHA. This is where you do texturing and lighting.
        * light(): Runs *once per pixel, per light*. Use this to create custom lighting models (e.g., stylized toon shading).
    * **uniform vs. varying (The "Pipe")**
      * uniform: A *parameter* sent from the CPU (GDScript) to the *entire* shader. It's constant for all vertices and pixels. (e.g., uniform float dissolve\_threshold, uniform vec4 flash\_color).
      * varying: A *variable* passed from the vertex() function to the fragment() function. The GPU *interpolates* this value across the surface of the triangle.
      * **Example:** varying vec2 custom\_uv; in vertex() you set custom\_uv \= UV \* 0.5;. In fragment(), you read this custom\_uv and it will be smoothly blended from one vertex to the next.
  * **12.3. Creating Reusable and Parametrizable Shaders**
    * **12.3.1. Inspector uniforms (The Key to Artist-Friendly Shaders)**
      * Use uniforms with *hints* to expose them in the Godot Inspector.
      * **Code Example:**
        shader\_type(spatial);

        // A color picker will appear in the inspector
        uniform vec4 albedo\_color : source\_color;

        // A slider from 0 to 1 will appear
        uniform float roughness\_amount : hint\_range(0.0, 1.0) \= 0.5;

        // A file dialog for a texture will appear
        uniform sampler2D noise\_texture : source\_color;

        void fragment() {
            ALBEDO \= albedo\_color.rgb;
            ROUGHNESS \= roughness\_amount;
            // ... use noise\_texture ...
        }

    * **12.3.2. Practical Example: "Dissolve" Shader**
      * **Concept:** Make an object "dissolve" using a noise texture and a threshold.
      * **Code:**
        uniform sampler2D noise\_texture : filter\_nearest;
        uniform float dissolve\_threshold : hint\_range(0.0, 1.0) \= 0.0;

        void fragment() {
            float noise \= texture(noise\_texture, UV).r; // Read red channel of noise

            if (noise \< dissolve\_threshold) {
                discard; // 'discard' completely kills the pixel
            }

            ALBEDO \= vec3(1.0, 1.0, 1.0);
        }

      * **GDScript:** material.set\_shader\_parameter("dissolve\_threshold", 0.5)
    * **12.3.3. Reusability with \#include**
      * **Concept:** Godot 4 allows .gdshaderinc files. You can create a library of common functions (e.g., noise.gdshaderinc, utils.gdshaderinc).
      * **How:**
        * // file: /shaders/common/noise.gdshaderinc
        * float simple\_noise(vec2 uv) { ... }
        * // file: /player/player.gdshader
        * \#include "res://shaders/common/noise.gdshaderinc"
        * void fragment() { float n \= simple\_noise(UV); ... }
  * **12.4. Shader Organization and Optimization**
    * **12.4.1. The Golden Rule: fragment is expensive, vertex is cheap.**
      * **Why:** A vertex shader might run 1,000 times for a model. The fragment shader might run 1920 \* 1080 \= 2,073,600 times (or more) for that same model.
      * **Action:** Move *any* calculation that is not pixel-dependent from fragment() to vertex(). Calculate it in vertex and pass it to fragment via a varying.
    * **12.4.2. Avoid if Statements (Branching)**
      * **Problem:** A GPU executes code in parallel (e.g., 32 pixels at once). If 16 pixels take an if and 16 pixels take an else, the GPU must run *both branches*. This is called "thread divergence" and is very slow.
      * **Solution:** Use built-in GLSL functions like step(), smoothstep(), and mix() which are "branchless" (use math, not logic).
      * **Example (Bad):**
        if (noise \< threshold) {
            ALPHA \= 0.0;
        } else {
            ALPHA \= 1.0;
        }

      * **Example (Good):**
        // step(edge, x) returns 0.0 if x \< edge, and 1.0 if x \>= edge
        ALPHA \= step(threshold, noise);

    * **12.4.3. Minimize Texture Lookups**
      * Sampling a texture (texture(...)) is a slow operation (fetches from VRAM).
      * **Action 1:** Don't sample textures in the vertex shader if you can avoid it.
      * **Action 2:** "Channel Packing." Store different grayscale maps in the R, G, B, and A channels of a single texture. (e.g., R=roughness, G=metallic, B=ambient\_occlusion). This is *one* texture lookup instead of *three*.
    * **12.4.4. Organization**
      * Follow the "Group by Feature" (Chapter 2\) principle.
      * A shader used *only* by the player lives in /player/player\_shader.gdshader.
      * A reusable shader lives in /shared/shaders/water.gdshader.
      * A reusable function library lives in /shared/shaders/include/noise.gdshaderinc.
