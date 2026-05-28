"""
ChargeGrid Intelligence AI — Sprint 2
EV Challenge 2026 | GoodWe x FIAP
Interface principal do chatbot via Streamlit.
"""

import os
import streamlit as st
from chatbot import ChargeGridBot

# ─── Configuração da página ───────────────────────────────────────────────────
st.set_page_config(
    page_title="ChargeGrid Intelligence AI",
    page_icon="⚡",
    layout="centered",
    initial_sidebar_state="expanded",
)

# ─── CSS personalizado ────────────────────────────────────────────────────────
st.markdown("""
<style>
    /* Fundo geral */
    .stApp { background-color: #0d1117; color: #e6edf3; }

    /* Header */
    .header-box {
        background: linear-gradient(135deg, #1a2332 0%, #0d2137 100%);
        border: 1px solid #00d4aa33;
        border-radius: 12px;
        padding: 20px 24px;
        margin-bottom: 20px;
        display: flex;
        align-items: center;
        gap: 16px;
    }
    .header-title { font-size: 1.5rem; font-weight: 700; color: #00d4aa; margin: 0; }
    .header-sub   { font-size: 0.8rem; color: #7d8590; margin: 0; }

    /* Mensagens */
    .msg-user {
        background: #1c2d40;
        border-left: 3px solid #1f6feb;
        border-radius: 8px;
        padding: 12px 16px;
        margin: 8px 0;
    }
    .msg-bot {
        background: #161b22;
        border-left: 3px solid #00d4aa;
        border-radius: 8px;
        padding: 12px 16px;
        margin: 8px 0;
    }
    .msg-label {
        font-size: 0.7rem;
        font-weight: 600;
        text-transform: uppercase;
        letter-spacing: 0.08em;
        margin-bottom: 6px;
    }
    .label-user { color: #1f6feb; }
    .label-bot  { color: #00d4aa; }

    /* Sidebar */
    .sidebar-badge {
        background: #1a2332;
        border: 1px solid #30363d;
        border-radius: 8px;
        padding: 10px 14px;
        margin-bottom: 8px;
        font-size: 0.82rem;
    }
    .badge-green { color: #3fb950; }
    .badge-blue  { color: #58a6ff; }

    /* Input area */
    .stTextInput > div > div > input {
        background: #161b22 !important;
        border: 1px solid #30363d !important;
        color: #e6edf3 !important;
        border-radius: 8px !important;
    }
    .stButton > button {
        background: linear-gradient(135deg, #00d4aa, #0096ff) !important;
        color: #0d1117 !important;
        font-weight: 700 !important;
        border: none !important;
        border-radius: 8px !important;
        width: 100% !important;
    }
    .stButton > button:hover { opacity: 0.9 !important; }

    /* Divider */
    hr { border-color: #30363d !important; }
</style>
""", unsafe_allow_html=True)

# ─── Inicialização do bot ─────────────────────────────────────────────────────
@st.cache_resource
def get_bot(api_key: str) -> ChargeGridBot:
    return ChargeGridBot(api_key=api_key)

# ─── Sidebar ──────────────────────────────────────────────────────────────────
with st.sidebar:
    st.markdown("## ⚡ ChargeGrid AI")
    st.markdown("**EV Challenge 2026** · GoodWe × FIAP")
    st.divider()

    # API Key
    api_key = st.text_input(
        "🔑 Google API Key",
        type="password",
        help="Insira sua chave da Google AI Studio. Nunca é salva nem enviada a terceiros.",
        value=st.session_state.get("api_key", os.getenv("GOOGLE_API_KEY", "")),
    )
    if api_key:
        st.session_state["api_key"] = api_key

    st.divider()
    st.markdown("**Status do Sistema**")
    st.markdown(f"""
<div class="sidebar-badge">
  <span class="badge-green">●</span> Protocolo OCPP: Online<br>
  <span class="badge-green">●</span> Protocolo MODBUS: Online<br>
  <span class="badge-blue">●</span> LLM: Gemini 1.5 Flash<br>
  <span class="badge-blue">●</span> Framework: LangChain
</div>
""", unsafe_allow_html=True)

    st.divider()
    st.markdown("**Escopo do Assistente**")
    st.markdown("""
- ⚡ Load Balancing / DLB
- 💰 Tarifação Dinâmica (TOU)
- 🔌 Troubleshooting OCPP
- 📡 Diagnóstico MODBUS
- 📊 Sessões de Recarga
""")

    st.divider()
    if st.button("🗑️ Limpar Conversa"):
        st.session_state["messages"] = []
        st.session_state["langchain_history"] = []
        st.rerun()

    st.caption("Sprint 2 — FIAP · 2026")

# ─── Header ───────────────────────────────────────────────────────────────────
st.markdown("""
<div class="header-box">
  <div>
    <p class="header-title">⚡ ChargeGrid Intelligence AI</p>
    <p class="header-sub">Copiloto operacional para gestão de eletropostos GoodWe · Hub FIAP</p>
  </div>
</div>
""", unsafe_allow_html=True)

# ─── Estado da conversa ───────────────────────────────────────────────────────
if "messages" not in st.session_state:
    st.session_state["messages"] = []
if "langchain_history" not in st.session_state:
    st.session_state["langchain_history"] = []

# ─── Área do chat ─────────────────────────────────────────────────────────────
chat_container = st.container()

with chat_container:
    if not st.session_state["messages"]:
        st.info(
            "👋 **Olá, Operador!** Sou o ChargeGrid AI. Estou pronto para auxiliar no "
            "monitoramento, configuração e diagnóstico da sua rede de eletropostos GoodWe. "
            "Como posso ajudar hoje?"
        )
    else:
        for msg in st.session_state["messages"]:
            if msg["role"] == "user":
                st.markdown(f"""
<div class="msg-user">
  <p class="msg-label label-user">👤 Operador</p>
  {msg["content"]}
</div>""", unsafe_allow_html=True)
            else:
                st.markdown(f"""
<div class="msg-bot">
  <p class="msg-label label-bot">⚡ ChargeGrid AI</p>
  {msg["content"]}
</div>""", unsafe_allow_html=True)

# ─── Input do usuário ─────────────────────────────────────────────────────────
st.divider()
with st.form(key="chat_form", clear_on_submit=True):
    user_input = st.text_input(
        "💬 Sua pergunta",
        placeholder="Ex: Como configuro tarifação de pico das 17h às 20h?",
        label_visibility="collapsed",
    )
    submitted = st.form_submit_button("Enviar ⚡")

if submitted and user_input.strip():
    if not api_key:
        st.error("⚠️ Insira sua Google API Key na barra lateral para usar o chatbot.")
        st.stop()

    # Adiciona mensagem do usuário
    st.session_state["messages"].append({"role": "user", "content": user_input})

    # Chama o bot
    with st.spinner("⚡ Processando..."):
        try:
            bot = get_bot(api_key)
            response, updated_history = bot.chat(
                user_message=user_input,
                history=st.session_state["langchain_history"],
            )
            st.session_state["langchain_history"] = updated_history
            st.session_state["messages"].append({"role": "assistant", "content": response})
        except Exception as e:
            st.error(f"Erro ao contatar a API: {e}")
    st.rerun()
