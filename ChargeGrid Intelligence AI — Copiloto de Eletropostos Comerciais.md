# sprint-1-Prompt-and-Artificial-Intelligence-REV2

# ⚡ ChargeGrid Intelligence AI — Copiloto de Eletropostos Comerciais

##  Integrantes do Grupo
* [Gabriel Souza] - RM [571583]
* [João Melo] - RM [571116]
* [Rafael Sá] - RM [569223]

##  1. O Problema Abordado
O crescimento da frota de veículos elétricos exige hubs de recarga eficientes no setor comercial (shoppings, frotistas, estacionamentos e universidades como a FIAP). No entanto, o mercado enfrenta um grande desafio: **a ausência de mecanismos integrados e inteligentes nos eletropostos para gerenciar e orquestrar dinamicamente a potência elétrica, registrar com precisão os ciclos de cada sessão e aplicar regras automatizadas de faturamento e tarifação dinâmica.**

Atualmente, a falta de inteligência operacional gera:
* **Sobrecarga na rede elétrica:** Risco de ultrapassar a demanda contratada da instalação comercial quando múltiplos veículos carregam simultaneamente.
* **Complexidade no faturamento:** Dificuldade em aplicar tarifas variáveis (ex: cobrar mais caro em horários de pico ou para alta rotatividade).
* **Gargalos técnicos de comunicação:** Complexidade no diagnóstico de falhas de comunicação física e lógica nos ecossistemas de carregadores, que utilizam os protocolos OCPP (nuvem) e MODBUS (hardware/medidores).

##  2. Escopo do Chatbot e Persona
O **ChargeGrid Intelligence AI** foi projetado para atuar como uma ferramenta operacional de suporte em tempo real, eliminando telas complexas e fornecendo respostas imediatas para tomada de decisão.

* **Persona Atendida:** Operador Comercial / Gestor de Infraestrutura de Recarga.
* **Justificativa do Escopo:** A escolha pelo cenário comercial (ChargeGrid Intelligence) em vez do modelo condominial justifica-se por sua maior complexidade técnica. O ambiente comercial exige orquestração de carga em larga escala, balanceamento dinâmico e conformidade rigorosa com protocolos industriais, cenários onde uma Inteligência Artificial entrega maior valor agregado para mitigar prejuízos financeiros e evitar falhas críticas na infraestrutura.
* **Capacidades Principais:** 1. Orientar sobre regras de balanceamento de carga (Load Balancing) e gerenciamento de potência.
  2. Auxiliar na configuração e simulação de políticas de tarifação dinâmica comercial.
  3. Servir como guia técnico para troubleshooting e diagnóstico rápido de conexões OCPP e MODBUS no EV Charger GoodWe.

## 🛠️ 3. Tecnologias Selecionadas e Justificativa Técnica
A arquitetura do projeto foi planejada para garantir escalabilidade, baixa latência e precisão nas respostas técnicas:

1. **Modelo de IA (LLM):** `Google Gemini 1.5 Flash` (via API da Google AI Studio).
   * *Justificativa:* Apresenta uma janela de contexto massiva, excelente velocidade de processamento e baixo custo por token, sendo ideal para um assistente operacional que lidará com logs de conexão e consultas rápidas.
2. **Framework de Orquestração:** `LangChain`.
   * *Justificativa:* Essencial para implementar a arquitetura RAG (Retrieval-Augmented Generation) na Sprint 2, permitindo conectar o modelo a arquivos locais (como manuais de OCPP da GoodWe e tabelas de tarifas) sem a necessidade de re-treinar a IA. Também gerencia de forma nativa a memória de curto prazo (histórico da conversa).
3. **Interface de Usuário:** `Streamlit` (Web UI em Python).
   * *Justificativa:* Permite o desenvolvimento acelerado de um dashboard funcional e interativo em Python, facilitando a demonstração prática do fluxo de conversação para os avaliadores.
