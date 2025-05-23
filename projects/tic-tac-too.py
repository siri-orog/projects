import numpy as np

# Initialize board
def create_board():
    return np.array([[" " for _ in range(3)] for _ in range(3)])

# Display board
def display_board(board):
    print("\n")
    for row in board:
        print(" | ".join(row))
        print("-" * 9)

# Check for a win
def check_winner(board, player):
    for row in board:
        if all(cell == player for cell in row):
            return True

    for col in range(3):
        if all(board[row][col] == player for row in range(3)):
            return True

    if all(board[i][i] == player for i in range(3)) or all(board[i][2-i] == player for i in range(3)):
        return True

    return False

# Check for a draw
def check_draw(board):
    return all(cell != " " for row in board for cell in row)

# Get player input
def get_move(board, player):
    while True:
        try:
            move = input(f"Player {player}, enter your move (row,col): ")
            row, col = map(int, move.split(","))
            if 0 <= row < 3 and 0 <= col < 3 and board[row][col] == " ":
                return row, col
            else:
                print("Invalid move. Try again.")
        except ValueError:
            print("Invalid input format. Please enter row and column as 'row,col'.")

# Main game loop
def play_game():
    board = create_board()
    current_player = "X"

    while True:
        display_board(board)
        row, col = get_move(board, current_player)
        board[row][col] = current_player

        if check_winner(board, current_player):
            display_board(board)
            print(f"🎉 Player {current_player} wins!")
            break

        if check_draw(board):
            display_board(board)
            print("It's a draw! 🤝")
            break

        current_player = "O" if current_player == "X" else "X"

    # Ask to play again
    replay = input("\nDo you want to play again? (yes/no): ").strip().lower()
    if replay == "yes":
        play_game()
    else:
        print("Thanks for playing! 😊")

# Start the game
play_game()