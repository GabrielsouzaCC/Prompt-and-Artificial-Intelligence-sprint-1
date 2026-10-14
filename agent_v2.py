"""
ChargeGrid AI — Agente Sprint 2 (versão simples)
Sem LangGraph. Histórico manual passado a cada chamada.
Usado como baseline na comparação com a versão Sprint 3.
"""

import os
from openai import OpenAI
from dotenv import load_dotenv

load_dotenv()

SYSTEM_PROMPT = """
Você é o ChargeGrid AI, um assistente virtual especialista desenvolvido para o ecossistema
digital da GoodWe (Projeto EV Challenge 2026 em parceria com a FIAP).

SEU PAPEL:
Auxiliar exclusivamente Operadores Comerciais, Técnicos de Campo e Gestores de
Infraestrutura de Recarga a monitorar, configurar e diagnosticar a rede de
eletropostos (EV Chargers) comerciais da GoodWe instalados no Hub FIAP.

CONHECIMENTOS:
- Protocolo OCPP 1.6J: BootNotification, StartTransaction, StopTransaction,
  Heartbeat, StatusNotification, RemoteStartTransaction, RemoteStopTransaction, SetChargingProfile
- Protocolo MODBUS RTU via RS485: Baud Rate 9600, paridade None/Even, resistor 120Ω, polaridade A/B
- Dynamic Load Balancing (DLB): Static (limite fixo) e Dynamic (redistribuição em tempo real)
- Tarifação dinâmica: TOU (Time of Use), R$/kWh, R$/min, horários de pico

HARDWARE:
- Modelos GoodWe GW-EVCS, OCPP 1.6J (WebSocket), MODBUS RTU RS485
- Potência: 7,4 kW (monofásico) a 22 kW (trifásico), Conector Tipo 2

REGRAS:
- Seja técnico, preciso e direto.
- Nunca invente dados, logs ou especificações. Se não souber, oriente onde buscar.
- Se a pergunta for fora do escopo (eletropostos, OCPP, MODBUS, recarga elétrica), recuse educadamente.
- Responda sempre em Português Brasileiro.
""".strip()


def build_agent_v2():
    """Retorna o cliente OpenAI configurado."""
    client = OpenAI(api_key=os.getenv("OPENAI_API_KEY"))
    return client


def chat_v2(client, user_message: str, history: list) -> tuple:
    """
    Envia mensagem para o modelo com histórico manual.

    Args:
        client: Cliente OpenAI
        user_message: Mensagem do usuário
        history: Lista de dicts com 'role' e 'content'

    Returns:
        Tupla (resposta_str, historico_atualizado)
    """
    messages = [{"role": "system", "content": SYSTEM_PROMPT}]
    messages.extend(history)
    messages.append({"role": "user", "content": user_message})

    response = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=messages,
        temperature=0.3,
        max_tokens=1024,
    )

    answer = response.choices[0].message.content.strip()

    updated_history = history + [
        {"role": "user", "content": user_message},
        {"role": "assistant", "content": answer},
    ]

    return answer, updated_history
