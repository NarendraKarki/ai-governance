# Source register - AI Risk Registers and Model Inventories walkthrough

Every document supplied for, used in, required by, or deliberately not used in producing the walkthrough v1.0, its worked example and its research note.

State as at **21 September 2026**. Hashes are SHA-256 of the file as supplied, truncated to 16 characters.

---

## 1. Primary law - HELD AND CITED

| # | Instrument | Version | SHA-256 | Provisions cited |
|---|---|---|---|---|
| 1 | **Regulation (EU) 2024/1689 - consolidated** (Artificial Intelligence Act) | `02024R1689-20260727`; consolidation stamp `02024R1689 - EN - 27.07.2026 - 001.001` on every page; supplied as `EU_AI_Act_consolidated_02024R1689-20260727.pdf`, 151 pp | `1ccd38d1c78482cf` | Arts 2(1)(a)-(c), 2(8), 3(1)-(4), 3(11)-(13), 3(23), 3(49), 4(1), 5(1)(a)-(b), 6(2)-(4), 9(1)-(3), 9(5), 9(9)-(10), 12(1)-(2), 15(5), 16(c)-(e), (i)-(j), 17(1)-(2), 18(1), 25(1)-(2), 25(4), 26(1)-(2), 26(4)-(7), 26(9), 26(11), 27(1), 49(1)-(3), 50(1), 50(5), 71(1)-(2), 71(4), 72(1)-(3), 73(1)-(6), 113; Annex III points 4(a), 4(b), 5(b); Annex VIII Sections A and B |

Read on 18 September 2026; Art 15(5) read on 21 September 2026 for R23 and R24. The file is byte-identical to the one read for Parts 2 and 3 (same hash).

## 1b. Framework source - HELD AND CITED

| # | Source | Version | SHA-256 | Used for |
|---|---|---|---|---|
| 4 | **NIST AI 100-1**, Artificial Intelligence Risk Management Framework (AI RMF 1.0) | January 2023; 48 pp; PDF metadata title `Artificial Intelligence Risk Management Framework (AI RMF 1.0)`, author `National Institute of Standards and Technology`, created 24 January 2023; supplied as `NIST.AI.100-1.pdf` (1,945,980 bytes) | `1607a122bbdb6caf` | The sixteen subcategory texts in the research note's framework mapping (GOVERN 1.5, 1.6, 1.7, 2.1, 6.1; MAP 1.1, 1.5, 4.1, 5.1; MEASURE 1.1, 3.1; MANAGE 1.2, 1.3, 2.4, 3.1, 4.1) and the Executive Summary quotation |

Supplied by the author and held on 21 September 2026. **Gate closed:** each of the sixteen subcategory texts quoted in the research note was checked against the held file on 21 September 2026 and matches word for word; the Core table page references (GOVERN p. 22, MAP p. 26, MEASURE p. 29, MANAGE p. 32, printed numbering) are confirmed. No text in the research note changed as a result.

## 1a. Primary law - NOT RE-HELD

| # | Instrument | Version | Status |
|---|---|---|---|
| 2 | **Regulation (EU) 2026/1744** (Digital Omnibus on AI) | OJ L 2026/1744, 24.7.2026 | Not re-supplied. The consolidation's `M1` markers were relied on; the omnibus text was read for Part 2 from file `21919e56c5d0d4e3` |
| 3 | **Regulation (EU) 2016/679** (GDPR), Arts 30 and 35 | EUR-Lex consolidated text CELEX `02016R0679-20160504` | Read through a text extraction from EUR-Lex on 18 September 2026; not held as a file. Cited as the inventory's analogue only; no GDPR duty is stated as a rule in the artifact body |

## 2. Framework sources - READ, NOT HELD

| # | Source | Version | Status |
|---|---|---|---|
| 5 | **ISO/IEC 42001:2023** Information technology - Artificial intelligence - Management system | ed. 1, December 2023, 51 pp | Not held (paid standard). Title, edition, date and page count confirmed from the ISO catalogue page on 18 September 2026. No clause or Annex A content is asserted anywhere in the artifact |

## 3. Existence and currency checks - WEB, not authority

| # | Item | Checked | Used for |
|---|---|---|---|
| 6 | UK Algorithmic Transparency Recording Standard hub, GOV.UK | 18 September 2026; latest update shown 8 May 2025; mandatory for government departments and arm's-length bodies delivering public or frontline services | Research note only, as a real-world example of a mandated public-sector inventory. Not cited in the artifact body |

## 4. Documents PRODUCED and their inputs

| Document | Version | Status |
|---|---|---|
| `AI_Risk_Register_Walkthrough.md` | 1.0 | EU AI Act positions verified against row 1, 18 Sep 2026; NIST positions verified against row 4, 21 Sep 2026 |
| `AI_Risk_Register_Worked_Example.md` | 1.0 | Tables transcribed from the Excel workbook's sheets; summary counts re-derived 21 Sep 2026 |
| `AI_Risk_Register_Research_Note.md` | 1.0 | Citations with B/M1 markers, corrections, framework mapping, choices |
| `AI_Risk_Register_Source_Register.md` | 1.0 | This document |
| `register/AI_Risk_Register_and_Inventory.xlsx` | 1.1 | The single published record: six synthetic systems and twenty-four synthetic risks, a Read Me glossary, a Summary sheet, both records with colour-coded severity bands, and two blank templates with live score and band formulas. The banding is the worked example's scale (section 2). SHA-256 `8009611e806410d0` (1.0 was built from separate CSV working files, since folded into this one file; 22 Sep 2026: the working-file references removed from the Read Me sheet, the author metadata corrected from a leftover `openpyxl` creator tag to Narendra Karki, and the three rating columns re-stored as numbers rather than text after an independent formula check - every score and band was already evaluating correctly by text coercion, but numbers are what sorting, filtering and a user's own edits need) |
| `downloads/*.docx` | 1.0 | Word exports |

## 5. HELD BUT NOT USED - outside this artifact's scope

| Document | Why held, why not used |
|---|---|
| **UK GDPR, Data Protection Act 2018, Data (Use and Access) Act 2025; ICO guidance** (as supplied to the project) | Held for Part 1. The worked example's group is UK-headquartered, and every UK duty that reaches its systems is pointed to through the Part 1 UK policy rather than restated here. The UK inventory analogue (the record of processing under UK GDPR Art 30) mirrors the EU one and is not separately stated |
| **Part 1 policy sets** - UK, Bahrain, Saudi Arabia, UAE, India, Singapore, Australia, EU | Each inventory row's "other laws" field points to the relevant Part 1 policy rather than restating it. Nothing about those jurisdictions' law is asserted here beyond the pointer. The Saudi set is published within its stated government-data scope |

## 6. NOT HELD - the gaps that shape what this artifact can say

| What is missing | Consequence |
|---|---|
| **ISO/IEC 42001:2023** | Named as the AI management-system standard; nothing about its content is asserted |
| **Commission guidelines under Art 6(5)** on high-risk classification | Classification of S2 and S6 rests on the Annex III text and the profiling rule alone |
| **Art 72(3) post-market monitoring template** (due 2 September 2027) | Post-market monitoring described by its statutory content only |
| **EU consumer law on personalised-pricing disclosure** | R15 is stated as unverified and its mitigation is "legal verification" |
| **Any Commission guidance on Art 4 AI literacy** | The duty is stated from the Article alone |

---

*Part 4 of the AI Governance Series - github.com/NarendraKarki/ai-governance. Educational, not legal advice.*
