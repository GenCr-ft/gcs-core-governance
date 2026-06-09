---
docId: GCS-GUIDE-204
title: Local Persistence Transition Guide
version: 1.0.0
authors:
- AI Gemini CLI
creation_date: '2026-05-05'
language: en
summary: 'Technical instructions for implementing the dual-path persistence model.
  Covers the IChunkStore interface, LocalFSAdapter, and relational fallback.

  '
last_updated_date: '2026-05-05'
knowledgeGuardian: Architecture Lead
metadata:
  lifecycle-stage: approved
  keywords:
  - persistence
  - localfs
  - s3
  - hexagonal-architecture
  - desktop-mode
  scope: studio-wide
  domain: development
  doc-type: guide
  intended-audience:
  - developers
  - architects
  security-classification: l2-confidential
  artifact-class: knowledge
  classification:
    category: to-describe
    type: guide
  lifecycle-phase: approved
  provenance:
    source: manual
date: '2026-05-06'
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/02-development-guides/GCS-GUIDE-204.local-persistence-transition-guide.md
---

# GCS-GUIDE-204 — Local Persistence Transition Guide

## 1. Overview

As defined in **ENG-ADR-060**, Aethel supports two persistence paths: **Cloud** (Postgres + Redis + S3) and **Desktop/Offline** (SQLite + In-Memory + Local Filesystem).

This guide provides the technical specifications for implementing the **Persistence Adapter** pattern to ensure seamless switching between these modes.

## 2. The `IChunkStore` Port (Voxel Data)

To abstract the storage of 32x32x32 voxel chunks, all I/O must pass through the `IChunkStore` interface.

### 2.1 Interface Definition

```typescript
interface IChunkStore {
  /**
   * Loads compressed bytes for a chunk.
   * Returns null if chunk is unmodified (generator fallback).
   */
  read(coords: ChunkCoords): Promise<Uint8Array | null>;

  /**
   * Writes compressed bytes to the store.
   * Implementation must be idempotent and atomic.
   */
  write(coords: ChunkCoords, data: Uint8Array): Promise<void>;

  /**
   * Checks if a mutation exists for this chunk.
   */
  exists(coords: ChunkCoords): Promise<boolean>;

  /**
   * Identifies the storage provider type (e.g., 's3', 'local').
   */
  readonly provider: string;
}
```

### 2.2 S3Adapter (Cloud Mode)
- **Implementation**: Uses `@aws-sdk/client-s3`.
- **Path Logic**: Maps coords to key: `${worldId}/${x}/${y}/${z}.bin`.
- **Trigger**: Activated when `S3_BUCKET_NAME` is defined.

### 2.3 LocalFSAdapter (Desktop Mode)
- **Implementation**: Uses `node:fs` (Server) or `FileAccess` (Godot).
- **Path Logic**: Maps to local save directory: `saves/${worldId}/chunks/${x}/${y}/${z}.bin`.
- **Security - Path Sanitization**:
  - **CRITICAL**: Implement strict sanitization for `${worldId}` and coordinates.
  - Reject any input containing `..` or null bytes to prevent **Path Traversal** attacks.
  - Use `path.join()` with a resolved base directory and verify the result is within the sandbox.
- **Atomic Safety**: Must write to a `.tmp` file and rename to `.bin` to prevent save corruption during power loss.
- **Trigger**: Default fallback or when `PERSISTENCE_MODE=local`.

## 3. Relational Data Fallback (Tier 1)

The persistence microservice (`gcl-srv-persistence`) uses **Prisma** to manage character and RPG data.

### 3.1 Prisma Provider Constraints
**Note on Inaccuracies**: Prisma does not support dynamic provider switching (e.g., `postgresql` vs `sqlite`) at runtime within a single generated client.

**Implementation Requirement**:
- We maintain a single `schema.prisma` targeting the **PostgreSQL** protocol (the studio standard).
- For **Desktop/Offline** mode, the service uses an **SQLite** adapter if possible, or we maintain two separate generated clients:
    - `@prisma/client-pg` (Production)
    - `@prisma/client-sqlite` (Local Dev / Desktop)
- Use a **Factory Pattern** in the `InfrastructureModule` to instantiate the correct repository implementation based on `PERSISTENCE_MODE`.

## 4. Configuration & Mode Detection

The Game Server (`gcp-aethel-server`) orchestrates the mode selection.

| Variable | Value | Result |
|----------|-------|--------|
| `PERSISTENCE_MODE` | `cloud` | Forces S3 and PostgreSQL. Fails if credentials missing. |
| `PERSISTENCE_MODE` | `local` | Forces Filesystem and SQLite. |
| (Undefined) | — | Defaults to `local` for developer ergonomics. |

## 5. Implementation Roadmap

1. **Phase 1**: Define `IChunkStore` interface in `gcl-srv-persistence` and `gcp-aethel-server`.
2. **Phase 2**: Implement `LocalFSAdapter` with base unit tests.
3. **Phase 3**: Implement `S3Adapter`.
4. **Phase 4**: Configure Prisma multi-db support for SQLite.
5. **Phase 5**: Integration test: Save a chunk in local mode, restart server, verify data persists.

---

## IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.
