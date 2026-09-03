# AI Governance Series - practical artifacts, verified against primary law

## What is AI governance?

AI governance is how an organisation directs and controls its use of
artificial intelligence: who may use which AI tools, on what data, under whose
oversight, with what checks before an output is relied on or a system goes
live - and who is accountable when it goes wrong. It covers everything from an
employee pasting text into a chatbot to an autonomous agent acting on the
organisation's behalf.

## Why it matters

Two forces make this urgent. First, AI has moved into decisions that affect
people - hiring, credit, eligibility, access to services - and into everyday
workflows that touch personal and confidential data. Ungoverned, that produces
concrete harm: regulatory fines, biased outcomes, data privacy leaks,
reputational damage, security vulnerabilities, intellectual property loss,
shadow AI growth, financial waste, lack of accountability, and loss of
customer trust.

Second, the law has caught up. Jurisdictions now attach real obligations to
automated processing - lawful grounds, impact assessments, transparency,
human oversight, transfer restrictions, breach deadlines - and those
obligations differ by country and stack rather than substitute. Some carry
criminal penalties. A firm processing data from more than one country has to
satisfy them all at once, which is why a generic "global AI policy" fails and
jurisdiction-specific governance is the working answer.

## The series

This repository is a series. Each part becomes a working, verified artifact
here as it is published - policies people can follow, obligations checked
against the consolidated primary legislation, and research notes that show
the working.

| # | In this series | Status |
|---|---|---|
| 1 | **AI acceptable use policies** | **Live** - ten jurisdictions: UK, Bahrain, EU, India, Singapore, UAE, Oman, US, and China published and verified within their stated scopes; Saudi Arabia published, government data scope ([below](#1-ai-acceptable-use-policies)) |
| 2 | Classifying AI systems by risk | Coming |
| 3 | Obligations across jurisdictions | Coming - a comparison matrix across the UK, EU, India, Singapore, and the GCC |
| 4 | Bias and fairness testing | Coming |
| 5 | AI risk registers and model inventories | Coming |
| 6 | Impact assessments | Coming |
| 7 | Assessing AI vendors | Coming |
| 8 | Incident response and human oversight | Coming |

**Educational, not legal advice.** Every artifact is a template for learning
and adaptation. Have your data protection lead or qualified legal counsel
review anything before adoption.

## What makes this different

- **Jurisdiction depth.** Most AI governance material stops at the EU and US.
  This project builds verified, jurisdiction-specific artifacts - including the
  GCC (Bahrain, Saudi Arabia, UAE, Oman), where verified, primary-source
  coverage is hardest to find.
- **Primary sources only.** Obligations are verified against the consolidated
  legislation texts, not summaries or blog posts. Each artifact ships with a
  research note recording every obligation, its source, and the verification
  date. Where a jurisdiction's authoritative text is not English (Bahrain's is
  Arabic), that is treated as a finding, not a footnote.
- **Usable rules.** Obligations are written as rules a team can follow. Article
  numbers live in the research notes, not the policy text.

## 1. AI acceptable use policies

The first artifact of the series: complete, per-jurisdiction policy sets, each
built on the same skeleton so they can be read side by side - the foundation
for the comparison matrix at part 3. Ten jurisdictions are live: the UK,
Bahrain, the EU, India, Singapore, Saudi Arabia, the UAE, Oman, the United
States, and China.

Each policy scales its controls through **levels of use**. The levels are the
organisation's own classification, not categories defined in any law - but
every level boundary is placed where a statutory duty actually begins, so
classifying a use also identifies the legal obligations that attach to it.
Each folder README states how its levels map to that jurisdiction's law.

### United Kingdom - published

**[policies/uk/](policies/uk/)** - full policy, one-page staff guide,
enterprise governance annex, and research note. Word versions in
[downloads](policies/uk/downloads/).

Built on the UK data protection regime as it stands after the Data (Use and
Access) Act 2025:

- [UK GDPR](https://www.legislation.gov.uk/eur/2016/679/contents) and the
  [Data Protection Act 2018](https://www.legislation.gov.uk/ukpga/2018/12/contents),
  as amended - lawful basis, data minimisation, impact assessments,
  automated decision-making safeguards, breach notification, transfers
- [Data (Use and Access) Act 2025](https://www.legislation.gov.uk/ukpga/2025/18/contents/data.html) -
  the reframed automated-decision rules, the new complaints-handling duty,
  and the reworded international transfer test
- [Equality Act 2010](https://www.legislation.gov.uk/ukpga/2010/15/contents) -
  non-discrimination in AI-informed decisions
- [Copyright, Designs and Patents Act 1988](https://www.legislation.gov.uk/ukpga/1988/48/contents) -
  intellectual property in AI inputs and outputs
- [ICO guidance on AI and data protection](https://ico.org.uk/for-organisations/uk-gdpr-guidance-and-resources/artificial-intelligence/guidance-on-ai-and-data-protection/)

### Kingdom of Bahrain - published

**[policies/bahrain/](policies/bahrain/)** - full policy, one-page staff
guide, enterprise governance annex, research note, and source register. Word
versions in [downloads](policies/bahrain/downloads/). Every cited obligation
verified against the enacted Arabic; the verification record - gates stated,
then closed in public - is in the [folder README](policies/bahrain/README.md).

Built on Bahrain's personal data protection regime - a system with features
that reshape AI governance: prior notice to the regulator before automated
processing, prior written authorisation for defined categories (where silence
past the statutory period is a refusal), and criminal penalties attached to
several duties:

- Personal Data Protection Law - Law No. (30) of 2018
  ([Personal Data Protection Authority](https://www.pdp.gov.bh/en/regulations.html))
- The implementing Ministerial Orders Nos. 42-51 of 2022
  ([executive decisions](https://www.pdp.gov.bh/en/executive-decisions.html)) -
  transfers outside the Kingdom and the adequate-countries record, technical
  and organisational measures, notifications and prior authorisation,
  sensitive personal data, Data Protection Guardians, data subject rights,
  complaints
- Read against the enacted Arabic in the
  [Official Gazette](https://www.legalaffairs.gov.bh/OG/3593.pdf) where held -
  Bahraini law is enacted in Arabic, and comparing the enacted text with the
  official English translations surfaced substantive divergences, recorded in
  the research note

### European Union - published

**[policies/eu/](policies/eu/)** - full policy, enterprise governance annex,
research note, and source register. Word versions in
[downloads](policies/eu/downloads/). Annex III read item by item against the
consolidated text; the verification record is in the
[folder README](policies/eu/README.md).

Built on Union law as it stands after the Digital Omnibus - a framework where
some AI practices are prohibited outright and the rest commences in stages:

- [AI Act - Regulation (EU) 2024/1689, consolidated 27 July 2026](https://eur-lex.europa.eu/eli/reg/2024/1689/2026-07-27/eng) -
  prohibited practices, the staged commencement schedule, and the transparency
  obligations in force since August 2026
- [Digital Omnibus - Regulation (EU) 2026/1744](https://eur-lex.europa.eu/eli/reg/2026/1744/oj/eng) -
  the amending instrument that deferred the high-risk regime to December 2027
  and August 2028 (a deferral, not an exemption - the set includes a readiness
  register so the time is used, not wasted)
- [GDPR - Regulation (EU) 2016/679](https://eur-lex.europa.eu/eli/reg/2016/679/oj/eng) -
  lawful basis, automated decisions, impact assessments, breach notification,
  transfers

### India - published

**[policies/india/](policies/india/)** - full policy, enterprise governance annex,
research note, and source register. Word versions in
[downloads](policies/india/downloads/). Verified against the Act, its commencement
notification and the rules; the verification record, including one correction
made when the Act was obtained, is in the
[folder README](policies/india/README.md).

Built on a framework that is enacted but largely not yet in force - the operating
obligations, the individual rights and the penalties all commence on 13 May 2027:

- [Digital Personal Data Protection Act, 2023 - No. 22 of 2023](https://www.meity.gov.in/static/uploads/2024/06/2bf1f0e9f04e6fb4f8fef35e82c42aa5.pdf) -
  grounds for processing, consent, the legitimate uses, the accuracy duty for
  decisions, children's data, Significant Data Fiduciaries, rights, and the
  penalty Schedule
- [Commencement notification - G.S.R. 843(E), 13 November 2025](https://www.meity.gov.in/static/uploads/2025/11/c56ceae6c383460ca69577428d36828b.pdf) -
  the Act's three tranches; read with the rules' own commencement in rule 1,
  since citing one without the other gives the wrong answer
- [Digital Personal Data Protection Rules, 2025 - G.S.R. 846(E)](https://www.meity.gov.in/static/uploads/2025/11/53450e6e5dc0bfa85ebd78686cadad39.pdf) -
  notice, security safeguards, breach intimation on two clocks, the one-year
  retention floor, rights machinery, and the ninety-day grievance period

### Kingdom of Saudi Arabia - published, government data scope

**[policies/saudi/](policies/saudi/)** - full policy, enterprise governance annex,
research note, and source register. Word versions in
[downloads](policies/saudi/downloads/). Every citation verified against the three
NDMO instruments held; the Implementing Regulation of the Personal Data
Protection Law, read in full on 2 September 2026, corroborates the set and
contradicts nothing in it. Scope and the remaining gates are in the
[folder README](policies/saudi/README.md).

**This set governs government data only** - public entities and business partners
handling government data. The PDPL itself and the Transfer Regulation are not yet
held; this set cannot serve a private organisation processing its own customers or
employees, and says so at section 1.1. The private-sector extension is the recorded
next step, with the Implementing Regulation's AI hooks - impact assessment on
dataset-linking, new technologies and automated decisions; explicit consent for
solely-automated decisions - already mapped in the research note. Three NDMO
instruments underpin the set:

- [National Data Management and Personal Data Protection Standards - v1.5 (2021)](https://ndmo.gov.sa) -
  personal data protection domain, classification controls, and the data management
  organisation roles
- [Data Classification Policy - v1 (2020)](https://ndmo.gov.sa) -
  the four classification levels and the principle that the highest level governs a
  combined dataset
- [Data Sharing Policy - v2.0 (2024)](https://ndmo.gov.sa) -
  the eight principles and the agreement contents that govern sharing government data
  with any external party, including AI vendors

### United Arab Emirates - published, DIFC scope

**[policies/uae/](policies/uae/)** - full policy, enterprise governance annex,
research note, and source register. Word versions in
[downloads](policies/uae/downloads/). Written for a DIFC-registered entity,
with the ADGM and federal breach positions stated - and nothing else asserted
about those regimes. Evidence tiers and open gates are in the
[folder README](policies/uae/README.md).

Three things make this edition unlike any other in the series. The UAE is
**three data protection jurisdictions, not one** - DIFC, ADGM and the federal
regime, with three different answers to the same breach question, and the free
zones an exclusion from the federal law rather than a variation on it. The
DIFC has the series' only **genuinely AI-specific instrument** - a
certification regime for autonomous and semi-autonomous systems processing
personal data, where high-risk use is gated on certification rather than
documented after the fact. And the regime's boundary is **autonomy, not
automation** - a tool becomes a regulated System the moment a vendor adds
tool-use, retrieval, memory or planning. Built on:

- DIFC Regulation 10 Accreditation and Certification Framework for Autonomous
  and Semi-Autonomous Systems Processing Personal Data
  ([DIFC Commissioner of Data Protection](https://www.difc.com/business/registrars-and-commissioners/commissioner-of-data-protection)) -
  read in full; the certification gate, the System definition, self-defined
  purposes, the Automated Systems Officer, bias and data quality evidence
- The three regimes' breach positions, verified against the official texts -
  including the finding that the widely repeated federal "72 hours" is a
  misattribution: the federal Executive Regulations that would set a period
  have not been issued, and the real 72-hour duty sits in ADGM

### Sultanate of Oman - published

**[policies/oman/](policies/oman/)** - full policy, enterprise governance
annex, research note, and source register. Word versions in
[downloads](policies/oman/downloads/). Written from the enacted Arabic texts
and checked against MTCIT's official English renderings - the Arabic governs,
and the divergences found between the two are recorded in the
[folder README](policies/oman/README.md) and source register.

Oman is one of the few jurisdictions anywhere with a **national AI policy that
binds by its own terms**: it states controls that using and developing
organisations commit to, it reaches the private sector, and it is enforced
through each institution's own sector regulator. Two findings shape the rest of
the edition. There are **two 72-hour breach clocks with different triggers** -
one to the regulator, one to the individual - and a breach can cross one
threshold and not the other. And **cross-border transfer carries the
framework's dominant penalty**: OMR 100,000 to 500,000, against a maximum of
OMR 20,000 for anything else in the law, which makes processing location a
gating question for every AI tool. Built on:

- [Personal Data Protection Law - Royal Decree 6/2022](https://mjla.gov.om/eng/legislation/decrees/details.aspx?Id=1397&type=L) -
  explicit consent as the default, the sensitive-category permit, data subject
  rights, breach notification, cross-border transfer, and the penalty structure
- Executive Regulations - Ministerial Decision 34/2024
  ([MTCIT personal data protection](https://mtcit.gov.om/sectors/governance/personal)) -
  the permit machinery and timetable, the two breach clocks, the transfer
  assessment, the Personal Data Protection Officer, and the complaints process
- The national policy for the safe and ethical use of AI systems (MTCIT,
  April 2025) - ten controls for using AI systems, thirteen for developing
  them, and the ethical principles, including a data-source traceability
  requirement that must be designed in

### Singapore - published

**[policies/singapore/](policies/singapore/)** - full policy, enterprise
governance annex, research note, and source register. Word versions in
[downloads](policies/singapore/downloads/). Every citation verified by direct
reading of the enacted Act; open gates - the subordinate legislation and the
regulator's AI guidelines - are stated in the
[folder README](policies/singapore/README.md).

Singapore's law is technology-neutral: no AI statute, no prohibited-practice
list, no right against automated decisions - and the set says so instead of
importing obligations from elsewhere. What it does have reshapes an
acceptable use policy from an unusual angle: **unauthorised disclosure or use
of personal data is a personal criminal offence turning on what the
organisation authorised**, which makes the policy itself the boundary of an
individual's criminal exposure; AI-inferred data about a person is
**accessible but not correctable** under the statute (a house standard closes
the gap); and the breach clock runs **from the notifiability assessment, not
from discovery**. Built on:

- [Personal Data Protection Act 2012](https://sso.agc.gov.sg/Act/PDPA2012) -
  2020 Revised Edition as amended, current to Act 19 of 2025: consent and its
  alternatives, purpose limitation, accuracy, protection, retention,
  transfers, access and correction, breach notification, the data
  intermediary regime, offences and enforcement

### United States - published, scoped

**[policies/us/](policies/us/)** - full policy, enterprise governance annex,
research note, and source register. Word versions in
[downloads](policies/us/downloads/). Scoped honestly: the federal sectoral
baseline plus California and Colorado, with every other state named as not
held - because there is no single US AI or privacy statute, and a set claiming
otherwise would be wrong the way a single global policy is wrong, one level
down. Open gates are in the [folder README](policies/us/README.md).

Three findings shape this edition. Colorado's AI Act duties are **in force
now** - the special-session amendment moved every operative date to 30 June
2026, so citing the 2024 act alone gives the wrong commencement. **Two
different AI tests cover overlapping ground** - Colorado catches systems that
are a substantial factor in a consequential decision, California's ADMT
regulations catch technology that substantially replaces human decisionmaking,
and the same tool can be inside one and outside the other. And in Colorado, a
**governance framework has legal effect**: the statute names the NIST AI RMF
and ISO/IEC 42001, with compliance supporting a rebuttable presumption of
reasonable care and an affirmative defense. Built on:

- Colorado SB 24-205 as amended by SB 25B-004
  ([leg.colorado.gov](https://leg.colorado.gov/bills/sb24-205)) - the high-risk
  AI regime: developer and deployer duties, impact assessments, consumer
  notices, adverse-decision rights, the ninety-day discrimination notice
- [CCPA as amended](https://leginfo.legislature.ca.gov/faces/codes_displayText.xhtml?division=3.&part=4.&lawCode=CIV&title=1.81.5)
  and the [CPPA's approved regulations](https://cppa.ca.gov/regulations/) -
  automated decisionmaking technology, risk assessments submitted to the
  regulator, cybersecurity audits
- The federal sectoral baseline - FTC Act s.5, FCRA adverse action, COPPA,
  GLBA Safeguards, HIPAA ([govinfo.gov](https://www.govinfo.gov),
  [ecfr.gov](https://www.ecfr.gov)) - and the
  [NIST AI Risk Management Framework](https://nvlpubs.nist.gov/nistpubs/ai/NIST.AI.100-1.pdf),
  which Colorado's statute names in its own text

### People's Republic of China - published

**[policies/china/](policies/china/)** - full policy, enterprise governance
annex, research note, and source register. Word versions in
[downloads](policies/china/downloads/). PRC law is enacted in Chinese with no
official English translation, so every citation was verified against the
Chinese texts directly; the verification record is in the
[folder README](policies/china/README.md).

China regulates AI by regulating service types - recommendation algorithms,
deep synthesis, generative AI, content labelling, and, since July 2026,
anthropomorphic interaction services - all resting on three pillar laws and
the 2025 data regulations. Two findings shape this edition. The **2025
amendment to the Cybersecurity Law renumbered the law** and added an AI
article, so eight years of familiar citations now point at the wrong
provisions. And the generative AI measures reach **services offered to the
public in China while excluding internal enterprise use** - one feature
toggle can convert an internal tool into a regulated public service, so the
policy makes that line a recorded determination for every tool. Built on:

- The three pillar laws - the
  [Cybersecurity Law as amended 2025](https://flk.npc.gov.cn/), the
  [Data Security Law](https://flk.npc.gov.cn/), and the
  [Personal Information Protection Law](https://flk.npc.gov.cn/) - from the
  National Database of Laws and Regulations
- The [Network Data Security Management Regulations](https://flk.npc.gov.cn/),
  in force January 2025 - the operational layer across all three laws
- The six CAC AI instruments -
  [algorithm recommendation](https://www.cac.gov.cn/2022-01/04/c_1642894606364259.htm),
  [deep synthesis](https://www.cac.gov.cn/2022-12/11/c_1672221949354811.htm),
  [generative AI](https://www.cac.gov.cn/2023-07/13/c_1690898327029107.htm),
  [content labelling](https://www.cac.gov.cn/2025-03/14/c_1743654684782215.htm),
  [cross-border data flows](https://www.cac.gov.cn/2024-03/22/c_1712776611775634.htm),
  and the
  [anthropomorphic interaction measures](https://www.cac.gov.cn/2026-04/10/c_1777558395078289.htm) -
  the last in force 15 July 2026, the newest AI instrument in this series

### Australia - published

**[policies/australia/](policies/australia/)** - full policy, enterprise
governance annex, research note, and source register. Word versions in
[downloads](policies/australia/downloads/). Open gates are in the
[folder README](policies/australia/README.md).

Australia has no AI Act and, since the National AI Plan of December 2025, has
said it will regulate AI through existing law; the six practices in the
National AI Centre's Guidance for AI Adoption are guidance, and the set adopts
them as labelled house standards. Three findings shape this edition. The
Privacy Act reaches AI without naming it, because personal information is
information about a person **whether true or not** - a hallucination about a
customer is personal information, entering it is a use or disclosure, and
generating it is a collection. The **automated-decision transparency duty
commences 10 December 2026 and the compiled Act does not show it** - the
provisions are uncommenced and live only in the amending Act and the endnotes,
and they attach to decisions made after that date whatever the age of the
system or the data. And the duty is disclosure only, so the set supplies
explanation, human review and notification as house standards. Built on:

- [Privacy Act 1988 (Cth)](https://www.legislation.gov.au/C2004A03712/latest/text) -
  compilation No. 104 of 4 June 2026: the thirteen Australian Privacy
  Principles, the notifiable data breaches scheme, the penalty tiers, and the
  statutory tort for serious invasions of privacy in force since 10 June 2025
- [Privacy and Other Legislation Amendment Act 2024](https://www.legislation.gov.au/C2024A00128/asmade) -
  the automated-decision provisions and their application rule, the security
  amendment, and the commencement table
- The Information Commissioner's guidance on
  [using commercially available AI products](https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/guidance-on-privacy-and-the-use-of-commercially-available-ai-products)
  and on
  [developing and training generative AI](https://www.oaic.gov.au/privacy/privacy-guidance-for-organisations-and-government-agencies/guidance-on-privacy-and-developing-and-training-generative-ai-models),
  and the May 2026 issues paper on automated-decision transparency
- The [National AI Plan](https://www.industry.gov.au/sites/default/files/2025-12/national-ai-plan.pdf)
  and the [Guidance for AI Adoption](https://www.industry.gov.au/publications/guidance-for-ai-adoption/our-approach)

## Formats

Markdown files are canonical. Word versions of each document are in the
`downloads/` folder beside them, regenerated from the Markdown on change.

## Licence

Documents are licensed under [CC BY 4.0](LICENSE.md) - use them, adapt them,
share them, with attribution.

## Feedback

Use it. Tell me what to improve - issues and pull requests welcome.

---

*Narendra Karki - CISSP | CISM | CISA | CAISP | CMCPSE*
*ORCID: 0009-0002-5757-8615*
