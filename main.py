# To clear screen
import os
# To give the bot a choice
import random

# Adds the board and starting values
board = [" ", " ", " ", " ", " ", " ", " ", " ", " "]
game_running = True
turn = "X"


# Makes the board itself
def game_board():
    print("-" * 25)
    print(" ")
    print(" " + board[0] + " || " + board[1] + " || " + board[2])
    print(" ============")
    print(" " + board[3] + " || " + board[4] + " || " + board[5])
    print(" ============")
    print(" " + board[6] + " || " + board[7] + " || " + board[8])


def computer():
    global turn
    computer_turn = True
    while computer_turn:
        number = random.randrange(0, 8)
        if board[number] == " ":
            board[number] = "O"
            turn = "X"
            computer_turn = False
            game_board()
            check_win()
            check_draw()


# Swaps players turns
def change(i):
    global turn
    if board[i] == " ":
        board[i] = turn
        if turn == "X":
            turn = "O"
            check_win()
            check_draw()
            computer()
        else:
            turn = "X"
    else:
        print("Invalid choice. Try again")


# Checks to see if there is a win
def check_win():
    global game_running
    if board[0] == "X" and board[1] == "X" and board[2] == "X":
        print("X WINS!")
        game_running = False
    elif board[0] == "O" and board[1] == "O" and board[2] == "O":
        print("O WINS!")
        game_running = False
    elif board[3] == "X" and board[4] == "X" and board[5] == "X":
        print("X WINS!")
        game_running = False
    elif board[3] == "O" and board[4] == "O" and board[5] == "O":
        print("O WINS!")
        game_running = False
    elif board[6] == "X" and board[7] == "X" and board[8] == "X":
        print("X WINS!")
        game_running = False
    elif board[6] == "O" and board[7] == "O" and board[8] == "O":
        print("O WINS!")
        game_running = False
    elif board[0] == "X" and board[4] == "X" and board[8] == "X":
        print("X WINS!")
        game_running = False
    elif board[0] == "O" and board[4] == "O" and board[8] == "O":
        print("O WINS!")
        game_running = False
    elif board[2] == "X" and board[4] == "X" and board[6] == "X":
        print("X WINS!")
        game_running = False
    elif board[2] == "O" and board[4] == "O" and board[6] == "O":
        print("O WINS!")
        game_running = False
    elif board[0] == "X" and board[3] == "X" and board[6] == "X":
        print("X WINS!")
        game_running = False
    elif board[0] == "O" and board[3] == "O" and board[6] == "O":
        print("O WINS!")
        game_running = False
    elif board[1] == "X" and board[4] == "X" and board[7] == "X":
        print("X WINS!")
        game_running = False
    elif board[1] == "O" and board[4] == "O" and board[7] == "O":
        print("O WINS!")
        game_running = False
    elif board[2] == "X" and board[5] == "X" and board[8] == "X":
        print("X WINS!")
        game_running = False
    elif board[2] == "O" and board[5] == "O" and board[8] == "O":
        print("O WINS!")
        game_running = False


def check_draw():
    global game_running
    count = 0
    for i in board:
        if i != " ":
            count += 1
            if count == 9:
                print("It's a TIE!")
                game_running = False


# The main game plays through here
while game_running:
    os.system('cls')
    print("Choose a spot.")
    print("1 through 9")
    print("Left to right, top to bottom")
    game_board()
    check_draw()
    check_win()
    choice = input()

    if choice == "1":
        change(0)
    elif choice == "2":
        change(1)
    elif choice == "3":
        change(2)
    elif choice == "4":
        change(3)
    elif choice == "5":
        change(4)
    elif choice == "6":
        change(5)
    elif choice == "7":
        change(6)
    elif choice == "8":
        change(7)
    elif choice == "9":
        change(8)
    else:
        print("Invalid Input!")

