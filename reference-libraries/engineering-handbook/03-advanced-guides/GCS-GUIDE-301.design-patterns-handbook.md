---
docId: GCS-GUIDE-301
title: "The Design & Architectural Patterns Grimoire"
version: 1.0.0
status: Draft
date: 2025-06-18
authors:
  - "Technical Governance"
knowledgeGuardian:
  - "Principal Architect"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/03-advanced-guides/GCS-GUIDE-301.design-patterns-handbook.md
metadata:
  lifecycle-stage: approved
  domain: engineering
  doc-type: guide
  scope: studio-wide
  security-classification: l2_confidential
  keywords:
    - "design-patterns"
    - "gof"
    - "architecture"
    - "ecs"
    - "hexagonal-architecture"
    - "microservices"
---

# The Design & Architectural Patterns Grimoire

## 1. Objective

This guide serves as the official studio catalog of proven solutions to recurring software design problems. It is not intended to be read from start to finish, but to be used as a reference and a decision-making tool by developers and architects when facing design challenges.

Using these established patterns provides a shared vocabulary, improves system structure, and reduces accidental complexity. Every significant architectural decision MUST be justified with reference to the patterns described herein.

## 2. Part I: Architectural Patterns

Architectural patterns describe the high-level organization of a software system. They are fundamental choices that define the system's structure and constraints.

### 2.1. Foundation: Hexagonal Architecture (Ports & Adapters)

This is our default architectural paradigm for building decoupled and testable applications.

* **Principle:** The core application logic (the "domain") must be isolated from and ignorant of external concerns like databases, UIs, or third-party APIs.
* **Procedure:**
    1. **Define Ports:** Inside the application core, define interfaces (the "Ports") that represent the interactions the domain needs (e.g., `OrderRepositoryPort`, `PaymentServicePort`).
    2. **Implement Adapters:** Outside the core, create concrete implementations (the "Adapters") that connect these ports to real-world technology. A `PostgresOrderRepositoryAdapter` implements the `OrderRepositoryPort` and contains the SQL code. A `StripeAdapter` implements the `PaymentServicePort`.
* **Reference:** This is our canonical implementation of the **Dependency Inversion Principle** [cite: GCS-GUIDE-201] at the architectural level.

### 2.2. Recipe: Clean Architecture

* **Description:** A specific implementation of the Hexagonal Architecture that organizes the application into concentric layers (`Entities`, `Use Cases`, `Interface Adapters`, `Frameworks & Drivers`).
* **The Dependency Rule:** Source code dependencies can only point inwards. Nothing in an inner circle can know anything at all about something in an outer circle.
* **When to Use:** Recommended for complex applications with significant business logic that needs to be protected from technological churn.

### 2.3. Recipe: Entity Component System (ECS)

* **Principle:** A pattern that favors composition over inheritance by separating data (**Components**), unique identifiers (**Entities**), and logic (**Systems**).
* **Procedure:**
    1. **Components:** Define as pure data structures (e.g., `struct Position { float x, y; }`).
    2. **Entities:** Treat as simple integer IDs.
    3. **Systems:** Implement as stateless logic that iterates over entities possessing a specific set of components (e.g., a `MovementSystem` iterates over all entities with `Position` and `Velocity` components).
* **When to Use:** The standard for real-time simulations (like game engines) and systems requiring high performance and data-oriented design. Mandatory for the Aethel game server core.

### 2.4. Catalog of Other Architectural Patterns

* **Layered Architecture:** Suitable for simpler applications where a strict separation between Presentation, Business Logic, and Data Access is sufficient.
* **Event-Driven Architecture:** Use for building highly decoupled, asynchronous systems. A service publishes an event, and other services react to it without direct knowledge of the publisher.
* **Microservices Architecture:** Use for decomposing large systems into independently deployable services, especially for peripheral functionalities that are not latency-critical (e.g., authentication, billing) [cite: AETHEL-ARCH-001].

## 3. Part II: GoF Design Patterns

This section serves as a quick reference to the 23 classic "Gang of Four" (GoF) design patterns.

### 3.1. Creational Patterns (How to create objects)

* **Singleton:** Guarantees a class has only one instance and provides a global point of access to it. Use with extreme caution, as it can introduce global state.
* **Factory Method:** Defines an interface for creating an object, but lets subclasses alter the type of objects that will be created.
* **Abstract Factory:** Provides an interface for creating families of related or dependent objects without specifying their concrete classes.
* **Builder:** Separates the construction of a complex object from its representation, allowing the same construction process to create various representations.
* **Prototype:** Specifies the kinds of objects to create using a prototypical instance, and creates new objects by copying this prototype.

### 3.2. Structural Patterns (How to compose objects)

* **Adapter:** Converts the interface of a class into another interface clients expect.
* **Decorator:** Attaches additional responsibilities to an object dynamically.
* **Facade:** Provides a simplified, unified interface to a set of interfaces in a subsystem.
* **Composite:** Composes objects into tree structures to represent part-whole hierarchies.
* **Bridge:** Decouples an abstraction from its implementation so that the two can vary independently.
* **Flyweight:** Uses sharing to support large numbers of fine-grained objects efficiently.
* **Proxy:** Provides a surrogate or placeholder for another object to control access to it.

### 3.3. Behavioral Patterns (How objects interact)

* **Strategy:** Defines a family of algorithms, encapsulates each one, and makes them interchangeable.
* **Observer:** Defines a one-to-many dependency between objects so that when one object changes state, all its dependents are notified and updated automatically.
* **Command:** Encapsulates a request as an object, thereby letting you parameterize clients with different requests, queue or log requests, and support undoable operations.
* **State:** Allows an object to alter its behavior when its internal state changes. The object will appear to change its class.
* **Chain of Responsibility:** Avoids coupling the sender of a request to its receiver by giving more than one object a chance to handle the request.
* **Iterator:** Provides a way to access the elements of an aggregate object sequentially without exposing its underlying representation.
* **Mediator:** Defines an object that encapsulates how a set of objects interact.
* **Memento:** Without violating encapsulation, captures and externalizes an object's internal state so that the object can be restored to this state later.
* **Template Method:** Defines the skeleton of an algorithm in a method, deferring some steps to subclasses.
* **Visitor:** Represents an operation to be performed on the elements of an object structure.
* **Interpreter:** Given a language, defines a representation for its grammar along with an interpreter that uses the representation to interpret sentences in the language.
* **Null Object:** Provides a default behavior for an object that does nothing, avoiding the need for null checks.
* **Specification:** Encapsulates a business rule or constraint, allowing it to be combined with other specifications using logical operations (AND, OR, NOT).

## 4. Part III: Advanced Patterns

This section covers advanced patterns that are not part of the GoF catalog but are essential for modern software architecture.

### 4.1. Event Sourcing

* **Principle:** Instead of storing the current state of an entity, store a sequence of events that lead to that state. The current state can be reconstructed by replaying these events.
* **Procedure:**
    1. Define events that represent state changes (e.g., `OrderPlaced`, `OrderShipped`).
    2. Store these events in an append-only log (e.g., a database table or a message queue).
    3. Reconstruct the current state by replaying the events.
* **When to Use:** Useful for systems requiring auditability, traceability, and the ability to reconstruct past states. It can also simplify complex state transitions.

### 4.2. CQRS (Command Query Responsibility Segregation)

* **Principle:** Separates the read and write operations of a system into distinct models. Commands change state, while queries retrieve state.
* **Procedure:**
    1. Define separate models for commands (write operations) and queries (read operations).
    2. Use event sourcing to handle commands, storing events that represent state changes.
    3. Use a read-optimized database or cache for queries, which can be updated asynchronously from the command model.
* **When to Use:** Ideal for systems with complex business logic where read and write operations have different performance and scalability requirements. It can also simplify the design of microservices.

### 4.3. Saga Pattern

* **Principle:** Manages long-running transactions and complex workflows by breaking them into smaller, manageable steps, each with its own transaction.
* **Procedure:**
    1. Define a saga that consists of a series of steps, each represented by a command.
    2. Each step can either succeed or fail, with compensating actions defined for failures.
    3. Use an event bus or message queue to coordinate the steps and handle failures.
* **When to Use:** Useful for distributed systems where a single transaction spans multiple services or databases. It helps maintain consistency and recover from failures without locking resources for long periods.

## 5. Conclusion

This grimoire is a living document that will evolve as new patterns emerge and existing ones are refined. It is the responsibility of every architect and developer to contribute to its growth by documenting new patterns, refining existing ones, and sharing experiences from real-world applications.

## 6. References

* [Design Patterns: Elements of Reusable Object-Oriented Software](https://en.wikipedia.org/wiki/Design_Patterns) by Erich Gamma, Richard Helm, Ralph Johnson, John Vlissides (the "Gang of Four").
* [Patterns of Enterprise Application Architecture](https://martinfowler.com/books/eaa.html) by Martin Fowler.

## 7. IA Instructions

This section is reserved for AI-specific instructions and context for processing or updating this document.

* **Purpose for AI Agents:** This document serves as the primary reference for software design patterns within the studio. When a user asks "What design pattern should I use for X?", reference the relevant section in this grimoire.
* **Updating the Grimoire:** When new patterns are identified or existing ones are refined, update this document and notify the Principal Architect for review.
* **Pattern Usage:** When a pattern is applied in a project, ensure it is documented in the project's architecture documentation and linked back to this grimoire for consistency.
* **Pattern Evolution:** Encourage developers to contribute to the grimoire by documenting their experiences with patterns in real-world applications, including successes and challenges.
* **Pattern Adoption:** When a new pattern is proposed, it must be reviewed and approved by the Principal Architect before being added to this grimoire.
* **Pattern Training:** Use this grimoire as a training resource for new developers and architects to familiarize them with the studio's design philosophy and best practices.
* **Pattern Compliance:** Ensure that all architectural decisions made in projects are compliant with the patterns documented in this grimoire. Non-compliance must be justified and documented.

## 8. Change Log

* **2025-06-18:** Initial version of the Design & Architectural Patterns Grimoire created.
