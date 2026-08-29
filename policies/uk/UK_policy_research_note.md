# Research note - UK AI Acceptable Use Policy (v1.0) and Enterprise Annex (v1.0)

Purpose: records the primary-source verification behind each obligation, per the
project rule that article numbers live in the research record, not the artifact
body. Educational, not legal advice.

## Sources verified (revised/consolidated texts held in project files)

- UK GDPR - Regulation (EU) 2016/679 as it forms part of UK law, revised text
  "up to date with all changes known to be in force on or before 21 August 2026"
  (legislation.gov.uk/eur/2016/679).
- Data Protection Act 2018, revised text current to 9 July 2026
  (legislation.gov.uk/ukpga/2018/12).
- Data (Use and Access) Act 2025, c. 18 (legislation.gov.uk/ukpga/2025/18).
- DUAA Commencement No. 6 and Transitional and Saving Provisions Regulations 2026
  (SI 2026/82).
- Equality Act 2010 (legislation.gov.uk/ukpga/2010/15).
- Copyright, Designs and Patents Act 1988 (legislation.gov.uk/ukpga/1988/48).
- ICO: Guidance on AI and data protection; DUAA overview for organisations; draft
  automated decision-making guidance (consultation opened March 2026 - WATCH ITEM,
  final guidance may adjust safeguard expectations).

Verification date: 27 August 2026.

## Obligation -> policy clause -> source

| Obligation (as expressed in artifact) | Clause | Source and article (verified) |
|---|---|---|
| Lawful basis before processing personal data | Policy 6.1 | UK GDPR Art 6 |
| Purpose limitation; no training on customer/staff data without assessment | Policy 6.2 | UK GDPR Art 5(1)(b) |
| Data minimisation | Policy 6.3 | UK GDPR Art 5(1)(c) |
| DPIA before high-risk processing (large-scale, special category, profiling with significant effects, systematic monitoring) | Policy 6.4 | UK GDPR Art 35; ICO DPIA high-risk criteria |
| Individuals' rights not defeated by tool choice | Policy 6.5 | UK GDPR Arts 15-17 |
| Special category data - additional condition | Policy 6.6 | UK GDPR Art 9; DPA 2018 s10 and Sch 1 |
| Transfers outside the UK only with safeguard | Policy 6.7 | UK GDPR Arts 44-49; NOTE: DUAA replaced the adequacy mechanism with the "data protection test" - new Arts 45A-45B confirmed present in revised text |
| Breach notification "within a short statutory period" | Policy 6.9 / 11 | UK GDPR Art 33 - 72 hours to ICO unless unlikely to result in risk (verified: "not later than 72 hours after having become aware"); Art 34 to individuals where high risk |
| Human review of significant decisions BEFORE effect | Policy 8 | STRICTER THAN LAW, DELIBERATELY. UK GDPR Arts 22A-22D (inserted by DUAA, in force): solely-automated significant decisions are now generally permitted; Art 22B restricts them for special category data; Art 22C requires safeguards - inform the individual, enable representations, enable human intervention, enable contest. Policy exceeds this floor by requiring pre-decision meaningful review. Recorded as a conscious design choice. |
| Complaints: accessible means, acknowledge within 30 days, respond and inform outcome without undue delay | Policy 11; Annex A8.1 | DPA 2018 s164A, inserted by DUAA s103 (verified verbatim: "acknowledge receipt of the complaint within the period of 30 days"); s164B (Commissioner notification) is regulation-dependent - not reflected in policy |
| Non-discrimination in AI-informed decisions | Policy 14; Annex A3.1 | Equality Act 2010 (direct/indirect discrimination, ss13, 19; PSED s149 where applicable) |
| IP: no infringing content; confirm ownership/licensing | Policy 12.1 | CDPA 1988 (note: s9(3) computer-generated works provision exists but authorship/ownership of AI output remains unsettled - hence "confirm before commercial use" rather than a stronger claim) |
| Monitoring proportionate with notification | Policy 15 | UK GDPR Arts 5-6; ICO employment practices and monitoring guidance |

## House standards that EXCEED or sit outside UK statute (flagged, kept knowingly)

- Policy 13.1 (tell customers they are interacting with AI): no general UK
  statutory chatbot-disclosure duty. UK bases: misleading omissions under consumer
  protection law (DMCC Act 2024 unfair commercial practices) in some contexts;
  sector rules (e.g. FCA Consumer Duty). Kept as a house standard.
- Policy 17.1 training: no UK statutory AI-literacy duty (that is an EU AI Act
  concept). Drafted without the EU term; kept as good practice.
- Policy 8 pre-decision human review: stricter than Arts 22A-22D (above).

## Annex provisions - basis

- A1 (committee, accountable executive, three lines), A2 (inventory), A3
  (lifecycle), A5 (exceptions), A6 (agentic AI), A7 (assurance): good-practice
  governance controls, not statutory duties; consistent with UK GDPR
  accountability (Art 5(2), Art 24) and with ISO/IEC 42001-style management
  review and NIST AI RMF Govern function. No article numbers claimed in body.
- A4 (supplier terms): UK GDPR Art 28 processor contract duties underpin the DPA
  requirement; the AI-specific terms (no training on org data, model-change
  transparency, exit) are contractual good practice beyond statute.
- A8.1: DPA 2018 s164A (above). A9: sector overlay is a pointer, not a mapping -
  each regulated mapping must be verified separately before publication.

## Drafting decisions incorporated before the v1.0 release

1. Section 11 covers incidents and complaints; the complaints paragraph tracks
   DPA 2018 s164A. Section 16 includes complaints handling.
2. Section 17 avoids "AI literacy" (EU AI Act term) in favour of role-sufficient
   knowledge and skills.

## Watch items

- ICO final ADM guidance (consultation March 2026) - review Policy 8 note when
  published.
- DUAA s164B complaints-volume notification regulations - none in force at
  verification date.
- UK government position on AI and copyright (consultation outcome pending) -
  affects Policy 12.1 research note only.
