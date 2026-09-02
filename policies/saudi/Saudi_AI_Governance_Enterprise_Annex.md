# AI Governance - Enterprise Annex - Saudi Arabia

### Government data - public entities and their business partners

**Entity:** [ENTITY]
**Effective date:** [DATE]  **Version:** 1.0
**Annex owner:** [Chief Data Officer]  **Personal data lead:** [Personal Data Protection Officer]
**Classification:** Public
**Review:** at least every six months, and on material change in tools or regulation

This annex extends the [ENTITY] Artificial Intelligence Acceptable Use Policy (Saudi
Arabia) for large entities. The policy governs how individuals use AI; this annex
governs how the entity manages AI as a portfolio - oversight, classification, inventory,
lifecycle, sharing, assurance, and the annual compliance assessment. Where this annex
and the policy overlap, the stricter requirement applies.

**This annex covers government data.** It does not govern an organisation's processing
of its own commercial personal data where no government data is involved - policy
Section 1.1 and A13.

---

## A1. Governance structure and accountability

A1.1 [ENTITY] maintains a Data Governance Committee whose remit includes AI: approving
this annex and the Acceptable Use Policy, approving Level 3 and Level 4 uses, approving
exceptions, reviewing incidents and metrics, owning the compliance readiness position
in A11, and monitoring regulatory change. Membership includes the Chief Data Officer,
the Personal Data Protection Officer, the Compliance Officer, Business Data Executives,
IT, security and legal. It meets at least quarterly.

A1.2 **AI governance is assigned to the existing role structure rather than to a new
one.** The standards require [ENTITY] to identify and appoint, with responsibilities set
out in job descriptions aligned to the published organisational manual: a Chief Data
Officer, a Compliance Officer, a Personal Data Protection Officer, Business Data
Executives, Business Data Stewards, and IT Data Stewards. Every AI responsibility in
this annex attaches to one of them.

A1.3 A named senior executive is accountable for AI governance across [ENTITY] and
reports on it, including compliance readiness, to [the entity's governing body] at least
[twice yearly].

A1.4 **The organisational manual defining those role responsibilities is published by
the national data management authority and is not held by [ENTITY]** in the form used to
write this annex. Where it defines a responsibility differently from this annex, it
governs. A11.5 makes obtaining it a standing action.

A1.5 Responsibility follows three lines: business functions own the risks of the AI
they use; the Compliance Officer and the Personal Data Protection Officer set standards
and challenge; internal audit provides independent assurance (A10).

## A2. AI system inventory

A2.1 Every AI system used or deployed by [ENTITY] - bought, built, or embedded in other
software - must be recorded in the AI system inventory before use. The record states:
business owner and Business Data Executive; purpose; **the highest classification level
the system is approved for, and the Restricted sub-category where applicable**; whether
it processes personal data; the role [ENTITY] holds for that processing; the categories
of personal data; **the data sharing agreement reference where government data leaves
[ENTITY]**; supplier, sub-processors and underlying model where known; **actual
processing and storage locations**; the point of human determination; the retention and
destruction position; **whether the system can identify whose personal data a given
exposure touched**; the dates of the three assessments at policy Section 11; and the
next review date.

A2.2 An AI system not in the inventory is treated as an unapproved tool under policy
Section 3.

A2.3 The inventory is reviewed [quarterly]. Material changes - model, supplier,
processing location, retention behaviour, purpose, or the classification of data the
system handles - reopen its approval.

A2.4 **The inventory is an information asset and is itself classified, catalogued and
maintained** in [ENTITY]'s data catalogue like any other artefact, with metadata
sufficient for the Compliance Officer to use it in the annual assessment.

## A3. Classification governance for AI

**This section exists because classification is the gate through which every AI use
passes, and because AI is unusually good at silently creating integrated datasets.**

A3.1 Every AI system in the inventory carries an approved maximum classification level,
set by the Business Data Steward for the domain and recorded by the business owner.

A3.2 **A corpus, index, retrieval store or fine-tuning dataset assembled from multiple
sources is an integrated dataset and takes the highest classification present.** Before
any such collection is built, its intended composition is stated and its resulting
classification determined **in advance**. The committee treats a store whose
classification was determined after assembly as a finding.

A3.3 The classification of an AI system's output store is determined at the same time as
its input, and is at least that of the input.

A3.4 Where an AI use would require data above the system's approved level, the answer is
a different system or a different dataset. **It is never a reclassification made for
convenience**, and any reclassification is a fresh impact assessment recorded by the
Business Data Steward with reasons.

A3.5 Handling and protection controls are assigned to AI datasets and artefacts by
classification. **The specifications for those controls are the mandate of the national
cybersecurity authority and are not stated in this annex** - policy 13.1. The committee
records which of that authority's requirements each AI system has been assessed against,
and by whom.

A3.6 Secret data in an internal AI system requires the written approval of the Chief
Data Officer and the security function, recorded in the inventory with an expiry date.
Top Secret data is outside the scheme entirely and no approval route exists.

## A4. Personal data governance

A4.1 The initial personal data protection assessment is maintained as a live document,
not a one-off. **Every AI system approved for personal data updates its four minimum
elements**: the types of personal data collected, the location and method of storage,
the current processing and uses, and the compliance challenges.

A4.2 The personal data protection plan carries AI readiness items in its roadmap, with
milestones and assigned resources, rather than holding them in a separate AI programme.

A4.3 **The yearly risk assessment of information systems containing personal data covers
AI systems by its own terms** - it reaches collection, processing, storage and
transmission "whether automated or manual". The committee confirms annually that every
AI system in the inventory that handles personal data appears in that assessment, and
treats an omission as a finding rather than an oversight.

A4.4 Findings from that assessment are documented, analysed for impact and likelihood,
and evaluated against current obligations and criticality to resolve. **A finding is not
closed until the measure is implemented and the implementation is dated** (policy 11.4).
The committee reviews open findings at every meeting.

A4.5 The internal privacy audit reports to the Personal Data Protection Officer. Where
non-compliance is found, corrective action is taken with notification to the regulatory
authority and the national data management authority, and documented in the audit
findings report. **The committee is told when such a notification is made**, on the day
it is made.

A4.6 The compliance register is maintained for not less than 24 months and records any
collection or processing of personal data, AI processing included. A5.4 governs how AI
entries reach it.

## A5. Individuals' rights operations

A5.1 [ENTITY] maintains a documented route by which a request is executed against every
AI system in the inventory, covering all seven rights: to be informed, of access, to
rectification, to erasure, to object, to restrict processing, and to data portability.

A5.2 The route reaches prompts, uploads, transcripts, embeddings, caches, indexes,
inferred attributes and logs. **A system that cannot satisfy all seven is not approved
for personal data** - and the two that fail most often are the right to restrict
processing and the right to object, because both require the system to keep data while
ceasing to use it. The inventory records how each system does that.

A5.3 Requests are submitted, responded to and **tracked**. The tracking record is
auditable and is within the scope of A4.5.

A5.4 Every AI processing of personal data produces a register entry recording what data,
for what purpose, through which tool, under what sharing agreement, and who authorised
it. Entries are generated by the system where possible and by the business owner where
not; a system that cannot generate them places an operational burden that is recorded at
approval, not discovered afterwards.

A5.5 **A model fine-tuned on personal data may retain it.** Before any such model is
deployed, [ENTITY] records how erasure, rectification and restriction would be given
effect against it, and where that is not possible, does not fine-tune on that data.

## A6. Sharing government data with AI suppliers

A6.1 No AI service receives government data without a **data sharing agreement** meeting
policy Section 9.2. Procurement does not treat a supplier's standard terms as
satisfying it; the agreement is assessed clause by clause against that list and the gaps
are closed or the supplier is declined.

A6.2 The committee maintains a register of AI sharing agreements recording, for each:
the legal basis and purpose; the classification levels shared; the pre-processing
applied or the reason none was; retention and the destruction mechanism; the use
restrictions imposed, including territorial limits; audit rights; the third parties
deriving benefit; duration, frequency and termination measures; and liability.

A6.3 **Four clauses are treated as non-negotiable for AI suppliers:**

- **no use of [ENTITY] data to train or improve the supplier's models** - this is use
  beyond the specified purpose;
- **disclosure of actual processing and storage locations**, and of any change, with
  notice sufficient to reassess before it takes effect;
- **identification of every third party deriving benefit**, including sub-processors,
  the model provider behind a reseller, and analytics partners;
- **a specified destruction mechanism** covering prompts, logs, embeddings, caches and
  backups, evidenced on exit.

A6.4 **Pre-processing is considered before every sharing.** Where masking, anonymisation
or aggregation would serve the purpose without affecting content, the data is shared in
that form; where it would not, the reason is recorded in the register at A6.2.

A6.5 Authorisation to access shared data is granted on need to know and least privilege,
with identification and verification of authorised personnel appropriate to the data's
nature, classification and sensitivity.

A6.6 **[ENTITY] remains accountable for government data it shares.** Collective
accountability among the sharing parties allocates roles; it does not transfer
[ENTITY]'s own responsibility, and the committee does not accept a supplier commitment
as a substitute for a control [ENTITY] can evidence.

A6.7 Third-party supplier security obligations are reflected in every AI engagement in
accordance with the national cybersecurity authority's requirements, which this annex
does not reproduce.

A6.8 Critical AI suppliers are reassessed at least annually. For any AI service the
entity critically depends on, an exit plan exists that discharges the destruction
mechanism at A6.3, and concentration risk is reviewed by the committee.

## A7. Lifecycle controls for systems the entity builds or adapts

A7.1 Before deployment: documented purpose and success criteria; the classification
determination under A3; the personal data assessment where applicable; testing for
accuracy, robustness and disparate outcome proportionate to the level; and sign-off by
the Business Data Executive and, where personal data is involved, the Personal Data
Protection Officer.

A7.2 In change: modifications with a material effect on behaviour - model, prompt,
configuration, or training data changes - go through change management and re-testing
proportionate to the change, **and a re-assessment of whether the notice given to
individuals still describes what the system does** and whether the classification still
holds.

A7.3 In operation: deployed systems are monitored for degraded performance, drift and
misuse; agreed thresholds trigger review by the business owner.

A7.4 At retirement: a decommissioning step covering disposal across every store
identified at A2.1, the destruction mechanism in the sharing agreement, dependent
processes, and closure of the inventory record - while preserving the register entries
for their 24-month minimum. **Disposal is evidenced, not asserted.**

A7.5 Training data provenance is documented for any system [ENTITY] builds or tunes:
what data was used, its classification, what personal data it contained, what notice
covered it, and what was done about accuracy and disparate outcome.

## A8. Agentic AI

A8.1 AI agents operate under their own credentials with least-privilege access. A
person's own credentials must never be given to an agent.

A8.2 **An agent's credentials carry a maximum classification level**, recorded in the
inventory, and the agent must not be able to reach data above it. An agent that can
select its own tools or data sources is assessed for whether it can reach such data at
all.

A8.3 Consequential actions - making payments, sending external communications, changing
records about people, deploying code, publishing, or deleting data - require a human
checkpoint before execution unless the committee has expressly approved autonomous
operation for that action and system.

A8.4 An agent must not disclose government data to any destination not covered by a
sharing agreement, must not process personal data outside the recorded purpose, and must
not delete data subject to a live request, an open incident, or a retention minimum.

A8.5 **An agent assembling context from multiple sources creates an integrated dataset
at run time.** A3.2 applies, and the agent's reachable data set is classified in advance
at its highest level.

A8.6 Agent activity is logged and attributable to a named human owner; sessions are
bounded in scope and duration; every agent has a documented means of immediate
suspension.

A8.7 Content an agent ingests from outside [ENTITY] is treated as untrusted input,
including instructions embedded in that content.

## A9. Breach operations

A9.1 The incident process records **awareness as a timestamp, by a named person, at the
moment it occurs**, and escalates to the Personal Data Protection Officer immediately
where personal data may be involved.

A9.2 Where it is determined that personal data has been compromised, notification to the
regulatory authority is made **within 72 hours**. The process holds pre-drafted
notification content so that drafting time does not consume the period.

A9.3 The breach management process sets out functions and responsibilities for the
affected team and covers the incident review with the regulatory authority, the
immediate response, **implementation of permanent corrective actions when issued by the
authority, and testing of those actions to validate the solution**.

A9.4 **The committee does not close an incident until the corrective-action test result
is recorded.** This is the step most often skipped, and A10.2 tracks it as a metric.

A9.5 The process identifies, at the outset of every incident, whose personal data is
affected, and escalates immediately where the system cannot answer (policy 14.5).
Inability to enumerate is an open finding against that system.

A9.6 An incident involving data classified above Public is escalated to the Chief Data
Officer the same day whether or not personal data is involved, and Secret or Top Secret
involvement is treated as a security incident under the cybersecurity authority's
requirements in parallel.

A9.7 Supplier agreements require immediate notification on the supplier becoming aware.
The committee reviews, after every incident, whether any supplier term constrained
[ENTITY]'s ability to meet 72 hours.

## A10. Assurance and metrics

A10.1 Internal audit reviews the AI governance programme at least [annually], including
a sample test that inventory classifications match what the systems actually handle, a
sample test that register entries exist for AI processing of personal data, and a
walkthrough of the breach process against a simulated incident.

A10.2 The committee tracks agreed indicators, including:

- approved-tool adoption, and unapproved-tool discoveries;
- **AI systems handling data above their approved classification level, which should be
  zero**;
- **integrated stores whose classification was determined after assembly, which should
  be zero**;
- **AI systems processing personal data with no register entry, which should be zero**;
- **AI systems that cannot satisfy all seven rights, which should be zero**;
- **systems that cannot enumerate affected individuals, which should be zero**;
- risk-assessment findings with measures identified but not implemented;
- AI sharing agreements missing any of the four clauses at A6.3;
- time from occurrence to awareness, and from awareness to regulatory notification;
- **incidents closed without a recorded corrective-action test result, which should be
  zero**;
- exception count and age;
- training completion, reported separately for the classification module.

A10.3 The committee conducts a management review of the whole programme at least
[annually]: policy and annex, inventory, sharing agreement register, risk-assessment
findings, metrics, incidents, supplier performance, and regulatory change, with
documented actions.

## A11. The annual compliance assessment

**This section exists because [ENTITY]'s compliance is scored, submitted, consolidated
and published - and because the scoring is unforgiving.**

A11.1 [ENTITY] conducts a compliance audit annually and submits the report to the
national data management authority **during the third quarter of each year**. The
exercise is led by the Chief Data Officer, supported by the other data management and
personal data protection roles.

A11.2 **Assessment is at the level of each specification and is binary: 100% where the
specification is fully implemented, 0% where it is partially or not implemented.** There
is no partial credit. Scores cascade to control, domain and overall entity level, and
the report must be supported with evidence of implementation for each specification
where applicable.

A11.3 **Results are consolidated and published to related stakeholders at entity, sector
and whole-of-government level.** [ENTITY]'s score is not a private matter, and the
committee treats it accordingly.

A11.4 The authority may conduct ad-hoc compliance audits on selected entities to review
and validate findings, based on the outcomes of submitted reports. **Evidence is
therefore held in a producible form throughout the year, not assembled in the third
quarter.**

A11.5 Two documents the standards direct [ENTITY] to are **not held**: the personal data
protection regulations they repeatedly refer to for detailed requirements, and the
organisational manual defining the data role responsibilities. **The committee treats
obtaining both as a standing action**, because specifications assessed against a
document [ENTITY] has not read cannot reliably be scored 100%.

A11.6 **The specifications are fully phased in.** The three-year implementation roadmap -
priority 1 in year one, priority 2 in year two, priority 3 in year three - has run its
course from the release of the standards. Nothing in them is deferred, and no AI
approval may rest on a specification not yet being due.

A11.7 The committee maintains a mapping from each AI control in this annex to the
specifications it supports, so that AI work is visible as compliance work rather than
competing with it.

## A12. Exceptions

A12.1 Departures from the policy or this annex require a written exception approved by
the annex owner, with the risk accepted in writing by a named senior owner. Exceptions
are time-bound (maximum [6 months]), carry compensating controls, and are recorded in an
exceptions register with expiry dates. The committee reviews the register at every
meeting; expired exceptions lapse automatically.

A12.2 **No exception may be granted against**: placing Top Secret data in an AI tool;
placing Secret data in an external AI tool; combining datasets without reclassifying at
the highest level present; or bypassing a control in this policy.

A12.3 An exception may not be granted to omit a required assessment, a register entry,
or a sharing agreement. Those are conditions of the processing being permissible at all,
not controls whose risk can be accepted.

A12.4 **Every exception is disclosed in the annual compliance report** where it bears on
a specification, because a specification supported by an active exception is not fully
implemented and scores zero.

## A13. What this annex does not assert

A13.1 This annex, like the policy, rests on the national data management, classification
and data sharing instruments. **It governs government data.**

A13.2 It does not state, and does not assert:

- **any data security specification** - that is the mandate of the national
  cybersecurity authority, and even within the standards one classification
  specification is expressly left to it;
- the detailed personal data requirements the standards direct the reader to - notice
  and consent, individuals' rights, breach requirements, the register, and the personal
  data protection plan;
- the lawful bases for processing personal data, or the definition of personal or
  sensitive personal data;
- the conditions for transferring personal data outside the Kingdom;
- any penalty for contravention;
- the responsibilities the published organisational manual assigns to the data roles;
- **any obligation applicable to an organisation processing only its own commercial
  personal data**, with no government data involved.

A13.3 The accompanying research note lists every point at which the held instruments
refer to a document [ENTITY] does not hold.

---

*This document is an educational policy template and does not constitute legal advice.
It reflects obligations under the national data management, classification and data
sharing instruments as set out in the accompanying research note, applies to government
data only, and must be reviewed by the Personal Data Protection Officer or qualified
legal counsel before adoption.*
