---
docId: GCS-GUIDE-201
title: "The Everyday Developer's Guide"
version: 1.0.0
status: Draft
date: 2025-06-17
authors:
  - "Technical Governance"
knowledgeGuardian:
  - "Lead Developer"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/02-development-guides/GCS-GUIDE-201.developer-guide.md
metadata:
  lifecycle-stage: approved
  domain: engineering
  doc-type: guide
  scope: studio-wide
  security-classification: l2_confidential
  keywords:
    - "developer"
    - "guide"
    - "workflow"
    - "git"
    - "clean-code"
    - "solid"
---

# The Everyday Developer's Guide

## 1. Objective

This guide is the primary reference for all developers at the studio. It provides clear, actionable, and mandatory procedures for the daily tasks of writing, reviewing, and delivering high-quality code. Its purpose is to establish a consistent and professional baseline for all our development activities.

It translates the abstract principles from our **Manifesto** [cite: GCS-GUIDE-101] into concrete, everyday actions.

## 2. Version Control Workflow (Git)

All development work MUST adhere to the studio's official version control workflow to ensure a clean, understandable, and stable project history.

### 2.1. Branching Strategy: GitHub Flow

Our studio has adopted the **GitHub Flow** as the standard branching model for its simplicity and support for continuous delivery.

1. **`main` Branch is Sacred:** The `main` branch is our single source of truth. It MUST always be in a stable, tested, and deployable state. Direct commits to `main` are strictly forbidden.
2. **Create Descriptive Branches:** All new work, whether a feature or a bugfix, MUST start on a new branch created from the latest version of `main`. Branch names must be descriptive and reference a ticket ID (e.g., `feat/AET-123-player-authentication`).
3. **Push Frequently:** Commit and push your work to your feature branch often. This avoids losing work and keeps the team informed of your progress.
4. **Open a Pull Request (PR):** When you are ready for feedback or your work is complete, open a Pull Request against the `main` branch.

### 2.2. Commits: Atomic and Semantic

Each commit is a historical record. It must be clear and focused.

* **Atomic Commits:** A commit should represent a single, logical unit of work. Do not mix unrelated changes (e.g., a feature implementation and a typo fix in another file) in the same commit.
* **Semantic Commit Messages:** Commit messages MUST follow the [Conventional Commits](https://www.conventionalcommits.org/) specification. This provides a clear history and allows for automated changelog generation.
  * **Format:** `<type>[optional scope]: <description>`
  * **Examples:**
    * `feat: add user login via email`
    * `fix: prevent crash when processing invalid input`
    * `refactor(auth): simplify token generation logic`
    * `docs: update API documentation for the user endpoint`

### 2.3. Pull Requests (PRs): The Gateway to `main`

PRs are our primary mechanism for code review and quality control.

1. **Clear Description:** The PR description MUST provide context. Use the provided PR template, linking to the relevant ticket and explaining the "what" and "why" of the change.
2. **Keep it Small:** Small, focused PRs are easier and faster to review. If a feature is large, break it down into multiple, smaller PRs.
3. **Self-Review First:** Before requesting a review, re-read your own code. Run linters and tests locally. You are the first line of defense for quality.
4. **Get it Approved:** A PR requires at least **one** approval from another team member before it can be merged. Address all feedback and ensure all CI checks are green.
5. **Merge Commit:** When merging, use a standard merge commit. This preserves the full atomic commit history (e.g., red/green/blue TDD commits) on `main`, making the change trail auditable and revertable at the commit level.

## 3. Code Quality Standards

We write code for other humans to read. Clarity, maintainability, and simplicity are not optional.

### 3.1. Clean Code Principles

* **Meaningful Names:** Variable, function, and class names must reveal their intent. Avoid single-letter variables (except for loop counters) and cryptic abbreviations.
* **Functions Do One Thing:** Functions should be short and have a single, clear responsibility. If you need to describe what a function does with a comment, it's probably too long and should be broken down.
* **Avoid Comments as Crutches:** The best comment is a well-named variable or function. Use comments to explain *why* something is done in a particular way, not *what* it does.
* **DRY (Don't Repeat Yourself):** Avoid duplicating code. Abstract common logic into reusable functions or classes.

### 3.2. SOLID Principles in Practice

A basic understanding and application of SOLID principles are expected.

* **Single Responsibility Principle (SRP):** A class should only have one reason to change. Don't create "God Objects" that do everything. For example, user authentication logic should be separate from user profile management.
* **Open/Closed Principle (OCP):** Our code should be open for extension, but closed for modification. Use interfaces and abstractions to allow new functionality to be added without changing existing, tested code.
* **Dependency Inversion Principle (DIP):** Depend on abstractions, not on concrete implementations. This is the foundation of a modular and testable system. Use dependency injection to provide implementations at runtime.

## 4. Essential Documentation

Documentation is not an afterthought; it is part of the development process.

### 4.1. README.md

Every project or service repository MUST have a `README.md` file at its root. It is the front door to your project and must contain, at a minimum:

* A brief description of the project's purpose.
* Instructions on how to build, configure, and run the project locally.
* Instructions on how to run the tests.
* A link to any relevant API documentation or other guides.

### 4.2. Code Comments

* **Public APIs:** All public functions, classes, and methods MUST have documentation comments (e.g., Javadoc, XML comments) explaining their purpose, parameters, and return values.
* **Complex Logic:** For any algorithm or piece of business logic that is not immediately obvious, add a concise comment explaining the "why" behind your implementation.
* **Avoid Redundant Comments:** Do not comment on obvious code. If the code is clear, no comment is needed. Comments should add value, not repeat what the code already expresses.

### 4.3. Architecture Documentation

* **Architecture Diagrams:** For complex systems, maintain architecture diagrams that illustrate the high-level structure and interactions between components. These should be updated as the architecture evolves.
* **Design Decisions:** Document significant design decisions in a `DECISIONS.md` file or similar. This helps future developers understand the rationale behind architectural choices and can prevent unnecessary rework.

## 5. Continuous Learning and Improvement

We are committed to continuous improvement, both as individuals and as a team.

### 5.1. Code Reviews

* **Peer Reviews:** All code changes MUST be reviewed by at least one other developer. This is not just a formality; it is an opportunity for learning, knowledge sharing, and improving code quality.
* **Constructive Feedback:** Reviews should be constructive and focused on the code, not the person. Use the review as a chance to teach and learn.
* **Learning Opportunity:** Use code reviews to learn from each other. If you see a pattern or technique you don't understand, ask questions. If you have suggestions for improvement, share them.

### 5.2. Knowledge Sharing

* **Documentation:** Regularly update documentation to reflect changes in the codebase. This includes README files, architecture documents, and inline comments.
* **Internal Workshops:** Participate in or lead internal workshops to share knowledge on specific topics, tools, or techniques. This helps build a culture of learning and collaboration.

### 5.3. Personal Development

* **Stay Updated:** Keep up with industry trends, new technologies, and best practices. Follow relevant blogs, attend webinars, and participate in online communities.
* **Skill Development:** Allocate time for personal skill development. This could include learning a new programming language, mastering a framework, or improving your understanding of design patterns.
* **Feedback Loop:** Regularly seek feedback on your work and be open to constructive criticism. Use this feedback to improve your skills and practices.
