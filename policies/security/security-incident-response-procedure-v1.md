# Security Incident Response Procedure

**Organization:** Igzibo Engineering Solutions, Inc.  
**Version:** 1.0  
**Status:** Living procedure  
**Effective Date:** September 16, 2026  
**Owner:** Igzibo Engineering Solutions, Inc.  
**Review Cycle:** At least annually and after any material security incident, material organizational change, or material change to applicable legal, regulatory, contractual, or client requirements.

## 1. Purpose

This procedure establishes the process Igzibo Engineering Solutions, Inc. uses to identify, report, assess, contain, investigate, recover from, and learn from security incidents.

The procedure operationalizes the incident-reporting and security requirements established by the Technology Acceptable Use Policy, Identity and Access Management Standard, Data Classification and Handling Standard, AI and Generative AI Usage Standard, and Technology and Third-Party Service Security Standard.

The procedure is designed to support a consistent response while remaining technology-neutral. Specific platform, vendor, cloud, endpoint, logging, and security-tool instructions should be maintained in separate implementation procedures or runbooks.

## 2. Scope

This procedure applies to:

- Employees, contractors, consultants, and other authorized users.
- Organizational accounts and identities.
- Devices, applications, source-code repositories, cloud services, SaaS services, APIs, and other organizational resources.
- Information owned, controlled, processed, or entrusted to Igzibo.
- Client information and client environments where Igzibo has an incident-response obligation.
- Third-party services and providers that process Igzibo information or connect to organizational resources.
- AI systems, AI agents, models, RAG systems, and related services used for business purposes.
- Suspected, attempted, or confirmed security incidents.

This procedure does not replace contractual, regulatory, legal, client, or law-enforcement reporting requirements. Where another requirement is more restrictive, the more restrictive requirement applies unless prohibited by law.

## 3. Definitions

**AI (Artificial Intelligence):** A machine-based system capable of generating predictions, recommendations, decisions, content, or other outputs based on inputs.

**CISA (Cybersecurity and Infrastructure Security Agency):** A U.S. government agency that publishes cybersecurity guidance and incident-response resources.

**Confidential Information:** Information that requires controlled access because unauthorized disclosure, alteration, or loss could create meaningful business, contractual, privacy, security, or client impact.

**Incident:** A suspected or confirmed event that may compromise the confidentiality, integrity, or availability of information, systems, accounts, services, or business operations.

**Incident Coordinator:** The person assigned to coordinate response activities, maintain the incident record, and ensure appropriate escalation.

**Incident Record:** The controlled record containing incident facts, decisions, actions, evidence references, communications, and closure information.

**Indicator of Compromise (IOC):** Observable evidence that may indicate malicious or unauthorized activity, such as a suspicious address, file, process, domain, account activity, or authentication event.

**Information Security Incident:** An incident involving actual or suspected unauthorized access, disclosure, alteration, destruction, loss, misuse, disruption, or compromise of information or technology resources.

**NIST (National Institute of Standards and Technology):** A U.S. government organization that publishes cybersecurity and technology guidance.

**Personal Information:** Information relating to an identified or identifiable person.

**Restricted Information:** Information requiring the highest level of protection under the Data Classification and Handling Standard.

**Security Event:** An observable occurrence in a system, service, account, device, or environment that may be relevant to security.

**Security Incident:** A security event that has been determined, or reasonably suspected, to require investigation or response.

**Third Party:** An external organization or individual that provides a service, product, system, personnel, or other capability to Igzibo.

**Triage:** The initial process of validating a report, determining its significance, establishing scope, and assigning response priority.

## 4. Relationship to Other Governance Documents

This procedure operates within the Igzibo technology governance framework.

The following documents establish related requirements:

1. Technology Acceptable Use Policy.
2. Identity and Access Management Standard.
3. Data Classification and Handling Standard.
4. AI and Generative AI Usage Standard.
5. Technology and Third-Party Service Security Standard.
6. Security Incident Response Procedure.

The Security Incident Response Procedure establishes how incidents are handled. It does not independently change the classification, access, acceptable-use, AI, or third-party security requirements established by the other documents.

Client contracts, statements of work, data-processing agreements, applicable laws, regulations, and other binding requirements may impose additional notification, preservation, investigation, or reporting obligations.

## 5. Incident Response Principles

Igzibo's incident response process follows these principles:

- Report suspected security incidents promptly.
- Protect people, clients, information, and critical business operations.
- Preserve evidence before taking actions that could destroy or alter it when practical.
- Contain active threats as quickly as reasonably possible.
- Use the minimum access necessary to investigate and respond.
- Maintain an accurate incident record.
- Separate confirmed facts from assumptions and unverified reports.
- Escalate incidents based on actual or reasonably anticipated impact.
- Protect confidential and restricted information during the response.
- Coordinate with affected clients and third parties when required.
- Do not make unauthorized public statements about incidents.
- Restore services only after reasonable security checks have been completed.
- Capture lessons learned and corrective actions.

## 6. Roles and Responsibilities

### 6.1 Incident Coordinator

The Incident Coordinator is responsible for coordinating the response and maintaining the incident record.

Responsibilities include:

- Establishing the incident record.
- Confirming the initial classification and priority.
- Assigning response tasks.
- Coordinating technical, business, legal, client, and third-party activities as appropriate.
- Maintaining a timeline of material actions and decisions.
- Tracking containment, eradication, recovery, and follow-up actions.
- Coordinating closure and lessons learned.

One person may perform multiple roles when the size of the incident or organization makes separate assignments impractical.

### 6.2 Technology or Security Responder

The responder performs technical investigation and response activities appropriate to the incident.

Responsibilities may include:

- Validating indicators and suspicious activity.
- Reviewing relevant logs and security information.
- Identifying affected accounts, devices, applications, services, and data.
- Containing affected resources.
- Removing malicious or unauthorized access.
- Restoring systems.
- Identifying additional indicators of compromise.
- Documenting technical findings.

### 6.3 Data Owner or Business Owner

The relevant Data Owner or business owner helps determine business impact, information sensitivity, client impact, and required business decisions.

### 6.4 Management

Management provides decisions and resources when an incident could materially affect business operations, clients, finances, legal obligations, personnel, reputation, or contractual commitments.

### 6.5 Legal and Privacy Support

Legal or privacy support should be engaged when appropriate, including incidents involving:

- Personal information.
- Confidential or restricted information.
- Client information.
- Potential regulatory obligations.
- Contractual notification requirements.
- Litigation, investigation, or legal holds.
- Law-enforcement requests.
- Potential material legal exposure.

Igzibo should obtain qualified legal advice when legal obligations are uncertain or material.

### 6.6 Third-Party Providers

Third-party providers must participate in incident response when their services, systems, personnel, or information are involved.

Service owners should use applicable contractual contacts and escalation procedures.

## 7. Incident Reporting

Any person who reasonably suspects a security incident must report it promptly through the designated Igzibo security or management reporting channel.

Examples include:

- Lost or stolen organizational devices.
- Suspected account compromise.
- Unexpected authentication activity.
- Accidental disclosure of confidential information.
- Malware or ransomware indicators.
- Unauthorized access.
- Suspicious email or messaging activity.
- Exposure of credentials, tokens, keys, or secrets.
- Unauthorized source-code or repository access.
- Suspicious changes to production systems.
- Security issues involving an AI service or AI agent.
- Suspected compromise of a third-party service.
- Client notification of suspected compromise involving Igzibo.
- Any event that could materially affect confidentiality, integrity, or availability.

Users should report suspected incidents even when they are uncertain whether an actual incident occurred.

A user should not delay reporting in order to complete an investigation independently.

## 8. Initial Response

Upon receiving a report, the Incident Coordinator or designated responder should:

1. Record the report.
2. Record the date and time received.
3. Identify the reporter and affected business area when known.
4. Record the known facts without speculation.
5. Determine whether immediate containment is required.
6. Identify potentially affected systems, accounts, services, information, and third parties.
7. Determine whether evidence should be preserved before remediation.
8. Assign an initial priority.
9. Escalate when required.

If an incident is actively causing harm, reasonable containment actions may begin before the investigation is complete.

## 9. Incident Classification and Priority

Incident priority should consider:

- Information classification.
- Number and type of affected users.
- Client impact.
- Whether privileged accounts are involved.
- Whether credentials or authentication mechanisms are compromised.
- Whether production systems are affected.
- Potential financial impact.
- Potential legal or regulatory impact.
- Business continuity impact.
- Scope and duration.
- Whether the threat remains active.
- Whether the incident may spread to other systems or organizations.
- Contractual or client notification deadlines.

### 9.1 Priority 1: Critical

Use Priority 1 when an incident presents a material and potentially immediate threat to critical operations, significant client information, Restricted Information, privileged access, or major business functions.

Examples may include:

- Active ransomware affecting critical systems.
- Confirmed compromise of a highly privileged organizational identity.
- Confirmed material disclosure of Restricted Information.
- Active compromise of a critical production service.
- A significant incident affecting multiple clients or core business operations.

### 9.2 Priority 2: High

Use Priority 2 when the incident has substantial security, client, operational, financial, or contractual impact but does not meet the Priority 1 threshold.

Examples may include:

- Confirmed compromise of a standard organizational account.
- Unauthorized access to Confidential Information.
- Significant compromise of a third-party service.
- Malware affecting an important business device or service.

### 9.3 Priority 3: Moderate

Use Priority 3 when the incident has limited scope or impact and does not currently present a significant threat to critical operations or highly sensitive information.

Examples may include:

- A contained malware event.
- A suspected account compromise that was blocked promptly.
- Limited unauthorized access with no evidence of sensitive-data exposure.

### 9.4 Priority 4: Low

Use Priority 4 for events requiring review but presenting limited apparent risk.

Examples may include:

- Low-risk policy violations.
- Benign security alerts after investigation.
- Isolated suspicious activity with no evidence of compromise.

Priority may be increased or decreased as facts become available.

## 10. Investigation and Analysis

The responder should establish what happened, what was affected, and whether the threat remains active.

Investigation should consider:

- Initial entry point.
- Affected identities.
- Authentication activity.
- Affected devices and systems.
- Affected applications and services.
- Data involved.
- Time period.
- Actions performed by the attacker or unauthorized user.
- Indicators of compromise.
- Persistence mechanisms.
- Lateral movement.
- Privilege escalation.
- Data access or exfiltration.
- Impact to availability or integrity.
- Third-party involvement.
- Client involvement.
- Remaining exposure.

Investigation records should distinguish:

- Confirmed facts.
- Reasonable findings.
- Unverified reports.
- Working hypotheses.
- Unknowns requiring further investigation.

## 11. Evidence Preservation

When practical, evidence should be preserved before destructive remediation actions.

Potential evidence includes:

- Authentication and access logs.
- Application and system logs.
- Security alerts.
- Email or messaging records.
- Relevant source-code or repository activity.
- File metadata.
- Network information.
- Cloud audit records.
- Device information.
- Screenshots or other observations.
- Relevant communications.
- Third-party incident records.

Evidence should be handled in a manner appropriate to its sensitivity and potential legal or investigative use.

Personnel should not alter, delete, or overwrite relevant evidence unnecessarily.

When a legal hold, investigation, or regulatory preservation requirement applies, the response should follow the applicable direction from qualified legal counsel or the responsible authority.

## 12. Containment

Containment is intended to prevent further unauthorized activity while preserving the ability to investigate and recover.

Depending on the incident, containment may include:

- Disabling or restricting compromised accounts.
- Revoking sessions, tokens, keys, or credentials.
- Isolating affected devices.
- Restricting network or application access.
- Suspending compromised integrations.
- Disabling malicious automation.
- Blocking identified indicators.
- Restricting affected third-party services.
- Removing public exposure.
- Temporarily suspending affected business processes.

Containment actions should be proportionate to the risk and documented in the incident record.

For high-impact incidents, the Incident Coordinator should consider whether containment could destroy evidence or interfere with legal, contractual, or client requirements before taking irreversible actions, unless immediate action is necessary to prevent ongoing harm.

## 13. Eradication

After reasonable containment and investigation, the responder should remove the cause or mechanism of compromise.

Depending on the incident, eradication may include:

- Removing malicious software.
- Removing unauthorized accounts or access.
- Rotating credentials and secrets.
- Removing persistence mechanisms.
- Correcting exploited configuration weaknesses.
- Patching affected software.
- Rebuilding compromised systems.
- Removing unauthorized integrations.
- Replacing compromised credentials, keys, or certificates.
- Correcting access-control weaknesses.

Eradication should address the underlying cause where reasonably possible rather than only removing visible symptoms.

## 14. Recovery

Recovery restores affected services to normal operation while reducing the likelihood of recurrence.

Before returning affected systems or services to normal operation, the responder should determine, as appropriate:

- Whether the threat has been contained.
- Whether unauthorized access has been removed.
- Whether required credentials and secrets have been rotated.
- Whether affected systems have been patched or rebuilt.
- Whether security controls are operating as expected.
- Whether data integrity has been reasonably validated.
- Whether monitoring has been increased.
- Whether clients or third parties require notification.
- Whether business owners approve restoration.

Recovery actions should be documented.

For critical services, recovery should be coordinated with applicable business continuity and backup procedures.

## 15. Communications and Notifications

Incident communications must be accurate, controlled, and appropriate to the audience.

### 15.1 Internal Communications

Internal communications should provide personnel with information necessary to perform their responsibilities.

Personnel should not speculate about the cause, scope, responsible party, or impact of an incident.

### 15.2 Client Communications

Client notifications must follow applicable contracts, statements of work, data-processing agreements, client security requirements, and other binding obligations.

When notification is required, the communication should be coordinated with the appropriate business and legal personnel.

### 15.3 Third-Party Communications

When a third-party provider is involved, the service owner should use the provider's established security or incident-response contact when appropriate.

### 15.4 External and Public Communications

Only authorized personnel may communicate externally on behalf of Igzibo about a security incident.

Public statements should not disclose confidential, restricted, client, investigative, or legally protected information without appropriate authorization.

## 16. Credentials and Identity Response

When an incident may involve credentials or identities, response should consider:

- Disabling compromised accounts.
- Revoking active sessions.
- Resetting passwords where applicable.
- Rotating API keys, tokens, certificates, or other secrets.
- Reviewing recent authentication activity.
- Reviewing privilege changes.
- Reviewing newly created accounts.
- Reviewing delegated access and third-party integrations.
- Reviewing service accounts.
- Requiring additional authentication controls where appropriate.

Credential rotation should account for dependencies so that legitimate services are not unintentionally disrupted.

## 17. Data Exposure Response

When information may have been accessed, disclosed, altered, or destroyed, the response should determine:

- What data was involved.
- Its classification.
- Whose information was involved.
- Whether client information was involved.
- Whether the information was actually accessed or only potentially exposed.
- The relevant time period.
- The likely scope of access.
- Whether copies may exist outside Igzibo's control.
- Applicable contractual, legal, regulatory, or client notification requirements.

Data incidents should be coordinated with the Data Owner and appropriate legal or privacy support.

## 18. AI-Related Incidents

Incidents involving AI systems, AI providers, AI agents, RAG systems, model integrations, or AI-generated code should be handled under this procedure and the AI and Generative AI Usage Standard.

Examples include:

- Unauthorized disclosure through an AI service.
- Prompt or output exposure of Confidential or Restricted Information.
- Compromise of an AI provider account.
- Unauthorized AI agent actions.
- Excessive permissions granted to an AI agent.
- Prompt injection leading to unauthorized actions or disclosure.
- Compromise of an AI-connected integration.
- Malicious or unauthorized code generated or deployed through an AI-assisted workflow.
- Model, retrieval, or tool behavior that creates a material security impact.

Where an AI system can take actions in business systems, responders should consider both the AI system and the connected identities, tools, data sources, and downstream systems.

## 19. Third-Party Incidents

When a third-party service reports or is suspected of experiencing an incident affecting Igzibo, the Service Owner should:

1. Obtain the provider's available incident information.
2. Identify affected Igzibo accounts, integrations, systems, and data.
3. Determine whether access should be restricted or suspended.
4. Review available logs and provider evidence.
5. Determine whether client information is affected.
6. Review contractual notification obligations.
7. Record provider communications and response actions.
8. Track remediation and required follow-up.
9. Reassess the service's security risk before normal use resumes.

Third-party incident handling should be coordinated with the Technology and Third-Party Service Security Standard.

## 20. Client Incidents and Client Systems

When Igzibo personnel discover a security incident involving a client environment, the response must follow the applicable client agreement and authorized procedures.

Igzibo personnel must not independently access, modify, investigate, contain, or restore client systems beyond their authorized scope.

If the client's instructions are unclear, the issue should be escalated to the designated client contact and appropriate Igzibo management.

## 21. Incident Closure

An incident may be closed when the Incident Coordinator determines that:

- Immediate threats have been contained.
- Required eradication actions are complete or appropriately tracked.
- Recovery is complete or has transitioned to normal operational work.
- Required notifications have been completed or assigned.
- Evidence and incident records are preserved as required.
- Outstanding risks have owners and due dates.
- Required client or third-party actions are documented.
- Lessons learned have been captured when appropriate.

Closure should record:

- Incident identifier.
- Dates and times.
- Summary.
- Root cause or most likely cause when known.
- Affected systems and information.
- Business and client impact.
- Containment actions.
- Eradication actions.
- Recovery actions.
- Notifications.
- Evidence references.
- Corrective actions.
- Open risks.
- Incident owner.
- Closure date.

## 22. Post-Incident Review

A post-incident review should be performed for material incidents and may be performed for lower-priority incidents when useful.

The review should consider:

- What happened.
- What worked.
- What did not work.
- Detection effectiveness.
- Response effectiveness.
- Communication effectiveness.
- Control failures.
- Process failures.
- Training gaps.
- Technology gaps.
- Third-party issues.
- Required policy or standard changes.
- Required technical remediation.
- Required monitoring improvements.

The purpose of the review is to improve security and response capability, not to assign blame.

## 23. Corrective and Preventive Actions

Corrective actions should be tracked to completion when material.

Actions may include:

- Access-control changes.
- Credential rotation.
- Security configuration changes.
- Patching.
- Architecture changes.
- Monitoring improvements.
- Data-handling changes.
- Vendor changes.
- Contractual changes.
- Training.
- Policy or standard updates.
- New procedures or runbooks.
- Backup or recovery improvements.

Each material action should have an owner and target completion date.

Risk acceptance or deferred remediation must follow the applicable exception process.

## 24. Incident Records and Retention

Incident records should be stored in an authorized organizational resource with access limited to personnel who require the information.

Incident records may contain highly sensitive information and should be classified and handled according to the Data Classification and Handling Standard.

Records should include enough information to support:

- Investigation.
- Client or contractual reporting.
- Regulatory or legal review where applicable.
- Internal accountability.
- Lessons learned.
- Future incident response.

Retention periods should follow applicable legal, contractual, regulatory, records-retention, and litigation-hold requirements.

## 25. Testing and Readiness

Igzibo should periodically test incident-response readiness appropriate to its size, risk, and operating model.

Testing may include:

- Tabletop exercises.
- Account-compromise exercises.
- Lost-device scenarios.
- Data-disclosure scenarios.
- Ransomware scenarios.
- Third-party service compromise scenarios.
- AI-agent or AI-service scenarios.
- Backup and recovery exercises.

Exercise results should be documented and used to improve the incident-response process.

## 26. Exceptions

Exceptions to this procedure require documented approval from the appropriate Igzibo authority.

An exception request should include:

- Requirement being excepted.
- Business justification.
- Scope.
- Duration.
- Risk created.
- Compensating controls.
- Owner.
- Approval.
- Review or expiration date.

Exceptions must not be used to bypass legal, regulatory, contractual, or client obligations.

## 27. Enforcement

Failure to follow this procedure may result in corrective action appropriate to the circumstances.

Nothing in this procedure prevents Igzibo from taking immediate action necessary to protect people, information, systems, clients, or business operations.

## 28. Technology-Neutral Implementation

This procedure establishes required outcomes and response activities rather than prescribing a specific vendor or technology.

Implementation may use different tools for:

- Identity and access management.
- Endpoint security.
- Logging and monitoring.
- Cloud security.
- Source-code security.
- Email security.
- Data-loss prevention.
- Ticketing and case management.
- Evidence collection.
- Backup and recovery.
- Threat intelligence.
- AI security.

Vendor-specific configuration requirements should be documented separately.

## 29. References and Research Basis

This procedure was developed with reference to the following authoritative guidance:

- NIST, Special Publication 800-61 Revision 3, *Incident Response Recommendations and Considerations for Cybersecurity Risk Management: A CSF 2.0 Community Profile*, April 2025.
  https://csrc.nist.gov/pubs/sp/800/61/r3/final

- NIST, *Incident Response* project resources.
  https://csrc.nist.gov/projects/incident-response

- NIST, *The NIST Cybersecurity Framework (CSF) 2.0*, February 2024.
  https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20

- CISA, *Cybersecurity and Infrastructure Security Agency*.
  https://www.cisa.gov/

- CISA, *Federal Government Cybersecurity Incident and Vulnerability Response Playbooks: Operational Procedures for Planning and Conducting Cybersecurity Incident and Vulnerability Response Activities in Federal Civilian Executive Branch Information Systems*, November 2021.
  https://www.cisa.gov/sites/default/files/publications/Federal_Government_Cybersecurity_Incident_and_Vulnerability_Response_Playbooks_508C.pdf

NIST SP 800-61 Revision 3 is the primary incident-response reference for this procedure. NIST SP 800-61 Revision 2 is not used as a current normative reference because NIST withdrew it when Revision 3 was finalized in April 2025.

## 30. Version History

| Version | Date | Description |
|---|---|---|
| 1.1 | September 16, 2026 | Corrected the CISA Cybersecurity Incident and Vulnerability Response Playbooks reference. The previous CISA webpage URL no longer resolves; the reference now points directly to the CISA-hosted playbook PDF. | 
| 1.0 | September 16, 2026 | Initial release. Establishes the organizational security incident response process and integrates incident response with the Igzibo technology governance framework. |
