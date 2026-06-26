---
docId: GOV-READ-PCG-001
title: pcg-guidelines — Navigation Index
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
# pcg-guidelines/

Procedural Content Generation theory and implementation reference for `gcp-aethel-pcg` (Rust/WASM). Content is **FROZEN** — see `gcp-aethel-pcg/AGENTS.md` for active build commands and requirements.

## Chapter Index

| Chapter | Title | Topics |
|---------|-------|--------|
| 1 | What is Procedural Generation | Taxonomy, use cases, PCG spectrum |
| 2 | The Foundational Pillars | Determinism, seeding, parameter spaces |
| 3 | Geometry and Topology | Mesh generation, graph-based structures |
| 4 | Agent-based and Heuristic Methods | L-systems, WFC, cellular automata |
| 5 | Advanced Algorithmic Approaches | OpenSimplex noise, Voronoi, fractal subdivision |
| 6 | Video Games | Game-specific PCG patterns (Aethel biomes, dungeons) |
| 7 | Visual Arts and Design | Art direction with PCG, palette control |
| 8 | Music and Audio | Procedural audio, Wwise integration with PCG |
| 9 | Science and Engineering | Simulation-driven generation, physics constraints |
| 10 | Practical Implementation | Rust/wasm-bindgen patterns, Xoshiro256++ seeding |
| 11 | Control and Directing PCG | Designer controls, seed pinning, PcgConfig schema |
| — | Part 3: Applications Across Domains | Cross-domain summary reference |
| — | Part 4: Implementation and Best Practices | Production checklist and review criteria |
| — | Appendices: The PCG Cookbook | Quick-reference algorithm recipes |

## Active Implementation References

- **Seeding standard:** Xoshiro256++ — see `gcp-aethel-pcg/src/world/seed.rs`
- **World height constant:** `WORLD_HEIGHT=256` — established in ENG-ADR-072
- **Voronoi biome boundaries:** Chapter 5 + `gcp-aethel-architecture/adrs/ENG-ADR-070.md`
- **PcgConfig schema:** `gcl-api-contracts/` (authoritative wire format)
