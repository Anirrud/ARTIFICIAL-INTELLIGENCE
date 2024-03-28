import math

def print_board(board):
    for row in board:
        print(" | ".join(row))
        print("-" * 5)

def check_winner(board):
    # Check rows
    for row in board:
        if row[0] == row[1] == row[2] != ' ':
            return row[0]

    # Check columns
    for col in range(3):
        if board[0][col] == board[1][col] == board[2][col] != ' ':
            return board[0][col]

    # Check diagonals
    if board[0][0] == board[1][1] == board[2][2] != ' ':
        return board[0][0]
    if board[0][2] == board[1][1] == board[2][0] != ' ':
        return board[0][2]

    return None

def is_board_full(board):
    for row in board:
        if ' ' in row:
            return False
    return True

def get_user_move():
    while True:
        try:
            row, col = map(int, input("Enter row and column (0-2, separated by space): ").split())
            if 0 <= row <= 2 and 0 <= col <= 2:
                return row, col
            else:
                print("Invalid input! Row and column should be between 0 and 2.")
        except ValueError:
            print("Invalid input! Please enter two integers.")

def evaluate(board):
    winner = check_winner(board)
    if winner == 'X':
        return 1
    elif winner == 'O':
        return -1
    else:
        return 0

def minimax(board, depth, is_maximizing):
    score = evaluate(board)

    if score == 1 or score == -1:
        return score

    if is_board_full(board):
        return 0

    if is_maximizing:
        best_score = -math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'X'
                    score = minimax(board, depth + 1, False)
                    board[row][col] = ' '
                    best_score = max(score, best_score)
        return best_score
    else:
        best_score = math.inf
        for row in range(3):
            for col in range(3):
                if board[row][col] == ' ':
                    board[row][col] = 'O'
                    score = minimax(board, depth + 1, True)
                    board[row][col] = ' '
                    best_score = min(score, best_score)
        return best_score

def find_best_move(board):
    best_score = -math.inf
    best_move = None

    for row in range(3):
        for col in range(3):
            if board[row][col] == ' ':
                board[row][col] = 'X'
                score = minimax(board, 0, False)
                board[row][col] = ' '
                if score > best_score:
                    best_score = score
                    best_move = (row, col)

    return best_move

def play_game():
    board = [[' ' for _ in range(3)] for _ in range(3)]
    print("Let's play Tic Tac Toe!")
    print_board(board)

    while True:
        # Player's move
        row, col = get_user_move()
        if board[row][col] != ' ':
            print("That position is already taken!")
            continue
        board[row][col] = 'O'
        print_board(board)
        if check_winner(board) == 'O':
            print("You win!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

        # Computer's move
        print("Computer's turn...")
        row, col = find_best_move(board)
        board[row][col] = 'X'
        print_board(board)
        if check_winner(board) == 'X':
            print("Computer wins!")
            break
        elif is_board_full(board):
            print("It's a draw!")
            break

if __name__ == "__main__":
    play_game()
