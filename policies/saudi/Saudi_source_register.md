# Source register - Saudi Arabia AI policy set

Every document referred to, used, or deliberately not used in producing the Saudi Arabia
AI Acceptable Use Policy v1.0, the Enterprise Annex v1.0, and the research note.

State as at 31 August 2026. Hashes are SHA-256 of the file as supplied, truncated to
16 characters.

---

## 0. Read this first - what this set is, and is not

**This set governs government data.** The three instruments it rests on apply to public
entities and to business partners handling government data. **They do not govern a
private organisation's processing of its own customers' or employees' personal data.**

**The Kingdom's personal data protection legislation and its implementing regulations
are not held.** A general private-sector AI acceptable use policy cannot be built from
what is here, and this set does not pretend to be one. The limitation is stated in the
policy's opening section and in the annex, not only in this register.

Research note section 2 sets out the four scope provisions this rests on, quoted.

## 1. Primary sources - HELD AND CITED

| # | Instrument | Version and date | SHA-256 | What is cited |
|---|---|---|---|---|
| 1 | **National Data Management and Personal Data Protection Standards** | Cover: **Version 1.5, January 2021**. 173 pp. Issued by the National Data Management Office | `784fdaae1ff5d9de` | Sections 1, 3, 4, 5, 8.1, 8.2; domain 9.14 in full (PDP.1.1, 1.2, 2.1, 3.1, 3.2, 4.1, 4.2, 4.3, 4.4, 5.1); DC.2.1; DO.2.1; DG.4; section 9.15 |
| 2 | **National Data Governance Policies - Data Classification Policy** | **Version 1, 5/5/2020**. 28 pp. NDMO | `bfad974c5343b264` | Clauses 1.1, 1.2 (principles 1-7), 1.3 (four levels and the Restricted sub-categories) |
| 3 | **Data Sharing Policy** | **Version 2.0, 2024**. 21 pp. NDMO | `93e843b8a20a75de` | Definitions; clause First (Scope); clause Second (the eight principles); clause Fifth (agreement contents, items 1-8); general rules |

**A version inconsistency in row 1, recorded not resolved.** The cover page reads
"Version 1.5 / January 2021". The internal document-control table records version 1.4 at
June 2021 and version 1.5 at June 2021. The two cannot both be right. **No provision
relied on in this set is affected**, but a position that turned on the precise date of
a version should be checked against an authoritative copy.

**Three byte-identical copies of row 1 were supplied.** The duplicates were verified
identical by hash and discarded before use.

## 2. HELD BUT NOT CITED

Substantial parts of the standards were read and set aside. The instrument spans 15
domains, 77 controls and 191 specifications; this set draws on the Personal Data
Protection domain in full and on individual specifications elsewhere. The remaining
domains - data governance beyond the organisation control, catalogue and metadata,
quality, operations beyond the retention specification, document and content management,
architecture and modelling, reference and master data, business intelligence and
analytics, data value realisation, open data, and freedom of information - are not cited
because no AI clause in this set rests on them.

**They are not irrelevant.** An entity implementing this policy is separately assessed
against all of them, and annex A11.7 requires a mapping from the AI controls here to the
specifications they support.

## 3. NOT HELD - the gaps that shape what these documents can say

### 3.1 The personal data legislation

**The Kingdom's personal data protection legislation and its implementing regulations
are not held.** This is why:

- the set cannot state the lawful bases for processing, or define personal or sensitive
  personal data;
- it cannot state the conditions for transferring personal data outside the Kingdom;
- it cannot state any penalty for contravention;
- **it cannot serve a private organisation with no government data.**

### 3.2 NDMO Personal Data Protection Regulations

**Nine of the ten Personal Data Protection specifications direct the reader to these
regulations "for more detailed requirements".** They are not held. Consequently the set
states what the standards themselves require - including the seven data subject rights,
the 72-hour breach notification period and the 24-month register minimum, all of which
**are** in the standards - and stops where the standards point elsewhere.

Research note section 7 tabulates every such pointer.

### 3.3 Every data security specification

**The Data Security and Protection domain contains eleven controls and no
specifications.** Both the specifications and the compliance assessment for that domain
are the mandate of the National Cybersecurity Authority and are expressly excluded from
the annual data management compliance assessment. One Data Classification specification
(DC.2.1, Security Controls) likewise carries the priority "As specified by NCA" rather
than a numbered priority.

**No instrument of that authority is held.** Policy Section 13 therefore states
[ENTITY]'s own house standards, says explicitly that it is doing so, and directs the
reader to that authority's requirements without reproducing, summarising or asserting
them. Where they differ, they govern.

### 3.4 NDMO Organizational Manual

Every specification in the Data Management Organization control requires the appointed
roles' responsibilities to be "aligned with the responsibilities defined in the
'Organizational Manual' published by NDMO". **The manual is not held.** Annex A1.4
provides that where it differs from this annex, it governs, and A11.5 makes obtaining it
a standing committee action.

### 3.5 Other

| What is missing | Consequence |
|---|---|
| **Sector regulator instruments** | No sector overlay exists |
| **Employment law, anti-discrimination law, intellectual property law** | Policy 18 and 20 carry no citation and are house standards |
| **Enforcement decisions and case law** | None relied on anywhere |

## 4. Sources appearing in the held instruments that were NOT used

The Personal Data Protection domain's own reference list names three documents: the NDMO
Personal Data Protection Regulation, **the General Data Protection Regulation (2018)**,
and **the California Consumer Privacy Act (2020)**. The Data Security domain's reference
list names PCI Security Standards Council material and two ISO standards.

**None of the foreign or industry instruments was consulted, cited, or relied on.**
Their appearance in a reference list inside a Saudi standard does not make them law in
the Kingdom, and importing an obligation from them would have been exactly the error
this set exists to avoid.

This is worth stating explicitly because the temptation is real: the seven data subject
rights in the standards are recognisably the shape of a familiar list, and it would have
been easy to fill in response periods, exemptions and verification requirements from
that familiar source. **Nothing of the kind was done.** The set states the seven rights
because the standards state them, and says nothing about how they operate because the
standards direct that question to regulations not held.

## 5. Documents supplied in the same batch and NOT used here

| Document | Jurisdiction | SHA-256 |
|---|---|---|
| Personal Data Protection Act 2012 (2020 Revised Edition) | Singapore | `d41a91872422d696` |
| Digital Personal Data Protection Rules, 2025 - G.S.R. 846(E) | India | `eabc7d05e0131446` |
| Corrigenda - G.S.R. 892(E) | India | `8f8d9526b5118018` |
| Data Protection Board composition - G.S.R. 845(E) | India | `812fe0ce802fe78f` |
| DIFC Regulation 10 Accreditation and Certification Framework | UAE (DIFC) | `1557019ef9551bbe` |

**No provision of any of these entered the Saudi set**, and no comparison to any other
jurisdiction appears in any Saudi document.

## 6. Document architecture

[ENTITY] supplied an existing policy set as a structural template. Only its architecture
was used: section order, tone, the convention that control and specification identifiers
live in the research note rather than the policy body, and the practice of flagging
house standards that exceed the instrument.

**No legal source from that template was carried across.** Every obligation in this set
was derived independently from the instruments in section 1. Where the template carried
a citation and no equivalent Saudi provision is held, the clause here is an unsourced
house standard and is labelled as such in the policy text itself, not only in this
register.

## 7. Documents PRODUCED

| Document | Version | Status |
|---|---|---|
| `Saudi_AI_Acceptable_Use_Policy.md` | 1.0 | Draft |
| `Saudi_AI_Governance_Enterprise_Annex.md` | 1.0 | Draft |
| `Saudi_policy_research_note.md` | 1.0 | Citations, findings, the map of the gaps |
| `Saudi_source_register.md` | 1.0 | This document |

## 8. Sources NOT used, as a matter of method

- **No web content entered any obligation.** No page was consulted as authority for
  anything in this set.
- **No AI-generated legal content.** Every provision cited resolves to text in the files
  at section 1.
- **No secondary commentary, law-firm briefing, or comparative summary.**
- **No foreign instrument**, including the two named in the standards' own reference
  list - section 4.
- **No comparison to any other jurisdiction.**

## 9. The verifications that mattered most

### 9.1 Scope, and the temptation to ignore it

The obvious document to write, asked for a Saudi AI policy, is a private-sector one. The
three instruments supplied do not support it. Section 3 of the standards limits them to
public entities and to business partners handling government data; the Classification
Policy applies to data "received, produced, or managed by public entities"; the Data
Sharing Policy governs "government entity data".

**A set written past that limit would have been wrong in a way that is very hard to
detect from the inside** - it would have looked like a competent privacy policy, cited
real Saudi instruments, and applied to nobody it claimed to apply to. The scope
statement is therefore the first thing in the policy, not a caveat at the end.

### 9.2 An arithmetic discrepancy that turned out not to be one

The standards state 77 controls and 191 specifications, with priority counts of 76 P1,
98 P2 and 16 P3 across the fifteen domains. **Those priorities total 190, not 191**, and
the shortfall localises to the Data Classification domain, whose row reads 10
specifications against 5 + 4 + 0 = 9.

Reading the domain body found ten specification identifiers (DC.1.1 through DC.5.1) and
nine priority tokens. **The tenth, DC.2.1 (Security Controls), carries the priority "As
specified by NCA".** It is a deliberate carve-out consistent with the security domain
being deferred to that authority throughout - not a table error and not an extraction
artefact.

**This was nearly recorded as a defect in the source.** It is recorded here as what it
actually is, and it reinforces the structural point at 3.3: data security is carved out
of these standards wherever it appears, not only in its own domain.

### 9.3 A citation that could not be made safely

The Data Management Organization control appoints the Chief Data Officer, Compliance
Officer, Personal Data Protection Officer, Business Data Executives, Business Data
Stewards, IT Data Stewards and others, each at priority P1 and each aligned to the
Organizational Manual. **The roles, their stated purposes and their priority are read
directly and are not in doubt.**

The specification numbers are another matter. The PDF renders that control as a
multi-column table, and text extraction batches the identifiers separately from the role
descriptions, so an individual DG.4.x number cannot be matched to an individual role with
confidence. **The research note therefore cites the control and not the specification
numbers**, and says why.

The alternative - assigning plausible numbers from the order in which fragments happened
to appear - would have produced citations that looked authoritative and could not be
checked. That is the failure mode this project exists to prevent, and the honest citation
is the less precise one.

### 9.4 The three routes

Since the instruments contain no AI provision at all, every AI obligation in the policy
had to be traced to an existing one. There turned out to be exactly three that carry
real weight:

- **Classification**, where the "highest level of protection" principle governs
  integrated datasets - which is what a corpus, an index, a fine-tuning set, or a
  multi-document prompt is;
- **The yearly personal data risk assessment**, which reaches information systems
  "whether automated or manual" and so carries AI systems in without any AI-specific
  language;
- **Data sharing**, because a commercial AI service receiving government data is a
  non-government data requester, and the agreement contents the policy prescribes map
  almost exactly onto what an AI vendor contract has to settle - purpose limitation,
  territorial limits, third-party benefit, and a destruction mechanism.

Everything else in the policy that goes beyond those three is a house standard and is
labelled as one where it appears.

## 10. Standing caveat

No provision cited in this set has been reviewed by qualified counsel. These documents
are educational templates, apply to government data only, and do not constitute legal
advice.

---

## 11. ADDENDUM 2 September 2026 - the personal-data corpus arrives

Three SDAIA documents were supplied on 2 September 2026 and are now HELD.
Hashes as supplied, truncated to 16 characters.

| # | Instrument | Version and date | Tier | SHA-256 |
|---|---|---|---|---|
| 4 | **Implementing Regulation of the Personal Data Protection Law** - English | **No version, issue date, or issuing decision number appears anywhere in the file** (see finding below). 27 pp, 38 articles. SDAIA | translation | `7607ea92027e1f10` |
| 5 | **Generative AI Guidelines for the Public** | 2025. 22 pp. SDAIA | guidance | `c4a2451c19eb3e78` |
| 6 | **Generative AI Guidelines for Government** | 2025. 30 pp, incl. operational appendix and checklist. SDAIA | guidance | `fb2427075540afee` |

**Finding - the Implementing Regulation file carries no translation disclaimer,
no version marker, and no dates.** The file was checked cover to cover, text
and page images. It does not state the decision that issued it, the date it
was issued, whether it reflects any amendment, or that the Arabic text
prevails. The register therefore records the Arabic-prevails position as a
matter of how Saudi law is enacted - the model proven on Bahrain Order 43 -
not as a quotation from this file. Two consequences:

- **Tier is translation, and the enacted Arabic is NOT held.** No divergence
  finding is possible until it is. On the Bahrain evidence (five divergences
  in one order's translation, none in another's), neither fidelity nor
  divergence should be assumed.
- **Currency is unverified.** A position that turns on precise wording must
  first establish that this text reflects the Regulation as amended.

**Still NOT held, and therefore still not asserted:**

| What is missing | Consequence |
|---|---|
| **The Personal Data Protection Law itself** (Royal Decree M/19 of 1443H as amended by M/148 of 5/9/1444H) | The Regulation is subordinate to it and cites it throughout. Lawful bases live in the Law; penalties live in the Law; the Regulation's own commencement is defined by reference to the Law's enforcement (Art 38). **The private-sector extension cannot be written from the Regulation alone** |
| **The Personal Data Transfer Regulation** (a separate SDAIA instrument) | The Implementing Regulation contains no transfer-conditions article; Art 33(5)(g) presupposes transfers are governed elsewhere. Cross-border conditions remain unstated |
| The enacted Arabic of the Implementing Regulation | Divergence verification blocked (finding above) |

Rows 5 and 6 are **guidance tier**: SDAIA guidance documents, not enacted
instruments. They can ground good-practice controls and the government-entity
GenAI overlay; they cannot ground a statement of legal obligation. Nothing in
the policy set yet cites them; they are recorded here on receipt so that the
GenAI overlay, when written, starts from declared sources.

Gap 3.1 is therefore **narrowed, not closed**: the Regulation is held and has
been read in full; the Law and the Transfer Regulation remain the gate to the
private-sector set. The research note's 2 September addendum records what the
Regulation independently corroborates in the existing set and the AI-specific
hooks it adds for the extension.
