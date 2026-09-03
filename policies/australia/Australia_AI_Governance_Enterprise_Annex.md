# AI Governance - Enterprise Annex - Australia

### Operating the six practices, the automated-decision determination and the privacy duties across the AI portfolio

**Organisation:** [ORGANISATION]
**Effective date:** [DATE]  **Version:** 1.0
**Owner:** [Accountable executive for AI]  **Privacy lead:** [Privacy Officer / privacy lead]
**Classification:** Internal
**Companion to:** Artificial Intelligence Acceptable Use Policy - Australia (policy clause references below are to that document)

---

## A1. Governance structure and accountability

A1.1 [ORGANISATION] is accountable for how and where AI is used. A senior leader,
[the accountable executive], owns AI governance across the organisation, with the
authority and the understanding of AI capabilities and risks to oversee all AI use.
This is the first of the six practices the government's adoption guidance asks for, and
[ORGANISATION] applies it as a house standard.

A1.2 The **AI Governance Committee** comprises the accountable executive (chair), the
data protection lead, the CISO, [Legal], [Risk] and the business owners of Level 3 and
Level 4 systems. It approves Level 4 uses, owns the policy and this annex, reviews the AI
register quarterly, receives the monitoring and incident reports at A9, and reviews
override rates on Level 4 decisions.

A1.3 The **data protection lead** approves Level 3 uses, owns privacy impact
assessments, holds the automated-decision determinations, drafts the privacy-policy
disclosure required from 10 December 2026, and is the contact for individuals'
complaints and requests concerning AI.

A1.4 Every AI system has a **named accountable person** who understands the technology
and its business implications, owns the system's register entry, risk assessment,
testing and monitoring, and is trained for the role.

A1.5 Where a system involves several parties (supplier, model developer, integrator,
[ORGANISATION]), the register records who is responsible for each part of the supply
chain, so that it is known who to go to when something goes wrong.

A1.6 The policy is the AI policy the adoption guidance asks for. This annex is the
governance framework it asks organisations to turn that policy into.

## A2. AI system inventory: the register

A2.1 The AI register lists every AI system in use or under evaluation, including AI
embedded in procured products (HR systems, customer engagement tools, office suites,
security tooling) and AI features enabled inside already-approved products. An AI
feature switched on is a new entry.

A2.2 Each entry records: system and supplier; purpose and business owner; accountable
person; level of use (policy clause 5); whether personal information is used, and of
what kinds; whether sensitive information is involved; where data is processed and
stored, and whether it leaves Australia; the supplier's rights over inputs and outputs,
including any right to train on them; the automated-decision determination (A4); the
privacy impact assessment reference; the risk screening outcome and controls (A5);
testing done and monitoring in place (A8); retention periods for prompts, outputs and
datasets; the supply-chain accountabilities; and whether the system is customer-facing
or interacts with children.

A2.3 The register is the source of the privacy-policy disclosure at A4.6, of the AI
use statements in collection notices, and of the quarterly review. It is reviewed
[quarterly]; material changes to a recorded system reopen approval.

## A3. Commencement readiness register

A3.1 The set treats the automated-decision transparency duty, which commences on 10
December 2026, as a design requirement from today. This register tracks readiness.

| Item | Source | Date | Status | Owner |
|---|---|---|---|---|
| Automated-decision determination recorded for every system bearing on decisions about people | Policy clause 12 | Before 10 Dec 2026, and at approval for new systems | [ ] | Data protection lead |
| Privacy policy carries the three required disclosures | Policy clause 13 | In place before 10 Dec 2026 | [ ] | Data protection lead |
| Regulator's final transparency guidance reviewed against the determinations (expected before commencement) | Source register | On publication | [ ] | Data protection lead |
| Children's Online Privacy Code registered and reviewed | Policy clause 19 | Registration due by 10 Dec 2026 | [ ] | Data protection lead |
| Statutory tort exposure reviewed for every monitoring, profiling and biometric system | Policy clause 18 | Complete | [ ] | Data protection lead |

A3.2 Every item carries an owner and a date. The register is a standing agenda item
for the AI Governance Committee until every item is closed, and is revived when a new
instrument is registered.

## A4. The automated-decision determination in operation

A4.1 For every system that bears on a decision about a person, the accountable person
records the determination at policy clause 12: whether [ORGANISATION] has arranged for
the program to make, or do a thing substantially and directly related to making, a
decision; whether the decision could reasonably be expected to significantly affect an
individual's rights or interests; and whether the individual's personal information is
used in the program's operation.

A4.2 The determination is made on the use, not the tool. The same tool used to draft
marketing copy and to shortlist applicants carries two determinations. When a system
could be used in more than one way, every use is considered, including foreseeable
misuse.

A4.3 The determination distinguishes decisions made **solely** by the program from
decisions to which the program **substantially contributes**, because the disclosure
must state each separately. A recommendation or summary that staff routinely act on is
a substantial contribution whether or not a person signs the decision.

A4.4 **Worked entries** (illustrative; each organisation records its own):

| System and use | Program makes or substantially contributes? | Significant effect on rights or interests? | Personal information used? | Within the duty from 10 Dec 2026? |
|---|---|---|---|---|
| Credit decisioning model, automated approval below a threshold | Makes (solely) | Yes - rights under a contract | Yes | Yes - disclose as a decision made solely by the program |
| Applicant screening assistant ranking CVs for a recruiter | Substantially contributes | Yes - access to employment | Yes | Yes - disclose as substantial contribution |
| Chatbot answering product questions, no account access | Neither | No | Possibly | No - but customer-facing disclosure applies |
| Spreadsheet calculating an age from a date of birth for a form | Directly but not substantially related | - | Yes | No |
| Fraud-scoring engine blocking transactions | Makes (solely) | Yes - access to a service | Yes | Yes |

A4.5 A system inside the duty is a Level 4 use and carries the human oversight,
explanation and review standards at policy clause 14, which go beyond what the Act
requires and are recorded as house standards.

A4.6 The **disclosure** is compiled from the register into the privacy policy: the
kinds of personal information used, the kinds of decisions made solely by such programs,
and the kinds of decisions to which such programs substantially contribute. The data
protection lead reviews it before commencement and on every register change that alters
it. The application rule is recorded: the duty attaches to decisions made after
commencement whatever the age of the arrangement, the data or the program.

## A5. Risk screening and management

A5.1 Every system and use case passes a risk screening before approval, using the
attributes the adoption guidance identifies as amplifying risk: opacity of the
technical architecture; reliance on generative AI in ways that can produce harmful
output; whether the output has a legal or significant effect on a person and whether
harm would be hard to contest; whether the system affects people with additional legal
protection, such as children, or is deployed in a public space; whether confidential,
personal, sensitive or biometric information is used in training, operation or
inference, and whether the data is representative; whether the system operates
autonomously without meaningful oversight; and whether it is general-purpose or easily
adapted beyond its intended use. A "yes" raises the level.

A5.2 The screening records use cases and qualities that represent an unacceptable
level of risk to [ORGANISATION] and that are not approved: the prohibitions at policy
clause 6.2 are the floor.

A5.3 Risk management distinguishes traditional software, narrow AI, general-purpose AI
and agentic AI, and applies controls proportionate to the level. Level 3 and Level 4
systems carry a written risk assessment and mitigation plan for each use case.

A5.4 AI incidents (policy clause 20.5) are investigated, documented and analysed, and
the lessons are applied to the system and to the risk process.

## A6. Privacy impact assessments

A6.1 A privacy impact assessment is completed before any Level 3 or Level 4 use, any
use that generates or infers personal information, any scraping or dataset
acquisition, any fine-tuning, any monitoring or profiling of staff or customers, and
any customer-facing AI. It is a living document, revisited as more is learned about
the system and on material change.

A6.2 The assessment addresses, as a minimum: the purposes for which the personal
information was collected and whether the AI use is within them; whether the use is a
use or a disclosure; the kinds of personal and sensitive information involved and the
basis for handling sensitive information; whether the system will generate or infer
personal information and the basis for that collection; accuracy and the steps to
ensure it; security and the supplier's access; overseas disclosure; retention and
destruction; notice and the privacy policy; the automated-decision determination; the
statutory tort; children and vulnerable people; and the stakeholder impact assessment
the adoption guidance asks for, with particular attention to vulnerable and
marginalised cohorts.

A6.3 Where the assessment cannot establish that a proposed secondary use for an
AI-related purpose is within individuals' reasonable expectations and related to the
primary purpose, the assessment records the consent or opt-out mechanism that will be
used instead, and the use does not proceed until it is in place.

## A7. Suppliers and the AI supply chain

A7.1 Before an AI supplier is engaged, [ORGANISATION] reviews the supplier's terms for:
rights over inputs and outputs, including any right to train on them; sub-processors;
data location; security measures and incident history; the supplier's ability to delete
on instruction and to evidence access; and, for generative tools, controls against
regurgitation of training or context data.

A7.2 The contract provides for: processing only for [ORGANISATION]'s purposes and on
its instructions; no use of [ORGANISATION] data to train or improve the supplier's
models unless expressly approved under policy clause 16; security measures; breach
notification to [ORGANISATION] without undue delay and in time for [ORGANISATION] to
meet the thirty-day assessment; return or deletion at the end; audit or assurance
rights; and, where the supplier is outside Australia, terms that support the reasonable
steps the cross-border disclosure principle requires.

A7.3 **Overseas recipients.** A disclosure of personal information to an overseas AI
supplier requires reasonable steps to ensure the supplier does not breach the
Australian Privacy Principles, and [ORGANISATION] remains accountable for the
supplier's handling as if it were its own, unless an exception applies (a substantially
similar binding law or scheme with an enforcement mechanism the individual can access; a
prescribed country or scheme; or express, informed consent). Deploying locally or on
premises is recorded as the more privacy-preserving option where it is available.

A7.4 Suppliers are asked for proof of testing, for documented capabilities and
limitations, and for information about training data sources sufficient for
[ORGANISATION] to assess accuracy and bias for its own use. Supply-chain
accountabilities are recorded in the register.

## A8. Testing, monitoring and assurance

A8.1 Systems are tested before deployment for the intended use, including for
inaccurate, biased and harmful outputs and for surfacing personal information about
others. Level 4 systems are tested for differential outcomes across the attributes
anti-discrimination law protects before deployment and at least [annually].

A8.2 Monitoring after deployment is matched to the level: performance drift, accuracy,
bias, unintended impacts, new risks not present at deployment, and, for Level 4,
override rates. Feedback from complaints and contestability channels is monitored for
systemic issues.

A8.3 Data governance and cybersecurity practices are extended to AI systems, including
protection of models that have learned from sensitive data, and access control and
logging over prompts and outputs.

A8.4 Level 3 and Level 4 systems are stress-tested against attempts to bypass safety,
security and policy controls. Systems identified at screening as needing additional
governance attention are independently tested before deployment, after significant
change and periodically.

A8.5 Human override points are documented for every system: who can pause, roll back
or shut it down, and how. Alternative pathways are maintained so that critical
functions continue if a system fails or is withdrawn.

## A9. Incident response

A9.1 The incident process at policy clause 20.5 is operated by [Security] with the
data protection lead. On a suspected eligible data breach involving an AI tool, the
clock for the thirty-day assessment starts when [ORGANISATION] becomes aware of
reasonable grounds to suspect; the statement to the Information Commissioner is
prepared and given as soon as practicable once there are reasonable grounds to believe;
individuals affected or at risk are notified of its contents. Where remedial action
taken before serious harm is likely removes the likelihood of serious harm, the
exception the Act provides is assessed and documented.

A9.2 AI-specific incident types are recognised and drilled: personal information
entered into an unapproved or public tool; a tool surfacing another customer's or
user's data; a supplier breach; model regurgitation of training or context data; an
agent acting outside its approved actions; a Level 4 system producing a systematically
wrong or discriminatory result; harmful or unlawful generated content.

A9.3 Every AI incident, whether or not a data breach, is recorded, investigated and
analysed, and the lessons are applied (A5.4).

## A10. Individuals' rights and contestability

A10.1 Individuals can access, and seek correction of, personal information about them
that AI has generated or that is held in AI tools. Requests are answered within a
reasonable period, without charge for the request or the correction; refusals are in
writing with reasons and the complaint mechanism; a statement of disputed accuracy is
associated with the information on request.

A10.2 Contestability channels proportionate to the seriousness of the impact are
maintained for every system affecting people, and [ORGANISATION] can act to set things
right where a system has negatively affected someone. For Level 4 decisions, the
explanation and human review standards at policy clause 14 apply.

A10.3 Complaints about AI handling of personal information follow the mechanism in the
privacy policy. Patterns are reported to the AI Governance Committee.

## A11. Training and awareness

A11.1 Staff training follows policy clause 21. Accountable people and those overseeing
Level 4 systems receive training on the system's capabilities, limitations and failure
points, on when to intervene, and on the automated-decision duty.

A11.2 The data protection lead and [Legal] maintain awareness of the regulator's AI
guidance, the transparency guidance expected before commencement, the Children's Online
Privacy Code on registration, and the privacy reform program the government has said it
is continuing.

## A12. Metrics reported to the AI Governance Committee

- Number of systems on the register by level; new, changed and retired in the period
- Systems bearing on decisions about people with a recorded determination, and the
  number inside the duty
- Privacy impact assessments open, completed and overdue
- Level 4 override rate by system
- Incidents by type; eligible data breach assessments opened and their durations;
  notifications made
- Complaints and contestability requests, and time to resolve
- Testing and monitoring findings, including bias testing results
- Training completion for users, accountable people and overseers
- Commencement readiness register status

## A13. Scope of this annex and what is not held

A13.1 This annex operates the Privacy Act 1988 (Cth) as compiled on 4 June 2026, the
Privacy and Other Legislation Amendment Act 2024, the Information Commissioner's AI
guidance of October 2024 and the automated-decision issues paper of May 2026, the
Guidance for AI Adoption of October 2025 and the National AI Plan of December 2025.

A13.2 **It does not hold**, and therefore does not state: the final regulator guidance
on automated-decision transparency; the Children's Online Privacy Code; any registered
APP code binding [ORGANISATION]; the Privacy Regulation and any prescribed countries or
schemes for cross-border disclosure; state and territory privacy, health-records and
surveillance-device laws; the Australian Consumer Law; anti-discrimination law and the
Fair Work Act; the Online Safety Act; prudential and sector standards. Each is named in
policy clause 22 as an open verification and is recorded in the source register.

---

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | 3 September 2026 | Initial annex, published within its stated scope. Every obligation traced to the held instruments in the research note. |

---

*Educational template - not legal advice. Review by qualified counsel before adoption.*
