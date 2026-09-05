# Two Misreadings of the EU AI Act - What the Law Expects Today

**Series:** AI Governance Series - companion to Part 2 (Classifying AI systems by risk)
**Legal baseline:** the EU Artificial Intelligence Act as consolidated at 27 July 2026, after amendment by the Digital Omnibus
**Version:** 1.0
**Status:** Verified against the consolidated primary text. Citations in the Part 2 research note; texts held in the Part 2 source register.

*Educational material, not legal advice. Have your DPO or legal counsel review
before relying on any position here.*

---

## Why this document exists

The most reproduced picture of the EU AI Act is a four-tier pyramid:
unacceptable at the top, then high-risk, then limited or transparency risk,
then minimal. As a first sketch it is fine. But most organisations do not use
it as a sketch - they use it as a map: find your system's tier, read off your
obligations. Used that way, it misleads twice, and both misreadings produce
real compliance failures in opposite directions. One makes companies miss
duties that already bind. The other makes them build for duties that do not
bind yet - or worse, ignore duties that were never deferred at all.

Very few teams outside specialist practice have internalised either point.
This document explains both, with worked examples.

## Misreading one - "transparency is a middle tier"

### What the pyramid suggests

That there is a class of systems - chatbots, image generators - which sit in
a "limited risk" band, and that a system is either high-risk OR
transparency-risk OR minimal. Pick one box.

### What the Act actually does

The transparency duties are not a box. They are a set of **overlay
obligations that attach by function**, whatever else the system is. They have
applied since **2 August 2026** - which makes them the newest live
obligations in the Act, and the ones most likely to affect systems your
organisation runs today. Four functions trigger them:

1. **The system talks to people.** People must be told, or be plainly able
   to tell, that they are interacting with an AI system - clearly, at the
   latest at the first interaction. The design duty sits with the provider;
   a deployer choosing and configuring the tool needs to make sure the
   disclosure actually reaches its users.
2. **The system generates synthetic content.** Audio, image, video and text
   outputs must be marked as artificially generated in a machine-readable,
   detectable form. This is a provider duty, with a carve-out for assistive
   editing that does not substantially change the input.
3. **The system does emotion recognition or biometric categorisation.**
   Where such a system is lawful at all, the people exposed to it must be
   informed it is operating, and the personal data handled under data
   protection law. This is a deployer duty.
4. **The output is a deep fake, or AI text published on matters of public
   interest.** The deployer must disclose that the content was artificially
   generated or manipulated. Artistic and satirical work needs only
   non-intrusive disclosure; AI-drafted text that passed human editorial
   control, with a person holding editorial responsibility, is outside the
   text duty.

Because these attach by function, they **stack**. A high-risk system that
talks to candidates owes them. A minimal-risk marketing tool that generates
images owes them. The pyramid's middle band is the one part of the picture
that was never a band at all.

### Worked example - an insurer with two systems

[INSURER] operates in the EU with two AI deployments: a public website
chatbot answering policy questions, and a licensed recruitment platform that
scores and ranks job applications, which last month added a chat interface
that conducts structured first-round interviews with candidates.

**The website chatbot.** On the classification walkthrough it clears every
gate until the last: it is not banned, not a safety component, not on the
high-risk list. The pyramid reader files it under "minimal - nothing to do"
and moves on. Wrong since 2 August 2026: it interacts directly with people,
so customers must be told they are talking to an AI system. In practice that
means the chat window identifies itself as an AI assistant at the start of
the conversation - not in a linked policy, not after the fact. If the
insurer's marketing team uses the same platform's image generator for
campaign visuals, those outputs must carry machine-readable marking - a
question to put to the vendor, since the technical duty is theirs, but the
insurer's brand is on the output. And if a campaign video depicts a real,
identifiable person synthetically, the deployer - the insurer - must
disclose the manipulation, whatever the vendor's marking does.

**The recruitment platform.** This is a listed high-risk system (employment:
filtering applications, evaluating candidates), and because it profiles
people, the narrow derogation is unavailable. The pyramid reader concludes
"high-risk - the heavy obligations apply" and, on learning those were
deferred to December 2027, relaxes entirely. Also wrong, twice over. The new
interview chatbot talks to candidates: the interaction disclosure applies to
it **today**, even though the system it belongs to is high-risk with
deferred substantive duties. And the staff running the platform fall under
the AI literacy duty - in force since February 2025 - so recruiters need
enough understanding of the tool to question and override it, and the
insurer needs to be able to show how it ensures that.

One organisation, two systems, and the "middle tier" duties landed on both -
including the high-risk one. That is what "the tiers are not exclusive"
means in practice.

## Misreading two - "the tiers all started together"

### What the pyramid suggests

A single regime with a single switch-on date - most people half-remember
"August 2026" and assume the whole Act, or read a headline about the Digital
Omnibus and assume the whole Act was postponed.

### What the Act actually does

Each part of the structure has its own date, and the Digital Omnibus moved
some of them - it did not move the structure:

| What | Binds from | Status on 1 September 2026 |
|---|---|---|
| Prohibited practices | 2 February 2025 | In force |
| AI literacy duty | 2 February 2025 | In force |
| Two added prohibitions (non-consensual intimate imagery; CSAM) | 2 December 2026 | Three months out |
| General-purpose AI model duties (on model providers) | 2 August 2025 | In force |
| Transparency duties | 2 August 2026 | In force |
| High-risk regime - listed systems (Annex III route) | 2 December 2027 | Deferred |
| High-risk regime - regulated products (Annex I route) | 2 August 2028 | Deferred |

Two consequences follow. **A deferral is not an exemption**: systems bought
or built now will be in service when their date lands, and the classification
decides which date. And **the bans were never deferred**: what is prohibited
has been prohibited since February 2025, and treating a banned practice as
merely "high-risk, so 2027's problem" is the most expensive way to misread
the chart.

### Worked example - a bank procuring a scoring model

[BANK] is negotiating a three-year licence for a consumer credit-scoring
model, to go live in early 2027. The vendor's sales deck says the AI Act's
high-risk rules "were postponed to the end of 2027", which is true, and
implies that nothing therefore needs to happen now, which is false.

Creditworthiness scoring of natural persons is a listed high-risk use, it
profiles people so the derogation cannot apply, and the contract will still
be running on 2 December 2027. If the bank signs without asking readiness
questions, it discovers in 2027 that its supplier has no conformity
assessment plan, no technical documentation, and no logging design - with
the bank operationally dependent on the system. What good governance looks
like in September 2026: classify the system at approval (high-risk, listed
route, no derogation); name a readiness owner and record the December 2027
date; put the provider's high-risk readiness into the contract - documented
classification, a dated compliance plan, cooperation duties for the deployer
obligations the bank itself will carry; and check the one exception that
could change the answer - a version of the model used solely to detect
payment fraud sits inside an express exception to the credit item, so the
fraud-detection deployment is classified separately from the lending one.

Meanwhile the same vendor offers an add-on that estimates loan applicants'
truthfulness from voice stress in phone interviews. That is not a 2027
question either, but the analysis has to be done precisely. The outright ban
on emotion inference reaches workplaces and education institutions - so if
the bank pointed the same capability at its own staff or job candidates, it
would be prohibited, and has been since February 2025. Pointed at customers,
it survives the ban gate but not the comfortable reading: emotion
recognition is a listed high-risk use in its own right, and the live
disclosure overlay applies today - every applicant on the call must be told
the system is operating, with the personal data handled under data
protection law. A tool whose business case depends on customers not knowing
it is running rarely survives its own disclosure duty, and the bank would be
buying a high-risk classification with a December 2027 bill attached.
Declined at procurement - which is precisely the point of classifying at
approval rather than at commencement.

## Gate 1 up close - the practice, not the component

One more misreading deserves its own section, because it decides what the
bans actually catch. The prohibited practices are not a list of dangerous
components. What the Act prohibits, for each listed item, is the practice:
placing an AI system on the market, putting it into service, or using it,
**for that purpose**. Three rules of thumb follow. For most items no harm
needs to have happened - the purpose alone is enough. The ban follows the
function into whatever product it is embedded in - a prohibited practice
does not become lawful by shipping as a feature or a toggle. And capability
alone does not condemn a general-purpose tool - what its provider markets it
for, and what a deployer actually uses it for, does.

Here is what that looks like in the two sectors that ask first.

### A finance environment

[LENDER] runs a consumer credit business. Its analytics team proposes three
enhancements.

**Enhancement one: an "affordability outreach" model** that identifies
customers in visible financial distress - missed payments elsewhere,
gambling-pattern spend, payday-loan usage - and targets them with urgent,
scarcity-framed offers for high-cost credit, timed for when the pattern
suggests they are most likely to accept. This is not a marketing question.
Exploiting a person's specific social or economic situation to materially
distort their behaviour, in a way likely to cause them significant harm, is
a prohibited practice - in force since February 2025. The component is an
ordinary propensity model; the practice is what is banned. Redirecting the
same model to flag those customers for forbearance support instead inverts
the purpose and takes the practice out of the prohibition entirely - same
component, opposite outcome at Gate 1.

**Enhancement two: a "customer reliability score"** assembled from data
unrelated to credit - social media conduct, complaint history with other
firms, lifestyle signals - used to deprioritise service or decline products
across contexts that have nothing to do with where the data came from. That
is social scoring: evaluating people over time on social behaviour or
personal characteristics, with the score producing detrimental treatment in
unrelated contexts or treatment disproportionate to the behaviour. Banned
outright. Contrast the score the team thinks it resembles: conventional
creditworthiness scoring built on financial data is not prohibited - it is
a listed **high-risk** use (deferred to December 2027, profiling blocks the
derogation), which is a different gate with different consequences. The
line between "banned" and "high-risk with a readiness plan" runs exactly
between those two projects, and a team that cannot articulate it will
either build the wrong one or kill the right one.

**Enhancement three: branch security cameras with biometric analysis** that
infers customers' likely religion or political leanings from appearance for
"risk segmentation". Biometric categorisation deducing sensitive traits is
prohibited - no security framing rescues it. Plain identity verification at
onboarding, by contrast, is expressly outside even the high-risk biometrics
item. In finance, Gate 1 outcomes turn almost entirely on purpose, not on
how sophisticated the model is.

### A healthcare environment

[HOSPITAL] is evaluating three AI deployments, and Gate 1 treats them
completely differently - including the one exception in the whole
prohibited list that people most often stretch.

**Deployment one: patient distress monitoring.** A ward system reads facial
expression and voice to flag pain, delirium or acute distress in patients
who cannot self-report, alerting clinical staff. Emotion inference is the
practice - but the ban on it is scoped to workplaces and education
institutions, and carries an express exception for systems intended for
medical or safety reasons. A clinical monitoring tool, procured and
deployed for patient care, sits inside that exception. What the exception
does NOT do is make the system free of the Act: emotion recognition remains
a listed high-risk use in its own right, and the live transparency duty
applies - the people exposed must be informed the system operates, and the
health data handled under data protection law. Escaping the ban is the
beginning of the analysis, not the end.

**Deployment two: staff wellbeing analytics.** The same vendor offers a
dashboard scoring nurses' stress and fatigue from voice, camera and shift
data, pitched to management as burnout prevention - a wellness framing, a
medical-sounding purpose. This is where the exception gets stretched, and
it should not be. Pointed at employees, this is inferring the emotions of
people in the workplace; the exception is for systems intended for medical
or safety reasons, not for workforce management wearing medical language.
This document takes the protective reading, stated as such, consistent with
the rest of the series. A fatigue-detection system genuinely operated
as a safety control (say, for surgeons or drivers, triggering rest rather
than ratings) presents a real boundary question - taken to counsel, not to
a product toggle. A wellbeing dashboard that feeds rostering and
performance conversations does not: it is the prohibited practice with a
softer name, banned since February 2025.

**Deployment three: emergency triage.** An AI system classifying emergency
calls and prioritising dispatch, or triaging emergency patients, sounds
like the most dangerous system in the building - and it is not banned at
all. It is a listed high-risk use: permitted, deferred to December 2027,
and exactly what the readiness track exists for. Meanwhile the least
dramatic system in the hospital - the staff wellbeing dashboard - is the
one the Act prohibits. Severity of consequence and position at Gate 1 are
different axes; that is why the gates are walked in order instead of
guessed from how alarming a system sounds.

## The three questions that replace the pyramid

For every AI system in the inventory, ask in order:

1. **What is banned already?** The prohibited practices have applied since
   February 2025, two more join in December 2026, and none of them can be
   risk-accepted. Anything caught is stopped, not managed.
2. **What is live already?** Transparency duties since August 2026; AI
   literacy since February 2025; and all of data protection law throughout.
   These apply now, to minimal and high-risk systems alike.
3. **What is deferred, and to when?** High-risk duties from December 2027
   (listed uses) or August 2028 (regulated products). Classify now, name an
   owner, date the plan, and make vendor readiness a contract term.

A system's answer to those three questions is its real position under the
Act. The pyramid cannot give it; the five-gate walkthrough in Part 2 can,
and this document is the why behind that design.

---

*Companion to Part 2 of the AI Governance Series. Educational material, not
legal advice. Every position here is verified against the consolidated
Artificial Intelligence Act of 27 July 2026; the Part 2 research note holds
the article-level citations and the source register lists the texts held.
Have classification and disclosure decisions on real systems reviewed by
qualified counsel.*
