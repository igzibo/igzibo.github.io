# Google Workspace Security Configuration Standard

**Organization:** Igzibo Engineering Solutions, Inc.  
**Document:** `google-workspace-security-configuration-standard-v1.md`  
**Version:** 1.0  
**Status:** Platform-Specific Standard  
**Effective Date:** September 16, 2026  
**Owner:** Igzibo Engineering Solutions, Inc.  
**Review Cycle:** At least annually and after material security, legal, contractual, or platform changes

## Definitions

- **AUP** — Technology Acceptable Use Policy.
- **AI** — Artificial Intelligence.
- **Admin Account** — An account with administrative privileges within Google Workspace.
- **Google Workspace** — Google's cloud productivity and collaboration service used by Igzibo when approved.
- **IAM** — Identity and Access Management.
- **MFA** — Multi-Factor Authentication.
- **SSO** — Single Sign-On.
- **Organizational Account** — An account issued, controlled, or authorized by Igzibo for business use.
- **Restricted Information** — Information requiring the highest level of protection under the Data Classification and Handling Standard.

## 1. Purpose

This standard defines minimum security configuration expectations for Igzibo's Google Workspace environment.

It is intentionally platform-specific. It implements the requirements of the broader technology governance framework and does not replace technology-neutral policies or standards.

## 2. Scope

This standard applies to Google Workspace services administered or authorized by Igzibo, including organizational accounts, administrative accounts, email, Drive, shared collaboration resources, and related Workspace security controls.

Where Google Workspace is not used, equivalent controls should be addressed through the applicable platform-specific standard.

## 3. Administrative Accounts

Google Workspace administrative access must use individually assigned administrator identities.

Administrative accounts must not be shared.

Administrative access should be limited to personnel who require it and should use MFA.

Where supported, stronger authentication methods should be used for administrative accounts.

## 4. Multi-Factor Authentication

MFA must be enabled for administrative accounts and should be enabled for organizational user accounts.

MFA settings should be configured to reduce the risk of account takeover, including controls that discourage unauthorized authentication approvals.

## 5. Account Lifecycle

Organizational accounts must be created, modified, suspended, and removed according to the Identity and Access Management Standard and Employee and Contractor Offboarding Procedure.

Inactive or unnecessary accounts should be disabled or removed.

Shared accounts should be avoided unless there is a documented business requirement and appropriate compensating controls.

## 6. External Sharing

External sharing must be controlled according to business need and information classification.

Users must not share Restricted Information externally unless authorized and permitted by applicable client, contractual, legal, and governance requirements.

Administrative settings should be configured to reduce unnecessary external sharing.

## 7. Google Drive and Shared Resources

Business information must be stored in approved organizational locations.

Access to shared drives, folders, and documents must follow least-privilege principles.

Ownership and access should be reviewed when personnel, projects, or business requirements change.

## 8. Email Security

Email security controls should be configured to reduce phishing, malware, unauthorized forwarding, and account-compromise risks.

Users must follow the Technology Acceptable Use Policy and Security Incident Response Procedure when suspicious messages or account activity are identified.

## 9. Account Recovery

Recovery options must be controlled and associated with authorized identities.

Administrative recovery mechanisms must be protected from unauthorized access.

## 10. Logging and Monitoring

Where supported by the applicable Google Workspace edition, security and administrative activity should be logged and reviewed according to risk.

Material security events should be handled under the Security Incident Response Procedure.

## 11. Data and AI Controls

Google Workspace information remains subject to the Data Classification and Handling Standard and AI and Generative AI Usage Standard.

Using a Google Workspace service does not by itself authorize disclosure of confidential, restricted, client, or personal information.

## 12. Third-Party Applications

Third-party applications requesting access to Google Workspace data must be evaluated and approved under the Technology and Third-Party Service Security Standard and the Technology and Third-Party Service Approval Procedure.

Users must not authorize unapproved applications to access organizational information.

## 13. Administrator Security

Administrators should:

- Use dedicated administrative identities.
- Use MFA.
- Minimize administrative privileges.
- Review administrative accounts periodically.
- Avoid routine productivity work from privileged accounts where practical.
- Protect recovery and security settings.
- Review significant security alerts and configuration changes.

## 14. Configuration Changes

Material security configuration changes should be documented and reviewed according to applicable change-management and project requirements.

Security settings must not be weakened merely to resolve user convenience issues without appropriate review.

## 15. Exceptions

Exceptions require documented approval and must identify the business justification, affected control, security risk, compensating controls, responsible owner, and review or expiration date.

## 16. Relationship to Other Governance Documents

This standard implements and complements:

1. Technology Acceptable Use Policy.
2. Identity and Access Management Standard.
3. Password and Authentication Standard.
4. Data Classification and Handling Standard.
5. AI and Generative AI Usage Standard.
6. Technology and Third-Party Service Security Standard.
7. Security Incident Response Procedure.
8. Employee and Contractor Offboarding Procedure.

If Google Workspace provider requirements conflict with an Igzibo requirement, the applicable issue must be reviewed rather than silently weakening the Igzibo control.

## Version History

| Version | Date | Summary |
|---|---|---|
| 1.0 | 2026-09-16 | Initial Google Workspace security configuration standard. |
