# Research note - United States AI policy set

Working note supporting the [ORGANISATION] Artificial Intelligence Acceptable Use
Policy (United States) v1.0 and the AI Governance Enterprise Annex v1.0.

**Provision identifiers live here, not in the policy or the annex.** This is where a
reader can check what each clause rests on, and where the limits of the set are
stated.

State as at 3 September 2026.

---

## 1. The instruments this set rests on

All held in full and read directly; hashes and retrieval details in the source
register.

| Instrument | What it grounds |
|---|---|
| **Colorado SB 24-205** (Consumer Protections for Artificial Intelligence, adding part 17 to article 1, title 6, CRS) - signed act | The high-risk AI regime: definitions, developer and deployer duties, consumer notices, enforcement |
| **Colorado SB 25B-004** - signed act, approved 28 August 2025 | The amendment that moved every operative date; read with SB 24-205, never without it |
| **CCPA as amended (Cal. Civ. Code Title 1.81.5, ss. 1798.100-1798.199.95)** - leginfo print | The California personal-information baseline |
| **CPPA Regulations, approved text (Cal. Code Regs., tit. 11, div. 6)** - Approved Regulations Text, final rulemaking of 22 September 2025 | ADMT, risk assessments, cybersecurity audits, service-provider contracts, consumer request machinery |
| **FTC Act s.5 (15 U.S.C. 45)** - US Code 2024 ed. | The unfair-or-deceptive baseline that reaches AI without an AI statute |
| **FCRA (15 U.S.C. 1681 et seq., subchapter III)** - US Code 2024 ed. | Adverse action machinery where consumer-report data feeds AI decisions |
| **COPPA Rule (16 CFR 312)**, **GLBA Safeguards Rule (16 CFR 314)**, **HIPAA Privacy/Security (45 CFR 164)** - eCFR, current to 31 Aug 2026 | The sectoral baseline points the policy cites |
| **NIST AI RMF 1.0 (AI 100-1)** and **Generative AI Profile (AI 600-1)** | Guidance tier - but see finding 4.2: Colorado's statute gives the RMF legal effect |

## 2. The structural finding - a patchwork, stated as one

There is no comprehensive federal AI or privacy statute in this corpus, because
none exists to hold. The set is scoped to the federal sectoral baseline plus
California and Colorado, and says so in policy 1.1 and 22.1. Two consequences:

- **Other states are named as not held**, not silently blended. State AI and
  employment-AI laws exist beyond this corpus and nothing here reflects them.
- **The federal baseline is sectoral.** The FTC Act's unfairness and deception
  prohibition is the general backstop (policy 3.1, 18.5); everything else attaches
  by data and activity.

## 3. Clause-by-clause basis

### 3.1 Policy

| Policy | Rests on |
|---|---|
| 1.2, 4.1-4.2 - Colorado test | CRS 6-1-1701(9) (high-risk), (3) (consequential decision), (11) (substantial factor); exclusions 6-1-1701(9)(b) |
| 1.2, 4.3, 4.5 - California test | CPPA regs s.7001 (ADMT; "substantially replace human decisionmaking"; human-involvement requirements), s.7001(ddd) (significant decision), s.7200(a) |
| 1.3, 9.5 - frameworks with legal effect | CRS 6-1-1703(2)(a)(I) (program reasonable considering NIST AI RMF / ISO 42001); 6-1-1702(1), 6-1-1703(1) (rebuttable presumption); 6-1-1706(3) (affirmative defense) |
| 3.1 - federal baseline | 15 U.S.C. 45(a); FCRA 15 U.S.C. 1681m (adverse action); 16 CFR 312; 16 CFR 314; 45 CFR 164 |
| 3.3 - "in force now" | SB 25B-004 ss.1-3: every "February 1, 2026" in CRS 6-1-1702, -1703, -1704 struck for "June 30, 2026"; approved 28 Aug 2025. See finding 4.1 |
| 3.4 - carve-outs | CRS 6-1-1705 (compliance with other law; insurers; banks; HIPAA-covered activity); CCPA statutory exemptions in Title 1.81.5 |
| 4.2 - the chatbot exclusion | CRS 6-1-1701(9)(b)(II)(R): natural-language information/referral technology excluded only if "subject to an accepted use policy that prohibits generating content that is discriminatory or harmful". See finding 4.3 |
| 6 - Level 4 boundary | The union of CRS 6-1-1701(3) areas and CPPA regs s.7001(ddd) areas |
| 7.6 - workplace inference | CPPA regs s.7150(b)(4) |
| 8.1 - purpose restriction | CPPA regs s.7002 (reasonable expectations; compatibility) |
| 8.2 - pre-use notice | CPPA regs s.7220(a)-(b), incl. notice before new ADMT processing of already-collected information |
| 8.3 - sensitive PI trigger | CPPA regs s.7150(b)(2) |
| 8.5 - training as trigger | CPPA regs s.7150(b)(6) ("intends to use" defined broadly) |
| 9.1 - assessment triggers | CPPA regs s.7150(b)(1)-(6); CRS 6-1-1703(3)(a) |
| 9.2 - assessment content | CRS 6-1-1703(3)(b)-(c) (the stricter list); CPPA regs s.7152 |
| 9.3 - cadence and retention | CRS 6-1-1703(3)(a)(II) (annual; 90 days post-modification), (3)(f) (3-year retention); CPPA regs s.7155 (before initiating; 3-year review) |
| 9.1/9.2 note - one assessment for both | CRS 6-1-1703(3)(e) (reasonably similar in scope and effect satisfies) |
| 9.4 - regulator reads them | CPPA regs s.7157 (submission; first deadline 1 April 2028 for 2026-27 assessments); CRS 6-1-1703(9) (AG 90-day demand; CORA exclusion; trade secret designation; privilege non-waiver per SB 25B-004) |
| 10.1 - pre-decision notice | CRS 6-1-1703(4)(a) |
| 10.2 - adverse decision | CRS 6-1-1703(4)(b): principal reasons incl. degree and manner of contribution, data type and sources; correction opportunity; appeal with human review where technically feasible. FCRA 15 U.S.C. 1681m in parallel where consumer reports |
| 10.3 - opt-outs | CRS 6-1-1703(4)(a)(III) (profiling opt-out cross-reference); CPPA regs s.7221 (ADMT opt-out), s.7222 (ADMT access) |
| 10.4 - public statements | CRS 6-1-1703(5) (deployer); 6-1-1702(4) (developer) |
| 10.5 - manner of notices | CRS 6-1-1703(4)(c) (direct, plain language, all business languages, accessible) |
| 11 - human determination | House standard; interacts with CPPA regs s.7001 human-involvement definition (a ratifying review is not involvement) and CRS appeal duty |
| 13.1 - contracts | CPPA regs ss.7050-7053 |
| 13.3 - developer documentation | CRS 6-1-1702(2)-(3) (statements, documentation, model cards / dataset cards) |
| 13.4 - developer role | CRS 6-1-1701(7); 6-1-1702(4) (public statement); developer 90-day notice per SB 25B-004 amendments to 6-1-1702 |
| 14.1 - annual review | CRS 6-1-1703(3)(g) |
| 14.2 - ninety-day clock | CRS 6-1-1703(7) |
| 14.4 - cure architecture | CRS 6-1-1706(3)(a) (feedback; adversarial testing or red teaming as defined or used by NIST; internal review) |
| 15 - interaction disclosure | CRS 6-1-1704(1), with the (2) obviousness exception |
| 16.4 - security anchors | 16 CFR 314 (financial institutions); CPPA regs ss.7120-7123 (audit thresholds incl. 250,000 consumers / 50,000 sensitive) |
| 17.2 - breach routed, not stated | State breach statutes NOT HELD - see finding 4.6 |
| 18.5 - capability claims | 15 U.S.C. 45(a) - deception requires no AI statute |
| 20.1 - employment | CRS 6-1-1701(3)(b); CPPA regs s.7001(ddd) (employment/compensation), s.7150(b)(4) |
| 22.4 - no executive orders | Method: executive policy is not held and shifts; nothing rests on it |

### 3.2 Annex

| Annex | Rests on |
|---|---|
| A2 - two determinations | As policy 4 |
| A2.4 - standing exclusion | CRS 6-1-1701(9)(b)(II)(R) |
| A4.5 - written for regulators | CPPA regs s.7157; CRS 6-1-1703(9) |
| A5 - framework position | CRS 6-1-1703(2)(a); 6-1-1706(3)-(4) (burden on the organisation) |
| A6.2 - statement machinery test | CRS 6-1-1703(4)(b) operationalised |
| A7.2 - developer docs as gate | CRS 6-1-1702(2)-(3) |
| A8.2 - ninety-day clock | CRS 6-1-1703(7) |
| A8.3 - bias pair | House standard |
| A11 - metrics | House standards derived from the above |

## 4. The findings worth recording

### 4.1 The commencement was moved, and the moved date has passed

SB 24-205 as enacted commenced its duties on 1 February 2026. **SB 25B-004 (special
session, approved 28 August 2025) struck every operative "February 1, 2026" in
sections 6-1-1702, 6-1-1703, and 6-1-1704 and inserted "June 30, 2026".** Nothing
else about the duties changed in those substitutions; the same act also added
trade-secret designation and privilege non-waiver language to the attorney-general
disclosure provisions.

Consequence: **as at this note's date, the Colorado AI Act's developer and deployer
duties are in force.** A reader holding only SB 24-205 would state the wrong
commencement; a reader holding only secondary summaries might still believe the
duties are pending. This set states them as live because the amending act says so
and the date has passed.

### 4.2 A statute that names its safe-harbour frameworks

CRS 6-1-1703(2)(a)(I) requires the deployer's risk management program to be
reasonable considering the NIST AI Risk Management Framework, ISO/IEC 42001, or an
equivalent framework; 6-1-1702(1) and 6-1-1703(1) attach a rebuttable presumption of
reasonable care to compliance; and 6-1-1706(3) makes framework compliance plus
discovery-and-cure an affirmative defense - with the burden on the organisation
(6-1-1706(4)). The NIST RMF held in this corpus is therefore not merely guidance for
this jurisdiction: it is the named reference for the statutory reasonableness
standard. Policy 1.3 and 9.5 and annex A5 are built on that, and the cure channels
(feedback, red-teaming "as defined or used by NIST", internal review) are
operationalised rather than recited.

### 4.3 An acceptable use policy is itself a statutory condition

The exclusion at CRS 6-1-1701(9)(b)(II)(R) takes ordinary informational chatbots out
of the high-risk regime **only** where the technology "is subject to an accepted use
policy that prohibits generating content that is discriminatory or harmful". The
policy a company writes is, in Colorado, part of what determines whether its
systems are regulated as high-risk. Policy 4.2 states this, 7.7 forbids weakening
the condition, and annex A2.4 makes its enforcement a standing evidenced item. No
other jurisdiction in this series gives the acceptable use policy that role.

### 4.4 Two tests, deliberately different

Colorado's trigger is the **substantial factor** - assists the decision, capable of
altering the outcome (6-1-1701(11)). California's is **substantially replacing human
decisionmaking** - output used without meaningful human involvement (regs s.7001),
with human involvement defined to require authority, information, and the ability to
reach a different conclusion. Decision-support tools with genuine review are
squarely inside Colorado and arguably outside California; fully automated decisions
are inside both. The worked example in policy 4.4 (resume screening) is chosen
because it sits in the divergence. The two determinations are therefore recorded
separately (annex A2), and audit tests them hardest (A10.2).

### 4.5 The dates are staggered

Colorado's duties: in force since 30 June 2026 (finding 4.1). California's ADMT
article: a business using ADMT for significant decisions before 1 January 2027 must
comply **no later than 1 January 2027** (regs s.7200(b)); risk assessments must
precede new triggering processing now, with the first regulator submission due by
1 April 2028 for assessments conducted in 2026-2027 (s.7157). The set states live
duties as live and dated duties with their dates; nothing is blended into a single
fictional commencement.

### 4.6 Breach deadlines are deliberately not stated

The state breach-notification statutes (including California Civil Code 1798.82 and
Colorado's C.R.S. 6-1-716) are **not held in this corpus**, and the CCPA text held
here is the privacy statute, not the breach statute. Rather than import deadlines
from memory or secondary sources - the exact failure this series exists to catch -
policy 17.2 routes breach obligations to the privacy lead's maintained statement
and names the gap. Obtaining the breach statutes is the recorded next verification
for this set.

### 4.7 What the CCPA is, and is not, in this set

The CCPA supplies the personal-information baseline: notice at collection, purpose
and reasonable-expectation restrictions, consumer rights, service-provider
contracts, sensitive-information handling. It is not a lawful-basis regime on the
GDPR pattern, and the policy does not pretend it is - obligations are stated as
notice, restriction, and rights machinery, which is what the held text provides.

## 5. Not held

| What is missing | Consequence |
|---|---|
| **Any state's law beyond California and Colorado** - including state AI-in-employment and biometric statutes | Nothing asserted; policy 20.2 and 22.1 route |
| **State breach notification statutes** | No breach deadline stated anywhere (finding 4.6) |
| **Colorado attorney general rules under 6-1-1707** | Permissive rulemaking; none held; the presumption position is stated on the statute alone |
| **CPPA Notice of Approval / effective-date instrument for the regulations** | The regulations' own internal dates (ss.7200(b), 7157) are stated from the held text; the instrument-level effective date is not asserted |
| **ISO/IEC 42001** | Named by the Colorado statute as an alternative framework; not held; the set builds on the held NIST RMF and asserts nothing about the ISO standard's content |
| **Sectoral regimes beyond the cited points** | HIPAA, GLBA, COPPA, FCRA are held and cited at the points used; their full compliance programs are the sector's own |
| **Federal executive AI policy** | Not law of general application; not held; nothing rests on it |
| **Case law and enforcement actions** | None relied on anywhere |

## 6. What this set therefore does not say

- It does not state any obligation for states other than California and Colorado.
- It does not state breach-notification deadlines.
- It does not state the content of any attorney-general rule or any ISO standard.
- It does not assert an effective date for the CPPA regulations as an instrument -
  only the compliance dates their held text carries.
- It does not state any federal AI statute, because none exists to state.

## 7. Method

Every provision cited above was read in the held text of the instrument concerned.
The Colorado act was read in the signed 2024 act as amended by the signed 2025B act,
never in either alone. Nothing was taken from a summary, a law-firm briefing, a
vendor page, or a comparative overview, and no obligation was imported from another
jurisdiction in this series. Where a figure lives in an instrument not held, the set
names the gap instead of filling it.

## 8. Standing caveat

No provision cited in this set has been reviewed by qualified counsel. These
documents are educational templates, apply only within the stated scope, and do not
constitute legal advice.
