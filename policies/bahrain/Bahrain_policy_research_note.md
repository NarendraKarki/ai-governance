# Research note - Bahrain AI Acceptable Use Policy (v1.0) and Enterprise Annex (v1.0)

Purpose: records the primary-source verification behind each obligation, per the
project rule that article numbers live in the research record, not the artifact body.
Educational, not legal advice.

## Sources verified (held in the platform corpus, hashed on ingest)

- **Law No. (30) of 2018 with respect to Personal Data Protection Law**. Held twice:
  the **authoritative Arabic** (`law_30_2018_arabic.md`, tier: **enacted_text**,
  source `L3018.pdf` from mola.gov.bh, transcribed 29 July 2026) and the official
  English translation (`law_30_2018_english.md`, tier: translation). The table below
  was built from the **translation**; Articles 15 and 22 were subsequently re-checked
  against the Arabic. See Correction 1.
- **MoJ Order No. (42) of 2022** - transfer of personal data outside the Kingdom.
  Tier: translation.
- **MoJ Order No. (43) of 2022** - technical and organisational measures. Held twice:
  the **authoritative Arabic** from Official Gazette issue 3593, 17 March 2022, pages
  92-97 (`order_43_2022_arabic.md`, tier: **enacted_text**), and the official English
  translation (`order_43_2022_technical_measures.md`, tier: translation). Where the
  two differ, the Arabic governs.
- **MoJ Order No. (44) of 2022** - notifications and prior authorisation requests.
  Tier: translation.
- **MoJ Order No. (45) of 2022** - sensitive personal data. Tier: translation.
- **MoJ Order No. (46) of 2022** - Data Protection Guardians. Tier: translation.
- **MoJ Order No. (48) of 2022** - data subject rights. Tier: translation.

Verification date: 3 August 2026.

**Nothing in these documents rests on web content.** No figure or provision was taken
from a web page.

## Obligation -> policy clause -> source

| Obligation (as expressed in artifact) | Clause | Source and article (verified) |
|---|---|---|
| Lawful ground before processing; consent unless a listed necessity applies | Policy 7.1 | PDPL Art 4 |
| Consent must be explicit and in writing, including electronically, obtained before processing | Policy 7.1 | Order 48/2022 Art 4, referring to PDPL Art 24 |
| Purpose limitation; no training on customer or staff data without separate assessment | Policy 7.2 | PDPL Art 3(2) |
| Adequate, relevant, not excessive | Policy 7.3 | PDPL Art 3(3) |
| Accuracy and currency | Policy 7.4 | PDPL Art 3(4) |
| Retention; no identification once purpose achieved; anonymise or encrypt for long-term historical, statistical, scientific use | Policy 7.5 | PDPL Art 3(5) |
| **Prior notice to the Authority of wholly or partially automated processing**, with exemptions incl. where a Data Protection Guardian is appointed | Policy 4.1 | PDPL Art 14(1) and the exemptions at Art 14(1)(a)-(d); procedure Order 44/2022 Art 2 |
| **Prior written authorisation** for automatic processing of sensitive data **in the Art 5(2) incapacity case**; biometric data for identity verification; genetic data; linkage of files of two or more controllers processed for different purposes; visual recording for surveillance | Policy 4.2, Level 4 | PDPL Art 15(1)(أ)-(هـ), **verified against the Arabic**. See Correction 2 |
| Thirty days to decide; **no reply = implied rejection** | Policy 4.2, Annex A2A.2 | PDPL Art 15(3); Order 44/2022 Art 4 (verified verbatim: "it is deemed as an implied rejection") |
| Authorisation does not waive the need for consent | Policy 4.4 | Order 44/2022 Art 4, final paragraph |
| Obligations of the authorised processor: transparency, non-excessive processing, restricted access, subject access | Annex A3, Policy 7 | Order 44/2022 Art 5 |
| Change notification within thirty days | Policy 4.3, Annex A2A.4 | PDPL Art 14(6); Order 44/2022 Art 7 |
| DPIA mandatory triggers | Policy 7.6 | **Order 43/2022 Art 3(ج) - Arabic**. See Finding 1 below |
| DPIA must seek the Data Protection Guardian's advice where designated | Policy 7.6, Annex A3.1 | Order 43/2022 Art 3(ب) |
| DPIA minimum content | Annex A3.1 | Order 43/2022 Art 3(4) |
| DPIA required with a prior authorisation request for biometric and visual-recording surveillance | Policy 7.6, Annex A2A | Order 44/2022 Art 6 |
| Individuals' rights not defeated by tool choice | Policy 7.7, Annex A7 | PDPL Arts 18-23 |
| Sensitive personal data - prohibited without consent save listed cases | Policy 7.8 | PDPL Art 5; Order 45/2022 Arts 2-4 |
| Criminal-proceedings data restricted | Policy 7.9 | PDPL Art 7 |
| **Transfers outside Bahrain prohibited** except to a listed adequate country or on case-by-case authorisation | Policy 8.1 | PDPL Art 12; Order 42/2022 Art 2 |
| Derogations, including consent to the transfer | Policy 8 (not enumerated in body) | PDPL Art 13(1) |
| Record of countries and territories with adequate protection, 83 entries | Policy 8.2 | Order 42/2022, schedule. **Dual-verified**: English translation and Gazette 3593 pp.90-91 Arabic |
| Contract terms required for transfer to a controller or third party outside the listed territories | Policy 8.4 | Order 42/2022 Art 5(1)-(6) |
| Intra-group transfers to unlisted destinations need authorisation plus corporate rules | Policy 8.5 | Order 42/2022 Art 4 |
| Human review before a significant decision takes effect | Policy 9.1-9.2 | **STRICTER THAN LAW, DELIBERATELY.** See "House standards" below |
| Right to require reconsideration other than by solely automated means; obligatory and free of charge; scoped to performance at work, financial standing, creditworthiness, reliability, conduct | Policy 9.3 | PDPL Art 22(1), **verified against the Arabic**. Contract carve-out at Art 22(2) |
| Inform the data subject of the automated decision; operate a clear electronic objection procedure and inform of the outcome within a reasonable period | Policy 9.3 | Order 48/2022 Art 3(1)-(2) |
| Security: appropriate technical and organisational measures, **recorded and accessible** to the Authority, controller and processor | Policy 12.4 | PDPL Art 8(1) |
| Processor selection and **written** contract; processor acts only on instructions; equivalent security and confidentiality duties | Policy 3.2, Annex A4.1 | PDPL Art 8(3) |
| Confidentiality; no disclosure without consent or judicial order; survives end of employment | Policy 7.10-7.11 | PDPL Art 9 |
| Breach notification to the Authority within a short statutory period **running from discovery**, unless unlikely to lead to a risk threatening data subjects' rights; late notification must carry justification | Policy 13 | **Order 43/2022 Art 4(ب) - Arabic.** Verbatim: "خلال مدة لا تجاوز اثنان وسبعين ساعة من وقت اكتشافه" - within a period not exceeding seventy-two hours from the **time** of its discovery. See Limitation 2 |
| Authority may compel notification of individuals where the incident may lead to high risks | Policy 13 | Order 43/2022 Art 4(ب), Arabic |
| Content of a breach notice to individuals: type and nature, details of data affected, mitigation recommendations | Policy 13 | Order 43/2022 Art 4(هـ)(1) |
| Content of a breach notice to the Authority, including **root cause and prevention of recurrence** | Not in policy body; see Finding 2 | Order 43/2022 Art 4(هـ)(2)(أ)-(هـ) |
| Information to be provided to the data subject at collection; and within five days where data was not obtained from them | Policy 15.2 | PDPL Art 17(1), 17(2) |
| Complaints to the Authority by anyone with a legitimate interest | Policy 13, Annex A9.1 | PDPL Art 25 |
| Data Protection Guardian: duties, independence, register enrolment, appointment notified within three working days | Policy 18, Annex A1.4 | PDPL Art 10(1)-(4); Order 46/2022 Arts 2, 4, 13 |
| Criminal penalties; imprisonment up to one year and/or BD 1,000-20,000 | Policy 1, 2 | PDPL Art 58(1), incl. 58(1)(3) failure to notify under Art 14(1) and 58(1)(5) processing without Art 15 authorisation |
| Fines doubled for legal persons where the offence results from act, omission, approval, cover-up or gross negligence of a board member or delegated official | Policy 1, Annex A1.2 | PDPL Art 59 |
| CBB notification pointer for financial services | Annex A10.1 | PDPL Art 38 - **pointer only, not a mapping** |

## CORRECTIONS to v1.0 of this note, made 3 August 2026

### Correction 1 - the PDPL Arabic is held, and I built the table from the translation

The first version of this note stated that only Order 43/2022 is held in enacted
Arabic. **That was wrong.** `law_30_2018_arabic.md` is held, tier `enacted_text`,
transcribed from `L3018.pdf`. Every PDPL citation in the table below was nonetheless
verified against the English translation, because I did not check the corpus before
starting - the exact failure this project exists to prevent, committed while writing
a document about preventing it.

Two provisions carrying most of the policy's weight have since been re-checked
directly against the Arabic:

- **Article 15** - the five categories requiring prior written authorisation, the
  thirty-day period and the implied rejection all match the translation. The Arabic
  fifth limb reads هـ- المعالجة التي تكون عبارة عن تسجيل بصري مما يستخدم لأغراض المراقبة.
- **Article 22** - the five assessment types (أدائه في العمل، مركزه المالي، مدى كفاءته
  للاقتراض، سلوكه، مدى جدارته بالثقة), the free-of-charge reconsideration (دون مقابل)
  and the contract carve-out all match.

**The remaining PDPL citations in the table are translation-grounded and provisional.**

Note also that the Arabic PDPL was transcribed by a **single** extraction strategy
(`geometric_rtl`), not the dual method used for Order 43. It is authoritative text
held at lower transcription confidence, and should be dual-verified before any
position turns on a fine reading of it.

### Correction 2 - Policy 4.2 overstated the sensitive-data trigger

v1.0 of the policy listed "automatic processing of sensitive personal data" as
requiring prior written authorisation, without qualification. Both texts scope it
more narrowly: PDPL Art 15(1)(أ) applies it to the case referred to in **Article
5(2)** - processing necessary to protect a person where the data subject or their
guardian is legally incapable of giving consent.

Stating a duty more broadly than the statute grants it is one of the failure modes
the platform's own gate blocks. Policy 4.2 has been corrected. Sensitive personal
data remains Level 3 and still requires the data protection lead's approval and a
lawful ground under Article 5; it is the **authorisation** trigger that is narrower
than v1.0 claimed.

### Correction 3 - the adequate-countries record is held, and I said it was not

v1.0 of this note and of the source register both listed the Order 42/2022 record of
countries and territories with adequate protection as **not held**, and called it the
largest practical gap in the set. Both statements were wrong. The record sits at the
end of the English translation already in the corpus, and the enacted Arabic is at
Official Gazette 3593 pages 90-91.

**Both sources carry 83 entries and agree**, which makes this one of the few Bahraini
positions in the corpus with genuine dual-source verification.

The record includes the **United States**, the **United Kingdom**, the EEA states,
**India**, **Singapore**, the **United Arab Emirates**, **Saudi Arabia**, Kuwait,
Oman, Canada, Australia, Japan, South Korea, Switzerland, **China**, Hong Kong,
Russia and Brazil. Practically, that means most mainstream AI hosting regions need no
case-by-case authorisation, and Policy 8 has been rewritten from "establish the
position" to "check the current record, then establish where processing actually
happens".

**This is the second time in this piece of work that I asserted an absence without
searching the corpus** - the first being Correction 1, the PDPL Arabic. The project's
own inventory already carries the worked example of this failure: the withdrawn
negative finding that "Bahrain PDPL creates no personal data breach notification
obligation", asserted after searching 2 of 12 Bahraini instruments. I repeated it
twice in one document. Recorded rather than quietly fixed.

**Currency caveat.** The record is as gazetted on 17 March 2022. The Authority may
have amended it since. Nothing in the corpus establishes that the March 2022 list is
still current, and Policy 8.3 therefore requires it to be re-checked at review.

## FINDINGS - new, and requiring your decision before publication

### Finding 1 - the English translation of Order 43 omits a mandatory DPIA trigger

The authoritative Arabic of Order 43/2022 Article 3(ج) lists **four** cases in which
a DPIA must be carried out. The official English translation held in the corpus
(`order_43_2022_technical_measures.md`) lists **three**. The missing fourth is:

> غ- معالجة البيانات بواسطة التسجيل البصري أو المعالجة الآلية لبيانات القياسات الحيوية

- processing of data by **visual recording**, or **automatic processing of biometric
data**.

This matters directly for an AI policy. Camera analytics and biometric identification
are among the most common enterprise AI proposals, and an organisation working from
the English translation would conclude a DPIA is discretionary for them.

**Corroboration.** Order 44/2022 Article 6 - a different instrument, and in English -
independently requires a DPIA to be undertaken when submitting a prior authorisation
request concerning automatic processing of biometric data and visual-recording
surveillance. Two documents with non-overlapping provenance agree, which is why this
is stated in Policy 7.6 rather than merely flagged.

**This is a fifth divergence between the Order 43 translation and the enacted text**,
on top of the four recorded on 30 July 2026 (paragraph lettering, date versus time,
the disapplication test, and the number of exemptions). It is your call whether it
also warrants a change in the rules engine's registry entry for Order 43 Article 3.
Nothing has been changed in the platform.

### Finding 2 - the regulator notice requires root cause and prevention of recurrence

Order 43/2022 Article 4(هـ)(2) sets five mandatory contents for a breach notice to
the Authority. The fifth - الإجراءات المتخذة لمعالجة السبب الرئيسي المؤدي للخرق،
ومنع تكراره, the measures taken to address the **root cause** and prevent recurrence
- is a distinct, mandatory element of the notice, and it calls for root-cause
analysis rather than a description of containment. It is not restated in the policy
body because the policy is not a notification template. Noted here so it is not lost
when a notification template is drafted.

## House standards that EXCEED or sit outside Bahraini statute (flagged, kept knowingly)

- **Policy 9.1 pre-decision human review.** PDPL Article 22 gives a *right to request*
  reconsideration by non-automated means after a decision, scoped to five listed
  assessment types, with a contract carve-out at Art 22(2). The policy instead
  requires meaningful human review **before** the decision takes effect, for a wider
  class of significant decisions. This is a conscious design choice and is labelled as
  such in Policy 9.4 rather than presented as law.
- **Policy 15.1 (tell customers they are interacting with AI).** No general Bahraini
  statutory chatbot-disclosure duty was found in the held corpus. Kept as a house
  standard. Sector rules may impose more.
- **Policy 16 non-discrimination.** No Bahraini equality statute is held in the
  corpus, so there is **no citation here** and the clause is carried as a house
  standard rather than as a legal obligation. If a Bahraini equality or labour-law
  basis is wanted, the instrument must be obtained first.
- **Policy 19.1 training.** No Bahraini statutory AI-literacy duty. Good practice.
- **Annex A5.2** (no exception against a statutory requirement) is a governance
  control, not a statutory rule, but follows directly from the criminal character of
  Arts 14 and 15.

## Annex provisions - basis

- A1 (committee, accountable executive, three lines), A2 (inventory), A3 (lifecycle),
  A5 (exceptions), A6 (agentic AI), A8 (assurance): good-practice governance
  controls, not statutory duties. No article numbers claimed in body.
- **A2A (regulatory filings register) is different**: it is a governance wrapper
  around genuine statutory duties (PDPL Arts 14, 15; Order 44/2022), and unlike the
  rest of the annex it exists to track a legal precondition to deployment rather
  than to improve practice.
- A4 (supplier terms): PDPL Art 8(3) underpins the written-contract requirement; the
  AI-specific terms are contractual good practice beyond statute.
- A7 (individual rights operations): PDPL Arts 18-23 and Art 23(5) third-party
  notification.
- A10: sector overlay is a pointer, not a mapping. PDPL Art 38 shows a CBB
  notification route exists; **the mapping itself is not asserted** and must be
  verified separately before publication.

## Limitations - stated rather than left to be found

1. **Most citations above rest on official English translations, not enacted text.**
   Enacted Arabic is held for **two** instruments: the PDPL and Order 43/2022. Of the
   PDPL citations here, only Articles 15 and 22 have been checked against it (see
   Correction 1); the rest are translation-grounded. **Orders 42, 44, 45, 46 and 48
   are held only in translations that disclaim being the law**, and every citation to
   them is provisional. Reading the Arabic of Order 43 corrected five things. It would
   be surprising if the other instruments contained none.
2. The 72-hour breach clock is grounded in the enacted Arabic, but reading "establish
   specific procedures to notify the Authority within 72 hours" as a **deadline
   binding the Controller** remains an approved interpretation (29 July 2026), not a
   quotation. The Arabic does not resolve it either way. Policy 13 therefore says "a
   short statutory period" rather than stating a number.
3. **CORRECTED - the record of adequate countries IS held, and is now
   dual-verified.** v1.0 of this note said it was missing. It is present at the end of
   `order_42_2022_transfer_outside_bahrain.md` (English translation, 83 entries) and
   in the enacted Arabic at Official Gazette 3593 pages 90-91 (83 entries). Both
   agree on the count. See Correction 3.
4. **No Bahraini AI-specific legislation is held.** These documents govern AI use
   under data protection law. If Bahrain has enacted or issued anything addressed to
   AI specifically, it is not in the corpus and nothing here reflects it.
5. **No provision cited here has been signed off by a Bahraini-qualified lawyer.**
6. The regulator is referred to as "the Authority", following the Law. The platform's
   registry labels it `PDO`; the Orders are issued by the Minister of Justice, Islamic
   Affairs and Waqf. The public-facing name should be confirmed before the documents
   are put in front of staff.

## Watch items

- **Order 48/2022 may be superseded.** pdp.gov.bh shows a 2025 gazette date for data
  subject rights, while the corpus holds a 2022 version. Policy 9.3 and Annex A7 rest
  partly on Order 48; obtain the current text before adoption.
- **Arabic of Orders 42, 44-51** - obtaining these is the single highest-value
  verification step available, for the reason in Limitation 1. The PDPL Arabic is
  already held but warrants a second extraction pass (Correction 1).
- Re-verify the remaining PDPL rows in the table above against the held Arabic.
- Whether the March 2022 adequate-countries record has been amended since.
- Whether Finding 1 should change the registry entry for Order 43 Article 3.

## ADDENDUM 30 August 2026 - watch items resolved

### Order 48/2022 - no supersession found
The 2025-supersession concern is closed as unfounded on present evidence. The
Authority's public site currently serves Order No. (48) of 2022 (issued 17
March 2022) as the operative data subject rights instrument; its article
headings match the corpus copy (definitions; scope; obligations related to
decisions based on automated processing; consent and its scope; unconsidered
consent; withdrawal; objection procedure; entry into force) and it contains no
amendment or repeal language. Searches surface no 2025 instrument on data
subject rights. The "2025 date" previously seen on pdp.gov.bh most plausibly
referred to a re-reviewed English translation (the current file is named
"Data-Subjects-Rights-REVIEWED.pdf"), not a new order. Method note: per the
source register, web material resolves doubt about existence and currency; it
does not become authority. Citations to Order 48 remain translation-tier until
the enacted Arabic (Gazette 3593 pp. 114-116, already held) is transcribed.

### Adequate-countries record - current as published
The record served today on the Authority's site is Order 42/2022's schedule
with 83 entries, matching the dual-verified corpus list entry for entry. No
amendment indicated. Policy 8.3's re-check-at-review instruction stands; the
currency doubt is answered as at 30 August 2026.

### One-page staff guide added
Bahrain_AI_Use_OnePager.md added 30 August 2026, completing the two-layer
structure. Its rules restate the policy; it introduces no new obligation and
cites nothing directly.

### Remaining before the draft banner lifts
1. Re-verify the translation-grounded PDPL citations against the held Arabic
   (dual-pipeline re-run recommended - platform-side work).
2. Transcribe the Arabic of Orders 44, 45, 46 and 48 from Gazette 3593
   (already held), starting with Order 44, on which policy Section 4 rests.
