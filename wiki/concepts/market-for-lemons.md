---
title: "Market for Lemons (Akerlof 1970)"
sources:
  - path: raw/papers/akerlof-1970-market-for-lemons.pdf
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [economics, information-asymmetry, adverse-selection, market-failure, signaling, procurement, b2g]
source_quality: high
interpretation_confidence: high
resolved_patches: []
provenance: source
reads: 2
retrievals_correct: 2
retrievals_gap: 0
last_read: 2026-04-08
quarantine: false
---

## Resumo

Akerlof (1970) demonstra que a assimetria de informação sobre qualidade pode destruir mercados por completo. No modelo de carros usados ("lemons"), vendedores conhecem a qualidade do bem mas compradores não — apenas a distribuição média. Como resultado, compradores pagam preço médio; vendedores de carros bons saem do mercado; a qualidade média cai; e o ciclo pode eliminar todo o comércio. Nobel de Economia 2001.

## Conteúdo

### O modelo formal: mercado de automóveis

Existem 4 tipos de carros: novos bons, novos ruins (lemons), usados bons, usados ruins. A probabilidade de um carro ser bom é q; de ser lemon é (1−q).

**Assimetria de informação:** Após possuir um carro, o dono aprende sua qualidade. Compradores sabem apenas a distribuição. Resultado: carros bons e ruins são vendidos ao mesmo preço.

**Modelo formal com dois grupos de traders:**
- Grupo 1 (vendedores potenciais): utilidade `U₁ = M + Σxᵢ` onde xᵢ = qualidade do i-ésimo carro
- Grupo 2 (compradores potenciais): utilidade `U₂ = M + Σ(3/2)xᵢ`

Grupo 1 tem N carros com qualidade distribuída uniformemente em [0,2]. Grupo 2 não tem carros.

**Oferta de carros:** `S₂ = pN/2` para p ≤ 2; qualidade média dos carros ofertados = p/2.

**Demanda do grupo 2:** `D₂ = Y₂/p` se `3μ/2 > p`; zero se `3μ/2 < p`.

**Equilíbrio sem troca:** Com μ = p/2, a condição de demanda do grupo 2 requer `3(p/2)/2 > p` → `3p/4 > p` → impossível para p > 0. **Nenhuma troca ocorre a nenhum preço positivo.**

Isso contrasta com o caso de informação simétrica (ambos sabem qualidade): nesse caso, equilíbrio com troca positiva existe para p = 1 (se Y₂ < N) ou p = Y₂/N (se 2Y₂/3 < N < Y₂).

### Generalização (caso contínuo)

No caso mais geral com múltiplos graus de qualidade, a dinâmica é: preço cai → qualidade média cai → preço cai mais → pode ocorrer colapso total do mercado. Gresham's law generalizada: carros ruins expulsam os bons (assim como moeda ruim expulsa boa) — mas com uma diferença: em Gresham's original, tanto comprador quanto vendedor distinguem boa de má moeda; no mercado de lemons, apenas o vendedor distingue.

### Aplicações

**A. Seguro saúde:** À medida que o preço do seguro sobe, os que têm certeza de precisar se tornam proporção maior dos segurados (adverse selection). Resultado: nenhum preço equilibra oferta e demanda. Dados: 1956 survey, 8,898 famílias — cobertura hospitalar cai de 63% (45-54 anos) para 31% (65+ anos). Justifica Medicare como análogo à despesa pública em estradas: cada indivíduo pagaria o custo esperado, mas nenhuma seguradora consegue oferecer a preço sustentável.

**B. Emprego de minorias:** Empregadores podem usar raça como statistic para habilidade quando não conseguem distinguir indivíduos no grupo. Decisão não é preconceito — é maximização de lucro dado custo de informação. Consequência: recompensas por investimento em qualificação acumulam ao grupo (elevando a média), não ao indivíduo — desincentivo ao treinamento.

**C. Custos da desonestidade:** Em mercado com mistura de agentes honestos e desonestos, agentes desonestos expulsam os honestos — não só pelo dano direto da fraude, mas por destruir o mercado legítimo. Em países subdesenvolvidos: qualidade mais heterogênea → custos de desonestidade maiores. India Export Quality Control Act (1963) cobre ~85% das exportações.

**D. Crédito em países subdesenvolvidos:** Taxas de juros do agiota local (15-50%) vs banco central (6-12%) refletem lemons problem: agiotas têm informação pessoal sobre clientes (crédito só onde granter tem "easy means of enforcing contract" ou "personal knowledge of the character of borrower"). Intermediário tentando arbitrar atrai os lemons e perde.

### Instituições que contrabalançam

Mercados desenvolvem mecanismos para reduzir assimetria:

1. **Garantias:** Transferem risco para o vendedor, que conhece a qualidade. Most consumer durables carry guarantees.
2. **Marcas (brand names):** Indicam qualidade esperada e proveem meio de retaliação ao comprador se qualidade não for cumprida. Novos produtos usam marcas antigas. Chains de restaurante em highways: oferecem qualidade média melhor que restaurante local médio (mas não melhor que o local favorito do residente).
3. **Licenciamento:** Médicos, advogados, barbeiros — certifica níveis mínimos de proficiência. High school diploma, PhD, Nobel Prize servem essa função.
4. **Redes de confiança pessoal:** Moneylenders no sul asiático operam com conhecimento íntimo de clientes — "com intimate knowledge of those around him he is able, without serious risk, to finance those who would otherwise get no loan at all" (Darling).

### Conclusão

"We have been discussing economic models in which 'trust' is important. Informal unwritten guarantees are preconditions for trade and production. Where these guarantees are indefinite, business will suffer — as indicated by our generalized Gresham's law." Arrow-Debreu não incorpora esse aspecto da incerteza. A dificuldade de distinguir qualidade boa de ruim é inerente ao mundo dos negócios.

## Interpretação

⚠️ Interpretação do compilador — não está explicitamente em Akerlof nesta forma.

**Relação com B2G:** Em licitações públicas, o comprador (governo) enfrenta assimetria de informação sobre qualidade das propostas. Fornecedores conhecem sua capacidade real; governo vê apenas preço e certificações. Contratos aditivos (expandindo contratos existentes perto do limite legal de 25%) podem ser estratégia de fornecedores para evitar o processo licitatório — precisamente o mecanismo de "marca/reputação" descrito por Akerlof sendo explorado para extrair renda.

**Relação com adverse selection em procurement:** Firmas que ganham licitações com preço baixo e depois pedem aditivos podem ser análogas ao modelo de lemons — a qualidade real (capacidade de execução) é observada pelo fornecedor mas não pelo governo no momento da licitação.

## Verificação adversarial

**O que o paper NÃO diz:**
- Não modela procurement público explicitamente (foco é mercado privado)
- A aplicação a B2G é nossa extensão, não derivada de Akerlof
- O modelo de dois grupos assume utilidade linear — simplificação explicitamente reconhecida pelo autor

**Robustez:** O resultado de "nenhuma troca" é extremo para o modelo linear específico. Com utilidade logarítmica ou concava, "exchange occurs but at suboptimal level" — Akerlof reconhece isso e mantém o modelo linear para focar no efeito qualitativo.

## Conexões

- [[market-failure-procurement]] — lemons como mecanismo subjacente de falha em procurement público
- [[information-asymmetry-b2g]] — assimetria vendedor/comprador em licitações
- [[tirole-procurement-renegotiation]] — renegociação como consequência de contratos incompletos com info assimétrica

## Fontes

- [Akerlof (1970)](../../raw/papers/akerlof-1970-market-for-lemons.pdf) — Quarterly Journal of Economics, Vol. 84, No. 3, pp. 488-500. Modelo formal completo, aplicações (seguro, minoria, desonestidade, crédito), instituições contrabalanceadoras.
