# Research note - AI Risk Registers and Model Inventories walkthrough (v1.0)

Purpose: records the primary-source basis for every legal and framework position stated in the walkthrough and the worked example, per the project rule that article numbers live in the research record and not in the artifact body. Educational, not legal advice.

## Verification status

**EU AI Act.** Every provision cited below was read in the consolidated text on **18 September 2026**. The file is the same one hashed for Parts 2 and 3 (`1ccd38d1c78482cf`), consolidation stamp `02024R1689 - EN - 27.07.2026 - 001.001` on every page. Provisions are marked as the consolidation marks them: `B` base text, `M1` inserted, replaced or deleted by the Digital Omnibus (Regulation (EU) 2026/1744).

**NIST AI RMF 1.0.** First read from the primary PDF at nvlpubs.nist.gov on 18 September 2026 through a text extraction, because the file could not be downloaded from either build environment. The PDF was supplied by the author and hash-held on **21 September 2026** (`1607a122bbdb6caf`, source register row 4); every subcategory text quoted below was re-read against the held file on that date and matches word for word. The gate that held the draft banner is closed.

**GDPR.** Article 30 and Article 35 read in the EUR-Lex consolidated text (CELEX 02016R0679-20160504) on 18 September 2026 through a text extraction; not re-held for this artifact. Cited as the analogue for the inventory only.

**ISO/IEC 42001:2023.** Not held (paid standard). Title, edition and date confirmed from the ISO catalogue page. No clause content is asserted anywhere in the artifact.

**UK Algorithmic Transparency Recording Standard.** Existence, mandatory scope and latest update date confirmed from the GOV.UK hub page on 18 September 2026. Cited in this note only, as a real-world example of a mandated public-sector inventory; not cited in the artifact body.

## Sources

| # | Instrument | Version | Status |
|---|---|---|---|
| 1 | **Regulation (EU) 2024/1689 consolidated** (AI Act) | `02024R1689-20260727` | **The operative text.** Held; hash in the source register |
| 2 | **NIST AI 100-1**, Artificial Intelligence Risk Management Framework (AI RMF 1.0), January 2023 | 1.0 | Held; hash in the source register. Verified 21 Sep 2026 |
| 3 | **Regulation (EU) 2016/679** (GDPR), Articles 30 and 35 | consolidated 04.05.2016 | Read from EUR-Lex; not held |
| 4 | **ISO/IEC 42001:2023** Information technology - Artificial intelligence - Management system, ed. 1, December 2023, 51 pp. | ed. 1 | Not held; title only |

## Legal positions, article by article

### Scope and roles (walkthrough section 3, first and second rules; step 3)

| Statement | Source | Status |
|---|---|---|
| The Regulation applies to providers placing on the market or putting into service AI systems in the Union, irrespective of where established | Art 2(1)(a) `B` | `V` |
| ...to deployers of AI systems that have their place of establishment or are located within the Union | Art 2(1)(b) `B` | `V` |
| ...to providers and deployers established or located in a third country where the output produced by the AI system is used in the Union | Art 2(1)(c) `B` | `V` - the reach rule for the worked example's group-run systems |
| Research, testing and development before placing on the market are outside scope; testing in real-world conditions is not | Art 2(8) `B` | `V` - the inventory's "trial" status does not remove a system from the record |
| 'AI system': machine-based, varying autonomy, may exhibit adaptiveness, infers from input how to generate outputs such as predictions, content, recommendations or decisions | Art 3(1) `B` | `V` - the inventory's definition (step 1) |
| 'risk': the combination of the probability of an occurrence of harm and the severity of that harm | Art 3(2) `B` | `V` - the register's two axes |
| 'provider': develops, or has developed, and places on the market or puts into service under its own name or trademark | Art 3(3) `B` | `V` |
| 'deployer': uses an AI system under its authority, other than personal non-professional use | Art 3(4) `B` | `V` |
| 'putting into service': supply for first use directly to the deployer or for own use in the Union for its intended purpose | Art 3(11) `B` | `V` |
| 'intended purpose': the use intended by the provider, including context and conditions, per the instructions for use, promotional materials and technical documentation | Art 3(12) `B` | `V` - the unit of the inventory |
| 'reasonably foreseeable misuse' | Art 3(13) `B` | `V` - step 4 |
| 'substantial modification': a change after placing on the market not foreseen in the initial conformity assessment that affects compliance with Chapter III Section 2 or modifies the intended purpose | Art 3(23) `B` | `V` - R22 |
| A deployer (or distributor, importer, other third party) is considered a provider of a high-risk system, subject to Art 16, where it (a) puts its name or trademark on a high-risk system already on the market, (b) substantially modifies a high-risk system so that it remains high-risk, or (c) modifies the intended purpose of a system not classified as high-risk so that it becomes high-risk | Art 25(1)(a)-(c) `B` | `V` - role drift (R8, R20, R21, R22) |
| The initial provider then ceases to be the provider of that system and must cooperate with the new provider: technical documentation, known limitations and failure modes, targeted technical access - unless it has clearly specified the system is not to be changed into a high-risk one | Art 25(2) `M1` | `V` - basis for the R22 mitigation ("ask the vendor to adopt the score as its own") |
| Provider of a high-risk system and a third party supplying components must specify by written agreement the information, capabilities, technical access and assistance needed for compliance | Art 25(4) `M1` | `V` |

### Classification (section 3, third rule; step 3)

| Statement | Source | Status |
|---|---|---|
| Annex III systems are high-risk | Art 6(2) `B` | `V` |
| Derogation: an Annex III system is not high-risk where it does not pose a significant risk to health, safety or fundamental rights, including by not materially influencing the outcome of decision making, and one of four conditions (narrow procedural task; improving a completed human activity; detecting decision patterns without replacing human assessment; preparatory task) is met | Art 6(3) first and second subparagraphs `B` | `V` |
| Notwithstanding the derogation, an Annex III system is always high-risk where it performs profiling of natural persons | Art 6(3) third subparagraph `B` | `V` - why S2 and S6 cannot use the derogation |
| A provider that concludes an Annex III system is not high-risk must document the assessment before placing on the market or putting into service, is subject to the Art 49(2) registration duty, and must provide the documentation on request | Art 6(4) `B` | `V` - the inventory's derogation fields |
| Recruitment or selection: placing targeted job advertisements, analysing and filtering applications, evaluating candidates | Annex III point 4(a) `B` | `V` - S2 |
| Decisions affecting terms of work-related relationships, promotion or termination, allocation of tasks based on individual behaviour or personal traits or characteristics, monitoring and evaluating performance and behaviour | Annex III point 4(b) `B` | `V` - S6; R8 (promotion) |
| Creditworthiness evaluation or credit score of natural persons, with the exception of AI systems used for the purpose of detecting financial fraud | Annex III point 5(b) `B` | `V` - S3 is outside the listing; R21 would bring S5 inside it |
| Prohibited: subliminal, purposefully manipulative or deceptive techniques materially distorting behaviour and causing or reasonably likely to cause significant harm | Art 5(1)(a) `B` | `V` - S5 screening |
| Prohibited: exploiting vulnerabilities of a person or group due to age, disability or a specific social or economic situation, materially distorting behaviour and causing or reasonably likely to cause significant harm | Art 5(1)(b) `B` | `V` - R16. The register does not conclude the feature meets the test; it records that it could approach it and that the feature is disabled pending assessment |
| Chapters I and II (incl. Art 4 AI literacy and Art 5 prohibitions) apply from 2 February 2025, with two further prohibitions (5(1)(ba), (bb)) from 2 December 2026 | Art 113(a) `M1` | `V` |
| Chapter III Sections 1-3 apply from 2 December 2027 for Annex III high-risk systems and 2 August 2028 for Annex I | Art 113(c) `M1` | `V` |
| The Regulation generally, including Chapter IV (Art 50), applies from 2 August 2026 | Art 113 second paragraph `B` | `V` |

### AI literacy and transparency (section 3; S1 rows)

| Statement | Source | Status |
|---|---|---|
| Providers and deployers must take measures to support the AI literacy of staff and others operating or using AI systems on their behalf; no guaranteed level required | Art 4(1) `M1` | `V` - the "applies today" duty on every inventory row |
| Providers must design systems intended to interact directly with natural persons so that those persons are informed they are interacting with an AI system, unless obvious | Art 50(1) `B` | `V` - S1. Provider design duty; the deployer's exposure is in removing or hiding the notice (R3) |
| Information is provided clearly and distinguishably at the latest at the first interaction | Art 50(5) `B` | `V` |

### Provider duties: risk management, quality management, documentation (section 3, fourth to fifth rules; steps 4-8)

| Statement | Source | Status |
|---|---|---|
| A risk management system shall be established, implemented, documented and maintained for high-risk systems | Art 9(1) `B` | `V` |
| Continuous iterative process over the whole lifecycle with regular systematic review; steps: identify and analyse known and reasonably foreseeable risks to health, safety or fundamental rights under intended purpose; estimate and evaluate risks under intended purpose and reasonably foreseeable misuse; evaluate other risks from post-market monitoring data; adopt appropriate and targeted measures | Art 9(2)(a)-(d) `B` | `V` - steps 4-6 and 8 |
| Only risks that may reasonably be mitigated or eliminated through design, development or adequate technical information | Art 9(3) `B` | `V` |
| High-risk systems shall be resilient against attempts by unauthorised third parties to alter their use, outputs or performance by exploiting system vulnerabilities; technical solutions to address AI-specific vulnerabilities include, where appropriate, measures against attacks manipulating the training data set (data poisoning), pre-trained components (model poisoning), inputs designed to cause the model to make a mistake (adversarial examples or model evasion), confidentiality attacks or model flaws | Art 15(5) `B` | `V` - the Act's own naming of the attack types. A provider duty for high-risk systems; cited here because it settles that these attacks are within AI risk management, not outside it. R23 and R24 sit on a transparency-tier and an unlisted system, so the provision is not a duty on those rows; the rows are there because the walkthrough's step 4 is harm-first, whatever the tier |
| Residual risk per hazard and overall residual risk judged acceptable; elimination or reduction as far as technically feasible, mitigation and control measures for the rest, information and training to deployers | Art 9(5) `B` | `V` - step 6 |
| Consideration of adverse impact on persons under 18 and other vulnerable groups | Art 9(9) `B` | `V` |
| Providers subject to other Union-law risk management processes may combine the two | Art 9(10) `B` | `V` |
| Provider obligations include a quality management system (Art 17), keeping documentation (Art 18), keeping logs (Art 19), registration (Art 49(1)), corrective action (Art 20) | Art 16(c)-(e), (i), (j) `B` | `V` |
| Quality management system in written policies, procedures and instructions including: compliance strategy incl. management of modifications; the Art 9 risk management system; post-market monitoring per Art 72; serious-incident reporting per Art 73; record-keeping systems and procedures; resource management; an accountability framework setting out the responsibilities of management and other staff | Art 17(1)(a), (g), (h), (i), (k), (l), (m) `B` | `V` - the register's owner column and review cycle |
| Implementation proportionate to the size of the provider, in particular SMEs and SMCs, without lowering the level of protection | Art 17(2) `M1` | `V` |
| Provider keeps technical documentation, QMS documentation, notified-body documents and the declaration of conformity at the disposal of authorities for 10 years after placing on the market or putting into service | Art 18(1) `B` | `V` |
| High-risk systems must technically allow automatic recording of events (logs) over the lifetime; logging enables identifying situations presenting a risk, post-market monitoring, and deployer monitoring under Art 26(5) | Art 12(1)-(2) `B` | `V` |

### Deployer duties (section 3, sixth rule; S2 and S6 rows)

| Statement | Source | Status |
|---|---|---|
| Use in accordance with the instructions for use | Art 26(1) `B` | `V` - R7, R18 |
| Assign human oversight to natural persons with the necessary competence, training and authority and support | Art 26(2) `B` | `V` - R18 |
| Ensure input data under the deployer's control is relevant and sufficiently representative | Art 26(4) `B` | `V` |
| Monitor operation on the basis of the instructions; inform the provider or distributor and the market surveillance authority and suspend use where the system may present a risk; inform the provider immediately of a serious incident | Art 26(5) first subparagraph `B` | `V` |
| Keep automatically generated logs under the deployer's control for at least six months | Art 26(6) `B` | `V` |
| Employers inform workers' representatives and affected workers before putting a high-risk system into service or using it at the workplace | Art 26(7) `B` | `V` - R18 |
| Deployers of Annex III systems that make or assist decisions about natural persons inform them that they are subject to the system | Art 26(11) `B` | `V` - R9 |
| Deployers use the Art 13 information to carry out a GDPR Art 35 DPIA where applicable | Art 26(9) `B` | `V` |
| Fundamental rights impact assessment is required of deployers that are public bodies or private entities providing public services, and deployers of Annex III 5(b) and (c) systems | Art 27(1) `B` | `V` - **not** required of the worked example's group for S2 or S6 (retail; points 4(a) and 4(b)). Stated in the walkthrough's misreadings by omission; recorded here explicitly |

### Serious incidents (section 3, seventh rule; the severity scale)

| Statement | Source | Status |
|---|---|---|
| 'serious incident': incident or malfunctioning leading directly or indirectly to (a) death or serious harm to health, (b) serious and irreversible disruption of critical infrastructure, (c) infringement of obligations under Union law intended to protect fundamental rights, (d) serious harm to property or the environment | Art 3(49) `B` | `V` - the worked example's severity level 4 to people |
| Providers report serious incidents to the market surveillance authority of the Member State where the incident occurred; immediately after establishing a causal link or reasonable likelihood, and not later than 15 days after awareness; two days for widespread infringement or 3(49)(b); ten days for a death; an incomplete initial report may be followed by a complete one | Art 73(1)-(5) `B` | `V` |
| Provider investigates, risk-assesses and takes corrective action; does not alter the system in a way affecting later evaluation before informing the authorities | Art 73(6) `B` | `V` |

### Registration and the EU database (section 3, eighth rule; the inventory fields)

| Statement | Source | Status |
|---|---|---|
| Before placing on the market or putting into service an Annex III high-risk system (other than point 2), the provider registers itself and the system in the EU database | Art 49(1) `B` | `V` - R7, R18 ask the vendor for its registration |
| A provider concluding under Art 6(3) that a system is not high-risk registers itself and the system | Art 49(2) `B` | `V` |
| Deployers that are public authorities or Union bodies register their use | Art 49(3) `B` | `V` - not the worked example's group |
| The EU database contains Annex VIII information; Sections A and B entered by the provider; publicly accessible and machine-readable except the restricted sections | Art 71(1), 71(2), 71(4) `B` | `V` - an earlier draft of this note marked 71(1) as `M1`; on re-reading, the marker preceding Article 71 is `B` (correction 6 below) |
| Annex VIII Section A: provider identity and contacts; authorised representative; trade name and unambiguous reference; description of intended purpose and components and functions supported; basic and concise description of the information used (data, inputs) and operating logic; status (on the market / in service / no longer / recalled); certificate details; Member States where available; declaration of conformity; electronic instructions for use; optional URL | Annex VIII Section A points 1-13 `B` | `V` - the minimum provider-side inventory record; the walkthrough's inventory fields cover each |
| Annex VIII Section B (Art 49(2) registrations): identity, trade name and reference, intended purpose, the Art 6(3) condition relied on, status; two points deleted by M1 | Annex VIII Section B points 1-6, 8 `B`; deletions `M1` | `V` |

### Post-market monitoring (step 8)

| Statement | Source | Status |
|---|---|---|
| Providers establish and document a post-market monitoring system proportionate to the technology and the risks; it actively and systematically collects, documents and analyses performance data throughout the lifetime | Art 72(1)-(2) `B` | `V` |
| Based on a post-market monitoring plan that is part of the Annex IV technical documentation; Commission guidance and template by 2 September 2027 | Art 72(3) `M1` | `V` - watch item carried from Part 3 |

### GDPR analogue (section 3, ninth rule)

| Statement | Source | Status |
|---|---|---|
| Record of processing activities contains: controller identity and DPO; purposes; categories of data subjects and personal data; categories of recipients including in third countries; third-country transfers; envisaged erasure time limits where possible; general description of security measures where possible | GDPR Art 30(1)(a)-(g) | `V` (read from EUR-Lex; not held) - the inventory row's data field links to this record rather than duplicating it |
| Derogation for enterprises under 250 persons unless processing is likely to result in a risk, is not occasional, or includes special categories | GDPR Art 30(5) | `V` (as above) |
| DPIA where processing is likely to result in a high risk to rights and freedoms; required in particular for systematic and extensive automated evaluation with legal or similarly significant effects, large-scale special-category processing, and large-scale systematic monitoring of public areas | GDPR Art 35(1), 35(3)(a)-(c) | `V` (as above) - referenced from register rows, not restated |

## Framework mapping - NIST AI RMF 1.0 (voluntary)

The framework is "intended to be voluntary, rights-preserving, non-sector-specific, and use-case agnostic" (Executive Summary). The Core tables begin at page 22 (GOVERN), 26 (MAP), 29 (MEASURE) and 32 (MANAGE). Subcategory texts verified against the held PDF on 21 September 2026; ellipses mark where a longer subcategory is quoted in part.

| Walkthrough step | Subcategory | Text |
|---|---|---|
| Step 1 (scales) | MAP 1.5 | Organizational risk tolerances are determined and documented |
| Step 1 (fields), section 5 (owner) | GOVERN 2.1 | Roles and responsibilities and lines of communication related to mapping, measuring, and managing AI risks are documented and are clear to individuals and teams... |
| Step 2 (discover) | GOVERN 1.6 | Mechanisms are in place to inventory AI systems and are resourced according to organizational risk priorities |
| Step 3 (purpose, reach, law) | MAP 1.1 | Intended purposes, potentially beneficial uses, context-specific laws, norms and expectations, and prospective settings in which the AI system will be deployed are understood and documented... |
| Step 3 (role; vendor systems) | GOVERN 6.1 | Policies and procedures are in place that address AI risks associated with third-party entities, including risks of infringement of a third-party's intellectual property or other rights |
| Step 4 (harm first) | MAP 5.1 | Likelihood and magnitude of each identified impact (both potentially beneficial and harmful) based on expected use, past uses of AI systems in similar contexts... |
| Step 4 (vendor components) | MAP 4.1 | Approaches for mapping AI technology and legal risks of its components - including the use of third-party data or software - are in place, followed, and documented... |
| Step 5 (rate) | MANAGE 1.2 | Treatment of documented AI risks is prioritized based on impact, likelihood, and available resources or methods |
| Step 5 (what is not measured) | MEASURE 1.1 | ...The risks or trustworthiness characteristics that will not - or cannot - be measured are properly documented |
| Step 6 (decide) | MANAGE 1.3 | Responses to the AI risks deemed high priority, as identified by the MAP function, are developed, planned, and documented. Risk response options can include mitigating, transferring, avoiding, or accepting |
| Step 6 (avoid; stop) | MANAGE 2.4 | Mechanisms are in place and applied, and responsibilities are assigned and understood, to supersede, disengage, or deactivate AI systems that demonstrate performance or outcomes inconsistent with intended use |
| Step 7 (indicators) | MEASURE 3.1 | Approaches, personnel, and documentation are in place to regularly identify and track existing, unanticipated, and emergent AI risks based on factors such as intended and actual performance in deployed contexts |
| Step 8 (triggers; vendor change) | MANAGE 3.1 | AI risks and benefits from third-party resources are regularly monitored, and risk controls are applied and documented |
| Step 8 (monitoring, decommissioning, incidents, change) | MANAGE 4.1 | Post-deployment AI system monitoring plans are implemented, including mechanisms for capturing and evaluating input from users and other relevant AI actors, appeal and override, decommissioning, incident response, recovery, and change management |
| Step 8 (retire) | GOVERN 1.7 | Processes and procedures are in place for decommissioning and phasing out AI systems safely and in a manner that does not increase risks or decrease the organization's trustworthiness |
| Section 5 (register is a control) | GOVERN 1.5 | Ongoing monitoring and periodic review of the risk management process and its outcomes are planned and organizational roles and responsibilities clearly defined... |

## Corrections and findings recorded openly

1. **The fundamental rights impact assessment does not reach the worked example.** An early draft of the register gave S2 a mitigation "complete the FRIA before December 2027". Article 27(1) confines the duty to public bodies, private entities providing public services, and deployers of Annex III 5(b) and (c) systems (credit scoring; life and health insurance). A retail group deploying recruitment and workforce systems is none of those. The mitigation was removed; the data protection impact assessment under GDPR Art 35 remains, referenced from the row.
2. **The fraud model is not caught by the credit-scoring listing, and the register says why.** Annex III 5(b) excludes AI used for the purpose of detecting financial fraud in terms. The inventory's basis field quotes the exclusion so that a reader does not have to take the "none" on trust.
3. **Article 26(5) financial-institution wording does not apply.** The worked example was changed from a bank (Part 3) to a retail group at the author's direction, which removes the financial-services deeming provisions in Arts 17(4), 18(3), 26(5) and 26(6) from the analysis. They are not cited in the artifact body.
4. **Consumer-law disclosure of personalised pricing is not verified.** R15 rests on a duty that this artifact has not read in the primary text. The register row and the inventory say so in terms, and the mitigation is "legal verification" rather than an asserted rule. Recorded as a watch item and as the reason the EU site's personalised pricing is switched off in the example.
5. **The prohibited-practice screening of S5 is a screening, not a conclusion.** Article 5(1)(b) requires exploitation of a vulnerability due to age, disability or a specific social or economic situation, material distortion of behaviour, and significant harm. The register records that the urgency-prompt feature could approach the test and that it is disabled; it does not find that the test is met.
6. **Marker corrections from the verification pass.** Article 71(1) was first marked `M1` from memory of the omnibus's database changes; the consolidation shows `B` immediately before Article 71 and the deletions the omnibus made are in Annex VIII Section B (points 7 and 9), not in Article 71(1). Article 12(1)-(2) was first marked with a mixed `B`/`M1` note; both paragraphs sit under a `B` marker. Both corrected in the tables above.

## Choices recorded openly

1. **Four-level scales.** One workable choice among several. The requirement stated in the walkthrough is that each level is defined in words and that the top severity level to people is anchored to the Art 3(49) outcomes.
2. **Severity to people and to the organisation kept separate.** This is the artifact's central design choice and the reason the worked example's ordering reverses between the two columns.
3. **One row per risk, not per system.** The alternative - a system-level score - is what produces "everything is medium".
4. **The non-EU jurisdictions are pointed to, not restated.** Each inventory row's "other laws" field references the Part 1 policy for the jurisdiction - the UK, Bahrain, Saudi Arabia, the UAE, India, Singapore and Australia. Nothing about those countries' law is asserted in this artifact beyond that pointer. The Saudi pointer is to a set published within its stated government-data scope; the private-sector position is that set's own open gate.
5. **The footprint was re-based on 21 September 2026, and the legal analysis did not move.** The example was first drafted as a Bahrain-headquartered group with stores in six Gulf states (BH, SA, AE, KW, QA, OM) and the same Dutch subsidiary. It was re-based to a UK-headquartered group with stores in the UK, three Gulf states, India, Singapore and Australia so that the portfolio reads as a global retailer's rather than a regional one. Every EU AI Act position is unchanged, because the reach rule for a deployer established outside the Union (Art 2(1)(c)) does not depend on which third country it is established in; the two high-risk classifications, the role analysis and all twenty-two risk statements then on the register are the same. What changed: the country codes in the inventory, the "other laws" pointers, R2's justification (eight jurisdictions, not seven), and the group's size. A side effect: every country now listed has a Part 1 policy to point to, which closes the earlier gap where Kuwait and Qatar were listed with no pointer.
6. **Two AI-specific security rows were added on 21 September 2026 (R23, R24).** The first register had no adversarial-attack risk, although the walkthrough's step 4 lists attacks among the causes and the video's opening frames the security test as necessary but not sufficient. A reader would have looked for the prompt-injection row and not found it. R23 (prompt injection on the customer assistant) and R24 (threshold probing of the fraud model) were added, each written as a harm statement with the vendor's clean red-team result recorded as an existing control. Both rate medium to people. The register's counts moved from twenty-two to twenty-four; nothing else changed.
7. **The synthetic vendors are named** (Helix Assist, TalentRank, Lumen Offers, ShiftWise) so that the rows read as a real register would. Each is marked synthetic in the workbook. If any coincides with a real product the coincidence is unintended and the name will be changed.

## Limitations

1. **One statute stated in full.** The EU AI Act only. Data protection, consumer and employment law are pointed to per jurisdiction.
2. **Commission guidelines not held**, including the Art 6(5) classification guidelines, any guidance on Art 4 literacy, and the Art 72(3) post-market monitoring template.
3. **Harmonised standards not held.**
4. **Synthetic organisation and portfolio.**
5. **No provision cited here has been reviewed by qualified counsel.**

## Watch items

- Commission guidelines under Art 6(5) with practical examples of high-risk and not-high-risk uses (Part 2 watch item; bears on S2 and S6).
- The Art 72(3) post-market monitoring template, due 2 September 2027.
- Delegated acts under Art 7 amending Annex III.
- The AI Office's voluntary model contract terms under Art 25(4) for provider / third-party agreements.
- EU consumer-law disclosure of personalised pricing (R15) - to be verified in the primary text.
