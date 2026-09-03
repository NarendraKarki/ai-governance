# AI Governance - Enterprise Annex - United States

### Federal sectoral baseline + California + Colorado

**Organisation:** [ORGANISATION]
**Effective date:** [DATE]  **Version:** 1.0
**Annex owner:** [CISO / Head of AI Governance]  **Privacy lead:** [Chief Privacy Officer]
**Classification:** Internal
**Review:** at least every six months, and on material change in tools or regulation

This annex extends the [ORGANISATION] Artificial Intelligence Acceptable Use Policy
(United States) for large organisations. The policy governs how individuals use AI;
this annex governs how the organisation manages AI as a portfolio - oversight, the
two determinations, inventory, assessments, suppliers, monitoring, and assurance.
Where this annex and the policy overlap, the stricter requirement applies.

---

## A1. Governance structure and accountability

A1.1 [ORGANISATION] maintains an AI Governance Committee with a defined remit:
approving this annex and the Acceptable Use Policy, approving Level 3 and Level 4
uses, approving exceptions, reviewing incidents and metrics, owning the assessment
register at A4 and the framework-compliance position at A5, and monitoring
regulatory change across the states [ORGANISATION] reaches. Membership includes
[security, privacy, legal, risk, HR, and business representation]. It meets at least
quarterly.

A1.2 A named senior executive is accountable for AI governance across the
organisation and reports to the board at least [twice yearly], including the
framework-compliance position - because in Colorado that position is the statutory
safe harbour, not a slide.

A1.3 Responsibility follows three lines: business functions own the risks of the AI
they use; privacy, risk and compliance set standards and challenge; internal audit
provides independent assurance (A10).

## A2. The two determinations

A2.1 Every AI tool that touches decisions about people carries both determinations
(policy clause 4), recorded separately, each with a date, a named decision-maker,
and the basis:

- **Colorado:** high-risk AI system or not - the substantial-factor test against the
  eight consequential-decision areas, and the exclusions read honestly.
- **California:** ADMT for a significant decision or not - the
  substantially-replaces-human-decisionmaking test against the five
  significant-decision areas.

A2.2 **The determinations compound differently.** A tool inside both regimes carries
the union of duties; inside one, that regime's duties; inside neither, this policy
still governs it. The committee treats "outside both" as a conclusion requiring the
same evidence as "inside".

A2.3 Both determinations reopen on: a vendor enabling agentic, retrieval, memory, or
planning capability; a change of model or purpose; a material change in the data; or
a weakening of the human review around the tool - the change most likely to go
unflagged, because nothing in the software changes when a reviewer stops genuinely
reviewing.

A2.4 **The chatbot exclusion is a standing condition, not a one-time gate.** Any
natural-language system relied on as excluded from the Colorado regime is listed,
and the enforcement of this policy's content rules against it is evidenced at each
review - the exclusion holds only while the accepted use policy is real.

## A3. AI system inventory

A3.1 Every AI system used or deployed - bought, built, or embedded - is recorded
before use. The record states: business owner; purpose; **both A2 determinations
with dates and decision-makers**; the role held for Colorado purposes (developer,
deployer, or both); risk level; categories of personal information; the assessment
reference where one is required; supplier, sub-processors, and underlying model;
processing and storage locations; the retention position across prompts, logs,
embeddings, and caches; the point of human determination; the notice position (
pre-use, adverse-decision, interaction disclosure); and the next review date.

A3.2 A tool not in the inventory is unapproved under policy clause 5.

A3.3 The inventory is reviewed [quarterly]; any A2.3 event reopens the record
immediately.

## A4. Assessment register

A4.1 [ORGANISATION] maintains an Assessment Register recording, for every processing
that requires an assessment (policy 9.1): the system; the trigger; the date; who
conducted and approved it; risks identified; measures identified **and the date each
was implemented**; the review dates against the annual, ninety-day, and three-year
cadences; and the submission status to the California regulator.

A4.2 One assessment may serve both regimes where reasonably similar in scope and
effect; the register records which regime's content list governed and why it is the
stricter.

A4.3 An assessment must precede the processing. A record created after processing
began is remediation, labelled as such, and reported to the committee.

A4.4 A measure identified but not implemented is an open finding, not a completed
assessment.

A4.5 **Assessments are written to be read by a regulator.** California submissions
run on the prescribed schedule; Colorado's attorney general may demand the risk
program, assessments, and records on ninety days' notice. Trade-secret designation
and privilege positions are recorded at drafting time, not asserted for the first
time under a deadline.

## A5. The framework-compliance position

**This clause exists because Colorado's statute gives framework compliance legal
effect: a rebuttable presumption of reasonable care, and - with discovery and cure -
an affirmative defense.**

A5.1 [ORGANISATION] maintains a documented mapping of its AI risk management program
to the NIST AI Risk Management Framework's four functions - govern, map, measure,
manage - and records the framework version relied on.

A5.2 The program is reasonable considering [ORGANISATION]'s size and complexity, the
nature, scope, and intended uses of the systems deployed, and the sensitivity and
volume of data processed - the statute's own reasonableness factors, recorded per
review.

A5.3 The discovery-and-cure machinery is deliberate: feedback channels users are
encouraged to use; adversarial testing or red-teaming in the NIST sense; and the
internal review at A8. A violation discovered and cured through these channels,
while the program complies, is the affirmative defense operating as designed - the
committee records each such event.

A5.4 One program may cover multiple high-risk systems; the mapping states which.

## A6. Notices in operation

A6.1 The committee owns evidence that each required notice actually operates: the
Colorado pre-decision notice and adverse-decision statement with correction and
appeal; the California pre-use notice with opt-out and access methods; the AI
interaction disclosure with any obviousness determinations; and the public website
statement, with its update history.

A6.2 The adverse-decision statement machinery is tested before a Level 4 system goes
live: can [ORGANISATION] state, for a real decision, the principal reasons, the
degree and manner of the system's contribution, and the data types and sources? A
system for which that statement cannot be produced is not approved.

A6.3 Appeals receive human review where technically feasible, by a person not
involved in the original decision, recorded.

## A7. Suppliers

A7.1 No AI service is procured or renewed without a written contract meeting the
California service-provider requirements and the AI-specific terms at policy 13.2.

A7.2 For any bought-in high-risk system, the Colorado developer documentation -
model cards, dataset summaries, known limitations, discrimination testing, intended
and inappropriate uses - is obtained before deployment and retained; a developer
that will not provide it is not approved.

A7.3 Where [ORGANISATION] is itself a developer to others, the annex owner maintains
the engagement list, the documentation package, the public developer statement, and
the ninety-day notification duty to the attorney general and known deployers on
discovering algorithmic discrimination.

A7.4 Critical AI suppliers are reassessed at least annually, with an exit plan and a
concentration risk review.

## A8. Monitoring, discrimination, and the ninety-day clock

A8.1 Deployed high-risk systems are reviewed at least annually for algorithmic
discrimination; Level 4 systems are tested for disparate outcomes before deployment
and at least annually, with results recorded.

A8.2 Suspected algorithmic discrimination is escalated same-day to the privacy lead.
**Discovery starts the ninety-day statutory notice clock to the Colorado attorney
general**; the committee treats the internal escalation path as part of the clock,
not prelude to it.

A8.3 Bias findings and model modifications made in response are tracked as a pair.
A rising count of findings with a flat count of modifications is the signal that
testing has become performative.

A8.4 Where discrimination is found and cannot be cured, the system is withdrawn, and
the withdrawal is evidence under A5.3.

## A9. Incidents

A9.1 The incident process records awareness as a timestamp by a named person.
Because this set does not hold the state breach statutes, the process names, for
each incident, which notification obligations were assessed and by whom - the
privacy lead's current statement of obligations is the reference, and its absence
from this corpus is stated in the README, not discovered mid-incident.

A9.2 Processing outside a recorded determination - a tool used on consequential
decisions it was not assessed for - is an incident, whether or not personal
information left the organisation.

A9.3 Supplier contracts require notification without undue delay; after every
incident the committee reviews whether any supplier term constrained
[ORGANISATION]'s response.

## A10. Assurance

A10.1 Internal audit reviews the AI governance programme at least [annually],
including: a sample test that the A2 determinations match what systems actually do;
a sample test that assessments preceded the processing they cover; verification that
the framework mapping at A5.1 is current; and a walkthrough of the adverse-decision
statement machinery against a simulated decision.

A10.2 Audit tests the determinations hardest - a wrong answer on either test
silently removes a whole regime of obligation, and nothing downstream will detect
it.

A10.3 The committee conducts a management review at least [annually]: policy and
annex, inventory, assessment register, framework position, notices in operation,
metrics, incidents, supplier performance, and regulatory change - including new
state laws entering the scope [ORGANISATION] actually reaches.

## A11. Metrics

A11.1 The committee tracks agreed indicators, including:

- approved-tool adoption, and unapproved-tool discoveries;
- **tools touching decisions about people with no recorded determinations, which
  should be zero**;
- **Level 4 systems with no assessment, or with measures identified but not
  implemented, which should be zero**;
- assessments completed after processing began;
- adverse-decision statements that could not be produced on request;
- bias findings and model modifications, reported as a pair;
- days from suspicion of discrimination to escalation, against the ninety-day
  statutory clock;
- California submissions made on schedule;
- exception count and age;
- training completion, reported separately for the two-determinations module.

## A12. Exceptions

A12.1 Departures from the policy or this annex require a written exception approved
by the annex owner, with the risk accepted in writing by a named senior owner,
time-bound (maximum [6 months]), with compensating controls and expiry dates,
reviewed at every committee meeting.

A12.2 **No exception may be granted against:** deploying a Colorado high-risk system
without the risk program, assessment, and notices; weakening the accepted-use-policy
condition on which a chatbot exclusion rests; or a Level 4 decision without human
determination.

## A13. What this annex does not assert

A13.1 It asserts nothing about states other than California and Colorado, about the
state breach statutes, or about any federal AI statute - none is held.

A13.2 The sectoral regimes (health, credit, children's data, financial institutions)
are engaged at the points the policy cites and are otherwise governed by
[ORGANISATION]'s sector compliance programs, not this annex.

A13.3 Where the attorney general adopts rules under the Colorado Act, or the
California regulator issues further regulations, the committee records the version
relied on and reopens the affected clauses.

---

**Version history:**
1.0 - initial annex, published 3 September 2026; verified within its stated
scope (federal sectoral baseline + California + Colorado) per the research note
and source register.

---

*This document is an educational policy template and does not constitute legal
advice. It reflects obligations under the United States instruments set out in the
accompanying research note, applies only within the scope stated, and must be
reviewed by the privacy lead or qualified legal counsel before adoption.*
