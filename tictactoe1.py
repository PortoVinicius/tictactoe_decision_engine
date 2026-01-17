# Tic-Tac-Toe: Humano vs Motor de Decisão

WIN_COMBOS = [
    (0,1,2),(3,4,5),(6,7,8),
    (0,3,6),(1,4,7),(2,5,8),
    (0,4,8),(2,4,6)
]

def print_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(board, player):
    for a,b,c in WIN_COMBOS:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

# Avaliação por padrões (manual) ==> Criar uma avaliação um pouco mais inteligente
def evaluate(board):
    score = 0

    # Vitória / derrota ainda têm peso máximo
    if check_winner(board, "O"):
        return 100
    if check_winner(board, "X"):
        return -100

    # Avaliar linhas
    for a, b, c in WIN_COMBOS:
        line = [board[a], board[b], board[c]]

        if line.count("O") == 2 and line.count(" ") == 1:
            score += 10   # quase ganhando
        if line.count("X") == 2 and line.count(" ") == 1:
            score -= 10   # quase perdendo

    # Centro é valioso
    if board[4] == "O":
        score += 20   # quase ganhando
    if board[4] == "X":
        score -= 5    # quase perdendo


    return score


def simulate(board, move, player):
    new_board = board.copy()
    new_board[move] = player
    return new_board

def choose_best_move(board):
    best_score = -999
    best_move = None

    for i in range(9):
        if board[i] == " ":
            future = simulate(board, i, "O")
            score = evaluate(future)

            if score > best_score:
                best_score = score
                best_move = i
                print("Testando jogada:", i, "Score:", score)

    return best_move

def player_move(board):
    move = int(input("Escolha uma posição (0-8): "))
    if board[move] == " ":
        board[move] = "X"
    else:
        print("Posição inválida")
        player_move(board)

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

game()
