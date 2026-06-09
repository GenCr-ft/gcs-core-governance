---
docId: GOV-GUIDE-400
title: "KB: Art Direction and Style Guides"
version: 1.0.0
authors:
  - Pascal (GCT-ART-ADIR-001)
  - AI Compliance Agent
knowledgeGuardian:
  - Pascal (GCT-ART-ADIR-001)
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/studio-handbook/02-knowledge-base-hub/GOV-GUIDE-400.kb-domain-art-direction.md
creation_date: '2025-05-26'
language: en
last_updated_date: '2026-05-20'
metadata:
  lifecycle-stage: approved
  domain: governance
  doc-type: guide
  scope: studio-wide
  security-classification: l2_confidential
  intended-audience:
    - AllGems
    - AllContributors
    - ArtTeam
    - GameDesigners
    - ProgrammingTeam
  keywords:
  - knowledge-base
  - art-direction
  - visual-standards
  - style-guides
---

# KB: Art Direction and Style Guides

**Version:** 1.0.0
**Last Updated:** 2025-06-13
**Status:** Approved
**Knowledge Guardian:** @Pascal (GCT-ART-ADIR-001)

## 1. Purpose and Scope

This knowledge base article defines the fundamental principles, guidelines, and style standards for **Art Direction** within GenCr-ft Studio. It ensures visual consistency, aesthetic quality, and technical feasibility across all game assets and visual communication, aligning with the studio's unique identity.

The scope of this document includes:

- The overarching artistic vision and core principles.
- Definition of the GenCr-ft Voxel Aesthetic.
- High-level guidelines for various art asset categories (characters, environments, VFX).
- Principles for art asset creation and optimization.
- Integration points with other studio departments (Game Design, Programming).

This document serves as a foundational reference for the entire Art Team, Game Designers, and Programmers involved in visual asset creation and integration.

## 2. Key Information / Concepts / Procedures

### 2.1. The GenCr-ft Voxel Aesthetic: "Exquisite Blocks"

GenCr-ft's artistic vision is defined by a unique **Voxel Aesthetic**, which we term "Exquisite Blocks." This is not merely pixel art in 3D, but a deliberate choice emphasizing:

- **Clarity and Readability:** Distinct shapes and forms, even at a distance.
- **Expressiveness over Detail:** Focus on conveying personality and mood through simplified forms and strong silhouettes.
- **Harmonious Palette:** Use of curated color palettes to achieve atmospheric depth and visual coherence across diverse biomes.
- **Tactile and Playful:** A sense of physicality and a charming, inviting quality inherent to voxel construction.
- **Performance-Conscious:** Designs that naturally lend themselves to efficient rendering and game performance.

### 2.2. Core Art Direction Principles

All visual assets created for GenCr-ft must adhere to the following principles:

- **Visual Coherence:** Maintain a unified visual language across all game elements (characters, environments, props, UI) to create a cohesive world.
- **Fidelity to Lore:** Visuals must support and enhance the game's lore and narrative themes (collaborate with `Gaspard`).
- **Gameplay Readability:** Art should clearly communicate gameplay elements (e.g., interactable objects, enemy types, hazards) to the player.
- **Performance Optimization:** Art creation must consider technical constraints and aim for optimal performance within the `gcl-voxel-engine` (collaborate with `Rémi` and `Léa`).
- **Scalability:** Assets should be designed to support procedural generation where applicable, offering modularity and parameterization (collaborate with `Karim`).
- **Ethical Representation:** Avoid stereotypes and promote inclusivity in character and environmental design, adhering to [AI Ethics Guidelines](../00-studio-vision-and-principles/GOV-POLICY-002.ai-ethics-guidelines.md) and the Code of Conduct.

### 2.3. Art Style Guides and Asset Specifications

The detailed, living documentation for the GenCr-ft art style and asset specifications is maintained in the dedicated `gcp-aethel-assets-styleguide` repository. This includes:

- **Main Art Style Guide (`gcp-aethel-assets-styleguide/Art-Style-Guide_Main.md`):** The definitive document for overall visual direction.
- **Character Art Style Guide (`gcp-aethel-assets-styleguide/characters/style_guide_characters_voxel.md`):** Guidelines for character modeling, texturing, and expression.
- **Environment Art Style Guide (`gcp-aethel-assets-styleguide/environments/style_guide_environments_voxel.md`):** Rules for terrain, structures, and vegetation.
- **VFX Style Guide (`gcp-aethel-assets-styleguide/vfx/style_guide_vfx_voxel.md`):** Principles for visual effects.
- **Animation Style Guide (`gcp-aethel-assets-styleguide/characters/animation_style_guide_voxel.md`):** Directives for motion, timing, and expressiveness.
- **Technical Specifications:** Detailed budgets (polycount, texture size), naming conventions, and export settings are defined here (`gcp-aethel-assets-styleguide/technical_specifications/`).

### 2.4. Art Asset Creation Pipeline and Tools

Art assets are created using a streamlined pipeline to ensure quality and efficiency:

- **Concept Art (`Sophie`):** Initial visual exploration and definition.
- **Voxel Modeling (`Théa`, `Ulysse`):** Creation of 3D voxel models.
- **Technical Art (`Rémi`):** Rigging, shader development, tool creation for artists, optimization.
- **Animation (`Valérie`):** Bringing characters and objects to life.
- **VFX (`William`):** Designing and implementing visual effects.
- **Tools:** Standard Digital Content Creation (DCC) tools (e.g., MagicaVoxel, Blender, Substance Painter, Photoshop) are used. Custom scripts and engine-integrated tools are developed by `Rémi` to support artist workflows.

### 2.5. Art Review and Approval Process

All key art assets and creative milestones undergo formal review and approval, as defined by Protocol S1: Feedback & Approval.

- **Reviewers:** Primarily `Pascal` (Art Director) and `Quentin` (Lead Artist), with input from Game Design (`Étienne`) and Programming (`Julien`, `Léa`) for technical and gameplay alignment.
- **Mechanism:** Typically via Pull Requests on `gcp-aethel-assets-styleguide` or designated art asset repositories, with visual previews and detailed feedback in comments.

## 3. Examples

-(This section will include conceptual diagrams of the art pipeline, examples of different voxel densities used for various assets, excerpts from mood boards, and side-by-side comparisons of concept art and final in-game assets. Visual examples are crucial for conveying artistic intent.)-

## 4. Responsibilities

The primary responsibility for **Art Direction** rests with `Pascal` (GCT-ART-ADIR-001) as the Knowledge Guardian for this domain. He defines the artistic vision and ensures its consistent application. `Quentin` (GCT-ART-LART-001) is responsible for leading the art production team in executing this vision. Collaboration with all members of the Art Team and cross-functional teams is essential.

## 5. Related Resources and Links

- -hub---readme.md)
- [SSoT Documentation Principles](GOV-PRIN-001.ssot-documentation-principles.md)
- [Knowledge Base Contribution and Style Guide](GOV-GUIDE-007.knowledge-management-and-contribution-guide.md)
- [KC&T Guiding Principles](../00-studio-vision-and-principles/GOV-GUIDE-008.kcandt-guiding-principles.md)
- [Overall Technical Architecture Vision](../00-studio-vision-and-principles/ENG-STRATEGY-002.overall-technical-architecture-vision.md)
- [Protocol S1: Feedback & Approval](../01-operational-protocols/OPS-GUIDE-021.s1-feedback-approval.md)
- [Protocol S4: Artifact Storage](../01-operational-protocols/OPS-GUIDE-020.s20-artifact-storage-and-retention.md)
- [Protocol S9: Intellectual Property Management](../01-operational-protocols/OPS-GUIDE-009.s9-intellectual-property-management.md)
- [`gcp-aethel-assets-styleguide` repository - main entry point](https://github.com/GenCr-ft/gcp-aethel-assets-styleguide/blob/main/README.md)
- [`gcp-aethel-architecture` repository - main entry point](https://github.com/GenCr-ft/gcp-aethel-architecture/blob/main/README.md)
- [`gcp-aethel-client` repository - main entry entry](https://github.com/GenCr-ft/gcp-aethel-client/blob/main/README.md)
- [`gcp-aethel-docs-gdd` repository - main entry point](https://github.com/GenCr-ft/gcp-aethel-docs-gdd/blob/main/README.md)
