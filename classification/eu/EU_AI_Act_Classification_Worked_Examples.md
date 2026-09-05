# Classifying Your AI Systems - Worked Examples for a Bank and a Hospital

**Series:** AI Governance Series - companion to Part 2 (Classifying AI systems by risk)
**Legal baseline:** the EU Artificial Intelligence Act as consolidated at 27 July 2026, after amendment by the Digital Omnibus
**Version:** 1.0
**Status:** Verified against the consolidated primary text. Citations in the Part 2 research note; texts held in the Part 2 source register.

*Educational material, not legal advice. The classifications below are worked
illustrations on invented systems, not opinions on any real product. Have your
DPO or legal counsel review before relying on any position here.*

---

## The method, in one page

You do not classify your organisation. You classify **one system at a time**,
and you write the answer down. For each AI system on your list, ask five
questions in order and stop at the first one that bites:

| # | Question | If yes |
|---|---|---|
| 1 | Is it a banned use? | Stop. It is illegal - drop it or turn the feature off. Applies since Feb 2025 |
| 2 | Is it a safety part of a product that needs safety approval? | High-risk. Rules bind Aug 2028 |
| 3 | Is it on the high-risk list? (jobs, credit, insurance, education, essential services, policing, migration, justice) | High-risk. Rules bind Dec 2027 |
| 4 | Does it talk to people, or make content, or read emotions? | You must tell people. Applies **now**, on top of any answer above |
| 5 | Anything left? | Yes - your staff must be competent to use it. Applies since Feb 2025 |

Three rules that decide most hard cases:

- **It is the use that counts, not the software.** The same model can be
  banned in one deployment and unremarkable in another. Classify the
  deployment.
- **Question 4 stacks.** It is not a tier. A high-risk system can owe
  disclosure too, and that duty is live today while the high-risk rules are
  not.
- **Being on the list is close to final.** There is a narrow way out for
  systems that do not really influence the outcome, but it disappears the
  moment the system profiles people - and claiming it requires written
  documentation and registration before deployment.

Write the outcome, the date, and an owner against every system. That record
is the deliverable. The rest of this document shows two organisations doing
exactly that.

---

## Example 1 - a retail bank

[BANK] is EU-established, uses AI bought from vendors, and builds nothing
itself. That makes it a **deployer** in every row below. The register it
produced:

| # | System | Outcome | Binds from | Do now |
|---|---|---|---|---|
| 1 | Website chatbot answering product questions | No tier duties, but **must disclose** | Disclosure live now | Make the chat window say it is an AI assistant at the first message |
| 2 | Credit scoring for personal loans | **High-risk** (essential services - creditworthiness) | 2 Dec 2027 | Name an owner; put vendor readiness into the contract |
| 3 | Card fraud detection | **No tier duties** - express exception | n/a | Keep the exception reasoning on file; it is a real carve-out, not an assumption |
| 4 | AML transaction monitoring | **No tier duties** - not on the list | n/a | Nothing under this Act; other financial-crime law is unaffected |
| 5 | CV screening for branch hiring | **High-risk** (employment - filtering applications) | 2 Dec 2027 | Same as row 2; also brief recruiters (question 5) |
| 6 | Marketing image generator | No tier duties, **marking duty on the vendor** | Live now | Ask the vendor how outputs are marked; disclose if a real person is depicted |
| 7 | Call-centre tool scoring staff stress and engagement | **BANNED** | Illegal since Feb 2025 | Turn it off. Record the decision |
| 8 | Voice-stress "truthfulness" scoring on loan calls | Declined at procurement | - | See the note below - this is the one that repays reading twice |

### Rows worth expanding

**Row 3 - fraud detection is genuinely different from credit scoring.** Both
score customers, both use similar models, and only one is high-risk. The
high-risk list covers systems that evaluate creditworthiness or set a credit
score, and it expressly excludes systems used to detect financial fraud.
This is not a loophole to lean on: if the same engine also produces a
lending decision, that use is high-risk on its own, and separating them
means separating them in fact, not just on paper.

**Row 4 - not everything serious is listed.** AML monitoring is heavily
regulated, business-critical, and produces consequences for customers. It is
still not in any of the eight high-risk areas. "Important to the bank" and
"high-risk under the AI Act" are different tests, and confusing them is how
compliance budgets end up in the wrong place.

**Row 7 - the banned one is the ordinary one.** Nobody procures "an illegal
AI system". They procure a call-centre quality platform, and it has an
engagement or sentiment module aimed at agents. Inferring emotions of people
in the workplace is prohibited outright, and has been since February 2025.
The platform is fine; the module is not. Disable it and write down that you
did.

**Row 8 - one product, three different answers.** A vendor offers voice
analysis that estimates whether a caller is being truthful.

- Pointed at **staff or job candidates**: emotion inference in the workplace.
  **Banned**, since February 2025.
- Pointed at **customers**: not banned - but emotion recognition is on the
  high-risk list in its own right, and the duty to tell people it is running
  is live **today**.
- The bank's conclusion: a system whose business case depends on customers
  not knowing it is running cannot survive its own disclosure duty. Declined
  at procurement, before a three-year contract existed.

---

## Example 2 - a hospital group

[HOSPITAL] runs clinical and administrative AI. It is a deployer of vendor
systems, except where noted. Note how badly intuition performs here: the
most alarming system on the list is permitted, and the most innocuous one is
banned.

| # | System | Outcome | Binds from | Do now |
|---|---|---|---|---|
| 1 | Radiology triage module inside a CE-marked device | **High-risk** (product route) | 2 Aug 2028 | Confirm the manufacturer's conformity plan covers the AI requirements |
| 2 | Emergency call classification and dispatch priority | **High-risk** (essential services) | 2 Dec 2027 | Name an owner; plan human oversight and logging now |
| 3 | Ward monitoring inferring pain or distress in patients who cannot speak | Not banned - **medical exception**. Still **high-risk** (emotion recognition) **and must disclose** | Disclosure live now; high-risk 2 Dec 2027 | Tell patients and families it operates; handle health data under data protection law |
| 4 | Dashboard scoring nurses' stress and burnout risk | **BANNED** | Illegal since Feb 2025 | Turn it off. Wellbeing framing does not rescue it |
| 5 | Nurse rostering optimiser | **Depends on how it decides** - see below | Dec 2027 if it allocates on behaviour or traits | Read the vendor's actual logic before deciding |
| 6 | Recruitment screening for clinical posts | **High-risk** (employment) | 2 Dec 2027 | Same track as the bank's row 5 |
| 7 | Appointment no-show prediction | **No tier duties** - not on the list | n/a | Watch it for fairness anyway; that is policy, not this Act |
| 8 | Facial recognition on entrances for security | Not banned here - **high-risk** (remote biometric identification) | 2 Dec 2027 | Data protection law bites hardest and bites now |

### Rows worth expanding

**Row 3 - the exception people stretch.** The ban on inferring emotions is
scoped to workplaces and education institutions, and it carries an express
exception for systems intended for medical or safety reasons. A ward
monitor watching patients for pain or delirium sits inside that exception.
What the exception does **not** do is remove the system from the Act:
emotion recognition is on the high-risk list, and the duty to inform the
people exposed to it is live now. Escaping question 1 is the start of the
analysis, not the end of it.

**Row 4 - the same technology, one floor away.** Point the same capability
at nurses and call it burnout prevention, and it is inferring the emotions
of people in the workplace. The medical exception is for systems intended
for medical or safety reasons, not for workforce management wearing medical
language. A genuine safety control - fatigue detection that triggers rest
rather than ratings - is a real boundary question for counsel. A dashboard
feeding rostering and performance conversations is not: it is the
prohibited practice with a softer name. This document takes the protective
reading, and says so.

**Row 5 - the honest edge case.** The high-risk list covers systems that
allocate tasks **based on individual behaviour or personal traits or
characteristics**, and systems that monitor and evaluate performance. A
rostering tool that solves for availability, contracted hours, skills and
statutory rest is not obviously doing either. One that scores individual
nurses on productivity or "reliability" and allocates the desirable shifts
accordingly is squarely inside it. Nobody can classify this from the
product name - somebody has to read what the optimiser actually optimises.
That is the work, and it is why the record has an owner's name on it.

**Row 8 - not banned, but not free.** Real-time remote biometric
identification in public spaces is prohibited **for law enforcement**
purposes, outside narrow authorised cases. A hospital running its own
security is not law enforcement, so the prohibition does not catch it. What
does catch it: remote biometric identification is on the high-risk list, and
data protection law governs biometric data today, with force. "Not banned"
is a long way from "go ahead".

**Rows 1, 2 and 7 together - intuition is not a classifier.** The radiology
module and the emergency triage system sound like the most dangerous AI in
the building. Both are permitted, both are high-risk, both have a date. The
no-show predictor sounds trivial and is outside the tiers entirely. And the
staff wellbeing dashboard - the one that sounded like a benefit - is the
only illegal system on the list. Severity of consequence and legal
classification are different axes. Walk the five questions; do not guess
from how alarming a system sounds.

---

## The blank record

Copy this per system. It is deliberately short - a record that takes an hour
per system gets abandoned.

```
System name:
What it actually does (one sentence):
Who supplies it / did we build it:
Our role:            provider / deployer
Where it is used:    which country, which people

Q1  Banned use?                              yes / no      note:
Q2  Safety part of a regulated product?      yes / no      note:
Q3  On the high-risk list?                   yes / no      which item:
    If listed - does it profile people?      yes / no
Q4  Talks to people / makes content /
    reads emotions?                          yes / no      what we disclose:
Q5  Staff competent to use it?               yes / no      training:

OUTCOME:             banned / high-risk / no tier duties
DUTIES LIVE TODAY:
DUTIES BINDING FROM: (date)
OWNER:
NEXT REVIEW:
```

Two habits make the register worth keeping. **Classify at approval, not at
commencement** - the system you sign a three-year contract for today will
still be running when its date arrives, and vendor readiness is a
negotiating point now and a crisis later. And **re-run the questions when
the use changes**, not when the software changes: the same tool pointed at a
different group of people can move from unremarkable to illegal without a
single line of code changing.

---

*Companion to Part 2 of the AI Governance Series. Educational material, not
legal advice. Every classification above rests on provisions verified in the
Part 2 research note against the consolidated Artificial Intelligence Act of
27 July 2026. Systems and organisations are invented for illustration. Have
real classification decisions reviewed by qualified counsel.*
