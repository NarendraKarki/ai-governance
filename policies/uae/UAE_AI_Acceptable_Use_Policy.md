# Artificial Intelligence Acceptable Use Policy - United Arab Emirates

### DIFC-registered entities, with routing for ADGM and the federal regime

**Organisation:** [ORGANISATION]
**Effective date:** [DATE]  **Version:** 1.0
**Policy owner:** [CISO]  **Data protection lead:** [Data Protection Officer]
**Automated Systems Officer:** [ASO - see Section 12]
**Classification:** Internal
**Review:** at least every six months, and on material change in tools or regulation

---

## 1. Purpose

[ORGANISATION] permits the use of artificial intelligence (AI) tools to improve
productivity, provided that use protects the organisation's data, its customers and
staff, its intellectual property, and its data protection obligations. This policy sets
the requirements for all such use.

**Four features shape this document, and the first is the one most often got wrong.**

### 1.1 The UAE is not one data protection jurisdiction

Three separate regimes operate, with different regulators, different obligations and
different breach clocks. **They do not share rules, and the free zones are not a
variation on the federal law - they are an exclusion from it.** The federal law's own
scope provision excludes free-zone companies that have their own data protection law.

Section 3 routes each entity to its regime. **An organisation applying the wrong one is
not partly compliant; it is complying with a law that does not govern it.**

This policy is written for a **DIFC-registered** entity. Section 3 states what changes
for ADGM and for federal-regime entities, and Section 22 states the limits of what this
set can say about either.

### 1.2 The DIFC has a genuine AI-specific regime, and it is a certification regime

Unlike a general data protection law applied to AI by analogy, the DIFC has a dedicated
instrument for **autonomous and semi-autonomous systems that process personal data**.
Its core rule is a prohibition with a condition attached: **no person may use, operate,
provide, offer or otherwise make available for commercial use such a system to engage in
High Risk Processing Activities unless all audit and certification requirements
established by the Commissioner are satisfied.**

That is a licence-style gate, not a documentation duty. Sections 5 to 13 set out what it
requires.

### 1.3 The regime turns on autonomy, and deliberately excludes deterministic software

The instrument defines a **System** as any machine-based system operating in an
autonomous or semi-autonomous manner that can process personal data for human-defined
purposes, or purposes the system itself defines, or both, and generate output on the
basis of that processing.

**It expressly does not capture purely automated systems** - systems with no degree of
autonomy, whose operation is deterministically controlled by humans - because the
underlying law already governs automated processing.

Section 4 explains why that boundary decides which of your tools are in scope, and why
it is not the same boundary other frameworks draw.

### 1.4 A system that can define its own purposes is contemplated, and constrained

The regime does not assume a system's processing purposes are fixed by its designers. It
contemplates a system **defining further purposes for itself**, requires the
human-defined limits within which it may do so to be stated, and requires that **any
self-defined purpose conform to a predefined set of human-approved principles**.

Section 11 sets this out. It is the most forward-looking requirement in the instrument
and the one most likely to bite on agentic deployments.

## 2. Scope

This policy applies to all employees, contractors, secondees, temporary staff and third
parties who use [ORGANISATION] systems, data or accounts. It covers all AI tools,
including public and generative AI services, AI features embedded in other software,
coding assistants, meeting and note-taking assistants, media generators, AI agents, and
internal AI systems.

It applies on company devices and accounts, and on personal devices or accounts whenever
used for [ORGANISATION] work or data.

Compliance is mandatory. Breaches may result in disciplinary action up to and including
termination.

## 3. Which regime applies

3.1 **DIFC-registered entities** are governed by DIFC data protection law and its
regulations, and supervised by the **DIFC Commissioner of Data Protection**. This policy
is written for them.

3.2 **ADGM-registered entities** are governed by the ADGM Data Protection Regulations and
supervised by the **ADGM Commissioner**. The obligations differ. **The single difference
most likely to cause a failure is the breach clock** - Section 14.2.

3.3 **Entities elsewhere in the UAE** are governed by the federal personal data
protection regime and supervised by the **UAE Data Office**. Section 14.3 states the
breach position, and Section 22 the limits of what this set says about it.

3.4 **Being in a free zone does not put an entity outside all UAE data protection law for
every purpose.** In-zone entities commonly process some personal data outside the zone,
and the federal regime is not displaced for that processing merely because the entity is
registered in a zone. Where [ORGANISATION] processes personal data outside its zone, the
data protection lead determines the applicable regime for that processing and records
the determination.

3.5 The federal regime's scope provision also excludes several categories that matter to
a financial-sector organisation - including **health data governed by its own
legislation** and **banking and credit data governed by its own legislation**. Where a
category is excluded from the federal regime, another regime governs it, and this policy
does not state what that regime requires.

3.6 **Sector rules are separate and may bite harder.** Both free zones exist to host
financial institutions, and the financial services regulator in each zone maintains its
own requirements on outsourcing, technology risk and incident reporting. **This policy
does not cover them and does not assert them** - Section 22.

## 4. Which of your tools are in scope

4.1 A tool is a **System** for the purposes of Sections 5 to 13 if it operates in an
**autonomous or semi-autonomous manner**, processes personal data for human-defined
purposes or purposes it defines itself, and generates output on that basis.

4.2 A tool is **not** a System merely because it is automated. Deterministic software
whose operation is entirely controlled by humans falls outside this definition and is
governed by the general provisions on automated processing instead.

4.3 This boundary is unusual and must be applied deliberately rather than assumed:

| Likely a System | Likely not a System |
|---|---|
| A generative model that plans, retrieves and composes its own response | A rules engine that applies fixed criteria in a fixed order |
| An agent that selects its own tools, sources or next steps | A scheduled batch job with fixed logic |
| A model that adapts behaviour from feedback or retraining | A deterministic scoring formula, however complex |
| An assistant that decides what to include, summarise or escalate | A template mail-merge |

4.4 The determination is made by the data protection lead with the [ASO], recorded in the
AI system inventory, and **revisited whenever the tool gains autonomy** - which is what
adding tool-use, retrieval, memory or planning to an existing product does.

4.5 **A tool can become a System without being replaced.** A vendor enabling an agentic
feature changes the analysis, which is why Section 6.4 makes material vendor changes
reopen the approval.

## 5. The certification gate

5.1 Where a System is used, operated, provided, offered or otherwise made available for
commercial use to engage in **High Risk Processing Activities**, the audit and
certification requirements established by the Commissioner must be satisfied.
[ORGANISATION] treats this as a gate to deployment, not a post-deployment formality.

5.2 **Certification is granted by an Accredited Certification Body**, or by the
Commissioner in exceptional circumstances arising from the absence or unavailability of
an accredited body. Applications are submitted **in English** with supporting
documentation.

5.3 **Certification is valid for three years** from initial certification. The
Commissioner retains authority to conduct periodic risk-based reviews, which may be
triggered by amendments to the certification criteria, significant changes to the
certified System, **recurring verified complaints about use of the System that negatively
impacts individuals**, or failure to adhere to the conditions of certification.

5.4 An audit confirming the effectiveness of the certification must be conducted **at
least once during the three-year validity**. Where the certification body assesses that
audits should be more frequent, it must give **at least 30 days' notice** before the
compliance audit.

5.5 **[ORGANISATION] may not state or imply that a System is certified** unless the
certification is valid and has not expired, been revoked, or been modified such that it
is no longer valid.

5.6 **Prior consultation is available.** [ORGANISATION] may seek an assessment from the
Commissioner or a delegate **before** deploying, operating or providing a System. The
committee considers this route for any System where the High Risk determination at 5.7 is
finely balanced.

5.7 **"High Risk Processing Activities" is a defined term in the underlying law and
regulations, which this policy does not reproduce.** The data protection lead determines,
in writing and for each System, whether its processing falls within it, and records the
reasoning. **Where the determination is uncertain, [ORGANISATION] proceeds as though it
does** until advice says otherwise, and considers prior consultation under 5.6.

5.8 **The timeline for implementing the certification framework is at the Commissioner's
discretion.** [ORGANISATION] does not treat that as a reason to defer readiness - Section
21.2 - and the committee tracks the Commissioner's position at each meeting.

## 6. Roles, and which one [ORGANISATION] holds

6.1 The regime distinguishes three roles, and an organisation may hold more than one:

- a **Provider** develops a System, or procures that one is developed for or on its
  behalf, with a view to providing, commercialising or otherwise making it available to
  Operators or Deployers;
- an **Operator** is a Provider that operates or supervises a System on behalf of, for
  the benefit of, and on the direction of a Deployer - **whether or not it exercises any
  control over the processing of personal data by the System**;
- a **Deployer** is the person under whose authority, on whose direction or for whose
  benefit the System is operated, **or** who receives the benefit of its operation or of
  any output it generates - **in each case whether or not that person operates,
  supervises or hosts the System, and whether or not that person defines the purposes for
  which personal data is processed by it.**

6.2 **The Deployer definition is deliberately wide.** Receiving the benefit of a
System's output is enough. An organisation that neither hosts the System nor sets its
purposes, and simply uses what it produces, is a Deployer.

6.3 [ORGANISATION] records, for every System in the inventory, which role it holds and
on what basis. Where it is a Deployer, it does not treat the Provider's or Operator's
obligations as covering its own.

6.4 **[ORGANISATION] becomes a Provider** if it develops a System, or procures that one
is developed for it, with a view to making it available to others. Fine-tuning,
rebranding or embedding a third-party System in a product [ORGANISATION] offers may
change the role. No such step is taken without a fresh role assessment, and a material
change by a vendor reopens the assessment too.

6.5 Separately, [ORGANISATION] is a **Controller** or **Processor** for data protection
purposes. The two role sets are independent and both are recorded.

## 7. Approved tools

7.1 Only AI tools on the [ORGANISATION] Approved AI Tools list may be used with
[ORGANISATION] or personal data.

7.2 A tool is added to the list only after: the System determination at Section 4; the
role determination at Section 6; a High Risk determination at 5.7 where it is a System;
security and data protection review; and a written contract meeting Section 10.

7.3 Use of any tool not on the list - including free or personal-account versions of
listed tools - is not permitted for [ORGANISATION] work or data.

7.4 Staff who need a tool that is not listed must request it through [FORM / CHANNEL];
requests are assessed within [N] business days.

7.5 Staff already using an unapproved tool must disclose this to the policy owner.
Good-faith disclosure will not of itself be treated as a disciplinary matter.

7.6 The approved list records, for each tool, whether it is a System, the role
[ORGANISATION] holds, whether its processing is High Risk, and its certification status.

## 8. Levels of use

**Level 1 - Open.** No confidential information and no personal data. Approved tools.

**Level 2 - Internal.** Internal non-personal information. Approved tools with a written
contract.

**Level 3 - Personal data.** Any personal data. Approved tools, written contract, a
recorded lawful basis, and registration in the AI system inventory.

**Level 4 - System engaged in High Risk Processing.** Everything at Level 3, plus
Sections 5, 11, 12 and 13, and approval by the AI Governance Committee.

Where a use sits between two levels, the higher applies.

## 9. Governance, principles and the impact assessment

9.1 A System used for High Risk Processing must be deployed **in accordance with an
overarching governance document** setting out requirements for adherence to the
principles of **fairness, transparency, accountability, security and ethics**. This
policy and its annex are that document for [ORGANISATION].

9.2 The principles the regime applies across a System's whole lifecycle are: **fairness,
transparency, ethics, security, data quality, necessity and proportionality,
risk-assessment, and accountability.**

9.3 **A risk-based necessity assessment comes first.** Before a System is used for High
Risk Processing, [ORGANISATION] must have determined, on a risk-based approach, that the
processing is necessary **through that System rather than through a different, lower-risk
System**. The question is not whether the System is useful; it is whether a less risky
one would do.

9.4 Where High Risk Processing through the System is necessary, [ORGANISATION] then
assesses and records:

- whether the identified risks of the System have been catalogued;
- whether the collection and processing of personal data is **necessary and
  proportionate** for the purpose of the use case; and
- whether appropriate measures to **effectively mitigate** the impact of those elements
  are in place.

9.5 [ORGANISATION] maintains, for each such System: a **risk management framework**; an
**AI data protection impact assessment** assessing necessity, identifying associated
risks, recording management action plans showing how controls were integrated into the
development process **and evidence that they were**; an **AI policy** carrying the
technical and organisational controls; and a **risk register** of the System's associated
risks with supporting documentation showing they have been identified and mitigated.

9.6 **An assessment that identifies a control and does not evidence its integration does
not meet 9.5.** The evidentiary standard is explicit, and the annex tracks implementation
dates.

## 10. Transparency, notice and third parties

10.1 A System must be **designed and implemented to be transparent and fair** to
individuals about why their personal data is collected, for what purposes, where it will
be stored, whether it will be shared with third parties, and any other information
necessary to help them understand and choose whether to share it.

10.2 [ORGANISATION] must be able to provide **evidence of meaningful notice** and
evidentiary explanations for its decisions about providing that information. The privacy
notice must describe the System's processing in a clear and easily understandable manner
and must in particular address:

- **the impact of the use of the System on the exercise of individuals' rights** under
  the law;
- **the human-defined purposes for processing**;
- **the human-defined principles on the basis of which, and all human-defined limits
  within which, the System is capable of itself defining further purposes for processing
  personal data**; and
- the codes, certifications or principles on which the System is designed or developed.

10.3 The third item is the one no ordinary privacy notice contains. **If [ORGANISATION]
cannot state the limits within which a System may define its own purposes, it cannot give
a compliant notice for it** - and Section 11.3 makes that a bar to deployment rather than
a drafting problem.

10.4 Where consent is the lawful basis, the System's consent mechanism is documented, and
a mechanism exists to update the System in response to user feedback.

10.5 **Third parties.** A System must have been developed, designed, procured or
otherwise obtained subject to **enhanced due diligence**, ensuring appropriate technical,
organisational or contractual arrangements safeguard personal data, and that processors
and other third parties related to the System's function **implement substantially
similar measures**.

10.6 [ORGANISATION] holds, for each System: due diligence documentation recording how the
Provider's System and its compliance were assessed; contracts clearly delineating data
protection roles and responsibilities; contracts for international transfers including
cross-border safeguards; and a review of the Provider's **data protection by design**
documentation.

10.7 **Roles and responsibilities regarding transparency and other compliance obligations
in the supply chain must be clear.** Where they are not, the arrangement is not approved.

## 11. Autonomy, self-defined purposes and human oversight

**This section carries the requirements most specific to autonomous systems. It applies
in addition to Section 15.**

11.1 A System must act in accordance with technical and organisational measures and
appropriate safeguards and controls, including disposal, vulnerability and attack
detection, resilience, and **failure of human-defined processing purposes**.

11.2 **Any self-defined purpose generated by the System must conform to a predefined set
of human-approved principles.** Those principles are defined and approved before
deployment, not derived afterwards from what the System did.

11.3 For every System, [ORGANISATION] records **the human-defined purposes**, **the
human-defined principles**, and **all human-defined limits within which the System may
define further purposes for itself**. A System whose limits cannot be stated is not
deployed - see 10.3.

11.4 The evidence [ORGANISATION] maintains includes: system architecture documentation;
**code review records assessing how the code implements human-defined purposes and the
absence of self-defined purposes**; **processing purpose logs** tracking the System's
processing purposes and documenting that processing is in line with human-defined
purposes; documentation of the externally predefined principles and how the System
conforms to them; internal policies on how the System should operate; and **algorithmic
audits** assessing the algorithms against human-defined processing purposes, with any
corrective actions taken.

11.5 **Processing purpose logging is a design requirement, not a monitoring preference.**
A System that cannot produce a record of the purposes it actually processed for cannot
evidence 11.2, and is not approved for High Risk Processing.

11.6 [ORGANISATION] maintains mechanisms assuring **routine review of the System's
processing purposes, of the output it produces, and of the manner in which that output is
used, ensuring human oversight throughout**. The review covers all three; reviewing the
output alone does not satisfy it.

11.7 Evidence of oversight includes documented oversight processes with measures for
receiving, investigating and responding to complaints about the System's function and
outputs; audit and review reports; training records for oversight personnel; feedback
logs; System adaptations maintaining alignment with intended purposes; and, where
[ORGANISATION] has one, an ethics committee.

## 12. The Automated Systems Officer

12.1 A System used for High Risk Processing must be **monitored by an Automated Systems
Officer (ASO)**, having at minimum the same or similar **competencies, status, role and
tasks as a Data Protection Officer** under the law, and in addition the **technical and
organisational expertise** to ensure effective governance and oversight of the System and
the ongoing validity of its certification.

12.2 The ASO's job profile specifies technical knowledge of Systems, ethics, data
protection, risk management, complaints handling and remediation, and regulatory and
legal requirements.

12.3 **There must be no gap of more than one month** before the operation of a System for
High Risk Processing, or between an outgoing ASO and a replacement, unless the
Commissioner approves an exception for extenuating circumstances.

12.4 **[ORGANISATION] treats 12.3 as a hard operational constraint.** A named deputy is
recorded for the ASO at all times, and an ASO departure triggers the succession process
on the day notice is given, not on the day of departure.

12.5 [ORGANISATION] provides appropriate support so the ASO may **independently** review
and assess audit documentation against the certification requirements, and provides a
**gap analysis, risk register and management action plan** where required to remedy
identified risks.

12.6 The ASO role is distinct from the Data Protection Officer role. Where one person
holds both, the committee records why that does not compromise the independence at 12.5,
and reviews the position annually.

## 13. Bias, data quality and monitoring

13.1 A System used for High Risk Processing must be deployed with **appropriate measures
in place to identify and mitigate risks of bias and discrimination**.

13.2 The evidence [ORGANISATION] maintains includes: job descriptions setting out
education, training or experience in ensuring fairness; training programmes on reducing
bias; **review and evaluation processes to identify and correct potential bias issues**;
**model modifications made to address biases**; and data quality assessments.

13.3 The fourth item is evidence of remediation, not of testing. **Finding bias and not
changing the model does not satisfy 13.1.**

13.4 A System must be designed to ensure that, so far as possible, the data and datasets
it processes are **accurate, quality-assessed, reliable, relevant and limited to its
specific purpose**, and, where required, **human intervention for review and assurance is
designed into the System**.

13.5 [ORGANISATION] documents: a data inventory evidencing that training and operating
datasets are adequately sized and relevant; the availability of metadata describing those
datasets; the use of **privacy-preserving methodologies** that reduce the personal data
that must be collected, stored or processed; measures to periodically review and update
datasets for accuracy, quality, currency, relevance and reliability; and statistical
assessments verifying the currency and validity of the data processed.

13.6 [ORGANISATION] maintains **active monitoring of the use and quality of collected
personal data**, and **review or regular model tuning** where appropriate - for example on
changes to customer behaviour, commercial objectives, risks, or corporate values - and a
mechanism for **giving and receiving updates to and from third parties** about the quality
and use of personal data collected through the System.

13.7 **Robustness and resilience.** A System must guard against unauthorised access
exploiting vulnerabilities, and against faults or errors arising from **changes in the
System's environment**. Evidence includes policies and procedures against attacks such as
**data poisoning**, security architecture documentation, training on recognising and
mitigating attacks, documented error-handling mechanisms and contingency plans, and
incident reports.

## 14. Personal data breach - three regimes, three answers

**The breach clock is where applying the wrong regime does the most damage. Read 14.1
before 14.2 or 14.3.**

14.1 **DIFC.** Notification to the Commissioner is required **as soon as practicable in
the circumstances**, for a breach that compromises an individual's confidentiality,
security or privacy. **There is no fixed period in the DIFC law.**

**That is a fact about the statute, not a gap in this policy.** It should not send anyone
hunting for a 72-hour rule, and it does not license delay: "as soon as practicable" is a
standard [ORGANISATION] must be able to evidence it met, and [ORGANISATION] sets an
internal target of [N] hours from awareness.

14.2 **ADGM.** Notification to the ADGM Commissioner is required **within 72 hours** of
becoming aware, and the duty is disapplied where the breach is unlikely to result in a
risk. **Neither the period nor the risk threshold applies in the DIFC.**

14.3 **Federal.** The controller must notify the Bureau on becoming aware of the breach,
**within the period and in accordance with the measures and requirements set by the
Executive Regulations**. Those Executive Regulations **have not been issued**, so no
period is established. See Section 22.3 on what circulates to the contrary.

14.4 **Do not carry a period across regimes.** A 72-hour figure attached to the DIFC or
to the federal law is wrong, however widely it is repeated, and Section 22.3 explains
where that figure actually comes from.

14.5 Any suspected breach involving an AI tool - a wrong recipient, an unapproved tool,
an exposed prompt log, a misconfigured index, a supplier notification - is reported to
[SECURITY CONTACT] and the data protection lead **immediately on suspicion**, not after
internal investigation. Awareness is recorded as a timestamp by a named person.

14.6 For each Level 3 and Level 4 System, [ORGANISATION] records in advance how it would
establish, from the System's own records, whose personal data a given exposure touched. A
System that cannot answer is not approved for personal data.

14.7 A System must be deployed with the appropriate level of security to protect personal
data, maintain confidentiality and prevent breaches that could cause **reputational,
psychological, financial, professional or other harm**. Evidence includes security risk
assessments, model debugging processes rectifying flaws and vulnerabilities, breach
policies and procedures, encryption and access controls, and privacy-enhancing
technologies where appropriate.

14.8 Supplier contracts require immediate notification to [ORGANISATION] on the supplier
becoming aware, with enough detail to meet whichever obligation at 14.1 to 14.3 applies.

14.9 Staff who report in good faith will not face disciplinary action for reporting.

## 15. Automated decisions and agents

15.1 No Level 4 decision about a person is made solely by a System. A named person
reviews the output, has the authority and information to reach a different conclusion,
and records the determination as their own. Where human intervention is designed into the
System under 13.4, this is how it operates in practice.

15.2 A review that only ratifies the output is not a review.

15.3 AI agents operate under their own credentials with least-privilege access. A
person's own credentials must never be given to an agent.

15.4 **An agent that selects its own tools, data sources or next steps is exercising the
autonomy that makes a tool a System** (Section 4) and, where it may define further
purposes, engages Section 11 in full. Its human-defined limits are recorded before it
runs.

15.5 Consequential actions - making payments, sending external communications, changing
records about people, deploying code, publishing, or deleting data - require a human
checkpoint before execution unless the committee has expressly approved autonomous
operation for that action and System.

15.6 Agent activity is logged and attributable to a named human owner; sessions are
bounded in scope and duration; every agent has a documented means of immediate
suspension. **Agent logs include the processing purpose logs required by 11.4.**

15.7 Content an agent ingests from outside [ORGANISATION] is treated as untrusted input,
including instructions embedded in that content.

## 16. Individuals' rights and access

16.1 [ORGANISATION] maintains a documented route by which a request from an individual is
executed against every AI tool in the inventory, including prompts, uploads, transcripts,
embeddings, caches and logs.

16.2 A tool from which personal data cannot be located and retrieved on request is not
approved for personal data.

16.3 [ORGANISATION] maintains a **register** accounting for information including
individuals' rights of access, lawful bases for processing, **automated decision-making**,
and the contractual obligations of joint controllers, processors and sub-processors.

16.4 A System must be designed so that **it will seek human intervention** where the
underlying regulations require it, and the design materials evidencing that are held.

16.5 The privacy notice must address **the impact of the System's use on the exercise of
individuals' rights** - Section 10.2.

## 17. Prohibited by [ORGANISATION]

17.1 Deploying a System for High Risk Processing without satisfying the certification
gate at Section 5, or without a current ASO under Section 12.

17.2 Deploying a System whose human-defined limits on self-defined purposes cannot be
stated - Section 11.3.

17.3 Stating or implying that a System is certified when it is not, or when the
certification has expired, been revoked or been modified such that it is no longer valid.

17.4 Entering personal data into any tool not on the approved list.

17.5 Entering credentials, keys, secrets or security configuration into any AI tool.

17.6 Using AI output as the sole basis for a Level 4 decision about a person.

17.7 Disabling, bypassing or reducing processing purpose logging, algorithmic audit
records, or any other evidence required by Sections 9 to 13.

17.8 Using AI to covertly monitor, profile or score employees.

17.9 Using AI to produce material that is unlawful, defamatory, harassing or
discriminatory.

No exception may be granted against 17.1, 17.2, 17.3 or 17.7.

## 18. Verification of output

18.1 AI output is a draft. The person who uses it is accountable for it.

18.2 Any factual claim, figure, calculation, date, quotation, citation or regulatory
reference taken from AI output and relied on externally, or in a decision, must be
verified against a primary source before use.

18.3 Code generated by AI is reviewed before merge, with attention to secrets, licence
terms and dependencies the model has introduced.

18.4 AI-generated citations are verified to exist and to say what they are said to say.

18.5 **Regulatory references in AI output are verified against the applicable regime.**
Section 22.3 records a real instance of a widely repeated citation error in this
jurisdiction, and it is the reason this clause exists.

## 19. Preventing harm

19.1 [ORGANISATION]'s personal information protection programme is designed to **prevent
the misuse of personal information**, and its organisational controls are **proportionate
to the likelihood and severity of any harm** threatened by the collection, use or transfer
of that information.

19.2 [ORGANISATION]'s privacy practices and policy are in accordance with the principles
of the applicable law, are **easy to find and accessible**, and apply to **all personal
information, whether collected online or offline**.

19.3 The certification assessment scheme organises its requirements around preventing
harm, notice, collection limitation, uses of personal information, choice, integrity of
personal information, security safeguards, access and correction, and accountability,
governance and oversight. [ORGANISATION] maps its controls to those headings so that
readiness is assessed in the terms the assessment will use.

## 20. Intellectual property, records and public-facing AI

20.1 AI-generated material used externally is reviewed for third-party rights before
publication.

20.2 [ORGANISATION] material must not be placed in tools whose terms grant the supplier
rights over input or output beyond what the approval accepted.

20.3 Records supporting compliance - determinations, assessments, approvals, contracts,
processing purpose logs, algorithmic audits, verification records and breach records - are
retained for [PERIOD] and are producible on request, including to the Commissioner.

20.4 A public-facing System requires committee approval before launch, discloses that the
person is interacting with an AI system, offers a route to a human, and is bounded in
what it may commit [ORGANISATION] to.

## 21. Responsibilities and readiness

21.1 **All staff** - use approved tools only; apply the correct level; verify output;
report suspected breaches immediately; never disable logging or audit records.

**Business owners** - the inventory record, the System and role determinations, the
impact assessment, the supplier relationship.

**Automated Systems Officer** - monitoring of Systems used for High Risk Processing,
independent review of audit documentation, the gap analysis and management action plan.

**Data protection lead** - the High Risk determinations, notices, individuals' rights, the
register, breach notification, and which regime applies under Section 3.

**Policy owner** - the approved tools list, security review, exceptions, and this policy.

**AI Governance Committee** - Level 4 approvals, certification readiness, the ASO
succession position, exceptions, metrics and regulatory change.

21.2 **The certification framework's implementation timeline is at the Commissioner's
discretion, and [ORGANISATION] does not wait for it.** The evidence the scheme requires -
the impact assessment, the risk register, the processing purpose logs, the algorithmic
audits, the ASO appointment - takes longer to build than a certification takes to apply
for, and cannot be produced retrospectively for a System already in service.

## 22. What this policy does not state, and why

### 22.1 The instruments behind it

This policy rests principally on the **DIFC Regulation 10 Accreditation and Certification
Framework** issued by the Commissioner of Data Protection, which [ORGANISATION] holds in
full.

**It does not hold Regulation 10 itself, nor a current consolidation of the DIFC data
protection law.** The Framework implements provisions of both and refers to them
repeatedly. Where it quotes them, this policy follows the quotation; where it only cites
them, **this policy states the Framework's requirement and not the underlying provision.**

Accordingly this policy does not state:

- **the definition of High Risk Processing Activities** - the trigger for the whole
  regime. Section 5.7 routes it to the data protection lead;
- the content of the regulation provisions the Framework cites for notice particulars,
  design principles and the certification obligation;
- the articles of the DIFC law governing prior consultation, contract clauses, government
  authority requests, notice, the Data Protection Officer, or accreditation;
- the penalties for contravention.

### 22.2 The other two regimes

This policy states the **breach position** for ADGM and for the federal regime because
each has been verified against the official text, and because getting that specific point
wrong is the most consequential error available here. **It states nothing else about
either regime.** An ADGM or federal-regime entity needs its own document.

It also does not state the financial services regulators' requirements in either zone -
Section 3.6.

### 22.3 A caution about published sources

A specific error circulates widely in this jurisdiction and has appeared in professional
commentary: **the phrase "without undue delay and, where feasible, not later than 72
hours after having become aware of it", attributed to the federal law's breach article.**

That wording is not in the federal law. It is the wording of a European provision, and
the real 72-hour duty in the UAE sits in **ADGM**, whose regulations adopted similar
language. Commentary took a free-zone rule and attached a federal article number to it.

Related claims that also fail against the official text: that the federal Executive
Regulations were issued in 2023 - they have not been, as at the date of this policy; that
a specific maximum fine is set in the federal decree-law - it is not; and that a
subject-access response period is specified in it - none is.

**This is why Section 18.5 exists.** A citation that verifies against a plausible source
and fails against the primary text is the failure mode this policy is most concerned
with, and it has been performed here by humans, in print, before any AI tool was
involved.

## 23. Knowledge, skills and acknowledgement

23.1 Staff who use AI tools with personal data complete training covering this policy,
**which regime applies (Section 3)**, the System determination (Section 4), and the
breach duties (Section 14), before access is granted and at least [annually] thereafter.

23.2 Staff who operate, oversee or make decisions informed by a System used for High Risk
Processing complete additional training on Sections 9 to 13.

23.3 Staff acknowledge this policy on joining, on material revision, and at least
annually.

23.4 Questions go to [CONTACT]. Asking before acting is always acceptable.

---

**Version history:**
1.0 - initial policy, published 2 September 2026; verified within its stated
scope (DIFC-registered entities; evidence tiers stated in the research note
and source register).

---

*This document is an educational policy template and does not constitute legal advice.
It is written for a DIFC-registered entity, reflects obligations as set out in the
accompanying research note, and must be reviewed by the data protection lead or qualified
legal counsel before adoption.*
