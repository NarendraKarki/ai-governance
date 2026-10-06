# Vendor assessment

Part 6 of the AI Governance Series. Educational material, not legal advice.

## What this is

An AI tool you buy is several companies deep: the vendor's product, the foundation model inside it (usually built by another company), the cloud it runs on, the vendor's subprocessors, and your own data at the centre. A vendor assessment asks what sits in each layer before you sign, and turns every gap into a contract clause. The workbook adds a sixth layer: the firm's own duties.

## Normal due diligence is not enough

A vendor can pass a normal security and supplier review and still be a risk, because that review checks the vendor, not the AI inside it. Each question in the workbook is marked **Standard due diligence** (what a normal review already asks) or **AI-specific** (what it misses). The split is a judgement, not a legal category; mature questionnaires increasingly include AI questions.

| | Normal due diligence | AI vendor assessment |
|---|---|---|
| Looks at | The vendor as a company | Every layer inside: the model and its maker, where prompts go, the model provider's terms, how the data is used |
| Evidence | Security questionnaire, SOC 2 or ISO 27001 report, data processing agreement | Those, plus the service terms, the subprocessor list and the model documentation |
| Assumes | The product is fixed once bought | The product can change underneath you: a new model, a new provider, an optional feature switched on |
| Data | Encrypted, where stored, who can access | Also: who keeps, reviews or trains on it, and can it surface in another customer's results |
| Output | Not covered | Accuracy, invented text, traceability, who pays for a wrong output |
| New attack routes | Not covered | Instructions hidden in uploaded documents; leakage through shared indexes or fine-tuning |
| Redone | At renewal | At renewal, and on every model change, new subprocessor or newly enabled feature |

In the worked example, the standard questions produced no Reds. All three Reds were AI-specific, and all three were about where client content goes inside the AI supply chain, which a security review does not trace.

## Beyond the UK and EU

The questions, the plain reasons and the contract clauses are written to work in most jurisdictions. Client contracts usually carry personal data (names, signatures, contact details), so data protection law applies; where a document holds none, confidentiality, privilege and the client's own terms still do. Most data protection laws leave the buyer responsible for the vendor it chooses and expect breaches to be reported; many also require a contract with the vendor and restrict sending personal data abroad, and some control the vendor's own suppliers. What the law rarely gives you (notice of model changes, the model's documentation, AI incident reporting, a fair liability cap) usually comes only from the contract.

Each question carries two legal columns: the UK and EU basis, as one verified worked example, and an empty column to map it to your own jurisdiction's law. Other jurisdictions may be added to the series once their texts have been checked.

This folder holds one workbook, `AI_Vendor_Assessment.xlsx`:

| Sheet | What it does |
|---|---|
| Read Me | Normal due diligence vs AI vendor assessment, why it matters, how to use the workbook, the worked example, sources |
| Summary | The worked example's live counts of Red, Amber and Green by layer and by type (standard or AI-specific), the status of every gap, and the decision: sign, sign with conditions before go-live, or do not sign yet |
| Questionnaire | The worked example: 34 questions across six layers, each marked standard or AI-specific, with a plain reason, the UK and EU legal basis, a column for your own jurisdiction, the vendor's answer, the evidence seen, the rating, the clause the contract needs, and whether it is secured (in the signed contract or, for the firm's own items, done) |
| Template Summary | The same counts and decision for your own vendor, read from the template |
| Questionnaire Template | The same 34 questions, blank, ready to send to a vendor |

Status is calculated: a Red not yet secured is a blocker; an Amber not yet secured or done is a condition before go-live.

## The worked example

Carrow Street Legal LLP (fictional), a law firm operating in the UK and the EU, buys a generative AI contract-review tool. The tool is built on a general-purpose model from a US model provider and hosted in a UK cloud region.

The vendor's security questionnaire raised no Reds. The assessment found three, all on AI-specific questions and all fixed in the contract before signing: prompts, documents and outputs kept in logs for 90 days; the model provider keeping prompts for up to 30 days for abuse monitoring; and default terms allowing customer content to be used for "service improvement". Every other gap that needed the contract, including notice of model changes and the model provider's documentation, was also agreed before signing. One condition remains before go-live, inside the firm: staff training before anyone gets access. Decision: sign, with one condition before go-live.

The firm, the vendor and the model provider are fictional.

## Legal basis for the worked example (UK and EU)

UK GDPR ([legislation.gov.uk](https://www.legislation.gov.uk/eur/2016/679/contents), read 5 October 2026):

- A controller may only use processors that provide sufficient guarantees (Art 28(1)). Using one that does not is the controller's own breach: fines up to £8,700,000 or 2% of total worldwide annual turnover, whichever is higher (Art 83(4)(a)).
- The processor contract must contain the terms in Art 28(3); subprocessors need the controller's prior written authorisation (Art 28(2)) and the same terms (Art 28(4)).
- A processor that, in breach of its role, decides to use the data for its own purposes is treated as a controller for that processing (Art 28(10)). If the contract allows such use, the firm is disclosing client data to another controller and needs its own basis to do so.
- A processor must report a personal data breach to the controller without undue delay (Art 33(2)).
- International transfers: Art 44A, in force since 5 February 2026 (the old Art 44 was omitted by the Data (Use and Access) Act 2025).

EU AI Act (consolidated text of 27 July 2026, CELEX 02024R1689-20260727, [EUR-Lex](https://eur-lex.europa.eu/legal-content/EN/TXT/?uri=CELEX:02024R1689-20260727); read 5 October 2026):

- Reviewing contracts for clients is not a high-risk use under Annex III (point 8(a) covers use by or on behalf of a judicial authority, and similar use in alternative dispute resolution), so the deployer duties in Art 26 do not apply to it. If a firm itself puts a tool not classified as high-risk to an Annex III use, it is treated as the provider (Art 25(1)(c)), from 2 December 2027 for Annex III systems (Art 113(c), as amended).
- The provider of a general-purpose AI model must give documentation that gives a good understanding of the model's capabilities and limitations, with at least the Annex XII content, to the providers who integrate it, that is the vendor (Art 53(1)(b)). Nothing obliges anyone to give it to the buyer; only the summary of training content is public (Art 53(1)(d)). For models placed on the market before 2 August 2025, this applies from 2 August 2027 (Art 111(3)). The buyer's leverage is the contract.
- Deployers in the EU must take measures to support the AI literacy of staff who use AI (Art 4).

Professional duties: [SRA Code of Conduct for Firms](https://www.sra.org.uk/solicitors/standards-regulations/code-conduct-firms/), paragraph 6.3 (client confidentiality), read 5 October 2026.

Not covered: the EU GDPR text for the EU office is not stated here; sector rules for regulated financial firms (outsourcing and operational resilience) are outside this workbook.

## How to use it

1. Work in the Questionnaire Template sheet (keep a blank copy first). Fill column G with your own jurisdiction's law, then send columns D and E to the vendor.
2. Record each answer and the evidence you actually saw.
3. Rate each answer Green, Amber or Red.
4. For every Amber or Red, negotiate the clause in column K and record whether it is secured (column L): in the signed contract or, for the firm's own items, done.
5. Read the decision on the Template Summary sheet. Re-assess on renewal, on any model change, on any new subprocessor, and whenever the way you use the tool changes.

Related parts: the AI risk register (Part 4) tracks the risks this assessment finds; the impact assessment workbook (Part 5) does the DPIA screen in question F3.

---

Educational, not legal advice. Have your DPO or legal counsel review any assessment and contract before it is relied on. Licensed under CC BY 4.0.
