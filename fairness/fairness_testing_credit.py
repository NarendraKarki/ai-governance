#!/usr/bin/env python3
"""
Bias and fairness testing - credit scoring worked example.
Part 3 of the AI Governance Series. Educational, not legal advice.

Generates a synthetic applicant dataset, trains a group-blind default model,
and measures it against three fairness criteria under three threshold policies.
Every figure quoted in the walkthrough is printed by this script.

Requirements: python3, numpy, pandas, scikit-learn. Run:  python3 fairness_testing_credit.py
Outputs: applicants_synthetic.csv, fairness_results.json, fairness_results.md
"""
import json
import numpy as np
import pandas as pd
from sklearn.linear_model import LogisticRegression
from sklearn.metrics import roc_auc_score

SEED = 20260910
rng = np.random.default_rng(SEED)
N = 20000

# ---------------------------------------------------------------- 1. data
# Two groups defined by a protected characteristic the lender is permitted to
# hold for bias testing. Group B is a minority with a shorter average credit
# history and lower average income - the structural correlates that make the
# default base rate differ even though group membership itself never enters
# the outcome equation.
group = rng.choice(["A", "B"], size=N, p=[0.72, 0.28])
is_b = (group == "B")

age = np.clip(rng.normal(41, 12, N), 21, 75).round()
income = np.exp(rng.normal(np.where(is_b, 10.35, 10.55), 0.42, N)).round(-2)          # annual, currency units
history_years = np.clip(rng.gamma(np.where(is_b, 2.2, 3.6), 2.6, N), 0, 30).round(1)
dti = np.clip(rng.normal(np.where(is_b, 0.36, 0.31), 0.13, N), 0.02, 0.95).round(3)   # debt-to-income
missed_24m = rng.poisson(np.where(is_b, 0.55, 0.38), N)                              # missed payments, last 24 months
# postcode band: a proxy. Bands 1-5, group B concentrated in bands 4-5.
band_p_a = [0.30, 0.28, 0.22, 0.13, 0.07]
band_p_b = [0.06, 0.12, 0.22, 0.30, 0.30]
postcode_band = np.where(is_b, rng.choice([1, 2, 3, 4, 5], N, p=band_p_b),
                                rng.choice([1, 2, 3, 4, 5], N, p=band_p_a))

# True default process: depends on real risk drivers only. Group is NOT a term.
z = (-2.55
     + 6.0 * (dti - 0.32)
     + 0.85 * missed_24m
     - 0.14 * (history_years - 6)
     - 1.1 * (np.log(income) - 10.5))
p_default = 1 / (1 + np.exp(-z))
default_24m = (rng.random(N) < p_default).astype(int)

df = pd.DataFrame(dict(applicant_id=np.arange(1, N + 1), group=group, age=age.astype(int),
                       income=income, history_years=history_years, dti=dti,
                       missed_24m=missed_24m, postcode_band=postcode_band,
                       default_24m=default_24m))
df.to_csv("applicants_synthetic.csv", index=False)

# ---------------------------------------------------------------- 2. model
# Group-blind: the protected characteristic is withheld from the model.
FEATURES = ["age", "income", "history_years", "dti", "missed_24m", "postcode_band"]
train = df.sample(frac=0.6, random_state=SEED)
test = df.drop(train.index).copy()

def fit(features):
    X = train[features].copy(); X["income"] = np.log(X["income"])
    Xt = test[features].copy(); Xt["income"] = np.log(Xt["income"])
    m = LogisticRegression(max_iter=2000).fit(X, train["default_24m"])
    return m.predict_proba(Xt)[:, 1]

test["score"] = fit(FEATURES)                    # predicted probability of default

# ---------------------------------------------------------------- 3. metrics
def metrics(t, reject_mask):
    """Positive class = predicted default = REJECT."""
    out = {}
    for g in ["A", "B"]:
        s = t[t.group == g]; r = reject_mask[t.group == g]
        y = s.default_24m.values
        out[g] = dict(
            n=int(len(s)),
            base_rate=float(y.mean()),                                   # actual default rate
            approval_rate=float(1 - r.mean()),                           # selection rate
            fpr=float(r[y == 0].mean()),                                 # good payers rejected
            fnr=float((~r)[y == 1].mean()),                              # defaulters approved
            default_rate_among_approved=float(y[~r].mean()),             # calibration at the decision
            mean_score_approved=float(s.score.values[~r].mean()),
        )
    a, b = out["A"], out["B"]
    out["gaps"] = dict(
        approval_ratio_B_over_A=b["approval_rate"] / a["approval_rate"],
        approval_gap_pts=(a["approval_rate"] - b["approval_rate"]) * 100,
        fpr_gap_pts=(b["fpr"] - a["fpr"]) * 100,
        fnr_gap_pts=(a["fnr"] - b["fnr"]) * 100,
        calibration_gap_pts=(b["default_rate_among_approved"] - a["default_rate_among_approved"]) * 100,
    )
    return out

def threshold_for_rate(t, g, target_rate, key):
    """Find the score threshold for group g that hits a target approval rate or FPR."""
    s = t[t.group == g]
    cands = np.unique(s.score.values)
    best, bestd = None, 9
    for c in cands[::5]:
        r = s.score.values >= c
        if key == "approval":
            v = 1 - r.mean()
        else:
            v = r[s.default_24m.values == 0].mean()
        if abs(v - target_rate) < bestd:
            best, bestd = c, abs(v - target_rate)
    return float(best)

results = {}
# Policy 1: one threshold for everyone (the model as built)
THR = 0.20
rej1 = (test.score >= THR).values
results["policy_1_single_threshold"] = dict(thresholds=dict(A=THR, B=THR), **metrics(test, rej1))

# Policy 2: thresholds chosen so approval rates are equal (demographic parity)
targetA = results["policy_1_single_threshold"]["A"]["approval_rate"]
thrB = threshold_for_rate(test, "B", targetA, "approval")
rej2 = np.where(test.group.values == "B", test.score.values >= thrB, test.score.values >= THR)
results["policy_2_equal_approval"] = dict(thresholds=dict(A=THR, B=thrB), **metrics(test, rej2))

# Policy 3: thresholds chosen so good payers are rejected at the same rate (equal FPR)
targetFPR = results["policy_1_single_threshold"]["A"]["fpr"]
thrB3 = threshold_for_rate(test, "B", targetFPR, "fpr")
rej3 = np.where(test.group.values == "B", test.score.values >= thrB3, test.score.values >= THR)
results["policy_3_equal_fpr"] = dict(thresholds=dict(A=THR, B=thrB3), **metrics(test, rej3))

# Calibration by score band, per group (does a score mean the same thing for both?)
bands = [0, 0.05, 0.10, 0.20, 0.30, 0.50, 1.0]
test["band"] = pd.cut(test.score, bands, include_lowest=True)
calib = test.groupby(["band", "group"], observed=True).agg(n=("default_24m", "size"),
                                                          actual=("default_24m", "mean"),
                                                          predicted=("score", "mean")).reset_index()
calib["band"] = calib["band"].astype(str)
results["calibration_by_band"] = calib.to_dict(orient="records")

# Proxy test: can the features recover the protected characteristic?
Xp = test[FEATURES].copy(); Xp["income"] = np.log(Xp["income"])
pm = LogisticRegression(max_iter=2000).fit(Xp, test.group == "B")
results["proxy_auc_all_features"] = float(roc_auc_score(test.group == "B", pm.predict_proba(Xp)[:, 1]))
Xq = Xp.drop(columns=["postcode_band"])
pm2 = LogisticRegression(max_iter=2000).fit(Xq, test.group == "B")
results["proxy_auc_without_postcode"] = float(roc_auc_score(test.group == "B", pm2.predict_proba(Xq)[:, 1]))

# Remediation trial: drop the proxy feature, re-run policy 1
test["score_noproxy"] = fit([f for f in FEATURES if f != "postcode_band"])
t2 = test.copy(); t2["score"] = t2["score_noproxy"]
results["policy_1_without_postcode"] = dict(thresholds=dict(A=THR, B=THR), **metrics(t2, (t2.score >= THR).values))
results["model_auc_with_postcode"] = float(roc_auc_score(test.default_24m, test.score))
results["model_auc_without_postcode"] = float(roc_auc_score(test.default_24m, test.score_noproxy))

# Label bias: a model trained on the OLD process's decisions instead of on
# observed repayment. The old process penalised postcode bands 4-5 by hand.
old_z = z + np.where(postcode_band >= 4, 0.9, 0.0) + rng.normal(0, 0.35, N)
df["old_decision_reject"] = (old_z > np.quantile(old_z, 0.80)).astype(int)
train_l = df.loc[train.index]; test_l = df.loc[test.index].copy()
Xl = train_l[FEATURES].copy(); Xl["income"] = np.log(Xl["income"])
Xlt = test_l[FEATURES].copy(); Xlt["income"] = np.log(Xlt["income"])
ml = LogisticRegression(max_iter=2000).fit(Xl, train_l["old_decision_reject"])
test_l["score"] = ml.predict_proba(Xlt)[:, 1]
overall_approval = 1 - (rej1.mean())
thr_l = float(np.quantile(test_l["score"], overall_approval))
results["label_bias_model"] = dict(thresholds=dict(A=thr_l, B=thr_l), **metrics(test_l, (test_l.score >= thr_l).values))
Xl2 = Xlt.drop(columns=["postcode_band"]); Xl2t = Xl.drop(columns=["postcode_band"])
ml2 = LogisticRegression(max_iter=2000).fit(Xl2t, train_l["old_decision_reject"])
t3 = test_l.copy(); t3["score"] = ml2.predict_proba(Xl2)[:, 1]
thr_l2 = float(np.quantile(t3["score"], overall_approval))
results["label_bias_model_without_postcode"] = dict(thresholds=dict(A=thr_l2, B=thr_l2), **metrics(t3, (t3.score >= thr_l2).values))

# Intersection: group x age band - the small-cell problem
test["age_band"] = np.where(test.age < 25, "under 25", "25 and over")
inter = []
for (g, ab), s in test.groupby(["group", "age_band"]):
    r = (s.score >= THR).values
    y = s.default_24m.values
    n = len(s); ar = 1 - r.mean()
    se = np.sqrt(ar * (1 - ar) / n)
    inter.append(dict(group=g, age_band=ab, n=int(n), approval_rate=float(ar),
                      ci95_low=float(ar - 1.96 * se), ci95_high=float(ar + 1.96 * se),
                      fpr=float(r[y == 0].mean())))
results["intersection_group_by_age"] = inter

# Bootstrap CI on the headline approval gap (policy 1)
gaps = []
for _ in range(400):
    bs = test.sample(frac=1, replace=True, random_state=int(rng.integers(1e9)))
    r = (bs.score >= THR).values
    gaps.append(((1 - r[bs.group.values == "A"].mean()) - (1 - r[bs.group.values == "B"].mean())) * 100)
results["approval_gap_bootstrap_ci95_pts"] = [float(np.percentile(gaps, 2.5)), float(np.percentile(gaps, 97.5))]

with open("fairness_results.json", "w") as f:
    json.dump(results, f, indent=2)

# ---------------------------------------------------------------- 4. report
def pc(x): return f"{x*100:.1f}%"
L = ["# Fairness testing results - synthetic credit scoring example", "",
     f"Seed {SEED}; {N} synthetic applicants; 60/40 train-test split; test set n = {len(test)}.", ""]
for key, title in [("policy_1_single_threshold", "Policy 1 - one threshold for everyone"),
                   ("policy_2_equal_approval", "Policy 2 - thresholds set to equalise approval rates"),
                   ("policy_3_equal_fpr", "Policy 3 - thresholds set to equalise good-payer rejection (FPR)"),
                   ("policy_1_without_postcode", "Policy 1 re-run with postcode band removed"),
                   ("label_bias_model", "Label-bias model - trained on the old process's decisions, same overall approval rate"),
                   ("label_bias_model_without_postcode", "Label-bias model with postcode band removed")]:
    R = results[key]
    L += [f"## {title}", "", f"Thresholds: A reject at score >= {R['thresholds']['A']:.3f}; B reject at score >= {R['thresholds']['B']:.3f}", "",
          "| Measure | Group A | Group B | Gap |", "|---|---|---|---|",
          f"| Applicants (test) | {R['A']['n']} | {R['B']['n']} | |",
          f"| Actual default rate (base rate) | {pc(R['A']['base_rate'])} | {pc(R['B']['base_rate'])} | |",
          f"| Approval rate | {pc(R['A']['approval_rate'])} | {pc(R['B']['approval_rate'])} | {R['gaps']['approval_gap_pts']:.1f} pts; ratio {R['gaps']['approval_ratio_B_over_A']:.2f} |",
          f"| Good payers rejected (FPR) | {pc(R['A']['fpr'])} | {pc(R['B']['fpr'])} | {R['gaps']['fpr_gap_pts']:.1f} pts |",
          f"| Defaulters approved (FNR) | {pc(R['A']['fnr'])} | {pc(R['B']['fnr'])} | {R['gaps']['fnr_gap_pts']:.1f} pts |",
          f"| Default rate among those approved | {pc(R['A']['default_rate_among_approved'])} | {pc(R['B']['default_rate_among_approved'])} | {R['gaps']['calibration_gap_pts']:.1f} pts |", ""]
L += ["## Calibration by score band", "", "| Score band | Group | n | Predicted | Actual |", "|---|---|---|---|---|"]
for r in results["calibration_by_band"]:
    L.append(f"| {r['band']} | {r['group']} | {r['n']} | {pc(r['predicted'])} | {pc(r['actual'])} |")
L += ["", "## Proxy test", "",
      f"AUC for recovering group from the model's features: {results['proxy_auc_all_features']:.3f} (all features); {results['proxy_auc_without_postcode']:.3f} without postcode band.",
      f"Model AUC for default: {results['model_auc_with_postcode']:.3f} with postcode band; {results['model_auc_without_postcode']:.3f} without.", "",
      "## Intersection - group by age band (policy 1)", "", "| Group | Age band | n | Approval rate | 95% CI | FPR |", "|---|---|---|---|---|---|"]
for r in results["intersection_group_by_age"]:
    L.append(f"| {r['group']} | {r['age_band']} | {r['n']} | {pc(r['approval_rate'])} | {pc(r['ci95_low'])} to {pc(r['ci95_high'])} | {pc(r['fpr'])} |")
lo, hi = results["approval_gap_bootstrap_ci95_pts"]
L += ["", f"Bootstrap 95% interval on the policy 1 approval gap: {lo:.1f} to {hi:.1f} points.", ""]
open("fairness_results.md", "w").write("\n".join(L))
print("\n".join(L))
