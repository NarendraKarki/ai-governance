# Research note - Bias and Fairness Testing walkthrough (v1.0)

Purpose: records the primary-source basis for every legal position stated in the walkthrough and the worked example, and the method literature behind the three-pan framing, per the project rule that article numbers live in the research record and not in the artifact body. Educational, not legal advice.

## Verification status

All AI Act citations below were read in the consolidated text on **10 September 2026**. The file is the same one hashed for Part 2 (`1ccd38d1c78482cf`), consolidation stamp `02024R1689 - EN - 27.07.2026 - 001.001` on every page. Provisions are marked as the consolidation marks them: `B` for base text, `M1` for text inserted, replaced or deleted by the Digital Omnibus. Three positions (Annex III 5(b), Art 6(3) third subparagraph, Art 113(c)(i)) were read again rather than carried forward from Part 2.

The reading corrected the artifact in one substantive respect - the special-category permission has moved and widened - and one minor one (a sub-point number). Both are recorded under "Corrections and findings" below and were applied to the walkthrough before the draft banner lifted.

## Sources

| # | Instrument | Version | Status |
|---|---|---|---|
| 1 | **Regulation (EU) 2024/1689 consolidated** (AI Act) | `02024R1689-20260727`, stamp `02024R1689 - EN - 27.07.2026 - 001.001` | **The operative text.** Held; hash in the source register. Incorporates amendment M1 |
| 2 | **Regulation (EU) 2026/1744** (Digital Omnibus on AI) | OJ L 2026/1744, 24.7.2026 | Not re-held for this artifact. The M1 markers are taken from the consolidation itself, which marks every amended passage; the omnibus was read for Part 2 |

## Legal positions, article by article

### Classification (walkthrough section 7, first rule)

| Statement | Source | Status |
|---|---|---|
| AI for evaluating creditworthiness of natural persons or establishing their credit score is high-risk; exception for AI used to detect financial fraud | Annex III point 5(b) `B` | `V` |
| The derogation from high-risk status is unavailable where the system profiles natural persons - credit scoring does | Art 6(3), third subparagraph `B` | `V` |
| Annex III high-risk duties apply from 2 December 2027 | Art 113(c)(i) `M1` | `V` |

### Data governance and bias examination (section 7, second and third rules; protocol steps 1, 4-6)

Commencement note: Art 4a sits in Chapter I, which applies under Art 113(a) `M1`; as an omnibus insertion it has applied since the omnibus entered into force (Part 2 register: OJ 24 July 2026, in force). The Art 10 duties on providers bind with the rest of Chapter III Section 2 from 2 December 2027 for Annex III systems.

| Statement | Source | Status |
|---|---|---|
| High-risk systems that train models on data are developed on data sets meeting the quality criteria in Art 10(2)-(4) and Art 4a(1); data sets subject to governance practices appropriate for the intended purpose | Art 10(1) `M1` (now cross-refers to Art 4a(1)); Art 10(2) chapeau `B` | `V` |
| Those practices include examination in view of possible biases likely to affect health and safety, negatively impact fundamental rights, or lead to discrimination prohibited under Union law, especially where outputs influence inputs for future operations | Art 10(2)(f) `B` | `V` |
| ...and appropriate measures to detect, prevent and mitigate biases identified under point (f) | Art 10(2)(g) `B` | `V` |
| Data sets relevant, sufficiently representative, as far as possible free of errors and complete; appropriate statistical properties including as regards the persons or groups the system is intended to be used on | Art 10(3) `B` | `V` - the representation test in step 4 |
| Data sets take account of the geographical, contextual, behavioural or functional setting of intended use | Art 10(4) `B` | `V` - the population definition in step 1 |
| **Art 10(5) is deleted** (M1 deletion marker stands in its place). The permission is re-enacted as **Art 4a** in Chapter I: providers of high-risk systems may exceptionally process special categories of personal data to the extent strictly necessary for bias detection and correction under Art 10(2)(f)-(g), in addition to GDPR / Reg 2018/1725 / Directive 2016/680, on **six** cumulative conditions - (a) not achievable with other data incl. synthetic or anonymised; (b) technical limits on re-use, state-of-the-art security and privacy-preserving measures incl. pseudonymisation; (c) measures securing the data incl. strict controls and documentation of access, authorised persons only, confidentiality obligations; (d) not transmitted, transferred or otherwise accessed by other parties; (e) deleted once the bias is corrected or at end of retention, whichever first; (f) records of processing state why strictly necessary and why other data would not do | Art 10(5) `M1` (deleted); Art 4a(1)(a)-(f) `M1` | `V` - step 1's lawful-basis rule, rewritten. Condition (c) is new relative to the base text |
| **Deployers** of high-risk systems, and providers and deployers of **other** AI systems and models, may exceptionally process special categories of data where strictly necessary for bias detection and correction (same bias description as Art 10(2)(f)) and all Art 4a(1) conditions are applied; "this paragraph does not create any obligation to conduct such bias detection and correction" | Art 4a(2)(a)-(b) and closing sentence `M1` | `V` - the widening. The walkthrough's step 1 and section 7 now state it; the duty to test remains provider-side under Art 10(2)(f)-(g) |

### Risk management (section 7, fourth rule; steps 3 and 7)

| Statement | Source | Status |
|---|---|---|
| Risk management system: continuous iterative process; identify and analyse known and reasonably foreseeable risks to health, safety or fundamental rights; adopt appropriate and targeted measures | Art 9(1)-(2) `B` | `V` |
| Residual risk per hazard and overall judged acceptable | Art 9(5) `B` | `V` |
| Testing to identify the most appropriate risk management measures; at any time in development and in any event before placing on the market; against prior defined metrics and probabilistic thresholds appropriate to the intended purpose | Art 9(6), 9(8) `B` | `V` - the basis for fixing the criterion and tolerances before results (step 3) |
| Consideration of whether the system is likely to adversely impact persons under 18 and, as appropriate, other vulnerable groups | Art 9(9) `B` | `V` - intersections in step 5 |

### Technical documentation (section 7, fifth rule; step 7)

| Statement | Source | Status |
|---|---|---|
| Technical documentation drawn up before placing on the market and kept up to date; at minimum the Annex IV elements; SMEs and SMCs may use a simplified Commission form | Art 11(1) first subparagraph `B`; second subparagraph `M1` | `V` |
| Annex IV: datasheets describing training methodologies and data sets - provenance, scope, main characteristics, how obtained and selected, labelling procedures, cleaning methodologies; validation and testing procedures and data, metrics used to measure accuracy, robustness and compliance with Section 2 requirements "as well as potentially discriminatory impacts"; test logs and test reports dated and signed by the responsible persons; appropriateness of the performance metrics | Annex IV points 2(d), 2(g), 4 `B` | `V` - the wording is "potentially discriminatory impacts"; step 7's signed record is what 2(g) asks for |

### Provider transparency and human oversight (remedy table, step 6)

| Statement | Source | Status |
|---|---|---|
| Instructions for use to include, when appropriate, performance regarding specific persons or groups of persons on which the system is intended to be used | Art 13(3)(b)(v) `B` | `V` - the basis for the deployer receiving per-group performance figures. Corrected from (iv) |
| Human oversight by design; persons assigned enabled to remain aware of the tendency to over-rely on the output (automation bias), in particular for systems providing recommendations for decisions by natural persons | Art 14(1), 14(4)(b) `B` | `V` - the referral-band remedy and its own bias monitoring |

### Deployer duties (section 7, sixth and seventh rules; step 8)

| Statement | Source | Status |
|---|---|---|
| Deployers monitor operation on the basis of the instructions for use; for financial institutions subject to Union financial services law on internal governance, the monitoring duty is deemed fulfilled by complying with those rules | Art 26(5), both subparagraphs `B` | `V` |
| Deployers keep automatically generated logs under their control for a period appropriate to the intended purpose, at least six months; financial institutions keep them within their financial-services documentation | Art 26(6) `B` | `V` |
| Fundamental rights impact assessment before first use by deployers that are public bodies or private entities providing public services, **and by deployers of high-risk systems under Annex III points 5(b) and (c)** - i.e. credit scoring and life/health insurance pricing; content includes the categories of persons likely affected, the specific risks of harm, and human oversight measures | Art 27(1)(a)-(f) `B` | `V` - **unchanged by the omnibus.** The credit-scoring limb stands. Added: results notified to the market surveillance authority with the filled template, Art 27(3) `B`; DPIA cross-referencing, Art 27(4) `M1`; AI Office template and automated tool, Art 27(5) `M1` |
| Provider post-market monitoring system collecting performance data throughout the lifetime; based on a plan that forms part of the Annex IV technical documentation; Commission guidance and template by 2 September 2027 | Art 72(1)-(2) `B`; 72(3) `M1` | `V` - step 8's provider-side counterpart |

## Method literature - the three pans and the impossibility result

These are not law. They are the established results the walkthrough's section 2 rests on, cited so a reader can check the claim that the three criteria cannot be levelled together when base rates differ.

| Claim | Source |
|---|---|
| Calibration within groups, equal false positive rates and equal false negative rates cannot all hold when the base rates differ between groups (except for a perfect predictor) | Chouldechova, A. (2017), "Fair prediction with disparate impact: a study of bias in recidivism prediction instruments", *Big Data* 5(2), 153-163 |
| The same incompatibility for calibration against balance for the positive and negative classes, in the risk-score setting | Kleinberg, J., Mullainathan, S. and Raghavan, M. (2016), "Inherent trade-offs in the fair determination of risk scores", arXiv:1609.05807 |
| Equalised odds and equal opportunity (equal FNR) as criteria, and the threshold-adjustment method the worked example's rounds 2 and 3 use | Hardt, M., Price, E. and Srebro, N. (2016), "Equality of opportunity in supervised learning", *Advances in Neural Information Processing Systems* 29 |
| The four-fifths (80%) selection-rate rule is US employment guidance, not EU law | Uniform Guidelines on Employee Selection Procedures (1978), 29 CFR 1607.4(D) - cited only to locate the rule's origin; the walkthrough's point is that it is *not* an EU legal test |

The worked example's "pan 1 / pan 2 / pan 3" correspond to demographic parity (selection rate), equalised odds (FPR and FNR), and calibration / predictive parity respectively. The plain-English names are used in the artifact deliberately; the technical names are here for readers who want to go to the literature.

## Corrections and findings recorded openly

1. **The special-category permission moved and widened.** The draft of this artifact cited Article 10(5) for the permission to process special categories of personal data for bias detection. In the consolidated text Article 10(5) is **deleted** - the M1 deletion marker stands where it was - and the permission is re-enacted as a new **Article 4a** in Chapter I. Three things changed: the conditions are six, not five (a new condition (c) requires documented, strict access controls and confidentiality obligations); Article 10(1) now cross-refers to Article 4a(1) as a data-quality criterion; and Article 4a(2) extends the permission beyond providers of high-risk systems to **deployers of high-risk systems and to providers and deployers of any other AI system**, while stating in terms that it creates no obligation to conduct bias detection. The walkthrough's step 1, section 7 and section 6 were rewritten before publication. This is the single most useful thing the reading produced: a lender *deploying* a vendor's scoring model, and an organisation testing a system that is not high-risk at all, now have an express basis for holding the data the test needs - and no new duty to run it.
2. **Article 27(1) is unchanged.** The draft flagged the fundamental rights impact assessment limb for credit-scoring deployers as the most consequential open reading. It carries the `B` marker; the omnibus touched Article 27 only to add DPIA cross-referencing (27(4)) and an AI Office template (27(5)). The flag was removed from the walkthrough body.
3. **Sub-point number.** The per-group performance item in the instructions for use is Article 13(3)(b)(v), not (iv) as drafted. (iv) is the explainability-capabilities item.
4. **Article 26(5)-(6) financial-institution provisions.** Not in the draft; found on reading. For a bank, the deployer monitoring and log-keeping duties are deemed met through Union financial-services governance rules and documentation. Added to the walkthrough's section 7 because the worked example is a bank.
5. **Article 72(3) is amended.** The post-market monitoring plan is now expressly part of the Annex IV technical documentation, with Commission guidance and a template due by 2 September 2027. Added as a watch item.

## Choices recorded openly

1. **Three pans, not the full taxonomy.** The literature names more than twenty fairness criteria. The walkthrough uses three because they are the ones that conflict in the way that matters for a decision-maker, and every other common criterion is a variant of one of them. This is a simplification, stated as one.
2. **Positive class = predicted default = refuse.** So "false positive" means a good payer refused. Fairness libraries often take the opposite convention (positive = approved), which flips the labels on the error rates. The worked example spells out each rate in words for that reason.
3. **The synthetic bank's primary criterion is calibration.** This is a defensible choice for credit and it is not the only one; the walkthrough's step 3 gives the alternatives and the worked example records the reasoning as a lender might. It is not a recommendation that every lender choose calibration.
4. **Group-specific thresholds are described as "likely to be unlawful in most jurisdictions".** This is a statement about equality law generally, which is out of scope, and is deliberately hedged. The worked example has the bank's own legal advice rule them out rather than the walkthrough asserting a legal conclusion.
5. **Round 1's pan 3 is "nearly level", not "level".** The approved default rate gap is 3.4 points. The video and the walkthrough say "nearly" and the tolerance in the completed record is 3 points, so the bank's own record marks pan 3 as within tolerance only by the band-level calibration evidence, not by the approved-default figure alone. Stated rather than rounded away.
6. **A group label was added to the video and withdrawn.** A cut of the Part 3 video labelled group A as men and group B as women, so that a general audience had a concrete referent - "two groups" with no content is the one thing a lay viewer cannot hold. It was withdrawn on review. The dataset's group variable is unlabelled and the disparity is generated from debt ratio, credit history and income only, so the label carried no finding; but the figures attached to it implied that women default at roughly twice the rate of men, which is not what the literature or the regulatory cases show. The documented pattern runs the other way - women receiving smaller limits and more refusals despite equal or better repayment. The published video names sex once, as the check people commonly run, and attaches it to no figure. Recorded here rather than quietly reversed, because a reader comparing cuts should be able to see why.
7. **Label-bias model threshold.** Set to the same *overall* approval rate as round 1 (79.5%), not the same threshold value, so that the comparison isolates the effect of the label rather than of a shifted operating point.

## Limitations

1. **The omnibus regulation itself was not re-held for this artifact.** The M1 markers are taken from the consolidation, which marks every amended passage; the omnibus text was read for Part 2. A reader who wants to see the amending instrument rather than its result should obtain Regulation (EU) 2026/1744.
2. **One jurisdiction.** Equality law and data protection law are out of scope and decide the lawfulness of several remedies. The Part 1 policy sets cover the data protection interplay per jurisdiction.
3. **Harmonised standards not held.** The technical standards being developed for high-risk AI (including on bias) are not held and not cited; when adopted, they will set what "appropriate" measures under the data governance duty look like in practice.
4. **Commission guidelines not held**, including any guidance on the data governance duty or on the fundamental rights impact assessment template.
5. **Synthetic data; two groups; one characteristic; binary decision.** Stated in the walkthrough's section 9.
6. **No provision cited here has been reviewed by qualified counsel.**

## Watch items

- The AI Office template and automated tool under Article 27(5) `M1` for the fundamental rights impact assessment.
- Commission guidance and template on the post-market monitoring plan under Article 72(3) `M1`, due by 2 September 2027.
- The Commission's simplified technical documentation form for SMEs and SMCs under Article 11(1) `M1`.
- Harmonised standards under Article 40 covering data governance and bias (CEN-CENELEC JTC 21 work programme).
- Delegated acts under Article 7 amending Annex III - the credit-scoring listing is the hinge of this artifact.
- The Article 6(5) guidelines (already a Part 2 watch item), which bear on whether a credit-adjacent system can claim the derogation.
- Any further amendment to Article 113 (the December 2027 date).
