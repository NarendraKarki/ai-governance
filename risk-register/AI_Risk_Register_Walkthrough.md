# AI Risk Registers and Model Inventories - a walkthrough, with a retail group as the worked example

**Part 4 of the AI Governance Series.** Version 1.0. EU AI Act positions verified against the consolidated text of 27 July 2026 on 18 September 2026; NIST AI RMF 1.0 positions verified against the held primary PDF on 21 September 2026 (research note and source register).

Educational material, not legal advice. The worked example uses a synthetic organisation; nothing in it describes a real company.

---

## 1. What this is

A method for building the two records that every other AI governance control depends on: an **inventory** of the AI systems an organisation uses, and a **risk register** that says what could go wrong with each of them, how badly, and who owns the answer. It is written for the people who have to build and keep these records - governance, risk, security, privacy, model risk and internal audit - and for the executives who will be asked to sign them.

The two records are usually built as one spreadsheet, and that is the first mistake this walkthrough sets out to prevent. An inventory is a record of fact: what exists, who provides it, what it does, where it runs, which law reaches it. Its test is completeness. A risk register is a record of judgement: what harm each system could cause, to whom, how likely, and what has been decided about it. Its test is honesty. Combined into one sheet, the judgement collapses into the fact-keeping and the result is a familiar document: forty rows, every risk "medium", every owner "IT", every review date the same. That document satisfies a checklist and controls nothing.

The worked example is a retail and e-commerce group with six AI systems, headquartered in the UK with stores across the Gulf, India, Singapore and Australia and a subsidiary in the EU. Retail is the right example for three reasons: its AI portfolio is ordinary (a chatbot, a hiring tool, fraud detection, forecasting, pricing, staff scheduling) and so is most organisations'; the same portfolio spans every tier of the EU AI Act, from a system with no duties to two that are listed as high-risk; and a group that operates across jurisdictions has to answer, for each system, which law reaches it and in what role - which is the question most inventories never ask.

Everything in the example is supplied in full, as one Excel workbook: the inventory and the register, with blank templates of both.

## 2. Two records, not one

**The inventory answers "what do we have".** One row per AI system in a use. The same model used for two purposes is two rows, because obligations attach to the intended purpose, not to the technology: a language model that answers customer questions and the same model repurposed to rank job applicants are, in law, two different systems with two different sets of duties. The inventory records, for each row, the facts that decide which duties apply: what the system does and for whom; whether the organisation built it, bought it, or bought it and changed it; where it is used and whose decisions its output feeds; what data goes in; and its status (in use, in trial, retired). Those facts are the inputs to classification, and classification is the input to everything else.

**The register answers "what could go wrong".** One row per risk, not per system. A system may carry five risks or one. A risk is a statement of the form "if [cause], then [event], and [harm] to [whom]", with a rating, an owner, a decision, and a trigger for looking again. The register is where judgement lives, and judgement has to be traceable: who rated it, when, on what basis, and what they decided.

The two records are linked by the system identifier and nothing else. The inventory feeds the register (a new row in the inventory raises the question of what its risks are) and the register feeds back (a risk rated unacceptable changes a system's status). But they have different owners, different review cycles and different tests of quality, and they are kept apart so that each can be judged by its own test.

## 3. What each record is for in law

The inventory and the register are not themselves named in most legislation, but the things they contain are. Stated as rules, with the provisions in the research note:

- The EU AI Act reaches an organisation in one of two **roles**, and the duties differ by role. A **provider** develops a system, or has it developed, and places it on the market or puts it into service under its own name. A **deployer** uses a system under its own authority. An organisation can be both, and a deployer becomes a provider - and inherits the provider's duties - if it puts its own name on a high-risk system, substantially modifies one, or changes the intended purpose of a system so that it becomes high-risk. The inventory has to record the role for each system, because it decides which column of obligations applies.
- The Act reaches organisations outside the EU in two ways: a provider anywhere that places a system on the EU market, and a provider or deployer anywhere whose system's **output is used in the EU**. A group headquartered outside the EU that runs one system for the whole group, including an EU subsidiary, is a deployer within scope for that system. The inventory has to record where each system's output is used, not just where the servers are.
- Obligations depend on **classification**: prohibited practices, high-risk systems (listed by use in Annex III, or safety components of regulated products), systems with transparency duties (those that interact with people, generate synthetic content, or recognise emotions), and everything else. A provider that concludes an Annex III system is not high-risk under the derogation must document that assessment before putting the system into service and register the system in the EU database - unless the system profiles natural persons, in which case it is always high-risk. The inventory has to carry the classification, the basis for it, and the date the duties bind: high-risk duties for Annex III systems bind from 2 December 2027, a deferral and not an exemption, while the transparency duties have applied since 2 August 2026 and the AI-literacy duty on all providers and deployers since 2 February 2025.
- For a high-risk system, the provider must run a **risk management system**: a continuous, iterative process over the whole lifecycle that identifies and analyses the known and reasonably foreseeable risks to health, safety and fundamental rights, estimates and evaluates them including under reasonably foreseeable misuse, evaluates other risks emerging from post-market data, and adopts targeted measures so that each residual risk and the overall residual risk is judged acceptable. The Act defines risk as the combination of the probability of an occurrence of harm and the severity of that harm. The register is that process, written down.
- The provider's **quality management system** must include the risk management system, a post-market monitoring system, serious-incident reporting procedures, record-keeping for all relevant documentation, and an accountability framework setting out the responsibilities of management and staff. The register's owner column and review cycle are that accountability framework in practice.
- A **deployer** of a high-risk system must use it in accordance with the instructions for use, assign human oversight to people with the competence and authority to exercise it, ensure input data under its control is relevant and representative, monitor operation and inform the provider and the authority if the system presents a risk, keep the logs for at least six months, inform workers' representatives before using a high-risk system in the workplace, and inform the people subject to decisions it makes or assists. Each of those is a row in the register with an owner.
- A **serious incident** is one that leads, directly or indirectly, to death or serious harm to health, serious and irreversible disruption of critical infrastructure, an infringement of Union-law obligations protecting fundamental rights, or serious harm to property or the environment. The provider must report it to the market surveillance authority within 15 days of becoming aware (two days for widespread infringement or critical-infrastructure disruption, ten days for a death), and a deployer that identifies one must inform the provider immediately. The register's severity scale has to put these outcomes at the top, because the law attaches a clock to them.
- Providers of Annex III high-risk systems must **register** themselves and the system in the EU database before placing it on the market, with the information listed in Annex VIII: provider identity, the system's trade name and a unique reference, its intended purpose and the functions it supports, a concise description of the data it uses and its operating logic, its status, the Member States where it is available, and the instructions for use. That list is, in effect, the minimum inventory record the law expects a provider to be able to produce for a high-risk system.
- Outside the AI Act, the closest legal analogue to an inventory is the GDPR's **record of processing activities**, which most organisations already keep: the purposes of processing, the categories of data subjects and data, the recipients, transfers, retention and security measures. Every AI system that processes personal data is already, or should be, a row in that record. The AI inventory should link to it rather than duplicate it.
- The NIST AI Risk Management Framework, which is voluntary and non-sector-specific, says the same thing in different words: mechanisms are in place to inventory AI systems and are resourced according to organisational risk priorities; organisational risk tolerances are determined and documented; treatment of documented risks is prioritised by impact, likelihood and available resources; responses (mitigate, transfer, avoid, accept) are planned and documented; and post-deployment monitoring, decommissioning, incident response and change management are in place. The walkthrough's eight steps are a way of doing those things; the research note maps each step to the framework's subcategories.
- ISO/IEC 42001 is the management-system standard for AI. It is a paid standard and is not held for this artifact, so nothing in this walkthrough asserts what it requires. Organisations certifying to it will find that the inventory and register here are the evidence its risk-assessment and risk-treatment clauses call for; the mapping is left to them.

## 4. Where inventories fail

Inventories fail on completeness, and completeness fails for predictable reasons. Five, each with its own discovery source in step 2:

1. **Nobody bought it.** AI arrived inside software the organisation already had. The CRM added lead scoring; the help desk added a summariser; the office suite added a writing assistant; the recruitment platform added candidate ranking. No procurement event, no security review, no inventory row. The discovery source is vendor release notes and the organisation's own SaaS administration consoles, read for features switched on by default.
2. **It is not called AI.** A forecasting model in a spreadsheet, a rules engine with a learned component, a "scoring" service, an "optimiser". The inventory's definition of an AI system has to be the legal one - a machine-based system that infers from inputs how to generate outputs such as predictions, recommendations or decisions - applied by someone who reads the description of what the thing does, not its name.
3. **It is someone's experiment.** A data scientist's notebook that became a nightly job; a marketing team's trial of a personalisation tool that never ended. The discovery source is the expense system, the identity provider's log of applications signed into, and the data platform's scheduled jobs.
4. **It is the vendor's model, so it is the vendor's problem.** The organisation is the deployer, and the deployer's duties are its own. Worse, if the organisation has tuned, wrapped or repurposed the vendor's system, it may have become the provider without noticing. The inventory's role column exists to force that question.
5. **It was in the inventory, once.** The system was retrained, the vendor pushed a new model, the use expanded to a new country, the population it is used on changed. The row was not updated because nothing told the inventory owner. Step 8's triggers are the fix: the inventory is updated on events, not on a calendar.

## 5. Where registers fail

Registers fail on honesty, and the failure has a recognisable shape.

**Everything is medium.** A 3x3 scale with no words attached to the numbers produces a register where every cell is 2x2, because 2 is the rating that requires no justification. The fix is definitional: each severity level and each likelihood level is defined in a sentence with an example, the top severity level is anchored to the outcomes the law calls a serious incident, and the definitions are published with the register so that a rating can be challenged.

**The risk is a category, not a statement.** "Risk: bias." "Risk: data privacy." "Risk: hallucination." A category cannot be rated, owned or closed. A risk is a statement: if the CV screening tool's training data reflects the historical gender balance of the sales function, then it will rank women lower for sales roles, and qualified candidates will be rejected without a human ever seeing their application. That can be rated, an owner can be named, and a test can be designed to see whether it is happening.

**Harm to the organisation and harm to people are mixed.** A register built by the risk function rates financial and reputational impact; a register built by compliance rates legal exposure; neither rates harm to the person the system makes a decision about. The law's risk management duty is about health, safety and fundamental rights - harm to people - and the serious-incident clock runs on harm to people. The register needs both, in separate columns, so that a risk which is low for the organisation and high for the individual (a wrongly rejected candidate; a customer wrongly flagged as a fraudster) is not rated away.

**The owner is a department.** "Owner: IT." "Owner: HR." A department cannot decide to accept a risk, cannot be asked why it did, and cannot be found a year later. The owner is a named role with the authority to make the decision the register records - to accept the residual risk, to fund the mitigation, to stop the system - and the register says which of those decisions was made and when.

**It was written once.** The register was built for an audit and has the same date on every row. A register is a control only if it changes when the world changes: the same triggers that update the inventory (step 8) re-open the register entries for that system.

## 6. The protocol

Eight steps. Steps 1 to 3 build the inventory; 4 to 7 build the register; 8 keeps both alive. The order matters because the register cannot be built for systems the inventory has not found, and the register's ratings depend on the classification the inventory records.

### Step 1 - define the unit, the fields and the scales

Before collecting anything, fix three things in writing.

**The unit of the inventory** is an AI system in a use. Write the definition of "AI system" the inventory will apply (the walkthrough uses the EU AI Act's) and the rule for splitting: one row per intended purpose, so that a system used for two purposes has two rows that share a technical reference.

**The fields.** The inventory needs, at minimum: identifier; name; what it does, in one sentence a lay reader would understand; the decision or output it produces and who acts on it; whether the organisation is provider, deployer or both, and why; the supplier, if any, and the contract reference; where it is used and where its output is used, by country; the categories of people it makes or shapes decisions about; the categories of data it uses, with a link to the record of processing; its classification under each law that reaches it, the basis for the classification, and the date each set of duties binds; its status; the business owner; the technical owner; and the date the row was last verified and by whom. Section 9 has the template.

**The scales.** Severity and likelihood, each defined level by level in words. The walkthrough uses four levels of each, and separates severity to people from severity to the organisation. The top level of severity to people is defined by the serious-incident outcomes, so that any risk rated there is understood to carry a statutory reporting clock if it materialises. The scales are the organisation's own choice - the point is that the words are written down and published with the register, not that four is the right number.

### Step 2 - discover

Run the five discovery sources from section 4, and record which source found each system, because the sources that find the most are the ones to automate:

| Source | What it finds | How |
|---|---|---|
| Procurement and contracts | Systems that were bought as AI | Contract register searched for AI, model, machine learning, automated decision, and the names of known AI vendors |
| SaaS administration consoles and vendor release notes | AI features switched on inside existing software | Each admin console reviewed for AI features and their default state; vendor release notes for the last 24 months |
| Identity provider and expense system | Trials, experiments and shadow tools | Applications signed into via single sign-on; card and expense transactions to AI vendors |
| Data platform and scheduled jobs | In-house models in production | Every scheduled job that loads a model artefact or calls a model endpoint |
| The people | Everything else | A short questionnaire to every function head: what decisions in your area are made or shaped by software that learns from data? |

A system found by only one source is a system that will be lost when that source is not checked. The inventory records the finding source so that the next sweep knows where to look.

### Step 3 - record each system: role, reach, classification

For each system found, fill the inventory row, and take three of the fields seriously because they decide everything downstream.

**Role.** Built in-house and used in-house: provider and deployer. Bought and used as supplied: deployer. Bought and changed: the change is examined against the three tests that turn a deployer into a provider - own name on a high-risk system, substantial modification of a high-risk system, or a change of intended purpose that makes a system high-risk. Record the answer and the reasoning. The organisation that tunes a vendor's general-purpose model into a candidate-ranking tool has become the provider of a high-risk system.

**Reach.** For each country the organisation operates in: is the system used there, and is its output used there? A group-wide system run from headquarters whose output is acted on by an EU subsidiary is in the EU AI Act's scope as a deployer for that subsidiary's use. Record the countries, and against each the law that applies and the organisation's role under it. The Part 1 acceptable use policies carry the per-jurisdiction rules; the inventory row points to them.

**Classification.** Under each law that reaches the system, the tier and its basis. For the EU AI Act: prohibited, high-risk (the Annex III point or the Annex I product), transparency-duty (which paragraph), or none; whether the derogation from high-risk was considered, and if claimed, the documented assessment and the database registration it requires; and the date the duties bind. Where a system's use differs by country, the classification may differ by country - a staff scheduling tool that allocates shifts on individual performance is high-risk where EU workers are subject to it and unlisted elsewhere - and the row records both.

### Step 4 - identify the risks, harm first

For each system, write the risk statements. Start from harm, not from technology: who could be harmed by this system, and how? Work through the categories of people the inventory row lists (customers, candidates, employees, the public) and, for each, the ways the system could harm them - a wrong decision, an unfair decision, a decision they cannot contest, a disclosure of their data, a manipulation, an injury. Then work through the organisation's own exposures: legal, financial, operational, reputational. Then the causes: for each harm, what in the data, the model, the vendor, the integration, the operation or the people around the system could produce it - including the ways the system itself can be attacked. Data poisoning, model poisoning, adversarial inputs, prompt injection and confidentiality attacks are causes, and they belong on this register as the "if" of a statement whose consequence is rated for people and for the organisation. A clean penetration test or red-team report is an existing control that lowers likelihood; it is not a reason to leave the row out, and it does not rate the consequence.

Each risk is one row, in the form: **if** [cause], **then** [event], **harm** [what, to whom]. A system with no plausible harm to people gets a short entry, not a long one; the register is not improved by padding.

Two risks belong on every deployer's register for every vendor-supplied system, because they are the ones inventories miss: **role drift** (the organisation changes or repurposes the system and becomes its provider without adopting the provider's duties) and **silent change** (the vendor updates the model and the organisation's classification, testing and instructions for use are now for a system that no longer exists).

### Step 5 - rate, with the published scales

For each risk: severity to people, severity to the organisation, likelihood, each on the step 1 scale, each with a one-line justification. Then existing controls - what is already in place that reduces likelihood or severity - and the residual rating with those controls counted. The justification is the part that makes the rating challengeable; a number without a sentence is a number nobody can argue with, which is the same as a number nobody believes.

Ratings are made by the people who understand the system and the harm together: the business owner, the technical owner, and whoever speaks for the people affected (privacy, legal, HR for employees). A rating made by one function alone is recorded as provisional.

### Step 6 - decide, and name who decided

For each risk, one of four decisions, recorded with the name and role of the person who made it and the date: **mitigate** (a named control will be added, with an owner and a date); **accept** (the residual risk is judged acceptable at this level, by someone with the authority to say so); **transfer** (contractually or by insurance, with the reference); **avoid** (the system, or the use, is stopped or not started). A risk rated at the top severity level for people cannot be accepted below a stated level of authority - the worked example reserves it to the Chief Risk Officer.

The decision is not the end of the row. A mitigation has a completion date, and until it is complete the risk sits at its pre-mitigation rating.

### Step 7 - set the indicator and the trigger

For each risk rated above the lowest level: what would show it is materialising, and where would that show up? An indicator is a measure that is already collected or can be (complaint volumes by category, override rates, drift metrics, vendor incident notices, model performance by group), a threshold on it, and the person who watches it. A risk with no indicator is a risk the organisation has decided not to notice, and the register should say so in those words.

### Step 8 - review on triggers, and retire

The inventory and the register are updated when any of these happens, and the event is recorded against the rows it touched: a new system or use; a retrain or a vendor model update; a change in the countries where the system or its output is used; a change in the population it is used on; a change in the law or in guidance; an incident, a complaint pattern, or an indicator crossing its threshold; and a system's retirement. Retirement is a step, not a deletion: the row's status changes, the date and reason are recorded, the data and logs are handled according to their retention rules, and the register's risks for that system are closed with the closure recorded. A calendar review - the walkthrough's example uses quarterly for high-risk systems and annually for the rest - is the backstop, not the mechanism.

## 7. The worked example - a synthetic retail group

The full inventory and register are in the companion `AI_Risk_Register_Worked_Example.md` and the Excel workbook. The shape:

**The organisation.** Marsa Retail Group (synthetic): a UK-headquartered retail and e-commerce group with stores in the UK, the Gulf, India, Singapore and Australia, and a subsidiary established in the EU. Six AI systems.

**What the discovery sweep found.** Procurement found two (the chatbot platform and the HR screening tool). The SaaS console sweep found one the group had not thought of as AI: the workforce management suite's shift optimiser, switched on by a vendor update fourteen months earlier and used by every store manager since. The data platform found two in-house models (fraud detection and demand forecasting). The function-head questionnaire found the sixth: a personalisation and promotions engine run by marketing under a contract nobody in procurement had classed as AI.

**Role and reach.** Four systems are vendor-supplied and used as supplied: deployer. Two are built in-house: provider and deployer. The CV screener is used for all group hiring, including the EU subsidiary's, so the group is a deployer within the EU AI Act's scope for that use. The shift optimiser is used in every store, including the EU subsidiary's; its output - who works when, allocated partly on individual performance - is used in the EU. The chatbot serves customers in both regions.

**Classification.** Two systems are Annex III high-risk in respect of their EU use: the CV screener (recruitment and selection - analysing and filtering applications) and the shift optimiser (allocating tasks based on individual behaviour, performance or characteristics). Duties bind from 2 December 2027. The derogation was considered for both and rejected: both profile natural persons, so it is unavailable. The chatbot carries the transparency duty, in force since 2 August 2026. The fraud model, the forecaster and the pricing engine are unlisted under the AI Act; the fraud model and the pricing engine carry data protection duties on profiling and automated decisions, which the register records under the Part 1 policies rather than here.

**The register's shape.** Twenty-four risks across six systems. Severity to people: three at the top level, all on the two high-risk systems; eight at the second; thirteen at the bottom two. Two rows are AI-specific security risks - prompt injection on the assistant, threshold probing of the fraud model - written as harm statements with the vendor's clean red-team result recorded as an existing control, not as a reason to omit them. The forecaster carries one risk with no harm to people at all, and the register says so in a line rather than inventing one. The two systems with the highest severity to people - the hiring tool and the shift optimiser - were the two rated "low" on the risk function's first draft, which scored by contract value; that is the whole reason for separating the columns.

**The finding the register produced.** The shift optimiser had been in use for fourteen months with no inventory row, no classification, no instructions for use on file, no human oversight assignment and no information to workers' representatives. It is a high-risk system in the EU subsidiary from December 2027. The register's first mitigation is to obtain the instructions for use and the provider's registration status from the vendor, assign oversight, and inform the EU works council before the duties bind - and the group's decision on whether to keep the tool in EU stores at all is recorded as pending that.

**The role-drift finding.** The HR team had asked the CV screener's vendor for a feature to rank internal candidates for promotion using the same model. The register's role-drift entry caught it: promotion decisions are a separate Annex III use, and the feature would have been the group's own configuration of the vendor's system for a purpose the vendor had not assessed. The request was withdrawn pending a provider-side assessment.

## 8. Common misreadings

**"We have a list of our AI vendors, so we have an inventory."** A vendor list is a procurement record. It does not know about AI features inside non-AI contracts, in-house models, or what any system is actually used for. Four of the six systems in the worked example are not "AI vendors".

**"It is the vendor's model, so the vendor is responsible."** The vendor is the provider and has the provider's duties. The organisation is the deployer and has the deployer's: use in accordance with the instructions, human oversight, input data, monitoring, logs, informing workers and affected people. Those are not transferable by contract, and the moment the organisation changes the system's purpose it may also be the provider.

**"Our servers are in London, so the EU AI Act does not reach us."** The Act reaches a provider or deployer anywhere whose system's output is used in the Union. Where the servers are is not the test.

**"High-risk duties are deferred to 2027, so nothing needs doing yet."** The transparency and AI-literacy duties already apply. The high-risk duties bind on a date, and the vendor's registration, the instructions for use, the oversight assignment and the workers' information all have to exist by that date, not start on it. The register's mitigation dates are set from the binding date backwards.

**"The risk register is the DPIA."** A data protection impact assessment is one input: it covers processing risk to data subjects for a given processing. The register covers every harm the system can cause, to people and to the organisation, across every jurisdiction, for the life of the system, and it carries the decisions. The DPIA is referenced from the register row, not replaced by it.

**"We rated everything and it is all medium."** Then the scales have no words, or the ratings were made by one function, or the register is padded with risks that are categories rather than statements. Section 5 has the fixes.

## 9. Blank records

### Inventory row

```
AI SYSTEM INVENTORY - ENTRY
Identifier:                          Name:                              Status: [ ] trial [ ] in use [ ] retired
What it does (one sentence):
Output and who acts on it:
Role: [ ] provider [ ] deployer [ ] both     Basis (built / bought / bought and changed - how):
Supplier and contract ref:                   Technical reference (model / version):
Countries where used:                        Countries where output is used:
People it makes or shapes decisions about:
Data used (link to record of processing):
Classification - EU AI Act:  [ ] prohibited [ ] high-risk (Annex III point __ / Annex I) [ ] transparency (Art 50(_)) [ ] none
  Derogation considered: [ ] yes [ ] no   Claimed: [ ] yes (assessment ref __ ; database registration ref __) [ ] no
  Duties bind from:                          Applies-today duties: [ ] AI literacy [ ] transparency [ ] other:
Classification - other laws reaching it (jurisdiction / instrument / tier / Part 1 policy ref):
Business owner (role):                       Technical owner (role):
Found by (discovery source):                 Last verified (date / by):
```

### Register row

```
AI RISK REGISTER - ENTRY
Risk ID:                 System ID:                 Raised (date / by):
Risk statement:  IF                                  THEN                                HARM (what, to whom)
Category of harm to people: [ ] wrong decision [ ] unfair decision [ ] uncontestable decision [ ] data [ ] manipulation [ ] safety [ ] none
Existing controls:
Rating (scale ref __):  Severity to people __   Severity to organisation __   Likelihood __   Residual __
Justification (one line per rating):
Decision: [ ] mitigate [ ] accept [ ] transfer [ ] avoid     By (name, role):            Date:
Mitigation (control / owner / due date):
Indicator (measure / threshold / watched by):
Review triggers (from step 8) and next calendar review:
Status: [ ] open [ ] mitigating [ ] accepted [ ] closed (date / reason)
```

## 10. Limitations

- **One statute stated in full.** Only the EU AI Act's provisions are set out as rules here. The data protection, consumer and employment law that also reach these systems are covered per jurisdiction in the Part 1 policy sets and are pointed to, not restated.
- **ISO/IEC 42001 not held.** The standard is named as the AI management-system standard and no clause content is asserted. The NIST AI RMF is held and hashed (source register).
- **Synthetic organisation.** Six systems, two regions, a simplified group structure. Real portfolios are larger and the reach analysis is harder, particularly where a system is provided by one group company to another.
- **Scales are illustrative.** The four-level scales are one workable choice, not a recommendation; the requirement is that the levels are defined in words and the top level is anchored to statutory outcomes.
- **Not reviewed by counsel.** Educational material, not legal advice.

---

*Part 4 of the AI Governance Series - github.com/NarendraKarki/ai-governance. Educational, not legal advice. Use it, and tell me what to improve.*
