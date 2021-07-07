### CONNECT 4 ###

#Import the coloring modules
import sys
from termcolor import colored

#Creates the board
#INPUT: none
#OUTPUT: "board" (list of list)
def create_board():
    board = []
    for e in range(7):
        #will create a column at a time
        colum = []
        for ele in range(7):
            colum.append(" ")
        #then append the column to the board
        board.append(colum)
    return board

#Function for printing the board in a user-friendly way
#INPUT: board
#OUTPUT: none
def printable(array):
    #The firsts rows will be on the bottom, and the last will be on top
    for a in range(6,-1,-1):
        linea = ""
        for k in range (15):
            if k % 2 == 1:
                j = (k-1) // 2 
                linea += array[a][j] 
            else:
                #Will create separators for the columns
                linea += "|"
        print(linea)
    print("¯"*15)

#Cheks the free slot of a given column, or if it is full
#INPUT: number of column, board
#OUTPUT: tuple (column, row), or boolean if full
def jugada(num, array):
    for a in range(7):
        if array[a][num] == " ":
            return (a, num)
    return False

#Checks if theres a winner. 
#INPUT: board (list)
#UTPUT: boolean
def checker(array):
    for xx in range(7):
        for yy in range(4):
            if array[xx][yy] != " " and array[xx][yy] == array[xx][yy+1] == array[xx][yy+2] == array[xx][yy+3]:
                    return True
    for xx in range(4):
        for yy in range(4):
            if array[xx][yy] != " " and array[xx][yy] == array[xx+1][yy+1] == array[xx+2][yy+2] == array[xx+3][yy+3]:
                    return True
        for yy in range(7):
            if array[xx][yy] != " " and array[xx][yy] == array[xx+1][yy] == array[xx+2][yy] == array[xx+3][yy]:
                    return True
        for yy in range(3,7):
            if array[xx][yy] != " " and array[xx][yy] == array[xx+1][yy-1] == array[xx+2][yy-2] == array[xx+3][yy-3]:
                    return True
    return False

#Game structure
def juego():
    #starting statements
    print("Let the game begin!")
    print("Player 1 plays with O's")
    print("Player 2 plays with X's")
    player1 = True
    #creates the board

    board = create_board()
    checkwin = False
    #This will work until a winner is declared

    while checkwin == False:
        print("\nTurn of the O's\n" if player1 == True else "\nTurn of the X's\n")

        #movements for player 1
        if player1 == True:
            turn = int(input("Player 1) enter the number of column: "))

            #checks if input is valid
            while turn < 1 or turn > 7:
                turn = int(input("Invalid input. Enter a number between 1 and 7: "))

            #checks if column is full
            if jugada(turn-1, board) == False:
                print("This column is full, your turn is over\n")
                player1 = False

            #change the value of the slot
            else:
                a, num = jugada(turn-1, board)
                board[a][num] = colored('O', 'blue')
                printable(board)
                if checker(board) == True:
                    print("Winner: Player 1 (O)\n####################")
                    checkwin = True
                player1 = False

        #movements for player 2
        else:
            turn = int(input("Player 2) enter the number of column: "))

            #checks if input is valid
            while turn < 1 or turn > 7:
                turn = int(input("Invalid input. Enter a number between 1 and 7: "))

            #checks if column is full
            if jugada(turn-1, board) == False:
                print("This column is full, your turn is over\n")
                player1 = True

            #change the value of the slot
            else:
                a, num = jugada(turn-1, board)
                board[a][num] = colored('X', 'red')
                printable(board)
                if checker(board) == True:
                    print("Winner: Player 2 (X)\n####################")
                    checkwin = True
                player1 = True          

#Start game!
juego()

#Ask if want to play a new match
playagain = True
while playagain == True:
    qst = input("Press enter if you want to play again")
    if qst == "":
        juego()
    else: 
        playagain = False