"""
ChargeGrid Intelligence AI — Sprint 2
EV Challenge 2026 | GoodWe x FIAP
Classe do Chatbot integrada ao Gemini via LangChain Core.
"""

from langchain_google_genai import ChatGoogleGenerativeAI
from langchain_core.messages import SystemMessage, HumanMessage, AIMessage
from typing import List, Tuple

class ChargeGridBot:
    def __init__(self, api_key: str):
        # Atualizado para gemini-2.0-flash para rodar na API estável atualizada
        self.model = ChatGoogleGenerativeAI(
            model="self.model = ChatGoogleGenerativeAI(
            model="gemini-1.5-flash", 
            google_api_key=api_key,
            temperature=0.7
        )2",
            google_api_key=api_key,
            temperature=0.7
        )
        
        # System Prompt definindo o escopo do copiloto operacional
        self.system_prompt = SystemMessage(
            content=(
                "Você é o ChargeGrid AI, um copiloto operacional especialista em gestão de eletropostos GoodWe. "
                "Seu papel é auxiliar operadores no monitoramento, balanceamento de carga (DLB), "
                "configuração de tarifação dinâmica (TOU) e diagnósticos de protocolos OCPP e MODBUS. "
                "Seja direto, técnico e profissional nas respostas."
            )
        )

    def chat(self, user_message: str, history: List[dict] = None) -> Tuple[str, List[dict]]:
        if history is None:
            history = []
            
        # 1. Reconstrói o histórico transformando dicionários em objetos do LangChain
        langchain_messages = [self.system_prompt]
        for msg in history:
            if msg["role"] == "user":
                langchain_messages.append(HumanMessage(content=msg["content"]))
            elif msg["role"] == "assistant":
                langchain_messages.append(AIMessage(content=msg["content"]))
                
        # 2. Adiciona a nova mensagem atual do usuário ao fluxo
        langchain_messages.append(HumanMessage(content=user_message))
        
        try:
            # 3. Chama a API da Google via LangChain
            response = self.model.invoke(langchain_messages)
            response_text = response.content if hasattr(response, 'content') else str(response)
            
            if not response_text.strip():
                response_text = "Desculpe, recebi uma resposta vazia do servidor. Pode tentar reformular a pergunta?"
        except Exception as e:
            response_text = f"Erro interno na geração da IA: {str(e)}"

        # 4. Atualiza a lista estruturada para o st.session_state do app.py
        updated_history = list(history)
        updated_history.append({"role": "user", "content": user_message})
        updated_history.append({"role": "assistant", "content": response_text})
        
        return response_text, updated_history
