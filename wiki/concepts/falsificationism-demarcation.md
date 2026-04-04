---
title: "Falsificationism and the Demarcation Problem (Popper)"
sources:
  - path: raw/papers/popper-1963-science-conjectures-refutations.md
    type: paper
    quality: primary
    stance: neutral
  - path: raw/articles/popper-falsifiability-scientific-method.md
    type: article
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [philosophy-of-science, falsificationism, demarcation, popper, testability, pseudoscience]
source_quality: high
interpretation_confidence: high
resolved_patches: []
reads: 0
retrievals_correct: 0
retrievals_gap: 0
last_read: 2026-04-04
quarantine: false
---

## Resumo

Popper (1963): critério de demarcação ciência/pseudociência não é verificabilidade (indução) mas falsificabilidade — uma teoria é científica se e somente se faz predições que PODERIAM ser refutadas. Einstein > Freud/Adler/Marx: Einstein especificou condições de teste; os outros acomodaram qualquer evidência. Corolário: confirmações fáceis têm pouco valor epistêmico; uma boa refutação vale mais que mil confirmações.

## Conteúdo

### O problema: como distinguir ciência de pseudociência?

Popper em 1919 observou que marxismo, psicanálise freudiana e psicologia individual adleriana pareciam igualmente capazes de "explicar" qualquer evento. Contraste com Einstein: a teoria da relatividade fez predições específicas que PODERIAM ter sido falsas (deflexão da luz pelo sol) — e foram testadas por Eddington (1919).

O problema não era "quando uma teoria é verdadeira?" mas "quando uma teoria é científica?"

### Critério de demarcação: falsificabilidade

**Definição:** Uma teoria T é científica se e somente se existe uma observação possível que, se ocorresse, seria incompatível com T.

- **Falsificabilidade ≠ falsidade:** Uma teoria pode ser falsificável sem estar errada. "Todos os cisnes são brancos" é falsificável (basta encontrar um cisne preto) e era errada (cisnes negros existem na Austrália).
- **Verificabilidade ≠ cientificidade:** "Existem unicórnios invisíveis" não é falsificável, portanto não é científica — independentemente de ser verdadeira ou falsa.
- **Confirmações têm valor limitado:** "A stream of confirmations... which in the eyes of their admirers constituted the strongest argument in favour of these theories" — Popper vê isso como fraqueza, não força.

### Assimetria lógica entre verificação e falsificação

**Verificação:** Nenhum número de confirmações pode provar universalmente uma teoria. "Todos os corvos são pretos" não pode ser verificado por finitas observações (problema da indução de Hume).

**Falsificação:** Uma única observação contraditória refuta a teoria logicamente. Modus tollens: se T → O e não-O, então não-T.

**Consequência prática:** Uma boa teoria científica faz predições precisas e arriscadas — que poderiam facilmente ser falsas. Quanto mais a teoria arrisca (prediz que algo NÃO vai ocorrer), mais é refutada a cada observação compatível.

### Conteúdo empírico e degrees of testability

Popper conecta falsificabilidade ao conteúdo informativo:
- Teoria que diz "ou vai chover ou não vai" tem conteúdo = 0
- Teoria que prediz "vai chover exatamente 3.2mm às 14h" tem conteúdo máximo

**"The degree to which a statement is falsifiable is also the degree to which it is empirically informative."**

### Relação com a lógica da descoberta científica

Popper propõe substituir o "método indutivo" por um ciclo:
1. **Problema** — anomalia ou questão
2. **Tentative theory** — hipótese ousada
3. **Eliminação de erros** — testes severos que tentam refutar
4. **Novo problema** — gerado pela refutação ou sobrevivência

Ciência progride por **conjecturas e refutações**, não por acumulação indutiva.

### Casos test: Freud, Adler vs. Einstein

**Freud e Adler:** "Whatever happened always confirmed it." Qualquer comportamento poderia ser interpretado via pulsão reprimida (Freud) ou sentimento de inferioridade (Adler). Tais teorias têm conteúdo empírico ≈ 0.

**Einstein:** "If observation shows that the predicted effect is definitely absent, then the theory is simply refuted." A predição de deflexão de 1.75" era específica e arriscada — se Eddington medisse 0", a relatividade geral teria sido refutada.

## Verificação adversarial

**Claim mais fraco:** O critério de falsificabilidade é difícil de aplicar a teorias complexas com hipóteses auxiliares — Duhem-Quine: qualquer teoria pode ser salva de qualquer refutação ajustando hipóteses auxiliares.

**O que o paper NÃO diz:** Popper não discute como uma comunidade científica deve decidir quando uma hipótese auxiliar é legítima vs. ad hoc. Lakatos (1970) elabora isso com os conceitos de "hard core" e "protective belt".

**Simplificações:** "Pseudociência" como categoria binária (científico vs. não-científico) é problemática. Teorias existem num espectro de testabilidade. Kuhn (1962) argumenta que paradigmas em ciência normal são "puzzle-solving", não falsificação — e que falsificação acontece apenas em revoluções.

**Prior work:** Hume (problema da indução), Mach (ciência como economia de pensamento), Schlick e o Círculo de Viena (verificabilidade). Popper escreve explicitamente contra o positivismo lógico do Círculo de Viena.

## Conexões

- complementsAt: [[scientific-research-programmes]] ON "how to apply falsification in practice" — Lakatos (1970) responde à crítica Duhem-Quine que Popper deixa sem resposta: o que conta como refutação legítima vs. ajuste ad hoc?
- complementsAt: [[question-taxonomy]] ON "Popper-style questioning" — o question-taxonomy já referencia Popper como framework de questionamento; este artigo fornece a base filosófica subjacente
- partOf: [[curation-anti-bias]] ON "testable predictions as quality signal" — a exigência de predições falsificáveis ressoa com o critério de quarentena da KB (especulações não testáveis → quarantena)

## Fontes

- [Popper — Science: Conjectures and Refutations (Ch.1)](../../raw/papers/popper-1963-science-conjectures-refutations.md) — critério de demarcação, assimetria verificação/falsificação, casos Einstein vs. Freud/Adler
- [Popper — Falsifiability (artigo resumo)](../../raw/articles/popper-falsifiability-scientific-method.md) — síntese do mesmo material

## Níveis epistêmicos

### Descrição (verificado)
- Critério de demarcação: falsificabilidade ≠ verificabilidade
- Assimetria lógica: verificação por indução é impossível; falsificação por modus tollens é possível
- Casos concretos: Einstein vs. Freud/Adler/Marx
- Ciclo conjecturas-refutações

### Interpretação (nossa)
- Conexão com critério de quarentena da KB

## Quality Gate
- [x] Wikilinks tipados: 3 (complementsAt ×2, partOf)
- [x] Instance→class: falsificabilidade como critério de Popper (1963), não como lei lógica universal — tensão com Duhem-Quine reconhecida
- [x] Meta-KB separado: referência à KB apenas em conexão de partOf
- [x] Resumo calibrado: não exagera o escopo do critério
