# AI Risk Registers and Model Inventories - a retail group as the worked example

**Part 4 of the AI Governance Series.** Version 1.0 - see Status.

A method for building the two records every other AI governance control depends on, built around one idea: an inventory is a record of fact and its test is completeness; a risk register is a record of judgement and its test is honesty; and the moment they are kept as one spreadsheet, the judgement collapses into the fact-keeping and every risk becomes "medium, owner: IT". The worked example is a synthetic retail group with six ordinary AI systems that between them span every tier of the EU AI Act, with the inventory and register supplied as one Excel workbook.

## What is in this folder

| File | What it is |
|---|---|
| `AI_Risk_Register_Walkthrough.md` | The artifact: two records not one, what each is for in law, where inventories fail, where registers fail, an eight-step protocol, the misreadings, and blank records |
| `AI_Risk_Register_Worked_Example.md` | The synthetic retail group: what discovery found, the inventory with role, reach and classification settled, the twenty-four-row register, its summary, the open decisions, and a completed entry |
| `AI_Risk_Register_Research_Note.md` | The working: every legal position with its provision and verification status, the NIST AI RMF mapping, corrections, and the choices made |
| `AI_Risk_Register_Source_Register.md` | What was held, what was read but not held, what was not held, and what therefore is not asserted |
| `register/AI_Risk_Register_and_Inventory.xlsx` | The inventory and the register as one Excel workbook: a Read Me sheet decoding every column, a Summary sheet with live counts, the six systems with every field filled, the twenty-four risks with statement, ratings with justification, decision, owner, mitigation, indicator and triggers, colour-coded severity bands with score and band formulas on the walkthrough's scale, and a blank template sheet for each record with one example row |
| `downloads/` | Word exports |

## Why this artifact exists

Most organisations have a list of AI vendors and a line in the enterprise risk register. Neither is an inventory and neither is a register. The inventory is missing the systems nobody bought (AI features switched on inside software already owned), the ones not called AI, and the ones that are someone's experiment; the register has no risk statements, no words behind its numbers, no named owner and no trigger for looking again. The worked example shows both failures on a portfolio most readers will recognise, and the finding a proper inventory produced: a high-risk system in use for fourteen months that nobody had classified.

It is written for the people who have to build and keep the records - governance, risk, security, privacy, model risk and internal audit - and for the executives who will be asked to sign them.

## Legal baseline and verification

Built on the **consolidated Artificial Intelligence Act of 27 July 2026** - Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744 - read in the primary text. Verification dates: **18 September 2026** (EU AI Act) and **21 September 2026** (NIST AI RMF 1.0). Every legal position in the walkthrough's section 3 is mapped to article and paragraph in the research note with its base-text or omnibus marker. The NIST AI Risk Management Framework is mapped step by step in the research note against the held and hashed primary PDF. ISO/IEC 42001 is named and not held; nothing about its content is asserted.

The reading corrected the draft: an early register entry required a fundamental rights impact assessment for the hiring tool, and the Act confines that duty to public bodies, providers of public services, and credit-scoring and insurance deployers - not a retail group. Corrections are recorded in the research note, not silently fixed.

## How to use it

Run the protocol in order. Step 1 fixes the unit, the fields and the scales before anything is collected. Step 2 is discovery from five sources, and records which source found what. Step 3 fills the inventory and takes role, reach and classification seriously. Steps 4 to 7 build the register: harm first, rated with published scales, decided by a named role, with an indicator. Step 8 is the list of events that re-open both records. Then apply the worked example's section 6 checks to your own records before the ratings are signed off.

## Status

Version 1.0. EU AI Act and NIST AI RMF 1.0 positions verified against the primary texts named and hashed in the source register. Use it, and tell me what to improve.

---

*Educational material, not legal advice. The classification of a real system, and any decision to accept a residual risk to people, should be reviewed by qualified legal counsel before it is relied on.*
