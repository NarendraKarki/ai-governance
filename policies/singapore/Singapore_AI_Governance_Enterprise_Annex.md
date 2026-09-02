# AI Governance - Enterprise Annex - Singapore

**Organisation:** [ORGANISATION]
**Effective date:** [DATE]  **Version:** 1.0
**Annex owner:** [CISO / Head of AI Governance]  **Data protection lead:** [Data Protection Officer]
**Classification:** Internal
**Review:** at least every six months, and on material change in tools or regulation

This annex extends the [ORGANISATION] Artificial Intelligence Acceptable Use Policy
(Singapore) for large organisations. The policy governs how individuals use AI; this
annex governs how the organisation manages AI as a portfolio - oversight,
classification, inventory, lifecycle, suppliers, and assurance. Where this annex and
the policy overlap, the stricter requirement applies.

---

## A1. Governance structure and accountability

A1.1 [ORGANISATION] maintains an AI Governance Committee with a defined remit:
approving this annex and the Acceptable Use Policy, approving Level 3 and Level 4
uses, approving exceptions, reviewing incidents and metrics, owning the assessment
register in A3, and monitoring regulatory change and regulator guidance. Membership
includes [security, data protection, legal, risk, HR, and business representation].
The committee meets at least quarterly.

A1.2 A named senior executive is accountable for AI governance across the organisation
and reports on it to the board at least [twice yearly].

A1.3 **The designated individual required by law is a statutory role, not a committee
seat.** [ORGANISATION] designates one or more individuals responsible for ensuring
compliance, makes the business contact information of at least one of them available
to the public, and keeps that information current. Designation does not relieve
[ORGANISATION] of any obligation, and this annex does not treat the designation as
transferring accountability away from the business.

A1.4 Where the designation is delegated to another individual, the delegation is
recorded, and the delegate is given the authority and the access the role requires.

A1.5 Responsibility follows three lines: business functions own the risks of the AI
they use; risk and compliance functions set standards and challenge; internal audit
provides independent assurance (A9).

## A2. AI system inventory

A2.1 Every AI system used or deployed by [ORGANISATION] - bought, built, or embedded
in other software - must be recorded in the AI system inventory before use. The record
states: business owner; purpose; **the role [ORGANISATION] holds for that system,
organisation or data intermediary**; risk level (policy Section 5); the categories of
personal data processed; **the lawful basis and, where one is required, the reference
to the completed assessment**; supplier and underlying model where known; the point of
human determination; **processing and storage locations and the transfer basis**;
**the retention position across prompts, logs, embeddings and caches**; and the next
review date.

A2.2 An AI system not in the inventory is treated as an unapproved tool under policy
Section 3, and its use may engage policy Section 11.

A2.3 The inventory is reviewed [quarterly]. Material changes to a recorded system -
model, supplier, processing location, retention behaviour, or purpose - reopen its
approval and require the lawful basis and the transfer basis to be re-assessed.

A2.4 The inventory is the operational record of what personal data the organisation
processes by AI, and must not diverge from the organisation's wider data inventory.

## A3. Assessment register

**This section exists because the assessments Singapore law requires are conditions of
lawfulness, not documentation. Where an assessment is required and has not been done,
the processing has no basis - it is not merely unevidenced.**

A3.1 [ORGANISATION] maintains an Assessment Register alongside the inventory. It
records, for every processing that depends on an assessment: the system; the basis
relied on; the date of the assessment; who conducted and who approved it; the adverse
effects identified; the measures identified; **the date each measure was actually
implemented**; and the review date.

A3.2 **An assessment that identifies a measure and does not implement it does not
satisfy the requirement.** The register carries an implementation date for every
measure, and the committee treats a measure identified but not implemented as an open
finding, not as a completed assessment.

A3.3 An assessment is required, and is recorded here, wherever [ORGANISATION] relies
on deemed consent by notification or on legitimate interests. [ORGANISATION]
additionally requires one for every Level 4 use whatever the basis, as a house
standard.

A3.4 **The assessment must precede the processing.** A record created after processing
has begun is remediation, is labelled as such in the register, and is reported to the
committee.

A3.5 Where reliance is placed on the business improvement purpose, the register
additionally records why the purpose cannot reasonably be achieved without personal
data in individually identifiable form, and the data protection lead's confirmation
that the basis is available to the entity relying on it and for the data flow
concerned.

A3.6 Where reliance is placed on the research basis, the register records the
confirmation that **the results will not be used to make any decision affecting the
individual**. Where model output will inform such a decision, this basis is
unavailable, and the register records the alternative relied on.

## A4. Lifecycle controls for systems the organisation builds or adapts

A4.1 Before deployment: documented purpose and success criteria; the role and level
assessment under A2.1; the lawful basis and the A3 assessment; testing for accuracy,
robustness, security and disparate outcome proportionate to the level; and sign-off by
the business owner and, where personal data is involved, the data protection lead.

A4.2 In change: modifications with a material effect on behaviour - model, prompt,
configuration, or training data changes - go through change management and re-testing
proportionate to the change, **and a re-assessment of whether the lawful basis still
covers what the system now does**.

A4.3 In operation: deployed systems are monitored for degraded performance, drift, and
misuse; agreed thresholds trigger review by the business owner.

A4.4 At retirement: a decommissioning step covering data disposal across every store
identified under A2.1, dependent processes, and closure of the inventory and register
records. **Retirement is where the retention obligation is most often missed**, and
the committee sees evidence of disposal, not an assertion of it.

A4.5 Training data provenance is documented for any system [ORGANISATION] builds or
fine-tunes: what personal data was used, on what basis, whether the purpose the data
was collected for covers that use, and what was done about accuracy and disparate
outcome.

A4.6 **A model fine-tuned on personal data may retain it.** Before any such model is
deployed, [ORGANISATION] records how an access request and a correction or withdrawal
would be given effect against it, and, where that is not possible, does not fine-tune
on that data.

## A5. Suppliers and the data intermediary relationship

A5.1 No AI service is procured or renewed without the security and data protection
review in policy Section 3 and **a contract evidenced or made in writing**. The
written contract is the condition on which the supplier's status as a data
intermediary rests; without it, the supplier holds full obligations it has not agreed
to, and [ORGANISATION] holds a risk it has not assessed.

A5.2 The contract covers: processing only on [ORGANISATION]'s documented instructions
and only for the stated purpose; confidentiality; **reasonable security arrangements**;
**the supplier ceasing to retain the data once the purpose is served**; sub-processor
authorisation and flow-down; assistance with access and correction requests; deletion
or return at end of service; and audit rights.

A5.3 **[ORGANISATION] retains every obligation for personal data processed on its
behalf as though it had processed the data itself.** Contractual allocation of
responsibility between the parties does not change that position externally. The
committee is not permitted to treat a supplier commitment as a substitute for a
control [ORGANISATION] can evidence.

A5.4 AI-specific terms additionally cover: **no use of [ORGANISATION] data to train
the supplier's models without express approval**; disclosure of material model
changes; disclosure of actual processing and storage locations and any change to them;
prompt and log retention, and whether it can be configured or disabled; and exit
arrangements.

A5.5 **Breach notification timing must be contractual, not aspirational.** A supplier
must notify [ORGANISATION] without undue delay on having reason to believe a breach
has occurred. [ORGANISATION]'s own duty is to assess expeditiously and then to notify
within 3 calendar days of that assessment; a supplier term that permits notification
after a long fixed period makes that sequence impossible and is not accepted.

A5.6 Where [ORGANISATION] is itself the data intermediary for a client, the annex
owner maintains the list of such engagements. **AI tools may not be introduced into
processing carried out for a client without that client's documented instruction**,
and the duty to notify the client without undue delay on suspecting a breach is
operationalised in the incident process, not left to the contract.

A5.7 Critical AI suppliers are reassessed at least annually. For any AI service the
business critically depends on, an exit plan exists and concentration risk is reviewed
by the committee.

## A6. Cross-border processing

A6.1 The committee maintains a current register of where each AI system processes and
stores personal data - inference, human review, logging, support, and backup - and the
transfer basis for each.

A6.2 A supplier that will not state its processing locations is not approved for
personal data. A supplier that reserves the right to change them without notice is
approved only where the contract requires notice sufficient for A6.3.

A6.3 A change of processing location reopens the transfer basis before the change
takes effect, not after.

A6.4 The prescribed transfer requirements are set out in subordinate legislation. The
data protection lead maintains the organisation's current statement of them and brings
any change to the committee.

## A7. Exceptions

A7.1 Departures from the policy or this annex require a written exception approved by
the annex owner, with the risk accepted in writing by a named senior owner. Exceptions
are time-bound (maximum [6 months]), carry compensating controls, and are recorded in
an exceptions register with expiry dates. The committee reviews the register at every
meeting; expired exceptions lapse automatically.

A7.2 **No exception may be granted that would authorise conduct constituting an
offence** - in particular unauthorised re-identification of anonymised information, and
unauthorised disclosure or use of personal data held by [ORGANISATION]. Those are not
risks the organisation is able to accept on an individual's behalf, and an exception
purporting to grant them would not protect the individual.

A7.3 An exception permitting an AI tool to be used with personal data changes what is
authorised for the purposes of policy Section 11. Every such exception names the
individuals it covers, the data it covers, and its expiry, so that the boundary of
authorisation stays legible.

## A8. Agentic AI

A8.1 AI agents - systems that plan and take actions with limited human prompting -
operate under their own credentials with least-privilege access. A person's own
credentials must never be given to an agent.

A8.2 Consequential actions - making payments, sending external communications,
changing records about people, deploying code, or deleting data - require a human
checkpoint before execution unless the committee has expressly approved autonomous
operation for that action and system.

A8.3 An agent must not process personal data outside the basis recorded for it, must
not transfer personal data outside Singapore other than on a recorded basis, and must
not disclose personal data to any destination not covered by an approval. An agent
that can select its own tools or data sources is assessed for whether it can reach
such a disclosure at all.

A8.4 **An agent acting outside its recorded authorisation raises the question of whose
conduct it is.** Every agent has a named human owner recorded in the inventory, agent
activity is logged and attributable to that owner, sessions are bounded in scope and
duration, and every agent has a documented means of immediate suspension.

A8.5 An agent's deletion capability is constrained: an agent must not be able to
delete personal data that is subject to a preserved-copy obligation or a live access
or correction request.

A8.6 Content an agent ingests from outside the organisation is treated as untrusted
input, including instructions embedded in that content.

## A9. Individuals' requests, and assurance

A9.1 [ORGANISATION] maintains a documented route by which an access or correction
request is executed against every AI system in the inventory, including prompts,
uploads, embeddings, caches and logs. A system that cannot support this is not
approved for personal data.

A9.2 The correction process includes onward notification: corrected data goes to every
organisation it was disclosed to within the preceding year unless they have no legal
or business need for it. **AI suppliers holding the data are within this.** Where a
correction is refused, the annotation requirement is executed and recorded.

A9.2a **The inventory records, for each system, which of its outputs about individuals
are data the organisation has itself derived from other personal data it holds.** That
category is outside the statutory correction right but inside the access right, and
[ORGANISATION] applies its own correction standard to it under policy 17.5. The
committee tracks the count of derived-output corrections applied and refused, so that
the house standard is visible rather than assumed.

A9.2b Exceptions to the access requirement are applied only by the data protection
lead and are recorded with the reason. A refusal on the ground that disclosure would
reveal confidential commercial information is reviewed by the committee, because it is
the exception most easily overused where a model's behaviour is the commercially
sensitive thing.

A9.3 Where access is refused, the preserved-copy obligation is executed and the
preservation is evidenced. Disposal processes must not delete data subject to it, and
retention automation is configured accordingly.

A9.4 Internal audit reviews the AI governance programme at least [annually], including
a sample test that inventory classifications match what systems actually do, and a
sample test that assessments in the A3 register were completed **before** the
processing they cover.

A9.5 The committee conducts a management review of the whole programme at least
[annually]: policy and annex, inventory, assessment register, metrics, incidents,
supplier performance, regulator guidance and regulatory change, with documented
actions.

## A10. Metrics

A10.1 The committee tracks agreed indicators, including:

- approved-tool adoption, and unapproved-tool discoveries;
- **Level 3 and Level 4 systems with no recorded lawful basis, which should be zero**;
- **assessments with measures identified but not implemented, which should be zero**;
- assessments completed after processing began;
- systems with an unestablished processing location or transfer basis;
- verification records for decision-bearing output;
- incidents and near misses; time from suspicion to breach assessment; time from
  assessment to notification;
- access and correction requests executed against AI systems, and any that could not
  be;
- exception count and age;
- training completion, reported separately for the personal-liability module.

A10.2 Time from suspicion to assessment is reported alongside time from assessment to
notification. Reporting only the second conceals the delay that matters.

## A11. Complaints and speak-up

A11.1 [ORGANISATION] develops and implements policies and practices necessary to meet
its obligations, **develops a process to receive and respond to complaints**,
communicates its policies and practices to staff, and makes information about them and
about the complaint process available on request. This annex and the policy are part
of discharging that duty, and the complaint process is documented, resourced and
published rather than assumed.

A11.2 Individuals can complain to [ORGANISATION] about the handling of their personal
data, including by AI systems. [ORGANISATION] informs the complainant of the outcome.
The data protection lead owns this process.

A11.3 The Commission may refer a complaint to mediation under a dispute resolution
scheme, and may do so without the consent of either party. The committee ensures the
organisation can produce, at short notice, the inventory record, the lawful basis, the
assessment and the verification record for any system a complaint concerns.

A11.4 An individual who suffers loss or damage directly as a result of a contravention
of the data protection obligations may bring proceedings in their own right. The
records required by this annex are the organisation's evidence in that event, which is
a further reason they are made contemporaneously rather than reconstructed.

A11.5 Staff can raise concerns about AI use - inaccuracy, unfair outcome, misuse, or
pressure to bypass controls - outside their line management and without detriment,
through [speak-up channel]. **A concern that a member of staff has been asked to put
personal data into an unapproved tool is treated as urgent** and routed to the annex
owner and data protection lead the same day, because of the personal exposure at
policy Section 11.

## A12. Enforcement exposure

A12.1 The committee records, and reports to the accountable executive at A1.2, the
organisation's exposure under the enforcement provisions: directions to comply,
financial penalties, voluntary undertakings, and the right of private action.

A12.2 **Financial penalties for a contravention of the data protection obligations are
capped by reference to the organisation's annual turnover in Singapore where that
turnover exceeds a statutory threshold, and by a fixed sum otherwise.** The applicable
maximum is prescribed within those caps. The research note states the figures; the
committee records the organisation's own turnover position so that the exposure is
known rather than estimated in an incident.

A12.3 In setting a penalty the Commission must have regard to, among other matters,
whether the organisation had implemented adequate and appropriate compliance measures
despite the non-compliance, what it did to mitigate, and how promptly. The registers
required by this annex are how that is evidenced. This is stated here so that the
records are understood as mitigation, not as overhead.

A12.4 The committee reviews any voluntary undertaking given by [ORGANISATION] at every
meeting until it is discharged.

## A13. Sector overlay [regulated firms]

A13.1 Where [ORGANISATION] is regulated, the committee maps this annex to the sector's
requirements and records the mapping in the inventory and risk register.

A13.2 Sector regulators impose technology risk, outsourcing and operational resilience
requirements on the firms they supervise, and AI suppliers fall within them. **Those
requirements are not covered by this annex and are not asserted in it.** They require
their own document grounded in the relevant regulator's own instruments, which this
set does not hold.

---

**Version history:**
1.0 - initial annex, published 2 September 2026; every citation verified by
direct reading of the enacted Act, with the prescribed figures in subordinate
legislation routed per the research note rather than asserted.

---

*This document is an educational policy template and does not constitute legal advice.
It reflects obligations under Singapore personal data protection law as set out in the
accompanying research note, and must be reviewed by the data protection lead or
qualified legal counsel before adoption.*
