# Segmentação de Diário Oficial — Abordagem análoga a NER (UnB/PPGI)

**Origem:** Seminário PPGI/UnB (ID: seminario-23-04-21)  
**URL:** https://ppgi.unb.br/index.php?Itemid=489&catid=78:noticias&id=445:seminario-23-04-21&lang=pt&option=com_content&view=article  
**Apresentado em:** Agosto 2022  
**Pesquisador:** Micael Filipe Ribeiro de Lima (mestrando)  
**Orientador:** Prof. Thiago de Paulo Faleiros  
**Domínio:** Diário Oficial do Distrito Federal (DODF)  
**Type:** note — seminário acadêmico; sem paper publicado com PDF acessível

---

## Hipótese Central

Segmentação semântica/tópica **não funciona** para Diários Oficiais porque a linguagem é especializada e compartilha vocabulário similar entre seções. A abordagem correta é sequence labeling análogo a NER, com modelos CRF-LSTM identificando **tokens de fronteira estrutural**.

---

## Evidências

- Experimentos com segmentação semântica falharam para o Diário Oficial do Distrito Federal (DODF)
- CRF-LSTM obteve "resultados promissores" em identificação de segmentos de atos de pessoal
- O problema é de **boundary detection estrutural**, não de classificação por conteúdo
- A formulação como sequence labeling (análogo a NER) é mais adequada que como topic detection

### Contexto Técnico

O DO do DF organiza informações em seções com tipos de publicação diversos:
- Atos de pessoal (portarias de nomeação, exoneração, concessão)
- Extratos de contrato
- Termos aditivos
- Avisos de licitação

Modelos tradicionais de NER requerem blocos limitados de sentenças, criando um gargalo de segmentação — o problema é identificar onde cada ato começa e termina antes de aplicar qualquer extração.

O vocabulário normativo especializado e compartilhado entre categorias inviabiliza identificação por conteúdo semântico: "a semântica não consegue distinguir de forma confiável as seções do DO, pois a linguagem especializada é similar entre categorias".

---

## Limitações / Falsificadores

- Seminário acadêmico sem paper revisado por pares — resultados "promissores" sem F1/Pk publicados
- Testado apenas no DODF — generalização para outros estados não validada empiricamente
- Modelos mais recentes (BERT fine-tuned para sequence labeling) podem ter desempenho diferente
- Não há informação sobre tamanho do dataset de treinamento usado

---

## Relevância para Zelox

**CRÍTICA** — É o finding mais importante para o design do pipeline de ingestion:

1. Invalida semantic chunking como estratégia primária para DOs
2. O boundary detector deve ser treinado como **sequence labeler** sobre tokens estruturais (cabeçalhos, numerações, assinaturas)
3. NÃO deve ser um classificador semântico/tópico

---

## Implication de Design

Tokens-alvo para sequence labeling em DOs:
- Cabeçalhos tipográficos (PORTARIA Nº, EXTRATO DE CONTRATO, AVISO DE LICITAÇÃO)
- Padrões de numeração (Art. X, § Y, item Z)
- Tokens de assinatura/autoridade (Secretário de Estado, Prefeito Municipal)
- Datas e locais de publicação

---

## Conexões

- Confirma: Aumiller 2021 é baseline negativo (semantic segmentation falha para DOs)
- Fundamenta: MultiLegalSBD metodologia de anotação para capturar tokens estruturais
