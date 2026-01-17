# ===============================
# Tic-Tac-Toe: Humano vs Motor de Decisão
# ===============================

# Histórico para aprendizado
history = []

# Pesos da avaliação
WEIGHTS = {
    "two_O": 10,
    "two_X": -10,
    "center_O": 3,
    "center_X": -3
}

LEARNING_RATE = 0.1

# Combinações vencedoras
WIN_COMBOS = [
    (0, 1, 2), (3, 4, 5), (6, 7, 8),
    (0, 3, 6), (1, 4, 7), (2, 5, 8),
    (0, 4, 8), (2, 4, 6)
]

# ===============================
# Funções utilitárias
# ===============================

def print_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(board, player):
    for a, b, c in WIN_COMBOS:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

# ===============================
# Avaliação do tabuleiro
# ===============================

def evaluate(board):
    score = 0

    if check_winner(board, "O"):
        return 100
    if check_winner(board, "X"):
        return -100

    for a, b, c in WIN_COMBOS:
        line = [board[a], board[b], board[c]]

        if line.count("O") == 2 and line.count(" ") == 1:
            score += WEIGHTS["two_O"]

        if line.count("X") == 2 and line.count(" ") == 1:
            score += WEIGHTS["two_X"]

    if board[4] == "O":
        score += WEIGHTS["center_O"]

    if board[4] == "X":
        score += WEIGHTS["center_X"]

    return score

# ===============================
# Simulação e decisão da máquina
# ===============================

def simulate(board, move, player):
    new_board = board.copy()
    new_board[move] = player
    return new_board

def choose_best_move(board):
    best_score = -999
    best_move = None

    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            score = minimax(board, depth=3, is_maximizing=False)
            board[i] = " "
            if score > best_score:
                best_score = score
                best_move = i

    return best_move

# ===============================
# Jogada do jogador
# ===============================

def player_move(board):
    move = int(input("Escolha uma posição (0-8): "))
    if board[move] == " ":
        board[move] = "X"
    else:
        print("Posição inválida")
        player_move(board)

# ===============================
# Aprendizado
# ===============================

def learn(result):
    # result = 1 (vitória), -1 (derrota), 0 (empate)
    for board in history:
        for a, b, c in WIN_COMBOS:
            line = [board[a], board[b], board[c]]

            if line.count("O") == 2 and line.count(" ") == 1:
                WEIGHTS["two_O"] += LEARNING_RATE * result

            if line.count("X") == 2 and line.count(" ") == 1:
                WEIGHTS["two_X"] -= LEARNING_RATE * result

        if board[4] == "O":
            WEIGHTS["center_O"] += LEARNING_RATE * result

        if board[4] == "X":
            WEIGHTS["center_X"] -= LEARNING_RATE * result

# ===============================
# Loop principal do jogo
# ===============================

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    # estados finais ou profundidade limite
    if abs(score) == 100 or depth == 0 or " " not in board:
        return score

    if is_maximizing:
        best = -999
        for i in range(9):
            if board[i] == " ":
                board[i] = "O"
                value = minimax(board, depth - 1, False)
                board[i] = " "
                best = max(best, value)
        return best
    else:
        best = 999
        for i in range(9):
            if board[i] == " ":
                board[i] = "X"
                value = minimax(board, depth - 1, True)
                board[i] = " "
                best = min(best, value)
        return best


def game():
    board = [" "] * 9

    while True:
        print_board(board)
        player_move(board)

        if check_winner(board, "X"):
            print_board(board)
            print("Você venceu!")
            break

        if " " not in board:
            print("Empate!")
            break

        move = choose_best_move(board)
        board[move] = "O"

        if check_winner(board, "O"):
            print_board(board)
            print("A máquina venceu!")
            break

    learn(1)
    learn(-1)
    learn(0)

    history.clear()
    print(WEIGHTS)

# ===============================
# Início do jogo
# ===============================

game()
