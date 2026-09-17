# Identity and Access Management Standard

**Organization:** Igzibo Engineering Solutions, Inc.  
**Document:** `identity-and-access-management-standard-v2.md`  
**Version:** 2.0  
**Status:** Living standard  
**Effective Date:** September 16, 2026  
**Owner:** Igzibo Engineering Solutions, Inc.  
**Review Cycle:** At least annually and after material security, legal, or technology changes

## 1. Purpose

This standard establishes minimum requirements for creating, authenticating, authorizing, reviewing, monitoring, and removing access to Igzibo Organizational Resources.

It implements the access-control principles established by the Technology Acceptable Use Policy and is technology-neutral.

## Definitions

- **AI** — Artificial Intelligence, technology capable of performing tasks commonly associated with human intelligence.
- **CISA** — Cybersecurity and Infrastructure Security Agency, a U.S. government agency that provides cybersecurity guidance and resources.
- **Igzibo** — Igzibo Engineering Solutions, Inc.
- **MFA** — Multi-Factor Authentication, authentication requiring two or more independent authentication factors.
- **NIST** — National Institute of Standards and Technology, a U.S. government agency that publishes cybersecurity and technology guidance.
- **Organizational Resource** — Any technology, account, system, service, device, information asset, or other resource owned, licensed, administered, funded, or authorized by Igzibo.

- **IAM** — Identity and Access Management, the processes and technologies used to establish identities and control access.
- **SSO** — Single Sign-On, authentication that allows an authenticated identity to access multiple authorized services.
- **IdP** — Identity Provider, a system that authenticates identities and provides identity information to applications.
- **RBAC** — Role-Based Access Control, assigning permissions according to defined roles.
- **JIT** — Just-in-Time access, temporary access granted only when needed and removed afterward.
- **Privileged Account** — An account capable of administrative, security-sensitive, or otherwise elevated actions.
- **Service Account** — A non-human identity used by software, automation, or a system.
- **Credential** — Information used to authenticate an identity, including passwords, tokens, keys, certificates, passkeys, and authentication devices.
- **Access Review** — A documented examination of identities and permissions to determine whether access remains necessary and appropriate.

## 2. Scope

This standard applies to human accounts, privileged accounts, service accounts, application identities, third-party access, authentication credentials, and authorization mechanisms.

## 3. Identity Principles

Igzibo will apply these principles:

1. Every person should have an individually attributable identity.
2. Access must be based on business need.
3. Access must follow least privilege.
4. Privileged access requires stronger controls.
5. Authentication should resist credential-theft attacks where practical.
6. Access must be removed promptly when no longer required.
7. Shared credentials should be avoided.
8. Access must be reviewable and auditable.
9. Business systems must not depend on an individual's personal identity.

These principles are consistent with NIST Cybersecurity Framework (CSF) 2.0 and CISA IAM guidance.

## 4. Account Provisioning

Accounts may be created only for authorized users or approved system functions.

Before provisioning, Igzibo must establish, as applicable:

- Identity.
- Business purpose.
- Role.
- Required resources.
- Appropriate access level.
- Account owner.
- Required approvals.

Permissions must be limited to those necessary for authorized duties.

## 5. Authentication

MFA is required for Organizational Accounts whenever technically supported.

Phishing-resistant authentication, including passkeys or security keys, should be preferred for privileged and high-risk accounts.

Passwords must be unique, confidential, and protected using an approved password manager when available.

Credentials must never be shared.

Unexpected authentication prompts must not be approved.

## 6. Privileged Access

Privileged access must be separately controlled.

Where practical:

- Administrative duties must use separate privileged identities.
- Administrative accounts must not be used for ordinary email or browsing.
- Privileged accounts must use MFA.
- Privileged actions should be logged.
- Privileged access should be reviewed periodically.
- Permanent administrative access should be minimized.
- JIT access should be used where supported and practical.

## 7. Role-Based Access

Igzibo should use RBAC where practical.

Role assignments must correspond to actual responsibilities and must not accumulate merely because a user previously held another role.

## 8. Service and Application Identities

Service Accounts and application identities must have:

- A documented owner.
- A documented purpose.
- Minimum necessary permissions.
- Managed credentials or keys.
- Periodic review.
- Prompt disablement when no longer required.

Service identities should not be used interactively by people unless specifically authorized.

Secrets must not be embedded in source code, public repositories, ordinary documentation, or ordinary email.

## 9. Third-Party Access

Third-party access must be authorized and limited to the minimum necessary.

Where practical:

- Use individually attributable accounts.
- Do not provide organizational passwords.
- Require MFA.
- Use time-limited access.
- Record the business owner.
- Review access periodically.
- Remove access when the engagement ends.

## 10. Access Reviews

Access reviews must occur at least annually and more frequently for privileged or high-risk systems.

Reviews must verify:

- Continued business need.
- Correct role.
- Justified privileged access.
- Authorized external users.
- Necessary service identities.
- Dormant-account status.
- Excessive permissions.

## 11. Joiner, Mover, and Leaver Lifecycle

### 11.1 Joiner

Before access is granted, authorization, role, required systems, and security requirements must be established.

### 11.2 Mover

When responsibilities change, existing access must be reevaluated. New permissions must not simply accumulate on top of obsolete permissions.

### 11.3 Leaver

When authorization ends, access must be disabled promptly.

The review must include organizational email, cloud applications, source control, remote access, administrative systems, third-party services, API credentials, tokens, and keys as applicable.

Business information must remain accessible to Igzibo after departure.

## 12. Account Recovery

Recovery methods for Organizational Resources must be controlled by Igzibo where practical.

Personal email addresses or Personal Accounts must not be the sole recovery mechanism for critical business accounts.

Critical administrative accounts must have documented recovery procedures.

## 13. Logging and Monitoring

Where supported, Igzibo should retain appropriate authentication and access logs.

Logs should support investigation of failed authentication, suspicious sign-ins, privilege changes, account creation, access changes, administrative actions, and security incidents.

## 14. Exceptions

Exceptions require documented authorization and must identify the reason, affected resource, duration, risk, and compensating controls.

## 15. Enforcement

Failure to follow this standard may result in access restriction, additional training, contractual or employment action, or other appropriate measures.

## 16. References

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- CISA, Identity and Access Management: Recommended Best Practices for Administrators: https://www.cisa.gov/sites/default/files/2023-12/ESF%20IDENTITY%20AND%20ACCESS%20MANAGEMENT%20RECOMMENDED%20BEST%20PRACTICES%20FOR%20ADMINISTRATORS%20PP-23-0248_508C.pdf

## 17. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-09-16 | Initial IAM standard. |
| 2.0 | 2026-09-16 | Coordinated governance revision; standardized definitions, lifecycle requirements, precedence, and mandatory control language. |
