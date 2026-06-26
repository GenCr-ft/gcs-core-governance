---
docId: GOV-READ-GB-001
title: godot-bible — Navigation Index
version: 1.0.0
authors: [Governance Crew]
metadata:
  lifecycle-stage: approved
  scope: studio
  domain: engineering
  doc-type: readme
  intended-audience: [contributors]
  security-classification: l1_internal
---
# godot-bible/

Comprehensive Godot 4 patterns and standards for the Aethel game client (`gcp-aethel-client`). Content is **FROZEN** — see active implementation in `gcp-aethel-client/AGENTS.md` for current requirements.

## Chapter Index

| Chapter | Title | Topics |
|---------|-------|--------|
| 01 | Naming and Style Conventions | GDScript naming, file layout, docstrings |
| 02 | Project Structure | Scene organization, autoloads, res:// layout |
| 03 | Version Control with Git | `.gitignore`, LFS, branch patterns |
| 04 | Fundamental Godot Patterns | Signals, groups, node composition |
| 05 | The ECS Architecture | Entity Component System in GDScript |
| 06 | Game System Architecture | Service locator, event bus, hexagonal boundary |
| 07 | Networked Multiplayer Architecture | ENet/WebSocket sync, authority model |
| 08 | Architecture for Modding and Plugins | Plugin API contracts, UGC boundaries |
| 09 | Communication and Community Systems | Chat, social, notification systems |
| 10 | Voxel Worlds and Procedural Geometry | Voxel mesh generation, biome transitions |
| 11 | Advanced Physics Simulation | Rapier.js interop, collision layers |
| 12 | Texture and Shader Management | Atlas packing, shader resource management |
| 14 | Animation, Rigging, and Cinematics | AnimationTree, blendspace, cinematic camera |
| 15 | Anti-Patterns (What to Avoid) | Common GDScript mistakes and fixes |
| 16 | TDD with Godot | GUT v9.3.0 patterns, headless runner setup |
| 17 | General Debugging and Optimization | Profiler, draw call budget, VRAM management |
| E | Appendix A: Useful Code Snippets | Reusable GDScript reference implementations |

> **Note:** Chapter 13 is absent from the reference library (not yet authored). See backlog for tracking.

## Key Cross-References

- **Testing patterns:** Chapter 16 + `gcp-aethel-client/AGENTS.md` testing commands
- **Multiplayer authority:** Chapter 07 + `gcl-voxel-engine/` architecture
- **Voxel geometry:** Chapter 10 + `gcp-aethel-pcg/` PCG pipeline
