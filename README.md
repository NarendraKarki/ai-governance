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
| 1 | **AI acceptable use policies** | **Live** - UK, Bahrain, EU, India, and UAE published and verified within their stated scopes; Saudi Arabia published, government data scope ([below](#1-ai-acceptable-use-policies)) |
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
  GCC (Bahrain, Saudi Arabia, UAE), where published material is thinnest and
  most often wrong.
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
for the comparison matrix at part 3. Six jurisdictions are live: the UK,
Bahrain, the EU, India, Saudi Arabia, and the UAE.

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

## Formats

Markdown files are canonical. Word versions of each document are in the
`downloads/` folder beside them, regenerated from the Markdown on change.

## Licence

Documents are licensed under [CC BY 4.0](LICENSE.md) - use them, adapt them,
share them, with attribution.

## Feedback

Use it. Tell me what to improve - issues and pull requests welcome.

---

*The topics covered broadly track the domains of recognised AI governance
bodies of knowledge, including the IAPP's AIGP certification. This is an
independent educational project with no affiliation to, endorsement by, or
connection with the IAPP or any certification body. AIGP is a trademark of
the International Association of Privacy Professionals.*

*Narendra Karki - CISSP | CISM | CISA | CAISP | CMCPSE*
*ORCID: 0009-0002-5757-8615*
