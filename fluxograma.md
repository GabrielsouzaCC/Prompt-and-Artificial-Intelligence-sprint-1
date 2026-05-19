## 📊 Fluxograma de Funcionamento do Chatbot

```mermaid
graph TD
    %% Definição de Cores
    classDef user fill:#e1f5fe,stroke:#03a9f4,stroke-width:2px;
    classDef interface fill:#fff3e0,stroke:#ff9800,stroke-width:2px;
    classDef backend fill:#e8f5e9,stroke:#4caf50,stroke-width:2px;
    classDef ai fill:#f3e5f5,stroke:#9c27b0,stroke-width:2px;

    %% Elementos
    A[👤 Usuário /<br>Operador Comercial]:::user
    B[💻 Interface Web -<br>Streamlit]:::interface
    C{⚙️ Backend Python /<br>LangChain}:::backend
    D[📄 System Prompt -<br>Contexto]:::backend
    E[🧠 API do LLM -<br>Gemini 1.5 Flash]:::ai
    F{🛡️ Verificação<br>de Escopo}:::backend
    G[✅ Resposta Técnica /<br>Solução]:::interface
    H[🚫 Mensagem de Recusa -<br>Fora do escopo]:::interface

    %% Fluxo
    A -->|1. Digita a Dúvida| B
    B -->|2. Envia Dúvida| C
    C -.->|3. Carrega Histórico da Conversa| C
    C -->|4. Junta Pergunta + Histórico| D
    D -->|5. Envia Pacote Completo| E
    E -->|6. Processa e Gera Resposta| F
    F -->|7a. Resposta é Válida| G
    F -->|7b. Pergunta Não Tem a Ver com a GoodWe| H
    G -->|8. Exibe na Tela| B
    H -->|8. Exibe na Tela| B
