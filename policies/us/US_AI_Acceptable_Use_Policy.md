# Artificial Intelligence Acceptable Use Policy - United States

### Federal sectoral baseline + California + Colorado, with other states named and not asserted

**Organisation:** [ORGANISATION]
**Effective date:** [DATE]  **Version:** 1.0
**Policy owner:** [CISO]  **Privacy lead:** [Chief Privacy Officer / privacy lead]
**Classification:** Internal
**Review:** at least every six months, and on material change in tools or regulation

---

## 1. Purpose

[ORGANISATION] permits the use of artificial intelligence (AI) tools to improve
productivity, provided that use protects the organisation's data, its customers and
staff, its intellectual property, and its obligations under United States law. This
policy sets the requirements for all such use.

Three features of the US framework shape this document.

### 1.1 There is no single US AI or privacy statute

The United States regulates AI through a patchwork: a federal baseline that is
sectoral (credit, health, children's data, financial institutions) plus a general
unfair-and-deceptive-practices power, and state laws that differ by state. **This
policy states the federal baseline, California, and Colorado - and nothing else.**
Clause 3 routes each obligation to its source, and clause 22 states what the set
does not cover. An organisation reaching consumers in other states must overlay those
states' laws; assuming California and Colorado cover the country is the error this
edition exists to prevent.

### 1.2 Two different AI tests apply to overlapping ground

Colorado regulates a **high-risk artificial intelligence system** - one that makes,
or is a **substantial factor** in making, a consequential decision. A system that
merely assists a decision and is capable of altering its outcome is in.

California's regulations regulate **automated decisionmaking technology (ADMT)** -
technology that **replaces or substantially replaces human decisionmaking** in a
significant decision. A system whose output a human meaningfully reviews is out.

**The same tool can be inside Colorado's regime and outside California's at the same
time.** Clause 4 turns both tests into one worked determination, because applying
only the test you met first is the most likely failure here.

### 1.3 A governance framework has legal effect in Colorado

Colorado's statute names the NIST Artificial Intelligence Risk Management Framework
and ISO/IEC 42001 in its own text: a risk management program must be reasonable
considering those frameworks, compliance supports a **rebuttable presumption of
reasonable care**, and framework compliance plus a cure is an **affirmative defense**
in an enforcement action. Clause 9 builds the risk program on the NIST framework for
that reason - in this jurisdiction, governance structure is not just good practice;
it is the statutory safe harbour.

## 2. Scope

This policy applies to all employees, contractors, temporary staff, and third parties
who use [ORGANISATION] systems, data, or accounts. It covers all AI tools, including
public and generative AI services, AI features embedded in other software, coding
assistants, meeting and note-taking assistants, media generators, AI agents, and
internal AI systems. It applies on company devices and accounts, and on personal
devices or accounts whenever used for [ORGANISATION] work or data.

Compliance is mandatory. Breaches may result in disciplinary action up to and
including termination.

## 3. Which law reaches which use

3.1 **The federal baseline reaches everyone.** Unfair or deceptive acts or practices
are unlawful whatever the technology - overstating what an AI product does, or using
it in a way that injures consumers unfairly, is actionable without any AI-specific
statute. Sectoral rules attach by data and activity: consumer-report data and
AI-driven eligibility decisions engage the credit-reporting regime and its adverse
action machinery; health information held by covered entities engages the health
privacy and security rules; children's online data engages the children's privacy
rule; customer information at financial institutions engages the safeguards rule.

3.2 **California attaches by the consumer.** Where [ORGANISATION] is a covered
business processing California consumers' personal information, the CCPA and its
regulations apply - including, for AI, the ADMT article, the risk-assessment article,
and the cybersecurity audit article at their own thresholds.

3.3 **Colorado attaches by the consumer too.** Where a high-risk AI system makes or
substantially factors into a consequential decision concerning a Colorado resident,
the Colorado AI Act's developer or deployer duties apply. **They are in force now** -
the commencement was moved once, and the moved date has passed.

3.4 **Sector carve-outs exist on both sides** - Colorado's Act and California's
regime each defer in defined ways to entities and processing already governed by
sectoral law (insurers, banks, HIPAA-covered activity, among others). Whether a
carve-out applies is determined by the privacy lead in writing per system, never
assumed.

3.5 The privacy lead determines, for each AI use, which of the above apply, and the
determination is recorded in the AI system inventory.

## 4. The two determinations

**Every AI tool that touches decisions about people passes through both tests, and
the answers are recorded separately.**

4.1 **Colorado test - is it a high-risk AI system?** Does the tool make, or is it a
substantial factor in making - it assists the decision, and is capable of altering
the outcome - a consequential decision: one with a material legal or similarly
significant effect on education, employment, financial or lending services,
essential government services, health-care services, housing, insurance, or legal
services, concerning a Colorado resident?

4.2 The statute excludes systems intended for a narrow procedural task, or for
detecting decision-making patterns without replacing human assessment, and a list of
ordinary technologies - unless they in fact make or substantially factor into a
consequential decision. **One exclusion deserves its own sentence: a
natural-language technology that provides information, referrals, or answers is
excluded only if it is subject to an accepted use policy that prohibits generating
discriminatory or harmful content.** This document is, among other things, that
policy - which means keeping it enforced is part of what keeps ordinary chatbots
outside the high-risk regime.

4.3 **California test - is it ADMT used for a significant decision?** Does the
technology process personal information and replace, or substantially replace, human
decisionmaking - the output is used without meaningful human involvement - in a
decision resulting in the provision or denial of financial or lending services,
housing, education, employment or compensation, or healthcare services, concerning a
California consumer?

4.4 **The tests diverge by design, not by accident.** A resume-screening model whose
scores a recruiter genuinely reviews may be outside California's ADMT article (a
human decides) and still inside Colorado's Act (the score is a substantial factor).
Both determinations are made by the privacy lead, in writing, per system, and both
reopen when a vendor adds capability, the use changes, or the human review around the
tool weakens.

4.5 **Human involvement that does not involve a human does not count.** A reviewer
must have the authority, information, and time to reach a different conclusion. A
review that only ratifies the output leaves the tool substantially replacing human
decisionmaking - and pulls it inside the California article it was thought to be
outside.

## 5. Approved tools

5.1 Only AI tools on the [ORGANISATION] Approved AI Tools list may be used with
[ORGANISATION] or personal information.

5.2 A tool is added to the list only after: the two determinations at clause 4;
security and privacy review; a written contract meeting clause 13; and, where a
risk assessment is required under clause 9, that assessment.

5.3 Use of any tool not on the list - including free or personal-account versions of
listed tools - is not permitted for [ORGANISATION] work or data.

5.4 Staff who need a tool that is not listed must request it through [FORM /
CHANNEL]; requests are assessed within [N] business days.

5.5 Staff already using an unapproved tool must disclose this to the policy owner.
Good-faith disclosure will not of itself be treated as a disciplinary matter.

## 6. Levels of use

**Level 1 - Open.** No confidential information and no personal information.
Approved tools.

**Level 2 - Internal.** Internal non-personal information. Approved tools with a
written contract.

**Level 3 - Personal information.** Any personal information. Approved tools,
written contract, the notices at clause 8, and registration in the AI system
inventory.

**Level 4 - Consequential.** AI output that makes, or is a substantial factor in, a
consequential or significant decision about a person - hiring, compensation, credit,
lending, housing, education, healthcare, insurance, essential services. Everything
at Level 3, plus clauses 9 to 12, and approval by the AI Governance Committee.

Where a use sits between two levels, the higher applies. The levels are
[ORGANISATION]'s own classification, not categories defined in law - but the Level 4
boundary is placed where the Colorado and California statutory triggers fire, so
classifying a use also identifies the obligations that attach to it.

## 7. Prohibited by [ORGANISATION]

These are policy prohibitions; where one also tracks a legal duty, that is noted.

7.1 Entering customer, employee, or candidate personal information into any tool not
on the approved list.

7.2 Entering credentials, keys, secrets, or security configuration into any AI tool.

7.3 Using AI output as the sole basis for a Level 4 decision without the human
determination at clause 11 - which, for California consumers, is also what keeps a
tool outside the ADMT article's opt-out and access machinery.

7.4 Deploying a high-risk AI system for Colorado consumers without the risk program,
impact assessment, and notices at clauses 9 and 10.

7.5 Using AI to generate content presented as the work of a named individual without
that person's agreement, or to imitate a real person's voice, likeness or signature.

7.6 Using AI to covertly monitor, profile or score employees. Automated inference
about employees' or applicants' performance, health, or reliability from systematic
observation is separately a risk-assessment trigger in California - it is not a quiet
zone.

7.7 Removing, weakening, or failing to enforce the content rules in this policy for
any natural-language system relied on as excluded under clause 4.2 - the exclusion
exists only while the policy is enforced.

7.8 Using AI to produce material that is unlawful, defamatory, harassing, or
discriminatory.

No exception may be granted against 7.4 or 7.7.

## 8. Personal information

8.1 Personal information may be put into an AI tool only at Level 3 or 4, only with
an approved tool, and only consistent with the notices given at collection. Feeding
information collected for one purpose into an AI system serving an incompatible
purpose fails the reasonable-expectations restriction in the California regulations
and is not permitted anywhere.

8.2 **Notice comes first.** Where personal information will be processed by ADMT for
a significant decision, California requires a pre-use notice - prominently, before
the processing, covering the use and the consumer's rights to opt out and to access.
Where information already collected will be newly processed by ADMT, notice precedes
the new processing.

8.3 The following are treated as high-sensitivity and must not be placed in any AI
tool without the privacy lead's written approval: financial account and payment
information; government identifiers; health information; information about children;
biometric information; precise geolocation; and any category [ORGANISATION]
classifies as sensitive. Sensitive personal information is separately a
risk-assessment trigger in California.

8.4 Minimisation applies at Level 3 and 4: the smallest amount of personal
information that serves the purpose, de-identified where the purpose survives
de-identification.

8.5 **Training is its own decision.** Personal information may not be used to train
an AI system - [ORGANISATION]'s or a supplier's - without the privacy lead's written
approval. In California, intending to train ADMT for significant decisions, or
identity-verifying or biometric-profiling technology, on personal information is a
risk-assessment trigger in itself. Suppliers that train on input do not receive
personal information.

## 9. Risk assessments and impact assessments

**The two regimes each require an assessment, and one document can serve both -
Colorado accepts an assessment prepared for another law if reasonably similar in
scope and effect. [ORGANISATION] therefore maintains a single assessment format that
satisfies the stricter content list, recorded per system in the assessment register.**

9.1 **When.** Before initiating: any use of ADMT for a significant decision; any
deployment of a Colorado high-risk AI system; processing of sensitive personal
information; selling or sharing personal information; automated workplace or
educational inference from systematic observation; and training uses at 8.5. The
assessment precedes the processing - a record created afterwards is remediation.

9.2 **What.** The assessment covers, at minimum: purpose, intended use cases and
deployment context; the categories of data in and outputs out; known or reasonably
foreseeable risks of algorithmic discrimination and the steps taken to mitigate
them; customisation data; performance metrics and known limitations; transparency
measures; and post-deployment monitoring and safeguards.

9.3 **Cadence.** Reviewed at least annually for deployed high-risk systems, within
ninety days after any intentional and substantial modification, and at least every
three years for California risk assessments. Records are retained at least three
years after final deployment.

9.4 **Submission is real.** California risk-assessment information is submitted to
the regulator on the prescribed schedule, and Colorado's attorney general may demand
the risk program, impact assessment, and records on ninety days' notice - with
trade-secret designation and privilege protection available. Assessments are written
knowing a regulator may read them.

9.5 The risk management program that frames these assessments follows the NIST AI
Risk Management Framework's four functions - govern, map, measure, manage -
proportionate to [ORGANISATION]'s size, the systems' scope, and the data's
sensitivity, per clause 1.3.

## 10. Consumer notices and adverse decisions

10.1 **Before the decision:** where a high-risk AI system makes or substantially
factors into a consequential decision about a Colorado consumer, the consumer is
notified before the decision, given a plain-language description of the system and
its purpose, and told how to access the public statement at 10.4.

10.2 **After an adverse decision:** the consumer receives the principal reasons -
including the degree and manner of the AI system's contribution, the type of data
processed, and its sources - an opportunity to correct incorrect personal data the
system processed, and an opportunity to appeal with human review where technically
feasible. Where the decision uses consumer-report information, the federal adverse
action duties apply in parallel.

10.3 **Opt-outs:** where required, consumers are informed of the right to opt out of
profiling in furtherance of significant decisions; California consumers receive the
ADMT opt-out and access rights in the regulations, operated through the methods in
clause 12.

10.4 **The public statement:** [ORGANISATION] publishes and periodically updates a
website statement summarising the types of high-risk AI systems it deploys, how it
manages the discrimination risks, and the nature, source, and extent of the
information used. Where [ORGANISATION] develops such systems for others, the
developer statement and documentation duties apply too.

10.5 All notices are direct, in plain language, in the languages [ORGANISATION]
ordinarily uses with its consumers, and accessible to consumers with disabilities.

## 11. Human determination

11.1 No Level 4 decision is made solely by an AI system. A named person reviews the
output, has the authority, information, and time to reach a different conclusion,
and records the determination as their own.

11.2 A review that only ratifies the output is not a review - and under the
California definition it is not human involvement at all (clause 4.5).

11.3 For each Level 4 use, [ORGANISATION] records before deployment: the decision
the system informs; the data it uses; tested performance and known limitations; the
groups on which performance was checked; the point of human determination; and the
appeal route.

## 12. Individuals' requests

12.1 [ORGANISATION] maintains a documented route by which access, deletion,
correction, and opt-out requests reach every AI tool in the inventory, including
prompts, uploads, transcripts, embeddings, caches, and logs. A tool from which
personal information cannot be retrieved on request is not approved for personal
information.

12.2 California consumers' requests to access ADMT, to opt out of ADMT, and the
CCPA's access, deletion, and correction rights are executed through the methods and
timelines in the regulations, owned by the privacy lead.

12.3 Corrections propagate: corrected data goes to the AI suppliers holding it, and
where an adverse Colorado decision rested on incorrect data, the correction
opportunity at 10.2 is honoured through the same route.

## 13. Suppliers

13.1 No AI service is procured or renewed without security and privacy review and a
written contract. Service-provider and contractor contracts satisfy the California
contract requirements; supplier flow-down covers sub-processors.

13.2 AI-specific terms: no use of [ORGANISATION] data to train supplier models
without express approval; disclosure of material model and capability changes -
which reopen the clause 4 determinations; disclosure of processing and storage
locations; developer documentation sufficient to complete the impact assessment at
clause 9 (model cards, dataset cards, known limitations, discrimination testing);
breach notification without undue delay; assistance with individuals' requests; and
exit arrangements.

13.3 Where [ORGANISATION] procures a high-risk system, it obtains and retains the
Colorado developer documentation; where the developer withholds it, the deployment
is not approved.

13.4 Where [ORGANISATION] develops or intentionally and substantially modifies an AI
system made available to others, it holds the developer duties - documentation,
website statement, and the ninety-day discrimination notice - and the committee
records the role per system.

## 14. Discrimination monitoring and the ninety-day clock

14.1 Deployed high-risk systems are reviewed at least annually to ensure they are
not causing algorithmic discrimination, and Level 4 systems are tested before
deployment and at least annually for disparate outcomes across the groups relevant
to the decision.

14.2 **Discovery starts a statutory clock.** If [ORGANISATION] discovers that a
deployed high-risk system has caused algorithmic discrimination, it must notify the
Colorado attorney general within ninety days, in the prescribed form. Suspected
discrimination is therefore escalated to the privacy lead and committee immediately
on suspicion - the clock is too short to absorb internal delay.

14.3 Where a difference in outcomes is found and cannot be justified, the system is
not deployed, or is withdrawn.

14.4 The affirmative-defense architecture at clause 1.3 rewards exactly this:
discovering and curing violations through feedback, red-teaming, or internal review,
while complying with the named frameworks. The monitoring in this clause is that
mechanism, operated deliberately.

## 15. AI interaction disclosure

15.1 Any AI system intended to interact with consumers discloses that the consumer
is interacting with an AI system, unless that would be obvious to a reasonable
person. The obviousness exception is applied by the privacy lead per system, not
assumed by the deploying team.

15.2 A route to a human is available and is not made deliberately difficult to find.

15.3 What a customer-facing system may commit [ORGANISATION] to is bounded and
documented.

## 16. Security

16.1 AI tools are accessed through [ORGANISATION] accounts with single sign-on and
multi-factor authentication. Personal accounts must not be used for [ORGANISATION]
work.

16.2 Access to AI tools handling personal information is granted on least privilege
and reviewed [quarterly]. Leavers are removed on the day of departure.

16.3 Content received from outside the organisation is treated as untrusted input
when placed in front of an AI system, including any instruction embedded within it.

16.4 Where [ORGANISATION] is a financial institution under the safeguards rule, its
information security program covers AI tools handling customer information; where
California's cybersecurity audit thresholds are met, AI systems are within the audit
scope. Security obligations for other organisations are [ORGANISATION] house
standards informed by the same controls.

## 17. Breach and incidents

17.1 Any suspected breach involving an AI tool - a wrong recipient, an unapproved
tool, an exposed prompt log, a misconfigured index, a supplier notification - is
reported to [SECURITY CONTACT] and the privacy lead immediately on suspicion.

17.2 **This set does not state breach-notification deadlines.** The state breach
notification statutes are not held in this corpus, and the sectoral rules carry
their own duties. The privacy lead maintains the current statement of the
notification obligations for each state and sector [ORGANISATION] operates in, and
the incident process names, for every incident, which obligations were assessed.

17.3 Staff who report in good faith will not face disciplinary action for reporting.

## 18. Verification of output

18.1 AI output is a draft. The person who uses it is accountable for it.

18.2 Any factual claim, figure, calculation, date, quotation, citation, or legal
reference taken from AI output and relied on externally, or in a decision, must be
verified against a primary source before use.

18.3 Code generated by AI is reviewed before merge, with attention to secrets,
licence terms, and dependencies the model has introduced.

18.4 AI-generated citations are verified to exist and to say what they are said to
say.

18.5 Public statements about what an AI product or feature can do are reviewed
before publication - overstating AI capability is the classic deception theory, and
it requires no AI-specific statute.

## 19. Intellectual property and records

19.1 AI-generated material used externally is reviewed for third-party rights before
publication.

19.2 [ORGANISATION] material must not be placed in tools whose terms grant the
supplier rights over input or output beyond what the approval accepted.

19.3 Records supporting compliance - the two determinations, risk assessments and
impact assessments, notices, verification records, supplier documentation, and the
public statement's versions - are retained for [PERIOD], and at least three years
for impact assessments after final deployment, and are producible on request,
including to a regulator.

## 20. Employment uses

20.1 AI used in recruitment, performance management, workforce analytics,
compensation, or termination decisions is Level 4. For Colorado employees and
candidates it engages the consequential-decision machinery in full; for California,
employment decisions are significant decisions under the ADMT article, and
systematic-observation inference about workers is a risk-assessment trigger.

20.2 Jurisdictions not held in this corpus impose further duties on AI in hiring -
they are named in the README as not held, and an organisation hiring in them must
obtain those instruments before relying on this clause.

## 21. Responsibilities

**All staff** - use approved tools only; apply the correct level; verify output;
report suspected incidents immediately.

**Managers** - ensure their teams know this policy; escalate Level 4 uses.

**Business owners of AI systems** - the inventory record, the two determinations'
inputs, the assessments, the supplier relationship, the notices in operation.

**Privacy lead** - the determinations at clauses 3 and 4, assessments, notices,
individuals' requests, regulator submissions, the ninety-day clock, and the current
statement of breach obligations.

**Policy owner** - the approved tools list, security review, exceptions, and this
policy.

**AI Governance Committee** - Level 4 approvals, the risk program, exceptions,
metrics, and regulatory change.

## 22. What this policy does not state, and why

22.1 It does not state the law of any state other than California and Colorado. The
state AI and privacy statutes multiplying elsewhere - including in employment and
biometrics - are not held, and nothing here reflects them.

22.2 It does not state breach-notification deadlines (clause 17.2).

22.3 It does not state the health, children's, credit, or financial-institution
rules beyond the points cited in the research note - those regimes govern
[ORGANISATION]'s sector directly and their own compliance programs apply.

22.4 It does not state any federal AI statute, because none is held and none is
asserted. Executive branch AI policy shifts with administrations and is not law of
general application; nothing here rests on it.

22.5 Every obligation stated here resolves to a provision in the research note,
verified against the held texts, with the verification dates recorded.

## 23. Knowledge, skills and acknowledgement

23.1 Staff who use AI tools with personal information complete training covering
this policy, the two determinations (clause 4), and the notice duties (clauses 8
and 10), before access is granted and at least [annually] thereafter.

23.2 Staff who make or inform Level 4 decisions complete additional training on the
limits of AI output and the human determination at clause 11.

23.3 Staff acknowledge this policy on joining, on material revision, and at least
annually.

23.4 Questions go to [CONTACT]. Asking before acting is always acceptable.

---

**Version history:**
1.0 - initial policy, published 3 September 2026; verified within its stated
scope (federal sectoral baseline + California + Colorado) per the research note
and source register.

---

*This document is an educational policy template and does not constitute legal
advice. It reflects obligations under the United States instruments set out in the
accompanying research note, applies only within the scope stated in clause 1.1, and
must be reviewed by the privacy lead or qualified legal counsel before adoption.*
