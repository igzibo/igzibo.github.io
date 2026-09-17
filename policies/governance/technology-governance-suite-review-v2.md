# Igzibo Technology Governance Suite Review

**Organization:** Igzibo Engineering Solutions, Inc.  
**Document:** `technology-governance-suite-review-v2.md`  
**Version:** 2.0  
**Status:** Living review record  
**Effective Date:** September 16, 2026  
**Owner:** Igzibo Engineering Solutions, Inc.  
**Review Cycle:** At least annually and whenever the governance framework materially changes

## Definitions

- **AUP** — Acceptable Use Policy, the high-level rules governing acceptable use of organizational technology.
- **AI** — Artificial Intelligence.
- **IAM** — Identity and Access Management.
- **NIST** — National Institute of Standards and Technology.
- **CISA** — Cybersecurity and Infrastructure Security Agency.
- **CSF** — Cybersecurity Framework.
- **C-SCRM** — Cybersecurity Supply Chain Risk Management.
- **MFA** — Multi-Factor Authentication.

## 1. Documents Reviewed

The coordinated review covered:

1. Technology Acceptable Use Policy.
2. Identity and Access Management Standard.
3. Data Classification and Handling Standard.
4. AI and Generative AI Usage Standard.
5. Technology and Third-Party Service Security Standard.

## 2. Review Objectives

The review evaluated:

- Cross-document consistency.
- Definitions and acronym handling.
- Mandatory versus recommended language.
- Technology neutrality.
- Overlapping requirements.
- Document precedence.
- Account and identity rules.
- Data handling.
- AI governance.
- Third-party risk.
- Lifecycle controls.
- Markdown cleanliness and absence of internal ChatGPT markup.

## 3. Key Corrections

### 3.1 Internal Markup

Internal ChatGPT citation and rendering artifacts were removed from the Technology and Third-Party Service Security Standard.

### 3.2 Public Information

The Data Classification and Handling Standard no longer treats personal email or personal cloud storage as generally authorized merely because information is classified Public.

Public classification describes information sensitivity. It does not authorize use of personal accounts or services for business activity.

### 3.3 Document Precedence

The AUP now establishes a clear precedence model and explains the relationship between the AUP and supporting standards.

### 3.4 Acronym Definitions

Important acronyms are defined early in each document under a dedicated Definitions section.

### 3.5 Technology Neutrality

Vendor-specific requirements are kept outside the governing policy framework wherever practical.

### 3.6 Risk Classification

The Technology and Third-Party Service Security Standard now uses risk factors rather than relying solely on examples.

### 3.7 Lifecycle Governance

Third-party services are governed through adoption, ownership, review, renewal, incident response, and termination.

## 4. Governance Relationships

The five documents form a layered framework:

```text
Technology Acceptable Use Policy
|
+-- Identity and Access Management Standard
|
+-- Data Classification and Handling Standard
|
+-- AI and Generative AI Usage Standard
|
+-- Technology and Third-Party Service Security Standard
```

The AUP establishes user-facing requirements.

The IAM Standard establishes identity and access controls.

The Data Classification and Handling Standard establishes information sensitivity and handling requirements.

The AI Standard establishes AI-specific requirements.

The Technology and Third-Party Service Security Standard establishes requirements for selecting and managing technology and external providers.

## 5. Research Basis

The coordinated revision considered current NIST and CISA guidance, including:

- NIST Cybersecurity Framework 2.0.
- NIST AI Risk Management Framework.
- NIST Generative AI Profile.
- NIST Cybersecurity Supply Chain Risk Management guidance.
- CISA Identity and Access Management guidance.
- CISA secure-by-demand procurement guidance.

The NIST Cybersecurity Framework 2.0 is designed as a flexible taxonomy of cybersecurity outcomes rather than a prescriptive control set. NIST's supply-chain guidance emphasizes identifying, assessing, and mitigating risks throughout the technology supply chain. NIST's Generative AI Profile addresses risk management across the generative AI lifecycle.

## 6. Remaining Future Work

The governance suite should eventually be supplemented with implementation procedures and standards such as:

1. Security Incident Response Procedure.
2. Employee and Contractor Offboarding Procedure.
3. Device and Remote Access Standard.
4. Password and Authentication Standard, if separate treatment becomes necessary.
5. Backup and Business Continuity Standard.
6. Technology and Third-Party Service Approval Procedure.
7. Records Retention and Disposal Standard.
8. Privacy and Personal Information Standard.
9. Secure Software Development Standard.
10. Platform-specific security configuration standards.

These should remain subordinate to the technology-neutral governance framework.

## 7. Version History

| Version | Date | Summary |
|---|---|---|
| 2.0 | 2026-09-16 | Coordinated review of the five-document governance suite and documentation of corrections and remaining work. |
