# Fairness testing results - synthetic credit scoring example

Seed 20260910; 20000 synthetic applicants; 60/40 train-test split; test set n = 8000.

## Policy 1 - one threshold for everyone

Thresholds: A reject at score >= 0.200; B reject at score >= 0.200

| Measure | Group A | Group B | Gap |
|---|---|---|---|
| Applicants (test) | 5819 | 2181 | |
| Actual default rate (base rate) | 9.7% | 21.1% | |
| Approval rate | 87.2% | 58.8% | 28.4 pts; ratio 0.67 |
| Good payers rejected (FPR) | 9.2% | 32.4% | 23.2 pts |
| Defaulters approved (FNR) | 54.0% | 26.2% | 27.7 pts |
| Default rate among those approved | 6.0% | 9.4% | 3.4 pts |

## Policy 2 - thresholds set to equalise approval rates

Thresholds: A reject at score >= 0.200; B reject at score >= 0.406

| Measure | Group A | Group B | Gap |
|---|---|---|---|
| Applicants (test) | 5819 | 2181 | |
| Actual default rate (base rate) | 9.7% | 21.1% | |
| Approval rate | 87.2% | 87.1% | 0.1 pts; ratio 1.00 |
| Good payers rejected (FPR) | 9.2% | 7.1% | -2.1 pts |
| Defaulters approved (FNR) | 54.0% | 65.5% | -11.5 pts |
| Default rate among those approved | 6.0% | 15.9% | 9.9 pts |

## Policy 3 - thresholds set to equalise good-payer rejection (FPR)

Thresholds: A reject at score >= 0.200; B reject at score >= 0.369

| Measure | Group A | Group B | Gap |
|---|---|---|---|
| Applicants (test) | 5819 | 2181 | |
| Actual default rate (base rate) | 9.7% | 21.1% | |
| Approval rate | 87.2% | 84.1% | 3.0 pts; ratio 0.97 |
| Good payers rejected (FPR) | 9.2% | 9.3% | 0.1 pts |
| Defaulters approved (FNR) | 54.0% | 59.7% | -5.7 pts |
| Default rate among those approved | 6.0% | 15.0% | 9.0 pts |

## Policy 1 re-run with postcode band removed

Thresholds: A reject at score >= 0.200; B reject at score >= 0.200

| Measure | Group A | Group B | Gap |
|---|---|---|---|
| Applicants (test) | 5819 | 2181 | |
| Actual default rate (base rate) | 9.7% | 21.1% | |
| Approval rate | 87.4% | 58.6% | 28.8 pts; ratio 0.67 |
| Good payers rejected (FPR) | 9.1% | 32.7% | 23.6 pts |
| Defaulters approved (FNR) | 54.3% | 26.0% | 28.3 pts |
| Default rate among those approved | 6.1% | 9.4% | 3.3 pts |

## Label-bias model - trained on the old process's decisions, same overall approval rate

Thresholds: A reject at score >= 0.400; B reject at score >= 0.400

| Measure | Group A | Group B | Gap |
|---|---|---|---|
| Applicants (test) | 5819 | 2181 | |
| Actual default rate (base rate) | 9.7% | 21.1% | |
| Approval rate | 89.6% | 52.5% | 37.1 pts; ratio 0.59 |
| Good payers rejected (FPR) | 7.6% | 39.3% | 31.7 pts |
| Defaulters approved (FNR) | 63.1% | 21.7% | 41.4 pts |
| Default rate among those approved | 6.9% | 8.7% | 1.9 pts |

## Label-bias model with postcode band removed

Thresholds: A reject at score >= 0.392; B reject at score >= 0.392

| Measure | Group A | Group B | Gap |
|---|---|---|---|
| Applicants (test) | 5819 | 2181 | |
| Actual default rate (base rate) | 9.7% | 21.1% | |
| Approval rate | 87.3% | 58.5% | 28.9 pts; ratio 0.67 |
| Good payers rejected (FPR) | 9.1% | 32.8% | 23.7 pts |
| Defaulters approved (FNR) | 54.0% | 25.8% | 28.2 pts |
| Default rate among those approved | 6.0% | 9.3% | 3.3 pts |

## Calibration by score band

| Score band | Group | n | Predicted | Actual |
|---|---|---|---|---|
| (-0.001, 0.05] | A | 2526 | 2.5% | 1.8% |
| (-0.001, 0.05] | B | 272 | 3.1% | 2.6% |
| (0.05, 0.1] | A | 1419 | 7.2% | 7.0% |
| (0.05, 0.1] | B | 410 | 7.5% | 8.0% |
| (0.1, 0.2] | A | 1128 | 14.0% | 14.3% |
| (0.1, 0.2] | B | 601 | 14.7% | 13.5% |
| (0.2, 0.3] | A | 430 | 24.0% | 29.1% |
| (0.2, 0.3] | B | 369 | 24.6% | 25.5% |
| (0.3, 0.5] | A | 248 | 36.6% | 37.9% |
| (0.3, 0.5] | B | 376 | 38.5% | 40.4% |
| (0.5, 1.0] | A | 68 | 58.8% | 61.8% |
| (0.5, 1.0] | B | 153 | 61.9% | 61.4% |

## Proxy test

AUC for recovering group from the model's features: 0.857 (all features); 0.780 without postcode band.
Model AUC for default: 0.813 with postcode band; 0.813 without.

## Intersection - group by age band (policy 1)

| Group | Age band | n | Approval rate | 95% CI | FPR |
|---|---|---|---|---|---|
| A | 25 and over | 5346 | 87.3% | 86.4% to 88.2% | 9.1% |
| A | under 25 | 473 | 85.6% | 82.5% to 88.8% | 10.9% |
| B | 25 and over | 2005 | 58.6% | 56.4% to 60.8% | 32.6% |
| B | under 25 | 176 | 61.4% | 54.2% to 68.6% | 30.1% |

Bootstrap 95% interval on the policy 1 approval gap: 26.1 to 30.5 points.
