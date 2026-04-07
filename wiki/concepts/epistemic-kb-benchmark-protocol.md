---
title: "Epistemic KB Benchmark Protocol"
sources: []
created: 2026-04-07
updated: 2026-04-07
tags: [meta-kb, benchmark, calibration, epistemic, experimental-design]
source_quality: low
interpretation_confidence: low
resolved_patches: []
provenance: emergence
emergence_trigger:
  pair: [kalshib-t0-rag, autonomous-kb-failure-modes]
  ask_session: outputs/logs/sessions/2026-04-07/ask-benchmark-metaxon.md
  connection_type: EMERGE-DE
  pearl_level: L2
emerged_on: 2026-04-07
quarantine: true
quarantine_reason: "draft — Braço B não totalmente congelado; leakage control e critérios T30 ainda incompletos; sem precedente empírico"
stability: tentative
---

## Resumo

Protocolo de benchmark para comparar KBs com guardrails epistêmicos (como metaxon) contra baselines vanilla. Separa dois problemas distintos: **calibração** (o sistema responde com confiança melhor hoje?) e **degradação temporal** (o sistema piora sob ingest contínuo?). O Eixo 1 é implementável agora; o Eixo 2 requer experimento novo de 30+ dias.

## Conteúdo

### Definição de Baseline ("vanilla")

[[kb-architecture-patterns]] Pattern 1 sem guardrails: `raw/ → wiki/ → /ask` sem stance tracking, sem quarantena, sem Gate 3, sem Bradford quota, sem corpus sufficiency check. Não é straw man — é o que qualquer KB simples com RAG faz.

### Eixo 1 — Calibração (implementável agora)

**Inspirado em:** [[kalshib-t0-rag]] (protocolo 3 braços para ECE/Brier score).

#### Braços — definições congeladas

Cada variável precisa estar explicitamente ativada ou desativada em cada braço para evitar confusão de variáveis:

| Configuração | Braço A | Braço B | Braço C |
|---|---|---|---|
| Contexto / retrieval | nenhum | wiki compilado, retrieval simples | wiki compilado, retrieval 3 camadas |
| Corpus sufficiency check | — | desligado | ligado |
| Stance tracking / Bradford | — | desligado | ligado |
| Quarantine / promoção | — | desligado | ligado |
| Challenge adversarial (Gate 3) | — | desligado | ligado |

Braço B = "metaxon com retrieval mas sem pipeline epistêmico." Isola o valor da arquitetura de indexação da camada de validação.

Se o objetivo for ablação completa, adicionar Braço D = Braço C sem Gate 3 (mede o delta do oracle especificamente).

#### Métricas

| Métrica | Definição | Papel |
|---------|-----------|-------|
| accuracy | % corretas | Linha de base |
| ECE | Expected Calibration Error | Métrica primária de calibração |
| Brier score / BSS | Quadratic scoring rule | Composta (accuracy × calibração) |
| selective_accuracy | accuracy acima de um limiar de confiança (ex: > 0.7) | Detecta se sistema é mais útil quando está confiante |
| abstention_rate | % "não sei" | Sinal de saúde epistêmica |
| abstention_quality | accuracy condicional em não-abstenção | Distingue abstention útil de abstention covarde |
| overconfidence_gap | mean_confidence − accuracy observada | Medida direta de overconfidence |

**Cautela:** um sistema pode melhorar ECE simplesmente ficando mais tímido, sem ficar mais útil. `selective_accuracy` e `abstention_quality` protegem contra esse caso.

#### Hipóteses falsificáveis

- **H1:** ECE(C) < ECE(A) — pipeline epistêmico reduz overconfidence
- **H2:** ECE(B) > ECE(C) — challenge adiciona valor além do retrieval sozinho
  - Falsificador: se ECE(B) ≤ ECE(C), challenge não adiciona valor de calibração
- **H3:** selective_accuracy(C) ≥ selective_accuracy(A) — sistema mais confiante é também mais preciso quando confiante
  - Falsificador: se selective_accuracy(C) < selective_accuracy(A), o pipeline apenas reduz confiança sem melhorar seletividade

#### Conjunto de teste — 3 classes de perguntas

Necessário para detectar se o sistema preserva nuance ou apenas memoriza headline. As perguntas precisam ser **cegas ao corpus** — não parafraseadas do wiki, derivadas do raw/ com verificação externa.

| Classe | Exemplo | O que testa |
|--------|---------|-------------|
| **Extração literal** | "Qual foi o % de redução em gastos faltantes no experimento de Olken?" | Recall de fato numérico. Ground truth: raw/papers/ original |
| **Comparação intra-paper** | "Olken (2007) compara dois mecanismos de redução de corrupção — qual teve efeito zero?" | Retenção de contraste interno. Testa se nuance foi colapsada |
| **Contradição / caveat** | "O paper de Shumailov et al. identifica uma condição em que model collapse não ocorre — qual é?" | A mais importante. Testa se caveats sobrevivem à compilação |

A terceira classe é a mais diagnóstica para FM1 (convergência semântica): sistemas que homogeneízam tendem a reter headline mas perder exceções e condicionais.

**Leakage control:** perguntas geradas do raw/ original (não do wiki), respondidas pela ground truth do paper. Se as respostas estiverem visíveis no wiki de forma quase literal, mede-se recall do compilado, não robustez epistêmica.

---

### Eixo 2 — Degradação temporal (requer 30+ dias)

**Fundamentado em:** [[autonomous-kb-failure-modes]] — Stage B: métricas verdes enquanto acurácia factual erode silenciosamente. O timeline do artigo (7-30 dias) é especulativo — sem base empírica. Este benchmark seria a primeira medição real.

#### Variáveis a congelar (ambos os braços)

Para que o drift seja atribuível à arquitetura, não à interação:

- **Ordem de ingestão idêntica** — mesmos papers, mesma sequência
- **Mesma janela de challenge** — mesmo número de challenges por artigo (ou zero no vanilla)
- **Mesma pressão de queries** — aplica-se conjunto de perguntas de calibração idêntico em T0, T14, T30
- **Sem queries intermediárias** — ou com queries idênticas nos dois braços; queries assimetricas podem induzir drift via retrieval feedback

#### Métricas adicionais para degradação

| Métrica | Definição | FM detectado |
|---------|-----------|-------------|
| accuracy_delta(T30-T0) | Quanto accuracy caiu | FM1-FM2 |
| ECE_delta(T30-T0) | Quanto calibração piorou | FM2 |
| caveat_preservation_rate | % de caveats originais do raw/ ainda presentes no wiki em T30 | FM1, FM4 |
| stance_diversity_index | Proporção confirming:challenging ao longo do tempo | FM1 |
| contradiction_retention | % de claims contraditórios preservados (não forçosamente resolvidos) | FM4 |

**Sobre similaridade semântica entre artigos:** útil como proxy para FM1, mas perigoso como métrica central — similaridade legítima em temas próximos seria penalizada. Usar apenas como **indicador auxiliar**, combinado com `caveat_preservation_rate` e `stance_diversity_index`.

#### Ground truth para T30

[[autonomous-kb-failure-modes]] é explícito: "External ground truth precisa ser independente do LLM que mantém o wiki." Opções em ordem de robustez:

1. **Perguntas com respostas numéricas/verificáveis mecanicamente** — datas, percentuais, nomes de autores (não requerem julgamento)
2. **Human spot-check** — humano lê 5-10 artigos contra raw/ original por braço
3. **Modelo diferente como avaliador** — mitiga self-enhancement, mas não garante independência epistêmica se modelos têm training overlap ([[knowledge-collapse-llm]])

Opção 1 é a mais robusta. Opção 3 é necessária mas insuficiente.

---

### Estado atual

O Eixo 1 é implementável com:
1. Conjunto de perguntas derivadas de `raw/papers/` (trabalho manual: ~20-30 perguntas cobrindo as 3 classes)
2. Script de avaliação ECE/Brier (calculável a partir de confidence + outcome)
3. Protocolo de blindagem: perguntas geradas antes de ler o wiki

O Eixo 2 requer design experimental de 30 dias e decisão sobre o que conta como vanilla operacional (braço B precisa ter ingest automatizado sem gates — atualmente não existe script para isso).

## Interpretação

(⚠️ nossa interpretação) Se H1 e H2 forem confirmadas simultaneamente, fornece primeira evidência empírica de que guardrails epistêmicos melhoram calibração em KBs operadas por LLM — não apenas qualidade estrutural. Isso transforma /challenge de ferramenta editorial em mecanismo de epistemologia aplicada.

(⚠️ nossa interpretação) A separação Eixo 1 / Eixo 2 é a contribuição metodológica central: confundir os dois eixos produziria benchmark que mede mistura de variáveis sem poder atribuir causa.

## Conexões

- [[kalshib-t0-rag]] — protocolo 3 braços + ECE como métrica primária; este artigo generaliza para KBs factuais
- [[autonomous-kb-failure-modes]] — FM1-FM4 são o que o Eixo 2 precisa detectar; Stage B é o sinal-alvo
- [[knowledge-collapse-llm]] — Stage B é a manifestação empírica do que o Eixo 2 mede
- [[kb-architecture-patterns]] — Pattern 1 define a baseline vanilla; Pattern 1 sem guardrails = Braço A
- [[curation-anti-bias]] — leakage control é instância de curation-anti-bias aplicado ao conjunto de teste
- [[falsificationism-demarcation]] — H1/H2/H3 têm falsificadores explícitos; estrutura Popperiana intencional

## Fontes

- (este artigo emergiu de sessão /ask — sem fontes raw/ diretas; claims são síntese da KB)
