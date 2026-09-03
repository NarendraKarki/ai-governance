# AI Governance - Enterprise Annex - Sultanate of Oman

**Organisation:** [ORGANISATION]
**Effective date:** [DATE]  **Version:** 1.0
**Annex owner:** [CISO / Head of AI Governance]
**Personal Data Protection Officer:** [PDPO]
**Classification:** Internal
**Review:** at least every six months, and on material change in tools or regulation

This annex extends the [ORGANISATION] Artificial Intelligence Acceptable Use Policy
(Oman) for large organisations. The policy governs how individuals use AI; this annex
governs how the organisation manages AI as a portfolio - oversight, inventory, permits,
lifecycle, transfers, suppliers, audit readiness and assurance. Where this annex and the
policy overlap, the stricter requirement applies.

---

## A1. Governance structure and accountability

A1.1 [ORGANISATION] maintains an AI Governance Committee whose remit includes: approving
this annex and the Acceptable Use Policy; approving Level 3 and Level 4 uses; approving
exceptions; reviewing incidents and metrics; owning the permit position at A4, the
transfer position at A6 and the audit readiness position at A8; and monitoring regulatory
change from **both** the ministry and [ORGANISATION]'s sector regulator. Membership
includes the Personal Data Protection Officer, security, legal, risk and business
representation. It meets at least quarterly.

A1.2 A named senior executive is accountable for AI governance across [ORGANISATION] and
reports to the board at least [twice yearly], including the permit and transfer
positions.

A1.3 **The Personal Data Protection Officer is a statutory designation, not a committee
seat.** Their tasks - advising on obligations, following up policy implementation and
performance of obligations, and coordinating with the Competent Department - are
owed whether or not the committee agrees with them. The committee does not place the
officer in a position that compromises the coordination duty.

A1.4 **[ORGANISATION] publishes the officer's name and contact details** and keeps them
current. The annex owner verifies the publication and the notice reference at every
review, because both decay quietly.

A1.5 Responsibility follows three lines: business functions own the risks of the AI they
use; the Personal Data Protection Officer and risk set standards and challenge; internal
audit provides independent assurance (A9).

## A2. AI system inventory

A2.1 Every AI tool used or deployed by [ORGANISATION] is recorded before use. The record
states: business owner; purpose; **the controller/processor role and the using/developing
role**; risk level; the categories of personal data processed and **whether any falls in
a permit category**; the **permit reference and expiry** where one applies; the recorded
consent basis and the notice reference; supplier, sub-processors and underlying model;
**actual processing and storage locations for inference, human review, logging, support
and backup**; the transfer assessment reference; the retention position; **whether the
system can identify whose personal data a given exposure touched**; **whether the data
sources it uses can be traced**; and the next review date.

A2.2 A tool not in the inventory is treated as unapproved under policy Section 3.

A2.3 The inventory is reviewed [quarterly]. **The following reopen the record
immediately** rather than at the next review: a change of supplier or sub-processor; a
change of model; a change of processing or storage location; a change of purpose; a new
category of personal data; and [ORGANISATION] beginning to fine-tune or adapt the system.

A2.4 **The inventory is the source of the register entry**, not a parallel document. A3
governs the relationship.

## A3. The processing activities register

A3.1 [ORGANISATION] maintains the statutory register of personal data processing
activities with the ten minimum fields at policy 14.1, and **every AI system processing
personal data has an entry**.

A3.2 The register is **updated continuously** and is provided to the Competent
Department whenever requested. The committee treats "we would need a week to compile
it" as a finding, since the obligation is to provide it on request.

A3.3 Two register fields are the ones AI systems populate badly, and the committee tests
them specifically:

- **the entities to which personal data is disclosed, and the purposes of disclosure** -
  an AI supplier is such an entity, and so is its sub-processor;
- **data relating to the movement and processing of personal data across borders** - this
  must reconcile to the locations recorded at A2.1, and a mismatch is escalated.

A3.4 The register also carries **breach records**, including the surrounding
circumstances, effects, and remedial or corrective action - so the incident process
writes into the register rather than into a separate log (A7.6).

A3.5 Retention of processing documents is governed by a specific and lawful reason, a
period proportionate to the purpose, and technical protection for secure retention. **The
committee records the reason and the period per system**, not per organisation.

## A4. Permits

**This section exists because a permit is a precondition to processing, takes up to 45
days, and is silently refused if the ministry does not reply.**

A4.1 [ORGANISATION] maintains a Permit Register recording, for each permit: the reference
and issue date; **the expiry date**; the categories covered; the purpose; the processor
named; the recipients of disclosure named; **the places of transfer or storage named**;
the protection systems named; and the systems in the AI inventory that rely on it.

A4.2 **A permit application is a project with a lead time.** The committee plans against
45 days for a decision, plus the possibility of a reasoned refusal, plus 60 days to
grieve and 30 days for the grievance to be answered or deemed refused. **The worst case is
materially longer than a quarter**, and no deployment date is set on the assumption of a
grant.

A4.3 **Renewal begins no later than six months before expiry.** A lapsed permit stops the
processing, and the renewal follows the same procedure and the same timetable as a fresh
application.

A4.4 **The permit describes the tooling, so tooling changes amend the permit.** Any change
to the named processor, the named recipients of disclosure, the named places of transfer
or storage, or the protection systems must be notified to the Competent Department
**within 15 days of making it**. A2.3 events are therefore screened against the Permit
Register as well as the inventory, and the committee tracks the interval.

A4.5 **Failure to notify amendments within the period is a ground for cancelling the
permit.** So is a contravention of the law or regulations, and so is obtaining the permit
by incorrect data. The committee treats an unreported change as a permit risk, not an
administrative slip.

A4.6 Where the permit position is uncertain - whether a data category falls inside 11.1,
whether an existing permit covers a new tool - the Personal Data Protection Officer
determines it in writing **before** processing, and the determination is recorded.

## A5. Lifecycle controls

A5.1 **Before deployment**: the role determinations; the objective evaluation against
alternatives required by policy 6.2, recorded; the notice and consent position; the
permit where required; the transfer assessment where data leaves Oman; the ethical,
social and environmental impact assessment where [ORGANISATION] develops or adapts the
system; bias and fairness testing; and sign-off by the business owner and the Personal
Data Protection Officer.

A5.2 **The evaluation against alternatives is a distinct artefact.** The national policy
requires the system to show practical feasibility and benefit *compared with available
alternatives*, evaluated objectively before adoption. A business case that never names a
lower-risk alternative does not satisfy it, and the committee returns it.

A5.3 **In change**: modifications with a material effect on behaviour go through change
management and re-testing, and reopen the notice at policy 10.4, the register entry, the
permit fields at A4.4, and the transfer assessment where locations move.

A5.4 **In operation**: continuous performance monitoring, with errors, deviations and
negative effects **documented immediately on detection** and corrective measures taken.
The committee reviews the interval between detection and documentation as a metric
(A10.1), because "immediately" is the standard.

A5.5 **Regular review and updating** of systems to keep pace with technical developments
and international standards, and **periodic evaluations verifying accuracy, including
independent technical reviews**. The review interval is recorded per system.

A5.6 **At retirement**: disposal across every store in the inventory record; closure of
the register entry with the retention position honoured; notification of permit
amendment where the permit named the system; and retention of the compliance records
under policy 20.3.

A5.7 **A model fine-tuned on personal data may retain it.** Before any such model is
deployed, [ORGANISATION] records how erasure, correction and withdrawal of consent would
be given effect against it, and where that is not possible, does not fine-tune on that
data.

## A6. Cross-border transfer governance

**This is the largest single financial exposure in the framework. It is governed as
such.**

A6.1 The committee maintains a **Transfer Register** recording, for every AI system that
moves personal data outside Oman: the consent basis or the exemption relied on; the
assessment reference and date; the external processing entity; the states through which
data passes and the **final destination**; the protection level determination; and the
review date.

A6.2 **Both exemptions from consent are narrow and are recorded with reasons.** Reliance
on the identity-concealment exemption requires [ORGANISATION]'s own written assessment
that identification is impossible by any means - **not a supplier's description of its
data as anonymised**. The committee reviews every such reliance.

A6.3 **The assessment is written to be produced.** The ministry may request a copy. The
committee therefore holds each assessment in final form rather than as a working
document, and reviews it when any of its five inputs changes.

A6.4 **Location is a gating question at procurement, not a diligence item.** A supplier
that will not state its processing and storage locations, or reserves the right to change
them without notice, is not approved for personal data. Where a supplier may change
regions, the contract must give notice sufficient to reassess **before** the change takes
effect (A7.2).

A6.5 The committee maintains a standing view of **which AI services would stop working if
the ministry suspended transfers**, since suspension of transfer abroad is an express
enforcement measure. That view informs concentration risk and the exit plans at A7.5.

A6.6 Where a permit is in force, the places of transfer and storage are permit fields.
A6.1 and A4.1 are reconciled at every committee meeting.

## A7. Suppliers

A7.1 No AI service is procured or renewed without the review at policy 3.2 and a written
contract. **Engaging a processor does not move [ORGANISATION]'s obligations**, and the
committee does not accept a supplier commitment as a substitute for a control
[ORGANISATION] can evidence.

A7.2 Contracts cover: processing only on [ORGANISATION]'s documented instructions and
only for the stated purpose; **disclosure of actual processing and storage locations and
advance notice of any change**; no use of [ORGANISATION] data to train the supplier's
models; disclosure of material model changes; **immediate breach notification with enough
detail to populate both 72-hour notifications**; the ability to identify whose personal
data an exposure touched; assistance with individuals' requests inside the 45-day period;
sub-processor authorisation and flow-down; secure deletion or return at end of service;
**audit and access rights sufficient for the external auditor at A8**; and exit
arrangements.

A7.3 **Sub-processors are recipients of disclosure** for register purposes and may be
permit fields. They are identified before approval, not discovered later.

A7.4 Where [ORGANISATION] is itself a processor for a client, the annex owner maintains
the list of such engagements, the instructions received, and the notification duties
accepted.

A7.5 Critical AI suppliers are reassessed at least annually, with an exit plan and a
concentration risk review by the committee, informed by A6.5.

## A8. External audit readiness

**The ministry can require an external audit, and the report is due to the Competent
Department within 60 days of the auditor's appointment. That is short.**

A8.1 The committee maintains a standing **audit pack**, derived from the inventory and
the registers, comprising: the processing activities register; the Permit Register; the
Transfer Register with assessments; the notice and consent evidence; the breach
documentation; the controls and procedures [ORGANISATION] has established for processing;
and the AI-specific documentation at A8.4.

A8.2 The auditor must be **accredited and licensed by the ministry** and **independent of
[ORGANISATION]**. The committee identifies candidate auditors in advance rather than
beginning the search when the requirement arrives.

A8.3 [ORGANISATION] must **enable the auditor to view and examine the records, processing
systems and data necessary** for the audit. Access provisioning for an independent
external party is designed in advance and tested, because a 60-day clock cannot absorb an
access dispute.

A8.4 The audit pack additionally holds, for AI systems: the objective evaluation against
alternatives (A5.2); the documentation of the development process where [ORGANISATION]
develops; the ethical, social and environmental impact assessments; the algorithm
documentation explaining decision logic and the data analysis process; bias monitoring
and fairness test results; and the analytical tools and reports enabling the logic of
operation to be evaluated.

A8.5 **The national policy requires production of documents to the regulatory authorities
on official investigation, both for use and for development.** A8.1 and A8.4 serve that
duty as well as the statutory audit.

## A9. Assurance

A9.1 Internal audit reviews the AI governance programme at least [annually], including: a
sample test that inventory records match what systems actually do; a reconciliation of
the inventory, the register, the Permit Register and the Transfer Register; verification
that published Personal Data Protection Officer details are current; and a walkthrough of
the incident process against a simulated breach that crosses **one** notification
threshold but not the other.

A9.2 **That last test is deliberate.** The two 72-hour duties have different triggers, and
the failure mode is an organisation that runs one clock and assumes it discharged both.

A9.3 The committee conducts a management review of the whole programme at least
[annually]: policy and annex, inventory, registers, permits, transfers, metrics,
incidents, supplier performance, and regulatory change from both the ministry and the
sector regulator, with documented actions.

## A10. Metrics

A10.1 The committee tracks agreed indicators, including:

- approved-tool adoption, and unapproved-tool discoveries;
- **AI systems processing personal data with no register entry, which should be zero**;
- **AI systems processing permit-category data without a permit, which should be zero**;
- **permits within six months of expiry with no renewal started**;
- **permit-relevant changes not notified within 15 days, which should be zero**;
- **AI systems moving personal data abroad with no current transfer assessment, which
  should be zero**;
- systems whose recorded locations do not reconcile to the register;
- **interval from detection to documentation** of errors, deviations and negative effects
  (A5.4);
- time from occurrence to awareness; time from awareness to regulator notification; time
  from awareness to data subject notification, **reported separately**;
- incidents where only one notification limb was assessed;
- data subject requests answered within 45 days, and any that were not;
- systems that cannot enumerate affected individuals, or cannot trace data provenance;
- Level 4 systems with no recorded evaluation against alternatives;
- bias findings raised and **remediations actually made**, reported as a pair;
- exception count and age;
- training completion, reported separately for the transfer module.

A10.2 The two notification timings at A10.1 are reported separately and never as an
average. **An average conceals precisely the failure A9.2 tests for.**

## A11. Individuals' requests

A11.1 [ORGANISATION] maintains a documented route by which a request is executed against
every AI system in the inventory - prompts, uploads, transcripts, embeddings, caches,
indexes and logs.

A11.2 A request to exercise the statutory rights is made in writing and answered **within
45 days of receipt, free of charge**. The individual may request **suspension of
processing pending the decision**, and the committee ensures systems can suspend as well
as delete.

A11.3 A request may be refused **partially or wholly only where it is repeated without
justification or its execution requires unusual effort**, and the refusal must be
**reasoned and notified within the same 45 days**. The Personal Data Protection Officer
approves every refusal and records the ground.

A11.4 **Erasure** is available where the purpose has ended, where consent has been
withdrawn, or where the processing does not comply with the law or the regulations.
[ORGANISATION] may refuse where a legal obligation under a law, judgment or judicial
decision requires retention, or where **a live dispute exists between [ORGANISATION] and
the data subject**. Both grounds are recorded with reasons.

A11.5 A **copy** of processed personal data is provided in a readable and clear format,
electronic or paper, **verified to be free of personal data identifying another person**.
For AI systems this verification is a real task - transcripts and prompt logs routinely
contain third parties - and the committee requires it to be evidenced, not assumed.

A11.6 **Portability** is to a new controller, and [ORGANISATION] transfers where legally
obliged to do so.

A11.7 A system that cannot support access, correction, erasure, restriction and
portability against its own stores is not approved for personal data. A5.7 governs the
fine-tuning case.

## A12. Complaints

A12.1 A data subject or other interested person may complain to the Competent
Department about any contravention, **within 30 days of certain knowledge of it**, and
the Competent Department notifies [ORGANISATION] with a copy **within 7 days** of
submission.

A12.2 [ORGANISATION] has **14 days from being notified** to reply. **This is the shortest
externally imposed deadline in the framework**, and the committee maintains a standing
process and an owner so that a complaint arriving during a holiday period does not
consume it.

A12.3 The Competent Department decides within **60 days** from the day after
[ORGANISATION]'s reply period expires, and **silence is a rejection of the complaint**.

A12.4 The committee reviews every complaint, its reply, and its outcome, and treats a
complaint about an AI system as a signal about the system rather than only about the
incident.

A12.5 Staff can raise concerns about AI use - inaccuracy, unfair outcome, misuse, or
pressure to bypass controls - outside their line management and without detriment,
through [speak-up channel]. A concern that personal data may have been exposed is routed
to the incident process the same hour, because both notification clocks run from
awareness.

## A13. Exceptions

A13.1 Departures from the policy or this annex require a written exception approved by the
annex owner, with the risk accepted in writing by a named senior owner. Exceptions are
time-bound (maximum [6 months]), carry compensating controls, and are recorded with expiry
dates. The committee reviews the register at every meeting; expired exceptions lapse
automatically.

A13.2 **No exception may be granted** to: process a permit category without a permit;
transfer personal data outside Oman otherwise than in accordance with policy Section 17;
process a child's data without verified guardian consent; or disable logging or audit
evidence.

A13.3 **An internal exception cannot substitute for a ministry decision.** Where the
framework provides for a permit, an approval or a grievance, only the ministry may grant
it, and the register records the application and its outcome rather than a self-granted
equivalent.

A13.4 Administrative sanctions available to the ministry include **warning, suspension of
the permit until the contravention is removed, an administrative fine per contravention,
and cancellation of the permit**. A person on whom a sanction is imposed may grieve to the
Minister **within 60 days**, and the Minister decides within **30 days**, with silence a
rejection. The committee records any sanction and any grievance.

## A14. Agentic AI

A14.1 AI agents operate under their own credentials with least-privilege access. A
person's own credentials must never be given to an agent.

A14.2 **An agent's reachable data set is classified in advance**, and an agent must not be
able to reach a permit category unless the permit covers it and the agent is within the
approved tooling.

A14.3 **An agent must not be able to move personal data outside Oman** other than to a
destination in the Transfer Register with a current assessment. Where an agent can select
its own tools or data sources, the committee assesses whether it can reach an
unassessed destination at all, and constrains it if so.

A14.4 Consequential actions - payments, external communications, changes to records about
people, code deployment, publication, deletion - require a human checkpoint before
execution unless the committee has expressly approved autonomous operation for that action
and system.

A14.5 An agent must not delete personal data subject to a live request, an open incident,
or a retention obligation.

A14.6 Agent activity is logged and attributable to a named human owner; sessions are
bounded in scope and duration; every agent has a documented means of immediate suspension.

A14.7 Content an agent ingests from outside [ORGANISATION] is treated as untrusted input,
including instructions embedded in that content.

## A15. What this annex does not assert

A15.1 This annex rests on the personal data protection law, its executive regulations and
the national AI policy, all held in full.

A15.2 It does **not** state any requirement of [ORGANISATION]'s sector regulator, of the
national data governance and management regulatory framework, of the national records law,
of the cybercrime law, of the IT risk management framework, or of the national AI and
advanced digital technologies programme. **None of those is held**, and the national AI
policy names several of them as related issuances.

A15.3 It does not state the competences of the Electronic Defence Centre, which the law
expressly preserves.

A15.4 **It does not apply to units of the State's administrative apparatus**, which are
governed by a separate national personal data protection policy. That instrument is held
and would be the basis of a separate government-sector document.

A15.5 **The committee treats obtaining the sector regulator's issuances as a standing
action**, because for a private-sector institution that regulator - not the issuing
ministry - monitors compliance with the national AI policy.

---

**Version history:**
1.0 - initial annex, published 3 September 2026; written from the enacted Arabic
texts and checked against MTCIT's official English texts, per the research note and
source register.

---

*This document is an educational policy template and does not constitute legal advice.
It reflects obligations under Omani personal data protection law and national AI policy
as set out in the accompanying research note, and must be reviewed by the Personal Data
Protection Officer or qualified legal counsel before adoption.*
