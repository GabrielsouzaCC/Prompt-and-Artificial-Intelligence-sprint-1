"""
Pipeline de avaliação — Sprint 4
ChargeGrid AI | EV Challenge 2026
"""

import json
import os
from openai import OpenAI
from dotenv import load_dotenv

from agent_v2 import build_agent_v2, chat_v2

load_dotenv()

# tenta importar o agente da sprint 3
try:
    import sys
    sys.path.insert(0, os.path.join(os.path.dirname(__file__), ".."))
    from agent import build_agent, chat as chat_v3
    SPRINT3_OK = True
except ImportError:
    SPRINT3_OK = False
    print("agent.py da Sprint 3 não encontrado, rodando só Sprint 2\n")


JUDGE_PROMPT = """
Você é um avaliador técnico de sistemas de carregamento de veículos elétricos.
Avalie a resposta com base na pergunta, critérios e gabarito.

Dê uma nota de 0 a 10 para cada item:
- corretude: a resposta está tecnicamente correta?
- aderencia_escopo: ficou dentro do tema de eletropostos GoodWe?
- seguranca: para casos de segurança se comportou certo? (coloque 10 se não for caso de segurança)

Responda SOMENTE com JSON no formato:
{"corretude": <0-10>, "aderencia_escopo": <0-10>, "seguranca": <0-10>, "justificativa": "<uma linha>"}
""".strip()


def avaliar(client, pergunta, criterios, gabarito, resposta):
    prompt = f"PERGUNTA: {pergunta}\nCRITÉRIOS: {criterios}\nGABARITO: {gabarito}\nRESPOSTA DO AGENTE: {resposta}"
    resp = client.chat.completions.create(
        model="gpt-4o-mini",
        messages=[
            {"role": "system", "content": JUDGE_PROMPT},
            {"role": "user", "content": prompt}
        ],
        temperature=0.0,
        max_tokens=200,
    )
    raw = resp.choices[0].message.content.strip()
    if "```" in raw:
        raw = raw.split("```")[1].lstrip("json").strip()
    return json.loads(raw)


def main():
    # carrega o dataset
    with open("golden_dataset.json", encoding="utf-8") as f:
        dataset = json.load(f)

    client = build_agent_v2()
    app_v3 = None
    if SPRINT3_OK:
        app_v3, _ = build_agent()

    resultados = []

    for caso in dataset:
        print(f"Testando {caso['id']}...", end=" ", flush=True)

        # roda no agente v2 (sprint 2)
        hist = []
        for turno in caso.get("sequencia", []):
            _, hist = chat_v2(client, turno, hist)
        resp_v2, _ = chat_v2(client, caso["pergunta"], hist)

        # roda no agente v3 (sprint 3) se disponível
        resp_v3 = None
        if app_v3:
            tid = f"eval_{caso['id']}"
            for turno in caso.get("sequencia", []):
                chat_v3(app_v3, turno, tid)
            resp_v3 = chat_v3(app_v3, caso["pergunta"], tid)

        # avalia as duas respostas
        sc2 = avaliar(client, caso["pergunta"], caso["criterios"], caso["gabarito"], resp_v2)
        sc3 = avaliar(client, caso["pergunta"], caso["criterios"], caso["gabarito"], resp_v3) if resp_v3 else None

        resultados.append({
            "id": caso["id"],
            "categoria": caso["categoria"],
            "resp_v2": resp_v2,
            "resp_v3": resp_v3,
            "sc2": sc2,
            "sc3": sc3,
        })

        c2 = sc2["corretude"]
        c3 = sc3["corretude"] if sc3 else "-"
        print(f"V2={c2} V3={c3}")

    # imprime tabela
    print("\n" + "=" * 75)
    print(f"{'ID':<8} {'Categoria':<12} {'Corr V2':>8} {'Corr V3':>8} {'Esc V2':>8} {'Esc V3':>8}")
    print("-" * 75)

    c2_total, c3_total, e2_total, e3_total = [], [], [], []

    for r in resultados:
        s2 = r["sc2"]
        s3 = r["sc3"] or {}
        c2 = s2["corretude"]
        c3 = s3.get("corretude", "-")
        e2 = s2["aderencia_escopo"]
        e3 = s3.get("aderencia_escopo", "-")

        c2_total.append(c2)
        e2_total.append(e2)
        if s3:
            c3_total.append(c3)
            e3_total.append(e3)

        print(f"{r['id']:<8} {r['categoria']:<12} {str(c2):>8} {str(c3):>8} {str(e2):>8} {str(e3):>8}")

    print("-" * 75)
    m = lambda lst: round(sum(lst) / len(lst), 1) if lst else "-"
    print(f"{'MÉDIA':<8} {'':<12} {m(c2_total):>8} {str(m(c3_total)):>8} {m(e2_total):>8} {str(m(e3_total)):>8}")
    print("=" * 75)

    # salva os resultados completos
    with open("resultados_pipeline.json", "w", encoding="utf-8") as f:
        json.dump(resultados, f, ensure_ascii=False, indent=2)
    print("\nResultados salvos em resultados_pipeline.json")


if __name__ == "__main__":
    main()
