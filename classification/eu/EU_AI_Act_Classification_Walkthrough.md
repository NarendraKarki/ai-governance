# Classifying AI systems by risk - European Union

**AI Governance Series - Part 2**
**Version:** 1.0  **Status:** Verified against the consolidated AI Act of 27 July 2026
**Text basis:** Regulation (EU) 2024/1689 as amended by Regulation (EU) 2026/1744
**Verification date:** 30 August 2026
**Use:** Educational demonstration. Not legal advice. Have counsel review before relying on any classification.

---

## 1. What this walkthrough does

The AI Act does not regulate "AI". It regulates particular AI practices, particular
AI systems, and particular AI models, and it does so in tiers. Everything an
organisation must do under the Act follows from one prior question: **which tier does
this system fall in?** Get that wrong and every downstream control is either missing
or wasted.

This walkthrough takes one system at a time through the tiers in the order the law
requires, states each test as a rule a governance team can apply, and ends with a
classification record. It reads the high-risk list (Annex III) item by item, because
"probably high-risk" is not a classification.

Two facts shape the whole exercise and are easy to get wrong:

- **The tiers are not equally in force.** The prohibitions bind now. The transparency
  duties bind now. The high-risk regime does not bind until 2 December 2027 (for the
  Annex III list) and 2 August 2028 (for products under Annex I). That is a deferral,
  not an exemption: the classification still has to be done now, so that the time is
  used.
- **The tiers stack.** A system can be high-risk and also carry transparency duties.
  A prohibited practice is prohibited whatever else the system is. Classification is
  not a single label; it is a set of findings.

The words "prohibited", "high-risk", "transparency" and "minimal" are used here as
working labels. The Act defines prohibited practices, high-risk systems and the
Article 50 transparency duties directly; "minimal" is simply the remainder, and the
Act attaches no specific duties to it.

## 2. Before the tiers: five gate questions

Do these first. Each one can end the exercise or change its outcome.

### Gate 1 - Is it an AI system at all?

The Act applies to a **machine-based system** that is designed to operate with some
degree of autonomy, that may adapt after deployment, and that **infers from the input
it receives how to generate outputs** (predictions, content, recommendations or
decisions) that can influence physical or virtual environments.

The operative word is **infers**. A system that only executes rules a human wrote in
full, with no inference from input to output, is a weaker candidate. A system that
learns a mapping from data, or that reasons over inputs to choose an output, is a
strong one. When in doubt, treat it as an AI system: the cost of a wrong "not AI"
finding is that no further check is made.

A separate track applies to **general-purpose AI models** (the underlying model,
rather than the system built on it). Model obligations fall on the model provider and
are outside this walkthrough. An organisation that builds a system on someone else's
model is classifying the **system**.

### Gate 2 - Is it within scope?

The Act reaches:

- **providers** placing an AI system on the market or putting it into service in the
  Union, wherever the provider is established;
- **deployers** established or located in the Union;
- providers and deployers in third countries **where the output is used in the
  Union**;
- importers, distributors, product manufacturers placing a system on the market with
  their product, and authorised representatives.

It does **not** reach, in whole or in part:

- systems placed on the market, put into service or used **exclusively** for military,
  defence or national security purposes;
- systems and models developed and put into service **for the sole purpose of
  scientific research and development**;
- **research, testing or development before** a system is placed on the market or put
  into service - but testing in real-world conditions is not covered by this
  exclusion;
- deployers who are natural persons using AI in a **purely personal, non-professional**
  activity;
- systems released under **free and open-source licences**, unless they are placed on
  the market or put into service as high-risk systems or as systems caught by the
  prohibitions or the transparency duties.

The open-source point is the one most often misread. Open-source licensing removes
the general obligations; it does not remove the prohibitions, the transparency
duties, or the high-risk regime if the system is high-risk.

### Gate 3 - Which role does the organisation hold?

Duties differ sharply between the **provider** (develops the system, or has it
developed, and places it on the market or into service under its own name or
trademark) and the **deployer** (uses the system under its own authority, other than
in a personal non-professional activity).

An organisation is a deployer of tools it buys, and a provider of tools it builds or
rebrands. It can become the provider of a high-risk system it did not build if it
puts its name on it, substantially modifies it, or changes its intended purpose so
that it becomes high-risk. Record the role for each system; the classification
record in section 7 has a field for it.

### Gate 4 - What is the intended purpose?

Most tests in this walkthrough turn on **what the system is intended to be used
for**, as the provider has specified it in the instructions, marketing and technical
documentation. Two consequences:

- A deployer who uses a system for something other than its stated intended purpose
  may be changing its classification, and may be becoming its provider.
- A provider who writes a narrow intended purpose does not thereby escape the
  prohibitions, which look at effect and use as well as intent, and must also account
  for **reasonably foreseeable misuse**.

Write the intended purpose down in one sentence before starting. If that sentence
cannot be written, the system is not ready to be classified.

### Gate 5 - Is a product safety regime involved?

If the system is, or is built into, a physical product that is itself regulated by
Union product legislation (toys, lifts, machinery, medical devices, vehicles,
aircraft and so on), the high-risk analysis takes a different route. Note it now;
section 4.1 handles it.

## 3. Tier 1 - Prohibited practices

Check this tier **first**, and check it whatever the answer to the others. A
prohibited practice cannot be cured by a risk assessment, a consent form, a
contract, or a business case. The Act prohibits the **placing on the market, the
putting into service, and the use** of a system for these practices; a deployer is
caught by "use" even where the provider is elsewhere.

**In force since 2 February 2025**, points 1 to 8. **From 2 December 2026**, points 9
and 10.

| # | Prohibited practice, as a rule | Boundary notes |
|---|---|---|
| 1 | Subliminal, manipulative or deceptive techniques that materially distort a person's behaviour by impairing their ability to make an informed decision, causing or likely to cause significant harm | Objective **or** effect is enough. "Significant harm" is the threshold; ordinary persuasion is not caught |
| 2 | Exploiting vulnerabilities of age, disability, or a specific social or economic situation, to materially distort behaviour in a way that causes or is likely to cause significant harm | The vulnerable group is defined by the three named grounds |
| 3 | Social scoring: evaluating or classifying people over time on social behaviour or personal characteristics, where the score leads to detrimental treatment in an unrelated context, or treatment that is unjustified or disproportionate | Both limbs are about the **consequence** of the score, not the scoring alone |
| 4 | Predicting the risk that a person will commit a criminal offence **based solely on** profiling or personality traits | Supporting a human assessment already based on objective, verifiable facts linked to a criminal activity is outside the prohibition |
| 5 | Creating or expanding facial recognition databases by untargeted scraping of facial images from the internet or CCTV | The target is the **database-building**, not facial recognition as such |
| 6 | Inferring the emotions of a person **in the workplace or in education institutions** | The one exception is a system intended for medical or safety reasons. Outside those two settings, emotion recognition is high-risk, not prohibited (section 4.2, area 1) |
| 7 | Biometric categorisation that deduces or infers race, political opinions, trade union membership, religious or philosophical beliefs, sex life or sexual orientation | Labelling or filtering lawfully acquired biometric datasets, and categorisation in law enforcement, are outside the prohibition |
| 8 | Real-time remote biometric identification in publicly accessible spaces **for law enforcement**, outside three narrow authorised objectives and the safeguards that attach to them | Applies to law-enforcement use. A private organisation is not within the exceptions; its real-time identification is governed by area 1 of the high-risk list and by data protection law |
| 9 | Generating or manipulating **realistic** intimate images, video, audio or similar material of an identifiable person, or of an identifiable person in sexually explicit activity, without that person's freely given, specific, informed, unambiguous and explicit consent | From 2 December 2026. See the scoping rules below |
| 10 | Generating or manipulating **child sexual abuse material** or child-abuse performance, except where a "without right" defence applies under national law | From 2 December 2026. See the scoping rules below |

**Scoping rules for points 9 and 10.** For a provider, placing on the market or putting
into service is prohibited only where generating that material is the **intended
purpose**, or where the system's design, training, capabilities or user-facing
features make it a **reasonably foreseeable and reproducible outcome** without
significant technical modification **and** the system lacks reasonable and adequate
safeguards to reliably prevent it and to correct observed or reported misuse. For a
deployer, use is prohibited only where the deployer uses the system **for the purpose
of** generating that material. Manipulation that does not increase the exposure of
intimate parts or alter the nature of depicted sexual activity is not "manipulation"
for point 9.

**What this means for classification.** A general-purpose image generator is not
prohibited by existence. Its provider must be able to show the safeguards; a
deployer who uses it to produce such material commits the prohibited practice
whatever the provider did.

If a system is caught by any point in this table, stop. Record the finding, record
the applicable date, and do not proceed to the other tiers as if the system could be
used on conditions.

## 4. Tier 2 - High-risk

There are exactly two routes into high-risk. A system is high-risk if it satisfies
**either** the product route (4.1) **or** the listed-area route (4.2), subject in the
second case to a narrow derogation (4.3). There is no third route, and there is no
general "high-risk because it is important" test.

### 4.1 Route A - the product route (Annex I)

A system is high-risk under this route only if **both** conditions hold:

- **Condition 1:** the system is intended to be used as a **safety component** of a
  product, or is itself a product, covered by the Union product legislation listed in
  Annex I; **and**
- **Condition 2:** that product is required to undergo a **third-party conformity
  assessment** under that legislation before being placed on the market or put into
  service.

The Omnibus tightened both conditions in the organisation's favour:

- A component is a **safety component** only if its intended purpose is to prevent or
  mitigate risks to health and safety of persons or property, or if its failure or
  malfunction would endanger health and safety.
- Systems used **solely** for non-safety user assistance, performance optimisation,
  service efficiency, automation, convenience or quality control are **not** safety
  components. But a system whose failure would endanger health and safety **is** a
  safety component regardless of that list.
- A product that needs third-party assessment **solely** for reasons other than
  health and safety (the example given is radio-spectrum or electromagnetic
  interference) does **not** satisfy Condition 2.

Annex I has two sections, and the difference matters:

**Section A** (the "New Legislative Framework" instruments): toys; recreational craft
and personal watercraft; lifts and lift safety components; equipment for explosive
atmospheres; radio equipment; pressure equipment; cableway installations; personal
protective equipment; gas appliances; medical devices; in vitro diagnostic medical
devices. Systems high-risk through Section A are subject to the full high-risk
regime, integrated into the product's own conformity assessment. **Machinery is no
longer in Section A**: the Omnibus deleted it from Section A and added the Machinery
Regulation to Section B.

**Section B** (other product legislation): civil aviation security; two- and
three-wheel vehicles and quadricycles; agricultural and forestry vehicles; marine
equipment; rail interoperability; motor vehicles and their trailers; motor vehicle
type-approval as regards general safety; civil aviation; and now machinery. For
systems high-risk through Section B, **only a handful of the Act's provisions apply**
directly (the classification rule itself, the new real-world testing article, and the
amending provisions); the substantive requirements are to be carried into the
sectoral legislation instead.

**Practical consequence.** If Gate 5 was answered "yes", the classification cannot be
finished from the AI Act alone. Whether the product needs third-party conformity
assessment is a question for the product legislation, and this walkthrough does not
hold those instruments (section 11). Record the Annex I instrument, record the
open question, and route the system to the product-compliance function.

**Date.** For systems high-risk under Route A, the high-risk requirements apply from
**2 August 2028**.

### 4.2 Route B - the listed areas (Annex III), read item by item

A system is high-risk under this route if it is an AI system **listed in Annex III**.
The list is closed: eight areas, each with named use cases. A system in the same
general field as a listed use case, but not matching one of them, is **not** high-risk
under this route. Read the sub-points, not the headings.

The tables below restate each item as a rule. The right-hand column records what the
item does **not** cover, taken from the text itself.

**Area 1 - Biometrics** (only in so far as the use is permitted by Union or national law)

| Item | Rule | Not covered |
|---|---|---|
| 1(a) | **Remote biometric identification** systems: identifying people, without their active involvement and typically at a distance, by comparing their biometric data against a reference database | **Biometric verification** whose sole purpose is to confirm that a specific person is who they claim to be (one-to-one matching, including authentication) |
| 1(b) | Biometric categorisation according to **sensitive or protected** attributes, based on inferring those attributes | Categorisation that infers the characteristics listed in prohibited practice 7 is **prohibited**, not high-risk. Categorisation ancillary to another commercial service and strictly necessary for technical reasons is outside the definition |
| 1(c) | **Emotion recognition**: identifying or inferring emotions or intentions from biometric data | In the workplace or education institutions this is **prohibited** (point 6). High-risk applies to every other setting |

**Area 2 - Critical infrastructure**

| Item | Rule | Not covered |
|---|---|---|
| 2 | Safety components in the management and operation of **critical digital infrastructure, road traffic, or the supply of water, gas, heating or electricity** | The term is "safety components": a system used for billing, forecasting or customer service in these sectors is not within area 2. Area 2 systems are exempt from the EU database registration and from the fundamental rights impact assessment |

**Area 3 - Education and vocational training** (institutions at all levels)

| Item | Rule | Not covered |
|---|---|---|
| 3(a) | Determining **access or admission**, or assigning people to educational or vocational training institutions | Course-content recommendation inside an institution, unless it determines access or assignment |
| 3(b) | **Evaluating learning outcomes**, including where those outcomes steer the learning process | Nothing is carved out; automated grading that feeds an adaptive pathway is squarely within |
| 3(c) | Assessing the **appropriate level of education** a person will receive or can access | - |
| 3(d) | **Monitoring and detecting prohibited behaviour during tests** (proctoring) | - |

**Area 4 - Employment, workers' management and access to self-employment**

| Item | Rule | Not covered |
|---|---|---|
| 4(a) | **Recruitment or selection**: in particular, placing targeted job advertisements, analysing and filtering applications, and evaluating candidates | The list is illustrative ("in particular"); any recruitment or selection use is within |
| 4(b) | Decisions affecting the **terms of work relationships, promotion or termination**; **allocating tasks** based on individual behaviour or personal traits; **monitoring and evaluating performance and behaviour** | Payroll, scheduling that is not based on individual behaviour or traits, and generic productivity tools are not within, unless they evaluate the person |

**Area 5 - Access to essential private and public services and benefits**

| Item | Rule | Not covered |
|---|---|---|
| 5(a) | Used by or on behalf of **public authorities** to evaluate eligibility for essential public assistance benefits and services, including healthcare, and to grant, reduce, revoke or reclaim them | Private-sector benefit administration is not within 5(a); check 5(b)-(d) instead |
| 5(b) | Evaluating the **creditworthiness** of people or establishing their **credit score** | Systems used **to detect financial fraud** are expressly excluded |
| 5(c) | **Risk assessment and pricing** of people for **life and health insurance** | Other insurance lines (motor, property, travel) are not within 5(c) |
| 5(d) | Evaluating and classifying **emergency calls**; dispatching or prioritising emergency first response (police, fire, medical); **emergency healthcare patient triage** | Non-emergency contact-centre routing |

**Area 6 - Law enforcement** (only in so far as the use is permitted by Union or national law)

| Item | Rule | Not covered |
|---|---|---|
| 6(a) | By or on behalf of law enforcement authorities: assessing the risk of a person **becoming a victim** of crime | - |
| 6(b) | **Polygraphs** or similar tools | - |
| 6(c) | Evaluating the **reliability of evidence** in investigation or prosecution | - |
| 6(d) | Assessing the risk of a person **offending or re-offending**, not solely on the basis of profiling; or assessing personality traits, characteristics or past criminal behaviour | Risk prediction based **solely** on profiling or personality traits is **prohibited** (point 4) |
| 6(e) | **Profiling** of people in the course of detection, investigation or prosecution | - |

Every item in area 6 is scoped to use **by or on behalf of law enforcement
authorities**, or by Union bodies supporting them. A private organisation's internal
fraud investigation tool is not within area 6.

**Area 7 - Migration, asylum and border control** (only in so far as the use is permitted by Union or national law)

| Item | Rule | Not covered |
|---|---|---|
| 7(a) | By or on behalf of competent public authorities: **polygraphs** or similar tools | - |
| 7(b) | Assessing a **risk** (security, irregular migration, health) posed by a person entering or who has entered a Member State | - |
| 7(c) | Assisting the **examination of applications** for asylum, visas or residence permits and associated complaints, including reliability of evidence | - |
| 7(d) | **Detecting, recognising or identifying** people in the migration, asylum or border context | **Verification of travel documents** is excluded |

All four items are scoped to competent public authorities and Union bodies.

**Area 8 - Administration of justice and democratic processes**

| Item | Rule | Not covered |
|---|---|---|
| 8(a) | By or on behalf of a **judicial authority**: assisting in researching and interpreting facts and law, and applying the law to a set of facts; and similar use in alternative dispute resolution | Legal research tools used by a private law firm are not within 8(a); the scope is judicial authorities and ADR |
| 8(b) | **Influencing the outcome of an election or referendum**, or people's voting behaviour | Tools to which voters are **not directly exposed** (organising, optimising or structuring a campaign administratively or logistically) are excluded |

**Reading the list correctly.** Three habits prevent most errors:

1. **Match the sub-point, not the area.** "HR" is not a classification; "4(a),
   evaluating candidates" is.
2. **Check the actor.** Areas 5(a), 6, 7 and 8(a) are scoped to public or judicial
   authorities. A private organisation building the same tool for private use is not
   within them (though its provider may be, if the tool is placed on the market for
   that public use).
3. **Check the overlap with the prohibitions.** Areas 1 and 6 sit next to prohibited
   practices 4, 6, 7 and 8. The high-risk finding is the second question; the
   prohibition is the first.

### 4.3 Route B derogation - "listed but not high-risk"

A system that matches an Annex III item is **not** high-risk if it does not pose a
significant risk of harm to health, safety or fundamental rights, **including by not
materially influencing the outcome of decision-making**. The Act allows this finding
only where **at least one** of four conditions is met:

- the system is intended to perform a **narrow procedural task**;
- the system is intended to **improve the result of a previously completed human
  activity**;
- the system is intended to **detect decision-making patterns or deviations** from
  prior patterns, and is not meant to replace or influence a completed human
  assessment without proper human review; or
- the system is intended to perform a **preparatory task** to an assessment relevant
  to a listed use case.

**The override.** None of the four conditions is available where the system performs
**profiling** of natural persons. Profiling carries its data protection meaning: any
automated processing of personal data to evaluate personal aspects of a person, in
particular to analyse or predict performance at work, economic situation, health,
preferences, interests, reliability, behaviour, location or movements. A listed system
that profiles is **always** high-risk.

**The paperwork.** A provider that relies on the derogation must **document its
assessment before** the system is placed on the market or put into service, must
register the system in the EU database, and must produce the assessment on request.
The derogation is a documented claim, not a private judgment.

**How to apply it.** In practice the profiling override decides most cases in areas
3, 4 and 5. A recruitment tool that ranks candidates profiles them. A credit tool
that scores a person profiles them. A proctoring tool that flags a student's
behaviour profiles them. For such systems, do not spend time on the four conditions;
the override answers the question.

### 4.4 What a high-risk finding means, and when

A system classified as high-risk is subject, when the regime commences, to the
requirements on risk management, data governance, technical documentation,
record-keeping, transparency to deployers, human oversight, and accuracy, robustness
and cybersecurity, together with provider obligations including conformity
assessment, EU declaration of conformity, CE marking, registration and post-market
monitoring. Deployers must use the system according to its instructions, assign
competent human oversight, ensure input data is relevant and representative where
they control it, monitor operation, keep logs, and inform affected workers and
individuals. Deployers that are public bodies or private providers of public
services, and all deployers of credit-scoring and life/health insurance systems,
must complete a **fundamental rights impact assessment** before first use (area 2
systems are exempt).

| Trigger | High-risk requirements apply from |
|---|---|
| Route B: Annex III listed area | **2 December 2027** |
| Route A: Annex I product | **2 August 2028** |
| Systems already on the market before the relevant date | Only if their **design is significantly changed** after that date; high-risk systems for use by public authorities must comply in any event by **2 August 2030** |
| Commission guidelines on how to classify (with examples of high-risk and not high-risk systems) | **Not deferred**. The Commission's duty to issue them stood at 2 February 2026 |

The last row matters. The classification exercise is live now even though the
obligations are not. Guidelines under this provision would bear directly on the
derogation in 4.3, and this walkthrough does not hold them (section 11).

## 5. Tier 3 - Transparency duties

**In force since 2 August 2026.** These duties attach to specific functions, not to a
risk level, and they **stack** with any other finding: a high-risk chatbot carries
them; a minimal-risk chatbot carries them.

| # | Rule | Who | Boundary notes |
|---|---|---|---|
| T1 | People interacting directly with an AI system must be **told they are interacting with an AI system**, unless that is obvious to a reasonably well-informed and observant person in the circumstances | Provider (design duty) | Systems authorised by law for criminal-offence detection and prosecution are excluded unless open to the public for reporting |
| T2 | Outputs of systems that **generate synthetic audio, image, video or text** must be **marked in a machine-readable format** and detectable as artificially generated or manipulated | Provider | Not required where the system performs an **assistive function for standard editing** or does not substantially alter the deployer's input or its meaning. Systems on the market before 2 August 2026 have until **2 December 2026** |
| T3 | People exposed to an **emotion recognition** or **biometric categorisation** system must be informed of its operation, and the personal data processed under data protection law | Deployer | Excluded where permitted by law for criminal-offence purposes with safeguards |
| T4a | **Deep fakes** (generated or manipulated image, audio or video resembling real people, objects, places, entities or events that would falsely appear authentic) must be **disclosed** as generated or manipulated | Deployer | For evidently artistic, creative, satirical or fictional works, disclosure is limited to a form that does not hamper the work |
| T4b | AI-generated or manipulated **text published to inform the public on matters of public interest** must be disclosed as such | Deployer | Not required where the text has undergone **human review or editorial control** and a person holds editorial responsibility |

Information under T1 to T4 must be clear, distinguishable, given **at the latest at
the first interaction or exposure**, and accessible.

**How this interacts with the other tiers.** T3 attaches to systems that are high-risk
under area 1 (and, in the workplace, prohibited). T2 attaches to the provider of a
generative system whatever the deployer does with it; T4 attaches to the deployer
whatever the provider marked. The classification record therefore captures
transparency duties as a separate line, not as a tier that replaces the others.

## 6. Tier 4 - Everything else

A system that is not caught by a prohibition, is not high-risk by either route, and
does not trigger a transparency duty carries **no specific obligation under the AI
Act**. That is most systems: spam filters, internal search, document summarisation
for staff, code assistants, demand forecasting, inventory optimisation, and the like.

Three things remain true of such systems:

- **AI literacy** applies to every provider and deployer, of every system. Since the
  Omnibus, the duty is to **take measures to support** the development of AI literacy
  among staff and others operating AI on the organisation's behalf; it does not
  require a guaranteed level for any individual.
- **Other law is untouched.** Data protection, consumer protection, product safety,
  employment and equality law all apply exactly as before. The AI Act says so
  expressly.
- **Reclassification is a live risk.** A minimal-risk tool becomes something else the
  moment its intended purpose changes. A document summariser pointed at candidate CVs
  to rank them is a 4(a) system. The classification record needs a review trigger.

## 7. The classification record

One record per system, held in the AI inventory. Fields, in the order the tests run:

```
System name / identifier:
Description in one sentence:
Intended purpose (as stated by the provider):
Provider:                                Role held by [ORGANISATION]: provider / deployer / other
Gate 1  AI system?                       yes / no      reason:
Gate 2  In scope?                        yes / no      exclusion relied on (if any):
Gate 4  Reasonably foreseeable misuse considered:       yes / no
Gate 5  Product safety regime involved?  yes / no      Annex I instrument:

Tier 1  Prohibited practice?             none / point # ...     date applicable:
Tier 2  Route A (Annex I)?               no / Section A / Section B
        Route A Condition 1 (safety component):        yes / no / open
        Route A Condition 2 (third-party assessment):  yes / no / open (product law not checked)
        Route B (Annex III)?             none / item # ...
        Derogation claimed?              no / yes - condition relied on:
        Profiling of natural persons?    yes (derogation unavailable) / no
        High-risk finding:               NO / YES via Route A / YES via Route B
        Requirements apply from:         n/a / 2 Dec 2027 / 2 Aug 2028
        FRIA required before first use:  no / yes (reason)
Tier 3  Transparency duties:             none / T1 / T2 / T3 / T4a / T4b
Tier 4  No specific AI Act duty:         yes / no

Other law engaged:                       (data protection: DPIA? Art 22 decision?; sector; employment)
Review trigger:                          (change of intended purpose; new version; new deployment context)
Classified by / date / text version:     ... / ... / consolidated AI Act 27 July 2026
Counsel review:                          not yet / date
```

## 8. Worked example - a recruitment screening tool

**Facts.** [ORGANISATION], a private employer established in the Union, licenses a
recruitment platform from a vendor. The platform ingests applications for advertised
roles, extracts skills and experience, scores each candidate against the role
profile, ranks the shortlist, and offers a chat assistant that answers candidates'
questions about the process. The vendor also offers a video-interview module that
"reads engagement" from facial expressions and voice. [ORGANISATION] has not switched
that module on but the sales team is keen.

**Gate 1 - AI system?** Yes. The scoring and ranking model infers from application
data how to produce a recommendation (the rank). The chat assistant infers from
questions how to generate answers.

**Gate 2 - In scope?** Yes. [ORGANISATION] is a deployer established in the Union.
None of the exclusions applies: this is professional use, in production, not research.

**Gate 3 - Role?** Deployer. [ORGANISATION] neither built the platform nor markets it
under its own name. It would become a provider if it retrained the scoring model on
its own data and deployed the result under its own brand, or if it repurposed the
tool beyond the vendor's intended purpose. Record: deployer; role change trigger
noted.

**Gate 4 - Intended purpose?** "To analyse and filter job applications and rank
candidates for advertised roles." One sentence; matches the vendor's documentation.

**Gate 5 - Product regime?** No physical product. Route A closed.

**Tier 1 - Prohibited?** Two checks.

- The scoring and ranking function: not subliminal or manipulative, not exploiting a
  named vulnerability, not social scoring (it operates within the context in which the
  data was collected), not crime prediction, not biometric. **Not prohibited.**
- The video-interview "engagement" module: it infers emotions or intentions from
  facial expressions and voice. That is emotion recognition from biometric data. The
  prohibition covers "the areas of workplace and education institutions". This
  walkthrough reads a recruitment process for employment as within the area of the
  workplace; that is a reading of the words, recorded as such in the research note,
  and no guidance is held that settles it. **Prohibited practice 6**, in force since
  2 February 2025. No medical or safety purpose applies. **Finding: the module must
  not be switched on. Not "with safeguards"; not at all.** Record it, and tell the
  vendor why. Even on the narrower reading, the module is high-risk under item 1(c)
  and carries transparency duty T3, so the outcome for [ORGANISATION] is the same:
  it stays off.

**Tier 2 - High-risk?** Route B, area 4. The tool is intended to "analyse and filter
job applications" and "evaluate candidates". That is **item 4(a)**, in the words the
Act uses. Match found.

**Derogation?** The scoring model evaluates a person's suitability by automated
processing of their personal data, predicting performance at work. That is profiling.
**The derogation is unavailable.** The four conditions need not be examined. Even if
they were, "ranking the shortlist" is not a narrow procedural task, not an
improvement of a completed human activity, not pattern detection, and not merely
preparatory: it materially influences the outcome.

**High-risk finding: YES, via Route B, item 4(a). Requirements apply from 2 December
2027.** Between now and then the system is lawful to use, subject to the other
findings below and to other law. The vendor, as provider, will carry the conformity
assessment, technical documentation and registration duties; [ORGANISATION], as
deployer, will carry the instructions-for-use, human oversight, input data,
monitoring, logging and worker-information duties, and must inform candidates that
they are subject to a high-risk system. **FRIA:** [ORGANISATION] is a private
employer, not a public body or a private provider of public services, and this is
not a credit or insurance system; no fundamental rights impact assessment is
required by the Act (a data protection impact assessment almost certainly is - see
"other law").

**Tier 3 - Transparency?** The candidate chat assistant interacts directly with
people. **T1 applies now**: candidates must be told they are talking to an AI system,
at the first interaction, unless obvious. The vendor designs for this; [ORGANISATION]
must check the deployment does not suppress the notice. If the assistant drafts
responses that are sent to candidates as if from a recruiter, the position is
worse, not better. No T2 (the platform does not publish generated media), no T3 (the
emotion module is off, and would be prohibited anyway), no T4.

**Tier 4?** Not applicable; the system carries duties under Tiers 2 and 3.

**Other law engaged.** Solely automated decisions with significant effects on
candidates; data protection impact assessment; information to candidates about the
logic involved; equality law on indirect discrimination in the ranking model;
Member State employment law and any works-council rights. The AI Act does not
displace any of these.

**Record.**

```
System:         Vendor recruitment platform - scoring/ranking + candidate assistant
Role:           Deployer (provider-change trigger: retraining or rebranding)
Tier 1:         Scoring/ranking - none.  Video "engagement" module - PROHIBITED, point 6,
                in force 2 Feb 2025. Module must remain off.
Tier 2:         Route A - n/a. Route B - item 4(a). Profiling - yes; derogation unavailable.
                HIGH-RISK. Requirements from 2 Dec 2027. FRIA - not required (private).
Tier 3:         T1 - candidate assistant. In force now.
Other law:      GDPR Art 22 decision; DPIA; Arts 13-14 information; equality law;
                national employment law.
Review trigger: change to intended purpose; enabling any biometric or emotion feature;
                retraining on own data; Commission classification guidelines.
Text version:   Consolidated AI Act, 27 July 2026.  Counsel review: not yet.
```

## 9. Further scenarios in short form

Each row is a classification, not a description. "Applies from" gives the date of
the most demanding finding.

| System and intended purpose | Tier findings | Why | Applies from |
|---|---|---|---|
| Customer-service chatbot on a retail website answering order queries | Transparency T1 | Interacts directly with people; not listed in Annex III | In force (2 Aug 2026) |
| Email spam filter | None (Tier 4) | No prohibition, no listed area, no transparency function | AI literacy only |
| Bank's credit-scoring model deciding consumer loan applications | High-risk 5(b); FRIA required | Creditworthiness evaluation; profiling, so no derogation; 5(b) deployers must do a FRIA | 2 Dec 2027 |
| Same bank's card-fraud detection model | None (Tier 4) | Expressly excluded from 5(b) | AI literacy only |
| Call-centre tool inferring customers' frustration from voice to escalate calls | High-risk 1(c); Transparency T3 | Emotion recognition from biometric data, outside workplace and education, so high-risk not prohibited; deployer must inform those exposed | T3 in force; high-risk 2 Dec 2027 |
| Same tool pointed at the **agents'** voices to score their composure | **Prohibited**, point 6 | Emotion inference in the workplace, no medical or safety purpose | In force (2 Feb 2025) |
| Online exam proctoring flagging suspicious behaviour | High-risk 3(d) | Monitoring prohibited behaviour during tests; profiling, so no derogation | 2 Dec 2027 |
| Warehouse system allocating shifts by predicted individual productivity | High-risk 4(b) | Task allocation based on individual behaviour; profiling | 2 Dec 2027 |
| Warehouse system allocating shifts purely by roster availability and rules | None (Tier 4) | Not based on individual behaviour or traits; arguably not an AI system at all | AI literacy only |
| Building access by face matching against enrolled employees, one-to-one at the gate | None from area 1; data protection law applies | Biometric **verification** is carved out of 1(a) | AI literacy only |
| Shopping-centre cameras identifying known shoplifters against a watch-list | High-risk 1(a) | Remote biometric identification, private operator; not the law-enforcement prohibition, but area 1 and data protection law bite hard | 2 Dec 2027 |
| AI safety function in a lift controller | High-risk Route A, Annex I Section A (lifts) - if the lift regime requires third-party assessment | Safety component of a Section A product; Condition 2 to be confirmed against the lifts legislation | 2 Aug 2028 |
| AI collision-avoidance in an industrial robot | High-risk Route A, Annex I **Section B** (machinery) | Machinery moved to Section B by the Omnibus; only limited AI Act provisions apply directly; requirements arrive through the Machinery Regulation | 2 Aug 2028 via sectoral law |
| Diagnostic software classifying radiology images | High-risk Route A, Annex I Section A (medical devices) - if class requires third-party assessment | Software is itself a product under the medical devices regime; Condition 2 turns on device class | 2 Aug 2028 |
| Marketing video with a synthetic presenter resembling a real actor | Transparency T2 (provider), T4a (deployer) | Deep fake; provider marks, deployer discloses | In force; pre-existing generators to mark by 2 Dec 2026 |
| Internal assistant summarising staff meeting notes | None (Tier 4); T2 unlikely | Summarising the deployer's own input without substantially altering its meaning is within the editing carve-out; no public interaction | AI literacy only |
| Same assistant repurposed to screen and rank CVs | High-risk 4(a) | Intended purpose changed; the organisation may now be the provider | 2 Dec 2027 |
| Public benefits agency tool flagging claims for review | High-risk 5(a); FRIA required; registration of use | Public authority evaluating eligibility; derogation unavailable if it profiles claimants, and "flagging for review" still materially influences outcome | 2 Dec 2027 |
| Council chatbot answering questions about bin collection | Transparency T1 | Direct interaction; not an eligibility decision | In force |
| Image generator offered to the public | Transparency T2; Tier 1 point 9 safeguards | Provider marks outputs; must show reasonable and adequate safeguards against non-consensual intimate material from 2 Dec 2026 | T2 in force; point 9 from 2 Dec 2026 |
| Open-source model weights published on a repository | A model, not a system: outside this walkthrough; the model-provider track applies, with its own open-source treatment | The system-level open-source exclusion does not answer a model question. A **system** built on those weights is classified on its own intended purpose | - |
| Political campaign tool drafting voter-targeted messages shown directly to voters | High-risk 8(b) | Influencing voting behaviour, voters directly exposed | 2 Dec 2027 |
| Same campaign's internal canvassing-route optimiser | None from 8(b) | Voters not directly exposed to the output | AI literacy only |

## 10. Common errors, and the rule that corrects each

| Error | Correction |
|---|---|
| Planning against 2 August 2026 for high-risk | The high-risk regime applies from 2 December 2027 (Annex III) and 2 August 2028 (Annex I). The transparency duties are what landed on 2 August 2026 |
| Treating the deferral as an exemption | Classification is due now; obligations are due later. Systems in use at the commencement date are grandfathered only until their design changes significantly |
| Claiming the "not significant risk" derogation for a tool that ranks, scores or evaluates people | Profiling removes the derogation. Most area 3, 4 and 5 tools profile |
| Treating the derogation as a private judgment | It must be documented before market, registered, and produced on request |
| Reading "biometrics" as one category | Verification (one-to-one) is carved out of the high-risk list. Identification (one-to-many, remote) is high-risk. Categorisation by protected characteristics is prohibited. Emotion recognition is prohibited at work and school, high-risk elsewhere |
| Treating fraud detection as credit scoring | Fraud detection is expressly excluded from item 5(b) |
| Assuming an area heading captures every system in the sector | The list is of specific use cases. A sector match is not an item match |
| Assuming public-sector items catch private systems | Items 5(a), 6, 7 and 8(a) are scoped to public, law-enforcement or judicial actors |
| Assuming an AI system inside a regulated product is automatically high-risk | Both conditions must hold: safety component (as narrowed by the Omnibus) and third-party conformity assessment for health and safety reasons |
| Assuming open-source licensing takes a system outside the Act | It does not, for prohibited practices, transparency duties, or high-risk systems |
| Treating "deep fake" as any synthetic content | A deep fake resembles real people, objects, places, entities or events and would appear authentic. Other generated media carries the provider marking duty but not the deployer disclosure duty |
| Counting the prohibitions from a summary | The consolidated text has ten points, lettered (a), (b), (ba), (bb), (c) to (h). Summaries that say "nine" merge the two December 2026 points |
| Reading the four "levels" as the statutory structure | They are a reading of the Act, not its terms. The Act defines prohibited practices, high-risk systems, and Article 50 duties; "minimal" is the remainder |

## 11. Verification status and gates

**Verified against the primary text, 30 August 2026:**

- Every prohibition, every Annex III item and sub-item, every Annex I entry, the two
  high-risk routes, the derogation and its profiling override, the transparency
  duties, and every date in this document, read in the consolidated AI Act of
  27 July 2026, cross-checked against the Omnibus amending regulation.
- Annex III carries no amendment marker in the consolidation: the Omnibus did not
  change the listed areas. Annex I did change (machinery moved from Section A to
  Section B).

**Not verified, and therefore not asserted:**

- **Whether any given product requires third-party conformity assessment.** That is
  a question for the Annex I instruments themselves (toys, lifts, medical devices and
  the rest), none of which is held. Route A findings in this document are conditional
  on that check.
- **Commission classification guidelines** under the provision carved out of the
  deferral. Not held. If issued, they bear directly on the derogation and on the
  boundary cases in section 9.
- **Commission guidelines on the definition of an AI system**, and on the
  prohibited practices. Referred to on the Commission's overview page; not held; not
  relied on. Gate 1 above is applied from the statutory definition alone.
- **Delegated acts** amending Annex III or the derogation conditions. None is
  reflected in the consolidation used; any adopted later supersedes this document.
- **Member State law**: national rules on real-time biometric identification,
  national employment law, and the "without right" defence for point 10.

**Review trigger for this document:** any consolidation of the AI Act later than
27 July 2026; publication of the classification guidelines; any delegated act
amending Annex III.

---

*AI Governance Series - Part 2 - Classifying AI systems by risk (European Union)*
*Narendra Karki - CISSP - CISM - CISA - CAISP - CMCPSE*
*Free and public - educational, not legal advice - CC BY 4.0*
