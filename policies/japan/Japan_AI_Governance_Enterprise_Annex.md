# AI Governance - Enterprise Annex - Japan

### Operating the APPI duties, the cessation right and the AI Guidelines principles across the AI portfolio

**Organisation:** [ORGANISATION]
**Effective date:** [DATE]  **Version:** 1.0
**Owner:** [Accountable executive for AI]  **Privacy lead:** [Privacy Protection Officer]
**Classification:** Internal
**Companion to:** Artificial Intelligence Acceptable Use Policy - Japan (policy clause references below are to that document)

---

## A1. Governance structure and accountability

A1.1 [ORGANISATION] is responsible under the APPI for the personal information it
handles, including where an entrusted processor handles it. A Privacy Protection Officer
is designated and gives effect to the Act through internal rules; this policy and annex
are those rules for AI. The role maps to the accountability principle in the AI
Guidelines.

A1.2 The **AI Governance Committee** comprises the accountable executive (chair), the
Privacy Protection Officer, the CISO, [Legal], [Risk] and the business owners of Level 3
and Level 4 systems. It approves Level 4 uses, owns the policy and this annex, reviews
the AI register quarterly, receives the monitoring and incident reports at A9, and
reviews approval and override rates.

A1.3 The **Privacy Protection Officer** approves Level 3 uses, owns purpose-of-use and
risk assessments, holds the clause 12 determinations, handles disclosure, correction and
cessation requests, and manages incident reporting to the Personal Information Protection
Commission.

A1.4 Every AI system has a **named accountable person** who owns its register entry,
assessments, testing and monitoring, and knows whether the system is a developer,
provider or business-user role for the purposes of the guidelines.

A1.5 The AI Guidelines' governance expectation - build AI governance that identifies,
assesses, mitigates and monitors AI risk across the lifecycle, and revisits it as the
technology and the rules change - is the frame for this annex.

## A2. AI system inventory: the register

A2.1 The AI register lists every AI system in use or under evaluation, including AI
embedded in procured products and AI features enabled in approved products.

A2.2 Each entry records: system and supplier; purpose of use, notified or announced as
required; business owner and accountable person; level of use; the personal information
handled and whether it is sensitive personal information; whether the supplier is an
**entrusted processor** under supervision or a **third party**; whether personal data is
provided outside Japan and the basis; whether the system identifies, locates or profiles
people from biometric features; the clause 12 determination, including whether the
handling could be likely to harm the person's rights or interests; the risk assessment;
testing and monitoring; retention periods for prompts, outputs and training data; and
the guidelines role (developer, provider, business user).

A2.3 The register is the source of the public handling statement (policy clause 8.1) and
of the quarterly review. Material changes reopen approval.

## A3. Amendment-readiness register

A3.1 The set relies on nothing in the 2026 APPI amendment. This register tracks it and
the subordinate rules applied by reference.

| Item | Source | Status | Owner |
|---|---|---|---|
| 2026 APPI amendment: Diet submission, passage, promulgation, effective date | PPC triennial-review reform policy, Jan 2026 (submission expected spring 2026; effect ~2 years after passage) | Monitored | [Legal] |
| If enacted: statistics/AI-development consent exception; under-16 rules with best-interests provision; facial-feature-data duties and opt-out prohibition; low-risk breach notice relaxation; targeting-information prohibition; administrative monetary penalties | PPC reform policy | Pending | Privacy Protection Officer |
| Cabinet Order and PPC Enforcement Rules: leak-report content and timing, opt-out filing particulars, equivalent-measures standard, disclosure procedure | APPI subordinate legislation (held) | Applied by reference; confirm current versions | Privacy Protection Officer |
| AI Guidelines for Business: successor versions | METI / MIC | Monitored | [Legal] |

## A4. The determination in operation

A4.1 For every system bearing on a decision about a person, the accountable person
records the two-part determination at policy clause 12: significant effect (Level 4
controls), and whether the handling could be likely to harm the person's rights or
interests (cessation right engageable).

A4.2 **Worked entries** (illustrative):

| System and use | Significant effect? | Handling likely to harm rights or interests? | Outcome |
|---|---|---|---|
| Credit model auto-approving below a threshold | Yes | Possibly, if wrong | Level 4; cessation right must be honourable; explanation as house standard |
| Applicant screening ranking CVs for a recruiter | Yes | Possibly | Level 4; same |
| Facial recognition identifying customers in-store | Yes | Yes - sensitive-tier identifiers | Level 3/4; consent required; opt-out provision prohibited |
| Chatbot answering product questions | No | No | Customer-facing disclosure only |

A4.3 The register records, for each system inside Level 4, how the person is told, the
explanation template (personal data used, principal factors), the review route, and how a
cessation request under policy clause 13.1 would be executed against that system's data
store.

## A5. Purpose-of-use and risk assessments

A5.1 Before any Level 3 or Level 4 use, any generation or inference of personal
information, any biometric use, any scraping or acquisition, any fine-tuning, and any
customer-facing AI, [ORGANISATION] confirms and records the specified purpose of use and
whether the AI use is within it, and completes a privacy risk assessment.

A5.2 The assessment addresses: the specified purpose and whether consent or a purpose
change is needed; sensitivity and the consent basis for sensitive personal information;
whether the system generates or infers personal information; security and the
AI-specific threats; entrustment versus third-party provision; cross-border provision;
retention and deletion; the cessation-right exposure; biometric and profiling functions;
minors and vulnerable people; and, for Level 4, unfair-bias testing.

A5.3 Where the assessment cannot establish a lawful basis for a use, it does not proceed
until consent is obtained or the design changes.

## A6. Entrustment, third parties and cross-border transfers

A6.1 For every AI supplier, [ORGANISATION] determines whether it is an **entrusted
processor** (handling personal data only on [ORGANISATION]'s instructions and for its
purposes) or a **third party** (able to use inputs or outputs for its own purposes). The
determination is recorded and drives the legal basis: supervision for the former,
consent or exception for the latter.

A6.2 For an entrusted processor, the contract confines the data to [ORGANISATION]'s
purposes, prohibits the supplier's own use including model training, requires security
and deletion, and permits audit; [ORGANISATION] exercises necessary and adequate
supervision.

A6.3 **Cross-border.** Before personal data is provided to a supplier in a foreign
country, [ORGANISATION] establishes the basis: the country is one the Commission
recognises; or the recipient maintains continuous equivalent measures under a compliant
system, in which case [ORGANISATION] takes the steps the Rules require to ensure their
continued implementation and to answer the person's enquiries; or the person's prior
consent, informed by information about the foreign regime, is obtained. The basis is
recorded in the register.

A6.4 Suppliers are asked for the information the guidelines expect developers and
providers to give: intended purpose and limitations, known failure cases, training-data
provenance where relevant, and security testing.

## A7. Notice and public statements

A7.1 [ORGANISATION]'s public statement of how it handles personal information covers AI
uses, AI suppliers, and provision of personal data outside Japan, and is kept current.

A7.2 Purposes of use are specified and, on acquisition, promptly notified or publicly
announced; where personal information is acquired directly in writing, the purpose is
expressly indicated at the point of acquisition.

A7.3 Customer-facing AI systems carry the disclosure at policy clause 15.1.

## A8. Testing, monitoring and assurance

A8.1 Systems are tested before approval for validity and reliability, inaccurate,
biased and harmful outputs, surfacing of others' personal information, and the
AI-specific threats (prompt injection, extraction, jailbreaking).

A8.2 Level 4 systems are tested for unfair differential outcomes before deployment and
at least [annually].

A8.3 Monitoring after deployment is matched to the level, and includes, for Level 4,
approval and override rates. Retrieval-augmented generation and similar measures are
used where they reduce hallucination.

A8.4 Human override points are documented for every system, and alternative pathways
maintained so critical functions continue if a system fails or is withdrawn.

## A9. Incident response

A9.1 The incident process at policy clause 20.5 is operated by [Security] with the
Privacy Protection Officer. On any suspected leak, loss or damage of personal data
involving an AI tool: containment; assessment against the Commission's Rules of whether
the situation is one likely to harm individual rights and interests; where it is, a
report to the Personal Information Protection Commission and notification of the affected
persons as the Rules require (or alternative protective measures where notice is
difficult); and a record in every case.

A9.2 AI-specific incident types are recognised and drilled: personal information entered
into an unapproved or public tool; a tool surfacing another person's data; a supplier
breach; extraction of training or context data; an agent acting outside its approved
actions; a Level 4 system producing a systematically wrong or discriminatory result;
generation of unlawful content.

A9.3 Every AI incident, whether or not a reportable leak, is recorded, investigated and
analysed, and the lessons applied.

## A10. Individuals' rights

A10.1 Disclosure, correction and cessation requests concerning personal data in or
generated by AI tools follow policy clause 11.3. Records are kept so that a request can
be answered, and so that a cessation request under policy clause 13.1 can be executed
against the relevant data store, prompts and outputs.

A10.2 For Level 4 decisions, the notice, explanation and review process at policy clause
13.2 is operated as recorded in the register (A4.3).

A10.3 Complaints follow the published mechanism; patterns are reported to the AI
Governance Committee.

## A11. Training and awareness

A11.1 Staff training follows policy clause 21. Reviewers of Level 4 decisions are trained
on the system and on the rights at clause 13.

A11.2 The Privacy Protection Officer and [Legal] maintain awareness of the 2026 APPI
amendment's progress, of Personal Information Protection Commission guidance including
its generative-AI cautions, of the Cabinet Order and Enforcement Rules, and of successor
versions of the AI Guidelines.

## A12. Metrics reported to the AI Governance Committee

- Systems on the register by level; new, changed and retired
- Systems inside Level 4; systems whose handling could be likely to harm rights or
  interests
- Purpose-of-use and risk assessments open, completed and overdue
- Level 4 approval and override rates by system
- Incidents by type; reports to the Commission; register entries
- Disclosure, correction and cessation requests, and time to resolve
- Testing and monitoring findings, including bias testing results
- Training completion for users, accountable people and reviewers
- Amendment-readiness register status

## A13. Scope of this annex and what is not held

A13.1 This annex operates the Act on the Protection of Personal Information (English
translation held), the AI Promotion Act (Act No. 53 of 2025), the AI Guidelines for
Business v1.1 and its Appendix, the APPI Cabinet Order and Enforcement Rules (held), and
reads the PPC's 2026 triennial-review reform policy without relying on it.

A13.2 **It does not hold**, and therefore does not state in detail: the enacted 2026
amendment (not law); the current-version numbering of the Cabinet Order and Enforcement
Rules beyond the held copies; the My Number Act; sector rules; the Unfair Competition
Prevention Act and copyright law; and Personal Information Protection Commission
guidance beyond the guidelines. Each is named in policy clause 22 as an open
verification and recorded in the source register.

---

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | 3 September 2026 | Initial annex, published within its stated scope. Every obligation traced to the held instruments in the research note. |

---

*Educational template - not legal advice. Review by qualified counsel before adoption.*
