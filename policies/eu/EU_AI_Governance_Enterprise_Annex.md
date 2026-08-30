# AI Governance - Enterprise Annex - European Union

**Organisation:** [ORGANISATION]
**Effective date:** [DATE]  **Version:** 1.0
**Annex owner:** [CISO / Head of AI Governance]  **Data protection lead:** [DPO / privacy lead]
**Classification:** Internal
**Review:** at least every six months, and on material change in tools or regulation

This annex extends the [ORGANISATION] Artificial Intelligence Acceptable Use Policy
(European Union) for large organisations. The policy governs how individuals use AI;
this annex governs how the organisation manages AI as a portfolio - oversight,
classification, commencement readiness, inventory, lifecycle, suppliers, and
assurance. Where this annex and the policy overlap, the stricter requirement applies.

---

## A1. Governance structure and accountability

A1.1 [ORGANISATION] maintains an AI Governance Committee with a defined remit:
approving this annex and the Acceptable Use Policy, approving Level 3 and Level 4
uses, approving exceptions, reviewing incidents and metrics, owning the commencement
calendar in A3, and monitoring regulatory change. Membership includes [security, data
protection, legal, risk, HR, and business representation]. The committee meets at
least quarterly.

A1.2 A named senior executive is accountable for AI governance across the organisation
and reports on it to the board at least [twice yearly], including the state of
high-risk readiness under A3.

A1.3 Responsibility follows three lines: business functions own the risks of the AI
they use; risk and compliance functions set standards and challenge; internal audit
provides independent assurance (A8).

A1.4 The data protection lead's statutory independence is preserved. They report to
the highest management level, are not instructed on how to perform the role, and are
not penalised for performing it. The committee must not place them in a position of
conflict.

## A2. AI system inventory

A2.1 Every AI system used or deployed by [ORGANISATION] - bought, built, or embedded
in other software - must be recorded in the AI system inventory before use. The record
states: business owner; purpose; **the role [ORGANISATION] holds for that system,
provider or deployer**; risk level (policy Section 5); **whether the system would fall
in the high-risk category and on what basis**; data categories processed; lawful basis;
supplier and underlying model where known; the point of human oversight; processing
locations and transfer basis; and the next review date.

A2.2 An AI system not in the inventory is treated as an unapproved tool under policy
Section 3. The inventory is reviewed [quarterly]. Material changes to a recorded
system reopen its approval and require the role and classification fields to be
re-assessed.

A2.3 The inventory is the source for the record of processing activities maintained
under data protection law; the two must not diverge.

## A3. Commencement readiness register

**This section exists because the artificial intelligence regime commences in stages.
Its purpose is to make sure the deferral of the high-risk regime is used rather than
forgotten.**

A3.1 [ORGANISATION] maintains a Commencement Readiness Register alongside the
inventory. For every system classified as high-risk-when-commenced under A2.1 it
records: the classification basis; the applicable commencement date; the named
readiness owner; the gap assessment against the high-risk requirements; the
remediation plan and its milestones; and the decision point at which the system will
be withdrawn if it will not be ready.

A3.2 **A system may not be approved on the basis that the obligations do not apply
yet.** Approval must state when they will apply and who owns readiness.

A3.3 The committee reviews the register at every meeting. Any system on the high-risk
track without a named owner or a dated plan is escalated to the accountable executive
at A1.2.

A3.4 The register also tracks obligations that commence for [ORGANISATION] between now
and then, including the two further prohibited practices taking effect in December
2026 (policy Section 6.2), so that tooling is checked before rather than after each
date.

A3.5 **Regulatory change is a standing agenda item.** The artificial intelligence
regime has already been amended once to change its own commencement dates. The
committee records, at each meeting, the version of the consolidated text the
organisation's position rests on.

## A4. Lifecycle controls for systems the organisation builds or adapts

A4.1 Before deployment: documented purpose and success criteria; the role and
classification assessment under A2.1; testing for accuracy, robustness, security and
bias proportionate to the risk level; the data protection impact assessment where
policy Section 7.6 requires one; and sign-off by the business owner and, where
personal data is involved, the data protection lead.

A4.2 In change: modifications with a material effect on behaviour - model, prompt,
configuration, or training data changes - go through change management and re-testing
proportionate to the change, **and a re-assessment of whether the change makes
[ORGANISATION] a provider** (policy Section 2.1).

A4.3 In operation: deployed systems are monitored for degraded performance, drift, and
misuse; agreed thresholds trigger review by the business owner. Where a system falls
within the transparency obligations, the disclosures required by policy Section 9 are
verified as actually present in the live product, not merely specified.

A4.4 At retirement: a decommissioning step covering data disposal, dependent
processes, and closure of the inventory and register records.

A4.5 Training data provenance is documented for any system [ORGANISATION] builds or
fine-tunes: what personal data was used, on what basis, whether the original purpose
covered that use, and what was done about accuracy and bias.

## A5. Suppliers and supply chain

A5.1 No AI service is procured or renewed without the security and data protection
review in policy Section 3, and a written contract covering: processing only on
[ORGANISATION]'s documented instructions; confidentiality; security measures;
sub-processor authorisation and flow-down; assistance with individuals' rights,
impact assessments and breach notification; deletion or return at end of service; and
audit rights.

A5.2 AI-specific terms additionally cover: no use of [ORGANISATION] data to train the
supplier's models without express approval; disclosure of material model changes;
disclosure of actual processing locations and any change to them; and exit
arrangements.

A5.3 Where the supplier is or may become a provider of a high-risk system,
[ORGANISATION] obtains the information and documentation it will need to discharge
its own deployer duties when that regime commences, and records whether the supplier
has committed to supply it.

A5.4 **Breach notification timing must be contractual, not aspirational.**
[ORGANISATION]'s own 72-hour clock starts when it becomes aware; a supplier term that
allows notification in a longer period makes that clock impossible to meet.

A5.5 Critical AI suppliers are reassessed at least annually. For any AI service the
business critically depends on, an exit plan exists and concentration risk is reviewed
by the committee.

## A6. Exceptions

A6.1 Departures from the policy or this annex require a written exception approved by
the annex owner, with the risk accepted in writing by a named senior owner. Exceptions
are time-bound (maximum [6 months]), carry compensating controls, and are recorded in
an exceptions register with expiry dates. The committee reviews the register at every
meeting; expired exceptions lapse automatically.

A6.2 **No exception may be granted against a prohibited practice** (policy Section
6.1). Those are not risks the organisation is able to accept, and no assessment,
consent or business justification changes that.

## A7. Agentic AI

A7.1 AI agents - systems that plan and take actions with limited human prompting -
operate under their own credentials with least-privilege access. A person's own
credentials must never be given to an agent.

A7.2 Consequential actions - making payments, sending external communications,
changing records about people, deploying code, or deleting data - require a human
checkpoint before execution unless the committee has expressly approved autonomous
operation for that action and system.

A7.3 An agent must not initiate processing of personal data outside the basis recorded
for it, must not transfer personal data outside the Union other than on a recorded
basis, and must not take any action within a prohibited practice. An agent that can
select its own tools or data sources is assessed for whether it can reach such
processing at all.

A7.4 Where an agent interacts with a person, the disclosure in policy Section 9.1
applies to the agent.

A7.5 Agent activity is logged and attributable to a named human owner. Agent sessions
are bounded in scope and duration, and every agent has a documented means of immediate
suspension.

A7.6 Content an agent ingests from outside the organisation is treated as untrusted
input, including instructions embedded in that content.

## A8. Individual rights operations

A8.1 [ORGANISATION] maintains a documented route by which a request from an individual
- for access, rectification, erasure, restriction, portability, or objection - is
executed against every AI system in the inventory, including prompts, uploads,
embeddings, caches and logs.

A8.2 The statutory response period is one month from receipt, extendable by two
further months where necessary given complexity and number, with the individual
informed of the extension and the reasons within the first month. Systems that cannot
support this are not approved for personal data.

A8.3 Where an individual contests a decision based solely on automated processing,
human intervention is provided by a person with authority to change the outcome, and
the intervention and its result are recorded.

A8.4 Where personal data is rectified or erased, recipients to whom it was disclosed
are informed unless that proves impossible or involves disproportionate effort. AI
suppliers are such recipients.

## A9. Assurance and metrics

A9.1 The committee tracks agreed indicators, including: approved-tool adoption;
unapproved-tool discoveries; **systems on the high-risk track without a dated
readiness plan, which should be zero**; transparency disclosures verified present in
live products; verification records for decision-bearing output; incidents and near
misses; time from breach awareness to notification; exception count and age; and
impact-assessment coverage for Level 3 and Level 4 uses.

A9.2 Internal audit reviews the AI governance programme at least [annually], including
a sample test that inventory classifications match what systems actually do.

A9.3 The committee conducts a management review of the whole programme at least
[annually]: policy and annex, inventory, readiness register, metrics, incidents,
supplier performance, and regulatory change, with documented actions.

## A10. Complaints and speak-up

A10.1 Individuals can complain to [ORGANISATION] about the handling of their personal
data, including by AI systems, and may complain to a supervisory authority
independently and without complaining to [ORGANISATION] first. [ORGANISATION] provides
an accessible means of complaint and informs the complainant of the outcome. [DPO /
privacy lead] owns this process.

A10.2 Staff can raise concerns about AI use - bias, safety, misuse, or pressure to
bypass controls - outside their line management and without detriment, through
[speak-up channel]. A concern that a system may be within a prohibited practice is
treated as urgent and routed to the annex owner and data protection lead the same day.

## A11. Sector overlay [regulated firms]

A11.1 Where [ORGANISATION] is regulated, the committee maps this annex to the sector's
requirements and records the mapping in the inventory and risk register.

A11.2 **Financial entities: see the separate DORA annex.** Union digital operational
resilience law imposes a distinct regime on financial entities in respect of ICT
third-party service providers, which is what AI vendors are. That regime is not
covered here and is **not** asserted in this annex; it requires its own document
grounded in its own primary text.

---

*This document is an educational policy template and does not constitute legal advice.
It reflects obligations under Union data protection and artificial intelligence law as
consolidated at the date of the accompanying research note, and must be reviewed by
the data protection lead or qualified legal counsel before adoption.*
