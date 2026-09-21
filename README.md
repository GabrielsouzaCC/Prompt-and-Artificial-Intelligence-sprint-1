# ChargeGrid Intelligence AI

Assistente operacional para gestão de eletropostos GoodWe
**EV Challenge 2026 | FIAP — Sprint 3**

---

## O que é

Chatbot desenvolvido para auxiliar operadores e técnicos na gestão dos eletropostos GoodWe do Hub FIAP. Responde dúvidas sobre balanceamento de carga, tarifação, protocolo OCPP e diagnóstico MODBUS.

Sprint 3: refatorado com LangGraph para ter memória de sessão automática e proteção contra prompt injection em nível de infraestrutura.

---

## Como rodar

### Pré-requisitos
- Python 3.10+
- Chave de API OpenAI

### Passos

```bash
# 1. Clone o repositório
git clone https://github.com/GabrielsouzaCC/Prompt-and-Artificial-Intelligence-sprint-1.git
cd Prompt-and-Artificial-Intelligence-sprint-1

# 2. Crie o ambiente virtual
python -m venv .venv
source .venv/bin/activate      # Linux/macOS
.venv\Scripts\activate         # Windows

# 3. Instale as dependências
pip install -r requirements.txt

# 4. Configure o .env
cp .env.example .env
# edite o .env e coloque sua OPENAI_API_KEY

# 5. Execute
python main.py
```

---

## Arquivos do projeto

```
├── agent.py              # agente LangGraph com memória e guardrail
├── main.py               # interface de terminal (CLI)
├── ChargeGrid_Sprint3.ipynb  # notebook Google Colab com todos os testes
├── relatorio_modelos.md  # comparação de configurações GPT-4o mini
├── casos_de_teste.md     # 13 testes: funcionais, memória e segurança
├── relatorio_evolucao.md # relatório Sprint 2 → Sprint 3
├── integrantes.txt       # nome, RM e turma do grupo
├── requirements.txt
├── .env.example
└── .gitignore
```

---

## Comandos do terminal

| Comando | O que faz |
|---------|-----------|
| `/limpar` | Zera a memória e começa nova sessão |
| `/modelo` | Alterna entre temperature 0.3 e 0.7 |
| `/sessao` | Mostra o ID da sessão atual |
| `/sair` | Encerra o programa |

---

## O que mudou na Sprint 3

| | Sprint 2 | Sprint 3 |
|---|---|---|
| Framework | LangChain direto | LangGraph |
| Modelo | Gemini (planejado) | GPT-4o mini (OpenAI) |
| Memória | Lista manual | MemorySaver automático |
| Guardrail | Só no system prompt | Nó dedicado no grafo |
| Sessões isoladas | Não | Sim (thread_id) |

---

## Licença

Projeto acadêmico — FIAP · EV Challenge 2026
Desenvolvido em parceria com GoodWe Brasil
