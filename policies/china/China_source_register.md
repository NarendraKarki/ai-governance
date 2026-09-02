# Source register - People's Republic of China AI policy set

Every document referred to, used, or deliberately not used in producing the
China AI Acceptable Use Policy v1.0, the Enterprise Annex v1.0, and the
research note.

State as at 3 September 2026. Hashes are SHA-256 of the file as supplied,
truncated to 16 characters.

---

## 0. Read this first

**PRC law is enacted in Chinese, and there is no official English translation
of any instrument in this corpus.** This jurisdiction therefore has no
translation tier at all: every verification read in this set was performed on
the Chinese text directly. This is the reverse of the Bahrain and Saudi
model, where an English translation tier exists beneath the operative Arabic -
here the operative language is the only language held, which removes the
divergence risk those registers track but concentrates everything on reading
the Chinese accurately. The extraction-normalisation step this required is
recorded in the research note (section 7).

**One citation trap was closed at intake.** The Cybersecurity Law was taken
as the consolidation amended on 28 October 2025 - which renumbered the law -
not the 2017 text whose article numbers still dominate secondary coverage
(research note finding 4.1).

## 1. Primary law - HELD AND CITED

### National People's Congress Standing Committee laws (statute tier)

| # | Instrument | Version and date | SHA-256 | Articles |
|---|---|---|---|---|
| 1 | **Cybersecurity Law** 中华人民共和国网络安全法 | Consolidated text **as amended by the NPCSC decision of 28 Oct 2025**; source flk.npc.gov.cn | `9e575cff7451bbc3` | 81, complete |
| 2 | **Data Security Law** 中华人民共和国数据安全法 | As adopted 10 Jun 2021, in force 1 Sep 2021; source flk.npc.gov.cn | `722d29084fef7348` | 55, complete |
| 3 | **Personal Information Protection Law** 中华人民共和国个人信息保护法 | As adopted 20 Aug 2021, in force 1 Nov 2021; source flk.npc.gov.cn | `1815f84f43dd5011` | 74, complete |

### State Council administrative regulation

| # | Instrument | Version and date | SHA-256 | Articles |
|---|---|---|---|---|
| 4 | **Network Data Security Management Regulations** 网络数据安全管理条例 | Dated 24 Sep 2024, in force 1 Jan 2025; source flk.npc.gov.cn | `331f4d18c167c81c` | 64, complete |

The held text of row 4 carries the regulation body without the promulgation
order header; the State Council order number is therefore not asserted from
this corpus.

### CAC departmental rules and normative documents

| # | Instrument | Order / notice; in force | SHA-256 | Articles |
|---|---|---|---|---|
| 5 | **Algorithm Recommendation Provisions** 互联网信息服务算法推荐管理规定 | CAC/MIIT/MPS/SAMR Order No. 9; 1 Mar 2022 | `588ba472c388c9fc` | 35, complete |
| 6 | **Deep Synthesis Provisions** 互联网信息服务深度合成管理规定 | CAC/MIIT/MPS Order No. 12; 10 Jan 2023 | `983233b3f7e83885` | 25, complete |
| 7 | **Generative AI Interim Measures** 生成式人工智能服务管理暂行办法 | Seven-department Order No. 15; 15 Aug 2023 | `d6f91705e41899eb` | 24, complete |
| 8 | **Cross-border Data Flow Provisions** 促进和规范数据跨境流动规定 | CAC Order No. 16; on publication, 22 Mar 2024 | `754e2e4270f4ac4e` | 14, complete |
| 9 | **AI-Generated Content Labelling Measures** 人工智能生成合成内容标识办法 | Notice Guo Xin Ban Tong Zi [2025] No. 2 of 7 Mar 2025; 1 Sep 2025 | `2e6a2dd3821b167b` | 14, complete |
| 10 | **Anthropomorphic Interaction Interim Measures** 人工智能拟人化互动服务管理暂行办法 | Five-department Order No. 21, adopted 2 Feb 2026, published 10 Apr 2026; **15 Jul 2026** | `0934d3aed27de753` | 32, complete |

Rows 5-10 were captured from the official pages at cac.gov.cn; each capture
carries the source URL in the file. Rows 1-4 were downloaded from the
National Database of Laws and Regulations (国家法律法规数据库,
flk.npc.gov.cn) as native-text documents.

## 2. Completeness verification at intake

Article-by-article continuity was verified for every instrument: each text
was normalised (NFKC - the CAC PDF fonts encode some characters as Kangxi
radical variants) and its article sequence checked for gaps. All ten
instruments are complete. One apparent gap was investigated and resolved:
the Labelling Measures text matches articles 16 and 17 only as
cross-references to the Deep Synthesis Provisions inside its own Art 4 - the
Measures themselves run to 14 articles with no gap.

## 3. NOT HELD - the gaps that shape what these documents can say

| What is missing | Consequence |
|---|---|
| **The mandatory national labelling standard** (named by Labelling Measures Art 11) | Nothing asserted about its technical content; the annex records the version relied on when implementing |
| **The 2025 CSL amending decision as a standalone text** | Held only as consolidated into row 1; the decision's own commencement date is not asserted; nothing in the set depends on it |
| **2022 Data Export Security Assessment Measures; 2023 PI Export Standard Contract Measures** | Modified by row 8 (its Art 13 prevails on conflict); procedure detail not asserted |
| **Critical information infrastructure designation rules** | The set states the consequences of CII status, not how status is determined |
| **Sector rules** (finance, health, news, publishing, audiovisual) | Named as applying in addition; nothing asserted |
| **Local and free-trade-zone rules, incl. FTZ negative lists** | Policy 22.1 names the check; nothing asserted |
| **Science and Technology Progress Law; Minors Network Protection Regulations; Civil Code; criminal law** | Named where the held instruments cite them; nothing asserted |
| **Enforcement decisions and case law** | None relied on anywhere |

## 4. Discarded at intake

| File | Reason |
|---|---|
| **National Defense Mobilization Law** 中华人民共和国国防动员法 (revised 28 Aug 2026) | `e16276ed4cd6f175` - a defence statute unrelated to data, AI, or privacy; uploaded in error alongside rows 1-3 and discarded at Narendra's confirmation |

## 5. Document architecture

[ORGANISATION] supplied an existing policy set as a structural template. Only
its architecture was used: section order, tone, the convention that provision
identifiers live in the research note rather than the policy body, and the
practice of flagging house standards. **No legal source from that template
was carried across**, and no obligation was imported from any other
jurisdiction in this series.

## 6. Documents PRODUCED

| Document | Version | Status |
|---|---|---|
| `China_AI_Acceptable_Use_Policy.md` | 1.0 | **Published 3 Sep 2026** - verified against the Chinese texts of rows 1-10 |
| `China_AI_Governance_Enterprise_Annex.md` | 1.0 | **Published 3 Sep 2026** - verified against the Chinese texts |
| `China_policy_research_note.md` | 1.0 | Clause-by-clause basis, findings, the map of the gaps |
| `China_source_register.md` | 1.0 | This document |

## 7. Sources NOT used, as a matter of method

- **No web content entered any obligation.** Web search was used to locate
  the official cac.gov.cn pages and confirm which instruments exist -
  existence and location only, never authority.
- **No translation was used, official or otherwise.** None exists officially;
  unofficial translations were deliberately not consulted, so that no
  translated phrasing could shape a stated obligation.
- **No AI-generated legal content.** Every provision cited resolves to text
  in a file at section 1.
- **No secondary commentary, law-firm briefing, vendor page, or comparative
  summary.** Chinese platform regulation has one of the largest secondary
  literatures of any jurisdiction in this series; none of it entered this
  set.
- **No comparison to any other jurisdiction** inside the artifacts (the
  research note's cross-references to the Saudi and Bahrain findings are
  method notes, not imported obligations).

## 8. The verifications that mattered most

**The renumbered law.** The Cybersecurity Law amendment of 28 October 2025
inserted two articles and shifted the numbering of most of the law. The
universally cited "Art 21" multi-level protection duties now sit at Art 23;
the new AI clause sits at Art 20. Reading the amended consolidation rather
than the 2017 text is the difference between citing the right and the wrong
article in every CSL reference in this set (research note finding 4.1).

**The public-facing exclusion.** GenAI Measures Art 2 para 3 was read in the
Chinese: organisations developing and applying generative AI without
providing services to the domestic public are outside the Measures. That one
paragraph decides which half of the regime an enterprise tool lives in, and
it became Determination B of the policy (finding 4.3).

**The minors bright line.** Anthro Art 14 para 1 was nearly summarised as
"minors need guardian consent". The held text is harder: virtual-intimacy
services (virtual relatives, virtual partners) may not be provided to minors
at all - consent is irrelevant - and guardian consent applies only to other
anthropomorphic services for under-fourteens. The summary would have stated
a weaker rule than the law (finding 4.5).

**The cumulative thresholds.** The cross-border volume thresholds count
cumulatively from 1 January of the current year (Xborder Arts 5, 7, 8) - not
per transfer, not rolling twelve months. A tool comfortably exempt in
February can cross into the standard-contract band, or the mandatory
assessment, by November.

## 9. Standing caveat

No provision cited in this set has been reviewed by qualified PRC counsel.
These documents are educational templates, apply only within the stated
scope, and do not constitute legal advice.
