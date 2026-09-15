# Bias and Fairness Testing - credit scoring as the worked example

**Part 3 of the AI Governance Series.**

A testing method for AI systems that make or shape decisions about people, built around one idea: fairness has three pans, not two, and when groups genuinely differ in the outcome being predicted, no model levels all three. The job is to choose which pan to level, write down why, and measure the other two. The worked example is a synthetic bank's credit scoring model, with every number reproducible from one script.

## What is in this folder

| File | What it is |
|---|---|
| `Bias_and_Fairness_Testing_Walkthrough.md` | The artifact: the three fairness criteria and why they conflict, where bias enters, an eight-step testing protocol, the misreadings, where the EU AI Act sits, and a blank testing record |
| `Bias_and_Fairness_Testing_Worked_Example.md` | The synthetic bank: a group-blind model tested on 8,000 applicants; the proxy that was not doing the work and the one that was; levelling one pan and watching the third tip; intersections; the completed record |
| `Bias_and_Fairness_Testing_Research_Note.md` | The working: every legal position with its provision and verification status, the method literature behind the three-pan framing, and the choices made |
| `Bias_and_Fairness_Testing_Source_Register.md` | What was held, what was not, and what therefore is not asserted |
| `fairness_testing_credit.py` | Generates the dataset, trains every model, prints every table. `python3 fairness_testing_credit.py` |
| `requirements.txt` | The package versions the published figures were produced with |
| `applicants_synthetic.csv` | The 20,000 synthetic applicants, as generated |
| `fairness_results.md` / `.json` | The script's output as published |
| `downloads/` | Word exports |

## Why this artifact exists

Most bias testing stops at one number - usually the approval-rate gap - and most "the model passed fairness testing" statements do not say which test. This walkthrough makes the choice of test explicit, puts it before the results rather than after, and shows on real (synthetic) numbers why the choice cannot be avoided: a well-built model that never sees the group is calibrated *and* approves one group 28 points less often, and every fix for the second fact costs the first.

It is written for the people who have to sign the record: model risk, governance, privacy, security and audit teams.

## Legal baseline and verification

Built on the **consolidated Artificial Intelligence Act of 27 July 2026** - Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744 (the Digital Omnibus on AI) - read in the primary text. Verification date: **10 September 2026**. Every legal position in the walkthrough's section 7 is mapped to article and paragraph in the research note with its base-text or omnibus marker.

The reading corrected the draft: the special-category permission for bias testing that the base text placed in Article 10(5) is deleted in the consolidation and re-enacted as Article 4a, with an additional condition and an extension to deployers and to non-high-risk systems - and an express statement that it creates no duty to test. The fundamental rights impact assessment duty on credit-scoring deployers is unchanged. Corrections are recorded in the research note, not silently fixed.

Everything numerical is verified differently: by running the script. The worked example's tables are transcribed from its output, and the environment used is recorded in the source register.

## How to use it

Run the protocol in order. Steps 1 to 3 are decisions, recorded before any result is seen. Steps 4 to 6 are the tests and the remedy trial. Step 7 is the record - section 8 of the walkthrough is a blank one, and section 7 of the worked example is a completed one. Step 8 is the monitoring that makes it a control rather than a gate.

## Status

Version 1.0. Verified against the primary text named in the source register. Use it, and tell me what to improve.

---

*Educational material, not legal advice. Bias testing of a real system, and any remedy that treats groups differently, should be reviewed by qualified legal counsel before it is relied on.*
