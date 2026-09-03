# AI Governance - Enterprise Annex - India

**Organisation:** [ORGANISATION]
**Effective date:** [DATE]  **Version:** 1.1
**Annex owner:** [CISO / Head of AI Governance]  **Data protection lead:** [Data Protection Officer / privacy lead]
**Classification:** Internal
**Review:** at least every six months, and on material change in tools or regulation

This annex extends the [ORGANISATION] Artificial Intelligence Acceptable Use Policy
(India) for large organisations. The policy governs how individuals use AI; this annex
governs how the organisation manages AI as a portfolio - oversight, classification,
commencement readiness, inventory, lifecycle, suppliers, and assurance. Where this
annex and the policy overlap, the stricter requirement applies.

---

## A1. Governance structure and accountability

A1.1 [ORGANISATION] maintains an AI Governance Committee with a defined remit:
approving this annex and the Acceptable Use Policy, approving Level 3 and Level 4
uses, approving exceptions, reviewing incidents and metrics, owning the commencement
calendar in A3, owning the Significant Data Fiduciary readiness position in A4, and
monitoring regulatory change. Membership includes [security, data protection, legal,
risk, HR, and business representation]. The committee meets at least quarterly.

A1.2 A named senior executive is accountable for AI governance across the organisation
and reports on it to the board at least [twice yearly], including the state of
readiness for the May 2027 commencement.

A1.3 **Contact information is a published obligation, not an internal assignment.**
[ORGANISATION] prominently publishes on its website or app the business contact
information of the Data Protection Officer where one is required, or of a person able
to answer individuals' questions about the processing of their personal data, and
ensures that information appears in every response to a rights communication. The
annex owner verifies both placements at each review, because the second is the one
that decays.

A1.4 Responsibility follows three lines: business functions own the risks of the AI
they use; risk and compliance functions set standards and challenge; internal audit
provides independent assurance (A10).

## A2. AI system inventory

A2.1 Every AI system used or deployed by [ORGANISATION] - bought, built, or embedded
in other software - must be recorded in the AI system inventory before use. The record
states: business owner; purpose; **the role [ORGANISATION] holds, Data Fiduciary or
Data Processor**; risk level (policy clause 5); the categories of personal data
processed and whether any belongs to a child or a person with disability who has a
lawful guardian; the basis and the notice used; supplier and underlying model where
known; the point of human determination; **processing and storage locations**;
**the retention position in both directions - the one-year minimum and any applicable
erasure duty**; **whether the system can identify whose data a given exposure touched**
(policy 15.6); and the next review date.

A2.2 An AI system not in the inventory is treated as an unapproved tool under policy
clause 3.

A2.3 The inventory is reviewed [quarterly]. Material changes to a recorded system -
model, supplier, processing location, retention behaviour, or purpose - reopen its
approval.

A2.4 The inventory is the operational record of what personal data [ORGANISATION]
processes by AI and must not diverge from the organisation's wider data inventory.

## A3. Commencement readiness register

**This clause exists because the compliance obligations commence on 13 May 2027 and
almost nothing binds before then. Its purpose is to make sure the interval is used
rather than forgotten.**

A3.1 [ORGANISATION] maintains a Commencement Readiness Register alongside the
inventory. For every AI system that will process personal data it records: the
obligations that will apply on commencement; the named readiness owner; the gap
assessment; the remediation plan and its milestones; and the decision point at which
the system will be withdrawn or replaced if it will not be ready.

A3.2 **A system may not be approved on the basis that the obligations do not apply
yet.** Approval must state when they will apply and who owns readiness.

A3.3 The register carries, at minimum, a readiness line for each of: the notice
contents and the parity between giving and withdrawing consent; the minimum security
safeguards list; breach intimation to individuals and to the Board on the two clocks;
the one-year retention minimum; any applicable erasure duty and its forty-eight hour
advance notice; the published rights-request means and the grievance redressal period;
the transfer position; and, if applicable, the Significant Data Fiduciary duties.

A3.4 The register also tracks the intermediate commencement of the Consent Manager
provisions in November 2026, so that any dependency on that institution is identified
before it exists rather than after.

A3.5 **Eighteen months is inside the life of every contract signed today.** Procurement
does not treat the deferral as a reason to omit a requirement from a contract; A6.2
lists the terms that go in now.

A3.6 **Regulatory change is a standing agenda item.** The committee records, at each
meeting, the version of the subordinate legislation the organisation's position rests
on, including any corrigenda, and the version of the Act and its commencement
notification. It also records the open items at policy 22.5 and whether any has
closed.

## A4. Significant Data Fiduciary readiness

A4.1 Notification as a Significant Data Fiduciary is a decision of the Central
Government and is not within [ORGANISATION]'s control. The committee maintains a
standing view of whether notification is plausible, on what basis, and what would
change if it occurred.

A4.2 [ORGANISATION] treats the following as the readiness set, and applies the third
of them from today as a house standard under policy 11.4:

- the appointment of a Data Protection Officer based in India, responsible to the
  board and the point of contact for grievances, and of an independent data auditor;
- the annual data protection impact assessment and audit, and the report of
  significant observations furnished to the Board;
- the restriction that specified personal data and its traffic data is not transferred
  outside India;
- **due diligence to verify that technical measures, including algorithmic software,
  are not likely to pose a risk to individuals' rights.**

A4.3 The due diligence record required by policy 11.5 is held for every Level 4 system
whether or not [ORGANISATION] is notified. The committee reviews the set at each
meeting and treats a Level 4 system without a current record as an open finding.

A4.4 **The localisation duty is a design constraint before it is a compliance one.**
Where a Level 3 or Level 4 system holds personal data that could plausibly fall within
a future specification, the architecture must permit relocating that data and its
traffic data to India without redesign. The inventory records whether it does.

A4.5 An assessment for the purpose of notifying a Data Fiduciary as significant is a
matter for which the Central Government may call for information. The committee
ensures the inventory, the due diligence records and the impact assessments could be
produced at short notice.

## A5. Lifecycle controls for systems the organisation builds or adapts

A5.1 Before deployment: documented purpose and success criteria; the role and level
assessment under A2.1; the notice and basis; the retention determination under A7;
testing for accuracy, robustness, security and disparate outcome proportionate to the
level; and sign-off by the business owner and, where personal data is involved, the
data protection lead.

A5.2 In change: modifications with a material effect on behaviour - model, prompt,
configuration, or training data changes - go through change management and re-testing
proportionate to the change, and a re-assessment of whether the notice given still
describes what the system does. **An itemised notice becomes inaccurate quietly**, and
a change that adds a data field or a purpose is a change to the notice.

A5.3 In operation: deployed systems are monitored for degraded performance, drift, and
misuse; agreed thresholds trigger review by the business owner.

A5.4 At retirement: a decommissioning step covering the inventory and register records,
dependent processes, and **disposal that respects the one-year minimum rather than
overriding it**. Decommissioning does not authorise deleting data the minimum period
still covers; the data outlives the system and its custody is reassigned.

A5.5 Training data provenance is documented for any system [ORGANISATION] builds or
fine-tunes: what personal data was used, on what basis, what notice covered it, and
what was done about accuracy and disparate outcome.

A5.6 **A model fine-tuned on personal data may retain it.** Before any such model is
deployed, [ORGANISATION] records how a request from an individual would be given
effect against it, and, where that is not possible, does not fine-tune on that data.

## A6. Suppliers and the Data Processor relationship

A6.1 No AI service is procured or renewed without the security and data protection
review in policy clause 3 and a written contract.

A6.2 The contract must include, from today and regardless of commencement dates:

- **an appropriate provision for taking reasonable security safeguards** - this is a
  specific requirement of the framework, directed at the contract itself;
- processing only on [ORGANISATION]'s documented instructions and only for the stated
  purpose;
- **retention that satisfies the one-year minimum**, and the ability to configure
  retention rather than inherit a vendor default;
- immediate notification to [ORGANISATION] on the supplier becoming aware of a breach,
  with enough detail to populate the intimations at policy 15.2 to 15.4;
- **the ability to identify whose personal data a given exposure touched**;
- disclosure of actual processing and storage locations, and of any change to them,
  with notice sufficient to reassess before the change takes effect;
- no use of [ORGANISATION] data to train the supplier's models without express
  approval;
- disclosure of material model changes;
- assistance with individuals' requests and with locating personal data across prompts,
  logs, embeddings and caches;
- sub-processor authorisation and flow-down;
- deletion or return at end of service, subject to the minimum retention period;
- audit rights; and
- exit arrangements.

A6.3 **[ORGANISATION] remains the Data Fiduciary for personal data processed on its
behalf.** Contractual allocation of responsibility between the parties does not change
that position externally, and the committee does not treat a supplier commitment as a
substitute for a control [ORGANISATION] can evidence.

A6.4 **A supplier's zero-retention or short-retention offering is not a privacy
feature here.** Where a supplier markets one, procurement records that it cannot be
used for personal data and either negotiates a compliant configuration or declines
the supplier for Level 3 and Level 4.

A6.5 Where [ORGANISATION] is itself the Data Processor for a client, the annex owner
maintains the list of such engagements. **AI tools may not be introduced into
processing carried out for a client without that client's documented instruction**,
and the duty to notify them immediately on suspecting a breach is operationalised in
the incident process rather than left to the contract.

A6.6 Critical AI suppliers are reassessed at least annually. For any AI service the
business critically depends on, an exit plan exists and concentration risk is reviewed
by the committee.

## A7. Retention governance

**Retention in this framework has a floor and, for some organisations, a ceiling. Both
are engineered, and neither is a default.**

A7.1 The committee maintains a Retention Register recording, for each AI system: the
one-year minimum and where it is enforced; whether any erasure duty applies to
[ORGANISATION] for that processing; the erasure period if so; **how the forty-eight
hour advance notice to the individual is generated**; and who owns the configuration.

A7.2 **[ORGANISATION] determines in writing whether it falls within any class subject
to the erasure duty.** The classes are defined by sector and by registered-user scale.
A determination that the organisation falls outside them is recorded with the reason
and is revisited whenever user numbers change materially, because the trigger is a
threshold the business can cross without noticing.

A7.3 Where an erasure duty applies, the advance-notice step is built into the system.
A forty-eight hour notice generated manually will not survive contact with volume.

A7.4 **Where the minimum retention period and an erasure duty appear to conflict for a
particular dataset, the data protection lead resolves it in writing before
configuration.** The committee reviews every such resolution. A team must not resolve
it by choosing the shorter period, and an unresolved conflict blocks approval.

A7.5 Retention automation must not delete data that is subject to a live request from
an individual, a live grievance, an open breach investigation, or the minimum period.
The committee tests this annually against a sample.

A7.6 The Retention Register covers supplier-side retention as well as
[ORGANISATION]'s own. A supplier whose retention cannot be evidenced is treated as a
system whose retention position is unknown.

## A8. Breach operations

A8.1 The incident process is built around the fact that **there is no threshold**. It
contains no assessment gate before intimation, and no step at which an incident is
closed on the basis that it was too small to report.

A8.2 The process holds pre-drafted intimation templates carrying the prescribed
contents for the individual intimation and for both Board intimations, so that
drafting time does not consume the clocks. Templates are reviewed [annually] and after
any use.

A8.3 **Awareness is recorded as a timestamp, by a named person, at the moment it
occurs.** Both clocks run from it. The committee reviews any incident where the
recorded awareness time was reconstructed after the fact.

A8.4 The process identifies, at the outset of every incident, **who is affected**, and
escalates immediately where the system cannot answer that (policy 15.6). Inability to
enumerate affected individuals is itself an open finding against that system.

A8.5 Where a longer period for the detailed Board report is needed, the written
request is made **before** the seventy-two hours expire. The committee treats a late
request as a separate failure from the late report.

A8.6 Post-incident, the committee reviews: time from occurrence to awareness; time
from awareness to individual intimation; time from awareness to first Board
intimation; time from awareness to the detailed report; and whether any supplier term
constrained any of these.

## A9. Exceptions

A9.1 Departures from the policy or this annex require a written exception approved by
the annex owner, with the risk accepted in writing by a named senior owner. Exceptions
are time-bound (maximum [6 months]), carry compensating controls, and are recorded in
an exceptions register with expiry dates. The committee reviews the register at every
meeting; expired exceptions lapse automatically.

A9.2 **No exception may be granted to delete personal data, traffic data or processing
logs before the minimum retention period**, and none to bypass a control in this
policy. Those are not risks the organisation is able to accept.

A9.3 An exception may not be granted to process a child's personal data, or that of a
person with disability who has a lawful guardian, without the verification at policy
clause 9. Verification is a factual determination, not a risk to be accepted.

## A10. Agentic AI, assurance and metrics

A10.1 AI agents operate under their own credentials with least-privilege access. A
person's own credentials must never be given to an agent.

A10.2 Consequential actions - making payments, sending external communications,
changing records about people, deploying code, or deleting data - require a human
checkpoint before execution unless the committee has expressly approved autonomous
operation for that action and system. **An agent must not be able to delete personal
data at all** where the minimum retention period, a live request, or an open incident
covers it.

A10.3 An agent must not process personal data outside the basis and notice recorded
for it, must not transfer personal data outside India other than on a recorded
position, and must not disclose personal data to any destination not covered by an
approval. An agent that can select its own tools or data sources is assessed for
whether it can reach such a disclosure at all.

A10.4 Agent activity is logged and attributable to a named human owner, sessions are
bounded in scope and duration, and every agent has a documented means of immediate
suspension. Agent logs are within the minimum retention period.

A10.5 Content an agent ingests from outside the organisation is treated as untrusted
input, including instructions embedded in that content.

A10.6 Internal audit reviews the AI governance programme at least [annually],
including a sample test that inventory classifications match what systems actually do,
a sample test that retention is configured as the Retention Register states, and a
walkthrough of the breach process against a simulated incident.

A10.7 The committee tracks agreed indicators, including:

- approved-tool adoption, and unapproved-tool discoveries;
- **Level 3 and Level 4 systems with no recorded basis or notice, which should be
  zero**;
- **systems whose retention does not match the Retention Register, which should be
  zero**;
- **systems that cannot enumerate affected individuals, which should be zero**;
- systems on the readiness register with no named owner or no dated plan;
- Level 4 systems without a current due diligence record;
- time from occurrence to awareness, and the three intimation intervals at A8.6;
- individuals' requests executed against AI systems, and any that could not be;
- grievance response times against the internal service level and against ninety days;
- exception count and age;
- training completion, reported separately for the retention and breach modules.

A10.8 The committee conducts a management review of the whole programme at least
[annually]: policy and annex, inventory, readiness register, retention register,
metrics, incidents, supplier performance, and regulatory change, with documented
actions.

## A11. Complaints, speak-up, and the Board

A11.1 Individuals can complain to [ORGANISATION] about the handling of their personal
data, including by AI systems, through the published grievance redressal system, and
[ORGANISATION] responds within its internal service level and in any event within the
ninety-day outer limit. The data protection lead owns this process.

A11.2 Individuals may complain to the Board, and the notice given to them must tell
them how. The committee ensures that route is described accurately in every notice
template, including those presented inside AI-driven flows.

A11.3 The Board functions as a digital office and may conduct proceedings without
physical presence. An inquiry is to be completed within six months of the intimation,
complaint, reference or direction, extendable by the Board for recorded reasons.
**[ORGANISATION] is expected to be able to respond digitally and at short notice**, and
the committee maintains the readiness to do so.

A11.4 An appeal against an order or direction of the Board lies to the Appellate
Tribunal, filed in digital form. The committee records any matter that could give rise
to one.

A11.5 Staff can raise concerns about AI use - inaccuracy, unfair outcome, misuse, or
pressure to bypass controls - outside their line management and without detriment,
through [speak-up channel]. **A concern that personal data has been exposed is routed
to the incident process the same hour**, because both breach clocks run from awareness.

## A12. Sector overlay [regulated firms]

A12.1 Where [ORGANISATION] is regulated, the committee maps this annex to the sector's
requirements and records the mapping in the inventory and risk register.

A12.2 Sector regulators impose their own technology risk, outsourcing, incident
reporting and data localisation requirements, and AI suppliers fall within them.
**Those requirements are not covered by this annex and are not asserted in it.** They
require their own document grounded in the relevant regulator's own instruments, which
this set does not hold. Where a sector incident-reporting clock is shorter than the
clocks at policy clause 15, the shorter one governs.

## A13. What this annex rests on, and what remains open

A13.1 This annex, like the policy, rests on the Act, the rules and the notifications
[ORGANISATION] holds. Where a control exceeds what any of them requires, it is
labelled a house standard where it appears.

A13.2 The items that remain open are listed at policy 22.5: transfer orders and
restriction notifications, the localisation specification, Significant Data Fiduciary
and age-exemption notifications, sector instruments, and Board decisions. None is
guessed at.

A13.3 **The committee treats each open item as a standing action**, reviewed at every
meeting, and records the date on which any of them closes.

---

*This document is an educational policy template and does not constitute legal advice.
It reflects obligations under Indian digital personal data protection law as set out
in the accompanying research note, and must be reviewed by the data protection lead or
qualified legal counsel before adoption.*
