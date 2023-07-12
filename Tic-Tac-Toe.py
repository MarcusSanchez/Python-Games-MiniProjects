import random

board = ["-", "-", "-",
         "-", "-", "-",
         "-", "-", "-"]

currentPlayer = "X"
winner = None
gameRunning = True


# print the game board
def printBoard():
    print(f"\n"
          f" {board[0]} | {board[1]} | {board[2]} \n"
          f"-----------\n"
          f" {board[3]} | {board[4]} | {board[5]} \n"
          f"-----------\n"
          f" {board[6]} | {board[7]} | {board[8]} ")


# take player input
def playerInput():
    print("")
    inp = None
    while inp not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
        inp = input("Enter Position 1-9: ")
        if inp not in ("1", "2", "3", "4", "5", "6", "7", "8", "9"):
            print(f"Sorry {inp} is not an option! TRY AGAIN!")
    inp = int(inp)
    if board[inp - 1] == "-":
        board[inp - 1] = currentPlayer
    else:
        print("Oops, that position is taken!")
        playerInput()


# check for win or tie
def checkHorizontal():
    global winner
    if board[0] == board[1] == board[2] and board[0] != "-":
        winner = board[0]
        return True
    elif board[3] == board[4] == board[5] and board[3] != "-":
        winner = board[3]
        return True
    elif board[6] == board[7] == board[8] and board[6] != "-":
        winner = board[6]
        return True


def checkVertical():
    global winner
    if board[0] == board[3] == board[6] and board[0] != "-":
        winner = board[0]
        return True
    elif board[1] == board[4] == board[7] and board[1] != "-":
        winner = board[1]
        return True
    elif board[2] == board[5] == board[8] and board[2] != "-":
        winner = board[2]
        return True


def checkDiagonal():
    global winner
    if board[0] == board[4] == board[8] and board[0] != "-":
        winner = board[0]
        return True
    elif board[2] == board[4] == board[6] and board[2] != "-":
        winner = board[2]
        return True


def checkTie():
    global gameRunning
    if winner is None:
        if "-" not in board:
            printBoard()
            print(f"\n"
                  f"TIE!")
            gameRunning = False


def checkWin():
    global gameRunning
    if checkDiagonal() or checkVertical() or checkHorizontal():
        printBoard()
        print(f"\n"
              f"The winner is is {winner}")
        gameRunning = False


# switch the player
def switchPlayer():
    global currentPlayer
    if currentPlayer == "X":
        currentPlayer = "O"
    else:
        currentPlayer = "X"


# computer
def computer():
    while currentPlayer == "O":
        if not gameRunning:
            break
        position = random.randint(0, 8)
        if board[position] == "-":
            board[position] = "O"
            switchPlayer()
        print(f"\n"
              f"Computer took position {position + 1}")


def reset():
    global gameRunning, board, currentPlayer, winner
    gameRunning = True
    board = ["-", "-", "-",
             "-", "-", "-",
             "-", "-", "-"]
    currentPlayer = "X"
    winner = None


def runGame():
    while gameRunning:
        printBoard()
        playerInput()
        checkWin()
        checkTie()
        switchPlayer()
        computer()
        if gameRunning:
            checkWin()
            checkTie()


# ask to play again
def replay():
    response = input("Do you want to play again? (Yes/No): ").upper()
    if response == "YES":
        reset()
        runGame()
        replay()
    else:
        print(f"\n"
              f"Good Game")


runGame()
replay()
