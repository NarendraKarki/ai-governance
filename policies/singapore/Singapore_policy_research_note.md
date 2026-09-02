# Research note - Singapore AI policy set

Working note supporting the [ORGANISATION] Artificial Intelligence Acceptable Use
Policy (Singapore) v1.0 and the AI Governance Enterprise Annex (Singapore) v1.0.

**Section numbers live here, not in the policy or the annex.** This is where a reader
can check what each clause rests on, and where the limits of the set are stated.

State as at 31 August 2026.

---

## 1. The single instrument this set rests on

**Personal Data Protection Act 2012, 2020 Revised Edition**, as amended, current to
Act 19 of 2025 (commenced 5 December 2025). Supplied as a Word document reproducing
the full enacted text with schedules and legislative history.

There is no second instrument in this set. Everything asserted in the policy and the
annex resolves to a provision of that Act. Section 5 of this note lists what is not
held, and Section 6 lists what the set therefore does not say.

## 2. What shapes the Singapore position

### 2.1 There is no artificial intelligence statute

The Act is technology-neutral. It contains no reference to artificial intelligence,
machine learning, automated decision-making, algorithmic systems, or profiling. A
full-text search of the enacted text returns no occurrence of "artificial
intelligence" or "automated decision".

This is not a gap in the research. It is the position, and it determines the shape of
the policy. Every AI obligation in the policy reaches AI as an obligation about
personal data, and the policy says so at Section 4 rather than implying an AI regime
that does not exist.

Two consequences follow that the policy states explicitly at 4.2:

- **No prohibited-practice list.** Policy Section 6 is a set of house prohibitions and
  is labelled as such.
- **No general right against automated decisions and no right to an explanation.**
  Policy Section 10 is a house standard and is labelled as such at its head.

### 2.2 The reasonable person standard

**Section 11(1).** In meeting its responsibilities under the Act, an organisation must
consider what a reasonable person would consider appropriate in the circumstances.

The same standard recurs as a condition of specific exceptions - First Schedule Part 5
paras 1(3)(b) and 1(4)(b), Second Schedule Part 2 Division 2 para 1(2)(b) - and in
section 18(a) on purpose limitation. It is the reason the policy asks for recorded
judgement rather than a checklist, and the reason policy 20.1 can rest a fairness
standard on the statute's own logic without claiming a discrimination provision the
Act does not contain.

### 2.3 Individual criminal liability

This is the most distinctive feature of the Singapore position for an acceptable use
policy, and the reason policy Section 11 exists as its own section.

| Provision | Conduct | Penalty |
|---|---|---|
| **s.48D(1)** | An individual discloses, or causes disclosure of, personal data in the possession or under the control of an organisation, where not authorised by the organisation, knowing that or reckless as to it | Fine not exceeding $5,000, or imprisonment not exceeding 2 years, or both |
| **s.48E(1)** | An individual uses such personal data without authorisation, knowingly or recklessly, **and thereby obtains a gain, causes harm to another individual, or causes a loss to another person** | Same |
| **s.48F(1)** | An individual takes action to re-identify, or cause re-identification of, the person to whom anonymised information relates, without authorisation, knowingly or recklessly | Same |

The defences are at ss.48D(2), 48E(2) and 48F(2) and are narrow: broadly, that the
data was already publicly available; that the conduct was permitted or required by
other law or by court order; or a reasonable belief in a legal right to act. For
re-identification, s.48F(2)(c) adds a defence where the accused reasonably believed
the re-identification was for a **specified purpose** and notified the Commission or
the organisation as soon as practicable.

**The "specified purposes" are exhaustively listed in the Eleventh Schedule** (s.48F(4)):
testing the effectiveness of anonymisation; testing the integrity and confidentiality
of anonymised information; and assessing, testing or evaluating the systems and
processes for safeguarding it. Policy 12.2 tracks these three and adds nothing.

The load-bearing word in all three offences is **authorised by the organisation**. The
Act does not define what authorisation looks like; it leaves the organisation to set
it. That is why policy 11.3 identifies the approved tools list as the boundary of
authorisation, and why annex A7.3 requires every exception to name whom and what it
covers - an exception that blurs the boundary increases an individual's exposure
rather than reducing it.

### 2.4 The organisation / data intermediary split

- **s.4(2)** - Parts 3, 4, 5, 6 (**except ss.24 and 25**), 6A (**except ss.26C(3)(a)
  and 26E**) and 6B impose no obligation on a data intermediary processing on behalf
  of and for the purposes of another organisation **pursuant to a contract evidenced
  or made in writing**. So a data intermediary carries: protection (s.24), retention
  (s.25), notification to the organisation it serves (s.26C(3)(a)), and, for public
  agency work, s.26E.
- **s.4(3)** - the organisation has the same obligation for personal data processed on
  its behalf and for its purposes by a data intermediary **as if it had processed the
  data itself**.

Policy 2.1 and annex A5.1-A5.3 rest on these. The written-contract condition in s.4(2)
is the reason annex A5.1 treats the contract as constitutive rather than
administrative: without it the supplier is not a data intermediary and the reduced
obligation set does not apply to it.

**s.4(1)** excludes from Parts 3-6B: an individual acting in a personal or domestic
capacity; **an employee acting in the course of employment with an organisation**; a
public agency; and prescribed cases. The employee exclusion is why the personal
exposure in ss.48D-48F matters so much: an employee is outside the data protection
obligations but squarely inside the offences.

**s.4(5)** - business contact information is outside Parts 3, 4, 5, 6 and 6A except
where expressly mentioned. **s.4(4)** - the Act does not apply to personal data in a
record at least 100 years old, or about a person dead more than 10 years (with
disclosure provisions and s.24 applying within 10 years).

## 3. Clause-by-clause basis

### 3.1 Policy

| Policy | Rests on |
|---|---|
| 1 - the three framing features | s.11(1); ss.48D-48F; absence of any AI provision in the Act |
| 2.1 - role | ss.4(2), 4(3); definition of "data intermediary", s.2(1) |
| 3.2 - written contract | s.4(2) ("pursuant to a contract which is evidenced or made in writing") |
| 4.1 - what binds | ss.13, 18, 20, 23, 24, 25, 26, 21, 22, 26C, 26D, 11(3), 11(5) |
| 4.2 - what the law does not give | Absence of ADM provisions; absence of a prohibition list; absence of a special-category regime; Part 6B and the Twelfth Schedule - see 4.2 of this note |
| 4.3 - guidance | s.49(1)-(3) |
| 6 - prohibitions | House standards. 6.5 additionally tracks s.48F(1) |
| 7.2 - consent | ss.13, 14(1), 14(2), 14(3) |
| 7.3 - other bases | s.15 (deemed); s.15A (deemed by notification); First Sch Pt 3 para 1 (legitimate interests); First Sch Pt 5 and Second Sch Pt 2 Div 2 (business improvement); Second Sch Pt 2 Div 3 (research); s.17(1) generally |
| 7.4 - the assessment | s.15A(4)(a) and (5); First Sch Pt 3 para 1(2)(a) and 1(3) |
| 7.5 - high sensitivity | House standard. The Act has no special-category regime |
| 7.6 - employment | ss.20(4) and 20(5); First Sch Pt 3 para 10 |
| 8 - transfers | s.26(1); s.26(2)-(4) on exemption |
| 9.1-9.3 - accuracy | s.23(a) and (b) |
| 9.4 - derived output | s.2(1) "derived personal data"; Fifth Schedule (no exception); Sixth Schedule para 1(f) (exception). House standard to disapply the exception |
| 10 - automated decisions | House standard throughout. No statutory basis, stated in the policy text |
| 11 - personal liability | ss.48D(1), 48E(1), and their defences at 48D(2), 48E(2) |
| 12 - re-identification | s.48F(1); s.48F(2)(c); Eleventh Schedule |
| 13 - retention | s.25 |
| 14 - verification | House standard, supported by s.23 where output concerns individuals |
| 15 - security | s.24(a) and (b) |
| 16 - breach | ss.26A, 26B(1)-(4), 26C(2)-(4), 26D(1)-(2), 26D(5)-(7), 26C(3)(a) |
| 17.1-17.4 - access and correction | ss.21(1)-(7), 22(1)-(5), 22A(1)-(2) |
| 17.2a - access exceptions | s.21(2), Fifth Schedule para 1(a)-(j); s.21(6)-(7) on notifying |
| 17.5-17.7 - correction limits | s.22(6) (opinion); s.22(7) and Sixth Schedule para 1(f) (derived); s.2(1) limb (b) on prescribed means |
| 18 - IP and records | House standards |
| 19 - customer-facing | House standards, stated as such at 19.2 |
| 20 - fairness | House standard, stated as such at 20.1 |
| 21 - monitoring | House standard; no monitoring provision in the Act |
| 22 - responsibilities | ss.11(2)-(6), 12 |

### 3.2 Annex

| Annex | Rests on |
|---|---|
| A1.3-A1.4 - the designated individual | ss.11(3), 11(4), 11(5), 11(5A), 11(6) |
| A3 - assessment register | s.15A(4)(a), 15A(5); First Sch Pt 3 para 1(2)(a), 1(3) |
| A3.5 - business improvement | First Sch Pt 5 para 1(3)-(4); Second Sch Pt 2 Div 2 para 1(2), 1(4) |
| A3.6 - research | Second Sch Pt 2 Div 3 para 1(c) |
| A5.1-A5.3 - suppliers | ss.4(2), 4(3) |
| A5.5 - breach timing | ss.26C(2), 26C(3)(a), 26D(1) |
| A5.6 - acting as intermediary | ss.4(2), 26C(3)(a) |
| A6 - cross-border | s.26(1) |
| A7.2 - no exception for offences | ss.48D, 48E, 48F |
| A9.1-A9.3 - requests | ss.21, 22(2)(b), 22(5), 22A(1) |
| A9.2a - derived output | s.2(1); Fifth Schedule; Sixth Schedule para 1(f) |
| A9.2b - access exceptions | s.21(2); Fifth Schedule para 1(g) in particular |
| A11.1 - complaints process | s.12(b) and (d)(ii) |
| A11.3 - mediation | s.48G(1) |
| A11.4 - private action | s.48O(1) |
| A12.1-A12.2 - enforcement | ss.48I, 48J, 48L, 48O |
| A12.3 - mitigation | s.48J(6)(d), (e), (g) |
| A12.4 - undertakings | s.48L |

## 4. The findings worth recording

### 4.1 The breach clock runs from the assessment, not from discovery

**s.26C(2)** - where an organisation has reason to believe a data breach affecting
personal data in its possession or under its control has occurred, it must conduct,
**in a reasonable and expeditious manner**, an assessment of whether the breach is
notifiable.

**s.26D(1)** - where the organisation assesses that the breach is notifiable, it must
notify the Commission **as soon as is practicable, but in any case no later than 3
calendar days after the day the organisation makes that assessment**.

The 3-day period therefore starts at the assessment. There is no fixed statutory
deadline running from discovery; the discipline on that leg is the expeditiousness
requirement in s.26C(2). Policy 16.5 states both, because stating only the 3 days
invites the organisation to start the clock late, and stating only the expeditiousness
duty loses the hard deadline.

Two further points the policy carries:

- **s.26B(4)** - a breach relating to unauthorised handling of personal data **only
  within** an organisation is deemed not to be a notifiable breach. Policy 16.6.
- **s.26C(3)(a)** - a data intermediary must notify the organisation it processes for
  **without undue delay**; the assessment under s.26C(3)(b) is then that
  organisation's. Policy 16.7 and annex A5.5-A5.6.

**The notifiability thresholds are not in the Act.** s.26B(2)(a) deems significant
harm where the breach concerns "prescribed personal data or class of personal data";
s.26B(3)(a) deems significant scale where it affects "not fewer than the prescribed
number of affected individuals". Both are prescribed by subordinate legislation which
is not held. Policy 16.3 therefore describes the test and routes the judgement to the
data protection lead rather than stating a category list or a number.

Notification to individuals: **s.26D(2)** requires it for breaches notifiable on the
significant-harm limb (s.26B(1)(a)). **s.26D(5)** disapplies it where remedial action
taken after the assessment, or a technological measure implemented before the breach,
renders significant harm unlikely. **s.26D(6)** prohibits notification where a
prescribed law enforcement agency so instructs or the Commission so directs.
**s.26D(7)** allows the Commission to waive it on written application.

### 4.2 A part and a schedule are enforced but absent

**Part 6B is cross-referenced throughout the Act and its provisions are not in the
enacted text.** It appears in s.4(1), s.4(2), s.4(6)(a) and (b), s.48I(1)(a) and (2),
s.48J(1)(a), s.48L(1)(a) and s.48O(1) - including in the enforcement provisions, so
the Commission's direction and financial-penalty powers reach a Part whose content the
text does not carry. No Part 6B heading appears between Part 6A and Part 7.

**The same pattern appears in the schedules.** The First Schedule's marginal reference
reads "Section 17(1) and Fifth and Twelfth Schedules". There is no Twelfth Schedule in
the text; the schedules run to the Eleventh.

The legislative history records Act 40 of 2020 (Personal Data Protection (Amendment)
Act 2020) as commencing 1 February 2021 **except sections 14, 24, 39, 42, 44 and 45**,
with a further date of 1 October 2022. Provisions carrying the marker
`[Act 40 of 2020 wef 01/10/2022]` in the text include the financial penalty caps at
s.48J(3), (4), (4A) and (5A).

**The obvious inference is that Part 6B and the Twelfth Schedule are the data
portability regime, enacted but not brought into force.** That inference is *not
verified in this set*: it would require the Amendment Act and the relevant
commencement notification, neither of which is held. What is verified is the fact -
the Act enforces a Part it does not contain.

Policy 4.2 therefore states the observable fact and commits to tracking it, without
asserting what Part 6B says or when it will arrive.

### 4.3 The business improvement basis splits on corporate form

This is the basis an organisation is most likely to reach for when it wants to train,
tune or evaluate an AI system on personal data it already holds. It is in two places
and they do not overlap.

**First Schedule Part 5** applies where X is a **corporation** and the data is
collected from, used, or disclosed by a **related corporation** Y, for the relevant
purposes at para 1(2): improving or developing goods or services; improving or
developing methods or processes for operations; learning about behaviour and
preferences; identifying or personalising goods and services. Conditions:

- para 1(3) for collection and disclosure - the purpose cannot reasonably be achieved
  without the data in individually identifiable form; a reasonable person would
  consider it appropriate; **and X and Y are bound by a contract, other agreement or
  binding corporate rules requiring appropriate safeguards**;
- para 1(4) for use - the first two conditions only;
- para 1(5) - for the behaviour-and-preferences and personalisation purposes, P must
  be an existing or prospective customer.

**Second Schedule Part 2 Division 2** applies to **use** by an organisation, on the
conditions at para 1(2)(a) and (b) - necessity in identifiable form, and
reasonableness - **and para 1(4) excludes a corporation from the meaning of
"organisation" for that Division**.

So a corporation relies on the First Schedule Part 5 route; a non-corporation
organisation relies on the Second Schedule Part 2 Division 2 route. Policy 7.3 and
annex A3.5 state that availability turns on corporate form and on whether data moves
between related entities, and route the determination to the data protection lead
rather than presenting a single rule.

**Neither route covers disclosure to an unrelated third party**, which is the shape of
sending personal data to an external AI vendor for that vendor's own model
development. That is one reason policy 13.4 forbids sending personal data to a
supplier that trains on input.

### 4.4 Derived personal data: accessible, but not correctable

This is the finding with the most direct bearing on AI output about people, and it is
easy to miss because it lives in a schedule rather than in a section.

**s.2(1)** defines **"derived personal data"** as personal data about an individual
that is derived by an organisation **in the course of business** from other personal
data - about that individual or another - in the organisation's possession or control;
excluding personal data derived using any **prescribed** means or method.

An AI-inferred attribute, a propensity score, a risk rating, a segment assignment, a
model-generated summary of a person's history - each is derived by the organisation
from personal data it holds. Each is derived personal data.

The two schedules then diverge.

| Right | Provision | Derived personal data |
|---|---|---|
| Access | s.21(2), **Fifth Schedule** para 1(a)-(j) | **Not excepted.** Access applies |
| Correction | s.22(7), **Sixth Schedule** para 1(f) | **Excepted.** Section 22 does not apply |

So an individual can obtain an AI-generated inference about themselves and has **no
statutory right to have it corrected**. The Fifth Schedule's ten exceptions cover
evaluative opinion data, examination material, private trusts, arbitration and
mediation, live prosecutions, legal privilege, **confidential commercial information
whose disclosure could harm the organisation's competitive position**, live
investigations, mediator and arbitrator material, and repetitious, disproportionate,
trivial or vexatious requests. Derived personal data is not among them. The Sixth
Schedule's six exceptions repeat the first five of those and add derived personal data
at para 1(f).

Policy 9.4 and 17.5 record the position and then decline to rely on the correction
exception, as a house standard. Two reasons make that the right call rather than
caution for its own sake:

- The **accuracy obligation at s.23** is unaffected by the correction exception. Where
  derived output about a person is likely to inform a decision affecting them, or to be
  disclosed onward, the organisation still owes a reasonable effort to accuracy. An
  organisation that refuses to correct a demonstrated error, and then acts on it, has
  not discharged s.23 merely because s.22 did not require the correction.
- The definition's carve-out at limb (b) - data derived using **prescribed** means or
  methods - can narrow the exception by subordinate legislation that is **not held**.
  A policy built on the exception would be built on a boundary the set cannot see.
  Policy 17.7 states this.

The Fifth Schedule para 1(g) exception is separately worth noting for AI: information
whose disclosure would reveal confidential commercial information capable of harming
the organisation's competitive position. Model weights, architecture and feature sets
plausibly sit inside it; the individual's own inferred attribute plausibly does not.
Annex A9.2b routes that judgement to the data protection lead and puts refusals on
that ground in front of the committee, because it is the exception most available to
misuse.

### 4.5 The research basis is closed to decision-bearing AI

**Second Schedule Part 2 Division 3** permits use for a research purpose only where:
the purpose cannot reasonably be accomplished without identifiable data; there is a
clear public benefit; **the results of the research will not be used to make any
decision that affects the individual**; and published results do not identify the
individual.

The third condition is decisive. A model developed under this basis cannot then inform
decisions about the individuals whose data trained it. Annex A3.6 records the
confirmation for that reason.

### 4.6 Assessments are conditions of lawfulness

Both s.15A(5) and First Schedule Part 3 para 1(3) require the organisation not merely
to identify adverse effects but to "**identify and implement** reasonable measures" to
eliminate, reduce the likelihood of, or mitigate them.

The verb is *implement*. An assessment that lists mitigations left undone does not
satisfy the paragraph, and the basis it was meant to support is unavailable. Annex
A3.2 turns this into a register field with an implementation date, and A3.4 requires
the assessment to precede the processing - s.15A(4) ("must, **before** collecting,
using or disclosing") and First Schedule Part 3 para 1(2)(a) ("**before** collecting,
using or disclosing") both say so expressly.

### 4.7 Enforcement exposure

**s.48J(3)** - a financial penalty on an organisation for contravening Parts 3, 4, 5,
6, 6A or 6B must not exceed the maximum prescribed, which in no case may be more than:

- **(a)** where the organisation's annual turnover in Singapore exceeds **$10 million**
  - **10% of that annual turnover**; or
- **(b)** in any other case - **$1 million**.

Turnover is ascertained from the most recent audited accounts available at the time
the penalty is imposed (s.48J(5A)). Both figures carry `[Act 40 of 2020 wef
01/10/2022]`.

Other caps, for completeness: s.48J(4) for Part 9 (Do Not Call) contraventions -
$200,000 for an individual, $1 million otherwise; s.48J(4A) for s.48B(1) - $200,000
for an individual, 5% of Singapore turnover where that exceeds $20 million, otherwise
$1 million.

**s.48J(2)** - the financial penalty power does not apply where the contravention is
itself an offence under the Act. The individual offences at ss.48D-48F are therefore
prosecuted, not penalised administratively.

**s.48J(6)** lists the factors the Commission must weigh, including at (e) whether the
organisation "had, despite the noncompliance, implemented adequate and appropriate
measures for compliance". Annex A12.3 rests on this: the registers are mitigation
evidence.

**s.48O(1)** - a person who suffers loss or damage directly as a result of a
contravention of Parts 4, 5, 6, 6A or 6B may bring proceedings in their own right.
**s.48G(1)** - the Commission may refer a complaint to mediation **without the consent
of either party**.

### 4.8 Advisory guidelines are interpretation, not law

**s.49(1)** - the Commission may issue written advisory guidelines indicating the
manner in which it will interpret the Act. s.49(2) allows variation or revocation.
s.49(3) requires publication but provides that failure to publish does not invalidate
the guidelines.

No guidelines are held in this set. Policy 4.3 therefore commits the data protection
lead to record and assess guidance without asserting any of its content. **This
matters more in Singapore than the absence of guidance usually would**, because the
Commission has issued AI-specific advisory guidelines and this set does not hold
them - see 5 and 6 below.

## 5. Not held

| What is missing | Consequence |
|---|---|
| **Personal Data Protection Regulations 2021** | The prescribed thresholds at s.26B(2)(a) and s.26B(3)(a); the prescribed transfer requirements under s.26(1); the prescribed access-rejection time under s.21(6); the preservation period under s.22A(1); prescribed forms and manner under s.26D(3)-(4); **and the prescribed means or methods that fall outside "derived personal data" under s.2(1) limb (b)**. **This is the largest gap in the set.** Policy 8.5, 16.3, 17.4 and 17.7 describe the obligation and route the specifics to the data protection lead rather than stating figures |
| **PDPC advisory guidelines on AI** | The Commission's stated interpretation of how the Act applies to AI recommendation and decision systems is not held. Nothing in this set asserts its content |
| **PDPC Model AI Governance Framework** | Not held, not cited, not asserted |
| **Personal Data Protection (Amendment) Act 2020, and commencement notifications** | Why Part 6B and the Twelfth Schedule are absent cannot be verified. See 4.2 |
| **Sector regulator instruments** | Technology risk, outsourcing and operational resilience requirements imposed by sector regulators on the firms they supervise. Annex A13.2 says so explicitly rather than gesturing at it |
| **Employment law, and anti-discrimination instruments** | Policy 20 and 21 carry no citation and are house standards |
| **Intellectual property law** | Policy 18 is a house standard; no statutory basis is asserted |
| **The Twelfth Schedule and Part 6B themselves** | Their content is unknown to this set |
| **Case law and enforcement decisions** | No decision of the Commission or the courts is relied on anywhere |

## 6. What this set therefore does not say

- It does not state what counts as significant harm or significant scale.
- It does not state the transfer conditions, only that they exist and are prescribed.
- It does not state the preservation period for refused access requests.
- It does not state which means or methods of derivation are prescribed out of the
  definition of derived personal data.
- It does not assert any position taken by the Commission in guidance or in a decision.
- It does not assert what Part 6B or the Twelfth Schedule contain, or when they arrive.
- It does not cover sector-regulated firms' technology risk obligations.
- It does not assert any AI-specific obligation, because there is none in the Act.

## 7. Method

Every provision cited above was read in the supplied text of the Act. Nothing in this
set was taken from a web page, a summary, a law-firm note, or a comparative overview.
Where a figure or a threshold is prescribed by subordinate legislation that is not
held, the set names the gap instead of filling it from any other source.

## 8. Standing caveat

No provision cited in this set has been reviewed by qualified counsel. These documents
are educational templates and do not constitute legal advice.
