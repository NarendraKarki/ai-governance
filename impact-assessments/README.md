# AI Impact Assessments: a fictional insurer as the worked example

**Part 5 of the AI Governance Series.** Version 1.0, see Status.

An AI impact assessment asks one question before a system goes live, and records the answer: who could this harm, and what do we do about it? In the UK and the EU the law asks that question in two forms. The data protection impact assessment (DPIA) is owed today, in both, whenever processing is likely to result in a high risk to people. The fundamental rights impact assessment (FRIA) under the EU AI Act is owed by a much narrower group, from 2 December 2027. This folder helps you work out which applies to each AI system, and then write it.

## What is in this folder

| File | What it is |
|---|---|
| `AI_Impact_Assessment.xlsx` | One Excel workbook. A Read Me explaining both assessments, when each applies, what happens if they are not done, and how they relate to an AI risk register; a Screening sheet that shows which assessment each AI system needs; a DPIA and a FRIA written in full for the worked example; nine risks to people rated before and after the measures, each linked to a risk register ID; a live Summary; and blank templates of the Screening, DPIA, FRIA and Risks sheets |

## The worked example

Northgate Life & Health (fictional) is a UK-headquartered insurer with a subsidiary in Ireland serving EU customers. Its underwriting model, UW-1, reads the application, declared medical history, a GP report obtained with the applicant's consent and, for members of its wellness programme, the step count from a wearable. It returns accept, decline or a premium loading.

The model's design notes classed the step count as lifestyle data. Raw activity data is not health data by itself; used to judge health risk, it reveals information about a person's health status, so here it is data concerning health. The assessment changed the lawful basis, the consent and the retention before any customer saw a price, and put every decline and every loading in front of an underwriter before the customer is told.

The Screening sheet runs the same questions over three more of the insurer's systems, so the workbook shows both outcomes: an assessment that is required, and one that is not, with the reason recorded.

## Legal baseline and verification

- **EU AI Act:** Regulation (EU) 2024/1689 as consolidated on 27 July 2026 (CELEX 02024R1689-20260727), read in the held text on 25 September 2026: Articles 27, 99, 111 and 113, and Annex III point 5.
- **UK GDPR:** the revised text as amended by the Data (Use and Access) Act 2025, read on 25 September 2026: Articles 4(15), 22A to 22C, 35, 58(2)(f) and 83(4), with the Data Protection Act 2018, section 157.
- **EU GDPR:** Regulation (EU) 2016/679, Articles 4(15) and 35, read from the EUR-Lex consolidated text on 25 September 2026. Not yet held as a file; the EU fine figure is therefore not stated anywhere in this folder.

Two positions worth checking in the text itself. The AI Act's own fine list for operators (Article 99(4)) covers deployer duties under Article 26 but not the Article 27 assessment; penalties for a missing FRIA are left to each Member State. And a high-risk system already in service before 2 December 2027 falls under the AI Act only if its design changes significantly after that date (Article 111(2)).

## How to use it

Start with the Read Me sheet. Run every AI system through the Screening Template; for each assessment it marks as required, fill in the DPIA Template or FRIA Template; for each assessment it marks as not required, write the reason. Rate each risk to people in the Risks Template before and after the measures, and link each row to your AI risk register. Part 4 of the series is a worked register.

## Status

Version 1.0. EU AI Act and UK GDPR positions checked against the texts named above. Use it, and tell me what to improve.

---

*Educational material, not legal advice. The insurer, its systems and its people are fictional. Have your DPO or legal counsel review any assessment before it is relied on.*
