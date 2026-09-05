# Research note - EU AI Act Classification Walkthrough (v1.0)

Purpose: records the primary-source verification behind every classification rule
stated in the walkthrough, per the project rule that article numbers live in the
research record, not the artifact body. Educational, not legal advice.

This note also covers the companion explainer `EU_AI_Act_What_Applies_Today.md`
(v1.0): every legal position in it restates a position already verified in the
tables below - the Art 50(1)-(5) overlay duties and their 2 Aug 2026 commencement,
the Art 113 schedule as amended, Art 5(1)(f) and its workplace-and-education
boundary, Art 4 literacy, Annex III points 1(c), 4(a) and 5(b) with the
fraud-detection exception, and the Art 6(3) profiling override. The explainer's
worked examples (insurer, bank) introduce no new legal claims; the voice-stress
example applies Art 5(1)(f) only to staff and candidates, and classifies the
customer-facing use via Annex III 1(c) plus Art 50(3), deliberately.

The explainer's sector section (finance, healthcare) rests on the same tables:
the distress-targeting example on Art 5(1)(b) `B` (specific social or economic
situation; materially distorting behaviour; significant harm caused or likely);
the customer reliability score on Art 5(1)(c)(i)-(ii) `B`, contrasted with
Annex III 5(b) `B` (creditworthiness as high-risk, not banned); the biometric
segmentation example on Art 5(1)(g) `B`, contrasted with the verification
exclusion in Annex III 1(a) `B`; the patient-monitoring example on the medical
or safety exception in Art 5(1)(f) `B`, with the surviving classification via
Annex III 1(c) `B` and the disclosure duty via Art 50(3) `B`; the staff
wellbeing dashboard on Art 5(1)(f) `B`, taking the protective reading of the
exception (stated as such in the document; the same boundary caveat as
Limitation 5 applies); and the triage example on Annex III 5(d) `B`. The
"practice, not component" framing restates the chapeau wording of Art 5(1)
(placing on the market, putting into service, use) and, for the December 2026
items, the system-vs-use test in Art 5(1a) `M1`.

`EU_AI_Act_Classification_Worked_Examples.md` (v1.0) is likewise derivative of
the verified tables. Bank rows: chatbot Art 50(1) `B`; credit scoring Annex III
5(b) `B` with Art 6(3) third subparagraph `B`; fraud detection the express
exception in Annex III 5(b) `B`; CV screening Annex III 4(a) `B`; image
generator Art 50(2), 50(4) `B`; call-centre engagement scoring and voice-stress
on staff or candidates Art 5(1)(f) `B`; voice-stress on customers Annex III
1(c) `B` plus Art 50(3) `B`. Hospital rows: radiology module Art 6(1)(a)-(b)
`B` with Annex I Section A item 11 `B`; emergency triage Annex III 5(d) `B`;
ward distress monitoring the medical or safety exception in Art 5(1)(f) `B`
plus Annex III 1(c) `B` and Art 50(3) `B`; staff burnout dashboard Art 5(1)(f)
`B` on the protective reading (Limitation 5 applies); rostering Annex III 4(b)
`B`, whose outcome turns on whether the system allocates on individual
behaviour or traits - stated in the document as an open question, not resolved;
clinical recruitment Annex III 4(a) `B`; entrance facial recognition NOT within
Art 5(1)(h) `B` (which is limited to law-enforcement purposes) but within Annex
III 1(a) `B`. Commencement dates throughout from Art 113 `M1` as tabulated
above. The five-question method restates Gates 1-5 of the walkthrough.

**Two negative classifications are asserted** in that document and rest on the
item-by-item Annex III reading dated 1 September 2026: AML transaction
monitoring and appointment no-show prediction fall within none of the eight
areas. A negative is only as good as the reading behind it - if Annex III is
amended under Art 7, both must be re-checked.

## Sources verified

All citations below were read in the primary text. Verification date:
**1 September 2026**.

| # | Instrument | Version used | Status |
|---|---|---|---|
| 1 | **Regulation (EU) 2024/1689 consolidated** (AI Act) | `02024R1689-20260727`, consolidation stamp `02024R1689 - EN - 27.07.2026 - 001.001` on every page | **The operative text.** Incorporates amendment M1 |
| 2 | **Regulation (EU) 2026/1744** (Digital Omnibus on AI) | OJ L, 2026/1744, 24.7.2026; adopted 8 July 2026; PE/30/2026/REV/1 | **In force.** The M1 amendment; amends Regulations (EU) 2024/1689, 2018/1139 and 2023/1230 |

Every AI Act citation below is from the consolidated text. Provisions are marked
as the consolidation marks them: `B` for base text, `M1` for text inserted or
replaced by the omnibus.

**Nothing in the walkthrough rests on web content.** No web source was consulted
for any provision; both instruments were supplied as files and read directly.

## The gates, article by article

### Threshold questions (walkthrough section 2)

| Statement in walkthrough | Source |
|---|---|
| Definition of AI system; "infers" as the load-bearing element | Art 3(1) `B` |
| Provider and deployer definitions | Art 3(3), 3(4) `B` |
| Scope: providers wherever established; deployers in the Union; third-country operators where output is used in the Union | Art 2(1)(a)-(c) `B` |
| Exclusions: military, defence, national security; scientific research; pre-market R&D (except real-world testing); purely personal non-professional use | Art 2(3), 2(6), 2(8), 2(10) `B` |
| Free and open-source exemption and its carve-back (prohibited, high-risk, or transparency-relevant systems) | Art 2(12) `B` |
| Deployer becoming provider (own name, substantial modification) | Art 25(1) `B` (value-chain switch, expressed for high-risk systems); Art 3(3) `B` (the general provider definition, which catches own-name placing regardless of tier); Art 3(23) `B` (substantial modification) |

### Gate 1 - prohibited practices (walkthrough section 3)

| Prohibition as expressed | Source |
|---|---|
| 1. Manipulation causing significant harm | Art 5(1)(a) `B` |
| 2. Exploiting vulnerabilities of age, disability, social or economic situation | Art 5(1)(b) `B` |
| 3. Social scoring (unrelated context, or unjustified/disproportionate treatment) | Art 5(1)(c)(i)-(ii) `B` |
| 4. Predicting individual offending solely from profiling or personality traits; support-of-human-assessment carve-out | Art 5(1)(d) `B` |
| 5. Untargeted scraping of facial images from internet or CCTV | Art 5(1)(e) `B` |
| 6. Emotion inference in workplace and education institutions, medical or safety exception | Art 5(1)(f) `B` |
| 7. Biometric categorisation deducing sensitive traits; lawful-dataset labelling carve-out | Art 5(1)(g) `B` |
| 8. Real-time remote biometric identification for law enforcement; authorised objectives and safeguards | Art 5(1)(h), 5(2)-(7) `B` |
| 9. Non-consensual intimate imagery | Art 5(1)(ba) `M1` |
| 10. CSAM generation or manipulation | Art 5(1)(bb) `M1` (by reference to Directive 2011/93/EU Art 2(c),(e)) |
| System-level vs use-level test for items 9-10 (intended purpose, or foreseeable-and-reproducible without adequate safeguards; use for the purpose prohibited outright) | Art 5(1a)(a)-(b) `M1` |
| Manipulation not increasing exposure or altering nature is out of item 9 | Art 5(1b) `M1` |
| Commencement: 2 Feb 2025; items 9-10 from 2 Dec 2026 | Art 113(a) `M1` |

### Gate 2 - product route (walkthrough section 4)

| Statement | Source |
|---|---|
| Two cumulative conditions: Annex I safety component or product, plus third-party conformity assessment | Art 6(1)(a)-(b) `B` |
| Non-safety functions (user assistance, performance optimisation, service efficiency, automation or convenience, quality control) are not safety components | Art 6(1a) `M1` |
| Failure or malfunction endangering health and safety qualifies regardless | Art 6(1b) `M1` |
| Third-party assessment solely for non-health-safety risks (e.g. radio spectrum, EMI) does not satisfy condition (b) | Art 6(1c) `M1` |
| Safety component definition (amended) | Art 3(14) `M1` |
| Annex I Section A: items 2-12 after the M1 deletion of item 1 (see Annex I note below); Section B: sectoral legislation incl. the Machinery Regulation | Annex I `B`+`M1` |
| Section B products: only Art 6(1), Art 60a and Arts 102-112 apply directly | Art 2(2) `M1` |
| Possible limitation of Arts 9-15, 17-25 where Section A legislation gives equivalent protection; delegated acts by 2 Aug 2027 | Art 2(13) `M1` |
| Commencement: 2 Aug 2028 | Art 113(c)(ii) `M1` |

**Annex I note.** The omnibus made two changes verified in the consolidated
Annex: former item 1, Directive 2006/42/EC (Machinery Directive), is **deleted**
(the `M1` deletion marker stands where item 1 was; Section A now runs items
2-12), and item 21, **Regulation (EU) 2023/1230** (Machinery Regulation), is
**added to Section B**. The omnibus also amends Regulation (EU) 2023/1230 itself
(per its own title), integrating AI requirements into the machinery regime -
which is why the walkthrough describes the machinery route as handled through
that Regulation's own procedures.

### Gate 3 - Annex III route (walkthrough section 5)

| Statement | Source |
|---|---|
| Annex III systems are high-risk | Art 6(2) `B` |
| The eight areas and every item under them, as restated in walkthrough section 5 | Annex III points 1-8 `B`, read item by item on 1 Sep 2026: 1(a)-(c), 2, 3(a)-(d), 4(a)-(b), 5(a)-(d), 6(a)-(e), 7(a)-(d), 8(a)-(b) |
| **The omnibus did not amend Annex III** - the whole Annex carries the `B` marker | Annex III `B`; confirmed against Reg 2026/1744, which contains no Annex III amendment |
| Biometric verification exclusion (identity confirmation only) | Annex III 1(a), second paragraph `B` |
| Credit fraud-detection exception | Annex III 5(b) `B` |
| Election campaign logistics exclusion | Annex III 8(b), second sentence `B` |
| Derogation: no significant risk incl. not materially influencing decision outcomes; the four conditions | Art 6(3), first and second subparagraphs, (a)-(d) `B` |
| Profiling override - always high-risk where the system profiles natural persons | Art 6(3), third subparagraph `B` |
| Documentation before placing on market or putting into service; production to authorities on request | Art 6(4) `B` |
| Registration of derogation claims in the EU database | Art 6(4) `B`, referring to Art 49(2) `B` |
| Commission guidelines with practical examples due by 2 February 2026 | Art 6(5) `B` - **the guidelines themselves are not held; see Limitations** |
| Commencement: 2 Dec 2027 | Art 113(c)(i) `M1` |

### Gate 4 - transparency (walkthrough section 6)

| Statement | Source |
|---|---|
| Interaction disclosure (provider duty); obviousness standard; law-enforcement exception | Art 50(1) `B` |
| Machine-readable marking of synthetic audio, image, video, text (provider duty); assistive-editing carve-out | Art 50(2) `B` |
| Emotion recognition / biometric categorisation disclosure (deployer duty) and data protection compliance | Art 50(3) `B` |
| Deep fake disclosure; artistic-work limitation; public-interest text duty and editorial-control exception | Art 50(4) `B` |
| Clear provision at first interaction or exposure | Art 50(5) `B` |
| Duties do not affect Chapter III - the basis for "overlay, not a tier" | Art 50(6) `B` |
| Codes of practice on detection, marking, labelling; Commission implementing act fallback | Art 50(7) `M1` |
| Commencement: 2 Aug 2026 (Chapter IV is not carved out of the general date) | Art 113, second paragraph `B` |

### Gate 5 - residual duties (walkthrough section 7)

| Statement | Source |
|---|---|
| AI literacy duty on providers and deployers; no guaranteed individual level | Art 4(1) `M1` (Article 4 as amended; the omnibus added support duties in Art 4(2)-(3) `M1`) |
| GPAI model duties fall on the model provider; systemic-risk tier | Arts 51-56 (Chapter V) `B`/`M1`; classification rule Art 51(1) `B` |
| Commencement: literacy 2 Feb 2025 (Chapter I); GPAI 2 Aug 2025 | Art 113(a) `M1`, 113(b) `B` |

### Commencement table (walkthrough section 8)

Verified against Article 113 as amended, in full:

| Provision | Applies from | Source |
|---|---|---|
| The Regulation generally (incl. Chapter IV, Art 50) | 2 August 2026 | Art 113, second paragraph `B` |
| Chapters I and II | 2 February 2025 | Art 113(a) `M1` |
| - except Art 5(1) points (ba), (bb) and Art 5(1a), (1b) | 2 December 2026 | Art 113(a) `M1` |
| Ch III S4, Ch V, Ch VII, Ch XII, Art 78 (except Art 101) | 2 August 2025 | Art 113(b) `B` |
| Ch III Ss 1-3 (except Art 6(5)) - Annex III high-risk | 2 December 2027 | Art 113(c)(i) `M1` |
| Ch III Ss 1-3 (except Art 6(5)) - Annex I high-risk | 2 August 2028 | Art 113(c)(ii) `M1` |
| Articles 102 to 110 | 27 July 2026 | Art 113(d) `M1` |

### Worked example and quick-fire rows (walkthrough sections 9-10)

| Call made | Basis |
|---|---|
| CV screening: high-risk, listed item, derogation blocked by profiling | Annex III 4(a) `B`; Art 6(3) third subparagraph `B` |
| Video "engagement" add-on prohibited | Art 5(1)(f) `B` - recruitment interviews are within "the areas of workplace and education institutions"; the walkthrough treats candidate assessment as within the workplace area, consistent with the provision's purpose. A narrower reading is conceivable; the artifact states the safer position |
| Row 2 (staff-meeting engagement scoring) prohibited | Art 5(1)(f) `B` |
| Rows 3-4 (credit scoring; fraud detection exception) | Annex III 5(b) `B` |
| Row 5 (cosmetic quality control not a safety component) | Art 6(1a) `M1` |
| Row 6 (guard-zone system; machinery) | Art 6(1b) `M1`; Annex I item 21 `M1`; Art 2(2) `M1` |
| Row 7 (medical device module) | Art 6(1)(a)-(b) `B`; Annex I Section A item 11 `B` (Regulation (EU) 2017/745) |
| Row 8 (image generator marking; deep fakes) | Art 50(2), 50(4) `B` |
| Row 9 (post-decision formatting assistant; derogation arguable, must be documented and registered) | Art 6(3)(a), (d) `B`; Art 6(4) `B`; Art 49(2) `B` |

## Corrections and findings recorded openly

1. **A supplied source contained no law.** The corpus for this artifact was
   supplied with a EUR-Lex print intended to be the consolidated GDPR
   (`CELEX:02016R0679-20160504`). The file is a one-page EUR-Lex error page
   reading "The requested document does not exist." - a malformed request URL
   (the CELEX number doubled in the query). Nothing in this artifact needed the
   GDPR, so nothing is affected; it is recorded because a source register that
   lists a file nobody opened is how unverified law gets cited. The register
   lists it as supplied-but-empty.
2. **File identity vs text identity.** The consolidated AI Act file held for
   this artifact hashes differently from the copy held for the Part 1 EU policy
   set (different download of the same consolidation). Identity was therefore
   verified from the text itself: the consolidation stamp
   `02024R1689 - EN - 27.07.2026 - 001.001` on every page and the M1 reference
   to Regulation (EU) 2026/1744 in the amendment table. The hashes in the source
   register authenticate the files actually read, not the CELEX version in the
   abstract.
3. **Article 4 is now titled "AI literacy".** Part 1's research note described
   the duty as "staff knowledge and skills" from the as-adopted text; in the
   consolidation the whole Article carries the M1 marker and the omnibus added
   Commission, Member State and Board support duties. The substance of the duty
   on organisations is unchanged; the walkthrough uses the consolidated framing.

## Limitations - stated rather than left to be found

1. **The Article 6(5) Commission guidelines are not held.** They were due by
   2 February 2026 and concern the practical implementation of Article 6 with
   worked examples. Nothing in this artifact rests on them, and no contested
   derogation call should be made without obtaining the current version.
2. **Annex I is verified as a list, not as a body of product law.** The
   underlying product legislation (machinery, medical devices, and the rest) was
   not read for this artifact. Gate 2 outcomes in a real case depend on that
   legislation's conformity assessment rules; rows 6 and 7 of the quick-fire
   table state the AI Act side of the analysis only.
3. **Directive 2011/93/EU is not held.** The CSAM prohibition defines its
   subject matter by reference to that Directive; the walkthrough states the
   prohibition without restating the Directive's definitions.
4. **The GDPR interplay is out of scope by design.** Automated decision-making
   rights, lawful basis and DPIA triggers interact with every classification
   outcome and are covered in the Part 1 policy sets; this artifact classifies
   under the AI Act only.
5. **The emotion-inference boundary in recruitment.** The prohibition covers
   "the areas of workplace and education institutions". This artifact takes
   candidate assessment to be within it. The consolidated text does not define
   the boundary and the Article 6(5)-adjacent guidance on prohibited practices
   is not held; the position taken is the protective one and is flagged where it
   is applied.
6. **No provision cited here has been reviewed by qualified counsel.**

## Watch items

- **Article 6(5) guidelines** - obtain; check whether issued on time and in what
  form.
- **Article 50(7) codes of practice** on marking and labelling, and any
  Commission implementing act if codes are found inadequate.
- **Delegated acts under Article 6(6)-(7)** amending the derogation conditions,
  and under Article 7 amending Annex III itself - the list is amendable and the
  item-by-item verification in this note is dated 1 September 2026.
- **Article 2(13) delegated acts** (due by 2 August 2027) limiting which
  high-risk requirements apply to Section A Annex I products - they will change
  the practical weight of a Gate 2 outcome.
- **Any further amendment to Article 113.** The dates are the spine of
  walkthrough section 8; they have been amended once already.
