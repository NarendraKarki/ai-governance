# Research note - Sultanate of Oman AI policy set

Working note supporting the [ORGANISATION] Artificial Intelligence Acceptable Use Policy
(Oman) v1.0 and the AI Governance Enterprise Annex (Oman) v1.0.

**Article numbers live here, not in the policy or the annex.** This is where a reader can
check what each clause rests on, and where the limits of the set are stated.

State as at 3 September 2026.

---

## 1. What this set rests on

| # | Instrument | Reference | Held |
|---|---|---|---|
| 1 | **Personal Data Protection Law** | Royal Decree **6/2022**, issued 7 Rajab 1443 H / **9 February 2022**. Official Gazette issue **1429**. 5 chapters, **32 articles** | Arabic enacted text and official English |
| 2 | **Executive Regulations of the Personal Data Protection Law** | Ministerial Decision **34/2024**, MTCIT, issued 16 Rajab 1445 H / **28 January 2024**. Official Gazette issue **1531**. 9 chapters, **45 articles** | Arabic enacted text and official English |
| 3 | **General Policy for the Safe and Ethical Use of Artificial Intelligence Systems** - MTCIT English title: ***Public Policy for Safe and Ethical Use of Artificial Intelligence Systems*** | MTCIT, Directorate General of Policies and Governance. **First edition, April 2025**; document record version 0.1, 2025. 29 pp | Arabic and official English |
| 4 | **Circular 6/2024 on the Personal Data Protection Policy for Units of the State's Administrative Apparatus** | MTCIT Minister's Office, 20 Ramadan 1445 H / **31 March 2024**, with the attached policy, Version 1, March 2024 | Full Arabic text |

**A note on language.** The four instruments above are the **Arabic enacted texts**, and
the Arabic governs. **MTCIT's official English texts of the Law, the Executive Regulations
and the AI Policy are also held**, and every substantive assertion in this set has been
checked against them; the terminology used throughout now follows MTCIT's own English.
Source register section 4 records what that check confirmed, what it changed, and the
three places where the two language versions diverge. No English version of Circular
6/2024 appears to be published.

**A note on method.** Items 1 and 2 carry a text layer that extracts in a legacy encoding
and comes out garbled; items 3 and 4 are image-only and carry no text layer at all. All
four were therefore read as **rendered pages**. The official English texts were then
OCR'd to give a searchable layer, and the set was verified against it.

**That cross-check is strong, but it is not two independent extractions of the Arabic
agreeing with each other.** Any derivation of these provisions into structured,
machine-readable rules should go through that stricter discipline first - section 10.

## 2. Commencement, and the conformity deadline that has passed

| Instrument | Provision | Effect |
|---|---|---|
| Royal Decree 6/2022 | **Decree Art 4** | Published in the Official Gazette and **in force one year after the date of publication** - so from **February 2023** |
| Royal Decree 6/2022 | **Decree Art 3** | **Repeals Chapter Seven of the Electronic Transactions Law** (Royal Decree 69/2008), and everything contrary to or conflicting with the new Law |
| Royal Decree 6/2022 | **Decree Art 2** | The Minister of Transport, Communications and IT issues the Executive Regulations; existing regulations and decisions continue until they are issued, so far as not conflicting |
| Ministerial Decision 34/2024 | **Decision Art 4** | Published in the Official Gazette and **in force from the day following publication** |
| Ministerial Decision 34/2024 | **Decision Art 2** | **Those addressed by the Regulations must bring their positions into conformity within a period not exceeding one year from the date the Regulations come into force** |
| AI Policy | Ethical principles, *Policy management* item 2 | **In force from the date of its approval and circulation by MTCIT** |
| Circular 6/2024 policy | *Document management* item 2 | **In force 24 months after the date of its approval and circulation by MTCIT** - so from about **March 2026** |

**Nothing in this framework is pending.** The one-year conformity period under the
Executive Regulations expired in early 2025, and the government-sector policy's 24-month
runway expired in early 2026. Policy 4.1 states this, and the annex contains no
commencement-readiness register because there is nothing left to be ready for - which is
the opposite of the Indian and EU positions.

## 3. The findings worth recording

### 3.1 Explicit written consent is the default, and the controller must prove it

**Law Art 10.** Personal data may not be processed **except within a framework of
transparency, honesty and respect for human dignity, and after the explicit consent of
the data subject**. The request for processing **must be written, clear, explicit and
comprehensible**, and **the controller is obliged to prove the written consent** of the
data subject to the processing of their data.

**Regulations Art 4** adds the validity conditions. The controller must obtain explicit
consent **before** processing, and for consent to be relied on it must:

1. issue from **a person of full legal capacity**;
2. issue **clearly and without coercion**;
3. be **written, electronic, or by any other means the controller specifies**.

Two consequences the policy carries at Section 10. **The burden of proof is expressly
allocated to the controller** - so a consent that cannot be evidenced is functionally no
consent. And there is no general legitimate-interests or contract-necessity route in the
body of the Law; Art 3 instead removes certain processing from the Law's scope
altogether (3.2), which is a different mechanism and produces a different answer.

### 3.2 The scope exclusions are exclusions from the Law, not lawful bases

**Law Art 2**: the Law's provisions apply to personal data that is processed.

**Law Art 3**: the Law's provisions **do not apply** to processing in the following cases:

| | Case |
|---|---|
| (a) | Protection of **national security or the public interest** |
| (b) | Execution by **units of the State's administrative apparatus** and other public legal persons **of the competences legally established for them** |
| (c) | **Execution of a legal obligation** on the controller under any law, judgment or court order |
| (d) | Protection of the **economic and financial interests of the State** |
| (e) | Protection of a **vital interest of the data subject** |
| (f) | **Detection or prevention of a criminal offence**, on an official written request from investigation authorities |
| (g) | **Performance of a contract to which the data subject is a party** |
| (h) | Processing in a **personal or family context** |
| (i) | **Historical, statistical, scientific, literary or economic research** purposes, by entities authorised to conduct such work, provided no indication or reference relating to the data subject is used in what is published, so that the data cannot be attributed to an identified or identifiable natural person |
| (j) | Where the data is **available to the public**, in a manner not contrary to the Law |

**Law Art 4**: personal data is protected under the Law.

The structural point the policy carries at 10.7: these are **carve-outs from the
instrument**, not bases within it. An organisation relying on (g) is not "processing on
the basis of contract" under this Law - it is asserting that the Law does not govern that
processing at all. That is a materially stronger claim and is recorded as a written
determination rather than assumed.

### 3.3 Sensitive-category processing requires a permit, with a decision timetable

**Law Art 5** prohibits processing personal data relating to **genetic data, biometric
data, health data, racial origin, sexual life, political or religious opinions or
beliefs, criminal conviction, or matters relating to security measures**, except after
obtaining a **permit from the Ministry**, in accordance with the controls and procedures
the Regulations determine.

**Regulations Chapter 2 (Arts 5-10)** supplies the machinery.

**Reg Art 5** - the application is made on the prescribed form and contains: the **name,
address and email of the Personal Data Protection Officer**; the **purpose** of
processing; **identification and classification of the personal data**; the **processor
contracted with, if any**; **any entity or third party to whom the data will be
disclosed**; the **places to which the data will be transferred or kept**; the **systems
for managing and protecting** personal data; and any other data the Ministry requires.

**Reg Art 6** - the application must be accompanied by the applicant's **personal data
protection policy and the precautionary measures adopted for the event of a breach**.

**Reg Art 7** - the Competent Department studies and decides the application **within
a period not exceeding 45 days** from completion of the required data and documents; a
refusal **must be reasoned**; **expiry of the period without a reply is deemed a
rejection**. The applicant may **grieve to the Minister within 60 days** of notification
or certain knowledge, and **failure to answer the grievance within 30 days is deemed a
rejection**.

**Reg Art 8** - the permit is issued by the Minister for a period **not exceeding five
years**, after payment of the prescribed fees; renewal follows the same procedures.

**Reg Art 9** - the controller must notify the Competent Department of **any
amendments to the data contained in the permit within 15 days** of making them.

**Reg Art 10** - the permit is **cancelled** where: the controller requests it; the
controller commits a contravention of the Law or the Regulations; **amendments are not
notified within the specified period**; or the permit was obtained by **fraud, deception,
forgery, or the provision of incorrect data or information**.

**Why this matters more for AI than it first appears.** Four of the eight fields at Reg
Art 5 are facts about tooling - the processor, the recipients of disclosure, the places of
transfer or storage, and the protection systems. **Changing an AI supplier, adding a
sub-processor, or moving a workload between regions changes the permit**, engaging the
15-day duty at Reg Art 9, and failure to notify is a cancellation ground at Reg Art 10(3).
Policy 11.5 and annex A4.4 turn that into a screening step against the Permit Register.

### 3.4 Two breach clocks, both 72 hours, with different triggers

This is the most operationally significant finding in the set.

**Law Art 19** creates the duty without a period: on the occurrence of a breach of personal
data leading to its **destruction, alteration, disclosure, unlawful access to it, or
unlawful processing**, the controller must **notify the Ministry and the data subject**,
in accordance with the controls and procedures the Regulations determine.

**Regulations Chapter 6 (Arts 30-33)** supplies the periods, and there are two of them.

| Duty | Provision | Period | Trigger |
|---|---|---|---|
| **To the Competent Department** | **Reg Art 30** | **Within 72 hours from the time of the controller's knowledge of the breach** | **If it would lead to a risk threatening the rights of data subjects** |
| **To the data subject** | **Reg Art 32** | **Within 72 hours from the time of the controller's knowledge of the breach** | **If the breach would cause serious damage or high risks to the data subject** |

**Reg Art 30** minimum contents: (1) a description and details of the **nature of the
breached data and the results arising** from the breach; (2) the **contact data and
information of the controller or any other contact point** for obtaining more
information; (3) a **description of the probable effects**; (4) the **corrective
procedures or technical and organisational measures the controller will take**, including
where necessary the **proposed measures to mitigate probable negative effects**; (5) the
**corrective procedures and technical and organisational measures the controller took
immediately upon learning of the breach and before notifying** the Competent Department.

Item (5) is unusual and worth naming: the notification asks what you did **before** you
notified. Policy 15.2 draws the conclusion - the provision rewards acting first and
reporting inside the window, and exposes an organisation that spent the 72 hours drafting.

**Reg Art 32** minimum contents: (1) the **type and nature** of the breach; (2) the
**details of the personal data exposed**; (3) **recommendations to limit or mitigate the
effects**, where required.

**Reg Art 31** - after receiving the notification the Competent Department may
**document it in the register prepared for that purpose**, and may: (1) **evaluate the
procedures and measures the controller took and the extent to which they meet the damage
resulting from the breach**; (2) **direct that the data subject be notified** if it sees
fit, without prejudice to Reg Art 32; (3) provide appropriate guidance or the necessary
support to the controller according to available capabilities.

**Reg Art 33** - the controller must **document cases of breach**, stating their causes and
the results arising, and the corrective procedures or technical and organisational
measures taken, and **retain them for the period the Competent Department determines**,
in the register under Reg Art 28.

**Three points the policy and annex carry.**

- **The thresholds are different.** A breach can cross one and not the other. Policy 15.4
  requires a recorded determination for each limb; annex A9.2 makes a simulated breach
  that crosses one but not the other the specific internal audit test, because the failure
  mode is running one clock and assuming it discharged both.
- **The regulator can direct notification** under Reg Art 31(2) after the organisation has
  decided not to notify. Policy 15.5 plans for it.
- **Both periods run from knowledge**, so the recorded awareness timestamp is the
  controlling fact for both.

### 3.5 Cross-border transfer carries a fine an order of magnitude above everything else

**Law Art 23** - without prejudice to the competences of the Electronic Defence Centre,
the controller may transfer personal data and permit its transfer outside Oman in
accordance with the controls and procedures the Regulations determine. **Transfer is
prohibited** where the personal data **was processed in contravention of the Law**, or
where the transfer **would cause harm to the data subject**.

**Regulations Chapter 8 (Arts 37-40)** supplies the conditions.

**Reg Art 37** - before transferring, the controller must obtain the **explicit consent of
the data subject**, and the transfer must **not prejudice national security or the higher
interests of the State**. Consent is **not required** in either of two cases: (1) the
transfer executes an obligation under an **international agreement to which Oman is a
party**; (2) the transfer is carried out **in a manner leading to concealing the identity
of the data subject, not linking the data to them, and the impossibility of identifying
them by any means whatsoever**.

**Reg Art 38** - the controller must ensure the **external processing entity has a level of
protection for personal data not less than the level prescribed** under the Law and the
Regulations.

**Reg Art 39** - the controller must conduct an **assessment** of the level of protection
the external processing entity provides and of the risks of transfer, covering in
particular: (1) a description of the **nature and volume** of the data and **its degree of
sensitivity**; (2) the **purpose** of processing, the **scope**, and the **entities with
which the data will be shared**; (3) the **time period** of processing and whether it is
**limited or incidental, once only, or repeated and regular** within a defined period;
(4) the **stages of transfer and the states through which the data may pass**, and the
**final destination**; (5) the **effects and risks** that may result and their **impact on
the data subject**.

**Reg Art 40** - **the Ministry may request a copy of the assessment report** to verify the
adequacy of protection at the external processing entity.

**And then the penalty.** Under **Law Art 29**, contravention of Law Art 23 is punished by
a fine of **not less than OMR 100,000 and not more than OMR 500,000**.

**The comparison is the point.** The next highest band in the statute, Law Art 28, tops out
at OMR 20,000. **The minimum fine for a transfer contravention is five times the maximum
fine available for any other contravention in the Law.** Policy 1.5 and Section 17, and
annex A6, are all consequences of that single figure.

### 3.6 The full penalty structure, which is not ordered as one would expect

| Provision | Fine | Contravention of |
|---|---|---|
| **Art 25** | OMR **500 - 2,000** | Art 14 (written notice before processing) |
| **Art 26** | OMR **1,000 - 5,000** | Arts 15, 16, 17, 18, 20, 22 (ministry controls; external auditor; retention of processing documents; cooperation with the Ministry; **designating the Personal Data Protection Officer**; marketing consent) |
| **Art 27** | OMR **5,000 - 10,000** | Art 13 (establishing the controls and procedures for processing) |
| **Art 28** | OMR **15,000 - 20,000** | Arts 5, 6, 19, 21 (permit categories; children's data; **breach notification**; confidentiality and publication) |
| **Art 29** | OMR **100,000 - 500,000** | Art 23 (cross-border transfer) |
| **Art 30** | OMR **5,000 - 100,000** on the **legal person** | Where the offence was committed in its name or for its account by its president, a board member, its manager or any other official, **with his approval, connivance, or gross negligence** |
| **Art 31** | - | The competent court may, in addition to the fine, order **confiscation of the tools used to commit the offence** |
| **Art 32** | Administrative fine **not exceeding OMR 2,000** | Ministry **administrative sanctions** for contraventions of the Law, Regulations or implementing decisions, without prejudice to the criminal penalties |

**Law Art 24** preserves any more severe penalty in the Penal Code or another law.

Two observations. **Failing to establish processing controls (Art 13) is priced above
failing to appoint the data protection officer or to retain processing documents** - the
architecture is treated as more serious than the roles. And **the notice obligation, which
is the one most organisations breach first and most often, carries the lowest band** -
which is worth knowing but is not a reason to treat it lightly, since it is also the
obligation most visible to a data subject and therefore most likely to generate the
complaint at Reg Art 41.

### 3.7 The national AI policy is a real instrument, and it reaches the private sector

**Scope of application**, stated in the policy's own *Scope* section: the document applies
to **all government units and private-sector institutions subject to regulation by the
regulatory authorities** which work on developing or using AI systems, and it covers the
stages of **implementation, data collection, system design, training, operation and
continuous evaluation**.

**A divergence between the two language versions, and it resolves in favour of the
private sector.** The Arabic document-control page carries a **distribution list** reading
only "all units of the State's administrative apparatus", which is narrower than the
Arabic scope section. **The official English distribution list reads "All State
Administrative Apparatus units and the Private Sector"** - so in English there is no
divergence at all: the distribution list and the scope section agree.

The set was originally written from the Arabic alone and followed the scope provision over
the narrower distribution list. **The English text confirms that reading was right**, and
does so on the very page that had appeared to contradict it. A reader working only from the
Arabic distribution list would have concluded the policy is government-only.

**Definitions** confirm the breadth: the **entity using AI systems** and the **entity
developing AI systems** are each defined as "any **governmental or private** institution".

**General provisions (First, items 1-5):**

1. Entities subject to the policy commit to **full compliance** with its technical
   controls and ethical principles for using and developing AI systems, **including
   generative AI systems**.
2. Using and developing entities commit to **evaluating AI system performance
   periodically**, including generative systems, to ensure compliance with the controls
   and principles, **data integrity, output integrity and accuracy, and the handling of
   biases and harmful content**.
3. The **Ministry** commits to preparing the supporting legislative environment.
4. **Regulatory authorities** commit to **aligning the policy with their own regulatory
   documents** and circulating it to the institutions subordinate to or associated with
   them.
5. **Regulatory authorities may, after obtaining the Ministry's approval, lay down
   additional provisions regulating the use of AI technologies and algorithms**, provided
   they do not conflict with the policy.

**Compliance with the policy (items 1-2):**

1. **MTCIT monitors the compliance of the units of the State's administrative apparatus
   and presents the results to the Council of Ministers.**
2. **The regulatory authorities monitor the compliance of the institutions in the sectors
   they supervise.**

**This is the enforcement architecture, and it is the reason policy 4.2 says what it
says**: for a private-sector institution the monitoring body is its **sector regulator**,
not the issuing ministry. Combined with general provisions 4 and 5, it means
[ORGANISATION] must track its own regulator's issuances and not only the national ones -
policy 4.3, annex A15.5.

### 3.8 Ten controls for using, thirteen for developing

**Second: controls and requirements for using AI systems.** Using entities commit to:

| | Control |
|---|---|
| 1 | Providing **mechanisms for human supervision and control over sensitive and influential decisions** taken by AI systems, and ensuring the possibility of **explaining, tracing and analysing** the results and their effects on individuals, society and institutions |
| 2 | Ensuring the systems have **clear practical feasibility and benefit compared with available alternatives**, achieving tangible added value in efficiency, quality or cost; systems must be **evaluated objectively before adoption** against the entity's needs and operational objectives |
| 3 | Ensuring systems can give **understandable explanations for the decisions they take, especially in applications affecting individuals such as employment, health and financial services** |
| 4 | **Monitoring performance continuously**, with any errors, deviations or negative effects **documented immediately upon detection** and the necessary corrective measures taken |
| 5 | **Providing all documents and information relating to use of the system to the regulatory authorities** to verify compliance, in the event of an official investigation into what AI employment may produce |
| 6 | **Restricting the use of personal data in AI systems** in compliance with local laws and regulations, ensuring use **only for the specified and authorised purposes**, and taking measures to protect it from unlawful or unauthorised use |
| 7 | **Classifying the data used**, with advanced security procedures for classified data such as **encryption, multi-factor authentication and identity-concealment techniques** |
| 8 | Systems must be **transparent in the decision-making mechanism**, with **accountability mechanisms and documentation of all procedures** to ensure verifiability and future analysis |
| 9 | Applying **clear data management and retention policies**, including **recommended retention periods and secure deletion** when no longer needed |
| 10 | **Restricting use of the analysis results to the purpose for which the system was used**, that purpose being compatible with the reasons and objectives on which it was based |

**Third: controls and requirements for developing AI systems.** Developing entities commit
to:

| | Control |
|---|---|
| 1 | **Documenting the development process transparently and clearly**, including the purpose, technologies and data used, and **retaining the documents** for reference |
| 2 | Developing **environmentally and technically sustainable solutions** |
| 3 | Conducting an **ethical, social and environmental impact assessment before publication and use**, and **retaining its results within the system documentation** |
| 4 | **Ensuring transparency in generated content** and taking measures to prevent generation of harmful or misleading content, with **mechanisms for detecting generative content through labelling or explanatory notices** |
| 5 | **Ensuring transparency in how algorithms work** through documents explaining **the logic of decision-making and the data analysis process** |
| 6 | **Regular review and updating** to keep pace with technical developments and international standards |
| 7 | **Periodic evaluations verifying system accuracy, including independent technical reviews** |
| 8 | **Providing all development documents to the regulatory authorities** in the event of an audit or official investigation |
| 9 | **Continuous monitoring and evaluation of potential biases in outputs**, with measures to reduce data- or algorithm-associated bias through **fairness and inclusiveness verification tests** |
| 10 | **Protection controls ensuring privacy and data security**, using access control and data encryption |
| 11 | **Analytical tools and reports explaining how decisions are made**, enabling **regulatory authorities and users** to evaluate the logic of operation and verify integrity and accuracy |
| 12 | **Granting individuals the right of access to their data**, including review of processing records, correction of errors, or deletion on request, **with easy-to-use interfaces** |
| 13 | **Best cybersecurity practice**, including regular software updating and **periodic penetration testing** |

**Item 4 of the development controls is a content-marking obligation** and is carried at
policy 19.2. **Item 2 of the use controls is a comparative-necessity test** and is carried
at policy 6.2 and annex A5.2 - a business case that never names a lower-risk alternative
does not satisfy it.

### 3.9 The ethical principles, and the one that is a design requirement

The policy defines its principles in the definitions section - **fairness, transparency,
accountability/responsibility, inclusiveness, humanity, explainability** - and then states
them operationally in four groups.

**Humanity and society (items 1-4)**: respect for human dignity and **the individual's
right to human intervention in sensitive decisions that directly affect their life, safety
or rights**; harnessing AI for societal welfare including health, education and social
work; promoting AI for sustainable development and environmental protection; considering
the economic and social dimensions of widespread use so that benefits are distributed
fairly and **the technology does not increase economic disparities**.

**Inclusiveness and fairness (items 1-3)**: designing systems to ensure **no bias on the
basis of race, gender, religion or any other personal characteristic**, through
**algorithm-auditing techniques** and excluding factors that may lead to discrimination,
**in a manner consistent with Islamic principles and values**; ensuring **diversity of
training data including representation of minorities and persons with disabilities**;
ensuring fair availability of the technology through government and private-sector
cooperation at reasonable prices, with focus on **access for limited-income groups**.

**Responsibility and accountability (items 1-5)**: ensuring systems are **safe from
breaches and produce no physical or psychological harm**; **clear and effective
accountability mechanisms** where errors or damage occur, with **easy and clear access to
complaint channels**, handled fairly and transparently; ensuring the **auditability** of
systems using **review reports, performance logs and independent third-party reviews**;
using technical tools to assure transparency such as **documenting decision-making
processes inside the system** and publishing periodic performance reports with the
participation of users and concerned parties; and **providing a mechanism enabling the
tracing of data sources and the standards of their use**, so that generated content can be
analysed and its effects understood.

**Policy management (items 1-2)**: ownership rests with MTCIT and the policy is subject to
review as needed; **the policy enters into force from the date of its approval and
circulation by MTCIT**.

**The fifth accountability item is a design requirement, not a reporting preference.**
Data-source traceability has to be built in; it cannot be added to a deployed system.
Policy 8.3.5 says so and annex A2.1 makes traceability an inventory field, with policy
14.4 making it a bar to Level 4 approval.

### 3.10 Obligations that shape AI operations specifically

**Law Art 13** - the controller must establish the **controls and procedures** to be
observed when processing, covering in particular: (a) **identifying the risks that may
fall on the data subject as a result of the processing**; (b) **procedures and controls
for transferring and transmitting** personal data; (c) **technical and procedural measures
to ensure processing is carried out in accordance with the Law**; (d) any other controls
or procedures the Regulations determine. *Fine band: OMR 5,000-10,000 (Art 27).*

**Law Art 14** - **before beginning any processing**, the controller must notify the data
subject **in writing** of: (a) the **controller's and processor's details**; (b) the
**contact details of the Personal Data Protection Officer**; (c) the **purpose of
processing and the source from which the data was collected**; (d) the **comprehensive and
precise description of the processing, its procedures, and the degrees of disclosure** of
the personal data; (e) the **data subject's rights including access, correction, transfer
and updating**; (f) any other information necessary to satisfy the conditions of
processing.

Limb (d) is the one AI deployments fail, and policy 10.5 says so.

**Law Art 16 and Reg Arts 23-24 - the external auditor.** At the **Ministry's request**,
the controller and processor must **appoint an external auditor** to verify that
processing was carried out in accordance with the Law and with the Art 13 controls, and
must **provide the Ministry with a copy of the report**. Reg Art 23 requires the auditor to
be **accredited and licensed by the Ministry** and **independent, not linked by any direct
or indirect connection with the controller or processor**, and requires the controller and
processor to **enable the auditor to view and examine the records, processing systems and
data necessary for the audit**. **Reg Art 24 sets the deadline: a copy of the report to the
Competent Department within 60 days of the auditor's appointment.**

Sixty days for an audit of an AI estate is short, which is why annex A8 maintains a
standing audit pack rather than assembling one on demand.

**Law Art 20 and Reg Arts 34-36 - the Personal Data Protection Officer.** The controller
**must designate** one. Reg Art 34 sets the selection controls: **qualified** for the Art
35 tasks; **knowledgeable of the Law, the Regulations and the data protection practices
followed** at the controller or processor; **professionally competent and able to deal
regularly and correctly with all matters relating to personal data protection**. Reg Art 35
sets the tasks: **proposals and advice** on obligations; **following up implementation of
data protection policies**; **following up performance of obligations**; **coordinating
with the Competent Department**. Reg Art 36 requires the controller to **publish the
officer's details including name and contact data by any means**, and gives the data
subject the right to contact the officer on all matters relating to processing of their
data.

**Law Art 21 and Reg Arts 25-26 - confidentiality.** The controller must ensure
confidentiality and **not publish personal data except with the data subject's prior
consent**. Reg Art 25 **prohibits the controller and processor from publishing, sharing or
disclosing the Art 5 categories** except within the limits and cases legally prescribed or
in execution of a judgment or judicial decision. Reg Art 26 sets the confidentiality
controls: **electronic systems preventing unlawful access, leakage, tampering or misuse**;
**systems for restoring personal data on a physical or technical incident**; and
**processes for testing the effectiveness of the technical procedures in place**.

**Law Art 22 and Reg Art 22 - marketing.** The controller must obtain the data subject's
**written consent before sending any advertising or marketing material for commercial
purposes**. Reg Art 22 adds three further duties: **notify the data subject of the means of
sending**; **specify a mechanism for stopping receipt**; and **stop sending immediately on
receiving a stop request, free of charge**.

**Law Arts 17-18 and Reg Arts 2, 27 - records and cooperation.** The controller and
processor must **retain the documents of processing operations** for the periods and
procedures the Regulations determine (Reg Art 27: the retention reason must be **specific
and lawful**, the period **proportionate to the purpose**, and **technical protection
systems for secure retention** provided), and must **cooperate with the Ministry**,
providing the data and documents it requires **within 30 days of the request** (Reg Art 2).

**Reg Arts 28-29 - the processing activities register.** The controller or processor must
create a **special register of personal data processing activities**, containing at
minimum the ten fields set out at policy 14.1, and must **update it continuously and
provide it to the Competent Department whenever requested**.

**Reg Art 3 - the processor relationship.** The controller may contract with a processor.
The processor is, in its relationship with others in what it provides on the controller's
behalf, **within the scope of civil liability and administrative liability before the
Ministry, and without prejudice to its own criminal liability** for its contraventions of
the Law and Regulations.

### 3.11 Data subject rights, with a 45-day answer and a free-of-charge rule

**Law Art 11** gives the data subject the right to: (a) **withdraw consent** to processing,
without prejudice to processing carried out before withdrawal; (b) request **amendment,
updating or blocking** of their data; (c) obtain a **copy** of their processed personal
data; (d) **transfer their data to another controller**; (e) request **erasure**, unless
the processing is necessary for **national preservation and documentation purposes**;
(f) **be notified of any breach or infringement of their personal data and of the measures
taken**.

**Law Art 12** - the data subject may complain to the Ministry if they consider that the
processing of their data does not comply with the Law.

**Regulations Chapter 4 (Arts 16-20)** supplies the machinery.

- **Reg Art 16** - a **written request** to exercise the rights at Law Art 11(a), (c), (d)
  and (e), **without charge**; the controller must decide **within a period not exceeding
  45 days** of receipt; the data subject may **request suspension of processing pending the
  decision**.
- **Reg Art 17** - the controller may refuse **partially or wholly** where the request is
  **repeated without justification** or its execution **requires unusual effort**; in all
  cases the controller must notify the data subject of the **reasoned refusal within the
  Art 16 period**.
- **Reg Art 18** - erasure is available where **the purpose of processing has ended**,
  where **consent has been withdrawn** (without prejudice to Art 17), or where **the
  processing does not comply with the Law or the Regulations**. The controller may refuse
  where there is **a legal obligation on the controller under any law, judgment or judicial
  decision**, or where **a live dispute exists between the controller and the data
  subject**.
- **Reg Art 19** - the copy is provided in a **readable and clear format, electronic or
  paper**, provided it is **verified to be free of any personal data identifying another
  person**.
- **Reg Art 20** - the data subject may transfer their data to a **new controller**, and
  the controller shall transfer **if legally obliged to do so**.

**Reg Art 21** - the controller or processor must place a **personal data protection policy
in a visible place** enabling the data subject to view it **before** processing, containing
**at minimum a mechanism and procedures for exercising the rights** under the Law and the
Regulations.

Annex A11.5 flags the practical difficulty in Reg Art 19 for AI systems: prompt logs and
transcripts routinely contain third parties, so the "free of other persons' data"
verification is real work and must be evidenced.

### 3.12 Children and persons without capacity

**Law Art 6** prohibits processing a child's personal data **except with the consent of
the guardian**, unless the processing is **in the child's best interests**, in accordance
with the controls and procedures the Regulations determine. *Fine band: OMR 15,000-20,000
(Art 28).*

**Regulations Chapter 3 (Arts 11-15):**

- **Reg Art 11** - the controller or processor must obtain the **guardian's explicit
  consent** before processing, and **may request from the child the minimum data about
  the guardian** for the purpose of verifying identity and obtaining consent.
- **Reg Art 12** - controls: the **aim must be clear, direct, safe and free of deception
  and misleading**; processing must be **limited to the minimum personal data** to achieve
  the specified purpose.
- **Reg Art 13** - the controller or processor must **identify and provide the means
  enabling the guardian to access the child's personal data**, to update and amend it.
- **Reg Art 14** - **no disclosure or sharing** of a child's personal data with others
  except after the guardian's explicit consent.
- **Reg Art 15** - a person **lacking or having diminished capacity, or who has lost
  capacity**, is represented by their **guardian, trustee or curator**, and this chapter
  applies to the processing of their personal data.

### 3.13 Ministry powers, and the complaints timetable

**Law Art 7** - the Ministry is responsible for applying the Law, **without prejudice to
the competences of the Electronic Defence Centre**, and in particular: (a) preparing and
adopting the controls and procedures for personal data protection, including the necessary
guarantees, measures and **codes of conduct**; (b) issuing the controls and procedures for
processing and **verifying controller and processor compliance**; (c) receiving reports and
complaints from data subjects and deciding them within the period the Regulations
determine; (d) **cooperating with counterpart authorities in other states**; (e) providing
advice, support and coordination to State administrative units and public legal persons;
(f) **issuing and cancelling licences for service providers entrusted with studying and
evaluating controller and processor compliance**; (g) preparing guidance templates;
(h) preparing **periodic reports on its activity and publishing them on its website**;
(i) **preparing a register in which controllers and processors meeting the prescribed
conditions are entered**.

**Law Art 8** - measures the Ministry may take to protect data subjects' rights:
(a) **warning** the controller or processor of the contravention; (b) **ordering correction
and erasure** of personal data processed in contravention; (c) **suspending processing
temporarily or permanently**; (d) **suspending the transfer of personal data to another
state or an international organisation**; (e) any other measure the Ministry considers
necessary.

**Law Art 9** - Ministry employees designated by decision of the competent authority in
agreement with the Minister have **judicial enforcement capacity** in applying the Law, the
Regulations and the implementing decisions.

**Regulations Chapter 9 (Arts 41-45) - complaints and sanctions:**

| Step | Provision | Period |
|---|---|---|
| Data subject or interested person complains to the Competent Department | **Reg Art 41** | **Within 30 days of certain knowledge of the contravention** |
| Competent Department notifies the controller with a copy | **Reg Art 41** | **Within 7 days of submission** |
| Controller's right to reply | **Reg Art 42** | **Within 14 days of being notified** |
| Competent Department decides | **Reg Art 43** | **Within 60 days from the day following expiry of the Art 42 period**; **silence is a rejection** |
| Administrative sanctions by the Minister | **Reg Art 44** | **Warning; suspension of the permit until the contravention is removed; administrative fine not exceeding OMR 2,000 per contravention; cancellation of the permit** |
| Grievance against a sanction | **Reg Art 45** | **To the Minister within 60 days**; the Minister decides **within 30 days**; **silence is a rejection** |

**The 14-day reply window at Reg Art 42 is the shortest externally imposed deadline in the
framework**, and annex A12.2 requires a standing process and a named owner for it.

## 4. Clause-by-clause basis

### 4.1 Policy

| Policy | Rests on |
|---|---|
| 1.1, 4.1-4.3 | AI Policy *Scope*, *General provisions* 3-5, *Compliance* 1-2 |
| 1.2, 10.1-10.3 | Law Art 10; Reg Art 4 |
| 1.3, 11 | Law Art 5; Reg Arts 5-10 |
| 1.4, 15 | Law Art 19; Reg Arts 30-33 |
| 1.5, 17 | Law Arts 23, 29; Reg Arts 37-40 |
| 2.1 | Law Art 1 (definitions); Reg Art 3; AI Policy definitions (using / developing entity) |
| 2.2, 22.2 | Circular 6/2024 policy, *Scope* |
| 3.6, 11.5 | Reg Art 5(4)-(7); Reg Art 9 |
| 4.2 | Law Arts 7, 8, 9; AI Policy *Compliance* 1-2 |
| 5 | House standard, built on Law Art 5 and the AI Policy scope |
| 6.1-6.10 | AI Policy *Second*, items 1-10 |
| 7.1-7.13 | AI Policy *Third*, items 1-13 |
| 8.1-8.3 | AI Policy *Ethical principles*, all four groups |
| 9 | House prohibitions, except 9.1 (Law Art 5), 9.3 (Law Art 23), 9.5 (Law Art 6), 9.8 (Law Art 22) |
| 10.4-10.5 | Law Art 14 |
| 10.6 | Reg Art 21 |
| 10.7 | Law Art 3 |
| 12.1-12.2, 12.4-12.5 | House standards, supported by AI Policy *Second* 1 and 3 |
| 12.3 | AI Policy *Ethical principles*, Humanity and society 1 |
| 13 | Law Art 20; Reg Arts 34-36 |
| 14.1-14.2 | Reg Arts 28-29 |
| 14.3 | Law Art 17; Reg Art 27 |
| 14.4 | AI Policy *Ethical principles*, Responsibility and accountability 5 |
| 14.5-14.6 | Law Art 16; Reg Arts 23-24 |
| 14.7 | Law Art 18; Reg Art 2 |
| 15.2 | Reg Art 30 |
| 15.3 | Reg Art 32 |
| 15.5 | Reg Art 31 |
| 15.6 | Law Art 11(f) |
| 15.7 | Reg Art 33 |
| 15.8 | House standard |
| 16 | Law Art 6; Reg Arts 11-15 |
| 18 | Law Art 22; Reg Art 22 |
| 19.1 | Law Art 21; Reg Art 25 |
| 19.2 | AI Policy *Third* 4 |
| 20.1-20.2, 20.4 | House standards |
| 20.3 | Law Arts 17, 18; AI Policy *Second* 5 and *Third* 8 |
| 22 | Section 6 of this note |

### 4.2 Annex

| Annex | Rests on |
|---|---|
| A1.3-A1.4 | Law Art 20; Reg Arts 34-36 |
| A2.1 | Reg Arts 5, 28; Reg Art 39; AI Policy *Ethical principles* R&A 5 |
| A3 | Reg Arts 28-29, 27, 33 |
| A4 | Reg Arts 5-10 |
| A5.1-A5.2 | AI Policy *Second* 2; *Third* 3 |
| A5.4 | AI Policy *Second* 4 |
| A5.5 | AI Policy *Third* 6-7 |
| A6 | Law Art 23; Reg Arts 37-40; Law Art 8(d) |
| A7 | Reg Art 3; Reg Art 5(4)-(5); Reg Arts 30, 32 |
| A8 | Law Art 16; Reg Arts 23-24; AI Policy *Second* 5, *Third* 8 |
| A10 | House standards derived from the above |
| A11 | Law Art 11; Reg Arts 16-21 |
| A12 | Reg Arts 41-45 |
| A13.4 | Reg Arts 44-45; Law Art 32 |
| A14 | House standards, built on Law Arts 5, 23 and Reg Art 39 |
| A15 | Section 6 of this note |

## 5. Held but not used - the government-sector instrument

**Circular 6/2024**, dated 31 March 2024 and signed by the Minister, transmits the
**Personal Data Protection Policy for Units of the State's Administrative Apparatus**
(Version 1, March 2024). It is **not used in this set**, because its scope section states
that it **applies to the units of the State's administrative apparatus** - defined by
reference to Royal Decree 75/2020 on the State Administrative Apparatus - and
[ORGANISATION] is assumed to be a private-sector organisation.

It is summarised here because it is held, because it would be the basis of a
government-sector variant, and because two of its features differ materially from the
private-sector position and would mislead if carried across.

The circular itself directs State administrative units to: **protect all information and
personal data in their possession**, including data received from or disclosed to other
units; **apply security and organisational measures** sufficient to protect data from
unintended or unauthorised destruction, accidental loss, unauthorised alteration,
disclosure, breach or other processing; **process personal data within the geographic
borders of Oman** to preserve national sovereignty over it and protect its owners'
privacy; **put in place sufficient security precautions** for all systems and storage media
concerned; and **publish a privacy statement on their websites**.

The attached policy uses **controlling unit** and **processing unit** rather than
controller and processor, and defines a **third party** as an entity working under the
supervision of the controlling or processing unit, authorised to process data on its
account, **and having its headquarters in the Sultanate of Oman**.

**The two divergences that matter:**

- **Breach notification goes to the Electronic Defence Centre**, not to MTCIT. Policy
  provision 1.11 requires the controlling unit to notify the Electronic Defence Centre on
  any **leakage, damage or breach** of personal data. That is a different recipient from
  the Competent Department under Reg Art 30.
- **Data localisation is the default.** Provision 1.12 requires processing **inside Oman's
  geographic borders**, with transfer or processing abroad permitted only for: performance
  of a contract to which the data subject is a party; commencing procedures to claim or
  defend legal rights; or protecting the vital interests of the data subject. Provision
  1.13 requires **the approval of the Electronic Defence Centre before transferring
  personal data outside Oman for processing**.

**Neither of those applies to a private-sector organisation under the Law and Regulations**,
and importing them would be an error in the cautious direction but an error nonetheless.

Compliance: **MTCIT monitors the units' compliance and presents the results to the Council
of Ministers.** Related references named: the Omani Personal Data Protection Law (2022) and
the Open Data Policy (2020).

## 6. Every point at which the held instruments refer to something not held

| Where | Refers to | What it would supply |
|---|---|---|
| **AI Policy** *General provisions* 4-5; *Compliance* 2 | **The regulatory authorities' own regulatory documents and any additional provisions on AI technologies and algorithms** | **The sector requirements that actually bind [ORGANISATION], and the body that monitors its compliance.** The single most important gap in this set |
| **AI Policy** *Related issuances* | **National Programme for AI and Advanced Digital Technologies (2024)** | Programme context |
| **AI Policy** *Related issuances* | **IT Risk Management Framework (2014)** | Risk methodology |
| **AI Policy** *Related issuances* | **Law on Combating Information Technology Crimes (2011)** | Cybercrime offences |
| **AI Policy** *Related issuances* | **National Records Law (52/2024)** | Records and retention obligations that may qualify erasure |
| **AI Policy** *Related issuances* | **Regulatory Framework for National Data Governance and Management (2025)** | National data governance obligations |
| **Law Arts 7, 23; Circular 1.11, 1.13** | **The Electronic Defence Centre** and its competences (established under Royal Decree 64/2020) | The competences the Law expressly preserves alongside the Ministry's |
| **Decree Art 3** | **Electronic Transactions Law (Royal Decree 69/2008)** | The repealed Chapter Seven, and what survives |
| **Circular policy, definitions** | **Royal Decree 75/2020 on the State Administrative Apparatus** | Which bodies are State administrative units |
| **Reg Art 5, 8** | **The prescribed forms and the prescribed fees** | Permit application mechanics. MTCIT publishes forms; none is held here |
| **Reg Art 33** | **The period the Competent Department determines** for retaining breach documentation | Retention period for breach records |
| **Law Art 7(f)** | **Licensed service providers** entrusted with evaluating compliance | Who may act, beyond the Reg Art 23 conditions |
| **Law Art 7(a)** | **Codes of conduct** the Ministry may adopt | Any code applicable to [ORGANISATION] |

## 7. Not held, beyond those

| What is missing | Consequence |
|---|---|
| **[ORGANISATION]'s sector regulator's issuances** | Policy 4.3 and 22.2; annex A15.5. **This is the standing action** |
| **An official English text of Circular 6/2024** | Its page serves a single attachment, labelled English, which is in fact Arabic. The set does not rest on the circular |
| **MTCIT guidance and forms** (processing permit form, breach report form, cross-border transfer assessment form, DPO appointment form, processing activity record, data subject rights guidelines, controller-processor guidelines, explicit consent guide) | Published by MTCIT and **not held**. Several map directly onto obligations in this set, and obtaining them would sharpen Sections 11, 15 and 17 considerably |
| **Employment law, anti-discrimination law, intellectual property law** | Policy 20 and parts of Section 8 are house standards |
| **Enforcement decisions and case law** | None relied on anywhere |

## 8. What this set therefore does not say

- It does not state any requirement of [ORGANISATION]'s sector regulator, which is both a
  source of additional AI provisions and the monitoring body for the national AI policy.
- It does not state the competences of the Electronic Defence Centre.
- It does not state the content of the national data governance framework, the national
  records law, the cybercrime law, or the IT risk management framework.
- It does not state the retention period for breach documentation, which the Competent
  Department determines.
- It does not reproduce the prescribed forms or state the permit fees.
- It does not govern units of the State's administrative apparatus - section 5.
- It does not resolve the divergences between the Arabic and English versions recorded
  at source register 4.4; where they differ, the Arabic governs.

## 9. Method

Every provision cited above was read in the supplied Arabic texts, page by page as
rendered. Nothing in this set was taken from a web page, a summary, a law-firm note, or a
comparative overview, and no comparison to any other jurisdiction appears in any Oman
document. Where a requirement is left to a form, a fee, a determination or a sector
regulator's issuance that is not held, the set names the gap instead of filling it.

## 10. A note on further derivation

This set is a policy deliverable and was produced by reading rendered pages. **The Arabic
texts have not been through a dual-extraction transcription discipline** - geometric
extraction plus independent OCR, accepting only where both agree.

If these provisions are ever derived into structured rules or any automated compliance
tooling, the Law and the Regulations should go through that discipline first, and the
derived positions re-established from it rather than carried across from this note. The
candidates that would matter most are the two 72-hour periods at Reg Arts 30 and 32 and
their differing triggers, and the transfer conditions at Reg Arts 37-39.

## 11. Standing caveat

No provision cited in this set has been reviewed by qualified counsel. These documents are
educational templates and do not constitute legal advice.
