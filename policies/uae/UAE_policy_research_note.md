# Research note - United Arab Emirates AI policy set

Working note supporting the [ORGANISATION] Artificial Intelligence Acceptable Use Policy
(United Arab Emirates) v1.0 and the AI Governance Enterprise Annex v1.0.

**Provision identifiers live here, not in the policy or the annex.** This is where a
reader can check what each clause rests on, and where the limits of the set are stated.

State as at 31 August 2026.

---

## 1. Two tiers of evidence, and why this note distinguishes them

This set is unusual: it rests on evidence of two different strengths, and the distinction
is load-bearing.

### Tier 1 - held in full and read directly

| Instrument | Detail |
|---|---|
| **DIFC Regulation 10 - Accreditation and Certification Framework For Autonomous and Semi-Autonomous Systems Processing Personal Data** | Issued by the Commissioner of Data Protection, Dubai International Financial Centre. 121 pp, read in full |

**Everything in policy Sections 4 to 13 and 15 to 21, and in annex A2 to A8, rests on
this document.** Twenty-seven substantive passages were checked verbatim against it.

### Tier 2 - verified previously against official texts, not held in this container

The breach positions for the three regimes, and the federal scope exclusions, were
verified in earlier work against **official government sources** - the UAE legislation
portal copy of the federal decree-law, and the ADGM and DIFC instruments transcribed into
the platform's corpus. Those texts are **not present in the container used to write this
set**.

**This note states them, marks them as tier 2, and does not go beyond what was verified.**
Policy 14 and 22.2 carry them; nothing else in the set depends on them.

### Tier 3 - not held at all

Regulation 10 itself; a current consolidation of the DIFC data protection law; the
federal Executive Regulations (not issued); the financial services regulators' rules in
either zone. Section 7 below.

**The reason for the distinction:** a policy that cites everything at the same confidence
teaches its reader nothing about where to check. This set marks the seams.

## 2. The structural finding - the UAE is three regimes

Stated first because misapplying it is the most consequential error available in this
jurisdiction, and because it has been made in print.

| Regime | Regulator | Breach obligation | Evidence tier |
|---|---|---|---|
| **DIFC** | DIFC Commissioner of Data Protection | **As soon as practicable in the circumstances. No fixed period.** Trigger: a breach that compromises a data subject's confidentiality, security or privacy | 2 |
| **ADGM** | ADGM Commissioner | **72 hours** from awareness. Disapplied where the breach is unlikely to result in a risk | 2 |
| **Federal** | UAE Data Office | Notify the Bureau on becoming aware, **within the period and in accordance with the measures and requirements set by the Executive Regulations**. **Those Regulations have not been issued**, so no period is established | 2 |

**Three regimes, three different answers to the same question.** The DIFC's is an
absence of a period established by reading the statute, not a gap in research - which is
why policy 14.1 says so explicitly and annex A9.2 requires the reasoning behind any
interval to be contemporaneous.

**The free zones are an exclusion from the federal regime, not a variation on it.** The
federal scope provision excludes free-zone companies that have their own data protection
law. It also excludes government data, security and judicial authorities, personal
purposes, **health data governed by its own legislation**, and **banking and credit data
governed by its own legislation** - the last two mattering directly to a financial-sector
organisation, and carried at policy 3.5.

**Being in a zone does not put an entity outside the federal regime for every purpose.**
In-zone entities commonly process some personal data outside the zone. Policy 3.4 requires
a per-processing determination; annex A9.4 requires the incident process to apply the
correct clock to each.

## 3. The held Framework - what it is and what it does

### 3.1 Its place in the structure

The Framework "serves to implement Articles 50 and 51 of the Law regarding the
requirement under Regulation 10.3.3(a) to certify Systems used in High Risk Processing
Activities". It sets out **Part 1: Accreditation** - how an organisation becomes an
Accredited Certification Body - and **Part 2: Certification** - how such a body certifies
an applicant's System.

**The operative prohibition it implements**, as the Framework states it: "The Regulations
mandate that **no person may use, operate, provide, offer or otherwise make available for
commercial use a System to engage in High Risk Processing Activities unless all audit and
certification requirements established by the Commissioner are satisfied.**"

Policy 1.2 and Section 5 rest on that sentence. It is a licence-style gate, not a
documentation duty.

**"The timeline for implementing the Framework is at the discretion of the
Commissioner."** Policy 5.8 and 21.2 state this and decline to treat it as a reason to
defer readiness; annex A4.5 requires the committee to record the Commissioner's current
position at each meeting.

### 3.2 The definition of a System, and what it excludes

The Framework's definitions table:

> **"System"** - Any machine-based system operating in an autonomous or semi-autonomous
> manner, that can: (i) Process Personal Data for human-defined purposes or purposes that
> the system itself defines, or both; and (ii) generate output as a result of or on the
> basis of such Processing.

It continues: the definition "has been adapted on the basis of the OECD guidelines and
the Regulation of the European Union on harmonised rules on AI ('EU AI Act') to encompass
systems that are capable of autonomous or semi-autonomous operation. **The Law already
contains provisions governing the use of automated Processing, so it is not intended that
purely automated systems (i.e. systems which have no degree of autonomy in their
operation and whose operation is deterministically controlled by humans) should be
captured in this definition.**"

**This is the most important boundary in the set, and it is not the boundary other
frameworks draw.** Autonomy is the trigger, not automation, not risk, not scale. Policy
Section 4 turns it into an operational test with a worked table, and 4.5 records the
consequence that a tool can become a System without being replaced - which is exactly
what a vendor does when it adds tool-use, retrieval, memory or planning.

**"Certification Applicant"** means "any Controller or Processor that is processing
personal Data through a System for commercial purposes that qualifies as High Risk
Processing Activities, that applies for certification of a System".

### 3.3 The three roles, quoted from Regulation 10.1.1

The Framework reproduces these verbatim, which is why the policy can state them:

> **"Deployer"** means, with respect to a System, the natural or legal person (i) under
> whose authority or on whose direction or for whose benefit the System is operated, or
> (ii) **who receives the benefit of the operation of the System or any output generated
> by the System** in each case without regard to whether or not the System is operated,
> supervised or hosted by such person, or such person defines or determines any of the
> purposes of which Personal Data is Processed by such System.

> **"Operator"** means a Provider that operates or supervises a System on behalf or
> otherwise for the benefit, and on the direction of a Deployer, in each case without
> regard to whether or not that Provider exercises any control over the Processing of
> Personal Data by the System.

> **"Provider"** means a natural or legal person that develops a System or procures that
> a System is developed for or on behalf of such person, in each case with a view to
> providing, commercialising or otherwise making such System available to Operators or
> Deployers.

**The Deployer limb is deliberately wide**: receiving the benefit of the output is
enough, whether or not you host the System or set its purposes. Policy 6.2 and annex
A2.2 draw the conclusion - "we only use the vendor's product" confirms the role rather
than avoiding it.

### 3.4 Certification mechanics

| Provision | Requirement |
|---|---|
| Part 2, Introduction | Certification by an **Accredited Certification Body**, or by the Commissioner in exceptional circumstances arising from the absence or unavailability of an accredited body. Applications submitted **in English** with supporting documentation |
| Part 2, Introduction | **"The certification is valid for three (3) years from the date of initial certification."** |
| Part 2, Introduction | The Commissioner retains authority to conduct **periodic risk-based reviews**, triggered by amendments to the criteria, significant changes to the System, **recurring verified complaints about use of the System that negatively impacts Data Subjects**, or failure to adhere to the conditions of certification |
| Part 2, Introduction | **Article 20 Prior Consultation** is available before deploying, operating or providing a System |
| 4.2 | Audit confirming effectiveness **"at least once in during the three (3) year validity"** (drafting as in the source) |
| 4.4 | Where the certification body assesses audits should be more frequent, it must notify the applicant **"no less than thirty (30) days prior to the compliance audit"** |
| 3.3 | The applicant may indicate it is certified **only while the certification is valid** and has not expired, been revoked or been modified such that it is no longer valid |
| 4.5 | None of this precludes the Commissioner's Office from inspecting for general compliance under its own methodology |

Policy Section 5 carries all of these.

### 3.5 The principles

Requirement 1's explanatory note: the certification body assesses that the System
"adheres, throughout the lifecycle of the System, to the fundamental principles of
**fairness, transparency, ethics, security, data quality, necessity and proportionality,
risk-assessment and accountability**".

**Requirement 1.1** requires deployment "in accordance with an overarching governance
document that details requirements for adherence to the principles of fairness,
transparency, accountability, security, and ethics, or sufficiently similar concepts
outlined in Regulation 10.3.1". Policy 9.1 makes the policy and annex that document.

## 4. The eight certification requirements under Requirement 1

| # | Requirement | Carried at |
|---|---|---|
| **1.1** | Overarching governance document evidencing the principles | Policy 9.1 |
| **1.2** | **Risk-based approach to determine the necessity of High Risk Processing through this System "rather than through a different, lower risk System"**; then assess whether risks are catalogued, whether collection and processing is necessary and proportionate, and whether measures effectively mitigate the impact | Policy 9.3-9.4 |
| **1.3** | Transparency and fairness to data subjects; **evidence of meaningful notice**; particulars per Article 29 and Regulation 10.2.2 | Policy 10.1-10.4 |
| **1.4** | Accountability mechanisms under a testing framework, delineating roles, responsibilities and System design; **supply-chain transparency responsibilities must be clear**; a register per Regulation 10.2.2(c)-(g) | Policy 10.7, 16.3-16.4 |
| **1.5** | **Measures to identify and mitigate risks of bias and discrimination** | Policy 13.1-13.3 |
| **1.6** | Data accurate, quality-assessed, reliable, relevant, limited to purpose; **human intervention designed in where required** | Policy 13.4-13.5 |
| **1.7** | Appropriate security preventing breaches causing **"reputational, psychological, financial, professional, or other types of harm"** | Policy 14.7 |
| **1.8** | **Active monitoring** of use and quality of collected data; **review or regular model tuning**; a mechanism for giving and receiving updates to and from third parties | Policy 13.6 |

**The evidentiary standard at 1.2 is explicit and worth quoting**: the acceptable evidence
includes "An AI Data Protection Impact Assessment that assesses the necessity of the
Systems...; identifies associated risks; includes management actions plans to address how
controls have been integrated into development process **(and evidence that controls have
been integrated)**; and ensures compliance with the Law."

Policy 9.6 and annex A4.4 draw the operational conclusion: **this cannot be met by a
document written after the fact.** The assessment must show controls were integrated
during development and evidence that they were.

**The notice particulars at 1.3 are the ones no ordinary privacy notice contains.**
Acceptable evidence includes a notice incorporating Regulation 10.2.2(b) elements,
"particularly regarding the human-defined purposes for Processing, **the human defined
principles on the basis of which, and all human-defined limits within which, the System
is capable of itself defining further purposes for Processing of Personal Data**, and the
codes, certifications or principles on which the Systems is designed or developed"; and
one incorporating Regulation 10.2.2(a) elements, "particularly regarding the impact of
the use of the System on the exercise of individual rights as provided under the Law in
Article 29(1)(h)(ix)".

Policy 10.2-10.3 carries both, and 10.3 makes the self-defined-purposes disclosure a bar
to deployment rather than a drafting problem.

**The bias evidence at 1.5 includes "Model modifications to address biases"** - evidence
of remediation, not of testing. Policy 13.3 states the consequence; annex A11.1 and A11.2
track findings and modifications **as a pair**, because a rising count of findings against
a flat count of modifications is the signal that testing has become performative.

## 5. Requirements 2 and 3 - the autonomy provisions

### 5.1 Requirement 2.3 - self-defined purposes

This is the most forward-looking provision in the instrument:

> An Accredited Certification Body shall assess that the System used for High Risk
> Processing acts in accordance with technical and organisational measures as well as
> appropriate safeguards and controls, including but not limited to disposal,
> vulnerability / attack detection, resilience or **failure of Human-defined processing
> purposes**. **Any Self-defined purposes generated by the System, i.e. automated
> decision-making, shall conform to a predefined set of human approved principles.**

The acceptable evidence is more specific still:

- system architecture documentation;
- **"Code review records showing assessments of how the code implements human-defined
  processing purposes and the absence of self-defined purposes"**;
- **"Processing purpose logs tracking the processing purposes of the system, documenting
  how data is being processed and ensuring that it's in line with human-defined
  purposes"**;
- documentation of the externally predefined principles and how the System conforms;
- internal policies on how the System should operate;
- **"Algorithmic audits showing the assessment of the algorithms against human-defined
  processing purposes and any corrective actions taken"**.

Policy Section 11 and annex A6 rest entirely on this. Three consequences the set draws:

- **Processing purpose logging is a design requirement** (policy 11.5, annex A6.3). A
  System that cannot produce a record of what purposes it actually processed for cannot
  evidence the requirement, and is not approved.
- **The code review must address the absence of self-defined purposes**, not merely the
  presence of the intended ones (annex A6.5).
- **Processing for a purpose outside the approved set is an incident, not a finding**
  (annex A6.6, A9.6).

### 5.2 Requirement 2 - third parties and resilience

**2.1** - the System must have been "promulgated, developed, designed or otherwise
procured subject to **enhanced due diligence**", ensuring appropriate technical,
organisational or contractual arrangements safeguard personal data, and that processors
and other third parties related to the System's function "**will implement substantially
similar measures**". Evidence includes due diligence documentation, contracts delineating
roles, transfer contracts with cross-border safeguards, and **review of the Provider's
Data Protection by Design documentation**. Annex A8.1-A8.4; A8.3 makes the last item a
bar.

**2.2** - the System must be **robust and resilient**, guarding against unauthorised
access exploiting vulnerabilities and against "faults or errors arising from changes in
the System's environment". Evidence includes policies against attacks "such as **data
poisoning**", security architecture documentation, personnel training, error-handling
mechanisms, contingency plans and incident reports. Policy 13.7.

**2.4** - compliance **by design or by default** with the law and regulations, with the
applicant demonstrating legitimate and lawful processing. Evidence includes procedures for
responding to government authority requests under Article 28.

### 5.3 Requirement 3 - governance and oversight

**3.1 - the Automated Systems Officer.** The System must be "monitored by an **Automated
Systems Officer (ASO)**, who will have at a minimum the same or similar competencies,
status, role and tasks of a Data Protection Officer (DPO) as set out in Articles 16, 17
and 18 of the Law and in relevant guidance. To distinguish the roles of DPO or similar,
**the ASO shall have the technical and organisational expertise** to ensure effective
governance and oversight of the System and ongoing validity of the certification."

The job profile must specify "technical knowledge of Systems, ethics, data protection,
risk management, complaints handling and remediation, regulatory requirements and legal
requirements".

**3.2 - routine review.** Mechanisms administered by the applicant assuring "routine
review of its processing purposes, **including the output which the System produces on the
basis of such Processing and the manner in which such output is used**, ensuring human
oversight throughout". Evidence includes complaint-handling about the System's function
and outputs, audits, training records, feedback logs, System adaptations, and an ethics
committee.

**The third limb is the one that gets dropped.** Policy 11.6 and annex A6.7 require the
business to report how output is actually consumed downstream, rather than the committee
assuming it.

**3.3** - certification may be represented only while valid; additional oversight applies
where a System is developed or deployed by an applicant within the same group as its
certification body, with conflicts monitored and independent confirmation sought.

### 5.4 Audit criteria - Requirement 4

**4.3 requires that the applicant:**

- **4.3.1** maintains consistent, up-to-date documentation showing the System is tested
  regularly against the certification requirements;
- **4.3.2** displays certification marks in accordance with applicable law, including
  Regulation 6.2 on **Unfair or Deceptive Practices** and intellectual property law;
- **4.3.3** regularly reviews the **necessity and proportionality** of the requirements
  for use of the System;
- **4.3.4** documents upgrades or changes in System architecture that maintain or improve
  the safeguards ensuring protection and transparency of System functionality;
- **4.3.5** has appointed an ASO, with **"no more than a gap of one month before the
  operation of a System for High Risk Processing or between a replacement ASO
  appointment, unless an exception to this rule for extenuating circumstances is approved
  by the Commissioner"**;
- **4.3.6** provides support so the ASO **may independently review and assess** the audit
  documentation, with a **gap analysis, risk register and management action plan** where
  required;
- **4.3.7** anything else the certification body, or the Commissioner case by case, deems
  appropriate to inspect.

**The one-month rule at 4.3.5 is the sharpest operational constraint in the instrument**,
and it is the one an organisation is most likely to breach by accident - through an
ordinary resignation. Policy 12.4 and annex A5.2-A5.4 turn it into a named deputy, a
succession process triggered on the day notice is given, and a metric counting days of
vacancy.

## 6. The assessment scheme's own structure

Appendix C organises the sample certification programme requirements into nine sections,
each with a question for the applicant and assessment criteria for the certification
body:

| Section | Subject |
|---|---|
| 0 | **Preventing Harm** |
| 1 | Notice |
| 2 | Collection Limitation |
| 3 | Uses of Personal Information |
| 4 | Choice |
| 5 | Integrity of Personal Information |
| 6 | Security Safeguards |
| 7 | Access and Correction |
| 8 | Accountability, Governance and Oversight |

**Section 0's assessment purpose** requires the applicant's personal information
protection programme to be "designed to prevent the misuse of such information", with
obligations taking account of risk and remedial measures **"proportionate to the
likelihood and severity of the harm threatened by the collection, use and transfer of
personal information"**.

Its verification criteria require the privacy practices and policy to include provisions
for compliance with Regulation 6.2, to accord with the principles of the law, to be
**"easy to find and accessible"**, and to apply to **"all personal information, whether
collected online or offline"**.

Policy Section 19 carries this, and 19.3 maps [ORGANISATION]'s controls to the nine
headings so that readiness is assessed in the terms the assessment will actually use.

## 7. Two defects in the source, recorded

### 7.1 The officer has two names

The Framework calls the role the **"Automated Systems Officer (ASO)"** at requirement 3.1
and the **"Autonomous Systems Officer (ASO)"** at audit criterion 4.3.5. The abbreviation
is the same and the role is plainly the same.

This set uses **"Automated Systems Officer"**, the form used where the role is
substantively defined, and records the variant here. Nothing turns on it, but an
organisation searching its own documents for one form will miss the other.

### 7.2 A duplicated clause

Audit criterion 4.3.5 ends: "...unless an exception to this rule for extenuating
circumstances is approved by the Commissioner, unless an exception to this rule for
extenuating circumstances is approved by the Commissioner". The clause appears twice.
**The requirement is unambiguous; the duplication is a drafting artefact** and is recorded
so that a reader comparing texts is not misled into thinking two different exceptions
exist.

A similar artefact appears at 4.2: "at least once **in during** the three (3) year
validity".

### 7.3 The issuer's own disclaimer

Every page of the Framework carries a notice stating that its content "is provided for
informational purposes only and **should not be considered complete, up to date or a
substitute for specific professional advice**".

**The issuing authority disclaims the completeness and currency of its own framework
document.** Annex A13.5 treats that as a standing reason to verify the current position
before any decision of consequence, and A4.5 requires the committee to record which
version it relies on.

## 8. Clause-by-clause basis

### 8.1 Policy

| Policy | Rests on | Tier |
|---|---|---|
| 1.1, 3.1-3.5 - three regimes | Federal scope provision; the three breach positions | 2 |
| 1.2, 5.1 - the gate | Framework, "Why is the Framework necessary?" quoting the Regulation 10.3.3 mandate | 1 |
| 1.3, 4.1-4.5 - System definition | Framework, definitions table ("System") | 1 |
| 1.4, 11.1-11.3 - self-defined purposes | Framework 2.3; 1.3 evidence (Reg 10.2.2(b) elements) | 1 |
| 3.6 - sector rules | Not asserted; recorded as not held | 3 |
| 5.2-5.5 - certification mechanics | Framework Part 2 Introduction; 4.2, 4.4, 3.3 | 1 |
| 5.6 - prior consultation | Framework Part 2 Introduction (Article 20) | 1 |
| 5.7 - High Risk determination | **Not defined in the Framework.** Routed to the data protection lead | 3 |
| 5.8, 21.2 - timeline | Framework, "What is the Framework?" | 1 |
| 6.1-6.5 - roles | Framework quoting Regulation 10.1.1 | 1 |
| 9.1-9.2 - governance and principles | Framework 1.1; Requirement 1 explanatory note | 1 |
| 9.3-9.6 - necessity and impact assessment | Framework 1.2 and its acceptable evidence | 1 |
| 10.1-10.4 - transparency and notice | Framework 1.3 and its acceptable evidence | 1 |
| 10.5-10.7 - third parties | Framework 2.1; 1.4 (supply chain clarity) | 1 |
| 11.4-11.5 - evidence of autonomy | Framework 2.3 acceptable evidence | 1 |
| 11.6-11.7 - routine review | Framework 3.2 | 1 |
| 12.1-12.5 - the ASO | Framework 3.1; 4.3.5; 4.3.6 | 1 |
| 12.6 - ASO/DPO separation | House standard | - |
| 13.1-13.3 - bias | Framework 1.5 | 1 |
| 13.4-13.5 - data quality | Framework 1.6 | 1 |
| 13.6 - monitoring and tuning | Framework 1.8 | 1 |
| 13.7 - robustness | Framework 2.2 | 1 |
| 14.1 - DIFC breach | DIFC law breach article | 2 |
| 14.2 - ADGM breach | ADGM Regulations breach section | 2 |
| 14.3 - federal breach | Federal decree-law breach article; Executive Regulations not issued | 2 |
| 14.6 - enumeration | House standard |  - |
| 14.7 - security | Framework 1.7 | 1 |
| 15.1-15.2 - human determination | House standard, supported by Framework 1.6 (human intervention designed in) | 1 |
| 15.4, 15.6 - agents | Framework definitions ("System"); 2.3; 3.2 | 1 |
| 16.3-16.4 - register and human intervention | Framework 1.4 evidence (Reg 10.2.2(c)-(g)) | 1 |
| 17 - prohibitions | House standards, except 17.1 (Framework 3.1, 4.3.5 and the Reg 10.3.3 mandate) and 17.3 (Framework 3.3) | 1 |
| 18.5 - verifying regulatory references | Section 9 of this note | 2 |
| 19.1-19.3 - preventing harm | Framework Appendix C Section 0 and its verification criteria | 1 |
| 20.4 - public-facing AI | House standards | - |

### 8.2 Annex

| Annex | Rests on | Tier |
|---|---|---|
| A2.1-A2.6 - the three determinations | Framework definitions; Reg 10.1.1 roles; the Reg 10.3.3 mandate | 1 |
| A3.1 - inventory fields | Framework 1.2, 1.3, 2.3, 3.1 | 1 |
| A4.1-A4.4 - readiness | Framework Requirement 1 evidence lists; 1.2 ("evidence that controls have been integrated") | 1 |
| A4.5 - version tracking | Framework's own disclaimer notice | 1 |
| A4.6 - prior consultation | Framework Part 2 Introduction | 1 |
| A5.1-A5.7 - the ASO | Framework 3.1, 3.3, 4.3.5, 4.3.6 | 1 |
| A6.1-A6.7 - purposes and limits | Framework 2.3; 1.3; 3.2 | 1 |
| A7.3-A7.6 - operation | Framework 1.8, 1.6 | 1 |
| A8.1-A8.5 - suppliers | Framework 2.1; 1.4 | 1 |
| A9.1-A9.4 - regime routing | The three breach positions | 2 |
| A9.6 - unapproved purpose is an incident | Framework 2.3, applied | 1 |
| A11 - metrics | House standards derived from the requirements above | - |
| A12.3 - Commissioner's exception | Framework 4.3.5 | 1 |
| A13.5 - the disclaimer | Framework's notice | 1 |

## 9. A caution about published sources - the error this jurisdiction attracts

A specific misattribution circulates widely and has appeared in professional commentary:
the phrase **"without undue delay and, where feasible, not later than 72 hours after
having become aware of it"**, attributed to the federal law's breach article.

**That wording is not in the federal decree-law.** It is European provision wording. The
real 72-hour duty in the UAE sits in **ADGM**, whose regulations adopted similar language
- which is why the sentence matches something. Commentary took a free-zone rule and
attached a federal article number to it.

Related claims that fail against the official text, all previously checked:

| Claim in circulation | Position on the official text |
|---|---|
| Breach notification is "without undue delay / 72 hours" under the federal law | The federal article defers the period to Executive Regulations |
| The federal Executive Regulations were issued in 2023 | Not issued as at the date of this note; the claim appears on vendor and consultancy pages, never with a Cabinet Decision number, never on the official portal |
| A specific maximum fine applies under the federal decree-law | No amount is in the decree-law; penalties are left to a Cabinet decision |
| A fixed subject-access response period applies under the federal law | No period is specified |
| Several article numbers commonly cited for breach, DPIA and consent | Verified against the official portal text and found misattributed |

**This is why policy 18.5 exists**, and it is worth stating plainly what it demonstrates:
a citation that verifies against a plausible secondary source and fails against the
primary text is a failure mode that predates AI tools and has been performed here by
humans, in print, on professional letterhead.

**Nothing in this set was taken from any such source.**

## 10. Not held

| What is missing | Consequence |
|---|---|
| **Regulation 10 itself** | The Framework implements it and cites 10.1.1, 10.2.2(a)-(g), 10.3.1 and 10.3.3. Where the Framework quotes, this set follows the quotation; where it only cites, **this set states the Framework's requirement and not the underlying provision** |
| **A current consolidation of the DIFC data protection law** | Articles 16, 17, 18 (DPO), 20 (prior consultation), 24 (contract clauses), 28 (authority requests), 29 (notice particulars) and 50-51 (accreditation) are cited by the Framework and **not stated in this set**. A previously held consolidation dated March 2022 predates both the 2023 amendments and Regulation 10 |
| **The definition of "High Risk Processing Activities"** | **The trigger for the entire regime.** Not defined in the Framework. Policy 5.7 routes it to the data protection lead and requires the cautious answer where uncertain |
| **The federal Executive Regulations** | **Not issued.** No federal breach period is established |
| **The full ADGM Regulations and DIFC law texts, in this container** | Tier 2 positions are stated only to the extent previously verified |
| **DFSA and FSRA rules** | **Both free zones exist to host financial institutions.** For a regulated firm the sector rules may bite harder than the data protection regime does. Annex A13.4 says so explicitly |
| **The Guidance and FAQs accompanying the Framework** | Referenced at Framework 3.1 and Part 2 Introduction; not held |
| **Guidance on Article 24 Contract Clauses** | Referenced at Framework footnote to 2.1; not held |
| **Appendix templates** | "All templates are available upon request from the Commissioner or relevant delegate" |
| **Penalties** | Not stated anywhere in this set |

## 11. What this set therefore does not say

- It does not define High Risk Processing Activities.
- It does not state the content of Regulation 10 or of the DIFC law articles the
  Framework cites.
- It does not state any penalty for contravention.
- It states, for ADGM and the federal regime, **the breach position and nothing else**.
- It does not cover the financial services regulators' requirements in either zone.
- It does not state a federal breach period, because none is established.
- It does not assume the certification framework is currently being enforced, nor that it
  is not - the timeline is at the Commissioner's discretion.

## 12. Method

Every tier 1 provision cited above was read in the supplied text of the Framework;
twenty-seven substantive passages were checked verbatim. Tier 2 positions were verified
in earlier work against official government sources and are marked as such throughout.
Nothing in this set was taken from a law-firm briefing, a vendor page, a comparative
summary, or any other secondary source - section 9 explains why that matters more here
than usual.

## 13. Standing caveat

No provision cited in this set has been reviewed by qualified counsel. These documents
are educational templates, are written for a DIFC-registered entity, and do not
constitute legal advice.
