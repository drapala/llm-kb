---
title: "Resource Competition and Coexistence (Tilman 1994)"
sources:
  - path: raw/papers/tilman-1994-competition-biodiversity.md
    type: paper
    quality: primary
    stance: neutral
created: 2026-04-04
updated: 2026-04-04
tags: [ecology, competition, coexistence, biodiversity, spatial, resource-ratio]
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

Tilman (1994): modelos não-espaciais preveem que no máximo n espécies coexistem em n recursos (princípio de exclusão competitiva). Modelo espacial com competição de vizinhança e dispersão aleatória inverte o resultado: potencialmente ilimitado número de espécies pode coexistir num único recurso via trade-off colonização-competição. Coexistência emerge de heterogeneidade espacial endógena, não de múltiplos recursos.

## Conteúdo

### O problema: exclusão competitiva vs. biodiversidade observada

Ecossistemas reais têm muito mais espécies do que recursos limitantes — paradoxo do plâncton (Hutchinson 1961). Modelos não-espaciais clássicos preveem exclusão competitiva: a espécie com menor R* (recurso de equilíbrio mínimo necessário) exclui todas as outras em competição por um único recurso.

**R* rule (Tilman 1980, 1982):** A espécie com menor R* exclui todas as outras. Em n recursos, no máximo n espécies coexistem em equilíbrio.

### O modelo espacial de 1994

**Variáveis de estado:** Fração do habitat ocupado por espécie i: pᵢ

**Competição de vizinhança:** A espécie superior competitiva (j) coloniza sítios ocupados pela inferior (i) a taxa cᵢpᵢpⱼ (j invade i)

**Dispersão:** Espécies colonizam sítios vazios à taxa cᵢpᵢ(1 - Σpⱼ)

**Perturbação:** Sítios são esvaziados à taxa m

**Regra de competição:** Espécies são hierarquicamente ordenadas: espécie 1 vence todas, espécie 2 vence todas exceto 1, etc.

### Resultado principal

Com competição de vizinhança e dispersão, as espécies podem coexistir indefinidamente se **espécies inferiores compensam via maior taxa de colonização**.

Condição de coexistência para espécie i+1 abaixo da i na hierarquia:

cᵢ₊₁ > [função de m, c₁,...,cᵢ e p₁,...,pᵢ]

**Trade-off colonização-competição:** Espécies que perdem na competição local sobrevivem colonizando espaços abertos mais rapidamente. Coexistência é dinâmica e espacialmente heterogênea.

**Biodiversidade ilimitada num único recurso:** Desde que o trade-off seja suficientemente forte, n espécies podem coexistir num único recurso limitante — resolução do paradoxo do plâncton sem requerer múltiplos recursos.

### Contraste com modelos não-espaciais

| Aspecto | Não-espacial | Espacial (Tilman 1994) |
|---|---|---|
| Previsão máx. espécies/recurso | 1 (R*) | Ilimitado |
| Mecanismo de coexistência | Múltiplos recursos | Trade-off C-C |
| Heterogeneidade | Exógena | Endógena |
| Equilíbrio | Estático | Dinâmico/não-equilíbrio |

### Implicações para diversidade

1. **Perturbação intermediária:** Perturbação baixa → exclusão competitiva; alta → colapso de tudo; intermediária → máximo de coexistência. Consistente com Connell (1978).
2. **Fragmentação do habitat:** Reduz dispersão efetiva → elimina o trade-off → reduz diversidade.
3. **Invasões biológicas:** Espécie invasora com C alto pode invadir mesmo sendo competitivamente inferior localmente.

## Verificação adversarial

**Claim mais fraco:** O modelo assume hierarquia de competição fixa e dispersão globalmente uniforme — em ecossistemas reais, a hierarquia muda com condições ambientais e a dispersão é limitada.

**O que o paper NÃO diz:** Não valida empiricamente o trade-off colonização-competição em sistemas reais (isso veio em trabalhos subsequentes); não modela especiação ou evolução.

**Simplificações:** O modelo é determinístico e em tempo contínuo — sistemas reais têm estocasticidade, especialmente em populações pequenas.

**Prior work:** MacArthur & Wilson (1967) island biogeography; Levins (1969) metapopulation; Tilman (1982) R* rule para modelos não-espaciais. O paper de 1994 é extensão espacial.

## Conexões

- contradicts: [[complexity-stability-tradeoff]] ON "spatial structure as stability mechanism" — May (1972): estrutura em blocos estabiliza sistemas aleatórios; Tilman (1994): espaço (competição de vizinhança) gera coexistência que modelos sem espaço não preveem. Espacialidade como solução para dois tipos de problemas
- complementsAt: [[complexity-stability-tradeoff]] ON "ecology framework" — May e Tilman são complementares: May pergunta "quando diversidade causa instabilidade?"; Tilman pergunta "como diversidade persiste apesar da competição?"

## Fontes

- [Tilman — Competition and Biodiversity in Spatially Structured Habitats](../../raw/papers/tilman-1994-competition-biodiversity.md) — trade-off colonização-competição, coexistência espacial, resolução do paradoxo da exclusão competitiva, Ecology 1994

## Níveis epistêmicos

### Descrição (verificado)
- R* rule (modelos não-espaciais): 1 espécie/recurso
- Modelo espacial: coexistência de n espécies/1 recurso via trade-off C-C
- Condição explícita de coexistência

### Interpretação (nossa)
- Conexão como complemento de May (1972) no framework de ecologia

## Quality Gate
- [x] Wikilinks tipados: 2 (contradicts, complementsAt)
- [x] Instance→class: previsões qualificadas como resultados do modelo, não observações diretas
- [x] Meta-KB separado: sem referências a esta KB
- [x] Resumo calibrado: limitação de heterogeneidade endógena vs. múltiplos recursos mencionada
