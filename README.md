# Estudo – Motor de Decisão (Base do AlphaGo)

## Objetivo

Construir e compreender um **motor de decisão** simples (estado → avaliação → escolha) usando Tic-Tac-Toe, sem ML e sem LLM.

---

## O que foi construído

* **Agente** que joga Tic-Tac-Toe contra um humano
* **Estado**: lista de 9 posições do tabuleiro
* **Ações**: jogar em qualquer casa vazia
* **Simulação**: imaginar jogadas futuras sem alterar o estado real
* **Avaliação**: pontuar estados como bons/ruins
* **Escolha**: selecionar a melhor ação com base no score

---

## Arquitetura mental

```
Estado atual (board)
   ↓
Ações possíveis
   ↓
Simulação (future board)
   ↓
Avaliação (score)
   ↓
Escolha da melhor ação
```

---

## Conceitos-chave (em linguagem simples)

* **Estado**: fotografia do mundo agora
* **Ação**: algo que pode ser feito
* **Simular**: perguntar "e se eu fizer isso?"
* **Avaliar**: dizer se o resultado é bom ou ruim
* **Decidir**: escolher a opção menos ruim / mais boa

---

## Código – Papéis das funções

* `board`: representa o estado
* `print_board`: visualização (não é inteligência)
* `check_winner`: regras fixas
* `evaluate`: função de valor (+1 ganha, -1 perde, 0 neutro)
* `simulate`: cria futuros possíveis
* `choose_best_move`: motor de decisão (loop + avaliação)

---

## O que este motor FAZ

* Avalia **1 jogada à frente**
* Ganha quando pode
* Bloqueia quando necessário
* Segue um **loop determinístico**

## O que este motor NÃO faz

* Não aprende
* Não planeja vários passos
* Não usa probabilidade
* Não entende significado

---

## Ligação com AlphaGo (base da base)

| Nosso motor      | AlphaGo          |
| ---------------- | ---------------- |
| Estado simples   | Tabuleiro Go     |
| Avaliação manual | Rede neural      |
| Simulação rasa   | MCTS             |
| Escolha direta   | Política + busca |

Mesma ideia estrutural, outra escala.

---

## Aprendizados principais

* Decisão pode ser **matemática**, não cognitiva
* Estratégia nasce de **simular + avaliar**
* Visualização ajuda o humano, não a máquina
* A base vem antes de ML/LLM

---

## Próximos passos

* Minimax (2+ passos à frente)
* Empate perfeito (invencível)
* Aprendizado de avaliação
* Conexão conceitual com MCTS

---

## Status

✔ Motor funcional
✔ Entendimento do fluxo
✔ Pronto para evoluir
#tictactoe_decision_engine
