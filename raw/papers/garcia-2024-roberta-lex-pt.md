# RoBERTaLexPT: A Legal RoBERTa Model pretrained with deduplication for Portuguese

**Venue:** PROPOR 2024 (Computational Processing of the Portuguese Language)  
**DOI:** 10.1007/978-3-031-45392-2_18  
**URL:** https://aclanthology.org/2024.propor-1.38.pdf  
**Autores:** Eduardo Garcia, Nadia Silva (UFG), Felipe Siqueira (USP), Juliana Gomes (UFG), Hidelberg O. Albuquerque, Ellen Souza (UFRPE), Eliomar Lima (UFG), André de Carvalho (USP)  
**Repositório:** https://github.com/eduagarcia/roberta-legal-portuguese

---

## Abstract

This work investigates the application of NLP in the legal context for the Portuguese language, emphasizing the importance of adapting pre-trained models from specialized corpora in the legal domain. We compiled and preprocessed a Portuguese Legal corpus (LegalPT), addressing challenges of high document duplication in legal corpora, and measuring the impact of hyperparameters and embedding initialization. Experiments revealed that pre-training on legal and general data resulted in more effective models for legal tasks, with RoBERTaLexPT outperforming larger models trained on generic corpora, and other legal models from related works. We also aggregated a legal benchmark, PortuLex benchmark.

---

## Corpus: LegalPT

- **Tamanho:** até 125 GiB de textos legais em português
- **Fontes:** documentos legais públicos agregados (legislação, jurisprudência, contratos, petições)
- **Contribuição chave:** primeiro corpus jurídico PT com **deduplicação explícita**
  - Prior corpora (Niklaus et al. 2023, Willian Sousa & Fabro 2019, Bonifacio et al. 2020): nenhum usava deduplicação
  - Deduplicated datasets tendem a melhorar performance de language models (Lee et al. 2022)
  - Modelos treinados sem deduplicação podem memorizar dados → contaminação train/val splits
- **Corpus adicional:** CrawlPT (general Portuguese) — combinação legal+geral produz modelos mais efetivos

---

## Benchmark: PortuLex

4 tarefas supervisionadas para avaliar LMs em direito PT-BR:

| Dataset | Task | Tipo |
|---------|------|------|
| RRI | Sentence classification | CLS |
| LeNER-Br | Legal NER | NER |
| UlyssesNER-Br | Legal NER | NER |
| FGV-STF | Sentence classification | CLS |

Todos anotados por especialistas legais (sem dados gerados automaticamente).

---

## Resultados

**RoBERTaLexPT supera:**
- BERTikal e JurisBERT (legal PT models) em todas as tarefas do PortuLex
- BERTimbau (generic PT) — significativamente nos benchmarks legais
- **LegalBert-pt (Silveira et al. 2023)** — superado em tarefas legais PT
- Modelos multilíngues maiores treinados em português legal (Niklaus et al. 2023)

**Nota sobre Niklaus et al. 2023:** modelo PT monolíngue falhou em superar BERTimbau em múltiplas tarefas legais — evidência de que apenas tamanho de corpus não basta; deduplicação e mix legal+geral importam.

---

## Contribuições Chave

1. **LegalPT corpus** — 125GiB, deduplicated, open access
2. **PortuLex benchmark** — 4 tarefas legais PT anotadas por especialistas
3. **RoBERTaLexPT** — melhor modelo legal PT-BR disponível (2024)
4. **Insight de deduplicação** — legal corpora têm alta taxa de duplicação; sem deduplicação, modelos memorizam ao invés de generalizar

---

## Limitações

- Avaliado principalmente em textos judiciais (jurisprudência, petições) — domínio administrativo/procurement não representado no PortuLex
- RoBERTa base (não large) — modelos maiores não testados com deduplicação
- Max sequence length: 512 tokens (padrão RoBERTa) — suficiente para chunks curtos, mas atos longos precisam truncação
- Corpus LegalPT tem viés para legislação federal e jurisprudência — DOs municipais provavelmente sub-representados
