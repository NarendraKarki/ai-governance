# Research note - Classifying AI systems by risk, EU (Part 2, v1.0)

Purpose: records the primary-source verification behind every rule, date and
scenario finding in the walkthrough. Educational, not legal advice.

Verification date: **30 August 2026**. Every citation below was read in the
consolidated text, not in a summary of it.

## 1. Sources verified

| # | Instrument | Version used | Status |
|---|---|---|---|
| 1 | **Regulation (EU) 2024/1689 consolidated** (AI Act) | `02024R1689-20260727`, ELI `reg/2024/1689/2026-07-27`, 183 pp | **The operative text.** Incorporates amendment M1 |
| 2 | **Regulation (EU) 2026/1744** (Digital Omnibus on AI) | OJ L, 2026/1744, 24.7.2026, of 8 July 2026, 53 pp | **In force.** The M1 amendment. Read to confirm what the consolidation shows as changed |
| 3 | **Regulation (EU) 2016/679** (GDPR) | OJ L 119, 4.5.2016 | Cited for one definition only: Art 4(4), profiling |
| 4 | **Regulation (EU) 2024/1689 as adopted** | OJ L, 2024/1689, 12.7.2024 | Retained to show what changed. **Nothing rests on it** |

One Commission overview page was also supplied. It is **web content**, is not cited
for any rule, and is discussed only in section 5 below, where it diverges from the
text in a way worth recording.

## 2. A note on citations in the artifact body

The project rule is that article numbers live in the research note, not the
artifact. This walkthrough departs from that rule in one respect, deliberately: it
names Annex III items by their point numbers (1(a), 4(b), 5(b) and so on) and the
transparency duties by working labels (T1-T4b). A classification record that does
not say which item was matched is not a classification record. Everything else -
article numbers, paragraph numbers, consolidation markers - stays here.

## 3. Rule -> source (consolidated AI Act unless stated)

### Gates

| Rule in artifact | Source |
|---|---|
| Definition of AI system (machine-based; autonomy; may adapt; infers from input how to generate outputs) | Art 3(1) |
| GPAI model and GPAI system defined separately; model track is Chapter V | Art 3(63), 3(66); Chapter V |
| Scope: providers wherever established; deployers in the Union; third-country operators where output used in the Union; importers, distributors, product manufacturers, authorised representatives | Art 2(1)(a)-(g) |
| Exclusions: military, defence, national security; scientific R&D sole purpose; pre-market research, testing and development (real-world testing not excluded); personal non-professional use; free and open-source unless high-risk or within Art 5 or Art 50 | Art 2(3), 2(6), 2(8), 2(10), 2(12) |
| Other law untouched: data protection; consumer protection and product safety; more favourable worker protection | Art 2(7) ▼M1, 2(9), 2(11) |
| Provider and deployer defined; deployer excludes personal non-professional use | Art 3(3), 3(4) |
| Role change on own name or trademark, substantial modification, or change of intended purpose making a system high-risk | Art 25(1)(a)-(c); "substantial modification" Art 3(23) |
| Intended purpose set by the provider through instructions, marketing, technical documentation | Art 3(12) |
| Reasonably foreseeable misuse | Art 3(13) |

### Tier 1 - prohibited practices

| Point in artifact | Source | Date |
|---|---|---|
| 1 subliminal / manipulative / deceptive | Art 5(1)(a) | 2 Feb 2025, Art 113(a) |
| 2 exploiting vulnerabilities (age, disability, social or economic situation) | Art 5(1)(b) | 2 Feb 2025 |
| 3 social scoring, two limbs | Art 5(1)(c)(i)-(ii) | 2 Feb 2025 |
| 4 criminal risk prediction based solely on profiling or personality; human-assessment carve-out | Art 5(1)(d) | 2 Feb 2025 |
| 5 untargeted scraping for facial recognition databases | Art 5(1)(e) | 2 Feb 2025 |
| 6 emotion inference in the workplace and education institutions; medical or safety exception | Art 5(1)(f) | 2 Feb 2025 |
| 7 biometric categorisation deducing listed characteristics; dataset labelling and law-enforcement carve-outs | Art 5(1)(g) | 2 Feb 2025 |
| 8 real-time RBI in public spaces for law enforcement; three objectives; safeguards | Art 5(1)(h)(i)-(iii); Art 5(2)-(7) | 2 Feb 2025 |
| 9 non-consensual intimate material | Art 5(1)(ba) ▼M1 | 2 Dec 2026, Art 113(a) ▼M1 |
| 10 child sexual abuse material; "without right" defence | Art 5(1)(bb) ▼M1, referring to Directive 2011/93/EU Art 2(c) and (e) | 2 Dec 2026 |
| Scoping rules: intended purpose, or foreseeable and reproducible outcome without adequate safeguards (provider); purpose of use (deployer); manipulation that does not increase exposure is not manipulation | Art 5(1a)(a)(i)-(ii), 5(1a)(b), 5(1b) ▼M1 | 2 Dec 2026 |
| "Placing on the market, putting into service, or use" - deployers caught by use | Chapeau wording of each point in Art 5(1) | - |
| Art 5 does not affect prohibitions under other Union law | Art 5(8) | - |

**Count.** The consolidated Art 5(1) first subparagraph has **ten** lettered points:
(a), (b), (ba), (bb), (c), (d), (e), (f), (g), (h). The two M1 insertions sit between
(b) and (c). Summaries that say "nine practices" merge (ba) and (bb).

### Tier 2 - high-risk

| Rule in artifact | Source |
|---|---|
| Route A: two cumulative conditions (safety component or product under Annex I legislation; third-party conformity assessment required) | Art 6(1)(a)-(b) |
| Safety component: fulfils a safety function, or failure endangers health and safety; safety function = intended purpose to prevent or mitigate health and safety risks | Art 3(14) ▼M1 |
| Not safety components: solely non-safety user assistance, performance optimisation, service efficiency, automation, convenience, quality control | Art 6(1a) ▼M1 |
| But failure endangering health and safety qualifies regardless | Art 6(1b) ▼M1 |
| Third-party assessment solely for non-health-and-safety reasons (radio spectrum, EMI) does not satisfy Condition 2 | Art 6(1c) ▼M1 |
| Annex I Section A list (points 2-12): toys; recreational craft; lifts; ATEX equipment; radio equipment; pressure equipment; cableways; PPE; gas appliances; medical devices; IVD devices | Annex I Section A. **Point 1 (Machinery Directive 2006/42/EC) deleted** ▼M1 |
| Annex I Section B list (points 13-21): civil aviation security; L-category vehicles; agricultural and forestry vehicles; marine equipment; rail interoperability; motor vehicles; vehicle general safety; civil aviation; **machinery (Reg (EU) 2023/1230)** | Annex I Section B; point 21 added ▼M1 |
| Section B systems: only Art 6(1), Art 60a and Arts 102-112 apply; Arts 57-59 only where requirements integrated in sectoral law | Art 2(2) ▼M1 |
| Machinery: essential requirements to be added to the Machinery Regulation by delegated acts applying by 2 Aug 2028 | Reg 2026/1744 Art 3(1), amending Reg 2023/1230 Art 8 |
| Possible limitation of Arts 9-15 and 17-25 where Section A law gives equivalent protection; delegated acts by 2 Aug 2027 | Art 2(13) ▼M1 |
| Route B: Annex III systems are high-risk | Art 6(2) |
| Annex III unchanged by the Omnibus | No ▼M1 marker anywhere in Annex III of the consolidation; Reg 2026/1744 Art 1 contains no amendment to Annex III (its annex amendments are items (41) Annex I, (42) Annex VIII, (43) new Annex XIV) |
| Derogation: no significant risk, including by not materially influencing outcome; four conditions | Art 6(3) first and second subparagraphs, (a)-(d) |
| Profiling override: always high-risk | Art 6(3) third subparagraph |
| Profiling defined by reference to GDPR | Art 3(52); GDPR Art 4(4) |
| Derogation must be documented before market; registration; produce on request | Art 6(4); Art 49(2) |
| Commission guidelines with practical examples, due by 2 Feb 2026 | Art 6(5) |
| Art 6(5) excluded from the deferral | Art 113(c) ▼M1: "with the exception of Article 6(5)" |
| Delegated acts may amend Annex III use cases and the derogation conditions | Art 7(1); Art 6(6)-(8) |
| Provider requirements (risk management, data, documentation, records, transparency to deployers, human oversight, accuracy/robustness/cybersecurity); provider obligations | Chapter III Section 2 (Arts 8-15); Section 3 (Arts 16-27) |
| Deployer duties: instructions for use; competent human oversight; input data; monitoring; logs; inform workers; inform affected persons | Art 26(1)-(2), (4)-(5), (6)-(7), (11) |
| FRIA: public bodies, private providers of public services, and deployers of 5(b) and 5(c) systems; area 2 excepted | Art 27(1) |
| Registration: providers of Annex III systems except area 2; public-authority deployers register use | Art 49(1), 49(3) |
| Annex III dates: 2 Dec 2027; Annex I: 2 Aug 2028 | Art 113(c)(i)-(ii) ▼M1 |
| Grandfathering: pre-existing high-risk systems only on significant design change; public-authority systems by 2 Aug 2030 | Art 111(2) ▼M1; per recital 39 of Reg 2026/1744 the decisive date is when the first unit of that type and model was placed on the market |

### Annex III, item by item

Each item was read in full. The "not covered" column of the artifact takes its
content from the words of the item itself, as follows.

| Item | Words relied on |
|---|---|
| 1(a) | "This shall not include AI systems intended to be used for biometric verification the sole purpose of which is to confirm that a specific natural person is the person he or she claims to be"; definitions Art 3(35), 3(36), 3(41) |
| 1(b) | "according to sensitive or protected attributes or characteristics based on the inference of those attributes"; definition Art 3(40) including the ancillary-service carve-out; overlap with Art 5(1)(g) |
| 1(c) | Definition Art 3(39); overlap with Art 5(1)(f) |
| Area 1 chapeau | "in so far as their use is permitted under relevant Union or national law" |
| 2 | "safety components in the management and operation of critical digital infrastructure, road traffic, or in the supply of water, gas, heating or electricity"; exemptions Art 27(1) and Art 49(1) |
| 3(a)-(d) | Text as printed; "at all levels" in each sub-point |
| 4(a) | "in particular to place targeted job advertisements, to analyse and filter job applications, and to evaluate candidates" |
| 4(b) | "terms of work-related relationships, the promotion or termination... to allocate tasks based on individual behaviour or personal traits or characteristics or to monitor and evaluate the performance and behaviour of persons in such relationships" |
| 5(a) | "by public authorities or on behalf of public authorities" |
| 5(b) | "with the exception of AI systems used for the purpose of detecting financial fraud" |
| 5(c) | "in the case of life and health insurance" |
| 5(d) | Text as printed, including "emergency healthcare patient triage systems" |
| 6(a)-(e) | Each sub-point opens "by or on behalf of law enforcement authorities, or by Union institutions, bodies, offices or agencies in support of"; 6(d) "not solely on the basis of the profiling" (contrast Art 5(1)(d)) |
| 7(a)-(d) | Each sub-point scoped to "competent public authorities or... Union institutions"; 7(d) "with the exception of the verification of travel documents" |
| 8(a) | "by a judicial authority or on their behalf... or to be used in a similar way in alternative dispute resolution" |
| 8(b) | "This does not include AI systems to the output of which natural persons are not directly exposed, such as tools used to organise, optimise or structure political campaigns from an administrative or logistical point of view" |

### Tier 3 - transparency

| Label | Source | Date |
|---|---|---|
| T1 inform of AI interaction unless obvious; law-enforcement exception | Art 50(1) | 2 Aug 2026 (Chapter IV not carved out of Art 113 second paragraph) |
| T2 machine-readable marking of synthetic audio, image, video, text; assistive-editing carve-out | Art 50(2) | 2 Aug 2026; pre-existing systems by 2 Dec 2026, Art 111(4) ▼M1 |
| T3 inform persons exposed to emotion recognition or biometric categorisation | Art 50(3) | 2 Aug 2026 |
| T4a deep fake disclosure; artistic works limitation | Art 50(4) first subparagraph; "deep fake" Art 3(60) | 2 Aug 2026 |
| T4b public-interest text disclosure; editorial-control exception | Art 50(4) second subparagraph | 2 Aug 2026 |
| Clear, distinguishable, at first interaction or exposure, accessible | Art 50(5) | - |
| Stacks with Chapter III and other transparency law | Art 50(6) | - |

### Tier 4 and cross-cutting

| Rule | Source |
|---|---|
| AI literacy: take measures to support development; no guaranteed individual level | Art 4(1) ▼M1 |
| Voluntary codes of conduct for non-high-risk systems | Art 95 |

## 4. Interpretive readings, flagged

These are readings of the words, not verified statements. Each is used in the
artifact with the fallback stated.

1. **Recruitment as "workplace" for Art 5(1)(f).** The prohibition covers "the
   areas of workplace and education institutions". The walkthrough treats a
   recruitment process for employment as within the area of the workplace. The
   Commission's prohibited-practices guidelines, which may address this, are not
   held. Fallback given in the worked example: even on the narrower reading the
   system is high-risk under Annex III 1(c) and carries Art 50(3), so the
   organisational outcome does not change.
2. **"Materially influencing the outcome" for tools that flag cases for human
   review.** The walkthrough treats a public-benefits flagging tool as materially
   influencing the outcome and therefore outside the derogation. Art 6(3) supports
   this reading for systems that profile; for a non-profiling flagging tool the
   question is closer and would turn on the Art 6(5) guidelines.
3. **Meeting-note summarisation and Art 50(2).** Treated as within the carve-out for
   systems that do not substantially alter the deployer's input or its semantics.
   A summariser that adds analysis or drafts new content moves out of the carve-out.
4. **Roster-based scheduling as "not an AI system".** Offered as "arguably"; the
   statutory test is whether the system infers from input how to generate output,
   and a pure rules engine may not.

## 5. Where the supplied web page diverges from the text

The Commission overview page (generated 30 August 2026) is well written and its
dates agree with the consolidated text. Three points are recorded because a reader
relying on the page rather than the text would come away with a different picture:

- The page says the Act "prohibits nine practices". The text has ten points; the
  page merges (ba) and (bb) into one.
- The page says the Omnibus "entered into force on 27 July 2026". The Omnibus
  provides for entry into force on the third day following publication (Art 4);
  publication was 24 July 2026; the consolidation is dated 27 July 2026 and Art
  113(d) uses 27 July 2026. The page and the text agree; the point is recorded
  because the **adoption** date (8 July 2026) and the **publication** date (24 July
  2026) are the ones a source register should carry.
- The page's high-risk bullet list is a paraphrase of Annex III headings, not of the
  items. It is a fair summary; it is not the test. Section 4.2 of the artifact
  exists because the headings are not enough.

## 6. Effect on the Part 1 EU policy set - recommended edits

Part 1's research note carried this as Limitation 3: "Annex III was not
individually verified... Any specific classification must be verified against the
Annex before it is relied on." This part closes that gate. Recommended edits, to be
made by hand in the Part 1 files:

| File | Edit |
|---|---|
| `EU_AI_Acceptable_Use_Policy.md` 12.1 | Replace "are expected to fall within the high-risk category" with "fall within the high-risk category (Annex III, items 4(a) and 4(b)) when that regime commences on 2 December 2027" |
| `EU_policy_research_note.md`, obligation table, last AI row | Replace "classification not individually verified; see Limitation 3" with "Annex III items 4(a)-(b), verified item by item in Part 2, research note section 3" |
| `EU_policy_research_note.md`, Limitation 3 | Replace with: "Annex III was read item by item on 30 August 2026 (see Part 2). The Omnibus did not amend it. Remaining gate: Route A findings depend on Annex I product legislation not held." |
| `EU_policy_research_note.md`, Limitation 4 | Keep. Art 6(5) guidelines remain not held. Add: "Part 2 states the consequence for the derogation." |
| `EU_policy_research_note.md`, "What is needed", item 2 | Mark closed, with a pointer to `classification/eu/` |
| `EU_source_register.md`, section 3, row "Annex III, read item by item" | Remove, or mark closed with the same pointer |
| `policies/eu/README.md` | Update the gate list accordingly |

The other two Part 1 EU gates - a current GDPR consolidation and a Member State
overlay note - remain open and are not affected by this part.

## 7. Limitations - stated rather than left to be found

1. **Route A is conditional.** Whether a product needs third-party conformity
   assessment is a question for the Annex I instrument. None is held. Every Route A
   finding in the artifact says so.
2. **Art 6(5) guidelines are not held.** They are carved out of the deferral and
   were due by 2 February 2026. If they exist, they bear on the derogation and on
   the boundary scenarios, and the readings in section 4 should be checked against
   them.
3. **Commission guidelines on the AI-system definition and on prohibited practices
   are not held.** The overview page refers to both. Gate 1 and Tier 1 are applied
   from the statute alone.
4. **No delegated act** under Art 7 or Art 6(6)-(7) is reflected. None appears in
   the consolidation of 27 July 2026.
5. **Member State law is not addressed**: national RBI authorisations (Art 5(5)),
   the "without right" defence for point 10, employment law, and any more
   favourable worker protections under Art 2(11).
6. **GDPR is cited from the 4 May 2016 OJ text**, for the definition of profiling
   only. That definition has not been amended, but the Part 1 caveat on corrigenda
   stands.
7. **No provision cited here has been reviewed by qualified counsel.**

## 8. Watch items

- The Art 6(5) guidelines. Their arrival changes section 4 of this note first.
- Any delegated act under Art 7 adding to or modifying Annex III, or under Art
  6(6)-(7) changing the derogation conditions.
- The Art 2(13) delegated acts, due by 2 August 2027, limiting high-risk
  requirements where Section A product law is equivalent.
- The Machinery Regulation delegated acts under Reg 2026/1744 Art 3, applying by
  2 August 2028.
- Any later consolidation of the AI Act. The date on the front of the artifact is
  the whole basis of its authority.
