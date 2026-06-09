---
docId: GCS-GUIDE-306
title: "The Application Security (Secure by Design) Guide"
version: 1.0.0
status: Draft
date: 2025-06-18
authors:
  - "Technical Governance"
knowledgeGuardian:
  - "Security Lead"
ssot_path: https://github.com/GenCr-ft/gcs-core-governance/blob/main/reference-libraries/engineering-handbook/03-advanced-guides/GCS-GUIDE-306.application-security-guide.md
metadata:
  lifecycle-stage: approved
  domain: engineering
  doc-type: guide
  scope: studio-wide
  security-classification: l2_confidential
  keywords:
    - "security"
    - "devsecops"
    - "secure-coding"
    - "owasp"
    - "vulnerabilities"
---

# The Application Security (Secure by Design) Guide

## 1. Objective

This guide provides mandatory defensive coding recipes and secure design principles for all engineering teams. Its purpose is to embed security into the entire development lifecycle ("Secure by Design"), moving from a reactive to a proactive security posture. All developers are responsible for understanding and implementing these protocols to protect our systems, our data, and our users.

## 2. Fundamental Secure Design Principles

Security starts with architecture. The following principles MUST be considered at the design stage of any new system or feature.

### 2.1. Principle of Least Privilege

* **Rule:** Every module, user, or system component must be allocated the minimum level of permissions necessary to perform its function, and no more.
* **Implementation:**
  * Application service accounts should have restricted database permissions (e.g., no `DROP TABLE` rights).
  * API tokens should be scoped to specific actions.
  * Run application processes as a non-root user [cite: GCS-GUIDE-202].

### 2.2. Defense in Depth

* **Rule:** Security should not rely on a single layer of protection. We must build multiple, layered defenses so that if one layer fails, others are in place to thwart an attack.
* **Implementation:**
  * A web application firewall (WAF) can block common attacks.
  * The application itself must validate all input.
  * The database layer should use parameterized queries.
  * All layers should have appropriate monitoring and alerting [cite: GCS-GUIDE-304].

### 2.3. Trust but Verify (Zero Trust on Boundaries)

* **Rule:** Never implicitly trust data or requests, especially across a system boundary (e.g., from a client to a server, or from one microservice to another).
* **Implementation:**
  * Every incoming request to a service MUST be re-authenticated and re-authorized, even if it comes from another internal service.
  * All data received from an external source MUST be strictly validated before being processed.

## 3. Defensive Coding Recipes

The following protocols are mandatory for preventing the most common application vulnerabilities.

### 3.1. Prevention of Injection Attacks (SQL, OS, etc.)

* **Problem:** Injection flaws occur when untrusted user input is sent to an interpreter as part of a command or query, tricking the interpreter into executing unintended commands.
* **Standard Protocol:**
    1. **Use Parameterized Queries:** For all database interactions, prepared statements (parameterized queries) MUST be used. Do not construct SQL queries by concatenating strings with user input.
    2. **Use Safe APIs:** Avoid using operating system command interpreters directly (`system()`, `exec()`). Use language-specific APIs that handle arguments safely.
    3. **Input Validation:** Validate that user input conforms to the expected format, type, and length.

### 3.2. Prevention of Cross-Site Scripting (XSS)

* **Problem:** XSS flaws occur when an application includes untrusted data in a new web page without proper validation or escaping, allowing an attacker to execute scripts in the victim's browser.
* **Standard Protocol:**
    1. **Contextual Output Encoding:** All user-supplied data that is rendered on a page MUST be encoded according to the context in which it is placed (HTML body, HTML attribute, JavaScript, CSS).
    2. **Use Modern Frameworks:** Leverage the built-in XSS protection features provided by modern UI frameworks (e.g., React, Angular), which often encode data by default.

### 3.3. Prevention of Cross-Site Request Forgery (CSRF)

* **Problem:** CSRF attacks trick a logged-in user's browser into sending a forged HTTP request, including the victim's session cookie, to a vulnerable web application, allowing the attacker to perform actions on behalf of the user.
* **Standard Protocol:**
    1. **Use Anti-CSRF Tokens:** All state-changing requests (e.g., `POST`, `PUT`, `DELETE`) MUST be protected by an anti-CSRF token (also known as a synchronizer token).
    2. The server generates a unique, unpredictable token and embeds it in a hidden field in the form.
    3. When the form is submitted, the server validates that the token from the form matches the one expected for the user's session.

## 4. Authentication and Session Management Protocols

### 4.1. Authentication Protocol

* **Password Storage:** User passwords MUST NEVER be stored in plaintext or with reversible encryption. They MUST be hashed using a strong, adaptive, and salted hashing algorithm. **Argon2id is the studio standard.**
* **Password Policies:** Enforce minimum password complexity and length requirements.
* **Multi-Factor Authentication (MFA):** All privileged user accounts (e.g., administrators) MUST have MFA enabled.

### 4.2. Session Management Protocol

* **Token Generation:** Session identifiers must be generated using a cryptographically secure pseudo-random number generator (CSPRNG) to ensure they are unpredictable.
* **Token Handling:**
  * Session tokens MUST be transmitted over secure (HTTPS) connections only.
  * Use appropriate cookie flags: `HttpOnly` to prevent access via JavaScript, and `Secure` to ensure it's only sent over HTTPS.
* **Session Termination:** Provide a clear "logout" function that properly invalidates the session on the server side. Sessions must also have a reasonable inactivity timeout.
* **Session Fixation Protection:** Regenerate session identifiers upon successful authentication to prevent session fixation attacks.

## 5. Vulnerability Management

### 5.1. Vulnerability Scanning

* **Automated Scans:** All code repositories MUST be scanned for vulnerabilities using automated tools (SAST, SCA) as part of the CI/CD pipeline.
* **Dependency Management:** Use tools to monitor and update third-party libraries and dependencies. All dependencies MUST be kept up-to-date to mitigate known vulnerabilities.

### 5.2. Incident Response

* **Vulnerability Reporting:** All team members MUST report suspected vulnerabilities immediately to the Security Lead.
* **Incident Response Plan:** The studio MUST maintain an incident response plan that outlines the steps to take in the event of a security breach, including communication protocols and escalation paths.

## 6. Training and Awareness

### 6.1. Mandatory Security Training

* **Annual Training:** All developers MUST complete mandatory security training annually, covering secure coding practices, common vulnerabilities, and the studio's security policies.

### 6.2. Security Awareness

* **Ongoing Awareness:** Regularly share security tips, updates on new vulnerabilities, and best practices through team meetings, newsletters, or dedicated channels.

## 7. Conclusion

This guide establishes the foundation for secure application development at Gencraft. All developers are expected to adhere to these protocols and principles to ensure the security and integrity of our systems. Security is a shared responsibility, and proactive measures are essential to protect our users and our data.

## 8. Related Resources and Links

- [OWASP Top Ten](https://owasp.org/www-project-top-ten/): The most critical security risks to web applications.
* [OWASP Secure Coding Practices](https://owasp.org/www-project-secure-coding-practices/): A comprehensive guide to secure coding practices.
