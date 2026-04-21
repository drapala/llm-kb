# Large Language Models Are Neurosymbolic Reasoners

**Autores:** Meng Fang, Shilong Deng, Yudi Zhang, Zijing Shi, Ling Chen, Mykola Pechenizkiy, Jun Wang  
**Publicação:** AAAI 2024  
**arXiv ID:** 2401.09334  
**Ano:** 2024 (submissão: 17 jan 2024)  
**URL:** https://arxiv.org/abs/2401.09334  
**Tipo:** paper / primary

---

## Tese central

LLMs possuem capacidade inerente para raciocínio simbólico — não apenas raciocínio semântico. O argumento central: LLMs já fazem raciocínio neurossimbólico *implicitamente*, sem que isso seja o design explícito. O paper demonstra isso via texto-based games como benchmark.

## Método

- Agente LLM recebe: observações, ações válidas do ambiente de texto, e um módulo simbólico específico
- O agente seleciona ações para interagir com ambientes de texto
- Benchmarks: raciocínio matemático, navegação, sorting, common-sense reasoning

## Resultado

- ~88% de performance média em tarefas de raciocínio simbólico via text-based games
- Melhoria substancial vs. LLMs sem o módulo simbólico

## Argumento Conceitual

LLMs processam linguagem natural que frequentemente codifica raciocínio simbólico — lógica, regras, inferências. Durante o pre-training, o modelo aprende esses padrões implicitamente. O "módulo simbólico" do paper externaliza e estrutura o que o LLM faz de forma latente.

**Implicação:** sistemas que combinam LLM + regras simbólicas explícitas não estão adicionando capacidade externa ao LLM — estão tornando explícito um modo de raciocínio que o LLM já usa implicitamente.

## Limitações

- Texto-based games são ambientes artificiais — generalização para sistemas de produção não está demonstrada
- "88% de performance" depende da qualidade e especificidade do módulo simbólico fornecido
- Causalidade não estabelecida: correlação entre LLM + simbólico e performance não prova que o LLM usa o módulo simbolicamente
