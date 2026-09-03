# AI Governance - Enterprise Annex - Kingdom of Bahrain

**Organisation:** [ORGANISATION]
**Effective date:** [DATE]  **Version:** 1.0
**Annex owner:** [CISO / Head of AI Governance]  **Data protection lead:** [DATA PROTECTION GUARDIAN / privacy lead]
**Classification:** Internal
**Review:** at least every six months, and on material change in tools or regulation

This annex extends the [ORGANISATION] Artificial Intelligence Acceptable Use Policy
(Kingdom of Bahrain) for large organisations. The policy governs how individuals use
AI; this annex governs how the organisation manages AI as a portfolio - oversight,
regulatory filings, inventory, lifecycle, suppliers, and assurance. Where this annex
and the policy overlap, the stricter requirement applies.

---

## A1. Governance structure and accountability

A1.1 [ORGANISATION] maintains an AI Governance Committee with a defined remit:
approving this annex and the Acceptable Use Policy, approving Level 3 uses, approving
Level 4 uses only once written authorisation from the Authority is held, approving
exceptions, reviewing incidents and metrics, and monitoring regulatory change.
Membership includes [security, data protection, legal, risk, HR, and business
representation]. The committee meets at least quarterly.

A1.2 A named senior executive is accountable for AI governance across the
organisation and reports on it to the board at least [twice yearly]. That reporting
must include the standing of every regulatory filing under A2A, because failures in
this area can attach criminal liability to the organisation and to individual
officers.

A1.3 Responsibility follows three lines: business functions own the risks of the AI
they use; risk and compliance functions set standards and challenge; internal audit
provides independent assurance (clause A8).

A1.4 Where a Data Protection Guardian is appointed - whether internal or external -
the Guardian's statutory duties are discharged independently and impartially, and are
not subordinate to the committee. The Guardian must be enrolled in the Authority's
register to be recognised, and the appointment must be notified to the Authority
within the short statutory period. The committee must not place the Guardian in a
position that conflicts with the duty to escalate unremedied violations to the
Authority.

## A2. AI system inventory

A2.1 Every AI system used or deployed by [ORGANISATION] - bought, built, or embedded
in other software - must be recorded in the AI system inventory before use. The
record states: business owner; purpose; risk level (policy clause 5); data
categories processed; lawful ground and, where relied on, the form and date of
consent; supplier and underlying model where known; the point of human oversight;
processing locations and the transfer basis; and the next review date.

A2.2 An AI system not in the inventory is treated as an unapproved tool under policy
clause 3. The inventory is reviewed [quarterly] and material changes to a recorded
system reopen its approval **and** trigger the change-notification assessment in
A2A.4.

## A2A. Regulatory filings register

**This clause exists because Bahraini law gates deployment on prior notice and, for
some processing, on prior written permission. Governing AI as a portfolio here means
governing the filings, not only the systems.**

A2A.1 [ORGANISATION] maintains a Regulatory Filings Register alongside the AI system
inventory. For every AI system that processes personal data it records: whether prior
notice to the Authority is required or an exemption applies and which; the date notice
was given; whether the processing falls in policy clause 4.2; the date any
authorisation request was submitted; the decision and its date, or the date on which
the statutory period expired without reply; and any conditions or time limits
attached to an authorisation.

A2A.2 **No Level 4 system may enter production on an unanswered request.** Silence
past the statutory period is a refusal. A system in that position is recorded as
refused and returns to the committee.

A2A.3 Authorisations that are conditional or time-limited carry a diary date. The
owner is responsible for renewal before expiry; an expired authorisation stops the
processing.

A2A.4 Material changes to notified or authorised information - purpose, data
categories, recipients, transfer destinations, security measures - must be reported
to the Authority within the statutory period. **Changing model, vendor, or hosting
region is capable of being such a change**, and the assessment must be recorded even
where the conclusion is that no filing is needed.

A2A.5 The committee reviews the register at every meeting. Any system operating
without its filing position resolved is escalated to the accountable executive at
A1.2 immediately, not at the next meeting.

## A3. Lifecycle controls for systems the organisation builds or adapts

A3.1 Before deployment: documented purpose and success criteria; testing for
accuracy, robustness, security, and bias (policy clause 16) proportionate to the
risk level; the data protection impact assessment where policy clause 7.6 requires
one, with the Data Protection Guardian's advice sought where designated; the
regulatory filing position resolved under A2A; and sign-off by the business owner
and, where personal data is involved, the data protection lead.

A3.2 In change: modifications with a material effect on behaviour - model, prompt,
configuration, or training data changes - go through change management and re-testing
proportionate to the change, and the A2A.4 assessment.

A3.3 In operation: deployed systems are monitored for degraded performance, drift,
and misuse; agreed thresholds trigger review by the business owner.

A3.4 At retirement: a decommissioning step covering data disposal, dependent
processes, closure of the inventory record, and notification to the Authority where
the cessation changes information previously filed.

A3.5 Training data provenance is documented for any system [ORGANISATION] builds or
fine-tunes: what personal data was used, on what ground, whether consent covered that
use, and whether the training itself required notice or authorisation.

## A4. Suppliers and supply chain

A4.1 No AI service is procured or renewed without the security and data protection
review in policy clause 3, and a **written** contract covering: processing only on
[ORGANISATION]'s instructions; security and confidentiality obligations equivalent to
those on [ORGANISATION]; no use of [ORGANISATION] data to train the supplier's models
without express approval; breach notification to [ORGANISATION] fast enough to meet a
clock that starts on discovery; transparency over sub-processors and material model
changes; and audit and exit rights.

A4.2 Where the supplier processes personal data outside the Kingdom, the contract
must additionally carry the transfer terms required by policy clause 8.4, and the
transfer basis must be recorded in A2A.1 before go-live.

A4.3 [ORGANISATION] takes reasonable steps to satisfy itself that the supplier
actually implements the technical and organisational measures required, rather than
relying on the contract alone.

A4.4 Critical AI suppliers are reassessed at least annually. For any AI service the
business critically depends on, an exit plan exists and concentration risk is
reviewed by the committee.

## A5. Exceptions

A5.1 Departures from the policy or this annex require a written exception approved by
the annex owner, with the risk accepted in writing by a named senior owner.
Exceptions are time-bound (maximum [6 months]), carry compensating controls, and are
recorded in an exceptions register with their expiry dates. The committee reviews the
register at every meeting; expired exceptions lapse automatically.

A5.2 **No exception may be granted against a statutory requirement.** In particular,
the committee cannot authorise processing that requires prior notice or prior written
authorisation to proceed without it. Those are not risks the organisation is able to
accept.

## A6. Agentic AI

A6.1 AI agents - systems that plan and take actions with limited human prompting -
operate under their own credentials with least-privilege access. A person's own
credentials must never be given to an agent.

A6.2 Consequential actions - making payments, sending external communications,
changing records about people, deploying code, or deleting data - require a human
checkpoint before execution unless the committee has expressly approved autonomous
operation for that action and system.

A6.3 An agent must not initiate processing that would require prior notice or
authorisation, and must not transfer personal data outside the Kingdom, unless that
specific behaviour has been filed and approved under A2A. An agent that can select
its own tools or data sources is assessed for whether it can reach such processing at
all.

A6.4 Agent activity is logged and attributable to a named human owner. Agent sessions
are bounded in scope and duration, and every agent has a documented means of
immediate suspension.

A6.5 Content an agent ingests from outside the organisation is treated as untrusted
input (policy clause 12.3), including instructions embedded in that content.

## A7. Individual rights operations

A7.1 [ORGANISATION] maintains a documented route by which a request from an
individual - to be told what data is held, to have it rectified, blocked, or erased,
or to object - is executed against every AI system in the inventory, including
prompts, uploads, embeddings, caches, and logs.

A7.2 The statutory response periods for these requests are short and are measured in
working days. Systems that cannot meet them are not approved for personal data.

A7.3 Where an individual exercises the right to have a solely automated decision
reconsidered, the reconsideration is carried out by a person, free of charge, and the
outcome is recorded together with the objection and the date.

A7.4 Where personal data is rectified, blocked, or erased on request, third parties
to whom the data was disclosed are notified within the statutory period unless that
proves impossible or unachievable. Suppliers of AI services are such third parties.

## A8. Assurance and metrics

A8.1 The committee tracks agreed indicators, including: approved-tool adoption;
unapproved-tool discoveries; **systems in production with an unresolved filing
position, which should be zero**; authorisations approaching expiry; verification
records for decision-bearing output; incidents and near misses; time from breach
discovery to notification; exception count and age; and impact-assessment coverage
for Level 3 and Level 4 uses.

A8.2 Internal audit reviews the AI governance programme at least [annually],
including a sample test that filings in A2A match what systems actually do.

A8.3 The committee conducts a management review of the whole programme at least
[annually]: policy and annex, inventory, filings register, metrics, incidents,
supplier performance, and regulatory change, with documented actions.

## A9. Complaints and speak-up

A9.1 Individuals can complain to [ORGANISATION] about the handling of their personal
data, including by AI systems. [ORGANISATION] provides an accessible means of
complaint, records it, takes appropriate steps to respond, and informs the
complainant of the outcome. Individuals may also complain directly to the Authority,
and doing so is not conditional on complaining to [ORGANISATION] first. [DATA
PROTECTION GUARDIAN / privacy lead] owns this process.

A9.2 Staff can raise concerns about AI use - bias, safety, misuse, or pressure to
bypass controls - outside their line management and without detriment, through
[speak-up channel]. Concerns that processing is running without a required
notification or authorisation are treated as urgent and routed to the data protection
lead and the annex owner the same day.

## A10. Sector overlay [regulated firms]

A10.1 Where [ORGANISATION] is regulated, the committee maps this annex to the
sector's requirements and records the mapping in the inventory and risk register.
Financial services firms should note that a separate duty to notify the Central Bank
of Bahrain can arise alongside the data protection duties in this annex; that mapping
must be verified with the firm's own regulatory advisers and is **not** asserted here.

---

*This document is an educational policy template and does not constitute legal
advice. It reflects obligations under the Bahraini personal data protection regime as
held in the source corpus and must be verified against primary sources - including
the authoritative Arabic texts published in the Official Gazette - and reviewed by
the data protection lead or Bahraini-qualified legal counsel before adoption.*
