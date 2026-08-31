# Research note - EU AI Acceptable Use Policy (v1.0) and Enterprise Annex (v1.0)

Purpose: records the primary-source verification behind each obligation, per the
project rule that article numbers live in the research record, not the artifact body.
Educational, not legal advice.

## Sources verified

All citations below were read in the primary text. Verification date: **30 August 2026**.

| # | Instrument | Version used | Status |
|---|---|---|---|
| 1 | **Regulation (EU) 2016/679** (GDPR) | OJ L 119, 4.5.2016, pp. 1-88 | In force |
| 2 | **Regulation (EU) 2024/1689** (AI Act) | OJ L, 2024/1689, 12.7.2024 - as adopted | In force, **amended** |
| 3 | **Regulation (EU) 2024/1689 consolidated** | `02024R1689-20260727`, ELI `reg/2024/1689/2026-07-27` | **The operative text.** Incorporates amendment M1 |
| 4 | **Regulation (EU) 2026/1744** (Digital Omnibus on AI) | OJ L, 2026/1744, 24.7.2026, of 8 July 2026 | **In force.** The M1 amendment |

**Regulation (EU) 2026/1744 was adopted and published.** The consolidated AI Act
marks its changes as `▼M1`. Every AI Act citation below is taken from the
**consolidated** text, not the 2024 original, and the original is retained only to
show what changed.

**Nothing in these documents rests on web content.** A Commission overview page on the
AI Act was supplied alongside the primary texts; it is **not cited anywhere** and was
used only to confirm which instruments to read.

### NOT HELD - and therefore not asserted

**Regulation (EU) 2022/2554 (DORA) is not among the sources.** It was requested but no
copy was supplied. Nothing about digital operational resilience is asserted in these
documents. Annex A11.2 is a pointer that says so explicitly and defers to a separate
annex that cannot yet be written. See "What is needed to complete the set" below.

## The commencement position - the central finding

The single most consequential fact for an EU AI policy written today is **which
obligations are in force**. Verified against Article 113 of the consolidated text as
amended:

| Provision | Applies from | Source |
|---|---|---|
| The Regulation generally | **2 August 2026** | Art 113, second paragraph |
| Chapters I and II (definitions, AI literacy, prohibited practices) | **2 February 2025** | Art 113(a) ▼M1 |
| — except Art 5(1) points (ba) and (bb), and Art 5(1a) and (1b) | **2 December 2026** | Art 113(a) ▼M1 |
| Chapter III Section 4, Chapter V, Chapter VII, Chapter XII, Art 78 (except Art 101) | **2 August 2025** | Art 113(b) |
| Chapter III Sections 1, 2 and 3 (except Art 6(5)) — **high-risk** — Annex III systems | **2 December 2027** | Art 113(c)(i) ▼M1 |
| Chapter III Sections 1, 2 and 3 — **high-risk** — Annex I systems | **2 August 2028** | Art 113(c)(ii) ▼M1 |
| Articles 102 to 110 | **27 July 2026** | Art 113(d) ▼M1 |

**Chapter IV (Article 50, transparency) is not carved out**, so it applies from the
general date of **2 August 2026**. It is in force now, and it is the newest live
obligation - which is why the policy gives it its own section rather than folding it
into a general transparency clause.

**The high-risk regime is deferred, not removed.** Policy Section 4.3 and Annex A3
exist because a deferral quietly consumed is a deferral wasted.

## Obligation -> policy clause -> source

### Artificial intelligence

| Obligation (as expressed in artifact) | Clause | Source (consolidated AI Act unless stated) |
|---|---|---|
| Provider / deployer role distinction; role can change on substantial modification or own-name placing | Policy 2.1, 4.4; Annex A2.1, A4.2 | Art 3 definitions; Art 25 |
| Staff AI knowledge and skills; no guaranteed individual level | Policy 20.1 | **Art 4**, in force since 2 Feb 2025 |
| Prohibited: subliminal / manipulative / deceptive techniques causing significant harm | Policy 6.1 | Art 5(1)(a) |
| Prohibited: exploiting vulnerabilities of age, disability, social or economic situation | Policy 6.1 | Art 5(1)(b) |
| Prohibited: social scoring leading to detrimental treatment in unrelated context, or unjustified / disproportionate treatment | Policy 6.1 | Art 5(1)(c)(i)-(ii) |
| Prohibited: predicting criminal offending based solely on profiling or personality traits | Policy 6.1 | Art 5(1)(d) |
| Prohibited: untargeted scraping of facial images to build or expand facial recognition databases | Policy 6.1 | Art 5(1)(e) |
| **Prohibited: inferring emotions in the workplace and education institutions**, except for medical or safety reasons | Policy 6.1, 12.1, 18 | **Art 5(1)(f)** — verbatim: "to infer emotions of a natural person in the areas of workplace and education institutions, except where the use of the AI system is intended to be put in place or into the market for medical or safety reasons" |
| Prohibited: biometric categorisation deducing race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation | Policy 6.1 | Art 5(1)(g) |
| Prohibited: real-time remote biometric identification in public spaces for law enforcement, outside authorised cases | Policy 6.1 | Art 5(1)(h), with Art 5(2)-(4) |
| Non-consensual intimate imagery; CSAM material — prohibited **from 2 Dec 2026** | Policy 6.2, Annex A3.4 | **Art 5(1)(ba), (bb) ▼M1**, scoped by Art 5(1a), (1b) ▼M1; commencement Art 113(a) ▼M1 |
| Inform people they are interacting with an AI system, unless obvious | Policy 9.1, 16.1 | **Art 50(1)** |
| Machine-readable marking of synthetic audio, image, video, text by providers; editing-assistance carve-out | Policy 9.4 | **Art 50(2)** |
| Deployers of emotion recognition / biometric categorisation must inform those exposed and process per GDPR | Policy 9.2 | **Art 50(3)** |
| Deep fake disclosure by deployers | Policy 9.3 | **Art 50(4)** |
| GPAI model obligations fall on the model provider | Policy 4.1 | Chapter V (Arts 51-56), from 2 Aug 2025 per Art 113(b) |
| High-risk classification and requirements — deferred | Policy 4.2, 5 (Level 4), Annex A3 | Chapter III Sections 1-3; commencement Art 113(c) ▼M1 |
| Recruitment / employment-management systems expected high-risk | Policy 12.1 | Annex III — **classification not individually verified; see Limitation 3** |

### Data protection

| Obligation | Clause | Source (GDPR) |
|---|---|---|
| Lawfulness, fairness, transparency; purpose limitation; minimisation; accuracy; storage limitation; integrity; accountability | Policy 7.1-7.5 | Art 5(1)-(2) |
| Lawful basis recorded before processing | Policy 7.1 | Art 6 |
| Special categories - additional condition | Policy 7.8 | Art 9 |
| Criminal convictions and offences data | Policy 7.8 | Art 10 |
| Information to be provided to the data subject, including meaningful information about the logic of automated decision-making | Policy 16.2 | Arts 13-14, incl. 13(2)(f), 14(2)(g) |
| Rights of access, rectification, erasure, restriction, portability, objection | Policy 7.7; Annex A8.1 | Arts 15-21 |
| One month to respond, extendable by two months with notice and reasons | Annex A8.2 | Art 12(3) |
| Notification of rectification or erasure to recipients | Annex A8.4 | Art 19 |
| **Right not to be subject to a solely automated decision** producing legal or similarly significant effects; permitted cases; safeguards including human intervention, expressing a view, contesting | Policy 10.3 | **Art 22(1)-(3)** |
| Such decisions not based on special category data save narrow conditions with safeguards | Policy 10.4 | Art 22(4) |
| Processor contract terms; sub-processor authorisation | Policy 7.9; Annex A5.1 | Art 28(2)-(4) |
| Record of processing activities | Annex A2.3 | Art 30 |
| Security of processing appropriate to risk | Policy 13.4 | Art 32 |
| **Breach notification to the supervisory authority without undue delay and where feasible within 72 hours of becoming aware**, unless unlikely to result in risk; reasons required if late | Policy 14 | **Art 33(1)** |
| Communication to the data subject where high risk | Policy 14 | Art 34(1) |
| DPIA where high risk; the three listed triggers; authority lists | Policy 7.6 | Art 35(1), 35(3)(a)-(c), 35(4) |
| Data protection officer position, independence, no penalisation, reports to highest management | Annex A1.4 | Arts 37-38, esp. 38(3) |
| Transfers on adequacy, appropriate safeguards, or derogations; derogations not for repetitive transfers | Policy 8.1-8.3 | Arts 45, 46, 49(1) and 49(1) second subparagraph |
| Right to lodge a complaint with a supervisory authority | Policy 14; Annex A10.1 | Art 77 |

## House standards that EXCEED or sit outside statute (flagged, kept knowingly)

- **Policy 10.1 pre-decision human review.** Article 22 GDPR operates as a right the
  individual holds, with safeguards attaching where a permitted exception applies. The
  policy instead requires meaningful human review **before** the decision takes effect,
  for a wider class of significant decisions. Deliberate; labelled in Policy 10.5.
- **Policy 6.2 - the December 2026 prohibitions applied from today.** The law defers
  them; the policy does not. A conscious choice, and one with no downside.
- **Policy 4.3 / Annex A3 - the readiness register.** Nothing requires an organisation
  to prepare for the high-risk regime in advance. This is governance, not statute.
- **Annex A5.4 - contractual breach-notification timing.** Article 33 binds the
  controller; requiring suppliers to notify fast enough to make the controller's clock
  achievable is good practice, not an express statutory term.
- **Policy 11 - output verification.** No statutory duty in these instruments; a house
  standard.
- **Policy 15.1 - intellectual property.** No Union IP instrument was supplied. The
  clause is a house standard and **no statutory basis is asserted**.
- **Policy 17 - non-discrimination.** No Union equality instrument was supplied. The
  clause is a house standard; the GDPR fairness principle in Art 5(1)(a) supports part
  of it but is not cited as the basis for the whole.

## Annex provisions - basis

- A1 (committee, accountable executive, three lines), A2 (inventory), A4 (lifecycle),
  A6 (exceptions), A7 (agentic AI), A9 (assurance): governance controls, not statutory
  duties, consistent with the accountability principle in GDPR Art 5(2) and Art 24. No
  article numbers claimed in the body.
- **A1.4** is statutory: GDPR Arts 37-38.
- **A2.3** is statutory: GDPR Art 30.
- **A3 (commencement readiness register)** is a governance wrapper around a statutory
  commencement schedule, AI Act Art 113 as amended. It is the one annex section whose
  reason for existing is a hard date rather than good practice.
- A5 (suppliers): GDPR Art 28 underpins the processing terms; the AI-specific terms
  are contractual good practice beyond statute.
- A8 (rights operations): GDPR Arts 12, 15-21.
- A11: sector overlay is a pointer, not a mapping.

## Limitations - stated rather than left to be found

1. **The AI Act's own commencement dates have already been amended once.** Regulation
   (EU) 2026/1744 changed them. The position in this note is the consolidated text at
   **27 July 2026**. Any later consolidation supersedes it, and Annex A3.5 requires the
   committee to record which version its position rests on.
2. **GDPR is cited from the OJ text as published on 4 May 2016.** The EUR-Lex record
   supplied notes the act has been changed and gives 04/05/2016 as the current
   consolidated version; the corrigenda published since should be checked before any
   position turns on precise wording.
3. **Annex III was not individually verified.** Policy 12.1 says recruitment and
   employment-management systems are "expected" to fall in the high-risk category. That
   word is doing real work: the Annex III list was not read item by item for this note,
   and the omnibus amended Annex I. **Any specific classification must be verified
   against the Annex before it is relied on.**
4. **Article 6(5) is excluded from the deferral** by Art 113(c) and was not examined.
   It concerns Commission guidelines on high-risk classification and may affect how
   classification is done in the interim.
5. **No provision cited here has been reviewed by qualified counsel.**
6. **Member State law is not addressed.** The GDPR leaves room for national provisions
   - notably on employment data, special categories, and criminal convictions data -
   and none was supplied or consulted. An organisation operating in a specific Member
   State must overlay that law.
7. **DORA is absent.** See below.

## What is needed to complete the set

1. **Regulation (EU) 2022/2554 (DORA)**, consolidated. Without it the financial-entity
   annex cannot be written to this standard, and nothing about ICT third-party risk,
   the register of information, ICT incident classification and reporting, contractual
   requirements or critical-provider designation is asserted anywhere in this set.
2. **Annex III of the consolidated AI Act**, read item by item, to replace "expected to
   fall" with a verified classification for the specific systems [ORGANISATION] uses.
3. **A current GDPR consolidation**, to close Limitation 2.
4. **The relevant Member State data protection act**, for the national provisions at
   Limitation 6.

## Watch items

- Any further amendment to AI Act Article 113. The dates in this note are the whole
  spine of Policy Section 4.
- Commission guidelines under Article 6(5) on high-risk classification.
- Harmonised standards and common specifications for the high-risk requirements, which
  will determine what "ready by December 2027" actually means in practice.
- Guidance on the Article 50 transparency obligations, in force since 2 August 2026 and
  the newest live duty in the set.

## ADDENDUM 31 August 2026 - gates closed

### Annex III read item by item (Limitation 3 - CLOSED)

Annex III of the consolidated text (02024R1689-20260727) was read in full.
It lists eight areas: (1) biometrics - remote biometric identification
(verification-only systems excluded), biometric categorisation on sensitive
or protected attributes, emotion recognition; (2) critical infrastructure
safety components; (3) education and vocational training - admission,
evaluation of learning outcomes, level assessment, test monitoring;
(4) employment, workers' management and access to self-employment;
(5) essential services - public assistance eligibility, creditworthiness
(fraud-detection excepted), life and health insurance risk assessment and
pricing, emergency call handling; (6) law enforcement; (7) migration, asylum
and border control; (8) administration of justice and democratic processes.
**The whole Annex is base text (▼B): Regulation (EU) 2026/1744 did not amend
it.** The omnibus's classification changes sit in Article 6(1a)-(1c) and
concern Annex I safety components.

What this changes in the set:

- **Policy 12.1 rewritten from "expected" to verified.** Annex III point 4(a)
  lists systems for recruitment or selection - targeted advertisements,
  application filtering, candidate evaluation; point 4(b) lists decisions on
  promotion, termination, task allocation based on behaviour or traits, and
  monitoring and evaluation of performance and behaviour. The policy now
  states the listing directly.
- **The listing is not automatic classification.** Article 6(3) derogates
  systems posing no significant risk (narrow procedural tasks, improving a
  completed human activity, deviation detection without replacing human
  assessment, preparatory tasks) - but the derogation **cannot apply where
  the system profiles natural persons**, and a provider invoking it must
  document the assessment before market placement (Art 6(4)). Most
  employment-context AI evaluating people involves profiling; the policy's
  wording reflects the listing with the derogation caveat.
- Other policy touchpoints confirmed in the list: creditworthiness scoring
  (5(b)), emotion recognition where not already prohibited by Art 5(1)(f)
  (1(c)), biometric categorisation (1(b)) - consistent with how Policy 6.1,
  12.1 and the Level 4 register treat them.
- **Article 6(5) guidelines:** the Commission was required to issue
  classification guidelines by 2 February 2026. They are not held in the
  corpus and nothing here rests on them; obtain before any contested
  classification call. (Watch item retained.)

### GDPR consolidation (Limitation 2 - currency CLOSED, wording check open)

Checked 31 August 2026: the current consolidated GDPR remains
`02016R0679-20160504`. The amending proposals in the data-side Digital
Omnibus package were **not adopted** as at this date - the adopted
Regulation (EU) 2026/1744 amends the AI Act, the aviation regulation and
the machinery regulation only, per its own title and text (held in corpus).
Web sources were used solely to confirm that no amending act exists to
obtain; no obligation rests on them. The corrigenda-wording pass against
the consolidated text (►C markers) remains the one open step; no position
in this set has been identified that turns on corrected wording, and the
cited obligations are structural rather than fine-worded.

### Member State overlay note (Limitation 6 - stated and scoped)

The GDPR is a regulation with opening clauses, and the AI Act leaves
national machinery to Member States. An organisation deploying in a specific
Member State must overlay, at minimum: national employment-data provisions
(the GDPR permits more specific national rules for the employment context,
including collective agreements); national conditions on special categories
and genetic, biometric or health data (Member States may maintain or
introduce further conditions); national rules on criminal-convictions data;
the national age of consent for information-society services (13 to 16 by
Member State); mandatory DPO designation beyond the GDPR's cases (some
Member States extend it); worker-representation rights over workplace AI
(works-council codetermination regimes can require agreement before
deployment of monitoring or evaluation systems); the Member State's AI Act
implementation - notified market surveillance authorities and the national
penalty regime; and sector supervisors. **None of this is mapped in this
set, by design** - it is a Union-law baseline; the overlay is stated so it
is planned for, not discovered late. Per-state columns belong to the
jurisdiction comparison matrix (series part 3).
