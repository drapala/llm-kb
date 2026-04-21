---
citation: "Hrdy, Camilla A. (2025). Trade Secrets and Artificial Intelligence. Rutgers Law School Research Paper. Forthcoming in Elgar Concise Encyclopedia of Artificial Intelligence and the Law (Abbott & Rothman eds., Edward Elgar, 2026)."
ssrn_id: "5350892"
posted: 2025-07-14
length_pages: 7
venue: "Encyclopedia chapter (Edward Elgar, forthcoming 2026); Rutgers Law School Research Paper"
url: https://ssrn.com/abstract=5350892
affiliation_author: "Rutgers Law School; Yale Information Society Project"
stub: true
stub_reason: "PDF SSRN exige login; abstract estruturado via WebSearch 2026-04-20. Texto curto (7pp) — ingestão full recomendada quando PDF disponível."
download_blocked: ssrn_auth_required
download_attempt_2026_04_20: "WebFetch retornou HTTP 403 em https://papers.ssrn.com/sol3/papers.cfm?abstract_id=5350892. Abstract + key doctrinal points disponíveis via RIIPL + SSRN metadata. Full PDF exige SSRN login — não executável nesta sessão. Próximo attempt: manual download + re-ingest."
ingested: 2026-04-20
type: legal-article
---

# Trade Secrets and Artificial Intelligence (Hrdy 2025)

## Citation

Hrdy, Camilla Alexandra, *Trade Secrets and Artificial Intelligence* (July 14, 2025). Rutgers Law School Research Paper, forthcoming in *Elgar Concise Encyclopedia of Artificial Intelligence and the Law* (Ryan Abbott & Elizabeth Rothman eds., Edward Elgar, 2026). Available at SSRN: https://ssrn.com/abstract=5350892.

## Summary

Mapeamento doutrinário curto (7pp) da interação entre **trade secret law** e **artificial intelligence**. Categoriza o que pode ser protegido como trade secret em pipelines de AI:

1. **Training data** — datasets proprietários usados em training.
2. **Model weights** — "model weights" destacados como emerging AI trade secret (Hrdy & Corsello USPTO presentation 2025).
3. **Prompts / system prompts** — production system prompts frequentemente kept secret.
4. **Telemetry / usage patterns** — agregados de interação usuário-modelo.
5. **Fine-tuning procedures** — pipelines de alignment e tuning propriamente tidos como secret.

## Doutrina Central

**Reasonable measures requirement** (core of trade secret law under DTSA 2016 + state UTSA):
- Para qualificar como trade secret, information deve ser (a) economically valuable, (b) not generally known, (c) subject to reasonable efforts of secrecy.
- **Implicação crítica para AI**: sem medidas razoáveis (access controls, NDA, technical barriers), proteção de trade secret evapora — mesmo que info seja objetivamente secreta.

## Pontos Doutrinários Chave

- Overlap trade secret × patent × copyright × contract em AI — contract (NDA) frequentemente the primary defensive layer.
- Cases envolvendo trade secrets em AI cresceram 2023-2025 (cite: Hrdy & Corsello USPTO presentation).
- **Model weights** novos como conceito de trade secret merecem tratamento distinto de código tradicional.

## Relevância para E39 Gap 3

- **Reasonable measures requirement** é test operacional: cross-tenant learning sem access controls + NDA compliance não é apenas risk contratual — é violação proativa de reasonable measures, **pode destruir claim de trade secret do cliente**.
- **Model weights como trade secret** relevante para claude-pipeline: rules/lessons derived from tenant A's code patterns contêm derivative information de weights expostos a esses patterns — argumento para isolation-by-default.
- **Contract is primary layer**: NDA/MSA clauses sobre training e derivative use dominam análise; data-privacy framework (GDPR, CCPA) não cobre trade secret.

## Notas de Ingestão

Stub. Texto curto (7pp) — download SSRN recomendado próxima sessão para extração verbatim. Encyclopedia chapter é secondary (não primary empirical), mas Hrdy é **primary doctrinal authority** na área, o que coloca quality=primary neste caso.

## Contexto Adicional

Hrdy é full professor Rutgers Law + Yale ISP fellow, autora de múltiplos papers sobre trade secret law. Presentation no USPTO (setembro 2025) com Corsello (IBM) discutiu role of trade secrets em AI R&D, types of info protectable, model weights como emerging trade secret.
