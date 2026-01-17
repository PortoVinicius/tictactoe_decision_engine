# Estudo – Motor de Decisão Evoluído (Base Conceitual do AlphaGo)

## Objetivo do Estudo

Evoluir um **motor de decisão clássico (estado → simulação → avaliação → escolha)** para um modelo **heurístico com ajuste de pesos**, introduzindo **aprendizado simples** sem uso de Machine Learning tradicional ou LLMs.

O projeto usa **Tic-Tac-Toe** como ambiente controlado para estudar conceitos fundamentais de IA clássica.

---

## Visão Geral

### Versão Inicial

* Avaliação **binária**: ganhar (+1), perder (-1), neutro (0)
* Olha apenas **1 jogada à frente**
* Nenhum aprendizado
* Comportamento totalmente determinístico

### Versão Evoluída (atual)

* Avaliação **heurística ponderada**
* Reconhecimento de padrões intermediários (quase vitória / quase derrota)
* Valorização posicional (controle do centro)
* **Ajuste dinâmico de pesos** com base no resultado das partidas
* Introdução de um **ciclo de aprendizado rudimentar**

---

## Arquitetura Mental (Atualizada)

```
Estado atual (board)
   ↓
Ações possíveis
   ↓
Simulação (1 passo à frente)
   ↓
Avaliação heurística (score contínuo)
   ↓
Escolha da melhor ação
   ↓
Registro do histórico
   ↓
Ajuste de pesos (aprendizado)
```

---

## Conceitos-Chave Introduzidos

### 1. Avaliação Heurística

Em vez de apenas vitória/derrota, o estado do jogo recebe um **score contínuo** baseado em padrões:

* Duas peças da máquina + espaço livre
* Duas peças do jogador + espaço livre
* Controle do centro do tabuleiro

Isso permite decisões **mais estratégicas**, mesmo sem ver o fim do jogo.

---

### 2. Pesos (WEIGHTS)

Os pesos representam a **importância relativa** de cada padrão:

```python
WEIGHTS = {
    "two_O": 10,
    "two_X": -10,
    "center_O": 3,
    "center_X": -3
}
```

Eles funcionam como uma **função de valor parametrizada**.

---

### 3. Histórico de Estados

Durante o jogo, o motor armazena os estados avaliados:

```python
history = []
```

Esse histórico é usado **após o jogo** para ajustar os pesos.

---

### 4. Aprendizado Simples (Weight Update)

Após o término da partida, os pesos são ajustados com base no resultado:

* Vitória → reforça padrões bons
* Derrota → penaliza padrões ruins
* Empate → ajuste neutro

```python
WEIGHTS[feature] += LEARNING_RATE * result
```

Isso é conceitualmente similar a:

* Reforço
* Funções de valor
* Gradiente extremamente simplificado

---

## Papéis das Funções (Atualizado)

| Função             | Papel                                |
| ------------------ | ------------------------------------ |
| `evaluate`         | Calcula score heurístico do estado   |
| `simulate`         | Gera estado futuro hipotético        |
| `choose_best_move` | Loop de decisão baseado em score     |
| `history`          | Memória de curto prazo               |
| `learn`            | Ajuste de pesos baseado em resultado |
| `WEIGHTS`          | Conhecimento aprendido               |

---

## O Que Este Motor FAZ Agora

* Avalia padrões intermediários
* Prioriza posições estratégicas
* Ajusta comportamento ao longo do tempo
* Continua simples, explicável e rastreável

---

## O Que Este Motor AINDA NÃO FAZ

* Não planeja múltiplos passos (sem Minimax)
* Não usa probabilidade
* Não generaliza estados
* Não possui exploração vs exploração

---

## Conexão Conceitual com AlphaGo

| Este Projeto        | AlphaGo              |
| ------------------- | -------------------- |
| Heurísticas manuais | Redes neurais        |
| Pesos ajustáveis    | Treinamento profundo |
| Histórico simples   | Replay buffer        |
| 1 passo             | MCTS profundo        |

> A **estrutura mental é a mesma** — muda apenas a escala e o poder computacional.

---

## Aprendizados Principais

* Inteligência pode surgir de **avaliação + ajuste**, não de cognição
* Pesos = conhecimento codificado
* Aprendizado não precisa ser complexo para ser real
* Entender isso antes de ML/LLM é fundamental

---

## Próximos Passos Naturais

* Minimax (2+ profundidades)
* Normalização de pesos
* Exploração aleatória controlada
* Separação treino vs jogo
* Transição conceitual para MCTS

---

## Status Atual

✔ Motor heurístico funcional
✔ Aprendizado simples implementado
✔ Base sólida para IA clássica
✔ Excelente material de estudo

#tictactoe #decision_engine #heuristics #learning #ai_basics
