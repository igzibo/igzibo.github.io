# Secure Software Development Standard

**Organization:** Igzibo Engineering Solutions, Inc.  
**Version:** 1.0  
**Status:** Living policy  
**Effective Date:** September 16, 2026  
**Owner:** Igzibo Engineering Solutions, Inc.  
**Review Cycle:** At least annually and after material changes to applicable law, client requirements, technology, or business operations.

## 1. Purpose

Establishes baseline requirements for secure planning, design, development, testing, release, maintenance, and retirement of software.

## 2. Scope

Employees, contractors, consultants, engineers, developers, project managers, R&D personnel, and third parties performing software development for Igzibo where contractually applicable.

## Definitions

**AI (Artificial Intelligence):** A machine-based system capable of generating predictions, recommendations, decisions, content, or other outputs based on inputs.
**CI/CD (Continuous Integration and Continuous Delivery or Deployment):** Processes used to build, test, validate, and deliver software changes.
**Dependency:** A software component, package, library, service, or other external component required by software.
**Igzibo:** Igzibo Engineering Solutions, Inc.
**R&D (Research and Development):** Research, experimentation, prototyping, engineering investigation, or development of products, services, methods, or technologies.
**SDLC (Software Development Life Cycle):** Activities used to plan, design, develop, test, release, operate, maintain, and retire software.

## 3. Core Principles

Software development must use authorized repositories and environments; protect secrets and sensitive information; control dependencies; apply appropriate testing and review; preserve client and intellectual-property restrictions; and address material vulnerabilities.

## 4. Planning and Design

Projects should identify security, privacy, contractual, data-classification, intellectual-property, availability, authentication, authorization, logging, and recovery requirements. Higher-risk systems should document material security decisions.

## 5. Source Code, Secrets, and Dependencies

Source code must reside in approved repositories. Passwords, tokens, API keys, private keys, and other secrets must not be committed or placed in public or unauthorized systems. Dependencies must come from legitimate sources and comply with license and security requirements.

## 6. Secure Implementation

Development should apply input validation, safe output handling, secure authentication and authorization, safe error handling, appropriate cryptography, dependency controls, and secure defaults.

## 7. Review, Testing, and CI/CD

Material changes should receive appropriate review and testing. Testing may include unit, integration, regression, security, static, dynamic, dependency, and manual testing. CI/CD identities and credentials must be protected and release changes controlled.

## 8. Vulnerability and Release Management

Material vulnerabilities must be assessed and remediated or formally accepted. Before release, teams should confirm testing, approvals, security findings, configuration, rollback or recovery capability, and client requirements.

## 9. Production Data and AI

Production or client data must not be copied into development or testing without authorization. AI-assisted development must comply with the AI and Generative AI Usage Standard and requires human review for material code.

## 10. Maintenance, Retirement, and Incidents

Retirement must address access, credentials, data, dependencies, client obligations, and ownership records. Software vulnerabilities and security incidents must be reported under the Security Incident Response Procedure.

## 11. Exceptions and Enforcement

Exceptions require documented authorization identifying risk, safeguards, duration, and authority. Violations may result in corrective action, access restrictions, contractual remedies, or termination.

## 12. References and Research Basis

- National Institute of Standards and Technology (NIST), [Secure Software Development Framework (SSDF) Version 1.1, SP 800-218](https://csrc.nist.gov/pubs/sp/800/218/final).
- NIST, [Cybersecurity Framework (CSF) 2.0](https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20).

NIST published a draft revision of SP 800-218 in 2025. This standard uses the final version 1.1 unless a later final version is formally adopted by Igzibo.

## Version History

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-09-16 | Initial secure software development standard. |
