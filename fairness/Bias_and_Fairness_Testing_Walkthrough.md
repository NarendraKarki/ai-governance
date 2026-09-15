# Bias and Fairness Testing - a walkthrough, with credit scoring as the worked example

**Part 3 of the AI Governance Series.** Version 1.0. Verified against the consolidated AI Act of 27 July 2026 on 10 September 2026 (research note).

Educational material, not legal advice. The worked example uses a synthetic dataset; nothing in it describes a real lender.

---

## 1. What this is

A method for testing an AI system that makes or shapes decisions about people for bias, written for the people who have to do the testing and sign the record: model risk, governance, privacy, security and audit teams. It is not a statistics course and it is not a fairness library manual. It is the sequence of decisions a testing team has to make, the order they have to make them in, and what has to be written down at each step so that the result can be defended a year later.

The worked example is a retail credit scoring model. Credit is the right example for three reasons: the harm of a wrong decision is concrete and asymmetric (a good payer refused loses access to credit; a defaulter approved costs the lender money); the base rate of the thing being predicted genuinely differs between groups in most real portfolios, which is exactly the condition under which fairness tests disagree with each other; and, under the EU AI Act, credit scoring of natural persons is a listed high-risk use with an explicit bias-examination duty attached, so the record this walkthrough produces is the record the law will ask for.

Everything numerical in this walkthrough is reproducible. The dataset is generated, the model is trained and every table is printed by one script in this folder. Change the seed and the numbers move by a point or two; the shape of the result does not.

## 2. Why "fair" is not one test

Every fairness slide shows a pair of scales. Two pans, one beam: put the two groups in the pans, level the beam, and the model is fair. Used as a test, the picture hides the real problem, because there are at least three different things the pans could be weighing, and they do not level together.

**Pan 1 - are both groups approved as often?** The selection rate. If 87% of one group is approved and 59% of the other, the gap is 28 points and the ratio is 0.67. This is the test most people mean by "bias" and the one most easily read off a dashboard. It says nothing about whether the decisions were right.

**Pan 2 - are the model's mistakes spread evenly?** Two error rates matter, and they point in opposite directions. The false positive rate here is the share of good payers the model refuses: harm to the applicant. The false negative rate is the share of eventual defaulters the model approves: harm to the lender, and in the long run to the other customers who pay for it. A model can have equal approval rates and still refuse good payers in one group three times as often as in the other.

**Pan 3 - does a decision carry the same risk in both groups?** Two related questions. Does a score of 20% mean a 20% chance of default whichever group the applicant is in (calibration)? And among the people approved, do both groups go on to default at the same rate (predictive parity)? If the answer is no, the model is treating identical scores as meaning different things, or the threshold is doing so.

Each pan is a legitimate reading of "fair". Each has a group it protects and a group it exposes. And when the two groups genuinely default at different rates - which is the normal case, not the exception - it is arithmetically impossible to level all three at once. This is not a limitation of any particular model. It is a property of the numbers, proven in the fairness literature in 2016 and 2017 and restated in the research note. A threshold that equalises approval rates must approve higher-risk applicants from the higher-base-rate group, so the risk among approved applicants diverges. A threshold that equalises the risk among approved applicants must approve fewer of the higher-base-rate group. There is no setting that escapes this.

The consequence for a testing team is the whole point of this walkthrough: **the job is not to find the fair model. The job is to decide which pan to level, write down why, and measure the other two.** A test report that says "the model passed fairness testing" without saying which criterion it passed and which it did not is not a test report.

## 3. Where bias enters

Bias is not one defect and testing for it is not one test. Five entry points, each with its own test in section 4:

1. **The label.** The model learns what it is shown. If the training label is "was approved under the old process" rather than "went on to repay", the model learns the old process, including whatever the old process did by hand. This is the single most common way a "group-blind" model reproduces a group-aware history. The worked example builds one of these deliberately.
2. **Representation.** If one group is 28% of applicants but 8% of the data the model was trained on, the model is better at predicting the majority and its errors concentrate in the minority. Thin-file applicants - short credit histories - are systematically under-represented in the outcomes data because they were refused more often in the past, so their repayment was never observed.
3. **Proxies.** Removing the protected characteristic from the inputs does not remove it from the model if other inputs carry it. Postcode, first name, employer, device type, and time of application all carry group information. A proxy is only a problem if the model uses it to do something the characteristic itself would not lawfully be allowed to do; the test in section 4 separates a proxy that is present from a proxy that is doing the work.
4. **Aggregation.** A single model fitted across the whole population can be well calibrated on average and wrong for every sub-group, if the relationship between the inputs and the outcome differs between groups. A short credit history means something different for a 22-year-old and a 45-year-old recent immigrant.
5. **Deployment.** The population drifts, the threshold is moved for commercial reasons, the model's refusals shape next year's training data (the refused never get to repay), and human overrides cluster in one group. Bias that was absent at launch appears in production. Testing is a control that runs, not a gate that is passed.

## 4. The testing protocol

Eight steps, in order. The order matters: steps 1-3 are decisions that must be recorded **before** any result is seen, because a criterion chosen after the results are in is a criterion chosen to pass.

### Step 1 - fix the decision, the population, and the characteristics

Write down, in one paragraph each: the decision the system makes or informs (approve, refuse, refer, price); the population it is applied to (new applicants for unsecured personal credit up to a stated amount; existing customers are a different population); the protected characteristics to be tested (as a minimum, those the applicable equality and data protection law names, and any the organisation's own policy adds); and the **lawful basis for holding those characteristics for testing**. The last is not a formality. Testing for bias against a characteristic the organisation does not hold requires either collecting it for that purpose, inferring it (with the accuracy and consent problems inference brings), or testing on proxies. Under the EU AI Act as amended, special categories of personal data may be processed, exceptionally and to the extent strictly necessary, for bias detection and correction - by providers of high-risk systems, and also by deployers of high-risk systems and by providers and deployers of other AI systems - subject to six cumulative conditions: other data including synthetic or anonymised data would not do; technical limits on re-use and state-of-the-art security and privacy-preserving measures including pseudonymisation; strict, documented access controls; no transmission to or access by other parties; deletion once the bias is corrected or the retention period ends, whichever is first; and a record of why the processing was strictly necessary and why other data would not achieve it. The permission creates no duty to test; the duty to examine data for bias sits separately on providers of high-risk systems. The research note records the provisions; the walkthrough treats the conditions as rules to be met and evidenced, not options.

### Step 2 - fix the comparison

For each characteristic: which group is the reference (usually the largest, or the group the law treats as the comparator), and what is the unit of comparison (individual applications, or applicants - a person who applies three times is three units under one and one under the other). Fix the minimum cell size below which a result is reported as "insufficient data" rather than as a number; the worked example uses 100, and shows why.

### Step 3 - choose which pan to level, and say why

Choose the primary fairness criterion for this decision, from the three in section 2 or a defensible variant, **and record the reasoning before running anything**. The reasoning has to address the harm: which mistake matters most to whom. For credit, the usual candidates are:

- Level pan 3 (calibration / predictive parity) as primary, because a lender's central obligation is that a stated risk is a true risk, and because a miscalibrated score cannot be explained honestly to a refused applicant. Then measure pans 1 and 2 and set tolerances for them.
- Level pan 2 on the applicant-harm side (equal rate of refusing good payers) as primary, because the harm of a wrong refusal falls on an individual who did nothing wrong, while the harm of a wrong approval is spread across the lender's book. Then measure pans 1 and 3.
- Level pan 1 (equal approval rates) as primary. This is rarely the right primary criterion for credit, because it requires approving applicants at materially different risk levels in different groups, which is itself a form of unequal treatment and is likely to be unlawful in most jurisdictions. It is the right thing to **measure**, because a large gap is the signal that something in the data or the model needs explaining.

Record the choice, the reasoning, and the tolerances for the other two pans. The record is signed by someone with authority to accept the trade-off - it is a business and legal decision, not a data science one.

### Step 4 - test the data before the model

Three tests on the training data, run before any model result is looked at:

- **Representation.** For each characteristic: the share of each group in the training data against its share of the applicant population, and its share of the *labelled* data (the rows with an observed outcome). A group that is 28% of applicants and 14% of labelled outcomes has had half its outcomes filtered out by past refusals.
- **Label quality.** What the label is. If it is an observed outcome (repaid or defaulted within 24 months), how it was observed and for whom. If it is a past decision, stop: the model is being trained to imitate the past process, and the past process must itself be tested first.
- **Proxy strength.** Train a simple model to predict the protected characteristic from the system's input features, holding the characteristic out, and report the AUC. 0.5 means the features carry no group information; anything above about 0.7 means the features can substantially reconstruct the group. This does not by itself mean the model is biased - it means "we removed the characteristic" is not a defence. Repeat with each candidate proxy removed to see which features carry the information.

### Step 5 - test the model's outcomes

At the operating threshold, for each characteristic, for each group against the reference, report all three pans:

| Pan | Measures | Report |
|---|---|---|
| 1 | Approval rate | rate per group; gap in points; ratio to reference |
| 2 | Good payers refused (FPR); defaulters approved (FNR) | rate per group; gap in points |
| 3 | Calibration by score band; default rate among approved | predicted vs actual per band per group; approved default rate per group; gap |

Every rate carries a confidence interval or a bootstrap range. A 3-point gap on 8,000 applicants is a finding; a 3-point gap on 90 applicants is noise, and the record must say which. Then repeat at the **intersections** the organisation has decided to test (group by age band, group by sex) and report cells below the minimum size as insufficient.

### Step 6 - trial the remedies, and record what each one costs

Bias findings have a short list of remedies, and each changes a different pan:

| Remedy | What it changes | What it costs | Note |
|---|---|---|---|
| Remove a proxy feature | Removes bias the proxy was *carrying*; changes nothing if the disparity comes from real risk differences | Predictive power, if the feature had any | The test in step 4 says whether it will help before it is tried |
| Relabel or reweight the training data | Corrects label bias and representation bias at source | Requires observed outcomes for the under-represented group, which may not exist | The only remedy that fixes the cause rather than the symptom |
| Change the threshold for everyone | Moves all groups along the same trade-off | Approval volume or default rate | Does not change the gaps much |
| Group-specific thresholds | Levels pan 1 or pan 2 exactly | Tips pan 3; treats identical scores differently by group, which may itself be unlawful direct discrimination | Must be checked against equality law before use, not after |
| Constrained retraining (fairness-aware objective) | Levels a chosen pan during training | Same trade-off as thresholds, less visibly | The invisibility is the risk: the trade-off must still be recorded |
| Referral band with human review | Routes borderline cases in the exposed group to a person | Cost and speed; human reviewers have their own biases, which must be tested too | Often the right first response while a data fix is built |

Run each candidate remedy on the held-out data, report the three pans for each, and put the table in the record. The decision-maker from step 3 chooses, and the choice is recorded with the table.

### Step 7 - record and sign

The record for one test cycle contains, at minimum: the steps 1-3 decisions and the date they were fixed; the data tests; the outcome tables with intervals; the intersection tables; the remedy trial; the remedy chosen and by whom; the residual gaps accepted and the tolerances they sit within; the retest triggers (step 8); and the versions of the data, the model, the threshold and the script that produced every number. Section 8 is a blank record. Under the EU AI Act the examination of the data for bias, and the measures taken, form part of the technical documentation a high-risk system must keep; the record is that documentation.

### Step 8 - monitor, and retest on triggers

Fairness testing is a running control. Set out: which of the pan measures are monitored in production and how often (monthly approval-rate gaps by group are cheap; error rates need observed outcomes and lag by the outcome window); the tolerance that triggers a retest; and the events that trigger one regardless - a threshold change, a retrain, a change in the applicant population or product, a change in the law, and a pattern in complaints or overrides. The deployer of a high-risk system has a duty to monitor its operation and to keep the logs; the monitoring here is how that duty is met for bias.

## 5. The worked example - a synthetic bank

The full tables are in the companion `Bias_and_Fairness_Testing_Worked_Example.md` and are printed by `fairness_testing_credit.py`. The shape of the findings:

**The setup.** 20,000 synthetic applicants for unsecured personal credit, two groups (A, 72%; B, 28%). Group B has, on average, a shorter credit history, a lower income and a higher debt-to-income ratio. Default is generated from those real risk drivers only: group membership is never a term in the outcome. The bank trains a logistic regression on age, income, history length, debt-to-income, missed payments and a five-band postcode indicator, with group withheld from the model, and refuses at a predicted default probability of 20% or more. The model's AUC on 8,000 held-out applicants is 0.81.

**Round 1 - one threshold for everyone.** Approval rates 87% (A) against 59% (B): a 28-point gap, ratio 0.67, bootstrap interval 26 to 31 points. Good payers refused: 9% (A) against 32% (B). Default rate among those approved: 6.0% against 9.4%. Calibration by score band is close in both groups. So pan 3 sits nearly level and pans 1 and 2 tip hard - with a model that never saw the group.

**Is the proxy doing the work?** The postcode band recovers group membership with an AUC of 0.86 (0.78 without it): a strong proxy is present. Removing it changes the approval gap from 28.4 to 28.8 points and the model's AUC not at all. The proxy is present but not doing the work; the disparity comes from the real risk drivers differing between groups. "We removed the proxy" would have fixed nothing and the test says so before anyone tries it.

**The label-bias model.** The same bank, training instead on the decisions of its old manual process, which penalised postcode bands 4 and 5 by hand, with the threshold set to the same overall approval rate. The approval gap widens to 37 points and good payers in group B are refused at 39%. Now remove the postcode band: the gap falls back to 29 points. Here the proxy *was* doing the work - it was carrying the old process's hand-applied penalty into the new model - and removing it removes exactly that, and nothing else. The residual 29 points is the same real-risk disparity as round 1. Two models, the same proxy, opposite answers to "should we remove it"; the test in step 4 is what tells them apart.

**Round 2 - level pan 1.** Set the threshold for group B so that approval rates match (87% and 87%). Pan 2 levels as well: good payers refused at 9% and 7%. Pan 3 tips: default among approved applicants is 6.0% (A) against 15.9% (B), because group B applicants are now approved up to a predicted risk of 41% while group A applicants are refused at 20%. Two applicants with identical scores now get different decisions. Levelling pan 2 instead (equal refusal of good payers) gives almost the same picture: approval gap 3 points, approved default 6.0% against 15.0%.

**The arithmetic.** Base rates 9.7% against 21.1%. No threshold, single or per-group, levels all three pans on this data, and none can. Round 1 shows what a well-built, group-blind model does when base rates differ: it is calibrated and it is unequal. Round 2 shows what levelling the inequality costs. The bank's decision is which of those it can defend.

**Intersections and cell sizes.** Group B under-25s: 176 applicants in the test set, approval 61%, interval 54% to 69%. The point estimate is 3 points higher than group B over-25s; the interval says the difference is not established. Reported as such.

**What the synthetic bank records.** Primary criterion: calibration (pan 3), because a stated risk must be a true risk and because per-group thresholds would treat identical scores differently. Tolerance on pan 3: 3 points on approved default rate. Pans 1 and 2 measured and reported; the 28-point approval gap and 23-point refused-good-payer gap are outside any tolerance the bank would set and trigger the remedy trial. Remedy chosen: a referral band (predicted risk 20% to 30%) routed to human review with its own bias monitoring, while a thin-file data programme is built to observe outcomes for short-history applicants - the representation fix that addresses the cause. Group-specific thresholds rejected on equality-law grounds. Retest quarterly and on every trigger in step 8.

## 6. Common misreadings

**"We do not collect the characteristic, so the model cannot be biased."** The model in round 1 never saw the group and produced a 28-point gap. Not holding the characteristic prevents *testing*, not bias, and the EU AI Act as amended expressly permits providers and deployers - of high-risk and other systems alike - to process special categories of data for bias detection under strict conditions, precisely because the alternative is not knowing.

**"We removed the proxy, so it is fixed."** Sometimes. The step 4 proxy test and a removal trial say whether the proxy was doing the work. In the worked example it was in one model and not in the other.

**"The four-fifths rule is the law."** The 80% selection-rate ratio is a US regulatory rule of thumb from employment guidance. It is a useful screening heuristic and it is not an EU legal test; nothing in the EU AI Act or in EU equality law sets a numerical threshold. Report the ratio, and do not report it as a pass mark.

**"The model is calibrated, so it is fair."** Calibration is one pan. A calibrated model on data with different base rates will refuse good payers unequally, as round 1 shows. Calibration is a good primary criterion for credit; it is not the end of the test.

**"We tested it at launch."** Deployment bias (section 3, item 5) appears after launch by construction. A single test is a snapshot; the control is the monitoring and the retest triggers.

**"The fairness library said it passed."** Libraries compute the pans. They do not choose which one to level, and their default thresholds are someone else's tolerance. The record has to show the choice.

## 7. Where the law sits

Stated as rules, with the provisions in the research note. This section covers the EU AI Act only; the interaction with data protection law (automated-decision rights, lawful basis, impact assessments) is covered in the Part 1 policy sets, and equality law is jurisdiction-specific and out of this artifact's scope.

- AI used to evaluate the creditworthiness of natural persons or establish their credit score is on the high-risk list, with an express exception for AI used to detect financial fraud. The high-risk duties bind from 2 December 2027 (a deferral, not an exemption - see Part 2).
- A provider of a high-risk system that trains models on data must apply data governance practices to training, validation and testing data that include examining the data for possible biases likely to affect health and safety, negatively impact fundamental rights, or lead to discrimination prohibited under Union law - especially where outputs feed future inputs - and taking appropriate measures to detect, prevent and mitigate those biases. Data sets must also be relevant, sufficiently representative and as far as possible error-free and complete, with appropriate statistical properties as regards the persons or groups the system will be used on, and must reflect the setting in which it will be used. Steps 4 to 6 are that duty.
- Special categories of personal data may be processed for bias detection and correction, to the extent strictly necessary, by providers of high-risk systems and - since the 2026 amendment - by deployers of high-risk systems and by providers and deployers of any other AI system, under six cumulative conditions (step 1 lists them). The permission is exceptional and creates no obligation to test; it removes the "we cannot lawfully hold the data" objection, which is a different thing. Step 1 is that rule.
- The risk management system must identify and address risks to fundamental rights; residual risk must be judged acceptable; testing is against metrics and probabilistic thresholds defined in advance; and the provider must consider adverse impact on under-18s and other vulnerable groups. Steps 3, 5 and 7 are that duty, and "defined in advance" is why step 3 comes before any result.
- The technical documentation must describe the training data (provenance, scope, characteristics, labelling and cleaning), the validation and testing procedures and data, the metrics used including for potentially discriminatory impacts, and dated, signed test reports. Step 7's record is that documentation.
- Deployers must monitor the operation of the system in accordance with the instructions for use and keep the automatically generated logs for at least six months. For a financial institution subject to Union financial services law on internal governance, the monitoring duty is deemed met by complying with those rules and the logs are kept as part of that documentation - which is where a bank's model risk framework meets this walkthrough. Step 8 is that duty on the deployer side; the provider's counterpart is a post-market monitoring plan, which now forms part of the technical documentation.
- Deployers of credit-scoring high-risk systems are among those who must carry out a fundamental rights impact assessment before first use - the duty otherwise falls only on public bodies and providers of public services - covering the categories of persons and groups likely to be affected, the specific risks of harm to them, the human oversight measures, and what happens if the risks materialise; the results are notified to the market surveillance authority. Where a data protection impact assessment already covers an element, it may be cross-referenced, and the AI Office is to provide a template. The step 1-3 record is the bias input to that assessment.

**Mapping to the series' acceptable use policies.** A system that makes or materially shapes credit decisions about individuals is at the top level of use in every jurisdiction's policy in Part 1 (decisions with legal or similarly significant effect); this walkthrough is the bias-testing control those policies require at that level.

## 8. Blank testing record

```
BIAS AND FAIRNESS TEST RECORD
System / model version:                 Threshold:                 Date:
Decision made or informed:
Population:
Characteristics tested:                 Lawful basis for holding each:
Reference group per characteristic:     Unit of comparison:        Minimum cell size:

PRIMARY CRITERION (fixed before results):  [ ] pan 1  [ ] pan 2 (FPR / FNR)  [ ] pan 3
Reasoning:
Tolerances for the other two pans:
Fixed by (name, role):                  Date fixed:

DATA TESTS
Representation (group share: applicants / training / labelled):
Label: observed outcome [ ]  past decision [ ]  - if past decision, STOP and test the process
Proxy AUC (all features):        Without each candidate proxy:

OUTCOME TESTS (per characteristic, per group vs reference, with intervals)
Pan 1 - approval rate / gap / ratio:
Pan 2 - good payers refused / defaulters approved / gaps:
Pan 3 - calibration by band / approved default rate / gap:
Intersections tested:                   Cells below minimum reported as insufficient: [ ]

REMEDY TRIAL (table of remedies x three pans attached)
Remedy chosen:                          By (name, role):           Date:
Residual gaps accepted and tolerance they sit within:

MONITORING
Measures monitored / frequency:
Retest tolerance:                       Retest triggers:
Versions: data           model           threshold           script
Signed:                                 Role:                      Date:
```

## 9. Limitations

- **One jurisdiction's law.** Only the EU AI Act is stated. Equality law (which decides whether group-specific thresholds are lawful) and data protection law are not covered here and change the answer to step 6 by jurisdiction.
- **Synthetic data.** The worked example's numbers are generated. Real portfolios have more groups, more features, and outcome data censored by past refusals in ways the example only gestures at.
- **Binary decisions.** Pricing, limits and referrals are decisions too, and the three pans apply to each; the walkthrough shows approve-or-refuse only.
- **Two groups.** Real testing runs across several characteristics and their intersections; the cell-size problem grows quickly.
- **Not reviewed by counsel.** Educational material, not legal advice.

---

*Part 3 of the AI Governance Series - github.com/NarendraKarki/ai-governance. Educational, not legal advice. Use it, and tell me what to improve.*
