# AI and Generative AI Usage Standard

**Organization:** Igzibo Engineering Solutions, Inc.  
**Document:** `ai-generative-ai-usage-standard-v2.md`  
**Version:** 2.0  
**Status:** Living standard  
**Effective Date:** September 16, 2026  
**Owner:** Igzibo Engineering Solutions, Inc.  
**Review Cycle:** At least annually and after material changes in AI technology, law, client requirements, or security risk

## 1. Purpose

This standard establishes requirements for responsible use of Artificial Intelligence (AI), including Generative Artificial Intelligence (Generative AI), for Igzibo business.

It is technology-neutral and applies regardless of provider, model, application, deployment method, hosting location, or device.

## Definitions

- **AI** — Artificial Intelligence, technology capable of performing tasks commonly associated with human intelligence.
- **CISA** — Cybersecurity and Infrastructure Security Agency, a U.S. government agency that provides cybersecurity guidance and resources.
- **Igzibo** — Igzibo Engineering Solutions, Inc.
- **MFA** — Multi-Factor Authentication, authentication requiring two or more independent authentication factors.
- **NIST** — National Institute of Standards and Technology, a U.S. government agency that publishes cybersecurity and technology guidance.
- **Organizational Resource** — Any technology, account, system, service, device, information asset, or other resource owned, licensed, administered, funded, or authorized by Igzibo.

- **Generative AI** — AI capable of generating content such as text, code, images, audio, or video from input.
- **AI RMF** — Artificial Intelligence Risk Management Framework, NIST's voluntary framework for managing AI risks and trustworthiness.
- **LLM** — Large Language Model, a machine-learning model designed primarily to process and generate language.
- **Prompt** — Information or instructions supplied to an AI system.
- **Output** — Content generated or returned by an AI system.
- **AI Provider** — An organization that develops, hosts, operates, or provides access to an AI service or model.
- **AI Agent** — An AI-enabled system capable of taking actions, using tools, or interacting with other systems beyond generating a response.
- **RAG** — Retrieval-Augmented Generation, a technique in which an AI system retrieves external information to help produce an output.
- **IP** — Intellectual Property, legally protectable creations or rights such as copyrights, patents, trademarks, trade secrets, and related rights.
- **Human Review** — Review by a qualified person before AI-generated material is relied upon for a consequential business purpose.

## 2. Scope

This standard applies to public and enterprise AI services, locally hosted models, coding assistants, chatbots, generative text/image/audio/video/code systems, AI-enabled business applications, AI agents, AI APIs, and AI embedded in other products.

It applies when AI is used for Igzibo business on any device or platform.

## 3. Relationship to Other Documents

AI use must comply with:

1. Applicable law and binding requirements.
2. Client and contractual requirements.
3. The Technology Acceptable Use Policy.
4. The Data Classification and Handling Standard.
5. The Technology and Third-Party Service Security Standard.
6. This standard.

The Data Classification and Handling Standard determines information sensitivity. This standard establishes AI-specific requirements for using that information.

## 4. General Rule

AI may be used for legitimate business purposes when the use is authorized, consistent with applicable requirements, and proportionate to risk.

Public availability or low cost does not make an AI service approved for Confidential or Restricted information.

## 5. Generally Permitted Uses

Subject to classification requirements, users may use AI for:

- Brainstorming.
- Drafting non-sensitive content.
- Summarizing approved information.
- Formatting.
- Synthetic test-data generation.
- Code explanation.
- Code scaffolding.
- Documentation assistance.
- Public-information research.
- Translation of non-sensitive material.
- Internal prototypes.

## 6. Uses Requiring Approval

Approval is required before AI is used to:

- Process Confidential or Restricted information.
- Process client information.
- Make decisions concerning personnel, candidates, customers, or other individuals.
- Take autonomous actions against production systems.
- Access sensitive organizational systems.
- Send consequential external communications without appropriate human review.
- Make financial, legal, security, or contractual determinations.
- Create an AI Agent with access to Organizational Resources.
- Train or fine-tune a model using organizational or client information.

## 7. Prohibited Inputs

Unless specifically approved for the particular service and use case, users must not enter:

- Passwords.
- API keys.
- Access tokens.
- Private keys.
- Authentication codes.
- Confidential client information.
- Restricted information.
- Sensitive PII.
- Non-public source code.
- Trade secrets.
- Security-incident evidence.
- Information subject to contractual restrictions.
- Information subject to a legal hold or investigation.

## 8. Data Minimization

Users must provide only the minimum information necessary.

Where possible, users should remove names, identifiers, credentials, unnecessary client details, and other information not needed to perform the task.

Synthetic data should be used instead of real sensitive data where practical.

## 9. AI Provider Evaluation

Before approving an AI service for business information, Igzibo should evaluate:

- Data retention.
- Training and model-improvement practices.
- Human access to submitted information.
- Encryption.
- Account security.
- MFA.
- Administrative controls.
- Data deletion.
- Data export.
- Geographic processing.
- Subprocessors.
- Contractual terms.
- Privacy terms.
- Security documentation.
- Incident notification.

AI services are subject to the Technology and Third-Party Service Security Standard.

## 10. Human Oversight

AI output is not automatically authoritative or correct.

Human review is required when errors could materially affect security, legal compliance, client obligations, financial consequences, privacy, reputation, or production systems.

Particular care is required for production code, security configurations, legal documents, contracts, client deliverables, financial analysis, personnel decisions, privacy decisions, technical architecture, and public statements.

## 11. Confidentiality and Client Work

Users must comply with client restrictions on AI use.

A client prohibition on AI processing controls even when Igzibo's internal requirements would otherwise permit the use.

Users must not disclose that confidential client information has been submitted to an AI service unless authorized.

## 12. Intellectual Property

AI-assisted output must be reviewed for copyright, licensing, trade-secret, third-party-rights, client-ownership, and open-source licensing concerns before commercial use or publication.

AI output must not be represented in a misleading manner or contrary to an applicable agreement.

## 13. Software Development

AI-generated code is subject to the same security, testing, quality, dependency, and licensing requirements as human-written code.

Users must review and test generated code, check dependencies and licenses where applicable, remove secrets, and follow client restrictions.

## 14. AI Agents and Tool Access

AI Agents require heightened review because they can take actions.

Before deployment, Igzibo should define:

- Authorized actions.
- Accessible systems.
- Accessible data.
- Maximum privileges.
- Approval requirements.
- Logging.
- Failure behavior.
- Emergency shutdown.
- Credential management.
- Human oversight.

AI Agents must use least privilege.

High-impact actions should require explicit human approval where practical.

## 15. Retrieval-Augmented Generation

RAG systems must enforce source and access controls.

A RAG system must not retrieve information that the requesting user is not authorized to access.

Indexing information does not override the original access restrictions.

## 16. AI Security

Users and system owners must consider risks including prompt injection, data leakage, malicious retrieved instructions, unauthorized tool use, excessive permissions, insecure generated code, fabricated information, supply-chain risk, and compromised providers or integrations.

AI systems connected to business tools must be treated as potentially untrusted application components and given only necessary permissions.

## 17. Accuracy and Verification

Users must independently verify material facts when errors could cause meaningful harm.

AI must not be treated as an authoritative source merely because it produces a confident response.

## 18. Records and Auditability

For material AI-assisted decisions or systems, Igzibo should retain enough information to understand the system used, business purpose, relevant inputs where appropriate, output used, human review, significant modifications, and approval decisions.

Recordkeeping should be proportional to risk.

## 19. Incident Reporting

Users must promptly report accidental submission of protected information, credential exposure, unexpected AI actions, unauthorized data retrieval, prompt-injection incidents, suspected provider compromise, or materially incorrect AI output that affected a client or business process.

## 20. Training and Governance

Personnel using AI for business purposes should receive appropriate guidance on data classification, prompt security, confidentiality, verification, AI limitations, secure coding, client requirements, and incident reporting.

Igzibo should maintain an inventory of material AI systems and review higher-risk systems more frequently.

## 21. References

- NIST AI Risk Management Framework 1.0: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-ai-rmf-10
- NIST AI Risk Management Framework: Generative Artificial Intelligence Profile: https://www.nist.gov/publications/artificial-intelligence-risk-management-framework-generative-artificial-intelligence
- NIST Cybersecurity Framework 2.0: https://www.nist.gov/publications/nist-cybersecurity-framework-csf-20

## 22. Version History

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-09-16 | Initial AI and Generative AI usage standard. |
| 2.0 | 2026-09-16 | Coordinated governance revision; clarified document precedence, approval requirements, data-classification relationship, AI-agent controls, and provider-review responsibilities. |
