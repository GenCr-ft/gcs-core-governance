---
docId: ENG-ADR-049
title: 'ENG-004: Real-Time Environment Update Notification via "Push" Model'
version: 1.0.0
authors:
- Gem-Strategist (AI)
- Gencraft DevOps Team
creation_date: '2025-06-26'
last_updated_date: '2026-05-20'
status: 'Accepted'
metadata:
  scope: studio
  domain: devops
  doc-type: adr

ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/devops-standards/records/adrs/adr-studio-001/ENG-ADR-049.real-time-environment-update-notification.md
---
# ADR-004: Real-Time Environment Update Notification via "Push" Model

## Context

**Problem Statement:** The studio now uses a centralized SSoT file (`role-matrix.yaml`) to define developer environments. When this file is updated (e.g., a new tool is added to a role), there is no mechanism to inform developers that their local environment is out of sync. This "configuration drift" undermines the goal of having standardized environments and can lead to tooling-related issues.

**Driving Forces:**

* **Need for Consistency:** All developers should have an easy way to stay aligned with the latest environment standards.
* **Need for Transparency:** Changes to core developer environments should be communicated clearly and proactively.
* **User Experience:** The update mechanism should not be overly intrusive or disruptive to a developer's workflow.
* **Open Source Preference:** The solution should prioritize open-source, self-hostable, and well-integrated tooling.

## Decision

We will implement a **"Push" notification model** to inform developers of environment updates in real time.

The chosen implementation is as follows:

1. A **GitHub Action** will be configured in the `gcs-core-governance` repository.
2. This action will trigger **only** when a commit to the `main` branch modifies the `foundations/governance/data/role-matrix.yaml` file.
3. The action will execute a script to generate a summary of the changes.
4. It will then use a community-vetted GitHub Action (such as `RocketChat/Rocket.Chat.GitHub.Action.Notification`) to send a formatted message to a dedicated **Rocket.Chat channel** (e.g., `#dev-environment-updates`).
5. The notification will clearly state the nature of the change and instruct developers to run a command (e.g., `gft-onboarding.sh --update`) to apply the changes at their convenience.

## Consequences

### Positive

* **Real-Time Awareness:** Developers are informed of critical environment changes almost immediately after they are approved and merged.
* **High Transparency:** The entire team has visibility into environment evolution through a shared communication channel.
* **User in Control:** The model is not intrusive. It informs the developer, who retains control over *when* to apply the update, minimizing disruption.
* **Simple & Fast Implementation:** This solution leverages existing, mature open-source tools (GitHub Actions, Rocket.Chat webhooks) and can be implemented quickly as a short-term solution.

### Negative

* **Not Fully Automated:** The final step of applying the update relies on human action. There is a risk that developers may ignore or delay applying updates.
* **Dependency on Chat Platform:** The reliability of the notification depends on the availability of the Rocket.Chat service.
* **Asynchronous for Offline Users:** Developers who are offline at the time of the notification will only see it when they next check the channel, potentially missing the real-time aspect.

## Options Considered

### 1. "Pull" Model (Scheduled Check)

* **Description:** A scheduled job (`cron`) on each developer's machine would periodically check for updates.
* **Reason for Rejection:** This approach is not real-time and can be considered "noisy" if it interrupts the user with notifications for updates they may already be aware of. It's less transparent than a central announcement.

### 2. "Active Agent" Model (`gft-cli`)

* **Description:** A background agent managed by our `gft-cli` would poll a central service for updates, calculate a precise diff, and offer to apply only the necessary changes.
* **Reason for Rejection (for now):** While this is the most powerful and sophisticated solution, its implementation complexity (requiring a backend service and significant CLI development) is too high for our short-term goal. It has been accepted as the **strategic long-term vision** and will be tracked in a separate Epic.

This "Push" model provides the best balance of speed, transparency, and implementation simplicity to meet our immediate needs.
