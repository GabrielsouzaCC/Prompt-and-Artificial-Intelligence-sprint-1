"""
ChargeGrid Intelligence AI — Sprint 3
Versão CLI (terminal).

Comandos:
    /limpar  → nova sessão (zera a memória)
    /modelo  → troca entre configurações do modelo
    /sessao  → mostra o ID da sessão atual
    /sair    → encerra
"""

import os
import uuid
from dotenv import load_dotenv
from agent import build_agent, chat as agent_chat

load_dotenv()

VERDE   = "\033[92m"
CIANO   = "\033[96m"
CINZA   = "\033[90m"
AMARELO = "\033[93m"
RESET   = "\033[0m"
BOLD    = "\033[1m"

# gpt-4o não disponível na chave do projeto — comparação por temperature
MODELOS = [
    ("GPT-4o mini | temperature 0.3 — padrão",      ("gpt-4o-mini", 0.3)),
    ("GPT-4o mini | temperature 0.7 — experimental", ("gpt-4o-mini", 0.7)),
]


def trocar_modelo(atual_nome, atual_temp):
    print(f"\n{AMARELO}Configurações disponíveis:{RESET}")
    for i, (label, (nome, temp)) in enumerate(MODELOS):
        marca = "→" if (nome == atual_nome and temp == atual_temp) else " "
        print(f"  {marca} [{i+1}] {label}")
    escolha = input(f"Escolha [1-{len(MODELOS)}] (Enter = manter): ").strip()
    if escolha.isdigit() and 1 <= int(escolha) <= len(MODELOS):
        return MODELOS[int(escolha) - 1][1]
    return (atual_nome, atual_temp)


def main():
    api_key = os.getenv("OPENAI_API_KEY", "")
    if not api_key:
        print("OPENAI_API_KEY não encontrada. Adicione ao arquivo .env.")
        return

    print(f"\n{CIANO}{BOLD}ChargeGrid Intelligence AI — Sprint 3{RESET}")
    print(f"{CINZA}Comandos: /limpar  /modelo  /sessao  /sair{RESET}\n")

    modelo_nome = "gpt-4o-mini"
    modelo_temp = 0.3
    thread_id   = str(uuid.uuid4())

    try:
        app, _ = build_agent(model_name=modelo_nome, temperature=modelo_temp)
    except Exception as e:
        print(f"Erro ao iniciar: {e}")
        return

    print(f"{CINZA}Modelo: {modelo_nome} | temp: {modelo_temp} | Sessão: {thread_id[:8]}...{RESET}")
    print(f"{CIANO}ChargeGrid AI:{RESET} Olá! Pronto para auxiliar na gestão dos eletropostos GoodWe.\n")

    while True:
        try:
            entrada = input(f"{VERDE}Você:{RESET} ").strip()
        except (KeyboardInterrupt, EOFError):
            print(f"\n{CINZA}Encerrando.{RESET}")
            break

        if not entrada:
            continue

        if entrada.lower() == "/sair":
            print(f"{CINZA}Até mais!{RESET}")
            break

        elif entrada.lower() == "/limpar":
            thread_id = str(uuid.uuid4())
            app, _ = build_agent(model_name=modelo_nome, temperature=modelo_temp)
            print(f"{AMARELO}Nova sessão iniciada. Memória zerada.{RESET}\n")

        elif entrada.lower() == "/modelo":
            novo_nome, novo_temp = trocar_modelo(modelo_nome, modelo_temp)
            if (novo_nome, novo_temp) != (modelo_nome, modelo_temp):
                modelo_nome, modelo_temp = novo_nome, novo_temp
                thread_id = str(uuid.uuid4())
                app, _ = build_agent(model_name=modelo_nome, temperature=modelo_temp)
                print(f"{VERDE}Configuração: {modelo_nome} | temp: {modelo_temp}{RESET}\n")

        elif entrada.lower() == "/sessao":
            print(f"{CINZA}Modelo: {modelo_nome} | temp: {modelo_temp} | Sessão: {thread_id}{RESET}\n")

        else:
            print(f"{CINZA}...{RESET}", end="\r")
            try:
                resposta = agent_chat(app=app, user_message=entrada, thread_id=thread_id)
                print(" " * 20, end="\r")
                print(f"{CIANO}ChargeGrid AI:{RESET} {resposta}\n")
            except Exception as e:
                print(f"Erro: {e}\n")


if __name__ == "__main__":
    main()
