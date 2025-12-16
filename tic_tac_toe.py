import random

def print_board(board):
    print()
    print(f"{board[0]} | {board[1]} | {board[2]}")
    print("--+---+--")
    print(f"{board[3]} | {board[4]} | {board[5]}")
    print("--+---+--")
    print(f"{board[6]} | {board[7]} | {board[8]}")
    print()

def check_winner(board, player):
    win_positions = [
        (0,1,2), (3,4,5), (6,7,8),
        (0,3,6), (1,4,7), (2,5,8),
        (0,4,8), (2,4,6)
    ]
    for a, b, c in win_positions:
        if board[a] == board[b] == board[c] == player:
            return True
    return False

def board_full(board):
    return " " not in board

def player_move(board):
    while True:
        move = int(input("Enter your move (1-9): ")) - 1
        if 0 <= move < 9 and board[move] == " ":
            board[move] = "X"
            break
        else:
            print("Invalid move, try again.")

def computer_move(board):
    # Try to win
    for i in range(9):
        if board[i] == " ":
            board[i] = "O"
            if check_winner(board, "O"):
                return
            board[i] = " "

    # Try to block player
    for i in range(9):
        if board[i] == " ":
            board[i] = "X"
            if check_winner(board, "X"):
                board[i] = "O"
                return
            board[i] = " "

    # Else random
    available = [i for i in range(9) if board[i] == " "]
    board[random.choice(available)] = "O"

print("🎮 TIC TAC TOE 🎮")

while True:
    board = [" " for _ in range(9)]
    print("You are X | Computer is O")

    while True:
        print_board(board)
        player_move(board)

        if check_winner(board, "X"):
            print_board(board)
            print("🎉 You win!")
            break

        if board_full(board):
            print_board(board)
            print("🤝 It's a draw!")
            break

        computer_move(board)

        if check_winner(board, "O"):
            print_board(board)
            print("😢 Computer wins!")
            break

    again = input("\nPlay again? (yes/no): ").lower()
    if again != "yes":
        print("Thanks for playing 👋")
        break
