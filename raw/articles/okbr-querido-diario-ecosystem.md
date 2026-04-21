# Querido Diário — OKBR Open Source Ecosystem

**Origem:** Open Knowledge Brasil  
**URLs:**  
- https://docs.queridodiario.ok.org.br/pt-br/latest/contribuindo/raspadores.html  
- https://docs.queridodiario.ok.org.br/pt-br/latest/entendendo/arquitetura.html  
**Tipo:** documentação oficial do projeto open source  
**Type:** note — documentação técnica; repositório ativo

---

## Hipótese Central

Raspagem + extração textual + índice full-text (OpenSearch) é o estado da arte atual em acesso aberto a DOs brasileiros. O problema de **fatiamento por ato** (segmentação em ato administrativo individual) está explicitamente em aberto como frente de pesquisa.

---

## Estado Atual do Projeto

- **350+ municípios** integrados com spiders Scrapy; meta: 5570 (total de municípios brasileiros)
- **Pipeline geral:** Scrapy (coleta) → Apache Tika (extração texto PDF/DOC/DOCX) → OpenSearch (full-text + índices temáticos)
- **Armazenamento:** DO Spaces (arquivos), PostgreSQL (metadados), OpenSearch (índice de busca)
- **Agendamento:** série histórica (uma vez, ao integrar município); edição recente (diária, 18h Brasília); redundância mês anterior (1º de cada mês, 20h)
- **Problema de fatiamento por ato:** explicitamente descrito como trabalho em aberto

---

## Arquitetura em 3 Etapas

### 1. Coleta de Dados

- Framework: Python + Scrapy
- Armazenamento: DO Spaces (arquivos PDF/DOC/DOCX) + PostgreSQL (metadados)
- Repositório: https://github.com/okfn-brasil/querido-diario

### 2. Processamento de Dados

Esta é a etapa central — extração de texto, indexação e segmentação.

- Extração de texto: **Apache Tika** (suporta PDF Texto, DOC, DOCX)
- Indexação e filtros temáticos: **OpenSearch**
- **Segmentadores de diários agregados:** para DOs que cobrem múltiplos municípios em um único PDF, os segmentadores fatiam os trechos por município e produzem arquivos TXT individuais por município

**⚠️ Distinção crítica:** os segmentadores do QD operam em **nível de município** — identificam qual seção do DO pertence a qual município. Isso é **diferente** de segmentação por ato (onde cada portaria, extrato ou aviso é isolado). O QD não faz segmentação por ato.

**Filtros temáticos:** buscas no índice principal para criar sub-índices temáticos ("Tecnologias na Educação", "Políticas Ambientais")

**Não suportado:**
- **PDF Imagem** — não integrado por baixa qualidade na extração via OCR
- **Fragmentados** — limitações na modelagem do banco de dados
- Repositório: https://github.com/okfn-brasil/querido-diario-data-processing

### 3. Disponibilização de Dados

- **API Pública:** FastAPI + Swagger (https://api.queridodiario.ok.org.br/docs)
  - Endpoints para DOs e CNPJs da Receita Federal
  - PostgreSQL (metadados de empresas) + OpenSearch (busca em diários)
  - Repositório: https://github.com/okfn-brasil/querido-diario-api
- **Backend:** Django REST Framework + Celery (tarefas assíncronas) + Redis
  - PostgreSQL (gestão de usuários e alertas)
  - Repositório: https://github.com/okfn-brasil/querido-diario-backend
- **Frontend:** TypeScript + Angular (https://queridodiario.ok.org.br)
  - Repositório: https://github.com/okfn-brasil/querido-diario-frontend

---

## Estrutura Técnica dos Raspadores

### Classe Gazette (item scrapy)

Cada edição de DO é representada por um objeto Gazette com campos:
- `date` (datetime.date) — data de publicação; obrigatório
- `edition_number` (string) — número da edição; opcional (pode ser vazio)
- `is_extra_edition` (boolean) — se é edição extra/extraordinária; default False
- `power` (string) — `'executive'` ou `'executive_legislative'` — se contém apenas executivo ou também legislativo
- `file_urls` (list[string]) — URLs de download do arquivo

### Hierarquia de Classes

```
scrapy.Spider
  └── BaseGazetteSpider
        └── UFMunicipioSpider     # um por município (uf_nome_do_municipio)
        └── BaseSistemaSpider     # para municípios com mesmo layout de plataforma
              └── UFMunicipioSpider (sistema)
```

- Nomenclatura: `uf_nome_do_municipio` (ex: `df_brasilia`, `sp_sao_paulo`)
- `TERRITORY_ID`: código IBGE do município (de territories.csv)

---

## Três Topologias de DO Documentadas

| Topologia | Descrição | Status no QD |
|-----------|-----------|-------------|
| **Agregado** | DO completo em único PDF — atos e municípios não separados | Suportado (segmentador por município; fatiamento por ato em aberto) |
| **Individual** | Cada ato/edição publicado como arquivo separado | Suportado |
| **Fragmentado** | PDF com estrutura parcial, atos por quebra de página | **Não suportado** (limitação DB) |

---

## O que o QD NÃO Faz

OpenSearch full-text **sem segmentação por ato** é insuficiente para retrieval por entidade de contrato:
- Busca retorna o DO completo (ou seção municipal), não o ato específico
- Não há extração de entidades (CNPJ, valor, modalidade)
- Não há estrutura hierárquica (seção → ato → cláusula)
- PDF Imagem não está integrado — DOs em formato scaneado precisam de OCR externo

---

## Applicabilidade Zelox

**CRÍTICA como mapa do território.**

Os spiders do QD são open source — reutilizáveis para acesso por UF sem reinventar a roda. O `power` field do Gazette permite filtrar por tipo de poder publicador.

O que o Zelox faz além do QD:
1. Segmentação por ato (boundary detection — o que o QD deixou em aberto)
2. Extração de entidades (CNPJ, valor, modalidade, objeto)
3. Indexação tri-camada (entidade / ato / resumo)
4. Suporte a PDF Imagem via OCR (gap não coberto pelo QD)

---

## Conexões

- Fornece: infraestrutura de acesso aos DOs (spiders, extração de texto)
- Gap: boundary detection por ato (UnB/PPGI, Aumiller 2021)
- Complementa: MultiLegalSBD (metodologia de anotação para o que o QD não faz)
