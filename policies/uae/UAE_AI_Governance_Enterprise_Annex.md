# AI Governance - Enterprise Annex - United Arab Emirates

### DIFC-registered entities, with routing for ADGM and the federal regime

**Organisation:** [ORGANISATION]
**Effective date:** [DATE]  **Version:** 1.0
**Annex owner:** [CISO / Head of AI Governance]  **Data protection lead:** [Data Protection Officer]
**Automated Systems Officer:** [ASO]
**Classification:** Internal
**Review:** at least every six months, and on material change in tools or regulation

This annex extends the [ORGANISATION] Artificial Intelligence Acceptable Use Policy
(United Arab Emirates) for large organisations. The policy governs how individuals use
AI; this annex governs how the organisation manages AI as a portfolio - oversight,
determination, inventory, certification readiness, lifecycle, suppliers, and assurance.
Where this annex and the policy overlap, the stricter requirement applies.

---

## A1. Governance structure and accountability

A1.1 [ORGANISATION] maintains an AI Governance Committee with a defined remit: approving
this annex and the Acceptable Use Policy, approving Level 3 and Level 4 uses, approving
exceptions, reviewing incidents and metrics, owning the certification readiness position
at A4 and the ASO succession position at A5, and monitoring regulatory change.
Membership includes the data protection lead, the ASO, security, legal, risk and business
representation. It meets at least quarterly.

A1.2 A named senior executive is accountable for AI governance across [ORGANISATION] and
reports to the board at least [twice yearly], including certification readiness.

A1.3 **The committee is not a substitute for either statutory role.** The Data Protection
Officer's independence is preserved, and the ASO's independence in reviewing audit
documentation (policy 12.5) is not qualified by committee membership.

A1.4 Responsibility follows three lines: business functions own the risks of the AI they
use; data protection, the ASO and risk set standards and challenge; internal audit
provides independent assurance (A10).

## A2. The three determinations

**Every AI tool passes through three determinations before approval, in this order. They
are distinct and each is recorded separately.**

A2.1 **Is it a System?** Does it operate in an autonomous or semi-autonomous manner,
process personal data for human-defined or self-defined purposes, and generate output on
that basis - or is it deterministic software outside the definition? Made by the data
protection lead with the ASO (policy 4.4).

A2.2 **Which role does [ORGANISATION] hold?** Provider, Operator, Deployer - or more than
one - and separately Controller or Processor. **The Deployer test is satisfied by
receiving the benefit of the System's output**, so the default answer for a bought-in
tool is Deployer, and the committee treats "we only use the vendor's product" as an
answer that confirms the role rather than avoiding it.

A2.3 **Is the processing High Risk Processing Activities?** Determined in writing by the
data protection lead against the definition in the underlying law and regulations, with
reasoning recorded. **Where uncertain, [ORGANISATION] proceeds as though it is** (policy
5.7) and the committee considers prior consultation with the Commissioner.

A2.4 Each determination carries a date, a named decision-maker, and the basis. **A
determination is not a permanent fact about a tool.** A2.6 governs when they reopen.

A2.5 **The three determinations compound.** A tool that is a System, deployed by
[ORGANISATION], for High Risk Processing engages the certification gate. Any one of the
three answering the other way takes it outside that gate but not outside this policy.

A2.6 All three reopen on: a vendor enabling agentic, retrieval, memory or planning
capability; a change of model; a change of purpose; [ORGANISATION] fine-tuning,
rebranding or embedding the System in something it offers; or a material change in the
data processed. **A tool can become a System without being replaced**, and the committee
treats vendor release notes as a governance input, not a product update.

## A3. AI system inventory

A3.1 Every AI tool used or deployed by [ORGANISATION] - bought, built, or embedded in
other software - is recorded before use. The record states: business owner; purpose;
**the three determinations at A2 with their dates and decision-makers**; the categories of
personal data processed and the lawful basis; supplier, sub-processors and underlying
model; **actual processing and storage locations and the transfer basis**; **the
human-defined purposes, principles and limits under policy 11.3**; whether processing
purpose logging is implemented and where the logs are held; the named ASO oversight
owner; certification status and expiry; **whether the System can identify whose personal
data a given exposure touched**; the retention position; and the next review date.

A3.2 A tool not in the inventory is treated as unapproved under policy Section 7.

A3.3 The inventory is reviewed [quarterly], and any A2.6 event reopens the record
immediately rather than at the next review.

A3.4 The inventory is the operational record of which regime governs each processing
(policy 3.4) and must not diverge from [ORGANISATION]'s wider processing record.

## A4. Certification readiness register

**This section exists because the certification framework's implementation timeline is at
the Commissioner's discretion, and because the evidence it requires cannot be produced
retrospectively.**

A4.1 [ORGANISATION] maintains a Certification Readiness Register for every System whose
processing is, or may be, High Risk. It records: the certification requirement each piece
of evidence supports; the named owner; the gap assessment; the remediation plan and
milestones; and the decision point at which the System will be withdrawn if it will not
be ready.

A4.2 The register carries a readiness line for each of: the overarching governance
document; the risk-based necessity assessment; the AI data protection impact assessment
with evidence of control integration; the risk register; the privacy notice including the
self-defined-purposes disclosure; the accountability and roles documentation; the bias
identification and mitigation evidence **including model modifications made**; the data
quality and dataset documentation; the security measures; the active monitoring and model
tuning procedures; the third-party due diligence and contracts; the robustness and
resilience measures; **the processing purpose logs and algorithmic audits**; the ASO
appointment; and the register of rights, bases, automated decision-making and processor
obligations.

A4.3 **A System may not be approved on the basis that certification is not yet being
enforced.** Approval states what evidence exists, what is missing, and who owns the gap.

A4.4 **Evidence is built during development, not assembled for an application.** The
impact assessment must show that controls were integrated into the development process
and provide evidence that they were - a requirement that cannot be met by a document
written afterwards. A4.2 items are therefore project deliverables with dates, not
compliance artefacts with deadlines.

A4.5 The committee records at each meeting the Commissioner's current position on
implementation, and the version of the Framework the organisation's position rests on.

A4.6 Where the High Risk determination is finely balanced, the committee considers **prior
consultation** with the Commissioner before deployment, and records the decision either
way.

## A5. The Automated Systems Officer

A5.1 [ORGANISATION] appoints an ASO for Systems used for High Risk Processing, with the
competencies, status, role and tasks described in policy Section 12.

A5.2 **The one-month rule is a hard operational constraint** (policy 12.3): no gap of more
than one month before the operation of such a System, or between an outgoing ASO and a
replacement, absent an approved exception.

A5.3 The committee therefore maintains, at all times: **a named deputy** recorded against
the ASO role; a documented succession process **triggered on the day notice is given**;
and a standing view of whether an exception application would be needed and on what
grounds.

A5.4 **An ASO vacancy exceeding one month is reported to the accountable executive at
A1.2 as a compliance failure, not a recruitment delay.** The committee tracks days
elapsed as a metric (A11.2).

A5.5 [ORGANISATION] provides support enabling the ASO to review and assess audit
documentation **independently**, and produces the gap analysis, risk register and
management action plan the ASO requires.

A5.6 Where one person holds both the ASO and Data Protection Officer roles, the committee
records why independence is not compromised and reviews the position annually.

A5.7 The ASO's oversight covers the ongoing validity of each System's certification, and
the committee is notified immediately where certification lapses, is revoked, or is
modified such that it is no longer valid - because policy 17.3 then bars any statement
that the System is certified.

## A6. Purposes, limits and the evidence of autonomy

**This section operationalises policy Section 11 and is the part of this annex with no
counterpart in an ordinary AI governance framework.**

A6.1 For every System, the inventory holds three artefacts before deployment: the
**human-defined purposes**; the **human-defined principles** to which any self-defined
purpose must conform; and **all human-defined limits** within which the System may define
further purposes.

A6.2 **These are approved by the committee, not drafted by the delivery team alone**, and
they are approved before the System runs. A set of principles derived after the fact from
observed behaviour does not satisfy policy 11.2.

A6.3 **Processing purpose logging is a functional requirement recorded in the inventory**
(A3.1). Where a System cannot log the purposes it actually processed for, the gap is
raised at approval and the System is not approved for High Risk Processing.

A6.4 [ORGANISATION] conducts **algorithmic audits** assessing the System's algorithms
against the human-defined processing purposes, and records the corrective actions taken.
Audits are conducted before deployment, on material change, and at least [annually].

A6.5 **Code review records must address the absence of self-defined purposes** where the
System is not intended to have any. A review that confirms the code implements the
intended purposes, without addressing whether it can generate others, is incomplete.

A6.6 The committee reviews, at each meeting, any System where the processing purpose logs
show processing for a purpose not in the approved set. **That is an incident, not a
finding**, and it enters the incident process at A9.

A6.7 Routine review under policy 11.6 covers the processing purposes, the output, **and
the manner in which the output is used**. The third limb requires the business to report
how output is actually consumed downstream, which the committee collects rather than
assumes.

## A7. Lifecycle controls

A7.1 Before deployment: the three determinations at A2; the risk-based necessity
assessment showing why a lower-risk System would not do; the AI data protection impact
assessment; the purposes, principles and limits at A6.1; bias testing; dataset
documentation; security assessment; and sign-off by the business owner, the data
protection lead and, for High Risk Systems, the ASO.

A7.2 In change: modifications with a material effect on behaviour go through change
management and re-testing, **and reopen the A2 determinations** and the notice at policy
10.2. Adding autonomy is the change that matters most and is the one least likely to be
flagged by the delivery team.

A7.3 In operation: **active monitoring of the use and quality of collected personal
data**, and review or regular model tuning where appropriate - on changes to customer
behaviour, commercial objectives, risks or corporate values. Agreed thresholds trigger
review by the business owner and the ASO.

A7.4 [ORGANISATION] maintains mechanisms for **giving and receiving updates to and from
processors and other third parties** about the quality and use of personal data collected
through the System.

A7.5 Datasets are **periodically reviewed and updated** for accuracy, quality, currency,
relevance and reliability, with statistical assessments verifying currency and validity.
The review interval is recorded per System.

A7.6 **Privacy-preserving methodologies** that reduce the personal data collected, stored
or processed are applied where available, and their use is documented as evidence.

A7.7 At retirement: disposal across every store in the inventory record, closure of the
certification position, notification to the certification body where required, and
retention of the evidence records under policy 20.3.

A7.8 Training data provenance is documented for any System [ORGANISATION] builds or
tunes: what personal data was used, on what basis, what notice covered it, the dataset's
size and relevance, and what was done about bias and data quality.

## A8. Suppliers and the supply chain

A8.1 No AI service is procured or renewed without **enhanced due diligence** and a written
contract. The due diligence documentation records the process by which the Provider's
System and its compliance were assessed.

A8.2 Contracts clearly delineate data protection roles and responsibilities, and cover
international transfers with cross-border safeguards where applicable.

A8.3 [ORGANISATION] obtains and reviews the Provider's **data protection by design
documentation** evidencing adherence to data protection principles. **A supplier that
cannot produce it is not approved for a System used in High Risk Processing.**

A8.4 The contract requires processors and other third parties related to the System's
function to implement **substantially similar measures** to those [ORGANISATION] applies,
and requires flow-down to sub-processors.

A8.5 **Roles and responsibilities regarding transparency and other compliance obligations
in the supply chain must be clear** (policy 10.7). Where a supplier will not state who is
responsible for what, the arrangement is not approved - ambiguity here defeats the
accountability requirement directly.

A8.6 Additional AI-specific terms: no use of [ORGANISATION] data to train the supplier's
models without express approval; **disclosure of material model and capability changes**,
because those may reopen the A2 determinations; disclosure of actual processing and
storage locations and any change; immediate breach notification; assistance with
individuals' requests; and exit arrangements.

A8.7 Where [ORGANISATION] is an Operator or Provider to another organisation, the annex
owner maintains the list of such engagements and the obligations [ORGANISATION] has
accepted in each.

A8.8 Critical AI suppliers are reassessed at least annually, with an exit plan and a
concentration risk review by the committee.

## A9. Incidents and breach

A9.1 The incident process records **awareness as a timestamp, by a named person, at the
moment it occurs.** Which clock then runs depends on the regime determined under policy
Section 3, and the incident record states which regime was applied and why.

A9.2 **For DIFC processing, the standard is "as soon as practicable in the
circumstances", with no fixed period.** [ORGANISATION] sets an internal target and, more
importantly, **maintains the evidence that would show the standard was met** - what was
known when, what was done, and why any interval was necessary. An open-ended standard is
audited on reasoning, so the reasoning is contemporaneous.

A9.3 **The committee does not permit a 72-hour figure to be used as the DIFC target by
default.** Doing so imports another zone's rule, and the incident record must name the
regime and the source of any period applied.

A9.4 Where [ORGANISATION] processes personal data outside its zone, the incident process
identifies which processing is affected and applies the correct clock to each - policy
3.4.

A9.5 The process identifies, at the outset of every incident, whose personal data is
affected, and escalates immediately where the System cannot answer (policy 14.6).
Inability to enumerate is an open finding against that System.

A9.6 **Processing for an unapproved purpose is an incident** (A6.6) whether or not
personal data left the organisation, and is investigated as one.

A9.7 Supplier contracts require immediate notification. The committee reviews, after
every incident, whether any supplier term constrained [ORGANISATION]'s ability to meet
its obligation.

## A10. Assurance

A10.1 Internal audit reviews the AI governance programme at least [annually], including:
a sample test that the A2 determinations match what systems actually do; a sample test
that processing purpose logs exist and are reviewed; verification that the ASO succession
position at A5.3 is current; and a walkthrough of the incident process against a
simulated breach in each regime [ORGANISATION] is subject to.

A10.2 **Audit tests the determinations hardest**, because a wrong System or High Risk
determination silently removes a whole tier of obligation and nothing downstream will
detect it.

A10.3 The committee conducts a management review of the whole programme at least
[annually]: policy and annex, inventory, readiness register, purposes and limits
artefacts, metrics, incidents, supplier performance and regulatory change, with
documented actions.

## A11. Metrics

A11.1 The committee tracks agreed indicators, including:

- approved-tool adoption, and unapproved-tool discoveries;
- **tools in use with no recorded A2 determination, which should be zero**;
- **Systems used for High Risk Processing with no recorded purposes, principles and
  limits, which should be zero**;
- **Systems used for High Risk Processing without processing purpose logging, which
  should be zero**;
- **days of ASO vacancy against the one-month limit** (A5.4);
- Systems with an algorithmic audit older than the agreed interval;
- bias findings raised, and **model modifications actually made in response**, reported
  as a pair;
- readiness register items with no named owner or no dated plan;
- **incidents where the regime applied was later found to be wrong, which should be
  zero**;
- time from occurrence to awareness, and from awareness to notification;
- Systems that cannot enumerate affected individuals;
- exception count and age;
- training completion, reported separately for the regime-routing module.

A11.2 The bias pair at A11.1 is reported as a pair deliberately. **A rising count of
findings with a flat count of modifications is the signal that testing has become
performative**, and the committee treats it as such.

## A12. Exceptions

A12.1 Departures from the policy or this annex require a written exception approved by
the annex owner, with the risk accepted in writing by a named senior owner. Exceptions
are time-bound (maximum [6 months]), carry compensating controls, and are recorded with
expiry dates. The committee reviews the register at every meeting; expired exceptions
lapse automatically.

A12.2 **No exception may be granted against**: deploying a System for High Risk
Processing without the certification gate or a current ASO; deploying a System whose
limits on self-defined purposes cannot be stated; representing a System as certified when
it is not; or disabling processing purpose logging, algorithmic audit records or other
required evidence.

A12.3 **An exception cannot substitute for the Commissioner's exception.** Where the
regime itself provides for an exception - such as the ASO gap rule - only the
Commissioner may grant it, and [ORGANISATION]'s internal register records the application
and its outcome, not a self-granted equivalent.

## A13. What this annex does not assert

A13.1 This annex rests principally on the **DIFC Regulation 10 Accreditation and
Certification Framework**, which [ORGANISATION] holds in full. **It does not hold
Regulation 10 itself, nor a current consolidation of the DIFC data protection law.**

A13.2 It therefore does not state: the definition of High Risk Processing Activities; the
content of the regulation and law provisions the Framework cites rather than quotes; or
any penalty for contravention.

A13.3 It states the ADGM and federal **breach positions only**, because those have been
verified against the official texts and because misapplying them is the most consequential
error available here. **It says nothing else about either regime**, and an ADGM or
federal-regime entity needs its own document.

A13.4 It does not state the financial services regulators' requirements in either free
zone. Both zones exist to host financial institutions, so for a regulated firm **those
rules may bite harder than the data protection regime does**, and they require their own
document grounded in their own instruments.

A13.5 **The issuing authority's own notice on the Framework states that its content is
provided for informational purposes and should not be considered complete, up to date, or
a substitute for specific professional advice.** The committee treats that as a standing
reason to verify the current position before any decision of consequence, and A4.5
records the version relied on.

---

**Version history:**
1.0 - initial annex, published 2 September 2026; verified within its stated
scope (DIFC-registered entities; evidence tiers stated in the research note
and source register).

---

*This document is an educational policy template and does not constitute legal advice.
It is written for a DIFC-registered entity, reflects obligations as set out in the
accompanying research note, and must be reviewed by the data protection lead or qualified
legal counsel before adoption.*
