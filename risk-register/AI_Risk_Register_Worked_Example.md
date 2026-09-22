# Worked example - a synthetic retail group builds its inventory and register

**Companion to the Part 4 walkthrough.** Version 1.0. The inventory and register below are the same records as the Excel workbook `AI_Risk_Register_and_Inventory.xlsx`'s AI Inventory and AI Risk Register sheets; section 6 summarises them.

Educational material, not legal advice. The group, its systems, its vendors and its people are synthetic. Vendor names are invented and marked as such.

---

## 1. The organisation

**Marsa Retail Group (synthetic).** A retail and e-commerce group headquartered in London, with stores in the UK, Bahrain, Saudi Arabia, the UAE, India, Singapore and Australia, and a subsidiary established in the Netherlands that runs the EU e-commerce site and a small number of stores. About 9,000 employees; 60% of store staff part-time. Group functions (HR, digital, data, marketing, supply chain) are run from headquarters and serve every entity, including the EU subsidiary.

The group has a risk function, a privacy officer, an information security team and, since mid-2026, an AI governance lead reporting to the Chief Risk Officer. Before this exercise it had no AI inventory. The risk function's enterprise register had one line: "AI - emerging technology risk - medium - owner: IT".

## 2. Step 1 - the unit, the fields and the scales

**Unit.** An AI system in a use, applying the EU AI Act's definition of an AI system. One row per intended purpose.

**Fields.** As in the walkthrough's section 9 template; the workbook's columns follow it.

**Scales.** Four levels each, defined in words. Published with the register.

| Level | Severity to people | Severity to the organisation | Likelihood |
|---|---|---|---|
| 1 | Inconvenience; reversible on request | Internal cost only; no external notice | Not expected in the system's life |
| 2 | Loss of time or money that is recoverable; a decision the person can contest and reverse | Regulatory query, complaints pattern, local press | Could occur once in the system's life |
| 3 | A decision with lasting effect on access to work, credit, goods or services; disclosure of personal data; distress | Enforcement action, material loss, loss of a contract or market | Expected within a year |
| 4 | A serious-incident outcome: death or serious harm to health; serious and irreversible disruption of critical infrastructure; infringement of Union-law obligations protecting fundamental rights; serious harm to property or the environment | Statutory-maximum penalty band; loss of licence to operate in a market; criminal exposure | Occurring now, or expected within months |

Residual band = severity x likelihood: 1-3 low; 4-6 medium; 8-9 high; 12-16 critical. Reported separately for people and for the organisation. A risk at severity 4 to people cannot be accepted below the Chief Risk Officer.

## 3. Step 2 - what discovery found

| Source | Found | Note |
|---|---|---|
| Procurement and contracts | S1 customer service assistant; S2 candidate screening tool | The only two systems anyone would have named as "our AI" |
| SaaS console sweep and vendor release notes | S6 shift optimiser | Enabled by a workforce-suite update in July 2025; used by every store manager since; never reviewed |
| Identity provider and expenses | Nothing new | Three individual trial subscriptions to writing assistants, cancelled and recorded as out of scope |
| Data platform scheduled jobs | S3 payment fraud detection; S4 demand forecasting | Both in production for over two years |
| Function-head questionnaire | S5 personalisation and promotions engine | Marketing contract, not in the procurement AI list; "no human in the loop" on prices |

Six systems. Four found by a source other than procurement.

## 4. Step 3 - the inventory

Condensed. The full rows, including data used, owners and verification, are in the workbook's AI Inventory sheet.

| ID | System | Role | Used / output used | People affected | EU AI Act tier and basis | Duties bind | Found by |
|---|---|---|---|---|---|---|---|
| S1 | Customer service assistant | deployer | GB, BH, SA, AE, IN, SG, AU, NL | Customers of the group | transparency - Art 50(1): intended to interact directly with natural persons; provider design duty; deployer must not remove the disclosure | 2 Aug 2026 (in force) | procurement |
| S2 | Candidate screening tool | deployer | GB, BH, SA, AE, IN, SG, AU, NL | Job applicants, including applicants to the EU subsidiary | high-risk - Annex III point 4(a): recruitment or selection, analysing and filtering applications and evaluating candidates. Derogation considered and unavailable: the system profiles natural persons | 2 Dec 2027 | procurement |
| S3 | Payment fraud detection | both | GB, SA, AE, SG, AU, NL | Customers of the e-commerce sites | none - not listed (fraud detection is not an Annex III use; the credit-scoring point expressly excludes it). Data protection profiling and automated-decision rules apply - Part 1 | AI literacy only (2 Feb 2025) | data platform |
| S4 | Demand forecasting | both | GB, BH, SA, AE, IN, SG, AU, NL | None - no decisions about natural persons | none | AI literacy only | data platform |
| S5 | Personalisation and promotions engine | deployer | GB, SA, AE, SG, AU, NL | Customers of the e-commerce sites | none - not listed. Screened against the prohibited practices: the urgency-prompt feature could approach the vulnerability-exploitation prohibition; disabled pending assessment (R16). Data protection profiling rules and consumer-law disclosure of personalised pricing (not verified for this artifact) - Part 1 | AI literacy only | function questionnaire |
| S6 | Shift optimiser | deployer | GB, BH, SA, AE, IN, SG, AU, NL | Store employees, including employees of the EU subsidiary | high-risk for the EU subsidiary's use - Annex III point 4(b): decisions affecting terms of work-related relationships and allocation of tasks based on individual behaviour or characteristics. Derogation unavailable: profiling. Unlisted in the non-EU jurisdictions - Part 1 | 2 Dec 2027 | SaaS console sweep |

**Three things the inventory settled that the group had assumed differently.**

*Reach.* The group's first position was that the EU AI Act reached only the Dutch subsidiary's own systems - which it thought were none, because every system is run from London. The Act reaches a deployer wherever established if the system's output is used in the Union. The CV screener filters applications to the Dutch subsidiary; the shift optimiser publishes the Dutch stores' rotas; the assistant answers Dutch customers. All three are in scope for those uses.

*Role.* The group is a deployer of four systems and provider-and-deployer of two. It had been about to become the provider of a third: the promotion-ranking feature HR had asked the vendor to build on the group's own criteria (R8). And the buy-now-pay-later plan for 2027 would, if built on the promotions engine, turn a deployer of an unlisted system into the provider of a high-risk one (R21).

*Classification.* Two high-risk systems, not none. Neither can use the derogation, because both profile natural persons. The duties bind on 2 December 2027, and the register's mitigation dates are set from that date backwards.

## 5. Steps 4 to 7 - the register

Twenty-four risks. P = severity to people, O = severity to the organisation, L = likelihood; residual band is to people. Existing controls, justifications, mitigations, indicators, thresholds and triggers are in the workbook's AI Risk Register sheet.

| Risk | System | If ... then ... | Harm to whom | P | O | L | Residual (people) | Decision | Decided by |
|---|---|---|---|---|---|---|---|---|---|
| R1 | S1 | If the assistant states a returns or refund rule that is not the group's policy, then customers act on it and are refused at the store or online | financial loss to the customer - recoverable on complaint | 2 | 2 | 3 | medium | mitigate | Head of Customer Operations |
| R2 | S1 | If customers paste card numbers or full order and address details into the chat, then transcripts containing that data are retained by the vendor beyond the contracted purpose and period | disclosure of customers' personal and payment data | 3 | 3 | 2 | medium | mitigate | Head of Customer Operations |
| R3 | S1 | If a website or app redesign removes or hides the 'you are talking to an AI assistant' notice, then customers are not told they are interacting with an AI system | customers cannot calibrate trust in what they are told; transparency-duty breach | 2 | 3 | 2 | medium | mitigate | Head of Customer Operations |
| R4 | S1 | If the vendor changes the underlying model without notice, then answer quality and tone change and the group's tests no longer describe the system in use | customers receive worse or different answers; the group's records describe a system that no longer exists | 2 | 2 | 3 | medium | mitigate | Head of Customer Operations |
| R20 | S1 | If the digital team extends the assistant to approve or refuse refunds itself rather than draft for an agent, then the group has changed the system's intended purpose and may have become its provider for that use | customers subject to automated refund decisions nobody assessed; provider duties inherited without notice | 2 | 2 | 2 | medium | mitigate | Head of Customer Operations |
| R23 | S1 | If a customer message, or a web page the assistant retrieves to answer it, contains instructions that override the assistant's own instructions, then the assistant discloses another customer's order or delivery details, or states a refund commitment the group did not authorise | disclosure of other customers' personal data; commitments the group must honour or retract | 3 | 3 | 2 | medium | mitigate | Head of Customer Operations |
| R5 | S2 | If the tool's training data reflects the historical gender balance of store and sales roles, then women applying for sales roles are ranked lower than men with equivalent qualifications | qualified candidates rejected without a human seeing the application; potential unlawful discrimination | 4 | 3 | 3 | critical | mitigate | Group HR Director |
| R6 | S2 | If applications below the rank threshold are rejected automatically with no recruiter review, then rejection decisions are solely automated | candidates cannot contest a decision no person made; automated-decision rights engaged for EU applicants | 4 | 3 | 4 | critical | mitigate | Group HR Director |
| R7 | S2 | If the instructions for use and the provider's EU database registration are not obtained before the high-risk duties bind, then the group uses a high-risk system without the instructions the deployer duties are framed around | candidates subject to a system used outside its assessed conditions; deployer in breach from 2 Dec 2027 | 2 | 3 | 3 | medium | mitigate | Group HR Director |
| R8 | S2 | If HR enables the vendor's proposed promotion-ranking feature configured on the group's own criteria, then the group becomes the provider of a high-risk system (promotion decisions) that no one has assessed | employees ranked for promotion by an unassessed system; provider duties inherited without a quality management system | 3 | 3 | 2 | medium | avoid | Group HR Director |
| R9 | S2 | If EU applicants are not told that an AI system is used to filter their application, then applicants are unaware and cannot exercise their rights | candidates uninformed; deployer information duty unmet from 2 Dec 2027 and data-protection transparency unmet now | 2 | 2 | 3 | medium | mitigate | Group HR Director |
| R10 | S3 | If the model's false-positive rate is higher for first-time customers and for deliveries to certain postcode bands, then legitimate orders from those customers are held for review more often | delay and refusal for legitimate customers concentrated in identifiable groups | 2 | 2 | 3 | medium | mitigate | Head of Payments |
| R11 | S3 | If a new fraud pattern emerges that the training data does not contain, then fraud losses rise until the model is retrained | financial loss to the group | 1 | 3 | 3 | low | accept | Head of Payments |
| R12 | S3 | If a held order is cancelled automatically after 48 hours without a person reviewing it, then the cancellation is a solely automated decision | EU customers lose an order with no human involvement and no route to contest | 2 | 2 | 2 | medium | mitigate | Head of Payments |
| R24 | S3 | If an organised fraud group probes the model with many small orders to learn which features and thresholds trigger a hold, then fraudulent orders are shaped to score just below the threshold and are released automatically | fraud loss and chargebacks to the group; legitimate customers held more often when the threshold is tightened in response | 2 | 3 | 3 | medium | mitigate | Head of Payments |
| R13 | S4 | If the model over- or under-forecasts for a product category, then stock-outs or overstock at store level | cost to the group; no decision about any natural person | 1 | 2 | 3 | low | accept | Head of Supply Chain |
| R14 | S5 | If offers and prices vary on features that proxy protected characteristics (postcode band; device type; name-derived signals), then customers in some groups systematically see higher prices or fewer offers | indirect discrimination in price; loss to those customers over time | 3 | 3 | 3 | high | mitigate | Chief Marketing Officer |
| R15 | S5 | If customers are not told that the price they see is personalised, then customers cannot compare or contest a personalised price | customers misled about the basis of the price; disclosure duties under consumer law may be engaged (not verified for this artifact) | 2 | 3 | 3 | medium | mitigate | Chief Marketing Officer |
| R16 | S5 | If the engine's urgency-prompt feature targets customers showing behavioural signals (late-night sessions; repeated returns to a basket), then customers in a vulnerable situation are pushed to purchase | manipulation of a person in a specific social or economic situation causing them financial harm - could approach a prohibited practice | 2 | 4 | 2 | medium | avoid | Chief Marketing Officer |
| R21 | S5 | If marketing configures the engine to score customers for eligibility for the group's buy-now-pay-later offer, then the group's own configuration turns the engine into a creditworthiness evaluation of natural persons - a listed high-risk use the vendor has not assessed | customers subject to credit-type decisions by an unassessed system; group becomes provider of a high-risk system | 3 | 3 | 2 | medium | mitigate | Chief Marketing Officer |
| R17 | S6 | If the performance score used for allocation is sales per hour unadjusted for shift timing and section, then staff who work quieter shifts or sections - disproportionately part-time staff with caring responsibilities - score lower and are allocated fewer and worse shifts | loss of income and lasting effect on work terms concentrated in a group defined by a protected characteristic; potential unlawful indirect discrimination | 4 | 3 | 3 | critical | mitigate | Group Retail Operations Director |
| R18 | S6 | If the optimiser is used in EU stores without instructions for use on file, without assigned human oversight, and without informing workers' representatives, then from 2 Dec 2027 the EU subsidiary is a deployer of a high-risk system in breach of the deployer duties | employees subject to a high-risk system without the safeguards the law attaches to it | 3 | 3 | 4 | critical | mitigate | Group Retail Operations Director |
| R19 | S6 | If the vendor update that enabled the optimiser also enabled attendance and performance monitoring features that were never reviewed, then employees are monitored and evaluated by features the group has not assessed or told them about | undisclosed monitoring of employees; data protection and employment-law duties unmet | 3 | 3 | 3 | high | mitigate | Group Retail Operations Director |
| R22 | S6 | If the group builds its own performance score and feeds it into the optimiser in place of the vendor's, then the group has substantially modified a high-risk system and becomes its provider for that modification | employees allocated by a score the vendor never assessed; provider duties inherited | 3 | 3 | 3 | high | mitigate | Group Retail Operations Director |

**Reading the register.**

*Where the top ratings sit.* Three risks at severity 4 to people (R5, R6, R17) and all on the two high-risk systems. That is not a coincidence: Annex III lists the uses it lists because the harms are of this kind. Four risks are critical on residual band to people; two of them (R6, R18) are critical because the likelihood is 4 - the condition is met today, not feared.

*What the risk function's first draft had.* One line, "medium", owned by IT. Its second draft, made before the walkthrough's scales were adopted, rated by contract value: the assistant (largest contract) highest, the shift optimiser (a free feature) and the screening tool (a small SaaS fee) lowest. The severity-to-people column reverses that ordering entirely.

*The two risks every vendor row carries.* Role drift (R8, R20, R21, R22) and silent change (R4, R19). Between them they account for six of the twenty-four rows, and R19 is the one that turned out to be already happening.

*The two attack rows.* R23 (prompt injection on the assistant) and R24 (threshold probing of the fraud model) are the register's AI-specific security risks, and they show how a vulnerability enters a harm-first register: as the cause in a statement whose consequence is rated for people and for the organisation, not as a category. Both systems had been security-tested - the assistant's vendor red-teamed it for injection and poisoning in August 2026 and found nothing - and that test result is recorded as an existing control that lowers likelihood, not as a reason to leave the row out. The same weaknesses can also sit on the information security register as technical findings; the AI register is where the consequence to people is rated and owned, and the two rows cross-reference.

*The forecaster.* One row, severity 1 to people, accepted by its owner in a sentence. The register is not improved by inventing a harm to people for a system that makes no decisions about any.

*Decisions.* Twenty mitigate, two accept (R11 and R13, both with severity 1 to people), two avoid (R8, closed once the feature request was withdrawn; R16, held at accepted while the feature stays disabled). Every mitigation has an owner and a date; every risk above low has an indicator with a threshold and a named watcher.

## 6. The register in summary

| Residual band to people (severity to people x likelihood) | Risks |
|---|---|
| Critical (12-16) | 4 |
| High (8-9) | 3 |
| Medium (4-6) | 15 |
| Low (1-3) | 2 |

| System | EU AI Act tier | Role | Risks | Highest severity to people | Open mitigations |
|---|---|---|---|---|---|
| S1 Customer service assistant | transparency | deployer | 6 | 3 | 6 |
| S2 Candidate screening tool | high-risk | deployer | 5 | 4 | 4 |
| S3 Payment fraud detection | none | both | 4 | 2 | 3 |
| S4 Demand forecasting | none | both | 1 | 1 | 0 |
| S5 Personalisation and promotions engine | none | deployer | 4 | 3 | 3 |
| S6 Shift optimiser | high-risk | deployer | 4 | 4 | 4 |

The same counts are calculated live on the Summary sheet of the Excel workbook. Before the register was accepted it was checked against the walkthrough's own rules: every inventory field that decides a duty is filled; every high-risk system records that the derogation was considered; no owner is a department; every risk is a statement with a cause and an event; every rating has a one-line justification; no severity-4 risk to people is simply accepted; every risk above low has an indicator; every deployer row has a role-drift risk and a vendor-update trigger; and a register where most ratings are 2 is flagged as "everything is medium". It passed on all of them.

## 7. Step 8 - the triggers, and the two decisions still open

The register's `review_triggers` column lists, per risk, the events that re-open it. Across the register the triggers fall into the walkthrough's seven kinds: new use requested (R8, R20, R21); vendor model or feature update, or a vendor response (R1, R4, R5, R6, R14, R16, R19, R22, R23); change of countries (none yet - the group's expansion plans would add one); population change (R5 - new role family); law or guidance change (R7, R9, R15, R18); incident, complaint pattern or indicator threshold (R1, R2, R11, R23, R24); and the calendar backstop (quarterly for S2 and S6; annually for S4).

Two decisions are recorded as open rather than made:

1. **Whether to keep the shift optimiser in EU stores at all** (R18). The vendor has been asked for instructions for use and its registration timetable. If neither exists by mid-2027, the group's options are to switch the feature off in the Netherlands or to take on the provider's duties itself, and the register says the decision is the Group Retail Operations Director's, to be recorded by 30 June 2027.
2. **Where the redesigned performance score runs** (R22). The obvious place is inside the optimiser, and that is the place that makes the group a provider. The register records the question and who answers it, and does not pre-empt them.

## 8. The completed inventory entry for S6

```
AI SYSTEM INVENTORY - ENTRY
Identifier: S6                       Name: Shift optimiser              Status: [ ] trial [x] in use [ ] retired
What it does (one sentence): Allocates shifts to store staff using availability and individual performance
  scores inside the workforce management suite.
Output and who acts on it: Published rota; store managers may edit before publishing but rarely do.
Role: [ ] provider [x] deployer [ ] both     Basis: Bought as part of the workforce management suite; feature
  enabled by vendor update 2025-07; not reviewed at the time. Group has not modified it (see R22).
Supplier and contract ref: ShiftWise (synthetic); CON-2023-058 (AI feature not in the contract description)
Technical reference: ShiftWise WFM 11.2 - Optimise module
Countries where used: GB, BH, SA, AE, IN, SG, AU, NL  Countries where output is used: the same
People it makes or shapes decisions about: Store employees, including employees of the EU subsidiary
Data used: Availability, contracted hours, sales-per-hour and attendance scores (ROP-033 - to be updated)
Classification - EU AI Act:  [ ] prohibited [x] high-risk (Annex III point 4(b)) [ ] transparency [ ] none
  Derogation considered: [x] yes   Claimed: [ ] yes [x] no - profiling of natural persons; derogation unavailable
  Duties bind from: 2 Dec 2027       Applies-today duties: [x] AI literacy [ ] transparency
Classification - other laws: GB, BH, SA, AE, IN, SG, AU - employee data protection per Part 1 policies; NL -
  employee data protection and works council information per Part 1 EU set
Business owner: Group Retail Operations Director       Technical owner: Workforce Systems Manager
Found by: SaaS console sweep                            Last verified: 2026-09-14 / AI governance lead
```

## 9. Using the templates

The Excel workbook carries two blank templates as sheets - Inventory Template and Risk Register Template - the column headers and one example row each, with the score and band formulas and the drop-down lists already in place. Apply the section 6 checks to your own records before the ratings are signed off - a blank required field, a severity-4 risk to people marked "accept", or "IT" as an owner are the three failures that matter most.

---

*Part 4 of the AI Governance Series - github.com/NarendraKarki/ai-governance. Educational, not legal advice.*
