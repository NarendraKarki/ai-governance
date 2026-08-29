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
| 1 | **AI acceptable use policies** | **Live** - UK published, Bahrain working draft ([below](#1-ai-acceptable-use-policies)) |
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
for the comparison matrix at part 3. The India, Saudi Arabia, and UAE editions
follow.

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

### Kingdom of Bahrain - working draft

**[policies/bahrain/](policies/bahrain/)** - full policy, enterprise
governance annex, research note, and source register. Word versions in
[downloads](policies/bahrain/downloads/). Verification gates are stated
openly in the [folder README](policies/bahrain/README.md).

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
