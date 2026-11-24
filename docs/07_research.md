---
title: Research — problem, users, competitors (Project Step 2)
version: 0.3.1
status: draft
owner: TBD
updated: 2026-11-24
---

# Research: AI_lawyer — a tool that speeds up the lawyer's work with contracts

**Track:** Startup  **Target country:** Poland (context — the EU market)  **Research date:** 23–24.11.2026
**Method:** search through an AI tool connected to a search engine; every figure below is marked by the reliability of its source (see section 5).

> **What changed in version 0.2.0.** The team adopted three inputs ([ADR-0002](decisions/0002-positioning-poland-in-house.md)):
> 1. the product is a **tool that speeds up the lawyer's work**, not a replacement for the lawyer for non-lawyers;
> 2. the target country is **Poland**;
> 3. the target client is **companies that need to optimise the lawyer's work** (in-house, or external on a retainer).
>
> Therefore the "SMEs without a lawyer" segment recommended in version 0.1.0 is no longer a target. The analysis of the problem, competitors, risks and the conclusions were revised for the new inputs; Polish competitors for lawyers (Wolters Kluwer, C.H.Beck) were added.

---

## 1. Problem

A company lawyer spends a large share of their time on repetitive review of incoming contracts (NDAs, supply, B2B services). The business waits for approval, the lawyer becomes a bottleneck, and contracts with bad terms still get through.

- On average companies lose **about 8.6–9% of annual revenue** due to weak contract management; the best lose about 3%, the worst 15% or more (World Commerce & Contracting, 2025, via secondary publications). ⚠️ Medium reliability: the figure is published by CLM vendors.
- Lawyers are already trying AI en masse: **more than 92%** of surveyed lawyers use at least one AI tool in daily work (Wolters Kluwer survey: 810 lawyers from law firms and legal departments in the USA, China and 9 European countries). ⚠️ Vendor survey, no separate data for Poland.
- Heads of legal functions at large companies stress that AI in legal departments must be introduced very carefully because of data sensitivity (EY Law General Counsel Study 2025, 1,000 heads of legal at companies with revenue > $1 billion). → Product requirement: confidentiality and control of data.
- **Size of the lawyer pool in Poland:** about **42.7 thousand practising radcy prawni** (of 55.8 thousand on the registers) and **22.9 thousand practising advocates (adwokaci)** — per a reply to a parliamentary interpellation, data as of June 2025. Radca prawny is the main profession of lawyers employed by companies (under an employment contract). ⚠️ How many of them work in-house could not be found.

**Conclusion:** the pain "the lawyer cannot keep up, contracts are reviewed slowly or superficially" is real, and lawyers are ready to use AI. But there are no Polish data on a lawyer's time per contract or on the share of in-house lawyers — this gap must be closed with interviews.

## 2. Target client: segments

### 2.1 Who buys and who uses

| Role | Who | What matters |
|---|---|---|
| **User** | In-house lawyer (radca prawny / prawnik) | Review a contract faster without losing quality, work in Word |
| **Buyer** | Head of Legal / General Counsel; in small companies — CFO or CEO | Lower workload for the lawyer without hiring, measurable time savings |
| **Beneficiary** | Sales, procurement | The contract is approved faster |
| **Controller** | IT / security / DPO | Where data is stored, whether the model is trained on contracts |

### 2.2 Comparison of company segments

| Criterion | **Mid-sized companies with 1–5 lawyers** (main) | Large companies with a legal department | Companies with an external lawyer on retainer | SMEs without a lawyer (was in v0.1.0) |
|---|---|---|---|---|
| Pain | The lawyer is overloaded with repetitive contracts, hiring another is expensive | Large flow of contracts, standards and control needed | Every review is billable hours | Do not understand the risks |
| Already served by | LEX / Libra, Beck-Noxtua, VAI Legal, ChatGPT/Claude | Luminance, LEGALFLY, Legartis, Legora, Libra | The external lawyer with their own tools | ChatGPT/Claude, templates |
| Willingness to pay | Medium: there is a budget for legal databases (LEX/Legalis) | High, but long sales cycles and tenders | Low: the savings go to the law firm | Low |
| Risk of "legal advice" | Low: the lawyer decides | Low | Low | High |
| Access for a student team | Medium: Kozminski network, LinkedIn | Difficult | Medium | Easy |
| Fit with the inputs | ✅ Full | ✅, but the market is taken | Partial | ❌ Does not fit |

**Recommendation:** the main segment is **Polish mid-sized companies with a small legal function (1–5 lawyers)** that have a high flow of **one type of contract** (for example NDAs or B2B services/supply agreements). Large legal departments are the next stage, once time savings are proven. Law firms are not part of the current inputs.

## 3. Competitors and customer reviews

### 3.1 Polish market — direct competitors

| Company / product | Behind it | For whom | What it does | Data reliability |
|---|---|---|---|---|
| **LEX Expert AI + Libra** | Wolters Kluwer Polska | Law firms and legal departments | AI chat on Polish law inside the LEX database; Libra — the lawyer's workspace (research, drafting, review), team-specific AI assistants, Word and Outlook add-ins. Since May 2026 — extended contract analysis. Free trial access. In August 2026 Libra was chosen by CRIDO | Low–medium: vendor press releases |
| **Beck-Noxtua** | Noxtua + Wydawnictwo C.H.Beck (Legalis) | Lawyers | AI workspace with answers linked to Legalis content; launch in Poland announced for spring 2026 | Low: launch not confirmed |
| **VAI Legal** | Startup | Lawyers, companies | Contract analysis under Polish law, risk assessment, edits in Word | Low: company website |
| **Gaius-Lex** | Startup | Lawyers | "Sovereign" AI for Polish and European law, data in the EEA | Low: company website |
| **LexTool** | Startup | Lawyers | Document assistant, from 249 zł net per month | Low: company website |

**Key conclusion for Poland:** the main competitors are **legal database publishers (Wolters Kluwer, C.H.Beck)**. Legal departments already pay them for LEX or Legalis, so AI features are sold as an add-on to a familiar product, with ready sales and trust. A new product will have to explain why it is worth buying in addition to them.

### 3.2 European players (for legal departments)

| Company | Country | For whom | What it does | Scale |
|---|---|---|---|---|
| **Legora** | Sweden | Law firms, large legal departments | General-purpose AI platform for lawyers | Series E €489 million, valuation ~€7.8 billion (Oct 2026) |
| **Luminance** | United Kingdom | Large companies | Contract review and automated negotiation | Series C $75 million, clients in 70+ countries |
| **LEGALFLY** | Belgium | Corporate legal departments | Contract review against company rules | ~€17 million (seed + Series A €15 million) |
| **Legartis** | Switzerland | Legal departments, procurement | Review of incoming contracts against the company playbook, 150+ clause types | No funding data found |
| **Juro** | United Kingdom | Growing companies | Contract management (CLM) with AI | — |

**General-purpose AI assistants.** In February 2026 Anthropic released an open-source contract review plugin for Claude, and in May 2026 — **Claude for Legal** with 12 plugins. The plugin reviews a contract against the team's playbook and gives a reference to the clause, the risk and an edit option. For a lawyer this is a strong alternative: they can verify the result themselves. Limitations for companies: data security policy and the absence of a Polish legal base out of the box.

### 3.3 What customers say

| Product | Ratings | What they praise | What they complain about |
|---|---|---|---|
| **Juro** | G2 4.5 (~180–240 reviews); Capterra — 48 reviews | Simplicity, support, Word add-in | Weak edits and negotiation, transfer of Word formatting, reports; AI features "average" (7.7–7.8 out of 10 on G2) — details below |
| **Luminance** | Gartner 4.6 (31 reviews) | Review automation, support | Very expensive, only for large companies, long implementation, training needed |
| **Genie AI** | G2 4.4–4.6; Capterra 4.5 | Simplicity, speed of the first draft | Worse with complex contracts; formatting |
| **LEGALFLY** | No independent reviews | Customer testimonial (ECS): review of transport contracts against its own terms | "−60% time" — the company's claim |
| **Legartis** | No independent reviews | — | "Up to 85% faster" — marketing |
| **Libra, LEX Expert AI, Beck-Noxtua** | No independent reviews found | — | — |

**Juro: which features are missing (per reviews)**

| What is missing | What users write | Where |
|---|---|---|
| **Edits and negotiation (redlining)** | The counterparty's edit can only be accepted or rejected as a whole, you cannot make an edit on top of an edit; over several negotiation rounds it is unclear who changed what. The most frequent complaint under "Missing Features" (~8–10 reviews) | [G2, p. 2](https://g2.com/products/juro/reviews?page=2), [G2, p. 3](https://g2.com/products/juro/reviews?page=3), [Oneflow (competitor)](https://oneflow.com/uk/blog/juro-reviews/) |
| **Formatting from Word** | Formatting is not always transferred correctly from Word; limited customisation of tables, complex layout and conditional formatting | [G2](https://www.g2.com/products/juro/reviews), [Capterra](https://www.capterra.com/p/167130/Juro/) |
| **Reports and analytics** | Reports are limited; to export detailed metrics (approval duration, risks per clause) manual work or the API is needed | [Capterra](https://www.capterra.com/p/167130/Juro/), [GetApp](https://www.getapp.com/operations-management-software/a/juro/reviews/), [ContractSafe (competitor)](https://www.contractsafe.com/contractsafe-vs-juro-comparison) |
| **Customisation** | Hard to change a contract after it was sent to the counterparty; inconvenient to reuse templates across workspaces; "Limited Customization" topic (~5 reviews) | [G2](https://www.g2.com/products/juro/reviews), [Capterra](https://www.capterra.com/p/167130/Juro/) |
| **Integrations** | No Microsoft Teams integration; some integrations only via Zapier | [G2](https://www.g2.com/products/juro/reviews), [PandaDoc (competitor)](https://pandadoc.com/blog/juro-review) |

⚠️ Medium reliability: G2 is closed to automated download, so the data comes from review page snippets in search; the number of reviews per topic differs between pages. The Oneflow, ContractSafe and PandaDoc reviews were written by Juro's competitors.

**What this means for AI_lawyer:** lawyers value convenient edits in negotiations and working directly in Word without losing formatting — this supports the choice of "work in Word, edits as track changes". A report on approval time is a possible feature for the buyer (head of legal).

**What the reviews show:** legal departments value simplicity, speed and customisation to their own rules; they complain about price and long implementation of enterprise solutions. For mid-sized companies this is a window: fast implementation and a clear price.

### 3.4 Poland: what lawyers say

**Reviews of Polish products.** No independent customer reviews of Polish AI tools for lawyers could be found:

| Product | What was found | Source |
|---|---|---|
| **LEX Expert AI** | Only vendor materials: the product was tested by lawyers and radcowie prawni before launch; an interview with Prof. Marcin Dziurda (radca prawny), who, by his account, was pleasantly surprised by the tool | [Wolters Kluwer](https://www.wolterskluwer.com/pl-pl/solutions/lex/expert-ai/dlaczego-lex-expert-ai) |
| **Libra** | The largest named client is CRIDO (~200 lawyers and consultants, a consulting company, not a legal department); no legal department reviews | [Wolters Kluwer](https://www.wolterskluwer.com/pl-pl/news/crido-wybiera-libre-od-wolters-kluwer-jako-nowe-srodowisko-pracy-ai), [prawo.pl](https://www.prawo.pl/prawnicy-sady/libra-nowy-ai-ulatwiajacy-prace-prawnikow,1537789.html) |
| **Gaius-Lex** | Listings on G2, Capterra, GetApp exist, no reviews (0 on GetApp) | [GetApp](https://www.getapp.com/all-software/a/gaius-lex/), [G2](https://www.g2.com/products/gaius-lex/reviews) |
| **VAI Legal, LexTool, Beck-Noxtua** | No reviews found | — |

**What Polish lawyers say in surveys**

| Study | Who was surveyed | Key data |
|---|---|---|
| **Raport Rynku Prawniczego 2025/2026** (Supesu Recruitment, Jan–Mar 2026) | 507 lawyers from law firms and **legal departments** | ~88% use AI tools; the most popular are **general-purpose**: ChatGPT (~63%), Copilot (56%), DeepL (51%); almost every second respondent mentions burnout |
| **Survey by Fundacja SET and Logit** | Advocates and radcowie prawni | 52.5% already use AI (22.5% intensively), another 32.5% plan to. Concerns: **data security and confidentiality — 81%**, **AI errors — 75.9%**, professional liability — 44.3%. **36.3% know none** of the specialised AI tools for lawyers on the Polish market ("shadow AI") |
| **In-House Lawyer Innovation Forum 2025** (Warsaw, 30.09.2025, organiser — Wolters Kluwer) | ~120–130 heads of legal departments | Panel "AI in the legal department": the question is no longer "whether" but "how". Main topics: data security and where the servers are, uncontrolled use of AI by company employees |

⚠️ Reliability: Supesu and SET/Logit — medium (independent organisations, but the methodology was not fully checked; data for legal departments are not separated). The forum and product materials — low–medium: the source is Wolters Kluwer, a seller of competing solutions.

**What this means for AI_lawyer:**
1. **Lawyers in Poland already use AI, but mostly general-purpose tools** (ChatGPT, Copilot) — this is both the main competitor and a sign of demand.
2. **The main objection is data, not text quality:** 81% worry about confidentiality. EU storage, no training on contracts and a clear data policy are a mandatory condition of sale.
3. **The market of specialised tools is poorly known** (36% know none) — there is room for a new player, but investment in awareness will be needed.
4. **There are no public reviews from Polish legal departments** — we must obtain them ourselves through 5–10 interviews; the survey data give hypotheses for the questions.


## 4. The strongest arguments against the idea

1. **The feature becomes standard.** Claude for Legal, ChatGPT, Libra already review contracts. If the product is "LLM + prompt", it is easy to copy.
2. **Strong local players with ready customers.** Wolters Kluwer and C.H.Beck sell AI to the same legal departments that already pay them for legal databases. Globally the market is occupied by well-funded companies, and even they lose: the British **Robin AI** failed to raise a round in 2025, cut staff and was sold off in parts.
3. **The lawyer is a demanding user.** If the tool makes mistakes or produces filler, the lawyer quickly stops using it: it is faster to check yourself than to double-check the AI. There are more than 1,300 court cases with AI-invented citations (April 2026) — lawyers know this risk and are sceptical about AI.
4. **Confidentiality and long sales cycles in the company.** Contracts are sensitive data; IT/security review, a DPO, a data processing agreement (GDPR) and sometimes legal privilege are needed. This lengthens the sale even for mid-sized companies.
5. **Knowledge of Polish law is needed.** Quality review requires a Polish legal base and practice; publishers have them, a startup does not.
6. **Time savings must be proven with numbers.** The buyer (GC, CFO) pays for the lawyer's saved hours; without a measurable result the product is "yet another subscription".

**What weakened compared with v0.1.0:** the risk of unauthorised legal advice is lower — the lawyer decides. In Poland what is reserved for advocates and radcowie prawni is mainly representation in courts and authorities; general legal assistance outside this scope is not expressly forbidden to other persons (per legal publications). ⚠️ To be verified in the text of the statutes.

**What can be set against this:**
- **The company playbook**, not a general AI: review against the rules and positions of a specific legal department, approved by its lawyer.
- **Work in Word** and export of edits as track changes — no new system.
- **One contract type with a high flow** and a measurable metric: minutes per contract before and after.
- **Every comment linked to the contract text** — the lawyer verifies quickly.
- **Data stored in the EU**, no model training on the client's contracts.

## 5. Source check

| Claim | Source | Reliability |
|---|---|---|
| Legora round €489 million | EU-Startups, Startup in Europe | High (several media) |
| Collapse of Robin AI | Legal Cheek, Sifted, Artificial Lawyer, Law360 | High |
| Claude for Legal, May 2026 | ABA Journal, TechCrunch, LawNext | High |
| Cases with AI "hallucinations" | D. Charlotin's database, Stanford CIS, NPR | High (per the author — understated) |
| Number of radcowie prawni and advocates (June 2025) | Reply to a parliamentary interpellation (api.sejm.gov.pl) | High (official document), but the in-house share is unknown |
| GC caution when introducing AI | EY Law General Counsel Study 2025 | Medium: consulting company, large companies, not only Poland |
| 92% of lawyers use AI | Wolters Kluwer via prawo.pl | Low–medium: vendor survey, Poland not separated |
| Libra: contract analysis, Word/Outlook, CRIDO | Wolters Kluwer press releases, prawo.pl | Low–medium: vendor information |
| Beck-Noxtua in Poland | Noxtua press release | Low: launch not confirmed |
| Legal assistance outside representation is not reserved for the professions | Palestra (2022), e-prawnik.pl | Medium/low: **verify in the statutes** |
| Losses of 8.6–9% of revenue | WorldCC via secondary publications | Medium: original not opened |
| G2/Capterra/Gartner ratings | Platform pages | Medium: numbers differ between pages |
| Surveys of Polish lawyers (Supesu 2026, SET/Logit) | rp.pl, cyberdefence24.pl | Medium: data for legal departments not separated |
| Reviews of Polish products, in-house forum | Wolters Kluwer, prawo.pl, GetApp | Low–medium: mostly vendor materials; no independent reviews |
| Juro's missing features | Snippets of G2, Capterra, GetApp reviews; competitor reviews | Medium: G2 does not open directly; some reviews are from competitors |
| 60% speed-up (LEGALFLY), 85% (Legartis) | Company websites | Low: marketing |
| Information on VAI Legal, Gaius-Lex, LexTool | Company websites | Low: no independent reviews |
| EU AI Act status of contract review | Law firm reviews | Not confirmed: contract review is not mentioned in Annex III in the sources found |
| Data on SMEs without a lawyer (YouGov/LawBite, Smallpdf) | — | Removed from v0.2.0: the segment is no longer a target |

## 6. Conclusions

1. **The problem of lawyer overload is confirmed**, and lawyers are already ready to use AI. The value of AI_lawyer is not "AI reads the contract" but **measurable time savings for the lawyer** on a specific contract type.
2. **In Poland the main competitors are legal database publishers** (Wolters Kluwer with LEX and Libra, C.H.Beck with Beck-Noxtua): they have Polish law, customers and sales. We cannot compete with them head-on; narrow specialisation is needed.
3. **Niche:** mid-sized Polish companies with 1–5 lawyers, one contract type with a high flow, review against the company playbook, work in Word, data in the EU. Enterprise solutions are expensive for them and slow to implement.
4. **The lawyer's trust is the main requirement:** a reference to the contract text in every comment, few false positives, transparency about where data is stored.
5. **Before development check:** (a) how much time a lawyer really spends on the chosen contract type and how much the company is ready to pay given LEX/Legalis; (b) IT/DPO requirements for contract storage — through **5–10 interviews with in-house lawyers and heads of legal in Poland**.

## 7. What to update in the Project Charter

- Solution: "An AI tool for in-house lawyers at Polish companies that speeds up the review of <contract type> against the company playbook and proposes edits in Word".
- Target client: mid-sized companies in Poland with a small legal function; the user is the lawyer, the buyer is the head of legal / CFO.
- How we will know it works: review time per contract dropped by X% on the test set; share of AI comments accepted by the lawyer; willingness of surveyed companies to pay.
- Open questions: contract type; which lawyer will help write the first playbook; price hypothesis relative to LEX/Legalis.

---

## Sources

**Polish market**
- [Number of advocates and radcowie prawni, June 2025 (reply to a parliamentary interpellation)](https://api.sejm.gov.pl/sejm/term10/interpellations/attachment/ATTDMXK2C/i12392-o1.pdf)
- [LEX Expert AI — launch (PAP MediaRoom)](https://www.pap.pl/mediaroom/zaufany-czat-ai-dla-prawnikow-wolters-kluwer-polska-wprowadza-lex-expert-ai) · [LEX Expert AI for the legal department](https://www.wolterskluwer.com/pl-pl/solutions/lex/expert-ai/zastosowania-ai-w-dziale-prawnym)
- [Libra on the Polish market (February 2026)](https://www.wolterskluwer.com/pl-pl/news/wolters-kluwer-wprowadza-na-polski-rynek-platforme-libra-w-ramach-europejskiej-ekspansji) · [Libra — contract analysis (May 2026)](https://www.wolterskluwer.com/pl-pl/news/wolters-kluwer-rozwija-platforme-libra) · [CRIDO chooses Libra](https://www.wolterskluwer.com/en/news/crido-chooses-libra-by-wolters-kluwer) · [Libra (prawo.pl)](https://www.prawo.pl/prawnicy-sady/libra-nowy-ai-ulatwiajacy-prace-prawnikow,1537789.html)
- [Beck-Noxtua for Poland (Noxtua)](https://www.noxtua.com/news/press-releases/beck-noxtua-poland)
- [VAI Legal](https://vai.legal/) · [Gaius-Lex](https://gaius-lex.pl/) · [LexTool](https://www.lextool.pl/) · [Overview of AI for lawyers in Poland (Lexedit)](https://lexedit.ai/pl/blog/ai-dla-prawnikow-narzedzia-zastosowania)

**Lawyers and AI**
- [Raport Rynku Prawniczego 2025/2026 — Supesu (Rzeczpospolita)](https://www.rp.pl/zawody-prawnicze/art44314141-raport-prawnicy-miedzy-algorytmami-a-wypaleniem)
- [AI in the legal sector — survey by Fundacja SET and Logit (CyberDefence24)](https://cyberdefence24.pl/polityka-i-prawo/sztuczna-inteligencja-w-sektorze-prawniczym-miedzy-innowacja-a-ryzykiem-systemowym)
- [In-House Lawyer Innovation Forum 2025 (Wolters Kluwer)](https://www.wolterskluwer.com/pl-pl/news/in-house-lawyer-innovation-forum-2025) · [prawo.pl](https://www.prawo.pl/biznes/in-house-lawyer-innovation-forum-2025,535159.html)
- [LEX Expert AI — why (Wolters Kluwer)](https://www.wolterskluwer.com/pl-pl/solutions/lex/expert-ai/dlaczego-lex-expert-ai) · [CRIDO chooses Libra (PL)](https://www.wolterskluwer.com/pl-pl/news/crido-wybiera-libre-od-wolters-kluwer-jako-nowe-srodowisko-pracy-ai) · [Gaius-Lex — GetApp](https://www.getapp.com/all-software/a/gaius-lex/) · [Gaius-Lex — G2](https://www.g2.com/products/gaius-lex/reviews)
- [EY Law General Counsel Study 2025 (PL)](https://www.ey.com/pl_pl/newsroom/2025/04/ey-law-general-counsel-study-pl)
- [Lawyers use AI every day (prawo.pl)](https://www.prawo.pl/biznes/prawnicy-na-co-dzien-korzystaja-z-ai-a-ai-zmienia-model-ich-zawodu,1540345.html)
- [Future Ready Lawyer 2026 (Wolters Kluwer)](https://www.wolterskluwer.com/pl-pl/news/wolters-kluwer-publikuje-raport-z-badania-future-ready-lawyer-2026)

**Competitors in Europe**
- [Legora — €489 million (EU-Startups)](https://www.eu-startups.com/2026/10/theres-no-stopping-legora-e489-million-for-stockholms-legaltech-unicorn/) · [Startup in Europe](https://startup-in-europe.com/legora-raises-approximately-e505-million-to-accelerate-its-expansion/)
- [Legal AI startups by fundraising (New Market Pitch)](https://newmarketpitch.com/blogs/news/legal-ai-top-startups-fundraising)
- [LEGALFLY Series A (Law.com)](https://law.com/legaltechnews/2024/07/16/belgian-ai-startup-legalfly-secures-16-3-million-in-series-a-keeps-the-legal-tech-funding-streak-hot) · [seed (Tech.eu)](https://tech.eu/2023/11/28/ai-co-pilot-legalfly-secures-over-2m-in-seed-funding/) · [ITdaily](https://itdaily.com/blogs/software/legalfly-legal-ai-organisation/) · [Legal 500](https://www.legal500.com/suppliers/legalfly/)
- [Legartis — AI contract review](https://legartis.ai/ai-contract-review) · [CB Insights](https://www.cbinsights.com/company/legartis/customers)
- [Robin AI — Legal Technology](https://legaltechnology.com/robin-ai-listed-for-distressed-sale-nine-months-after-making-the-sunday-times-100-tech-list/) · [Sifted](https://sifted.eu/articles/robin-ai-cuts-a-third-of-staff) · [Artificial Lawyer](https://www.artificiallawyer.com/2025/10/27/robin-ai-lays-off-staff-as-growth-disappoints/)
- [Claude for Legal (ABA Journal)](https://www.abajournal.com/news/article/anthropic-launches-claude-for-legal-giving-lawyers-20-new-program-integrations-and-12-practice-area-plugins/) · [Artificial Lawyer](https://artificiallawyer.com/2026/02/02/anthropic-moves-into-legal-tech) · [TechCrunch](https://techcrunch.com/2026/05/12/the-ai-legal-services-industry-is-heating-up-anthropic-is-getting-in-on-the-action)

**Customer reviews**
- [Genie AI — G2](https://www.g2.com/products/genieai/reviews) · [Capterra](https://www.capterra.com/p/10003121/Genie-AI/reviews/)
- [Juro — G2](https://www.g2.com/products/juro/reviews) · [Capterra](https://www.capterra.com/p/167130/Juro/) · [GetApp](https://www.getapp.com/operations-management-software/a/juro/reviews/) · [Oneflow on Juro (competitor)](https://oneflow.com/uk/blog/juro-reviews/) · [ContractSafe vs Juro (competitor)](https://www.contractsafe.com/contractsafe-vs-juro-comparison) · [PandaDoc on Juro (competitor)](https://pandadoc.com/blog/juro-review)
- [Luminance — Gartner](https://www.gartner.com/reviews/vendor/luminance) · [ToolRadar](https://toolradar.com/tools/luminance) · [Spellbook on Luminance pricing (competitor)](https://spellbook.com/learn/luminance-pricing)

**Problem**
- [WorldCC — Contract Management 2025](https://info.worldcc.com/contract-management-aug-2025)
- [Legal Dive — contract value erosion](https://legaldive.com/news/contract-value-erosion-CLM-software-contracts-contracting/688790)

**Risks and regulation**
- [AI hallucinations in courts (UNC Law Library)](https://library.law.unc.edu/2026/06/handling-hallucinations-a-reflection/) · [Stanford CIS](https://cyberlaw.stanford.edu/blog/2025/10/whos-submitting-ai-tainted-filings-in-court/)
- [Legal assistance outside the reserved professions (Palestra)](https://ojs.academicon.pl/palestra/article/download/8212/8452/22856) · [Uprawnienia do świadczenia pomocy prawnej (e-prawnik.pl)](https://e-prawnik.pl/porady-prawne/uprawnienia-do-swiadczenia-pomocy-prawnej.html)
- [BGH Smartlaw (LTO)](https://www.lto.de/recht/juristen/b/bgh-urteil-izr11320-vertragsgenerator-smartlaw-keine-unzulaessige-rechtsdienstleistung-rak-hamburg-rdg-legal-tech) — EU context
- [EU AI Act Omnibus (Hogan Lovells)](https://www.hoganlovells.com/en/publications/eu-legislators-agree-to-delay-for-highrisk-ai-rules) · [Orrick](https://www.orrick.com/ja-JP/Insights/2026/07/EU-AI-Act-Update-Digital-Omnibus-Finalizes-8-Compliance-Changes)
