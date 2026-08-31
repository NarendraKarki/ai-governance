# Source register - Bahrain AI policy set

Every document referred to, used, or deliberately not used in producing the Bahrain
AI Acceptable Use Policy v1.0, the Enterprise Annex v1.0, and the research note.

Corpus state as at 3 August 2026. Hashes are SHA-256 of the held file, truncated to
16 characters; the full values are in the platform's source inventory.

---

## 1. Bahraini primary law - HELD AND CITED

| # | Instrument | File | Tier | SHA-256 | Articles cited |
|---|---|---|---|---|---|
| 1 | **Law No. (30) of 2018** - Personal Data Protection Law (Arabic, enacted) | `law_30_2018_arabic.md` | enacted_text | `dafbf16e251cba72` | 15, 22 |
| 2 | **Law No. (30) of 2018** - official English translation | `law_30_2018_english.md` | translation | `091d034c7c60a847` | 3, 4, 5, 7, 8, 9, 10, 12, 13, 14, 17, 18-23, 24, 25, 38, 58, 59 |
| 3 | **MoJ Order No. (42) of 2022** - transfer outside the Kingdom (Arabic, enacted) | `order_42_2022_arabic.md` | enacted_text | *new 3 Aug 2026* | 1-6 and the schedule |
| 3a | **MoJ Order No. (42) of 2022** - official English translation | `order_42_2022_transfer_outside_bahrain.md` | translation | `100e30d996a7ff4f` | 2, 3, 4, 5 |
| 4 | **MoJ Order No. (43) of 2022** - technical and organisational measures (Arabic, enacted) | `order_43_2022_arabic.md` | enacted_text | `5011d6fcb045e453` | 3(ب), 3(ج), 4(ب), 4(هـ) |
| 5 | **MoJ Order No. (43) of 2022** - official English translation | `order_43_2022_technical_measures.md` | translation | `ce0dcf0da54cd04c` | 3 - used only to establish the divergence in Finding 1 |
| 6 | **MoJ Order No. (44) of 2022** - notifications and prior authorisation requests | `order_44_2022_notifications_and_authorizations.md` | translation, **cited articles verified against enacted Arabic 31 Aug 2026** | `cfce95b13a8027bb` | 2, 4, 5, 6, 7 |
| 7 | **MoJ Order No. (45) of 2022** - sensitive personal data | `order_45_2022_sensitive_data.md` | translation, **cited articles verified against enacted Arabic 31 Aug 2026** | `0a09fea2a2784139` | 2, 3, 4 |
| 8 | **MoJ Order No. (46) of 2022** - Data Protection Guardians | `order_46_2022_data_protection_guardians.md` | translation, **cited articles verified against enacted Arabic 31 Aug 2026** | `bddac252878eee8a` | 2, 4, 13 |
| 9 | **MoJ Order No. (48) of 2022** - data subject rights | `order_48_2022_data_subject_rights.md` | translation, **cited articles verified against enacted Arabic 31 Aug 2026** | `8844f21749fc113d` | 3, 4 |

**Provenance of the two enacted-text files.** Order 43/2022 was transcribed from
Official Gazette issue 3593, 17 March 2022, pages 92-97, using dual extraction
(geometric RTL for structure and digits, Tesseract `ara` OCR for letters), and the
operative sentences are reproduced only where both passes agree. The PDPL Arabic was
transcribed from `L3018.pdf` (mola.gov.bh) on 29 July 2026 using a **single**
strategy, `geometric_rtl`, and therefore sits at lower transcription confidence.

Neither file carries a `verified_by` sign-off. Both are
`retrieved_not_yet_legally_verified`.

## 2. Bahraini primary law - HELD BUT NOT CITED

Present in the corpus, read for relevance, no obligation in these documents rests on
them.

| Instrument | File | Tier | SHA-256 |
|---|---|---|---|
| MoJ Order No. (47) of 2022 - Guardian register fees | `order_47_2022_guardian_register_fees.md` | translation | `fdae0279cb5fcb98` |
| MoJ Order No. (49) of 2022 - complaints procedure | `order_49_2022_complaints.md` | translation | `2fc397e0909e67a1` |
| MoJ Order No. (50) of 2022 - criminal proceedings data | `order_50_2022_criminal_proceedings_data.md` | translation | `8de6cfe22ac2809f` |
| MoJ Order No. (51) of 2022 - public registers | `order_51_2022_public_registers.md` | translation | `5a4390beedc1a9ee` |

Order 49 is the natural source for the complaints machinery in Policy 13 and Annex
A9. It was not used, so those clauses rest on PDPL Article 25 alone and on house
practice. Worth revisiting.

## 3. NOT HELD - the gaps that shape what these documents can say

| What is missing | Consequence in the documents |
|---|---|
| ~~**Arabic of Orders 42, 44-51**~~ **NO LONGER MISSING** | All ten Orders 42-51 are in Official Gazette 3593, pages 87-123, which has been on disk since 30 July. See section 8 |
| **Any Bahraini AI-specific instrument** | These documents govern AI use *under data protection law*. Nothing here reflects an AI statute, strategy or guideline, because none is held |
| **Bahraini equality or anti-discrimination legislation** | Policy 16 carries no citation and is a house standard |
| **Bahraini intellectual property / copyright law** | Policy 14.1 is a house standard; no statutory basis is asserted |
| **Bahraini employment / labour law on monitoring** | Policy 17 rests on the general data protection duties only |
| **CBB Rulebook** | Annex A10.1 is a pointer. PDPL Article 38 shows a CBB notification route exists; the mapping is not asserted |
| **A current version of Order 48/2022** | pdp.gov.bh indicates a 2025 gazette date for data subject rights; the corpus holds a 2022 version. Policy 9.3 and Annex A7 rest partly on it. **This is now the only Bahraini instrument that genuinely needs downloading** |
| **Confirmation that the March 2022 adequate-countries record is still current** | Policy 8.3 requires re-checking it at review rather than assuming |
| **Any Authority guidance** | No Bahraini regulator guidance is held, so DPIA criteria and monitoring expectations rest on the statutory text alone |

## 4. Document architecture

[ORGANISATION] supplied an existing policy set as a structural template. Only its
architecture was used: section order, tone, the convention that article numbers live
in the research note rather than the policy body, and the practice of flagging house
standards that exceed statute.

**No legal source from that template was carried across.** Every obligation in this
set was derived independently from the Bahraini instruments listed in section 1. No
Bahraini obligation was inferred from any other jurisdiction's provision. Where the
template carried a citation and Bahrain has no held equivalent, the clause here is an
unsourced house standard and is labelled as such.

## 5. Documents PRODUCED

| Document | Version | Status |
|---|---|---|
| `Bahrain_AI_Acceptable_Use_Policy.md` | 1.0 | Draft. Section 4.2 corrected after Arabic re-check |
| `Bahrain_AI_Governance_Enterprise_Annex.md` | 1.0 | Draft |
| `Bahrain_policy_research_note.md` | 1.0 + corrections | Carries Findings 1-2 and Corrections 1-2 |
| `Bahrain_source_register.md` | 1.1 | This document |
| `order_42_2022_arabic.md` | - | **New corpus file.** Enacted Arabic of Order 42, six articles verified, 83-entry schedule dual-verified. Drop into `bahrain_pdpl/` |

## 6. Sources NOT used, as a matter of method

- **No web content.** No figure, provision, date or article number in any of these
  documents was taken from a web page. Web material is used only to raise doubt that
  a document exists or is current; it never becomes authority.
- **No AI-generated legal content.** Every provision cited resolves to text in a file
  listed in section 1 above.
- **No secondary commentary, law-firm briefing, or comparative summary.**

## 7. Standing caveat

No provision cited in this set has been signed off by a Bahraini-qualified lawyer.
The two enacted-text files are transcriptions that carry no legal verification. These
documents are educational templates and do not constitute legal advice.


---

## 8. ADDENDUM 3 August 2026 - what was already on disk

Official Gazette issue 3593 (17 March 2022, 160 pages), retrieved 30 July 2026 and
recorded in the source inventory, **contains the enacted Arabic of all ten Orders**,
not only Order 43. Located by text extraction:

| Order | Subject | Pages in 3593 |
|---|---|---|
| 42/2022 | transfer of personal data outside the Kingdom | 87-89 |
| - | **record of countries and territories with adequate protection, 83 entries** | **90-91** |
| 43/2022 | technical and organisational measures | 92-97 |
| 44/2022 | notifications and prior authorisation requests | 98-101 |
| 45/2022 | processing of sensitive personal data | 102-103 |
| 46/2022 | Data Protection Guardians | 104-110 |
| 47/2022 | Guardian register fees | 111-113 |
| 48/2022 | data subject rights | 114-116 |
| 49/2022 | complaints | 117-119 |
| 50/2022 | criminal proceedings data | 120-121 |
| 51/2022 | public registers | 122-123 |

**Why this was not noticed until now.** The controlled search that cleared the
neighbouring issues 3592 and 3594 looked for اختراق, انتهاك and اكتشاف - breach
vocabulary. Orders 42 and 44-51 concern transfers, notifications, sensitive data,
guardians, fees, rights, complaints, criminal data and public registers, and contain
none of those words. The search could not have found them. The negative finding was
sound for the question it asked and silent on this one.

Only Order 43 was transcribed from this file. **Nine Orders remain untranscribed in a
document already held, hashed and declared.** Transcribing them would move nine
Bahraini instruments from `translation` to `enacted_text` without downloading
anything.


---

## 9. RECOMMENDATION 3 August 2026 - what to do next, and what not to

**Do not batch-transcribe the remaining eight Orders.** Order 42 came back with no
divergence from its translation. That is new evidence and it lowers the expected
yield of the exercise: the assumption that "Order 43 had five errors, so the others
will too" now has one clean counter-example. Transcribe an Order when a position
actually rests on it, starting with Order 44, on which Section 4 of the policy is
built.

**Do these three first.**

1. **Settle whether Order 48/2022 was superseded in 2025.** Highest live risk. If it
   was, the corpus holds and cites a repealed instrument, and Policy 9.3, Annex A7
   and the automated-decisions position all rest on it. `repealed_article` is its own
   category in the platform's adversarial set for good reason. Nothing in Gazette
   3593 resolves this - it needs the 2025 issue.
2. **Re-run the PDPL Arabic through the dual pipeline.** It is the most-cited
   Bahraini instrument and carries the weakest transcription in the corpus - single
   `geometric_rtl` strategy, no second pass. The dual method is now proven against
   Order 43. No download required.
3. **Decide Finding 1** - whether the registry entry for Order 43 Article 3 is
   re-grounded on the Arabic's four DPIA triggers rather than the translation's
   three. This changes what the platform asserts and therefore is not a decision
   these documents can make.

**Cheap and worth doing while there:** re-search Gazette issues 3592 and 3594 with
the right vocabulary. The existing negative finding searched breach terms only
(اختراق, انتهاك, اكتشاف), which is why it could not have found Orders 42 and 44-51
had they been there. Searching قرار رقم and البيانات الشخصية would close the question
deliberately rather than by accident.

---

## 10. ADDENDUM 31 August 2026 - Arabic verification completed

The two items in section 9's "do these first" that gate publication are
closed, together with the recommendation's larger aim:

- **PDPL second extraction.** The mola.gov.bh source document (`L3018`, Word
  format) was read through its native text layer - an independent extraction
  path from the corpus transcription's single `geometric_rtl` pass. Every
  PDPL article cited in the research note was verified against it. No
  divergence affecting a policy position.
- **Orders 44, 45, 46 and 48.** The cited articles were read in the enacted
  Arabic from Gazette 3593's embedded text layer (pages 98-116), with the
  operative clauses confirmed visually against the page images. No
  divergence affecting a policy position. Precision notes and two new
  findings (Order 48's cookie-wall invalidity and withdrawal rules) are in
  the research note's 31 August addendum.

Section 9's counsel against batch transcription stands: these are targeted
verifications of the cited articles, not full transcriptions. The
translation files remain in the corpus at translation tier; what changed is
that every citation that rests on them has now been checked against the
enacted text. Order 48/2022 supersession and adequacy-record currency were
closed 30 August 2026 (research note addendum).
