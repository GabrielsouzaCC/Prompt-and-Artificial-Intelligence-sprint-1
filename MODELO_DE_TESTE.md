##  Modelo de Teste Simplificado (Para Validação na Sprint 2)

| ID | Contexto | Pergunta do Usuário (Input) | Resposta Ideal Esperada (Output) |
| :---: | :--- | :--- | :--- |
| **01** | Tarifação | "Como cobro 25% a mais na recarga no horário de pico das 17h às 20h?" | "No menu do ChargeGrid, crie uma regra de 'Tarifa por Horário (TOU)' para os dias úteis das 17h às 20h e configure o valor do kWh com um multiplicador de 1.25. O sistema aplicará a taxa extra automaticamente ao encerrar a sessão." |
| **02** | Potência | "Tem muito carro carregando junto e vai cair o disjuntor da FIAP. O que fazer?" | "O ChargeGrid resolverá isso ativando o Smart Charging (Balanceamento Dinâmico). Ele reduz a potência enviada aos carros automaticamente para respeitar o limite elétrico do prédio sem derrubar o disjuntor." |
| **03** | Hardware | "O medidor parou de marcar o consumo de energia. O que eu mudo no MODBUS?" | "Verifique se os fios A e B do cabo RS485 não estão invertidos, se o resistor de 120 ohms está no fim da linha e confirme se o Baud Rate está configurado em 9600 no carregador e no medidor." |
| **04** | Software | "O cliente já tirou o carro, mas o app continua cobrando ele. O que houve?" | "Verifique nos logs se o carregador enviou o comando `StopTransaction` via OCPP. Se houve queda de internet nessa hora, o sistema não entende que a recarga acabou e continua cobrando." |
| **05** | Escopo | "Me indica um restaurante bom perto da FIAP para eu almoçar?" | "Como assistente do ChargeGrid GoodWe, meu foco é exclusivo no gerenciamento de eletropostos e protocolos de recarga. Não consigo ajudar com indicações de restaurantes ou turismo." |
