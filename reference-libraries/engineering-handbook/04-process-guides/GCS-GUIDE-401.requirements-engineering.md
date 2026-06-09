---
docId: GCS-GUIDE-401
title: "The Requirements Engineering Guide"
version: 1.0.0
status: Draft
date: 2025-06-18
authors:
  - "Technical Governance"
  - "Product Management"
knowledgeGuardian:
  - "Lead Product Manager"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/04-process-guides/GCS-GUIDE-401.requirements-engineering.md
metadata:
  lifecycle-stage: approved
  domain: engineering
  doc-type: guide
  scope: studio-wide
  security-classification: l2_confidential
  keywords:
    - "requirements"
    - "user-story"
    - "acceptance-criteria"
    - "product"
    - "agile"
---

# The Requirements Engineering Guide

## 1. Objective

This guide establishes the official studio protocol for defining, documenting, and validating software requirements. Its purpose is to ensure that every development task is based on a clear, shared understanding of the business need and the expected outcome. This prevents ambiguity, reduces rework, and aligns engineering efforts with product goals.

No development work on a new feature shall begin without a corresponding, approved User Story that follows the protocols described herein.

## 2. The User Story Protocol

The User Story is our primary artifact for describing a feature from an end-user's perspective.

### 2.1. Standard Format

All User Stories MUST follow the standard "Connextra" template:

**As a** `<type of user>`,
**I want** `<to perform some action>`,
**so that** `<I can achieve some goal/value>`.

* **`<type of user>`:** The persona. Who are we building this for? (e.g., "a new player," "a guild administrator").
* **`<to perform some action>`:** The goal. What is the user trying to do? (e.g., "to join a guild," "to view my inventory").
* **`<so that>`:** The value. Why does the user want this? This is the most important part as it provides the business context.

### 2.2. The I.N.V.E.S.T. Criteria

A good User Story must adhere to the I.N.V.E.S.T. criteria:

* **I**ndependent: The story should be self-contained and not inherently dependent on another story.
* **N**egotiable: It is not a rigid contract. It is an invitation to a conversation between the Product Owner and the development team.
* **V**aluable: It must deliver clear value to the end-user or the business.
* **E**stimable: The development team must have enough information to estimate the effort required to implement it.
* **S**mall: It should be small enough to be completed within a single sprint. Large stories (Epics) MUST be broken down.
* **T**estable: The story must be testable. This is defined by its Acceptance Criteria.

## 3. The Acceptance Criteria Protocol

Acceptance Criteria (AC) are the conditions that a software product must meet to be accepted by a user, a customer, or other stakeholders. They define the "Done" from a user's perspective.

### 3.1. Standard Format: Gherkin Syntax

All Acceptance Criteria MUST be written using the Gherkin syntax for clarity and to facilitate automated testing (BDD).

**Scenario:** `<A descriptive title for the behavior>`
**Given** `<The initial context or state>`
**When** `<A specific action is performed by the user>`
**Then** `<The expected outcome or change in state>`

* **Example:**
  * **Scenario:** Successful login with valid credentials
  * **Given** I am on the login page
  * **And** I have entered a valid username and password
  * **When** I click the "Login" button
  * **Then** I should be redirected to my account dashboard

### 3.2. Purpose

* **Removes Ambiguity:** ACs clarify what needs to be built, leaving no room for misinterpretation.
* **Defines Scope:** They provide clear boundaries for the User Story.
* **Enables Testing:** They are the direct source for writing acceptance tests. A story is not "Done" until all its ACs pass.

## 4. Requirements Classification

It is crucial to distinguish between two types of requirements:

* **Functional Requirements:** Define *what* the system should do. They are typically described by User Stories (e.g., "a user can purchase an item").
* **Non-Functional Requirements (NFRs):** Define *how* the system should perform a certain function. They are quality attributes that the system must have. NFRs MUST be documented as constraints on the relevant User Stories or Epics.
  * **Examples of NFRs:**
    * **Performance:** "The login page must load in under 2 seconds."
    * **Security:** "All user passwords must be hashed using Argon2." [cite: GCS-GUIDE-306]
    * **Reliability:** "The authentication service must have a 99.95% availability." [cite: GCS-GUIDE-202]
    * **Usability/Accessibility:** "All UI elements must be navigable via keyboard and compliant with WCAG 2.1 AA." [cite: GCS-GUIDE-402]
