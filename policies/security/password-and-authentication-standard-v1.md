# Password and Authentication Standard

**Organization:** Igzibo Engineering Solutions, Inc.  
**Document:** `password-and-authentication-standard-v1.md`  
**Version:** 1.0  
**Status:** Active Standard  
**Effective Date:** September 16, 2026  
**Owner:** Igzibo Engineering Solutions, Inc.  
**Review Cycle:** At least annually and after material security, legal, contractual, or technology changes

## Definitions

- **Authentication** — The process of verifying the identity of a person, service, device, or other entity.
- **Authenticator** — A credential, device, secret, or other mechanism used to authenticate an identity.
- **AUP** — Technology Acceptable Use Policy.
- **AI** — Artificial Intelligence.
- **IAM** — Identity and Access Management.
- **MFA** — Multi-Factor Authentication, authentication using two or more independent factors.
- **Password** — A secret used to authenticate an identity.
- **Privileged Account** — An account with elevated administrative, security, financial, or other sensitive permissions.
- **Service Account** — An account used by an application, service, integration, or automated process rather than an individual user.
- **SSO** — Single Sign-On, an authentication mechanism that allows an authorized identity to access multiple services through a centralized identity system.

## 1. Purpose

This standard establishes minimum requirements for passwords, authentication, multi-factor authentication, and related credential controls used to access Igzibo Engineering Solutions, Inc. resources.

## 2. Scope

This standard applies to employees, contractors, administrators, service accounts, applications, and other identities that access Igzibo resources.

Client environments may impose additional requirements.

## 3. Authentication Principles

Igzibo uses authentication controls appropriate to the sensitivity and risk of the resource.

The following principles apply:

- Use individual identities whenever practical.
- Do not share passwords or authentication factors.
- Use MFA for administrative access and other resources where required.
- Prefer centralized authentication and SSO where practical.
- Use phishing-resistant authentication where appropriate and supported.
- Apply stronger controls to privileged and high-risk accounts.

## 4. Password Requirements

Where passwords are used, users must:

1. Use unique passwords for Igzibo accounts.
2. Avoid passwords based on easily discovered personal or organizational information.
3. Never disclose passwords to another person.
4. Never store passwords in unsecured documents, notes, email, or chat.
5. Use an approved password manager when available.
6. Change a password promptly when compromise is suspected or confirmed.
7. Avoid reusing compromised credentials on other services.

Igzibo should prefer controls that detect or prevent commonly compromised passwords.

## 5. Multi-Factor Authentication

MFA must be enabled where required by the Identity and Access Management Standard, a client requirement, or the applicable service.

MFA factors must not be shared.

Users must not approve an unexpected authentication request. Unexpected MFA prompts must be treated as a potential security event and reported when appropriate.

## 6. Privileged Accounts

Privileged accounts must receive stronger protection than ordinary user accounts.

Where practical:

- Administrative access should use a separate privileged identity.
- Privileged accounts should use MFA.
- Administrative credentials should not be used for routine activities.
- Privileged access should be limited to the minimum required scope and duration.
- Administrative activity should be logged where supported.

## 7. Service Accounts and Non-Person Identities

Service accounts must have a documented owner and business purpose.

Service-account credentials must:

- Be protected from unauthorized disclosure.
- Have only the permissions required for the service.
- Not be used as substitutes for individual user accounts.
- Be rotated or replaced when compromise is suspected or when required by the applicable system.
- Be disabled when no longer required.

## 8. Recovery and Account Reset

Account recovery processes must provide reasonable assurance that the requesting party is authorized.

Recovery methods must not bypass required security controls without appropriate authorization.

## 9. Credential Storage and Transmission

Credentials must be stored and transmitted using approved security mechanisms.

Passwords and authentication secrets must not be transmitted through unapproved channels or included in source code, configuration files, tickets, or other locations where unauthorized persons could obtain them.

## 10. Compromised Credentials

Suspected credential compromise must be reported promptly.

Igzibo may revoke sessions, disable accounts, reset credentials, rotate service credentials, or take other protective actions.

## 11. Third-Party and Client Systems

Users must follow the authentication requirements of client systems and approved third-party services.

A third party must not receive Igzibo credentials unless specifically authorized and technically appropriate.

## 12. Exceptions

Exceptions require documented approval and must identify the reason, risk, compensating controls, responsible owner, and expiration or review date.

## 13. Relationship to Other Governance Documents

This standard supports:

1. Technology Acceptable Use Policy.
2. Identity and Access Management Standard.
3. Device and Remote Access Standard.
4. Data Classification and Handling Standard.
5. Security Incident Response Procedure.
6. Technology and Third-Party Service Security Standard.

## Version History

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-09-16 | Initial password and authentication standard. |
