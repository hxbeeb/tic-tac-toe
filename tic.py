
board = [' ' for _ in range(9)]

# Function to print the board
def print_board(board):
    for row in [board[i*3:(i+1)*3] for i in range(3)]:
        print('| ' + ' | '.join(row) + ' |')


winning_combinations = [
    [0, 1, 2], [3, 4, 5], [6, 7, 8],  # Rows
    [0, 3, 6], [1, 4, 7], [2, 5, 8],  # Columns
    [0, 4, 8], [2, 4, 6]              # Diagonals
]


def check_win(board, player):
    for combo in winning_combinations:
        if all(board[i] == player for i in combo):
            return True
    return False

# Function to check for a draw
def check_draw(board):
    return ' ' not in board

# Minimax algorithm with alpha-beta pruning
def minimax(board, depth, is_maximizing, alpha, beta):
    if check_win(board, 'O'):
        return 1
    if check_win(board, 'X'):
        return -1
    if check_draw(board):
        return 0

    if is_maximizing:
        max_eval = -float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'O'
                eval = minimax(board, depth + 1, False, alpha, beta)
                board[i] = ' '
                max_eval = max(max_eval, eval)
                alpha = max(alpha, eval)
                if beta <= alpha:
                    break
        return max_eval
    else:
        min_eval = float('inf')
        for i in range(9):
            if board[i] == ' ':
                board[i] = 'X'
                eval = minimax(board, depth + 1, True, alpha, beta)
                board[i] = ' '
                min_eval = min(min_eval, eval)
                beta = min(beta, eval)
                if beta <= alpha:
                    break
        return min_eval


def best_move(board):
    best_val = -float('inf')
    move = -1
    for i in range(9):
        if board[i] == ' ':
            board[i] = 'O'
            move_val = minimax(board, 0, False, -float('inf'), float('inf'))
            board[i] = ' '
            if move_val > best_val:
                best_val = move_val
                move = i
    return move

def play_game():
    print("Welcome to Tic-Tac-Toe!")
    print_board(board)
    while True:
        # Human move
        human_move = int(input("Enter your move (1-9): ")) - 1
        if board[human_move] == ' ':
            board[human_move] = 'X'
            print_board(board)
        else:
            print("Invalid move. Try again.")
            continue

        if check_win(board, 'X'):
            print("You win!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

        ai_move = best_move(board)
        board[ai_move] = 'O'
        print("AI move:")
        print_board(board)

        if check_win(board, 'O'):
            print("AI wins!")
            break
        if check_draw(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
