# MultiLegalSBD — Multilingual Legal Sentence Boundary Detection Dataset

**arXiv:** 2305.01211  
**Publicado:** 2023  
**URL:** https://arxiv.org/abs/2305.01211  
**Type:** STUB — arxiv HTML não disponível; baseado em análise do usuário  
**Nota:** Paper inclui pequeno conjunto em português (~1800 sentenças)

---

## Hipótese Central

É possível construir um dataset multilíngue de sentence boundary detection em textos legais com alta qualidade (F1 até 98.5%) usando anotação humana guiada por annotation guidelines explícitos. Inclui pequeno conjunto em PT.

---

## Guidelines de Anotação (Documentados no Paper)

- Anotação via **Prodigy** (ferramenta de anotação)
- Decisão de anotar o **span completo da sentença** (não apenas primeiro/último token) — incentiva o anotador a ler o texto completo, não apenas escanear terminadores
- Divisão de documentos longos: leis em chunks de 1-3 artigos por chunk; decisões divididas apenas se excedessem ~15.000 caracteres
- **Regras explícitas para casos ambíguos:** colons seguidos de newline, listas com itens incompletos, abreviações

---

## Resultados Quantitativos

| Modelo | F1 |
|--------|-----|
| CRF (treinado no dataset) | até 98.5% |
| NN (treinado no dataset) | até 98.5% |
| CRF em textos legais alemães **não vistos** | 81.1% ⚠️ |
| Modelos multilíngues (incluindo zero-shot PT) | 91.6% |

**Gap de generalização real:** 98.5% in-distribution → 81.1% out-of-distribution. Este resultado é crítico para qualquer abordagem que treina em um estado e aplica em outros.

---

## O que NÃO Existe (Gap para Zelox)

MultiLegalSBD é **sentence boundary**, não **act boundary**:

| Problema | Nível | Status |
|----------|-------|--------|
| Sentence boundary em texto legal | Token-level | Resolvido (F1 98.5%) |
| Act boundary em DOs brasileiros | Documento-level | **Gap — não existe dataset** |

O problema do Zelox é um nível acima: não onde termina a sentença, mas onde termina o **ato administrativo completo**.

---

## Transferência Metodológica para Zelox

O schema de anotação para DOs brasileiros deve documentar:

1. **Definição formal de "ato"** — o que é e o que não é um ato completo (extrato de contrato, portaria, aviso de licitação, despacho)
2. **Casos ambíguos explícitos:**
   - Atos que referenciam outros atos ("nos termos do Contrato nº X")
   - Republicações ("Republicado por incorreção")
   - Erratas
   - Atos conjuntos de múltiplos órgãos
3. **Critério de IAA (Inter-Annotator Agreement)** — mínimo definido antes de treinar qualquer modelo
4. **Tamanho mínimo por UF** — literatura sugere 300-500 exemplos para CRF-LSTM convergir

---

## Applicabilidade Zelox

**CRÍTICA como metodologia de referência** para o Gap 3 (Annotation Methodology).

O paper valida que annotation guidelines explícitos são o pré-requisito para qualquer modelo de boundary detection. O Annotation Schema Document para o Zelox deve seguir esta estrutura.

**Ferramenta de anotação alternativa:** Doccano (open source) ou Label Studio (open source com UI melhor) em vez de Prodigy (pago).

---

## Paper Adicional Relacionado

**Fine-Grained NER in Legal Documents (Leitner et al., Springer)**  
`springer.com/chapter/10.1007/978-3-030-33220-4_20`

67.000 sentenças, 54.000 entidades, 19 classes semânticas. Finding central: **não existe tipologia uniforme de conceitos semânticos** relacionados a NEs em documentos legais — as annotation guidelines precisam ser construídas do zero para cada domínio.

Implication para Zelox: antes de anotar qualquer linha de DO, é necessário um **Annotation Schema Document** formal que define as entidades do domínio B2G brasileiro (CNPJ-contratante vs CNPJ-contratado, valor-contrato vs valor-aditivo, modalidade vs fundamento legal).

---

## Conexões

- Fundamenta: Gap 3 (Annotation Methodology para boundary detection em DOs)
- Metodologia de referência: Prodigy/Doccano guidelines pattern
- Relaciona com: UnB/PPGI 2021 (CRF-LSTM como abordagem correta para DOs)
