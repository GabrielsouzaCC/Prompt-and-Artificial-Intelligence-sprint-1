# ChargeGrid Intelligence AI
 
**EV Challenge 2026 | GoodWe × FIAP — Sprint 3**
 
---
 
## Sobre o projeto
 
O ChargeGrid AI nasceu de um problema real: o crescimento da frota de veículos elétricos no Brasil está criando uma demanda enorme por infraestrutura de recarga, mas os operadores dessas redes ainda enfrentam dificuldades do dia a dia sem ter onde buscar suporte técnico rápido.
 
Um gestor de hub de recarga num shopping ou universidade precisa saber como configurar uma tarifa de pico, o que fazer quando vários carros carregam ao mesmo tempo e o risco de derrubar o disjuntor, ou como diagnosticar um medidor que parou de funcionar. Essas perguntas exigem conhecimento técnico em protocolos como OCPP e MODBUS que nem sempre estão acessíveis na hora certa.
 
O ChargeGrid AI foi desenvolvido para ser esse suporte. Um assistente que entende o contexto dos eletropostos GoodWe, responde de forma técnica e direta, e ainda mantém memória do que o operador já informou durante a conversa — sem precisar repetir tudo do zero a cada mensagem.
 
---
 
## Como o projeto evoluiu
 
Na Sprint 1 definimos o problema, a persona do usuário e o fluxo do chatbot. Na Sprint 2 colocamos o chatbot para funcionar de verdade, com um modelo de linguagem e gerenciamento de histórico. A memória era feita na mão — o código montava uma lista com as mensagens e passava para o modelo a cada turno.
 
Na Sprint 3 evoluímos a arquitetura. Migramos o núcleo para o LangGraph, um framework de agentes que gerencia o fluxo da conversa como um grafo de estados. Isso trouxe três ganhos concretos:
 
- A memória passou a ser gerenciada automaticamente pelo MemorySaver, com sessões isoladas por thread_id
- Criamos um nó de guardrail separado que detecta tentativas de prompt injection antes mesmo de chamar o modelo
- O código ficou mais organizado e mais fácil de expandir no futuro
Também migramos o modelo para GPT-4o mini via API da OpenAI, que se mostrou estável, rápido e com respostas técnicas precisas para o contexto de eletropostos.
 
---
 
## O que o assistente sabe fazer
 
- Orientar sobre configuração de tarifas dinâmicas por horário (TOU)
- Auxiliar no balanceamento de carga entre múltiplos carregadores (DLB)
- Diagnosticar falhas de comunicação nos protocolos OCPP e MODBUS
- Manter contexto ao longo da conversa, lembrando informações do hub sem que o operador precise repetir
- Recusar tentativas de uso fora do escopo ou de manipulação do comportamento do assistente
---
 
## Relevância para o mercado
 
O mercado de mobilidade elétrica no Brasil está crescendo de forma acelerada. Montadoras, shoppings, universidades e empresas de frota estão instalando eletropostos, mas a mão de obra técnica especializada ainda é escassa. Um operador bem treinado em OCPP e MODBUS é difícil de encontrar e mais difícil ainda de manter de plantão 24 horas.
 
Um assistente como o ChargeGrid AI pode reduzir o tempo de resposta a incidentes, evitar erros de configuração que geram prejuízo, e diminuir a dependência de suporte técnico especializado para questões do dia a dia. Para gestores de infraestrutura, isso representa menos tempo parado e mais eficiência operacional.
 
Além disso, o projeto demonstra na prática como arquiteturas de agentes com LangGraph, memória de sessão e guardrails de segurança podem ser aplicadas em ambientes industriais reais — não apenas em demos. Esse tipo de solução tem demanda crescente em empresas de energia, logística, mobilidade e infraestrutura urbana.
 
---
 
## Como rodar
 
### Pré-requisitos
- Python 3.10+
- Chave de API OpenAI
### Passos
 
```bash
git clone https://github.com/GabrielsouzaCC/Prompt-and-Artificial-Intelligence-sprint-1.git
cd Prompt-and-Artificial-Intelligence-sprint-1
 
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows
 
pip install -r requirements.txt
 
cp .env.example .env
# adicione sua OPENAI_API_KEY no arquivo .env
 
python main.py
```
 
### Google Colab
 
Abra o arquivo `ChargeGrid_Sprint3.ipynb` no Colab, adicione a `OPENAI_API_KEY` nos Secrets do menu lateral e execute as células em ordem.
 
---
 
## Comandos do terminal
 
| Comando | O que faz |
|---------|-----------|
| `/limpar` | Zera a memória e começa nova sessão |
| `/modelo` | Alterna entre configurações de parâmetros |
| `/sessao` | Mostra o ID da sessão atual |
| `/sair` | Encerra o programa |
 
---
 
## Arquivos
 
```
├── agent.py                  # agente LangGraph: guardrail + memória + GPT-4o mini
├── main.py                   # interface de terminal
├── ChargeGrid_Sprint3.ipynb  # notebook com todos os testes
├── relatorio_modelos.md      # comparação de configurações do modelo
├── casos_de_teste.md         # 13 testes documentados
├── relatorio_evolucao.md     # evolução Sprint 2 → Sprint 3
├── integrantes.txt           # equipe do projeto
├── requirements.txt
├── .env.example
└── .gitignore
```
 
---
 
## Equipe
 
| Nome | RM | Responsabilidade |
|------|----|-----------------|
| Gabriel Souza | 571583 | Desenvolvimento do agente LangGraph e integração OpenAI |
| Rafael Sá | 569223 | Testes e comparação de modelos |
| João Melo | 571116 | Relatório de evolução e documentação |
 
**FIAP · Ciência da Computação · Turma CCPQ · 2026**
