# Lessons Learned from the Combined Development of OWL and SHACL

**Autores:** Edna Ruckhaus, Jhon Toledo, Edgar Alexis Martínez Sarmiento, Óscar Corcho (Universidad Politécnica de Madrid / OEG)  
**Publicação:** K-CAP 2025 (Knowledge Capture Conference)  
**DOI:** 10.1145/3731443.3771340  
**GitHub:** https://github.com/oeg-upm/shacl-owl-kcap-2025  
**Ano:** 2025  
**Tipo:** paper / primary  
**Status:** STUB — full text bloqueado por paywall ACM; conteúdo baseado em abstract, metadados, GitHub, e web search.

---

## Tese Central

Análise da combinação de OWL e SHACL em desenvolvimento prático de ontologias. Conclusão principal: **validação de knowledge graphs deve ser implementada em SHACL** (Closed World Assumption), enquanto **modelagem de domínio e inferência pertencem ao OWL** (Open World Assumption). As duas tecnologias têm semânticas fundamentalmente incompatíveis — tentar usar OWL para validação gera inferências inesperadas que conflitam com o comportamento de constraint esperado.

## Principais Findings

**OWL vs SHACL — quando usar cada um:**
- **OWL (Open World Assumption):** modelagem de domínio, subsunção de classes, inferência de novo conhecimento. Constraints OWL geram *novas inferências*, não erros de validação.
- **SHACL (Closed World Assumption):** toda validação de dados deve ser feita em SHACL. SHACL reporta violações; OWL reporta entailments.
- **Incompatibilidade semântica:** a mesma constraint expressa em OWL (ex: domain restriction) e SHACL tem comportamentos radicalmente diferentes — OWL inferirá novas classes, SHACL reportará violação.

**Shape templates identificados:**
- Validação de propriedades datatype/object
- Validação de taxonomias
- Grupos de regras de negócio reutilizáveis

## Domínios de Aplicação

**Railway Transport (RINF — Register of Infrastructure, Agência Ferroviária da UE):**
- KGs construídos com RML mappings, validados com SHACL
- Domínio regulatório europeu com requirements formais de conformidade

**Public Transport (Transmodel):**
- Referência europeia de interoperabilidade para transporte público

## Limitações

- Heterogeneidade de engines SHACL: diferentes suportes para componentes reutilizáveis
- OWL-to-SHACL conversion tools geram artefatos difíceis de manter (hash IDs para shapes)
- Propagação de mudanças entre OWL e SHACL é trabalhosa
- Performance em queries SPARQL + validação SHACL em grafos complexos não discutida
