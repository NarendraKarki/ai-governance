# Source register - United States AI policy set

Every document referred to, used, or deliberately not used in producing the US AI
Acceptable Use Policy v1.0, the Enterprise Annex v1.0, and the research note.

State as at 3 September 2026. Hashes are SHA-256 of the file as supplied, truncated
to 16 characters.

---

## 0. Read this first

**The United States is a patchwork, and this set is scoped, not universal.** It
states the federal sectoral baseline plus California and Colorado - the general
consumer-privacy anchor and the closest thing the country has to an AI statute -
and names every other state as not held. A set claiming to cover "US law" in one
document would be wrong the way a single global AI policy is wrong, one level down.

**Two amendment traps were closed at intake.** The Colorado act's operative dates
were moved by a special-session amendment; the set holds and reads both acts
together (finding 4.1 of the research note). The California regulations were taken
from the regulator's approved final rulemaking text, not from the proposal drafts
that circulated for a year before it.

## 1. Primary law - HELD AND CITED

| # | Instrument | Version and date | SHA-256 | Cited |
|---|---|---|---|---|
| 1 | **Colorado SB 24-205** - Consumer Protections for Artificial Intelligence (adds CRS title 6, art. 1, part 17) | Signed act, 2024 regular session; 26 pp | `fbe1ecf21ababdd8` | 6-1-1701 to 6-1-1707 |
| 2 | **Colorado SB 25B-004** | Signed act, 2025 special session B; approved 28 Aug 2025; 7 pp | `07e8f48f3d0bcd31` | ss.1-4 (amendments to 6-1-1702, -1703, -1704; effective-date clause) |
| 3 | **California Consumer Privacy Act as amended** - Civil Code div. 3, pt. 4, tit. 1.81.5, ss.1798.100-1798.199.95 | Official leginfo print, retrieved 2 Sep 2026; 38 pp | `a64e77b40d4ef9d2` | The personal-information baseline; ADMT and assessment rulemaking authority at 1798.185 |
| 4 | **CPPA Regulations - Approved Regulations Text** (Cal. Code Regs. tit. 11, div. 6) - CCPA updates, cybersecurity audits, risk assessments, ADMT, insurance | Final rulemaking of 22 Sep 2025; 127 pp | `7a34306cebf12ae9` | ss.7001, 7002, 7050-7053, 7120-7123, 7150-7157, 7200, 7220-7222 |
| 5 | **FTC Act s.5** - 15 U.S.C. 45 | US Code 2024 edition (GPO) | `d511071d1408df86` | s.45(a) |
| 6 | **FCRA** - 15 U.S.C. ch. 41, subch. III | US Code 2024 edition (GPO); 68 pp | `51962ffac6195fdc` | 1681m (adverse action) and the subchapter as sector baseline |
| 7 | **COPPA Rule** - 16 CFR 312 | eCFR, current to 31 Aug 2026 | `bdb220582dc7f9e6` | Sector baseline point |
| 8 | **GLBA Safeguards Rule** - 16 CFR 314 | eCFR, current to 31 Aug 2026 | `9f77c19eaa7589d7` | Policy 16.4 |
| 9 | **HIPAA Privacy and Security** - 45 CFR 164 | eCFR, current to 31 Aug 2026; 89 pp | `ac7652bbe0ef097d` | Sector baseline point; Colorado carve-out context |

## 2. Guidance tier - HELD AND CITED

| Instrument | Detail | SHA-256 |
|---|---|---|
| **NIST AI RMF 1.0** (AI 100-1) | 48 pp | `54f2affe7f200efe` |
| **NIST Generative AI Profile** (AI 600-1) | 64 pp | `6e73620ab6b64e90` |

Guidance, not law - **but the Colorado statute names the RMF in its own text** as a
reasonableness reference, presumption anchor, and affirmative-defense component
(research note finding 4.2). That statutory role is why these sit in the corpus as
load-bearing rather than decorative.

## 3. NOT HELD - the gaps that shape what these documents can say

| What is missing | Consequence |
|---|---|
| **Every state's law beyond California and Colorado** - incl. AI-in-employment and biometric statutes elsewhere | The scope statement at policy 1.1; nothing asserted about any of them |
| **State breach notification statutes** (incl. Cal. Civ. Code 1798.82; C.R.S. 6-1-716) | **No breach deadline is stated anywhere in this set.** Policy 17.2 routes to the privacy lead's maintained statement. Obtaining these is the recorded next verification |
| **Colorado AG rules under 6-1-1707** | Permissive rulemaking; none held; the presumption position rests on the statute alone |
| **CPPA Notice of Approval** (effective-date instrument for row 4) | The regulations' internal compliance dates are stated from the held text; the instrument-level effective date is not asserted |
| **ISO/IEC 42001** | Named by the Colorado statute as an alternative framework; not held; nothing about its content is asserted |
| **Federal executive AI policy** | Shifts with administrations; not law of general application; nothing rests on it |
| **Enforcement decisions and case law** | None relied on anywhere |

## 4. Discarded at intake

| File | Reason |
|---|---|
| Duplicate copy of SB 24-205 | Byte-identical to row 1 (`fbe1ecf21ababdd8`); one recorded, one discarded |
| `Codes_Display_TextII.pdf` | 882 bytes, blank - a failed save; skipped at Narendra's instruction, contents never determined |

## 5. Document architecture

[ORGANISATION] supplied an existing policy set as a structural template. Only its
architecture was used: section order, tone, the convention that provision
identifiers live in the research note rather than the policy body, and the practice
of flagging house standards. **No legal source from that template was carried
across**, and no obligation was imported from any other jurisdiction in this series.

## 6. Documents PRODUCED

| Document | Version | Status |
|---|---|---|
| `US_AI_Acceptable_Use_Policy.md` | 1.0 | **Published 3 Sep 2026** - verified within stated scope (federal baseline + California + Colorado) |
| `US_AI_Governance_Enterprise_Annex.md` | 1.0 | **Published 3 Sep 2026** - verified within stated scope |
| `US_policy_research_note.md` | 1.0 | Clause-by-clause basis, findings, the map of the gaps |
| `US_source_register.md` | 1.0 | This document |

## 7. Sources NOT used, as a matter of method

- **No web content entered any obligation.** Web search was used once, to locate
  official download pages - existence and location only, never authority.
- **No AI-generated legal content.** Every provision cited resolves to text in a
  file at sections 1-2.
- **No secondary commentary, law-firm briefing, vendor page, or comparative
  summary.** US state AI law is a subject with a large secondary literature and a
  fast-moving legislative map; none of it entered this set.
- **No comparison to any other jurisdiction.**

## 8. The verifications that mattered most

**The moved commencement.** SB 24-205 alone dates every duty 1 February 2026.
SB 25B-004 struck each of those dates for 30 June 2026 - which has passed, making
the duties live. Either act read alone gives a wrong answer; the pair gives the
right one. This is the same class of trap as India's commencement notification and
the EU's Digital Omnibus, and it is why the amending act was made a condition of
starting the build.

**The two definitions that do not coincide.** Colorado's substantial-factor test
and California's substantially-replaces test were read side by side in the held
texts, and the divergence made a design decision: two recorded determinations per
tool, never one (research note finding 4.4).

**The exclusion that depends on this document.** CRS 6-1-1701(9)(b)(II)(R) was
nearly summarised as "ordinary chatbots excluded". The held text conditions the
exclusion on the technology being subject to an accepted use policy prohibiting
discriminatory or harmful content - which makes the policy itself part of the
regulatory analysis, and turned a summary line into policy 4.2, 7.7, and annex A2.4.

## 9. Standing caveat

No provision cited in this set has been reviewed by qualified counsel. These
documents are educational templates, apply only within the stated scope, and do not
constitute legal advice.
