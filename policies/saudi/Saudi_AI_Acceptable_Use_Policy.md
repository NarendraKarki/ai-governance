# Artificial Intelligence Acceptable Use Policy - Saudi Arabia

### Government data - public entities and their business partners

**Entity:** [ENTITY]
**Effective date:** [DATE]  **Version:** 1.0
**Policy owner:** [Chief Data Officer]  **Personal data lead:** [Personal Data Protection Officer]
**Classification:** Public
**Review:** at least every six months, and on material change in tools or regulation

---

## 1. Purpose and the limits of this policy

[ENTITY] permits the use of artificial intelligence (AI) tools to improve productivity,
provided that use protects government data, the individuals whose personal data
[ENTITY] holds, and [ENTITY]'s obligations under the national data management,
classification and sharing instruments. This policy sets the requirements for all such
use.

**Read this clause before any other. Four features of the framework shape this
document, and the first is a limit on the document itself.**

### 1.1 This policy governs government data

The instruments this policy rests on apply to **public entities**, and extend to
**business partners handling government data** - entities engaged in producing,
managing or overseeing government data, who must apply the same standards to all
government data within their control and custody.

**This is therefore not a general private-sector AI policy.** An organisation
processing only its own customers' or employees' personal data, with no government
data, is governed by the Kingdom's personal data protection legislation, **which is
not the basis of this document**. Clause 22 says so plainly and explains what would
be needed to write that document instead.

If [ENTITY] holds both government data and its own commercial personal data, this
policy governs the first and must be read alongside a separate instrument for the
second.

### 1.2 There is no artificial intelligence provision anywhere in these instruments

The standards were issued under a mandate to develop policies, governance mechanisms,
standards and controls **for data and artificial intelligence**. They contain no AI
obligation: no reference to machine learning, no reference to algorithms, no automated
decision-making provision, no model governance requirement, and no profiling
provision in the personal-data sense.

That is the position, not a gap in research. Every AI obligation in this policy
therefore reaches AI as an obligation about **data classification, personal data,
or data sharing**. Clauses 4, 6 and 9 are the three routes, and every clause in this
policy that goes further is labelled a house standard where it appears.

### 1.3 Classification is the gate, and it is not optional

Data is classified on creation or receipt, by an impact assessment, into four levels.
Where a dataset combines levels, **the highest level governs the whole**. Classification
determines who may handle the data, how it is protected, and - for the purposes of this
policy - **whether it may be placed in an AI tool at all**. Clause 4 is the operational
spine of this document.

### 1.4 Security is deliberately not specified here

The Data Security and Protection domain of the standards sets out controls but **no
specifications**. Both the specifications and the compliance assessment for that domain
are the mandate of the National Cybersecurity Authority, and are expressly excluded
from the annual data management compliance assessment. One classification
specification likewise carries no priority of its own and is left to that authority.

**[ENTITY] therefore cannot derive its AI security controls from the instruments behind
this policy**, and this policy does not pretend otherwise. Clause 13 states the
controls [ENTITY] applies as house standards and directs the reader to the cybersecurity
authority's own requirements, which this policy does not reproduce.

## 2. Scope

This policy applies to all employees, contractors, secondees, temporary staff and third
parties who use [ENTITY] systems, data or accounts. It covers all AI tools, including
public and generative AI services, AI features embedded in other software, coding
assistants, meeting and note-taking assistants, media generators, AI agents, and
internal AI systems. It applies on entity devices and accounts, and on personal devices
or accounts whenever used for [ENTITY] work or data.

It covers all data received, produced or managed by [ENTITY] regardless of source, form
or nature - including paper records, meetings, communications through social media and
applications, emails, information stored on electronic media, audio and video
recordings, maps, photographs and handwritten documents. **A photograph of a screen is
within scope. So is a meeting transcribed by an assistant.**

Compliance is mandatory. Breaches may result in disciplinary action up to and including
termination.

### 2.1 Roles this policy assumes

[ENTITY] identifies and appoints, with responsibilities set out in job descriptions:
a **Chief Data Officer**; a **Compliance Officer** to audit and monitor the data
agenda; a **Personal Data Protection Officer**; **Business Data Executives** and
**Business Data Stewards** for each domain; and **IT Data Stewards**. This policy
allocates AI responsibilities to those existing roles rather than creating new ones -
clause 21.

Where [ENTITY] handles personal data, it acts as **data controller** or **data
processor** as the case may be. An AI supplier processing government data on [ENTITY]'s
behalf does not thereby become responsible for it.

## 3. Approved tools

3.1 Only AI tools on the [ENTITY] Approved AI Tools list may be used with [ENTITY] data
of any classification above Public, or with any personal data.

3.2 A tool is added to the list only after: an impact assessment against the
classification levels it will handle; a personal data assessment where personal data is
involved; a review against the cybersecurity authority's requirements; and, where
government data will leave [ENTITY], **a data sharing agreement** meeting clause 9.

3.3 Use of any tool not on the list - including free or personal-account versions of
listed tools - is not permitted for [ENTITY] work or data.

3.4 Staff who need a tool that is not listed must request it through [FORM / CHANNEL];
requests are assessed within [N] business days.

3.5 Staff already using an unapproved tool must disclose this to the policy owner.
Good-faith disclosure will not of itself be treated as a disciplinary matter.

3.6 The approved list records, for each tool, the **highest classification level** it is
approved for and whether it is approved for personal data. Those two facts are the
first thing a member of staff checks.

## 4. Classification and AI - what may be placed where

**This is the operational core of the policy.**

### 4.1 The principles that govern classification

- **Open by default** in the development sector, unless nature or sensitivity requires
  higher classification and protection; **top secret by default** in the political and
  security sectors, unless nature or sensitivity requires lower.
- **Necessity and proportionality** - classification reflects nature, sensitivity and
  impact, balancing value against confidentiality.
- **Timely classification** - on creation, or on receipt from another entity, and
  time-bound.
- **Highest level of protection** - where an integrated dataset carries different
  levels, **the highest level is applied to the whole**.
- **Segregation of duties** across classification, access, disclosure, use,
  modification and destruction.
- **Need to know** - access and use for the least possible number of people.
- **Least privilege** - access limited to what the role requires.

The fourth principle is the one AI use breaks most easily. **Assembling a corpus,
building an index, or pasting several documents into one prompt creates an integrated
dataset**, and it takes the classification of its most sensitive component. A prompt
combining Public and Restricted material is Restricted.

### 4.2 The levels

| Level | Impact | Use in AI tools |
|---|---|---|
| **Top Secret** | High | **Never.** No AI tool, internal or external, under any exception |
| **Secret** | Medium | **Never in an external tool.** Internal systems only, with written approval of the Chief Data Officer and the entity's security function |
| **Restricted** | Low | Approved tools only, at the approved classification level, with the controls in clauses 6, 9 and 13. Sub-category is recorded |
| **Public** | None | Approved tools. Ordinary care applies |

Restricted data carries a sub-category by the scale of impact: **Category (A)** where
impact is at the scale of an entire sector or general economic activity; **Category (B)**
where it cuts across multiple entities or the interests of a group of individuals;
**Category (C)** where it relates to a single entity or a specific individual. The
sub-category is recorded in the AI system inventory and informs the approval decision.

The mapping of levels to AI use in the right-hand column is a **house standard**. The
instruments classify data and require handling controls proportionate to
classification; they do not name AI tools. [ENTITY] adopts this mapping because an
external AI service is a disclosure outside [ENTITY]'s control, and because the impact
definitions for the two highest levels describe consequences that cannot be accepted
for productivity gain.

### 4.3 Practical rules

4.3.1 **Classify before you prompt.** If you cannot state the classification of what you
are about to enter, do not enter it.

4.3.2 Every entity conducts its own impact assessment of unauthorised access or
disclosure. Where a classification is uncertain, treat it at the higher level until the
Business Data Steward determines it.

4.3.3 AI output derived from classified input carries at least the classification of
that input. **A summary of a Restricted document is Restricted.**

4.3.4 Handling and protection controls are assigned to datasets and artefacts by
classification, to secure their handling, processing, sharing and disposal, following
the cybersecurity authority's requirements. Those requirements are not reproduced here.

4.3.5 Classification is reviewed, and AI outputs stored as artefacts are classified and
catalogued like any other artefact.

## 5. Levels of use

**Level 1 - Open.** Public data only, no personal data. Approved tools.

**Level 2 - Internal.** Restricted data, no personal data. Approved tools at the
approved level, recorded in the AI system inventory.

**Level 3 - Personal data.** Any personal data. Everything at Level 2, plus the
requirements of clause 6, and inclusion in the personal data register.

**Level 4 - Consequential.** AI output that materially informs a decision about a
person, or that concerns Restricted Category (A) or (B) data. Everything at Level 3,
plus clauses 10 and 11, and approval by the Data Governance Committee.

Where a use sits between two levels, the higher level applies. Secret and Top Secret
data sit outside this scheme entirely - clause 4.2.

## 6. Personal data

The instruments place five controls on personal data protection: a plan, training,
breach handling, lifecycle management, and a register. Each has a consequence for AI
use.

### 6.1 Assessment and plan

6.1.1 [ENTITY] performs an initial personal data protection assessment covering, at
minimum: the **types of personal data collected**; the **location and method of
storage**; the **current processing and uses**; and the privacy challenges to meeting
the applicable personal data protection regulations.

6.1.2 **Introducing an AI tool changes all four.** A new tool is not added to the
approved list until the assessment has been updated to reflect the personal data it will
receive, where that data will be stored, and how it will be processed.

6.1.3 [ENTITY] maintains a personal data protection plan with a roadmap, milestones,
and assigned resources and budget for achieving and maintaining compliance. AI
readiness items sit in that plan and not in a separate one.

### 6.2 Notice and consent

6.2.1 [ENTITY] defines and documents its processes for giving individuals notice and
requesting consent **at all points along the data lifecycle where personal data is
collected**.

6.2.2 [ENTITY] provides all possible options to the individual and obtains their
approval, implicit or explicit, regarding the collection, use or disclosure of their
personal data.

6.2.3 A privacy notice is documented and made available for individuals to review
**before or at the time** permission is requested. Where [ENTITY] maintains an internet
presence, a hyperlink to the notice is maintained, and the notice must be available for
inspection by the national data management authority on request.

6.2.4 **Placing personal data into an AI tool is a use, and where the tool is external
it is also a disclosure.** If the notice does not cover it, the notice is updated
before the tool is used - not after.

### 6.3 Individuals' rights

6.3.1 [ENTITY] establishes and documents rights management processes supporting the
individual's:

- right to be informed;
- right of access;
- right to rectification;
- right to erasure;
- right to object;
- right to restrict processing;
- right to data portability.

6.3.2 [ENTITY] informs individuals about these rights and provides the means by which
requests are **submitted, responded to and tracked**.

6.3.3 **A request reaches AI systems.** Prompts, uploads, transcripts, embeddings,
inferred attributes and logs are within scope where they contain the individual's
personal data. A tool from which personal data cannot be located, retrieved, corrected,
erased, restricted or exported on request **is not approved for personal data**.

6.3.4 The right to restrict processing and the right to object are the two most often
overlooked in AI systems, because they require the system to continue holding data
while ceasing to use it. A tool that can only delete, and cannot suspend, cannot
satisfy them.

### 6.4 Annual risk assessment

6.4.1 [ENTITY] conducts **yearly risk assessments** of the operation and use of its
information systems containing personal data - including collection, processing,
storage and transmission - **whether automated or manual**.

6.4.2 **AI systems containing personal data are within this, without needing an
AI-specific provision to bring them in.** The words "whether automated or manual" are
what carry them, and no separate AI assessment regime is asserted by this policy.

6.4.3 Findings are, at minimum, documented; analysed for impact and likelihood of
occurrence; and evaluated against current regulatory obligations and criticality to
resolve.

6.4.4 A finding that identifies a measure is not closed until the measure is
implemented and the implementation is dated. This is a house standard and clause 11.4
carries it into the annex's register.

### 6.5 Compliance monitoring and audit

6.5.1 [ENTITY] conducts internal audits to monitor compliance with privacy
requirements and documents its findings in a report presented to the **Personal Data
Protection Officer**. Where non-compliance is found, corrective action is taken with
notification to the regulatory authority and the national data management authority,
and is documented in the audit findings report.

6.5.2 The AI system inventory and the records required by this policy are within the
scope of that audit.

### 6.6 Training

6.6.1 [ENTITY] conducts personal data protection training **for every employee**,
covering at minimum: the importance of personal data protection and the consequences
to [ENTITY] and the individual; the definition of personal data; individuals' rights;
[ENTITY] and individual responsibilities; and notification - when [ENTITY] or the
individual should be notified, and how to handle inquiries about collection, processing
and sharing.

6.6.2 The AI module at clause 23 is delivered as part of that training, not separately
from it.

### 6.7 The register

6.7.1 [ENTITY] documents in a register its compliance records for **not less than 24
months**, and makes them available on request by the national data management
authority. The register includes, at minimum, a record of **any collection and/or
processing of any personal data**.

6.7.2 **Processing personal data through an AI tool is processing, and it goes in the
register.** The entry records what data, for what purpose, through which tool, under
what agreement, and who authorised it.

6.7.3 Twenty-four months is a floor. Records supporting an AI approval are retained for
the life of the approval and for 24 months afterwards.

## 7. Prohibited by [ENTITY]

7.1 Placing **Top Secret** data in any AI tool. **No exception.**

7.2 Placing **Secret** data in any external AI tool. **No exception.**

7.3 Placing government data of any classification above Public into a tool not on the
approved list.

7.4 Placing personal data into any tool not approved for personal data.

7.5 Entering credentials, keys, secrets or security configuration into any AI tool.

7.6 Using AI output as the sole basis for a Level 4 decision, without the human
determination at clause 10.

7.7 Combining datasets in a prompt, index or corpus without reclassifying the result at
the highest level present.

7.8 Re-identifying, or attempting to re-identify, data that has been masked, anonymised
or aggregated, without written authorisation from the Personal Data Protection Officer.

7.9 Sharing government data with an AI supplier outside a data sharing agreement
meeting clause 9.

7.10 Using AI to covertly monitor, profile or score employees.

7.11 Bypassing, disabling or circumventing a control in this policy.

7.12 Using AI to produce material that is unlawful, defamatory, harassing or
discriminatory.

No exception may be granted against 7.1, 7.2, 7.7 or 7.11.

## 8. Ethical use

8.1 All parties to a data sharing arrangement must adhere to ethical principles, to
ensure **responsibility, fairness, integrity and trust** in data use.

8.2 [ENTITY] treats that requirement as reaching AI use directly, and gives it the
following content as a house standard: a system whose behaviour cannot be explained is
not trustworthy; a system that has not been tested for unjustified differences in
outcome cannot be said to be fair; and a system operated without a named accountable
owner is not operated responsibly.

8.3 Clause 20 sets out what [ENTITY] does about fairness in practice. That content is
[ENTITY]'s own; the ethical use requirement supplies the obligation, not the method.

## 9. Sharing government data with an AI supplier

**Sending government data to a commercial AI service is a data sharing event with a
non-government data requester. It is governed as one.**

9.1 Data sharing is conducted for **legitimate purposes** grounded in a legal basis or
justified operational need, and must not compromise national interests, the operations
of entities, individual privacy or environmental safety. **The recipient may use the
data solely for the purposes specified in the request.**

9.2 A **data sharing agreement** is required. Before any government data reaches an AI
supplier, the agreement establishes:

- the **legal basis** and the purpose;
- the **authorisation**, granted on need to know and least privilege, with
  identification and verification of authorised personnel appropriate to the data's
  nature, classification and sensitivity;
- the **data type**, described clearly, with its classification levels stated;
- **pre-processing** - whether the data should be masked, anonymised or aggregated
  before sharing, and by what method, provided the processing does not affect content;
- the **means of sharing**, and the security and reliability of the channel;
- **retention periods and the destruction mechanism** on fulfilment of the purpose;
- **use and protection after sharing**, with controls implemented according to
  classification, and appropriate **restrictions on permitted use or processing - such
  as processing constraints, territorial or time limitations, or exclusive and
  commercial rights**;
- **[ENTITY]'s rights**, including to conduct audits and reviews, and its rights against
  any third party benefiting from the data;
- **dispute resolution**;
- whether **a third party will derive benefit** from the shared data, and the mechanism
  governing that beneficiary;
- **duration, frequency and termination**, including a deadline for access or storage,
  review and modification requirements, and the measures on termination - such as
  de-identification, revocation of access, or destruction;
- who may terminate early, on what grounds, and with what notice; and
- **liability**.

9.3 Four of those bear directly on AI supply and are where a standard vendor contract
usually fails:

- **Purpose limitation.** A supplier term permitting use of input to improve the
  supplier's models is a use beyond the specified purpose. It is not accepted.
- **Territorial limitation.** The agreement may impose territorial limits on processing.
  Where it does, the supplier's actual processing and storage locations must be
  established, recorded, and monitored for change.
- **Third-party benefit.** Sub-processors, model providers behind a reseller, and
  analytics partners are third parties deriving benefit. They are ascertained and
  governed, not discovered later.
- **Destruction on termination.** The mechanism is specified in advance and evidenced on
  exit, and covers prompts, logs, embeddings, caches and backups.

9.4 **Pre-processing is considered before every sharing, not after a problem.** Where
masking, anonymisation or aggregation would serve the purpose, the data is shared in
that form. Where it would not, the reason is recorded.

9.5 **Transparency.** All necessary information about the sharing is available to all
parties: a clear description of the data, its classification levels, the collection
purpose, storage methods, protection controls and destruction mechanism.

9.6 **Collective accountability.** The parties are collectively accountable for sharing
decisions, consistent with the roles set out in the agreement, to ensure data is
processed in alignment with the specified purposes. **This does not move [ENTITY]'s own
accountability to the supplier.**

9.7 Data minimisation applies: only the minimum data required to fulfil the purpose is
shared, retained for no longer than the purpose requires.

## 10. Automated decisions about people

**These are house standards.** The instruments behind this policy contain no
automated-decision provision. [ENTITY] imposes the following because a decision about a
person that cannot be accounted for cannot be defended to that person, to an auditor,
or to the regulatory authority.

10.1 No Level 4 decision is made solely by an AI system. A named person reviews the
output, has the authority and the information to reach a different conclusion, and
records the determination as their own.

10.2 A review that only ratifies the output is not a review. The reviewer must be able
to state what the decision rests on and what would have changed it.

10.3 For each Level 4 use, [ENTITY] records before deployment: the decision the system
informs; the data it uses and its classification; the tested performance and known
limitations; the groups on which performance was checked; the point of human
determination; and the route by which a person can contest the outcome.

10.4 An individual affected by a Level 4 decision is told, on request, that an AI system
was used, in general terms what it considered, and how to contest the outcome. The
right to object and the right to restrict processing at clause 6.3 remain available.

10.5 Where a decision is contested, a person not involved in the original decision
reviews it. The review and its result are recorded.

## 11. Assessment discipline

11.1 Three assessments bear on AI at [ENTITY], and they are distinct: the **impact
assessment** that sets a classification level; the **personal data protection
assessment** and its annual refresh; and the **yearly risk assessment** of information
systems containing personal data.

11.2 An AI system at Level 3 or Level 4 has all three. The AI system inventory records
the date of each and the person accountable for it.

11.3 An assessment conducted after the processing has begun is remediation. It is
labelled as such and reported to the Data Governance Committee.

11.4 **An assessment that identifies a measure and does not implement it is not a
completed assessment.** Every identified measure carries an implementation date.

## 12. Verification of output

12.1 AI output is a draft. The person who uses it is accountable for it.

12.2 Any factual claim, figure, calculation, date, quotation, citation or regulatory
reference taken from AI output and relied on externally, or in a decision, must be
verified against a primary source before use.

12.3 Code generated by AI is reviewed before merge, on the same basis as human-authored
code, with attention to secrets, licence terms, and dependencies the model has
introduced.

12.4 AI-generated citations are verified to exist and to say what they are said to say.
This is the most common single failure of generative tools.

12.5 Output that will be published, shared with another entity, or made open must be
verified and classified before release. **Publication is a classification decision, not
a formatting one.**

## 13. Security

13.1 **The security specifications for data are the mandate of the National
Cybersecurity Authority and are not set out in the instruments behind this policy.**
This clause states what [ENTITY] applies as a house standard. It does not reproduce,
summarise or assert that authority's requirements, and it does not displace them. Where
they differ, they govern.

13.2 AI tools are accessed through [ENTITY] accounts with single sign-on and
multi-factor authentication. Personal accounts must not be used for [ENTITY] work.

13.3 Access is granted on **need to know** and **least privilege** and reviewed
[quarterly]. Leavers are removed on the day of departure.

13.4 **Segregation of duties** is preserved: the person who classifies data, the person
who authorises its use in a tool, and the person who audits that use are not the same
person.

13.5 Access to AI systems handling data above Public is logged, and the logs are
retained and reviewed.

13.6 Content received from outside [ENTITY] - documents, emails, web pages, supplier
files - is treated as untrusted input when placed in front of an AI system, including
any instruction embedded within it.

13.7 Third-party supplier security obligations are reflected in the engagement of every
AI supplier, in accordance with the cybersecurity authority's requirements.

## 14. Personal data breach

14.1 Any suspected breach involving an AI tool - a wrong recipient, an unapproved tool,
an exposed prompt log, a misconfigured index, a supplier notification - is reported to
[SECURITY CONTACT] and to the Personal Data Protection Officer **immediately on
suspicion**, not after internal investigation.

14.2 Where it is determined that personal data has been compromised, [ENTITY] as data
controller or data processor **notifies the regulatory authority within 72 hours**.

14.3 [ENTITY] maintains a documented breach management process setting out functions
and responsibilities for the affected team, including the cases in which the regulatory
authority is notified once a breach has been identified. The process covers, at minimum:

- conducting an **incident review with the regulatory authority**;
- formulating an **immediate response** by the controller and, where relevant, the
  processor;
- implementing **permanent corrective actions when issued by the regulatory authority**;
  and
- **testing the implemented corrective actions** to validate the personal data
  protection solutions.

14.4 The third and fourth items are the ones organisations forget. **Corrective actions
issued by the authority are implemented and then tested**, and the test result is
recorded. Closing an incident without that step does not close it.

14.5 For each Level 3 and Level 4 AI system, [ENTITY] records in advance how it would
establish, from the system's own records, whose personal data a given exposure touched.
A system that cannot answer that is not approved for personal data.

14.6 Supplier agreements require immediate notification to [ENTITY] on the supplier
becoming aware of a compromise, with enough detail to meet 14.2 within the period.

14.7 A breach involving data classified above Public is escalated to the Chief Data
Officer the same day, whether or not personal data is involved.

14.8 Staff who report in good faith will not face disciplinary action for reporting.

## 15. Data lifecycle, storage and retention

15.1 [ENTITY] maintains a storage and retention policy for the data lifecycle covering,
at minimum: storage conditions protecting data in the event of disaster; **retention
periods based on data type, classification, business value and legal requirements**;
**disposal and destruction rules based on data type and classification**; and the
actions required on accidental permanent loss of data.

15.1a Data handled by AI tools sits inside that policy, not beside it. **Retention and
destruction for an AI system are set by the classification of the data it holds**, which
is why the AI system inventory records the classification and the retention position
together.

15.2 Retention is assessed across the whole AI footprint: prompts and completions;
uploaded files; vector embeddings and indexes; caches; session transcripts;
supplier-side logs; and any copy in a monitoring, analytics or support system.

15.3 Where data has been shared with a supplier, the retention period and destruction
mechanism agreed under clause 9.2 govern, and destruction is evidenced rather than
asserted.

15.4 The personal data register at clause 6.7 is retained for not less than 24 months
irrespective of the retention applied to the underlying data.

## 16. Open data and freedom of information

16.1 AI output is not published as open data without classification, verification under
clause 12, and the approval that any other open data release requires.

16.2 Where [ENTITY] receives a request for information, AI-generated material held by
[ENTITY] is within the scope of the search like any other record. **A prompt log is a
record.**

16.3 AI must not be used to answer a request for information without a named officer
verifying the response and its classification before it is sent.

## 17. Business intelligence and analytics

17.1 Where AI is used for analysis rather than drafting, the data requested must be the
minimum required, and the analysis must be conducted on data obtained through the
proper sharing route.

17.2 Where data is requested from another entity for analytical purposes, it is
requested in the form appropriate to analysis - aggregated or de-identified where that
serves the purpose.

17.3 Insight derived from classified data carries the classification of the source
until a fresh impact assessment says otherwise.

## 18. Intellectual property, transparency and records

18.1 AI-generated material used externally is reviewed for third-party rights before
publication.

18.2 [ENTITY] data must not be placed in tools whose terms grant the supplier rights
over input or output beyond what the sharing agreement permits.

18.3 Where AI has made a material contribution to a deliverable shared outside
[ENTITY], that is disclosed where the recipient would reasonably expect to know.

18.4 Records supporting compliance - classifications, assessments, approvals, sharing
agreements, verification records, register entries and breach records - are retained
for [PERIOD] and never less than 24 months, and are producible on request.

## 19. Public-facing AI

19.1 A public-facing AI system requires approval by the Data Governance Committee
before launch.

19.2 [ENTITY] discloses that a person is interacting with an AI system rather than a
human being. This is a house standard.

19.3 A route to a human is available and is not made deliberately difficult to find.

19.4 What the system may commit [ENTITY] to is bounded and documented. Where it cannot
answer, it says so rather than producing a plausible answer.

19.5 Where the system collects personal data, the notice at clause 6.2 is presented in
the flow, before or at the time approval is requested.

## 20. Fairness

20.1 AI systems used in decisions about people must not produce unjustified differences
in outcome between groups. [ENTITY] adopts this under the ethical use requirement at
clause 8; the content of the standard is [ENTITY]'s own.

20.2 Level 4 systems are tested before deployment and at least [annually] for disparate
outcomes across the groups relevant to the decision, and the results are recorded and
fed into the yearly risk assessment at clause 6.4.

20.3 Where a difference is found and cannot be justified, the system is not deployed, or
is withdrawn.

## 21. Responsibilities

**All staff** - classify before you prompt; use approved tools only at the approved
classification level; verify output; report suspected breaches immediately; complete
the required training.

**Business Data Stewards** - classify data in their domain; determine uncertain
classifications; approve the classification level recorded for each AI use in their
area.

**Business Data Executives** - own the AI uses within their domain and their entries in
the inventory and the register.

**IT Data Stewards** - implement handling and protection controls by classification;
maintain access, logging and retention configuration for AI systems.

**Personal Data Protection Officer** - the personal data assessment and plan, notice and
consent, individuals' rights, the yearly risk assessment, the register, breach
notification, and the internal privacy audit.

**Compliance Officer** - audits and monitors the data agenda, including AI use, and
prepares [ENTITY]'s input to the annual compliance assessment.

**Chief Data Officer** - owns this policy, leads the annual compliance exercise, and
approves internal use of Secret data in AI systems.

**Data Governance Committee** - Level 4 approvals, public-facing systems, exceptions,
metrics, and regulatory change.

## 22. What this policy does not state, and why

**This policy rests on the national data management, classification and data sharing
instruments. The Kingdom's personal data protection legislation and its implementing
regulations are not held by [ENTITY] in the form used to write this document.**

The instruments this policy does rest on repeatedly direct the reader to those
regulations for more detailed requirements - on notice and consent, on individuals'
rights, on breach notification, on the compliance register, and on the personal data
protection plan. **This policy states what the standards themselves require and stops
where they point elsewhere.**

It therefore does not state:

- the statutory definition of personal data, or of sensitive personal data;
- the lawful bases for processing;
- the detailed requirements for notice, consent and the exercise of rights that the
  regulations supply;
- the conditions and mechanisms for transferring personal data outside the Kingdom;
- the detailed breach notification requirements beyond the 72-hour period the standards
  state;
- any penalty for contravention;
- **any data security specification**, which is the mandate of the National
  Cybersecurity Authority - clause 1.4 and 13.1.

It also does not govern an organisation's processing of its own commercial personal
data where no government data is involved - clause 1.1.

The accompanying research note lists every point at which the standards refer to a
document [ENTITY] does not hold, so that the gap is legible and can be closed.

## 23. Knowledge, skills and acknowledgement

23.1 Staff who use AI tools with [ENTITY] data complete training covering this policy,
**the classification rules at clause 4**, the personal data requirements at clause 6,
and the breach duties at clause 14, before access is granted and at least [annually]
thereafter. It is delivered within the personal data protection training at clause 6.6.

23.2 Staff who make or inform Level 4 decisions complete additional training on the
limits of AI output and on the determination required at clause 10.

23.3 Staff acknowledge this policy on joining, on material revision, and at least
annually.

23.4 Questions go to [CONTACT]. Asking before acting is always acceptable.

---

**Version history:**
1.0 - initial policy, published 2 September 2026; verified within its stated
scope (government data) per the research note and source register.

---

*This document is an educational policy template and does not constitute legal advice.
It reflects obligations under the national data management, classification and data
sharing instruments as set out in the accompanying research note, applies to government
data only, and must be reviewed by the Personal Data Protection Officer or qualified
legal counsel before adoption.*
