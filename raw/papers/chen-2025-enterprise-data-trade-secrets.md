---
citation: "Chen, Yang (2025). The Promise and Perils of Enterprise Data as Trade Secrets. 29 Stanford Technology Law Review 1."
ssrn_id: "5456754"
posted: 2025-06-12
venue: "Stanford Technology Law Review, Vol. 29, p. 1"
url: https://law.stanford.edu/publications/the-promise-and-perils-of-enterprise-data-as-trade-secrets/
pdf_url: https://law.stanford.edu/wp-content/uploads/2026/01/Enterprise-Data-as-Trade-Secrets.pdf
ssrn_url: https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5456754
affiliation_author: "City University of Hong Kong, School of Law"
pdf_path: raw/papers/chen-2025-enterprise-data-trade-secrets.pdf
stub_upgraded: 2026-04-20
ingested: 2026-04-20
type: legal-article
---

# The Promise and Perils of Enterprise Data as Trade Secrets (Chen 2025)

## Citation

Yang Chen, *The Promise and Perils of Enterprise Data as Trade Secrets*, 29 Stan. Tech. L. Rev. 1 (2025). Available at https://law.stanford.edu/wp-content/uploads/2026/01/Enterprise-Data-as-Trade-Secrets.pdf and https://ssrn.com/abstract=5456754.

## Contributions (per abstract + analyses)

### 1. Doctrinal Framework

Identifica três categorias distintas de enterprise data qualificáveis como trade secret:

- **Confidential enterprise data** — fully private, access-controlled data (ex: client lists, internal metrics, proprietary research).
- **Private data compilations** — agregados privados derivados de operações internas (ex: usage telemetry, analytics aggregates, behavior patterns).
- **Semi-public enterprise data compilations** — **front-end publicly accessible**, mas **back-end compilation kept private**. Exemplo: plataforma cuja UI é acessível mas cujo aggregate index/rank é secreto.

### 2. Comparative Analysis (US / China / EU)

- **US**: protection sob DTSA 2016 + state UTSA; cases recentes (ex: *Compulife v. Newport*) expandem protection mas criam standards incertos.
- **China**: protection sob Anti-Unfair Competition Law 2019; crescente mas com standards diferentes (mais deferência a formal secrecy marking).
- **EU**: Trade Secrets Directive 2016/943; mais restritivo, exige reasonable steps demonstrados.

Categorias 1 e 2 (confidential, private compilations) têm **crescente reconhecimento** em todas as jurisdições.

### 3. Normative Critique da Categoria 3 (Semi-public)

Chen argumenta que proteger semi-public compilations como trade secret **não serve aos objetivos core de trade secret law**:

- **Compulife standard problematic**: ruling depende da dificuldade de reconstrução por **human manual effort**, ignorando scraping technology atual. Quando fatorado assistance tecnológica, most semi-public compilations são **readily ascertainable** e portanto não devem qualificar.
- **Arms race inefficiency**: proteger semi-public incentiva measures cada vez mais agressivas (IP blocking, CAPTCHAs, device fingerprinting), escalando arms race em vez de alleviá-lo.

Chen propõe standard mais restritivo: trade secret protection para semi-public apenas se **front-end access é meaningfully restricted a um limited number of users**.

## Relevância para E39 Gap 3

- **Category 2 (Private data compilations)**: rules/lessons/antipatterns derivados de codebase interno de cliente = **private enterprise data compilation**. Treat as trade secret by default.
- **Reasonable steps requirement** (EU especialmente rígido): cross-tenant learning sem tenant isolation pode violar "reasonable steps" expected, mesmo se cliente A não tem objeção direta — **EU court pode ruling que cliente A falhou em proteger e portanto perdeu proteção**.
- **Category 3 critique**: se pipeline infer padrões de tenant via scraping + aggregation, argumento Chen de que "readily ascertainable with technology" enfraquece claim cliente. **Importante**: argumento corta dos dois lados — pode beneficiar ou prejudicar dependendo de quem reclama.
- **Comparative US/China/EU**: implica que deploy multi-jurisdictional exige matrix de compliance, não single ADR. EU mais rígido, China mais deferencial a formal marking, US mais casuístico.

## Notas de Ingestão

**Stub upgraded 2026-04-20** — PDF público baixado via WebFetch de `https://law.stanford.edu/wp-content/uploads/2026/01/Enterprise-Data-as-Trade-Secrets.pdf` (986KB). Extração `pdftotext -layout` → 2674 linhas. Versão é "Fall 2025 / 29 Stan. Tech. L. Rev. 1 (2026)" — nota: paper cita próprio ano de publicação como **2026** na capa, embora data de SSRN seja 2025-06-12.

**Verificação post-PDF (2026-04-20):**
- **Três categorias (confidential / private compilations / semi-public)** confirmadas no Table of Contents (sections II.A, III.A, III.B).
- **Compulife Software v. Newman, 959 F.3d 1288 (11th Cir. 2020)** confirmado como leading case criticado.
- **DTSA 2016** confirmado como US federal framework.
- **Directive 2016/943** confirmada como EU framework mais restritivo.
- **China Anti-Unfair Competition Law 2019** confirmado.
- **Normative argument** — trade secret protection para semi-public data compilations fails core theoretical aims porque protection extension não gera business efficiency justificando custos. Stub original capturou essencialmente isto.
- **Data scraping** — paper (Section IV.B) argumenta que scraping sem intrusion ou direct circumvention of access controls não deve ser sanctionável via trade secret law. Stub original capturou.

## Contexto Autoral

Yang Chen: assistant professor City University of Hong Kong. LLB China University of Political Science & Law, LLM LSE, LLM + SJD Penn Law. Publicação em Stanford TLR é high-quality primary legal scholarship.
