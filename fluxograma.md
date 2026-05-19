graph TD
    %% Definição de Cores
    classDef user fill:#e1f5fe,stroke:#03a9f4,stroke-width:2px;
    classDef interface fill:#fff3e0,stroke:#ff9800,stroke-width:2px;
    classDef backend fill:#e8f5e9,stroke:#4caf50,stroke-width:2px;
    classDef ai fill:#f3e5f5,stroke:#9c27b0,stroke-width:2px;

    %% Elementos
    A[👤 Usuário / Operador Comercial]:::user
    B[💻 Interface Web - Streamlit]:::interface
    C{⚙️ Backend Python / LangChain}:::backend
    D[📄 System Prompt - Contexto]:::backend
    E[🧠 API do LLM - Gemini 1.5 Flash]:::ai
    F{🛡️ Verificação de Escopo}:::backend
    G[✅ Resposta Técnica/Solução]:::interface
    H[🚫 Mensagem de Recusa - Fora do escopo]:::interface

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
