# AI Governance - Enterprise Annex - Canada

### Operating two privacy regimes, the automated-decision determination and the incident duties across the AI portfolio

**Organisation:** [ORGANISATION]
**Effective date:** [DATE]  **Version:** 1.0
**Owner:** [Accountable executive for AI]  **Privacy lead:** [Person in charge of the protection of personal information]
**Classification:** Internal
**Companion to:** Artificial Intelligence Acceptable Use Policy - Canada (policy clause references below are to that document)

---

## A1. Governance structure and accountability

A1.1 [ORGANISATION] is responsible for personal information under its control,
including information transferred to third parties for processing. Accountability for
compliance rests with a designated individual, whose identity is made known on
request; in Quebec that person is the person exercising the highest authority, who may
delegate in writing, and whose title and contact information are published.
[ORGANISATION] has one person in charge for both regimes: [title].

A1.2 The **AI Governance Committee** comprises the accountable executive (chair), the
person in charge, the CISO, [Legal], [Risk] and the business owners of Level 3 and
Level 4 systems. It approves Level 4 uses, owns the policy and this annex, reviews the
AI register quarterly, receives the monitoring and incident reports at A9, and
reviews approval and override rates on Level 4 decisions.

A1.3 The **person in charge** approves Level 3 uses, owns privacy impact assessments,
is consulted from the outset of every project to acquire, develop or overhaul a system
involving personal information, holds the clause 12 determinations, is consulted on
every incident risk assessment, and is the contact for complaints and requests.

A1.4 Every AI system has a **named accountable person** who owns its register entry,
its assessments, testing and monitoring. Where a system involves several parties
(supplier, model developer, integrator), the register records who is responsible for
each part of the supply chain.

A1.5 This policy and annex are the policies and practices that give effect to the
privacy principles for AI: procedures to protect personal information, to receive and
respond to complaints, to train staff, and to explain the organisation's practices.

## A2. AI system inventory: the register

A2.1 The AI register lists every AI system in use or under evaluation, including AI
embedded in procured products and AI features enabled inside approved products. An AI
feature switched on is a new entry.

A2.2 Each entry records: system and supplier; purpose and business owner; accountable
person; level of use; the personal information used and its sensitivity; the legal
authority for each collection, use and disclosure (the identified purpose, the consent
obtained and its form, or the exception relied on); whether the system generates or
infers personal information; whether it identifies, locates or profiles people, and
whether those functions are off by default; where data is processed and stored, and
whether it leaves Quebec or Canada; the supplier's rights over inputs and outputs; the
clause 12 determination; the privacy impact assessment and, for Level 4, the
algorithmic impact assessment; testing and monitoring; retention periods; supply-chain
accountabilities; and whether the system is customer-facing or reaches minors.

A2.3 The register is the source of the openness statements at policy clause 8 and of
the quarterly review. Material changes reopen approval.

## A3. Regime-readiness register

A3.1 The set relies on nothing in Bill C-36. This register tracks what would change
if it were enacted, and the items that remain open.

| Item | Source | Status | Owner |
|---|---|---|---|
| Bill C-36 progress: second reading, committee, Senate, Royal Assent, coming-into-force order | Parliament of Canada | First reading 15 June 2026; monitored | [Legal] |
| If enacted: policy clause 13.2 (explanation and representations for substantially automated decisions) becomes a duty rather than a house standard; the public policies at clause 8 must give a general account of automated decision system use | Bill C-36 as introduced | Pending | Person in charge |
| If enacted: appropriate-purposes factors (necessity, effectiveness, less intrusive means, proportionality) become statutory; clause 17 already applies them | Bill C-36 as introduced | Pending | Person in charge |
| Consolidated Quebec P-39.1 text (Légis Québec) added to the source register for the "updated to" date | Source register | Site unavailable at build; open | Person in charge |
| Regulations under both Acts on breach records, incident notices and publicly available information | Source register | Not held; open | [Legal] |
| Alberta and British Columbia Acts, where [ORGANISATION] has staff or customers there | Policy clause 22 | Not held; open | [Legal] |

## A4. The automated-decision determination in operation

A4.1 For every system bearing on a decision about a person, the accountable person
records the two-limb determination at policy clause 12: exclusively automated
(Quebec duty), or substantially contributed to (house standard), or neither.

A4.2 The determination is made on the use, not the tool, and on how the decision is
actually made, not how the process is described. A person who signs what the system
proposes without the information, time or authority to decide otherwise is not
exercising judgment, and the decision is recorded as exclusively automated.

A4.3 **Worked entries** (illustrative):

| System and use | Exclusively automated? | Substantially contributes? | Outcome |
|---|---|---|---|
| Credit model auto-approving below a threshold, no human step | Yes | - | Quebec duty applies: inform, explain on request, observations to a reviewer |
| Applicant screening assistant ranking CVs for a recruiter who reads the top ten | No | Yes | House standard: same three things provided |
| Fraud engine blocking a transaction pending review by an analyst within the hour | No, if the analyst can and does reverse | Yes | House standard; override rate monitored |
| Fraud engine blocking a transaction with no review path | Yes | - | Quebec duty applies |
| Chatbot answering product questions, no decision | No | No | Customer-facing disclosure only |

A4.4 For each system inside either limb, the register records: how the person is
informed and when; the template for the explanation (personal information used,
reasons, principal factors and parameters, right to correction); who the reviewing
member of staff is and how observations reach them; and how the review is recorded.

A4.5 The Quebec duty attaches at the moment the person is informed of the decision.
Systems are designed so that the notice is part of the decision communication, not a
separate step that can be missed.

## A5. Privacy impact assessments

A5.1 A privacy impact assessment is completed for every project to acquire, develop or
overhaul an AI system involving the collection, use, communication, keeping or
destruction of personal information; before any personal information is communicated
outside Quebec; and before any Level 3 or Level 4 use, any generation or inference of
personal information, any scraping or dataset acquisition, any fine-tuning, any
profiling and any customer-facing AI. The person in charge is consulted from the
outset.

A5.2 The assessment is proportionate to the sensitivity of the information, the
purposes, the quantity and distribution, and the storage medium. It addresses, as a
minimum: the identified purposes and whether the AI use is within them; the legal
authority and the form of consent; sensitivity; whether the system generates or infers
personal information and the authority for that collection; necessity and
proportionality (policy clause 17); accuracy, validity and reliability; safeguards and
the AI-specific threats; retention; openness; the automated-decision determination;
identification, location and profiling functions; minors and vulnerable groups; and,
for Level 4, an algorithmic impact assessment covering bias and fairness.

A5.3 The person in charge may propose protection measures at any stage: a person
responsible for implementing them, measures for project documents, a description of
participants' responsibilities, and training for participants.

A5.4 Where the assessment cannot establish legal authority for a proposed use, the
use does not proceed until consent is obtained or the design is changed.

## A6. Transfers and suppliers

A6.1 **Before personal information leaves Quebec** for an AI supplier or cloud
service, the assessment at A5 considers the sensitivity, the purposes, the protection
measures including contractual ones, and the legal framework of the receiving state.
The communication proceeds only if the assessment establishes adequate protection, in
light of generally recognised personal information protection principles, and under
a written agreement that reflects the assessment and any mitigation agreed.
[ORGANISATION] applies the same assessment to every cross-border AI supplier whatever
the origin of the data.

A6.2 **Federally**, information transferred to a third party for processing remains
[ORGANISATION]'s responsibility, and contractual or other means provide a comparable
level of protection while it is processed.

A6.3 Supplier terms are reviewed before engagement for: rights over inputs and
outputs, including any right to train; sub-processors; data location; safeguards and
incident history; the supplier's testing for prompt injection, model inversion and
jailbreaking; deletion on instruction; and evidence of access. Suppliers are asked for
documentation of the datasets used to train the model, their sources and legal
authority, known failure cases, and any accuracy limitations, as the commissioners'
principles expect developers and providers to publish.

A6.4 The contract provides for: processing only for [ORGANISATION]'s purposes and on
its instructions; no use of [ORGANISATION] data to train or improve the supplier's
models unless approved under policy clause 16; safeguards; incident notification
without delay and in time for [ORGANISATION] to notify promptly; return or deletion;
audit or assurance rights; and the transfer terms at A6.1.

## A7. Openness and notice in operation

A7.1 The privacy policy and the confidentiality policy published on
[ORGANISATION]'s website are drafted in clear and simple language and cover the
matters at policy clause 8.1, including a general account of AI uses of personal
information and of any automated decision-making.

A7.2 Notices at collection state AI purposes, generation or inference of personal
information, disclosure to AI suppliers, communication outside Quebec or Canada, and,
where technology can identify, locate or profile the person, the use of that
technology and the means to activate those functions.

A7.3 Customer-facing AI systems carry the disclosure at policy clause 15.1 at the
start of every interaction.

## A8. Testing, monitoring and assurance

A8.1 Systems are tested before approval for validity and reliability for the intended
purpose, for inaccurate, biased and harmful outputs, for surfacing personal
information about others, and adversarially for unintended inappropriate uses and for
prompt injection, model inversion and jailbreaking.

A8.2 Level 4 systems are tested for differential outcomes on protected grounds before
deployment and at least [annually]; the training data's representation of any specific
group the use relates to is assessed.

A8.3 Monitoring after deployment is matched to the level: performance drift,
accuracy, bias, inappropriate uses and biased outcomes not disclosed as limitations
(which are reported to the supplier), and, for Level 4, approval and override rates.

A8.4 Human override points are documented for every system, and alternative pathways
maintained so that critical functions continue if a system fails or is withdrawn.

## A9. Incident response

A9.1 The incident process at policy clause 20.5 is operated by [Security] with the
person in charge. On any suspected confidentiality incident or breach of security
safeguards involving an AI tool: reasonable measures to reduce the risk of injury and
prevent recurrence; a risk assessment with the person in charge on sensitivity,
anticipated consequences and likelihood of injurious use; where there is a risk of
serious injury, prompt notice to the Commission d'accès à l'information and to the
persons concerned; where there is a real risk of significant harm, a report to the
Privacy Commissioner of Canada and conspicuous, direct notice to individuals as soon
as feasible after determining the breach has occurred; and an entry in the incident
register in every case.

A9.2 AI-specific incident types are recognised and drilled: personal information
entered into an unapproved or public tool; a tool surfacing another person's data; a
supplier breach; extraction of training or context data from a model; an agent acting
outside its approved actions; a Level 4 system producing a systematically wrong or
discriminatory result; a use found to be within a no-go zone.

A9.3 Every AI incident, whether or not a privacy incident, is recorded, investigated
and analysed, and the lessons applied.

## A10. Individuals' rights and contestability

A10.1 Access, challenge and correction requests concerning personal information in or
generated by AI tools follow policy clause 11.4. Records are kept so that a request
about a decision can be meaningfully answered; information used to make a decision is
retained long enough for that.

A10.2 For decisions inside either limb of the clause 12 determination, the notice,
explanation and observations process at policy clause 13 is operated as recorded in
the register (A4.4).

A10.3 Complaints follow the mechanism in the privacy policy; patterns are reported to
the AI Governance Committee.

## A11. Training and awareness

A11.1 Staff training follows policy clause 21. Reviewers of Level 4 decisions are
trained on what a meaningful review requires and on the rights at clause 13.

A11.2 The person in charge and [Legal] maintain awareness of Bill C-36's progress,
of guidance from the Privacy Commissioner of Canada and the Commission d'accès à
l'information, of regulations under either Act, and of the substantially similar
provincial Acts where [ORGANISATION] operates.

## A12. Metrics reported to the AI Governance Committee

- Systems on the register by level; new, changed and retired
- Systems inside each limb of the clause 12 determination
- Privacy impact assessments open, completed and overdue; transfer assessments
- Level 4 approval and override rates by system
- Incidents by type; notifications to each commissioner; register entries
- Access, correction and explanation requests, and time to resolve
- Testing and monitoring findings, including bias testing results
- Training completion for users, accountable people and reviewers
- Regime-readiness register status

## A13. Scope of this annex and what is not held

A13.1 This annex operates the Personal Information Protection and Electronic
Documents Act as consolidated to 21 June 2026, the Act respecting the protection of
personal information in the private sector as amended by 2021, chapter 25, the
commissioners' generative AI principles of December 2023 and the Privacy Commissioner
of Canada's business guidance, and reads Bill C-36 as introduced without relying on it.

A13.2 **It does not hold**, and therefore does not state: the consolidated Quebec Act
from Légis Québec (unavailable at build); the regulations under either Act; Alberta's
and British Columbia's Acts; provincial health-information Acts; human rights and
consumer protection law; the federal Directive on Automated Decision-Making and its
companion guides, which bind federal institutions; and guidance the Commission d'accès
à l'information has issued on Law 25. Each is named in policy clause 22 as an open
verification and recorded in the source register.

---

## Version history

| Version | Date | Change |
|---|---|---|
| 1.0 | 3 September 2026 | Initial annex, published within its stated scope. Every obligation traced to the held instruments in the research note. |

---

*Educational template - not legal advice. Review by qualified counsel before adoption.*
