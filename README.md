# ChargeGrid Intelligence AI
 
**EV Challenge 2026 | GoodWe × FIAP**
 
---
 
## Sobre o projeto
 
O ChargeGrid AI é um assistente técnico para operadores de eletropostos GoodWe. A ideia surgiu de um problema real: quem gerencia um hub de recarga em um shopping ou universidade precisa saber configurar tarifas de pico, evitar sobrecarga na rede elétrica e diagnosticar falhas nos medidores — tudo isso com conhecimento de protocolos como OCPP e MODBUS que nem sempre estão acessíveis na hora certa.
 
O assistente responde perguntas técnicas, mantém o contexto da conversa e recusa tentativas de uso fora do escopo.
 
---
 
## Como o projeto evoluiu
 
**Sprint 1** — definimos o problema, a persona do usuário, o fluxograma e o system prompt inicial, com 5 casos de teste.
 
**Sprint 2** — chatbot funcionando com chamada direta à API OpenAI e histórico de conversa em lista Python, passado manualmente a cada turno.
 
**Sprint 3** — refatoramos o núcleo para LangGraph. A memória passou a ser gerenciada automaticamente pelo MemorySaver por thread_id, e adicionamos um nó de guardrail que bloqueia tentativas de prompt injection antes de chamar o modelo.
 
**Sprint 4** — construímos um pipeline de avaliação automatizada. Criamos um golden dataset com 15 casos e usamos o GPT-4o-mini como juiz (LLM-as-a-judge) para comparar as versões Sprint 2 e Sprint 3 com métricas reprodutíveis.
 
---
 
## Arquivos
 
```
├── agent.py                   # agente Sprint 3 — LangGraph + guardrail + memória
├── agent_v2.py                # agente Sprint 2 — chamada direta, histórico manual
├── main.py                    # interface de terminal
├── evaluator.py               # avaliador LLM-as-a-judge
├── pipeline.py                # pipeline de avaliação automatizada
├── golden_dataset.json        # 15 casos com gabarito
├── ChargeGrid_Sprint3.ipynb   # notebook Sprint 3
├── ChargeGrid_Sprint4.ipynb   # notebook Sprint 4
├── requirements.txt
├── .env.example
└── .gitignore
```
 
---
 
## Equipe
 
| Nome | RM | Responsabilidade |
|------|----|-----------------|
| Gabriel Souza | 571583 | Agente LangGraph, pipeline de avaliação, integração OpenAI |
| Rafael Sá | 569223 | Testes, golden dataset, comparação de modelos |
| João Melo | 571116 | Relatórios, documentação, entregáveis |
 
**FIAP · Ciência da Computação · Turma CCPQ · 2026**
 
---
 
## Como rodar
 
### Pré-requisitos
- Python 3.10+
- Chave de API OpenAI
### Configuração
 
```bash
git clone https://github.com/GabrielsouzaCC/Prompt-and-Artificial-Intelligence-sprint-1.git
cd Prompt-and-Artificial-Intelligence-sprint-1
 
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows
 
pip install -r requirements.txt
 
cp .env.example .env
# adicione sua OPENAI_API_KEY no arquivo .env
```
 
### Rodar o chatbot
 
```bash
python main.py
```
 
### Rodar o pipeline de avaliação
 
```bash
python pipeline.py
```
 
### Google Colab
 
Abra `ChargeGrid_Sprint3.ipynb` ou `ChargeGrid_Sprint4.ipynb` no Colab, adicione a `OPENAI_API_KEY` nos Secrets do menu lateral e execute as células em ordem.
 
### Comandos do terminal
 
| Comando | O que faz |
|---------|-----------|
| `/limpar` | Zera a memória e começa nova sessão |
| `/modelo` | Alterna entre temperature 0.3 e 0.7 |
| `/sessao` | Mostra o ID da sessão atual |
| `/sair` | Encerra o programa |
