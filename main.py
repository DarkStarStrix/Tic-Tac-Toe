# create a tic-tac-toe game in command line

# import modules
import random
import os


# clear the screen
def clear():
    os.system('cls' if os.name == 'nt' else 'clear')


# print the board
def print_board(board):
    clear()
    print("  {} | {} | {}".format(board[0], board[1], board[2]))
    print("-------------")
    print("  {} | {} | {}".format(board[3], board[4], board[5]))
    print("-------------")
    print("  {} | {} | {}".format(board[6], board[7], board[8]))


# check if the player has won
def check_win(board, player):
    if (board[0] == player and board[1] == player and board[2] == player) or \
            (board[3] == player and board[4] == player and board[5] == player) or \
            (board[6] == player and board[7] == player and board[8] == player) or \
            (board[0] == player and board[3] == player and board[6] == player) or \
            (board[1] == player and board[4] == player and board[7] == player) or \
            (board[2] == player and board[5] == player and board[8] == player) or \
            (board[0] == player and board[4] == player and board[8] == player) or \
            (board[2] == player and board[4] == player and board[6] == player):
        return True
    else:
        return False


# check if the board is full
def check_full(board):
    if " " in board:
        return False
    else:
        return True


# check if the player can move to the position
def check_move(board, position):
    if board[position] == " ":
        return True
    else:
        return False


# get the player's move
def get_move(board):
    while True:
        move = int(input("Enter your move (1-9): "))
        if move < 1 or move > 9:
            print("Invalid move. Try again.")
        elif check_move(board, move - 1):
            return move - 1
        else:
            print("Invalid move. Try again.")


# get the computer's move
def get_computer_move(board):
    while True:
        move = random.randint(0, 8)
        if check_move(board, move):
            return move


# main function
def main():
    # initialize the board
    board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]

    # initialize the player
    player = "X"

    # initialize the game
    game_over = False

    # initialize the winner
    winner = None

    # initialize the turn
    turn = "player"

    # initialize the game
    while not game_over:
        # print the board
        print_board(board)

        # get the move
        if turn == "player":
            move = get_move(board)
        else:
            move = get_computer_move(board)

        # make the move
        board[move] = player

        # check if the player has won
        if check_win(board, player):
            game_over = True
            winner = player
        # check if the board is full
        elif check_full(board):
            game_over = True
            winner = "tie"
        # switch the turn
        else:
            if turn == "player":
                turn = "computer"
            else:
                turn = "player"

    # print the board
    print_board(board)

    # print the winner
    if winner == "tie":
        print("It's a tie!")
    else:
        print("{} won!".format(winner))


# run the main function
if __name__ == "__main__":
    main()1


# end of program

# explanation of the game code
# 1. initialize the board
# 2. initialize the player
# 3. initialize the game
# 4. initialize the winner
# 5. initialize the turn
# 6. initialize the game
# 7. print the board
# 8. get the move
# 9. make the move
# 10. check if the player has won
# 11. check if the board is full
# 12. switch the turn
# 13. print the board
# 14. print the winner
# 15. end of program



