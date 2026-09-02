# Research note - Saudi Arabia AI policy set

Working note supporting the [ENTITY] Artificial Intelligence Acceptable Use Policy
(Saudi Arabia) v1.0 and the AI Governance Enterprise Annex (Saudi Arabia) v1.0.

**Control, specification and clause identifiers live here, not in the policy or the
annex.** This is where a reader can check what each clause rests on, and where the
limits of the set are stated.

State as at 31 August 2026.

---

## 1. What this set rests on

| # | Instrument | Version | Issuer |
|---|---|---|---|
| 1 | **National Data Management and Personal Data Protection Standards** | Cover states **Version 1.5, January 2021**; the internal document-control table records v1.4 and v1.5 both at June 2021. 173 pp | National Data Management Office (NDMO) |
| 2 | **National Data Governance Policies - Data Classification Policy** | **Version 1, 5/5/2020**. 28 pp | NDMO |
| 3 | **Data Sharing Policy** | **Version 2.0, 2024**. 21 pp | NDMO |

The version inconsistency at row 1 is recorded in the source register rather than
resolved; it does not affect any provision relied on.

## 2. The scope finding - stated first because it governs everything else

**These instruments apply to public entities and to business partners handling
government data. They do not govern a private organisation's processing of its own
customers' or employees' personal data.**

The evidence is explicit and in three places.

**Standards, section 3 (Purpose and Scope):** the standards "are intended to be adopted
by all Public Entities within the Kingdom", and "In addition to Public Entities, the
scope of the National Data Management and Personal Data Protection Standards also
extends to business partners handling government data. Such business partners are
responsible to understand and apply the Data Management and Personal Data Protection
standards to all government data assets within their control and custody." The standards
"apply to all government data regardless of form or type".

**Standards, section 1 (Definitions):** "Business Partners - Entities engaged in
producing, managing, or overseeing government data".

**Data Classification Policy, clause 1.1 (Scope):** the policy applies "to all data
received, produced, or managed by public entities regardless of its source, form, or
nature".

**Data Sharing Policy, clause First (Scope):** the policy governs "the sharing of
government entity data with Data Requesters".

**Consequence.** The policy and annex are titled and scoped to government data, and
policy Section 1.1 and annex A13 say so in the documents themselves. A general
private-sector AI acceptable use policy for the Kingdom would rest on the personal data
protection legislation and its implementing regulations, which are not held - see
section 7.

This is the single most important thing to understand about this set, and it is stated
in the first paragraph a reader encounters rather than buried in a register.

## 3. There is no AI provision in any of the three instruments

The standards were developed pursuant to a directive of the Saudi Authority for Data and
Artificial Intelligence, under Cabinet Resolution number 292 of 27/04/1441H, directing
NDMO "to develop and implement policies, governance mechanisms, standards and controls
for **data and artificial intelligence** and monitor compliance upon publication"
(standards, section 3).

**The standards nonetheless contain no artificial intelligence obligation.** A full-text
search of all three instruments returns:

| Term | Standards | Data Sharing Policy | Data Classification Policy |
|---|---|---|---|
| "artificial intelligence" | 2 - both the issuing authority's name and the mandate quoted above | 0 | 0 |
| "machine learning" | 0 | 0 | 0 |
| "algorithm" | 0 | 0 | 0 |
| "profiling" | 2 - both **data quality profiling** (statistical analysis of data attributes), not profiling of individuals | 0 | 0 |
| "automated" | 27 - all referring to automated tooling and workflows (automated data catalogue tools, automated data sharing between entities), none to automated decision-making | 5 - automated data sharing channels | 0 |

There is no risk classification of systems, no model governance requirement, no
automated-decision provision, and no conformity assessment.

Every AI obligation in this set therefore reaches AI through one of three existing
routes: **data classification**, **personal data protection**, or **data sharing**.
Policy 1.2 states this, and Sections 4, 6 and 9 of the policy are those three routes.

## 4. The security carve-out

**Standards, section 9.15 (Data Security and Protection Domain)** carries eleven
controls and **no specifications**. Its introductory note states that the National
Cybersecurity Authority "is the government entity in charge of cybersecurity in Saudi
Arabia", serves as the national authority "both from a regulatory and operational
perspective", and that "the controls and corresponding specifications for the Data
Security and Protection Domain will be detailed and addressed by NCA". It adds:
"Compliance to the Data Security and Protection controls will be conducted by NCA, as
per their requirements and methodology, **and not as part of NDMO's annual Data
Management and Personal Data Protection compliance assessment**."

The eleven control names are given without specifications: Information Security
Governance; Information Security Architecture; Information Systems Design, Development
and Testing; Identity and Access Management; Third Party Supplier Security; Information
Security Training, Awareness and Communication; Information Asset Management;
Information Security Operations Management; Information Security Incident Management;
Information Security Risk Management; Information Systems Continuity Management.

**The carve-out reaches into another domain.** Specification **DC.2.1 (Security
Controls)**, in the Data Classification domain, requires the entity to "assign data
handling and protection controls to datasets and artifacts based on their classification
to ensure secure handling, processing, sharing and disposal of data by following the
National Cybersecurity Authority regulations" - and its priority field reads **"As
specified by NCA"** rather than P1, P2 or P3.

**Consequence.** [ENTITY] cannot derive AI security controls from these instruments.
Policy 1.4 and 13.1 say so, state what [ENTITY] applies as house standards, and direct
the reader to the cybersecurity authority's own requirements without reproducing,
summarising or asserting them. **No NCA instrument is held by this set.**

## 5. The findings worth recording

### 5.1 Classification is the gate, and integrated datasets are where AI breaks it

**Data Classification Policy, clause 1.2** sets seven principles:

1. **Open by Default** - data shall primarily be accessible in the development sector
   unless nature or sensitivity requires higher classification, and top secret in the
   political and security sectors unless nature or sensitivity requires lower.
2. **Necessity and Proportionality** - classification by nature, sensitivity and impact,
   balancing value against confidentiality level.
3. **Timely Classification** - on creation or on receipt from another entity;
   time-bound.
4. **Highest Level of Protection** - "If information includes an integrated dataset with
   different classification levels, the highest classification level shall be approved."
5. **Segregation of Duties** across classification, access, disclosure, use,
   modification and destruction.
6. **Need to Know** - for the least possible number of people.
7. **Least Privilege**.

**Clause 1.3** sets four levels against impact:

| Level | Impact | Test |
|---|---|---|
| **Top Secret** | High | Unauthorised access or disclosure has an **exceptionally serious and irreparable** effect on national interests and the other listed matters |
| **Secret** | Medium | |
| **Restricted** | Low | |
| **Public** | None | |

Restricted is further sub-classified: **Category (A)** where the impact is at the scale
of an entire sector or a general economic activity; **Category (B)** where it cuts
across the activities of multiple entities or the interests of a group of individuals;
**Category (C)** where it relates to the activity of a single entity or the interests of
a specific individual.

The policy adds that every entity conducts its own impact assessment of unauthorised
access or disclosure, and that the illustrative impact table is non-exhaustive.

**Principle 4 is the one AI use breaks.** Building a retrieval corpus, an index, or a
fine-tuning dataset, or pasting several documents into one prompt, creates an integrated
dataset that takes the classification of its most sensitive component. Policy 4.1 and
4.3.3 state it; annex A3.2 requires the composition and resulting classification to be
determined **before** assembly, and A8.5 extends it to agents that assemble context at
run time.

**The mapping of the four levels to AI use in policy 4.2 is a house standard**, and the
policy says so in the paragraph immediately beneath the table. The instruments classify
data and require handling controls proportionate to classification; they do not mention
AI tools.

### 5.2 The Personal Data Protection domain - five controls, ten specifications

**Standards, section 9.14.** The domain "focuses on protection of a subject's entitlement
to the proper handling and non-disclosure of their personal information".

| ID | Control | Specifications | Priority |
|---|---|---|---|
| **PDP.1** | Plan | PDP.1.1 Personal Data Protection Initial Assessment; PDP.1.2 Personal Data Protection Plan | P1, P1 |
| **PDP.2** | Training and Awareness | PDP.2.1 Personal Data Protection Training | P1 |
| **PDP.3** | Data Breach | PDP.3.1 Data Breach Notification; PDP.3.2 Data Breach Management Process | P2, P1 |
| **PDP.4** | Data Lifecycle Management | PDP.4.1 Privacy Notice and Consent Management; PDP.4.2 Data Subject Rights; PDP.4.3 Personal Data Protection Risk Assessments; PDP.4.4 Compliance Monitoring and Audit | P2, P2, P3, P2 |
| **PDP.5** | Artifacts | PDP.5.1 Personal Data Protection Register | P2 |

**PDP.1.1** requires an initial assessment covering at minimum: identification of the
types of personal data collected; location and method of storage; current processing and
uses; and privacy challenges to meeting compliance. Policy 6.1.1-6.1.2 makes the point
that **introducing an AI tool changes all four**.

**PDP.1.2** requires a plan addressing strategic and operational requirements, with a
roadmap of activities and key milestones and assigned resources and budget. Policy 6.1.3
and annex A4.2 keep AI readiness inside that plan.

**PDP.2.1** requires training **for every employee** covering at minimum five items: the
importance of personal data protection and the consequences to the entity and the data
subject; the definition of personal data; data subject rights; entity and data subject
responsibilities; and notification - when the entity or the data subject should be
notified, and how to handle inquiries about collection, processing and sharing. Policy
6.6 and 23.1 place the AI module inside it.

**PDP.4.1** requires the entity to define and document its processes for providing
notice and requesting consent **at all points along the data lifecycle where personal
data is collected**; to provide all possible options to the data subject and obtain his
implicit or explicit approval regarding collection, use or disclosure; to document and
make available a privacy notice for review **before or at the time** permission is
requested; and, where the controller maintains an internet presence, to maintain a
hyperlink to the notice, which must be available to NDMO for inspection on request.

Policy 6.2.4 draws the operational conclusion: **placing personal data into an AI tool
is a use, and where the tool is external it is also a disclosure** - so if the notice
does not cover it, the notice is updated before the tool is used.

**PDP.4.2** enumerates seven data subject rights: to be informed; of access; to
rectification; to erasure; to object; to restrict processing; to data portability. The
entity should inform data subjects of their rights and provide the means by which
requests are **submitted, responded to and tracked**.

**These seven are stated in the held instrument**, which is why policy 6.3 can enumerate
them. Policy 6.3.3 makes satisfying all seven a condition of approving a tool for
personal data, and 6.3.4 names the two that AI systems fail most often - **restriction
and objection, because both require the system to keep data while ceasing to use it.**

**PDP.4.3** requires **yearly risk assessments** of the operation and use of information
systems containing personal data, including collection and processing, and storage and
transmittal by each system - **"whether automated or manual"**. Findings must at minimum
be documented, analysed for impact and likelihood of occurrence, and evaluated against
current regulatory obligations and criticality to resolve.

**This is the provision that carries AI systems into the assessment regime**, and it does
so without any AI-specific language. Policy 6.4.2 says exactly that, and annex A4.3
requires the committee to confirm annually that every AI system handling personal data
appears in the assessment.

**PDP.4.4** requires internal audits monitoring compliance, documented in a report
presented to the **Data Protection Officer**, with corrective action on non-compliance
**notified to the Regulatory Authority and to NDMO** and documented in the findings
report. Annex A4.5 requires the committee to be told, the day such a notification is
made.

**PDP.5.1** requires compliance records to be documented in a register "for a reasonable
period of time, but **not less than 24 months**", made available on NDMO's request, and
including at minimum **a record of any collection and/or processing of any personal
data**. Policy 6.7.2 states the consequence: AI processing is processing, and it goes in
the register. Annex A5.4 specifies what the entry contains.

**Every PDP specification except PDP.4.3 directs the reader to "the National Data
Management Office's Personal Data Protection Regulations for more detailed
requirements". Those regulations are not held** - section 7.

**The domain's own reference list** names the NDMO Personal Data Protection Regulation,
the General Data Protection Regulation (2018) and the California Consumer Privacy Act
(2020). **Nothing in this set was taken from the second or third**, and their appearance
in a reference list does not make them law in the Kingdom.

### 5.3 Breach - 72 hours, and two steps organisations skip

**PDP.3.1** - "The Entity's Data Controller or Data Processor handling personal data
shall, in the event it is determined that personal data has been compromised, notify the
Regulatory Authority within the allotted timeframe specified within the National Data
Management Office's Personal Data Protection Regulations. **The allotted timeframe for
notification is 72 hours.**"

**PDP.3.2** - the entity shall develop and document breach management procedures
setting functions and responsibilities for the affected work team, including the cases
in which the Regulatory Authority is notified once a breach has been identified. The
process shall include at minimum:

1. conducting an **incident review by the Data Controller with the Regulatory
   Authority**;
2. formulating an **immediate response** by the controller and/or processor;
3. implementing the **permanent corrective actions when issued by the Regulatory
   Authority**;
4. **conducting testing of the implemented corrective actions** to validate the personal
   data protection solutions.

Items 3 and 4 are the ones that get skipped. Policy 14.4 and annex A9.4 make the
recorded corrective-action test result a condition of closing an incident, and A10.2
tracks incidents closed without one as a metric that should be zero.

Note that the trigger is "in the event it is determined that personal data has been
compromised" - a determination, not a threshold of harm or scale. The detailed
requirements sit in the regulations that are not held, so **this set states the 72 hours
and nothing further about the notification's contents or the notifiable threshold**.

### 5.4 Data sharing - the frame that fits AI suppliers

The Data Sharing Policy governs the sharing of government entity data with data
requesters, and defines a **Data Requester** as "The public or private entity or the
individual submitting a data-sharing request". **A commercial AI service receiving
government data is a non-government data requester.** Policy Section 9 is built on that
reading, and it is the most productive of the three routes.

**Clause Second - the eight principles:**

1. **Data Sharing Culture** - source entities share the data they produce to enhance
   utilisation and achieve integration among government entities.
2. **The Single Source of Truth (SSOT)** - collect once, reuse, reducing duplication and
   inconsistency.
3. **Legitimate Purpose** - sharing for legitimate purposes grounded in a legal basis or
   justified operational need; must not compromise national interests, entity
   operations, individual privacy or environmental safety; **the shared data shall be
   used by the Data Requester solely for the purposes specified in the request**.
4. **Authorized Access** - all parties authorised to access, obtain and use the data,
   through identification and verification of authorised personnel, contingent where
   necessary on the data's nature, classification and sensitivity level as outlined in
   the Data Classification Policy.
5. **Transparency** - all necessary information available to all parties: a clear
   description of the requested data, its classification levels, collection purpose,
   storage methods, protection controls and destruction mechanism.
6. **Collective Accountability** - all parties collectively accountable for sharing
   decisions, consistent with the roles in the agreement, to ensure data is processed in
   alignment with the specified purposes.
7. **Data Security** - appropriate security controls per the requirements and directives
   issued by the **National Cybersecurity Authority**.
8. **Ethical Data Use** - all parties shall adhere to ethical principles "to ensure
   **responsibility, fairness, integrity, and trust** in data use".

**Clause Fifth - what a data sharing agreement must settle.** The policy's eight
headings map almost exactly onto what an AI vendor contract has to get right:

| Heading | Requirement |
|---|---|
| 1. Legal Basis | The basis and purpose |
| 2. Authorization | Granted on **need to know and least privilege** when handling shared data |
| 3. Data Type | Clear description, classification stated |
| 4. Data Pre-processing | Determine whether pre-processing is needed before sharing and agree the method - **masking, anonymization, aggregation** - provided processing does not impact content; assess quality, validity and integrity |
| 5. Data Sharing Means | Secure and reliable channels; **agree retention periods and the destruction mechanism** on fulfilling the purpose |
| 6. Data Usage and Protection | Identify data protection requirements and implement controls **according to classification**; impose **appropriate restrictions on permitted use or processing - such as processing constraints, territorial or time limitations, or exclusive or commercial rights**; determine the sharing entity's rights **including to conduct audits and reviews** and against any third party benefiting; agree dispute resolution; **ascertain whether a third party will derive benefit** and agree the governing mechanism |
| 7. Duration, Frequency, Termination | A specific duration including a deadline for access or storage; frequency; review and modification requirements; measures on termination such as **de-identification, revocation of access, or destruction** |
| 8. Liability | Liability provisions |

Policy 9.2 reproduces this list as the agreement's contents, and 9.3 names the four
clauses at which a standard AI vendor contract usually fails: **purpose limitation**
(training on input is use beyond the specified purpose), **territorial limitation**,
**third-party benefit** (sub-processors, the model provider behind a reseller, analytics
partners), and **destruction on termination**. Annex A6.3 makes those four
non-negotiable.

**Ethical Data Use** is the only place in the three instruments where fairness appears as
an obligation. Policy 8 uses it as the hook for the fairness standard at Section 20, and
is explicit that the principle supplies the obligation while the method is [ENTITY]'s
own.

### 5.5 The compliance assessment is binary, and the result is published

**Standards, section 4 (Compliance and Enforcement):**

- Entities conduct a compliance audit **annually** and submit the report to NDMO
  **during the third quarter of each year**.
- **NDMO reviews and consolidates all entity reports and publishes to related
  stakeholders the annual compliance results at the entity, sector, and
  whole-of-government level.**
- Assessment is at the level of each specification, with **a binary value of either 100%
  for fully implemented or 0% for partially or not implemented**. Scores cascade to
  control, domain and overall entity level.
- The report must be **supported with evidence** for implementation of each
  specification where applicable.
- The exercise is **led by the Chief Data Officer**, supported by the other data
  management and personal data protection roles.
- **NDMO may conduct ad-hoc compliance audits** on selected entities to review and
  validate findings.

Three consequences the annex carries. **No partial credit** (A11.2). **The score is
published at entity level** (A11.3). And because ad-hoc audits follow from submitted
reports, **evidence is held in producible form throughout the year** (A11.4). A12.4 adds
that an exception bearing on a specification means that specification is not fully
implemented and scores zero.

### 5.6 The standards are fully phased in

**Standards, section 8.** The standards comprise **77 controls and 191 specifications**,
prioritised:

- **P1** - foundational; implemented by all adopting entities **in the first year** from
  release;
- **P2** - implemented **from the second year**;
- **P3** - implemented **from the third year**.

Section 8.2 sets the three-year roadmap: end of year 1 all P1; end of year 2 all P1 and
P2; end of year 3 all P1, P2 and P3.

**Priority counts across the fifteen domains: 76 P1, 98 P2, 16 P3 - totalling 190
against 191 specifications.** The reconciliation is not an error: **DC.2.1 carries the
priority "As specified by NCA"** rather than a numbered priority (section 4 above). One
specification, one carve-out, and the arithmetic closes.

Given a release date of June 2020 for the specifications' version 1.0 and a standards
version of 2021, **all three implementation years have elapsed**. Annex A11.6 states the
consequence: nothing in these standards is deferred, and **no AI approval may rest on a
specification not yet being due**. This is the opposite of the position under
instruments that commence in stages.

### 5.7 The role structure, and the manual that defines it

**Standards, DG.4 (Data Management Organization)** requires the entity to identify and
appoint each of the following, with responsibilities highlighted in a job description
and **aligned with the responsibilities defined in the "Organizational Manual" published
by NDMO**. Every specification in this control is **P1**:

| Role | Purpose as stated |
|---|---|
| **Chief Data Officer** | Appointed to lead the data management agenda; leads the annual compliance exercise (standards s.4) |
| **Data Stewards** and an **Open Data** role | Appointed under their own specifications in the same control |
| **Compliance Officer** | To audit and monitor the data management agenda |
| **Personal Data Protection Officer (PDPO)** | To support the personal data protection agenda |
| **Business Data Executive (BDE)** | To enable the data management agenda for their related domains |
| **Business Data Steward** | To enable the data management agenda for their related domains |
| **IT Data Steward** | To enable the data management agenda from an IT perspective |
| **Legal** role | Appointed under a further specification in the same control |

**A caution on citation.** The supplied PDF renders DG.4 as a multi-column table, and
extraction batches the specification identifiers separately from the role text, so
individual DG.4.x numbers cannot be matched to individual roles with confidence from the
extracted text. **This note therefore cites the control (DG.4) and not the
specification numbers.** The roles themselves, their stated purposes, their P1 priority
and the Organizational Manual reference are all read directly and are not in doubt.

Policy 2.1 and 21, and annex A1.2, allocate every AI responsibility to one of these
existing roles rather than inventing an AI governance role. **The Organizational Manual
that defines their responsibilities is not held** - annex A1.4 says so and provides that
where it differs, it governs.

### 5.8 Guiding principle: Data Protection by Design

**Standards, section 5** lists Data Management Guiding Principles mapped to domains. One
is **Data Protection by Design**: "Build systems and processes that are proactive in
protecting the privacy of individuals as well as their right to consent and/or refuse
under the applicable KSA laws", mapped to Personal Data Protection, Data Classification,
Data Security and Protection, and Open Data.

Another is **Data as a National Asset**: government data should be discoverable,
protected and maintained with clear accountability. **Open by Default** appears here too,
mapped to Open Data.

These are principles, not specifications, and nothing in this set is asserted on their
authority alone. They are recorded because "proactive" and "by design" are the language
in which annex A7.1 requires assessment before deployment rather than after.

## 6. Clause-by-clause basis

### 6.1 Policy

| Policy | Rests on |
|---|---|
| 1.1 - scope limit | Standards s.3; Standards s.1 (Business Partners); Classification Policy 1.1; Sharing Policy, Scope |
| 1.2 - no AI provision | The full-text search at section 3 of this note |
| 1.3 - classification is the gate | Classification Policy 1.2 principle 4, 1.3 |
| 1.4 - security carve-out | Standards s.9.15 note; DC.2.1 priority field |
| 2 - scope of data | Classification Policy 1.1; Sharing Policy, Scope cl.1 |
| 2.1 - roles | Standards DG.4 (Data Management Organization); s.4 (CDO leads the compliance exercise) |
| 3.2 - approval prerequisites | Classification Policy 1.3; PDP.1.1; Sharing Policy cl. Fifth |
| 4.1 - principles | Classification Policy 1.2 principles 1-7 |
| 4.2 - levels table | Classification Policy 1.3 and the Restricted sub-levels. **The right-hand column is a house standard, stated as such** |
| 4.3.2 - own impact assessment | Classification Policy 1.3, closing paragraph |
| 4.3.4 - handling controls | DC.2.1 |
| 5 - levels of use | House standard, built on Classification Policy 1.3 |
| 6.1 - assessment and plan | PDP.1.1, PDP.1.2 |
| 6.2 - notice and consent | PDP.4.1 items 1-4 |
| 6.3 - rights | PDP.4.2 |
| 6.4 - annual risk assessment | PDP.4.3 |
| 6.5 - audit | PDP.4.4 |
| 6.6 - training | PDP.2.1 items 1-5 |
| 6.7 - register | PDP.5.1 |
| 7 - prohibitions | House standards, built on Classification Policy 1.2-1.3 and Sharing Policy cl. Fifth |
| 8 - ethical use | Sharing Policy, Eighth Principle. **Content of 8.2 is a house standard** |
| 9.1 - legitimate purpose | Sharing Policy, Third Principle |
| 9.2 - agreement contents | Sharing Policy cl. Fifth, items 1-8 |
| 9.3 - the four failure points | House reading of cl. Fifth items 6 and 7 against the Third Principle |
| 9.4 - pre-processing | Sharing Policy cl. Fifth item 4.A |
| 9.5 - transparency | Sharing Policy, Fifth Principle |
| 9.6 - collective accountability | Sharing Policy, Sixth Principle |
| 9.7 - minimisation | Sharing Policy, Scope cl.3.B; cl. Fifth |
| 10 - automated decisions | House standards throughout, stated as such |
| 11 - assessment discipline | Classification Policy 1.3; PDP.1.1; PDP.4.3. 11.4 is a house standard |
| 12 - verification | House standards |
| 13 - security | **House standards. 13.1 states that the specifications are NCA's mandate.** 13.3-13.4 track Classification Policy 1.2 principles 5-7 |
| 14.2 - 72 hours | PDP.3.1 |
| 14.3 - breach process | PDP.3.2 items 1-4 |
| 14.5 - enumeration | House standard |
| 15 - retention | Standards **DO.2.1** (Storage and Retention Policy, P1); Sharing Policy cl. Fifth items 5.B and 7.B; PDP.5.1 for the 24 months |
| 16 - open data and FOI | Standards s.9.11, s.9.12 domains, as framing only. The clauses are house standards |
| 17 - BI and analytics | Standards s.9.9 domain; Sharing Policy general rules cl.13 (analytical purposes) |
| 18, 19, 20 | House standards, except 19.5 which rests on PDP.4.1 |
| 22 - what is not stated | Section 7 of this note |

### 6.2 Annex

| Annex | Rests on |
|---|---|
| A1.2 - roles | Standards DG.4 |
| A1.4 - manual not held | Standards DG.4 ("Organizational Manual" published by NDMO) |
| A2.1 - inventory fields | Classification Policy 1.3; PDP.1.1, PDP.5.1; Sharing Policy cl. Fifth |
| A3.2 - integrated datasets | Classification Policy 1.2 principle 4 |
| A3.5 - controls by classification | DC.2.1 |
| A4.1-A4.2 | PDP.1.1, PDP.1.2 |
| A4.3-A4.4 | PDP.4.3 |
| A4.5 | PDP.4.4 |
| A4.6, A5.4 | PDP.5.1 |
| A5.1-A5.2 - seven rights | PDP.4.2 |
| A6.1-A6.2 - agreements | Sharing Policy cl. Fifth |
| A6.3 - four non-negotiables | Sharing Policy, Third Principle; cl. Fifth items 6.B, 6.E, 7.B |
| A6.4 - pre-processing | cl. Fifth item 4.A |
| A6.5 - authorisation | cl. Fifth item 2.B; Fourth Principle |
| A6.6 - accountability stays | Sixth Principle |
| A6.7 - supplier security | Standards s.9.15 (Third Party Supplier Security control); Seventh Principle |
| A7 - lifecycle | House standards, built on PDP.1.1 and PDP.4.3 |
| A8 - agents | House standards, built on Classification Policy 1.2 principles 4, 6, 7 |
| A9.2-A9.4 - breach | PDP.3.1, PDP.3.2 |
| A11.1-A11.4 - compliance assessment | Standards s.4 |
| A11.6 - fully phased in | Standards s.8.1, s.8.2 |
| A12.4 - exceptions score zero | Standards s.4 (binary assessment) |
| A13 - what is not asserted | Section 7 of this note |

## 7. Every point at which the held instruments refer to a document not held

This is the map of the gap.

| Where | Refers to | What it would supply |
|---|---|---|
| **PDP.1.1 item 4** | NDMO **Personal Data Protection Regulations** | The compliance requirements the initial assessment must be measured against |
| **PDP.1.2 items 1-2** | Same | What the plan must achieve |
| **PDP.3.1** | Same | The detailed breach notification requirements. **The 72 hours is stated in the standards; nothing else about the notification is** |
| **PDP.3.2** | Same, **and NCA's guidance** | Detailed breach process requirements |
| **PDP.4.1** | Same | The prescribed notice and consent requirements |
| **PDP.4.2** | Same | The detail of the seven rights - response periods, exceptions, verification |
| **PDP.4.4** | Same | Detailed compliance monitoring requirements |
| **PDP.5.1** | Same | What the register must contain beyond the stated minimum |
| **Standards DG.4, every specification** | NDMO **"Organizational Manual"** | The defined responsibilities of the Chief Data Officer, Compliance Officer, Personal Data Protection Officer, Business Data Executives, Business Data Stewards and IT Data Stewards |
| **Standards s.9.15; DC.2.1** | **National Cybersecurity Authority** regulations and methodology | **Every data security specification**, and the compliance assessment for that domain |
| **Sharing Policy, Seventh Principle; cl. Fifth item 5.A** | NCA requirements and directives | Security controls for sharing channels |
| **Classification Policy** and standards throughout | "applicable KSA laws"; "relevant regulatory requirements" | The statutory framework the instruments operate within |
| **Standards s.9.14.3** | GDPR (2018); CCPA (2020) | **Listed as domain references. Nothing in this set was taken from either, and their appearance does not make them law in the Kingdom** |

**Two documents would close most of it**: the Personal Data Protection Regulations, and
the Organizational Manual. The security gap needs the cybersecurity authority's own
instruments and is separate.

## 8. Not held, beyond those

| What is missing | Consequence |
|---|---|
| **The Kingdom's personal data protection legislation and its implementing regulations** | **A general private-sector AI policy cannot be built from this set.** Policy 1.1 and 22; annex A13.2 |
| **Any instrument of the National Cybersecurity Authority** | No security specification is stated anywhere. Policy 1.4, 13.1 |
| **NDMO Personal Data Protection Regulations** | Section 7 |
| **NDMO Organizational Manual** | Section 7 |
| **Any transfer regulation** | The conditions for moving personal data outside the Kingdom are not stated. Policy 22 |
| **Sector regulator instruments** | No sector overlay exists |
| **Employment law, anti-discrimination law, IP law** | Policy 18 and 20 are house standards |
| **Enforcement decisions and case law** | None relied on anywhere |

## 9. What this set therefore does not say

- It does not govern an organisation processing only its own commercial personal data.
- It does not state any data security specification.
- It does not state the lawful bases for processing, or define personal or sensitive
  personal data.
- It does not state the detailed notice, consent, rights, breach or register
  requirements the standards direct the reader elsewhere for.
- It does not state the conditions for transferring personal data outside the Kingdom.
- It does not state any penalty for contravention.
- It does not state the responsibilities the Organizational Manual assigns.
- It does not assert any AI-specific obligation, because there is none in these
  instruments.

## 10. Method

Every provision cited above was read in the supplied text of the three instruments at
section 1. Nothing in this set was taken from a web page, a summary, a law-firm note, or
a comparative overview. The GDPR and CCPA appear in one domain's reference list in the
standards and **were not consulted, cited or relied on**. Where a requirement is left to
a regulation, manual or authority whose instrument is not held, the set names the gap
instead of filling it from any other source.

The three source PDFs were checked for duplication before use: three byte-identical
copies of the standards were supplied and the duplicates discarded.

## 11. Standing caveat

No provision cited in this set has been reviewed by qualified counsel. These documents
are educational templates and do not constitute legal advice.
