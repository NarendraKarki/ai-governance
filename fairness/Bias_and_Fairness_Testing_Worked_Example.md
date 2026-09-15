# Worked example - a synthetic bank tests its credit scoring model

**Companion to the Part 3 walkthrough.** Version 1.0. Every table below is printed by `fairness_testing_credit.py` from `applicants_synthetic.csv`; run it and the numbers reproduce exactly (seed 20260910; numpy 2.4.4, pandas 3.0.2, scikit-learn 1.8.0 - other versions may move a figure by a tenth of a point).

Educational material, not legal advice. The bank, the applicants and the outcomes are synthetic.

---

## 1. The setup

**Decision.** Approve or refuse an application for unsecured personal credit. Refuse if the model's predicted probability of default within 24 months is 20% or more.

**Population.** 20,000 synthetic applicants; 12,000 used to train the model, 8,000 held out for every test below.

**Groups.** Two, defined by a protected characteristic the bank holds for bias testing only (A: 72%; B: 28%). The characteristic is deliberately unnamed here: the arithmetic is the same for sex, age band, ethnicity or nationality, and naming one would imply a finding about that group which synthetic data cannot support. The Part 3 video leaves them unlabelled for the same reason: an earlier cut read them as men and women for a general audience, and that was withdrawn because it attached an invented default rate to a real protected group - and attached it in the direction opposite to the pattern the evidence shows. The generator gives group B a shorter average credit history, a lower average income, a higher average debt-to-income ratio and a slightly higher rate of missed payments - the structural correlates that make base rates differ in real portfolios. **Group membership is not a term in the default equation.** Default is generated from debt-to-income, missed payments, history length and income only.

**Features the model sees.** Age, income, credit history length, debt-to-income ratio, missed payments in the last 24 months, and a five-band postcode indicator. Group B is concentrated in postcode bands 4 and 5, which makes the band a proxy. **The model never sees the group.**

**Model.** Logistic regression trained on observed default. AUC 0.813 on the held-out set.

## 2. Round 1 - one threshold for everyone

| Measure | Group A | Group B | Gap |
|---|---|---|---|
| Applicants (held-out) | 5,819 | 2,181 | |
| Actual default rate (base rate) | 9.7% | 21.1% | |
| **Pan 1** - approval rate | 87.2% | 58.8% | 28.4 pts; ratio 0.67 |
| **Pan 2** - good payers refused (FPR) | 9.2% | 32.4% | 23.2 pts |
| **Pan 2** - defaulters approved (FNR) | 54.0% | 26.2% | 27.7 pts |
| **Pan 3** - default rate among those approved | 6.0% | 9.4% | 3.4 pts |

Bootstrap 95% range on the approval gap: 26.1 to 30.5 points. The gap is real, not sampling noise.

**Pan 3 in detail - calibration by score band.** Does a score mean the same thing in both groups?

| Score band | Group A: n / predicted / actual | Group B: n / predicted / actual |
|---|---|---|
| 0 to 5% | 2,526 / 2.5% / 1.8% | 272 / 3.1% / 2.6% |
| 5 to 10% | 1,419 / 7.2% / 7.0% | 410 / 7.5% / 8.0% |
| 10 to 20% | 1,128 / 14.0% / 14.3% | 601 / 14.7% / 13.5% |
| 20 to 30% | 430 / 24.0% / 29.1% | 369 / 24.6% / 25.5% |
| 30 to 50% | 248 / 36.6% / 37.9% | 376 / 38.5% / 40.4% |
| 50% and over | 68 / 58.8% / 61.8% | 153 / 61.9% / 61.4% |

Predicted and actual track each other in both groups within a few points in every band with a workable cell size. The score means the same thing for an A applicant and a B applicant. The model is, in this sense, fair - and it approves group B 28 points less often and refuses group B's good payers three and a half times as often.

**Reading.** This is what a competently built, group-blind, calibrated model does when the groups genuinely default at different rates. Nothing went wrong in the modelling. The gap is in the data's risk drivers, which differ between groups for reasons the model neither knows nor can fix.

## 3. Is the proxy doing the work?

**Proxy strength.** A logistic regression trained to predict *group* from the model's six input features recovers it with AUC 0.857. Without the postcode band, 0.780. A strong proxy is present, and even without it the remaining features carry a good deal of group information (income and history length do the rest).

**Removal trial.** Retrain the default model without the postcode band, same threshold:

| Measure | Group A | Group B | Gap |
|---|---|---|---|
| Approval rate | 87.4% | 58.6% | 28.8 pts; ratio 0.67 |
| Good payers refused | 9.1% | 32.7% | 23.6 pts |
| Default rate among approved | 6.1% | 9.4% | 3.3 pts |

Model AUC: 0.813 before, 0.813 after. **Nothing changed.** The proxy was present but not doing any work, because the model had no use for it - the outcome it was trained on does not depend on postcode, so the fitted coefficient on the band was near zero. Removing it costs nothing and fixes nothing.

## 4. The label-bias model - where the proxy *is* doing the work

The same bank, a different training label. Instead of observed default, the model is trained to predict the **decisions of the bank's old manual process**, which refused the riskiest 20% of applications and, by hand, applied a penalty to postcode bands 4 and 5. The threshold is set so that the overall approval rate matches round 1.

| Measure | Group A | Group B | Gap |
|---|---|---|---|
| Approval rate | 89.6% | 52.5% | 37.1 pts; ratio 0.59 |
| Good payers refused | 7.6% | 39.3% | 31.7 pts |
| Defaulters approved | 63.1% | 21.7% | 41.4 pts |
| Default rate among approved | 6.9% | 8.7% | 1.9 pts |

The approval gap has widened by 9 points and group B's good payers are now refused at 39%. The model learned the old process, hand-applied postcode penalty included, from a label that never mentioned postcode or group.

**Removal trial on this model** - retrain without the postcode band, threshold reset to the same overall approval rate:

| Measure | Group A | Group B | Gap |
|---|---|---|---|
| Approval rate | 87.3% | 58.5% | 28.9 pts; ratio 0.67 |
| Good payers refused | 9.1% | 32.8% | 23.7 pts |
| Default rate among approved | 6.0% | 9.3% | 3.3 pts |

The gap falls back to 29 points - the same figure as round 1. Removing the proxy removed exactly the bias it was carrying (the old process's manual penalty) and nothing else. What remains is the real-risk disparity, which no feature removal touches.

**Reading.** Two models, one proxy, opposite answers. The proxy test in step 4 of the walkthrough (AUC 0.857 in both cases) says a proxy is *present*; only the removal trial says whether it is *working*. And the label test in step 4 would have caught this model before any of it: its label was a past decision, not an observed outcome, which is the walkthrough's instruction to stop and test the process first.

## 5. Round 2 - level pan 1

Keep group A's threshold at 20% and set group B's so that approval rates match. The search lands on 40.6%: a group B applicant is approved up to a predicted default risk of 41%, a group A applicant refused from 20%.

| Measure | Group A | Group B | Gap |
|---|---|---|---|
| **Pan 1** - approval rate | 87.2% | 87.1% | 0.1 pts; ratio 1.00 |
| **Pan 2** - good payers refused | 9.2% | 7.1% | -2.1 pts |
| **Pan 2** - defaulters approved | 54.0% | 65.5% | -11.5 pts |
| **Pan 3** - default rate among approved | 6.0% | 15.9% | 9.9 pts |

Pans 1 and 2 (on the applicant-harm side) are level. Pan 3 has tipped: an approved group B customer is now two and a half times as likely to default as an approved group A customer, and two applicants with identical scores of, say, 30% receive opposite decisions depending on their group.

**Level pan 2 instead** - set group B's threshold (36.9%) so that good payers are refused at the same rate:

| Measure | Group A | Group B | Gap |
|---|---|---|---|
| Approval rate | 87.2% | 84.1% | 3.0 pts; ratio 0.97 |
| Good payers refused | 9.2% | 9.3% | 0.1 pts |
| Defaulters approved | 54.0% | 59.7% | -5.7 pts |
| Default rate among approved | 6.0% | 15.0% | 9.0 pts |

Same picture. On this data, pans 1 and 2 (applicant side) can be levelled together, at the cost of pan 3; or pan 3 can be held level, at the cost of pans 1 and 2. That is the arithmetic the walkthrough describes, in numbers.

## 6. Intersections and the small-cell problem

Group by age band, round 1 threshold:

| Group | Age band | n | Approval rate | 95% interval | Good payers refused |
|---|---|---|---|---|---|
| A | 25 and over | 5,346 | 87.3% | 86.4% to 88.2% | 9.1% |
| A | under 25 | 473 | 85.6% | 82.5% to 88.8% | 10.9% |
| B | 25 and over | 2,005 | 58.6% | 56.4% to 60.8% | 32.6% |
| B | under 25 | 176 | 61.4% | 54.2% to 68.6% | 30.1% |

Group B under-25s are approved 3 points *more* often than group B over-25s on the point estimate. The interval is 14 points wide and contains the over-25 figure comfortably. Recorded as "no established difference at n=176", not as a finding in either direction. With the bank's minimum cell size of 100 the cell is reportable; a further split (by sex, say) would take it below and be reported as insufficient.

## 7. The synthetic bank's completed record

```
BIAS AND FAIRNESS TEST RECORD
System / model version: PD-retail-v3 (logistic, observed-default label)   Threshold: 20%   Date: 10 Sep 2026
Decision made or informed: approve / refuse, unsecured personal credit
Population: new applicants, held-out set n=8,000 of 20,000
Characteristics tested: one (A / B)          Lawful basis for holding each: the AI Act's special-category
                                              permission for bias detection and correction, all six conditions
                                              evidenced (synthetic data would not do - the disparity is in the
                                              real risk drivers; pseudonymised; access logged; not transmitted;
                                              deleted at cycle end; reasons recorded)
Reference group: A                            Unit of comparison: application    Minimum cell size: 100

PRIMARY CRITERION (fixed before results):  [ ] pan 1  [ ] pan 2  [x] pan 3 (calibration / approved default rate)
Reasoning: a stated risk must be a true risk; per-group thresholds would give identical scores
  different decisions by group, which the bank's equality-law advice rules out.
Tolerances for the other two pans: pan 1 ratio no lower than 0.80 as a screening trigger; pan 2
  good-payer refusal gap no more than 5 points. Both are triggers for the remedy trial, not pass marks.
Fixed by: Head of Model Risk                 Date fixed: 8 Sep 2026

DATA TESTS
Representation: B is 28% of applicants, 28% of training rows, 28% of labelled rows (synthetic; a real
  portfolio would show the labelled share lower)
Label: observed outcome [x]  past decision [ ]
Proxy AUC (all features): 0.857        Without postcode band: 0.780

OUTCOME TESTS (A vs B, round 1)
Pan 1 - approval 87.2% / 58.8%; gap 28.4 pts (26.1 to 30.5); ratio 0.67   -> OUTSIDE tolerance
Pan 2 - good payers refused 9.2% / 32.4%; gap 23.2 pts                    -> OUTSIDE tolerance
Pan 3 - calibration by band within 3 pts in all bands n>=150; approved default 6.0% / 9.4%; gap 3.4 -> within
Intersections tested: group x age band        Cells below minimum reported as insufficient: [x] (none this cycle)

REMEDY TRIAL
  remove postcode band      -> no change on any pan (proxy present, not working)
  per-group thresholds      -> pans 1-2 level; pan 3 gap 9.9 pts; rejected on equality-law grounds
  referral band 20-30%      -> 799 applications (430 A, 369 B) to human review; pans re-measured post-review
  thin-file outcome programme -> addresses representation of short-history applicants at source; 12 months
Remedy chosen: referral band now; thin-file programme funded    By: Chief Risk Officer    Date: 10 Sep 2026
Residual gaps accepted: pan 1 and pan 2 gaps as measured, pending programme; reviewed quarterly

MONITORING
Measures monitored / frequency: approval-rate gap and referral-band overrides by group, monthly;
  error rates and approved default rate by group, quarterly on 24-month matured cohorts
Retest tolerance: approval ratio moves by 0.05; any pan 3 gap over 3 pts
Retest triggers: threshold change, retrain, product or population change, legal change, complaints pattern
Versions: data applicants_synthetic.csv (seed 20260910)   model PD-retail-v3   threshold 0.20
          script fairness_testing_credit.py
Signed: Head of Model Risk                   Date: 10 Sep 2026
```

## 8. Reproducing it

```
pip install numpy pandas scikit-learn
python3 fairness_testing_credit.py
```

The script regenerates `applicants_synthetic.csv`, trains every model above, and writes `fairness_results.md` and `fairness_results.json`. Change `SEED` to see how far the figures move (a point or two) and how little the shape does.

---

*Part 3 of the AI Governance Series - github.com/NarendraKarki/ai-governance. Educational, not legal advice.*
