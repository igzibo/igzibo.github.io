# Technology and Third-Party Service Security Standard

**Organization:** Igzibo Engineering Solutions, Inc.  
**Document:** `technology-and-third-party-service-security-standard-v2.md`  
**Version:** 2.0  
**Status:** Living standard  
**Effective Date:** September 16, 2026  
**Owner:** Igzibo Engineering Solutions, Inc.  
**Review Cycle:** At least annually and after material security, legal, contractual, or technology changes

## 1. Purpose

This standard establishes minimum security requirements for selecting, evaluating, approving, implementing, using, monitoring, renewing, and retiring technology products and third-party services used by Igzibo.

It is vendor-neutral and applies regardless of whether a service is provided by Google, Microsoft, Amazon, GitHub, a payroll provider, recruiting platform, AI provider, software vendor, independent contractor, or another third party.

The standard complements the Technology Acceptable Use Policy, Identity and Access Management Standard, Data Classification and Handling Standard, and AI and Generative AI Usage Standard.

## Definitions

- **AI** — Artificial Intelligence, technology capable of performing tasks commonly associated with human intelligence.
- **CISA** — Cybersecurity and Infrastructure Security Agency, a U.S. government agency that provides cybersecurity guidance and resources.
- **Igzibo** — Igzibo Engineering Solutions, Inc.
- **MFA** — Multi-Factor Authentication, authentication requiring two or more independent authentication factors.
- **NIST** — National Institute of Standards and Technology, a U.S. government agency that publishes cybersecurity and technology guidance.
- **Organizational Resource** — Any technology, account, system, service, device, information asset, or other resource owned, licensed, administered, funded, or authorized by Igzibo.

- **API** — Application Programming Interface, a defined mechanism through which software systems communicate.
- **SaaS** — Software as a Service, software delivered and operated by a provider rather than entirely by the customer.
- **C-SCRM** — Cybersecurity Supply Chain Risk Management, the process of identifying, assessing, and managing cybersecurity risks arising from technology products, services, suppliers, and dependencies.
- **Third Party** — An organization or individual outside Igzibo that provides technology, services, access, data processing, or other capabilities.
- **Technology Service** — A software, hardware, cloud, hosted, managed, or technology-enabled product or service used for business purposes.
- **Service Owner** — The person responsible for the business purpose, configuration, access, risk, and continued need for a Technology Service.
- **Security Review** — A documented evaluation of security, privacy, access, data, operational, and contractual risks.
- **Due Diligence** — Reasonable investigation performed before entering into or materially expanding a relationship with a provider.
- **SSO** — Single Sign-On, an authentication mechanism allowing an authorized identity to access multiple services through a centralized identity system.
- **RBAC** — Role-Based Access Control, assigning permissions according to defined roles.
- **DPA** — Data Processing Agreement, a contract defining how a provider may process information on behalf of an organization.
- **SLA** — Service Level Agreement, contractual commitments concerning service availability, performance, support, or response.
- **SOW** — Statement of Work, a document defining the scope, deliverables, responsibilities, and terms of an engagement.
- **SBOM** — Software Bill of Materials, a record of software components and dependencies included in a software product.
- **Critical Service** — A service whose significant interruption, compromise, or loss could materially affect Igzibo operations, clients, security, finances, or legal obligations.

## 2. Scope

This standard applies to:

- Software and cloud services.
- SaaS platforms.
- Infrastructure and hosting providers.
- APIs.
- Browser extensions and plugins.
- AI services.
- Developer tools.
- Code repositories and package registries.
- Collaboration and document platforms.
- Email and identity services.
- Payroll and human resources systems.
- Recruiting and staffing platforms.
- Financial and payment platforms.
- Security products.
- Managed service providers.
- Consultants and technology contractors.
- Technology suppliers and resellers.
- Any third-party service that receives Igzibo information or connects to an Igzibo system.

It applies to paid, free, and trial services.

## 3. Governance Principles

Igzibo will apply these principles:

1. Security must be considered before adoption.
2. Review requirements must be proportional to risk.
3. Information sensitivity must influence review depth.
4. Access must follow least privilege.
5. Every material service must have an accountable owner.
6. Organizational accounts must be controlled by Igzibo rather than dependent on personal identities.
7. Critical services require continuity and exit planning.
8. Contracts should address security and data-handling requirements appropriate to risk.
9. Services must be reviewed throughout their lifecycle.
10. Igzibo should maintain visibility into material third-party dependencies.

These principles are consistent with NIST Cybersecurity Framework 2.0 and NIST Cybersecurity Supply Chain Risk Management guidance.

## 4. Technology Inventory

Igzibo should maintain an inventory of material Technology Services.

The inventory should identify, where applicable:

- Service name.
- Provider.
- Service Owner.
- Business purpose.
- Data classification.
- Users.
- Integrations.
- Administrative accounts.
- Contract owner.
- Renewal date.
- Criticality.
- Security review status.
- Known dependencies.
- Termination or exit requirements.

The inventory should include materially important free and trial services.

## 5. Service Ownership

Every material Technology Service must have an identifiable Service Owner.

The Service Owner is responsible for:

- Confirming business need.
- Maintaining appropriate access.
- Ensuring authorized use.
- Coordinating security review.
- Reviewing integrations.
- Monitoring continued business need.
- Coordinating renewal or termination.
- Ensuring information can be recovered or transferred when necessary.

A material service should not be adopted without an accountable owner.

## 6. Risk Classification

Technology Services must be classified as Low, Moderate, High, or Critical.

Risk classification must consider at least:

- Information sensitivity.
- Number and type of users.
- Administrative privileges.
- Identity-system access.
- Production-system access.
- Financial or personnel information.
- Client information.
- Business continuity impact.
- Regulatory or contractual obligations.
- External integrations.
- Provider concentration or lock-in.
- Security maturity and available assurance.
- Consequences of compromise or outage.

### 6.1 Low Risk

A service is generally Low Risk when it handles only Public information, has limited organizational impact, and does not receive privileged access or sensitive information.

### 6.2 Moderate Risk

A service is generally Moderate Risk when it handles Internal information, supports ordinary business operations, or has limited integrations without privileged access.

### 6.3 High Risk

A service is generally High Risk when it:

- Processes Confidential or Restricted information.
- Processes client information.
- Accesses organizational identities.
- Connects to production systems.
- Processes financial, personnel, or sensitive information.
- Has administrative capabilities.
- Is materially important to business operations.

### 6.4 Critical

A service is Critical when significant interruption, compromise, or loss could materially affect core operations, clients, security, finances, legal obligations, or access to other critical systems.

Examples may include primary identity, email, core source control, payroll, core financial systems, and critical production infrastructure.

When multiple criteria apply, the higher reasonable risk classification must be used unless an authorized risk decision documents otherwise.

## 7. Pre-Adoption Review

Before adopting a Moderate-, High-, or Critical-Risk service, Igzibo should evaluate:

### Provider

- Legal business identity.
- Operating jurisdictions.
- Relevant experience.
- Security history.
- Material public security incidents.
- Operational and financial stability where relevant.

### Security

- MFA.
- Administrative controls.
- Logging.
- Encryption.
- Vulnerability management.
- Security testing.
- Incident response.
- Security documentation.
- Independent assurance where appropriate.

### Data

- Information collected.
- Business purpose.
- Storage and processing locations.
- Access by provider personnel.
- Retention.
- Training or product-improvement use.
- Export capability.
- Deletion capability.
- End-of-contract treatment.

### Integration

- Information accessed.
- Actions performed.
- Requested permissions.
- Identity access.
- Cloud-storage access.
- Source-code access.
- Financial access.
- Persistent tokens or credentials.

### Continuity

- Provider outage impact.
- Data export.
- Alternative providers.
- Recovery process.
- Migration difficulty.
- Contractual notice periods.

Security review should be proportional to risk. CISA Secure by Demand guidance supports considering security capabilities during procurement rather than treating security solely as a vendor responsibility.

## 8. Free and Trial Services

Free and trial services are subject to the same security principles as paid services.

Users must not assume that a free service is suitable for organizational information.

Confidential or Restricted information must not be uploaded to a free or trial service without authorization.

Trial accounts must not become permanent business systems without appropriate ownership and review.

## 9. Third-Party Account Creation

Business accounts created with third-party services must:

- Have an authorized business purpose.
- Use an Organizational Account where practical.
- Be owned or controlled by Igzibo.
- Have an identifiable Service Owner.
- Use MFA where available.
- Avoid dependency on personal email.
- Avoid dependency on personal payment accounts.
- Have a documented recovery method.

Users must not create Personal Accounts using Igzibo identities.

## 10. Third-Party Integrations and Delegated Access

Integrations must be reviewed according to the information and permissions they require.

Users must not approve an integration merely because a service requests it.

Before approval, determine:

- What information can be accessed.
- What actions can be performed.
- Whether access can be limited.
- Whether persistent tokens are created.
- Whether access can be revoked.
- Whether access exceeds the immediate business purpose.

Unused integrations must be removed.

OAuth, where used, must be configured with the minimum permissions necessary.

Broad access to email, cloud storage, source repositories, or administrative functions requires heightened review.

## 11. Contractual Requirements

High-risk and critical services should have written contractual terms appropriate to risk.

Where applicable, agreements should address:

- Confidentiality.
- Data ownership.
- Data processing.
- Security requirements.
- Incident notification.
- Breach response.
- Subcontractors.
- Data location.
- Data retention.
- Data deletion.
- Data export.
- Availability.
- Support.
- Termination.
- Transition assistance.
- Assurance or audit information.

A DPA should be considered when a provider processes personal information on behalf of Igzibo or a client.

An SLA should be considered when availability or response times are material to operations.

## 12. Client Requirements

Client contracts and security requirements must be reviewed before using a third-party service for client information.

Client restrictions on cloud providers, AI services, data locations, subcontractors, repositories, software, or integrations must be followed.

Igzibo approval of a service does not override a client-specific restriction.

## 13. Software Supply Chain

Software obtained from third parties must be evaluated according to risk.

For material software, Igzibo should consider:

- Publisher and source.
- Version.
- Update history.
- Known vulnerabilities.
- Dependencies.
- Package integrity.
- Signatures or checksums where available.
- Security advisories.
- End-of-support status.
- Licensing.
- SBOM availability where appropriate.

NIST SP 800-161 Rev. 1, including the November 2024 update, provides guidance for identifying, assessing, and mitigating cybersecurity supply-chain risks.

## 14. Open-Source Software

Open-source software may be used when appropriate.

Material components should be evaluated for:

- License requirements.
- Known vulnerabilities.
- Maintainer activity.
- Dependency health.
- Package authenticity.
- Update practices.
- Production suitability.

Open-source software must not be treated as inherently safe or unsafe solely because it is open source.

## 15. Developer Tools and Browser Extensions

Developer tools, browser extensions, plugins, and command-line utilities must be evaluated for:

- File access.
- Credential access.
- Network access.
- Source-code access.
- Data transmission.
- Telemetry.
- Downloaded-code execution.
- Elevated privileges.

Tools that bypass organizational security controls must not be installed.

## 16. AI Services

AI services are subject to this standard and the AI and Generative AI Usage Standard.

Before approving an AI service for business information, Igzibo should evaluate data retention, model-improvement practices, human access, security controls, account ownership, deletion, export, subprocessors, integration permissions, and client restrictions.

AI services capable of taking actions through connected tools require heightened review.

## 17. Security Assurance

For higher-risk services, Igzibo may request or review available security evidence, such as independent assessments, security certifications, penetration-testing summaries, vulnerability-management information, incident-response documentation, architecture documentation, and privacy documentation.

The absence of a certification does not automatically disqualify a provider.

Assurance requirements must be proportional to risk.

## 18. Provider Security Incidents

Material provider security incidents must be evaluated promptly.

The Service Owner should determine whether:

- Igzibo information may be affected.
- Client information may be affected.
- Credentials or tokens must be revoked.
- The service should be disabled.
- Contractual notification requirements apply.
- Clients or other parties must be notified.
- An alternative service is required.

## 19. Vulnerability and Patch Management

Technology services and software must be maintained reasonably current.

Critical security updates should be prioritized.

Unsupported software must not be used for critical business functions without documented risk acceptance and compensating controls.

## 20. Data Location and Transfer

For Confidential, Restricted, or client information, Igzibo should understand where information is stored and processed when relevant to legal, contractual, privacy, or security requirements.

International transfers must comply with applicable legal and contractual requirements.

## 21. Business Continuity and Exit Planning

Critical Services must have a reasonable exit strategy.

Where practical, Igzibo should know:

- How data can be exported.
- Export formats.
- Who controls administrative access.
- How credentials can be recovered.
- How integrations can be disconnected.
- How users can be migrated.
- How information can be deleted after migration.
- Contractual notice periods.
- Material migration dependencies.

Vendor lock-in must be considered when it could materially affect continuity.

## 22. Renewal Review

Renewal is not automatic approval.

For High-Risk and Critical services, the Service Owner should periodically confirm:

- Continued business need.
- Appropriate security.
- Appropriate access.
- Acceptable data handling.
- Acceptable contractual terms.
- Material incidents or changes.
- Continued ability to exit or migrate.

## 23. Termination

When a service is retired:

1. Revoke user access.
2. Revoke administrative access.
3. Revoke API credentials and tokens.
4. Disable integrations.
5. Export required information.
6. Preserve information subject to retention or legal requirements.
7. Delete information according to contractual and organizational requirements.
8. Close or cancel the service.
9. Update the technology inventory.
10. Document material termination activities.

## 24. Exceptions

Exceptions require documented authorization and must identify the affected service, requirement, business justification, duration, risk, and compensating controls.

## 25. Enforcement

Failure to follow this standard may result in service suspension, access restriction, additional training, contractual action, employment action where applicable, or other appropriate measures.

## 26. References

- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20
- NIST SP 800-161 Rev. 1, updated November 2024: https://csrc.nist.gov/pubs/sp/800/161/r1/upd1/final
- NIST Cybersecurity Supply Chain Risk Management publications: https://csrc.nist.gov/Projects/cyber-supply-chain-risk-management/publications
- CISA: https://www.cisa.gov/

## 27. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-09-16 | Initial technology and third-party service security standard. |
| 2.0 | 2026-09-16 | Coordinated governance revision; removed internal citation artifacts, standardized terminology, strengthened risk-classification criteria, clarified service lifecycle requirements, and aligned supply-chain references with current NIST guidance. |
