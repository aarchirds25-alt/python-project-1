# Tic Tac Toe Game

# Create the board
board = [" "] * 9


# Display the board
def display_board():
    print()
    print(" " + board[0] + " | " + board[1] + " | " + board[2])
    print("---|---|---")
    print(" " + board[3] + " | " + board[4] + " | " + board[5])
    print("---|---|---")
    print(" " + board[6] + " | " + board[7] + " | " + board[8])
    print()


# Take player's move
def get_move(player):
    while True:
        try:
            move = int(input("Player " + player + ", enter position (1-9): "))
            return move
        except ValueError:
            print("Please enter a number.")


# Check whether the move is valid
def validate_move(move):
    if move < 1 or move > 9:
        return False

    if board[move - 1] != " ":
        return False

    return True


# Check for winner
def check_winner(player):
    winning_positions = [
        [0, 1, 2],  # Row 1
        [3, 4, 5],  # Row 2
        [6, 7, 8],  # Row 3
        [0, 3, 6],  # Column 1
        [1, 4, 7],  # Column 2
        [2, 5, 8],  # Column 3
        [0, 4, 8],  # Diagonal
        [2, 4, 6]   # Diagonal
    ]

    for position in winning_positions:
        if (board[position[0]] == player and
            board[position[1]] == player and
            board[position[2]] == player):
            return True

    return False


# Check for draw
def check_draw():
    return " " not in board


# Change player
def switch_player(player):
    if player == "X":
        return "O"
    else:
        return "X"


# Reset the game
def reset_game():
    global board
    board = [" "] * 9


# Main game function
def play_game():

    global board

    while True:

        reset_game()
        player = "X"

        print("\n===== TIC TAC TOE =====")
        print("Positions are:")
        print(" 1 | 2 | 3 ")
        print("---|---|---")
        print(" 4 | 5 | 6 ")
        print("---|---|---")
        print(" 7 | 8 | 9 ")

        while True:

            display_board()

            # Get player's move
            move = get_move(player)

            # Validate move
            if not validate_move(move):
                print("Invalid move! Try again.")
                continue

            # Put player's symbol on board
            board[move - 1] = player

            # Check winner
            if check_winner(player):
                display_board()
                print("Player " + player + " wins!")
                break

            # Check draw
            if check_draw():
                display_board()
                print("Game Draw!")
                break

            # Change player
            player = switch_player(player)

        # Ask for new game
        again = input("Do you want to play again? (yes/no): ")

        if again.lower() != "yes":
            print("Thank you for playing!")
            break


# Start the game
play_game()