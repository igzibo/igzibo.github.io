# Data Classification and Handling Standard

**Organization:** Igzibo Engineering Solutions, Inc.  
**Document:** `data-classification-and-handling-standard-v2.md`  
**Version:** 2.0  
**Status:** Living standard  
**Effective Date:** September 16, 2026  
**Owner:** Igzibo Engineering Solutions, Inc.  
**Review Cycle:** At least annually and after material legal, contractual, security, or technology changes

## 1. Purpose

This standard establishes a practical classification system for Igzibo information and defines minimum handling requirements.

The standard is technology-neutral and applies regardless of where information is stored or which vendor provides the storage, processing, communication, or collaboration service.

## Definitions

- **AI** — Artificial Intelligence, technology capable of performing tasks commonly associated with human intelligence.
- **CISA** — Cybersecurity and Infrastructure Security Agency, a U.S. government agency that provides cybersecurity guidance and resources.
- **Igzibo** — Igzibo Engineering Solutions, Inc.
- **MFA** — Multi-Factor Authentication, authentication requiring two or more independent authentication factors.
- **NIST** — National Institute of Standards and Technology, a U.S. government agency that publishes cybersecurity and technology guidance.
- **Organizational Resource** — Any technology, account, system, service, device, information asset, or other resource owned, licensed, administered, funded, or authorized by Igzibo.

- **PII** — Personally Identifiable Information, information that identifies or can reasonably be linked to an individual.
- **Public Information** — Information approved for unrestricted public distribution.
- **Internal Information** — Non-public information intended for routine organizational use.
- **Confidential Information** — Non-public information whose unauthorized disclosure could create meaningful business, contractual, privacy, competitive, or reputational risk.
- **Restricted Information** — Information requiring the strongest controls because unauthorized access, disclosure, alteration, or loss could cause significant harm, legal exposure, contractual problems, or security risk.
- **Data Owner** — The person responsible for determining appropriate business use, classification, access, and handling requirements.
- **Data Custodian** — A person or system responsible for storing, processing, securing, or administering information.
- **DLP** — Data Loss Prevention, controls intended to prevent unauthorized disclosure or movement of information.
- **Encryption** — A technical method that transforms information so it cannot reasonably be read without the required key or credentials.

## 2. Scope

This standard applies to information created, received, stored, processed, transmitted, or otherwise handled by Igzibo, including information belonging to or supplied by clients.

It applies to email, cloud storage, source repositories, databases, local devices, paper records, collaboration systems, approved AI systems, and other storage or processing locations.

## 3. Classification Levels

### 3.1 Public

Information approved for public release.

Examples include published website content, public marketing materials, public job postings, approved public documentation, and intentionally public repositories.

### 3.2 Internal

Non-public information intended for normal Igzibo business use.

Examples include internal procedures, routine internal communications, internal project planning, and non-public operational documentation.

### 3.3 Confidential

Information requiring controlled access because disclosure could create meaningful business, contractual, privacy, competitive, or reputational risk.

Examples include client information, contracts, proposals, non-public pricing, business plans, worker information, non-public source code, internal security documentation, and business credentials.

### 3.4 Restricted

Information requiring the strongest controls.

Examples include authentication secrets, private cryptographic keys, highly sensitive PII, security-incident evidence, client data subject to strict controls, legally restricted information, and high-impact financial or identity information.

## 4. Classification Rules

When classification is uncertain, users must apply the more protective reasonable classification until the Data Owner provides guidance.

Client or contractual requirements may require a stricter classification.

Users must not downgrade information merely to make it easier to share.

## 5. Handling Requirements

| Handling Activity | Public | Internal | Confidential | Restricted |
|---|---|---|---|---|
| Public disclosure | Allowed | Not allowed unless approved | Prohibited | Prohibited unless specifically authorized |
| Organizational storage | Allowed | Allowed | Approved systems only | Approved restricted systems only |
| External sharing | Allowed | Business need | Explicit authorization | Explicit authorization and appropriate controls |
| Personal email | Not authorized for business use | Prohibited for business use | Prohibited | Prohibited |
| Personal cloud storage | Not authorized for business use | Prohibited for business use | Prohibited | Prohibited |
| Unapproved AI service | May be used for public information only | Review required | Prohibited | Prohibited |
| Encryption in transit | Recommended | Required where practical | Required | Required |
| Encryption at rest | Recommended | Recommended | Required where supported | Required where supported |
| Access control | Minimal | Authenticated users | Least privilege | Strongest practical controls |
| Public repository | Allowed only when intentionally approved | Prohibited unless approved | Prohibited | Prohibited |

Public classification does not independently authorize use of personal accounts or personal services for business activity. The Technology Acceptable Use Policy still governs account and service use.

## 6. Collection and Minimization

Igzibo should collect and retain only information reasonably necessary for an authorized business purpose.

Users should avoid unnecessary copies, exports, downloads, retention, and collection of sensitive information.

## 7. Storage

Confidential and Restricted information must be stored only in approved systems appropriate to its sensitivity.

Such information must not be stored in personal email, personal cloud storage, personal repositories, unapproved applications, unapproved AI services, or public file-sharing locations.

## 8. Transmission and Sharing

Recipients must be verified before Confidential or Restricted information is transmitted.

Users must use encrypted or access-controlled transfer methods where appropriate.

External sharing requires a legitimate business purpose and minimum necessary information and access.

Public links must not be used for Confidential or Restricted information.

Access must be removed when no longer required.

## 9. Credentials and Secrets

Credentials, passwords, API keys, access tokens, private keys, certificates, and similar secrets are Restricted by default.

They must not be committed to source control, published publicly, sent through ordinary email, stored in plaintext documentation, or uploaded to unapproved services.

Secrets should be stored using an approved secrets-management mechanism.

## 10. Client Information

Client information must be handled according to applicable contracts and client security requirements.

If client requirements are stricter than this standard, the client requirement applies.

Client information must not be used for unrelated personal, educational, demonstration, marketing, or AI-training purposes.

## 11. AI and Automated Processing

Confidential and Restricted information must not be entered into an AI or automated-processing service unless the service and use case are approved.

Approval must consider retention, model training, human access, third-party transfers, deletion, contractual protections, and other relevant risks.

## 12. Retention and Disposal

Information should be retained only as long as necessary for legitimate business, legal, contractual, or operational requirements.

Legal holds, contractual requirements, investigations, and other mandatory preservation requirements take precedence over ordinary deletion.

Information no longer required should be securely deleted or destroyed using a method appropriate to its sensitivity.

## 13. Data Incidents

Accidental disclosure, loss, unauthorized access, or incorrect sharing of Confidential or Restricted information must be reported promptly.

Users must not conceal mistakes.

## 14. Data Ownership

Unless otherwise established by contract, organizational information created for Igzibo business is an organizational resource.

Client-owned information remains subject to client ownership and contractual requirements.

## 15. References

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- NIST Privacy Framework: https://www.nist.gov/privacy-framework

## 16. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-09-16 | Initial data classification and handling standard. |
| 2.0 | 2026-09-16 | Coordinated governance revision; corrected personal-account handling for Public information and standardized classification, handling, and terminology. |
