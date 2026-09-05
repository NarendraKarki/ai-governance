# Classifying AI Systems by Risk - an EU AI Act Walkthrough

**Series:** AI Governance Series - Part 2
**Focus:** Laws and regulations - European Union
**Legal baseline:** the EU Artificial Intelligence Act as consolidated at 27 July 2026, after amendment by the Digital Omnibus on AI
**Version:** 1.0
**Status:** Verified against the consolidated primary text. Verification record in the accompanying research note.

*Educational material, not legal advice. Classification of a real system should be
reviewed by qualified counsel. Article-level citations for every statement in this
document are in the research note; the source register states exactly which texts
were held and verified.*

---

## 1. Why classification comes first

Every obligation in the EU AI Act hangs off a classification question. Whether a
system may be used at all, what its provider must build and document, what its
deployer must tell people, and when any of that becomes enforceable - all of it
depends on where the system lands in the Act's structure. Classify wrongly and an
organisation either builds a compliance programme for duties it does not have, or
walks into duties it did not see.

The popular picture of the Act is a pyramid of four risk tiers. It is a useful
first sketch and a poor decision tool, for two reasons this walkthrough keeps
returning to:

- **The tiers are not exclusive.** The transparency duties are a set of overlay
  obligations, not a stratum between high-risk and minimal. A system can be
  high-risk and carry transparency duties at the same time; a system with no other
  obligations can still carry them.
- **The tiers do not commence together.** The prohibitions bind since February
  2025 and the transparency duties since August 2026, but the high-risk regime is
  deferred to December 2027 and August 2028. A deferral is not an exemption:
  systems procured or built today will be caught, on a known date, and the
  classification determines which date.

This walkthrough turns the Act's structure into a sequence of five gates. Work
through them in order, for one system at a time, with its intended purpose written
down before you start.

## 2. Before the gates: three threshold questions

### 2.1 Is it an AI system in the Act's sense?

The Act covers machine-based systems that operate with some degree of autonomy,
may adapt after deployment, and infer from their inputs how to generate outputs -
predictions, content, recommendations, decisions - that can influence real or
virtual environments. The load-bearing word is **infers**. Software that only
executes rules written entirely in advance by a person is on the wrong side of
that line; a model that learned its behaviour from data is squarely on the right
side of it. Most systems marketed today as AI, including every general-purpose
model and everything built on one, are within the definition. When in doubt,
classify - the cost of running the gates on a borderline system is an hour; the
cost of skipping them is not knowing what you are operating.

### 2.2 Are you within the Act's reach?

The Act applies to providers placing systems on the Union market wherever those
providers are established, to deployers established or located in the Union, and -
easily missed - to providers and deployers in third countries **where the
system's output is used in the Union**. A firm outside the EU whose AI-produced
scores, decisions or content are used inside it is within scope.

Certain activity is outside the Act entirely: systems used exclusively for
military, defence or national security purposes; research, testing and
development activity before a system is placed on the market or put into service
(though not testing in real-world conditions); systems developed and put into
service solely for scientific research; and purely personal, non-professional
use. Free and open-source releases are outside scope **unless** the system is a
prohibited practice, is high-risk, or falls under the transparency duties - so
the exemption never removes the gates that matter.

### 2.3 Which role do you hold?

The Act splits duties between the **provider** - who develops a system or has it
developed and supplies it under their own name - and the **deployer** - who uses
it under their authority. Classification itself is the same exercise for both,
but its consequences differ: the documentation and registration duties attached
to a classification call sit mostly with the provider, while use-facing duties
sit with the deployer. A deployer that rebrands a system, substantially modifies
it, or markets it under its own name takes on the provider role for it. Record
the role alongside the classification; the two travel together.

## 3. Gate 1 - Prohibited practices: may this system be used at all?

The first gate is absolute. The Act names practices that may not be placed on the
market, put into service or used - full stop. No impact assessment, consent
mechanism or business case cures a prohibited practice, and this part of the Act
has applied since **2 February 2025**.

Test the system against each prohibition, on its intended purpose and on what it
actually does in operation:

1. **Manipulation causing harm** - subliminal, purposefully manipulative or
   deceptive techniques that materially distort behaviour by impairing an
   informed decision, causing or likely to cause significant harm.
2. **Exploiting vulnerability** - exploiting age, disability, or a specific
   social or economic situation to materially distort behaviour, with significant
   harm caused or likely.
3. **Social scoring** - evaluating people over time on social behaviour or
   personal characteristics, where the score leads to detrimental treatment in an
   unrelated context, or treatment unjustified or disproportionate to the
   behaviour.
4. **Predictive policing of individuals** - assessing or predicting the risk of a
   person committing a criminal offence based solely on profiling or personality
   traits. Systems supporting a human assessment already grounded in objective,
   verifiable facts directly linked to criminal activity are outside the
   prohibition.
5. **Untargeted face scraping** - creating or expanding facial recognition
   databases by untargeted scraping of facial images from the internet or CCTV.
6. **Emotion inference at work and in education** - inferring the emotions of a
   person in the workplace or in education institutions, except where the system
   is intended for medical or safety reasons. This is the prohibition an ordinary
   business proposal reaches most easily: sentiment scoring of staff from camera,
   voice or keystroke data, AI-scored analysis of a candidate's demeanour, and
   mood-rating productivity tools are all within it.
7. **Biometric categorisation of sensitive traits** - biometric categorisation
   deducing race, political opinions, trade union membership, religious or
   philosophical beliefs, sex life or sexual orientation, subject to narrow
   law-enforcement dataset carve-outs.
8. **Real-time remote biometric identification for law enforcement** in publicly
   accessible spaces, outside narrowly authorised cases with judicial or
   independent authorisation under national law.

Two further prohibitions, added by the Digital Omnibus, apply from
**2 December 2026**:

9. **Non-consensual intimate imagery** - AI systems that generate or manipulate
   realistic images, video or audio of an identifiable person's intimate parts or
   sexually explicit activity without that person's freely given, specific,
   informed, unambiguous and explicit consent.
10. **Child sexual abuse material** - AI systems that generate or manipulate such
    material as defined in Union law.

For these two, the Act distinguishes the *system* from the *use*: placing a
system on the market is prohibited where such generation is its intended purpose,
or where its design and capabilities make that output reasonably foreseeable and
reproducible and the system lacks adequate safeguards to prevent and correct it;
using any system for that purpose is prohibited outright. A general-purpose tool
with real, working safety measures is not itself prohibited; the person who
bends it to this purpose still is.

**If the system falls here, classification ends.** There is no tier below a
prohibition. The remaining gates are only for systems that pass this one.

## 4. Gate 2 - High-risk by the product route

The Act's first high-risk category has nothing to do with the famous list of use
cases. A system is high-risk where **both** of the following hold:

- it is a safety component of a product - or is itself a product - covered by the
  Union product legislation listed in the Act's Annex I (machinery, toys, lifts,
  medical devices, vehicles, aircraft, and similar regulated products); and
- that product must undergo a **third-party** conformity assessment under that
  legislation before sale.

So an AI system inside a medical device that a notified body must assess is
high-risk by this route; the same algorithm in an unregulated consumer app is
not. The question is answered by product law, not by the AI's sophistication.

The Digital Omnibus tightened this gate in three ways that matter in practice:

- **Convenience is not safety.** Systems used solely for non-safety aspects -
  user assistance, performance optimisation, service efficiency, automation or
  convenience, quality control - do not count as safety components.
- **Unless failure hurts people.** A system whose failure or malfunction would
  endanger health and safety qualifies as a safety component regardless.
- **Only safety-driven assessments count.** A product sent for third-party
  assessment solely for risks other than health and safety - radio spectrum or
  electromagnetic interference, for instance - does not satisfy the second
  condition.

The omnibus also reorganised the machinery route: AI in machinery is now handled
through the new Machinery Regulation, listed in the section of Annex I whose
products keep their own sectoral procedures, with only a narrow slice of the AI
Act applying directly. For AI embedded in regulated products generally, this gate
commences on **2 August 2028**.

If the system is high-risk here, record it, and still run Gates 4 and 5 - the
transparency overlay and the residual duties apply to high-risk systems too.

## 5. Gate 3 - High-risk by the Annex III list

The second high-risk category is the listed one: systems whose intended purpose
falls in one of **eight areas** in Annex III. The Digital Omnibus did not touch
this list - every item below is unamended base text, verified item by item
against the consolidated Act. The area headings are the map; the items under them
are the law. A system is caught by an item, not by an area heading.

**1. Biometrics** (where permitted under Union or national law)
- remote biometric identification systems - but not biometric verification whose
  sole purpose is confirming a person is who they claim to be (device unlocking,
  passport e-gates);
- biometric categorisation according to sensitive or protected attributes
  inferred from biometric data (the sensitive-trait cases are already prohibited
  at Gate 1; this item catches categorisation by protected attributes that
  survives Gate 1);
- emotion recognition - where not already prohibited at Gate 1, which reaches
  workplaces and education. Emotion recognition of customers, for example, is
  not prohibited but is high-risk, and carries a disclosure duty at Gate 4.

**2. Critical infrastructure**
- safety components in the management and operation of critical digital
  infrastructure, road traffic, or the supply of water, gas, heating or
  electricity.

**3. Education and vocational training**
- systems determining access, admission or assignment to institutions;
- systems evaluating learning outcomes, including where the evaluation steers a
  student's learning;
- systems assessing the level of education a person will receive or can access;
- systems monitoring and detecting prohibited student behaviour during tests.

**4. Employment, workers' management and access to self-employment**
- systems for recruitment or selection - targeted job advertising, analysing and
  filtering applications, evaluating candidates;
- systems making decisions on the terms, promotion or termination of work
  relationships, allocating tasks based on behaviour or personal traits, or
  monitoring and evaluating performance and behaviour.

**5. Essential private and public services**
- eligibility for essential public assistance benefits and services, including
  healthcare, and granting, reducing, revoking or reclaiming them;
- creditworthiness evaluation and credit scoring of natural persons - except
  systems used for detecting financial fraud;
- risk assessment and pricing for life and health insurance;
- classifying and dispatching emergency calls and emergency first response,
  including emergency healthcare triage.

**6. Law enforcement** (where permitted under Union or national law)
- assessing the risk of a person becoming a victim of crime; polygraphs and
  similar tools; evaluating the reliability of evidence; assessing offending or
  re-offending risk otherwise than by profiling alone (profiling-only prediction
  is prohibited at Gate 1); profiling in the course of detection, investigation
  or prosecution.

**7. Migration, asylum and border control**
- polygraphs and similar tools; risk assessments of persons entering a Member
  State; assisting examination of asylum, visa and residence applications;
  detecting, recognising or identifying persons in this context, except
  verification of travel documents.

**8. Administration of justice and democratic processes**
- systems assisting judicial authorities in researching and interpreting facts
  and law and applying it to facts, including in alternative dispute resolution;
- systems for influencing the outcome of an election or referendum or voting
  behaviour - excluding campaign logistics tools whose output voters never see.

### 5.1 The derogation: listed does not always mean high-risk

A system falling under an Annex III item is **not** high-risk where it does not
pose a significant risk of harm to health, safety or fundamental rights,
including by not materially influencing the outcome of decision-making. That
applies only where at least one of four conditions is met - the system is
intended to:

- perform a narrow procedural task;
- improve the result of a previously completed human activity;
- detect decision-making patterns or deviations from them, without replacing or
  influencing a completed human assessment absent proper review; or
- perform a task preparatory to an assessment relevant to a listed use case.

**The override:** the derogation can never apply where the system performs
**profiling of natural persons**. A listed system that profiles people is always
high-risk. Since most employment, credit and education systems that evaluate
people do so by processing their personal aspects, the derogation is far narrower
than it first reads.

**The paperwork is not optional.** A provider claiming the derogation must
document the assessment **before** the system is placed on the market or put
into service, register the system in the EU database, and produce the
documentation to national authorities on request. An undocumented derogation
claim is not a classification; it is a compliance gap. The Commission was also
required to issue guidelines on this Article with practical examples by
February 2026 - obtain the current version before making a contested call.

The Annex III high-risk regime commences on **2 December 2027**.

## 6. Gate 4 - Transparency duties: the overlay, not a tier

These duties have applied since **2 August 2026** and are the newest live
obligations in the Act. They attach by function, regardless of what earlier
gates concluded - which is why treating "transparency" as a middle tier of the
pyramid misclassifies systems on both sides of it. Four functions trigger them:

- **Systems that interact directly with people** - providers must design them so
  people are told, or can obviously tell, that they are dealing with an AI
  system.
- **Systems generating synthetic content** - providers must mark audio, image,
  video and text outputs as artificially generated, in machine-readable and
  detectable form, with a carve-out for assistive editing that does not
  substantially alter the input. The Digital Omnibus added a mechanism for codes
  of practice, and failing those common implementing rules, on how marking is
  done.
- **Emotion recognition and biometric categorisation** - deployers must inform
  the people exposed, and handle the personal data under data protection law.
- **Deep fakes and AI text on matters of public interest** - deployers must
  disclose that content was artificially generated or manipulated; artistic and
  satirical work needs only non-intrusive disclosure, and AI-drafted text that
  passed human editorial control with a person holding editorial responsibility
  is out of the text duty.

The information must reach people clearly, at the latest at first interaction or
exposure. These duties stack: a high-risk recruitment chatbot owes them; so does
a minimal-risk marketing image generator.

## 7. Gate 5 - What remains for everything else

A system that passes Gates 1 to 4 untouched lands where most workplace AI lands
today: no system-specific obligations under the Act. Three things still apply,
and a classification record that omits them overstates the comfort:

- **AI literacy** - providers and deployers must ensure staff dealing with the
  operation and use of AI systems have sufficient AI knowledge and skills for
  their role. In force since February 2025, and it applies to the organisation
  whatever the system's tier.
- **General-purpose AI model duties** - obligations on GPAI models (and the
  heavier ones for models with systemic risk) sit with the **model provider**,
  in force since August 2025. Deployers do not inherit them by using the model,
  but they should know whether their supplier carries them.
- **Everything else that already applied** - data protection law above all. A
  minimal-risk classification under the AI Act says nothing about lawfulness
  under the GDPR.

## 8. The classification, in time

Classification tells you which duties; the commencement schedule, as amended by
the Digital Omnibus, tells you when. As at 1 September 2026:

| Outcome | Duties bind from | Status today |
|---|---|---|
| Prohibited practice (items 1-8) | 2 February 2025 | **In force** |
| Prohibited practice (intimate imagery, CSAM) | 2 December 2026 | Three months out |
| High-risk - Annex III route | 2 December 2027 | Deferred - readiness window |
| High-risk - Annex I product route | 2 August 2028 | Deferred - readiness window |
| Transparency duties | 2 August 2026 | **In force** |
| AI literacy | 2 February 2025 | **In force** |
| GPAI model duties (on the model provider) | 2 August 2025 | **In force** |

The deferral is the reason to classify now rather than in 2027. A high-risk
system procured today on the basis that "the rules do not apply yet" is a system
approved without an owner for the compliance work that lands on a known date.
Classification now, a named readiness owner, and a documented path to the
applicable date - that is what the deferral is for.

## 9. Worked example - a CV-screening tool, gate by gate

**The system.** [ORGANISATION], an EU-established company, licenses a
SaaS tool that ingests applications for open roles, parses CVs, scores each
candidate against the role profile using a model trained on past hiring
outcomes, ranks the shortlist, and flags candidates for automatic rejection
below a threshold. Recruiters see the ranking and can override it. The vendor
recently offered an add-on that estimates candidate engagement from video
interviews.

**Threshold.** It is machine-based, autonomous in operation, and infers scores
and rankings from input data - an AI system. [ORGANISATION] uses it under its
own authority and did not develop it: [ORGANISATION] is the **deployer**, the
vendor the **provider**. Buying the SaaS does not change that; rebranding it or
fine-tuning it into a product of its own would.

**Gate 1 - prohibitions.** The core tool manipulates no one and infers no
emotions. The video add-on is different: estimating a candidate's engagement
from interview footage is inferring the emotions of a person in a
workplace-and-education context, and recruitment is where that prohibition
bites hardest. It is not high-risk; it is **not permitted at all**, since
February 2025, and no vendor assurance or consent checkbox changes that. The
add-on is declined; the core tool proceeds to Gate 2.

**Gate 2 - product route.** The tool is not a safety component of any Annex I
product. Not applicable.

**Gate 3 - Annex III.** The employment area lists systems for recruitment or
selection, and names analysing and filtering applications and evaluating
candidates. The tool is a direct hit on the listed item - not merely the area.

*Derogation?* Run the four conditions honestly. Scoring and ranking candidates
is not a narrow procedural task; it does not improve a completed human
activity, since it produces the assessment the human then works from; it does
not merely detect deviations; and it is not preparatory - the ranking materially
influences who a recruiter ever looks at. No condition fits. And the override
settles it regardless: the tool evaluates personal aspects of individuals to
score them - profiling - so the derogation **cannot** apply. The recruiter
override does not rescue it either; human review mitigates a high-risk system,
it does not declassify one.

**Conclusion: high-risk, Annex III route.** The provider's classification
duties, and the high-risk requirements, bind from 2 December 2027.

**Gate 4 - transparency.** If candidates interact with a chatbot during
application, they must be told it is one - that duty is live now. The scoring
itself is not a Gate 4 function.

**Gate 5 - the rest.** Recruiters using the tool need sufficient AI literacy to
question and override it - live now. Data protection law applies in full to the
processing, today, whatever the AI Act's dates say.

**What [ORGANISATION] records.** Classification: high-risk (employment,
recruitment item), derogation unavailable (profiling), role: deployer,
readiness owner named, target date 2 December 2027; vendor asked for its
Article 6(4)-style documentation and its plan for the provider-side high-risk
requirements; video add-on rejected as a prohibited practice. One system, one
page, five gates.

## 10. Quick-fire classifications

Nine more systems, run through the same gates. Each of these turns on one
decisive feature - the point of the exercise is finding it.

| # | System | Decisive feature | Outcome |
|---|---|---|---|
| 1 | Customer-service chatbot on the public website | Interacts directly with people; no listed use | No tier duties; **disclosure duty live now**; literacy applies |
| 2 | Staff-meeting analytics scoring employee engagement from video and voice | Emotion inference in the workplace | **Prohibited** since Feb 2025; medical or safety purpose exception does not cover productivity |
| 3 | Consumer-loan credit scoring model | Listed: creditworthiness of natural persons; profiles people, so no derogation | **High-risk** (Annex III) from Dec 2027 |
| 4 | Same model, used only to detect payment fraud | Express exception in the credit item | Not high-risk by that item; run remaining gates |
| 5 | Vision system rejecting cosmetically flawed products on a packaging line | Quality control is a non-safety function post-omnibus; failure endangers no one | Not a safety component; **no tier duties** |
| 6 | Vision system halting a press when a hand enters the guard zone | Failure endangers health and safety; machinery route | **High-risk** (product route) - via the Machinery Regulation's integrated procedure, from Aug 2028 |
| 7 | X-ray triage module inside a notified-body-assessed medical device | Annex I product + third-party conformity assessment | **High-risk** (product route) from Aug 2028 |
| 8 | Marketing team's image generator for campaign visuals | Synthetic content | No tier duties; provider-side **marking duty live**; deep-fake disclosure if real people are depicted |
| 9 | HR document assistant converting interview notes into a standard template after the hiring decision is made | Employment area, but: narrow procedural and preparatory-formatting task, no influence on outcome, no profiling | Listed area, **derogation arguable** - and only with the assessment documented and the system registered before deployment |

Row 9 is the honest edge case: it is the only row where reasonable people
disagree, and the Act's answer is procedural - the provider claiming it must
write the assessment down first and register the claim. If the paperwork feels
harder than complying, that is the Act telling you something.

## 11. Mapping to the policy sets in this series

The acceptable use policies in Part 1 of this series scale controls through
organisation-defined levels of use. Those levels are anchored to the statutory
categories this walkthrough produces, and the mapping is deliberate:

- A **prohibited** outcome at Gate 1 corresponds to the policies' prohibited
  practices sections - banned outright, no level applies.
- A **high-risk** outcome at Gate 2 or 3 is the policies' Level 4 - the
  high-risk track: treated as the highest control level today and recorded with
  a readiness owner and target date for the applicable commencement date.
- A **transparency** duty at Gate 4 maps to the policies' disclosure sections,
  live obligations owed today.
- A **no-tier** outcome at Gate 5 still lands in Levels 1-3 on the policies'
  own risk criteria - the organisation's classification keeps working where the
  statute goes quiet.

## 12. Five misreadings this walkthrough is built to prevent

1. **"The four tiers are exclusive."** Transparency is an overlay. High-risk
   systems carry it too, and so can systems with no other duties.
2. **"High-risk rules were pushed back, so classification can wait."** The dates
   moved to December 2027 and August 2028; the systems being bought today will
   still be in service then. Classify at approval, not at commencement.
3. **"It's on the Annex III list, so it's high-risk"** - and its mirror image,
   "we can self-assess our way off the list." The derogation exists, it is
   narrow, profiling kills it, and it must be documented and registered before
   deployment - not asserted afterwards.
4. **"Emotion AI is high-risk."** In the workplace and education it is
   prohibited. Elsewhere it is high-risk and carries a live disclosure duty.
   The difference is not a nuance; one of the three is a ban.
5. **"Minimal risk means nothing to do."** AI literacy has applied since
   February 2025, transparency duties since August 2026, and data protection law
   throughout. Minimal is a statement about this Act's tiers, not about the law.

---

*Part 2 of the AI Governance Series. Educational material, not legal advice.
Verified against the consolidated Artificial Intelligence Act of 27 July 2026;
the research note records every citation and the source register records every
text held. Have classification calls on real systems reviewed by qualified
counsel.*
