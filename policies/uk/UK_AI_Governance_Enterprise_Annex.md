# AI Governance - Enterprise Annex

**Organisation:** [ORGANISATION]
**Effective date:** [DATE]  **Version:** 1.0
**Annex owner:** [CISO / Head of AI Governance]  **Data protection lead:** [DPO / privacy lead]
**Classification:** Internal
**Review:** at least every six months, and on material change in tools or regulation

This annex extends the [ORGANISATION] Artificial Intelligence Acceptable Use
Policy for large organisations. The policy governs how individuals use AI;
this annex governs how the organisation manages AI as a portfolio - oversight,
inventory, lifecycle, suppliers, and assurance. Where this annex and the policy
overlap, the stricter requirement applies.

---

## A1. Governance structure and accountability

A1.1 [ORGANISATION] maintains an AI Governance Committee with a defined remit:
approving this annex and the Acceptable Use Policy, approving Level 3 uses,
approving exceptions, reviewing incidents and metrics, and monitoring
regulatory change. Membership includes [security, data protection, legal, risk,
HR, and business representation]. The committee meets at least quarterly.

A1.2 A named senior executive is accountable for AI governance across the
organisation and reports on it to the board at least [twice yearly].

A1.3 Responsibility follows three lines: business functions own the risks of
the AI they use; risk and compliance functions set standards and challenge;
internal audit provides independent assurance (Section A7).

## A2. AI system inventory

A2.1 Every AI system used or deployed by [ORGANISATION] - bought, built, or
embedded in other software - must be recorded in the AI system inventory
before use. The record states: business owner; purpose; risk level (policy
Section 4); data categories processed; lawful basis where personal data is
involved; supplier and underlying model where known; the point of human
oversight; and the next review date.

A2.2 An AI system not in the inventory is treated as an unapproved tool under
policy Section 3. The inventory is reviewed [quarterly] and material changes
to a recorded system reopen its approval.

## A3. Lifecycle controls for systems the organisation builds or adapts

A3.1 Before deployment: documented purpose and success criteria; testing for
accuracy, robustness, security, and bias (policy Section 14) proportionate to
the risk level; and sign-off by the business owner and, where personal data is
involved, the data protection lead.

A3.2 In change: modifications with a material effect on behaviour - model,
prompt, configuration, or training data changes - go through change management
and re-testing proportionate to the change.

A3.3 In operation: deployed systems are monitored for degraded performance,
drift, and misuse; agreed thresholds trigger review by the business owner.

A3.4 At retirement: a decommissioning step covering data disposal, dependent
processes, and closure of the inventory record.

## A4. Suppliers and supply chain

A4.1 No AI service is procured or renewed without the security and data
protection review in policy Section 3, and contract terms covering: no use of
[ORGANISATION] data to train the supplier's models without express approval;
breach notification; transparency over sub-processors and material model
changes; and audit and exit rights.

A4.2 Critical AI suppliers are reassessed at least annually. For any AI
service the business critically depends on, an exit plan exists and
concentration risk is reviewed by the committee.

## A5. Exceptions

A5.1 Departures from the policy or this annex require a written exception
approved by the annex owner, with the risk accepted in writing by a named
senior owner. Exceptions are time-bound (maximum [6 months]), carry
compensating controls, and are recorded in an exceptions register with their
expiry dates. The committee reviews the register at every meeting; expired
exceptions lapse automatically.

## A6. Agentic AI

A6.1 AI agents - systems that plan and take actions with limited human
prompting - operate under their own credentials with least-privilege access.
A person's own credentials must never be given to an agent.

A6.2 Consequential actions - making payments, sending external
communications, changing records about people, deploying code, or deleting
data - require a human checkpoint before execution unless the committee has
expressly approved autonomous operation for that action and system.

A6.3 Agent activity is logged and attributable to a named human owner. Agent
sessions are bounded in scope and duration, and every agent has a documented
means of immediate suspension.

A6.4 Content an agent ingests from outside the organisation is treated as
untrusted input (policy Section 10.3), including instructions embedded in
that content.

## A7. Assurance and metrics

A7.1 The committee tracks agreed indicators, including: approved-tool
adoption; unapproved-tool discoveries; verification records for
decision-bearing output; incidents and near misses; exception count and age;
and impact-assessment coverage for Level 3 uses.

A7.2 Internal audit reviews the AI governance programme at least [annually].

A7.3 The committee conducts a management review of the whole programme at
least [annually]: policy and annex, inventory, metrics, incidents, supplier
performance, and regulatory change, with documented actions.

## A8. Complaints and speak-up

A8.1 Individuals can complain to [ORGANISATION] about the handling of their
personal data, including by AI systems. [ORGANISATION] provides an accessible
means of complaint, acknowledges receipt within 30 days, takes appropriate
steps to respond, and informs the complainant of the outcome without undue
delay. [DPO / privacy lead] owns this process.

A8.2 Staff can raise concerns about AI use - bias, safety, misuse, or
pressure to bypass controls - outside their line management and without
detriment, through [speak-up channel].

## A9. Sector overlay [regulated firms]

A9.1 Where [ORGANISATION] is regulated, the committee maps this annex to the
sector's requirements - for example, in financial services: consumer
outcomes, operational resilience, outsourcing and third-party expectations,
and individual accountability regimes - and records the mapping in the
inventory and risk register.

---

*This document is an educational policy template and does not constitute
legal advice. It reflects obligations under the UK data protection regime as
amended, verified against the revised legislation texts; it must be reviewed
by the data protection lead or legal counsel before adoption.*
