"""
***************Documentation****************
Tic-Tac-Toe game by Bhargav.S.S in Python 3
-Features : User vs Computer where the Computer plays optimally using a greedy algorithm.
"""
import random

def drawGrid(grid):
    #Displays the current grid
    print(' ' + grid[6] + ' | ' + grid[7] + ' | ' + grid[8] + ' ')
    print('___________')
    print(' ' + grid[3] + ' | ' + grid[4] + ' | ' + grid[5] + ' ')
    print('___________')
    print(' ' + grid[0] + ' | ' + grid[1] + ' | ' + grid[2] + ' ')
    print()


def checkWin(grid , player):
    #Check if the player has won
    if ((grid[6] == grid[7] == grid[8] == player) or (grid[3] == grid[4] == grid[5] == player) or (grid[0] == grid[1] == grid[2] == player) or (grid[6] == grid[3] == grid[0] == player) or (grid[7] == grid[4] == grid[1] == player) or (grid[8] == grid[5] == grid[2] == player) or (grid[6] == grid[4] == grid[2] == player) or (grid[8] == grid[4] == grid[0] == player)):
        return True


def possibleMoves(grid):
    #Returns a list of all possible moves
    lst = []
    for i in range(9):
        if grid[i] == ' ':
            lst.append(i)
    return lst


def listCopy(b):
    #Copies list b to list a and returns a
    a = []
    for i in b:
        a.append(i)
    return a


def usersTurn(grid,user):
    print('\nYour turn-\n')
    possiblemoves = possibleMoves(grid)
    move = int(input('Enter your move:'))
    if move not in possiblemoves:
        print('That move\'s already taken:(')
        move = int(input('Try again:'))
    grid[move] = user
    drawGrid(grid)
    a = checkWin(grid, user)
    if a == True:
        print('You won!!!!!!Congo!')
    return a


def computersTurn(grid,computer):
    print('\nComputer\'s turn-\n')
    possiblemoves = possibleMoves(grid)
    #Trying to win
    possibleToWin = False
    for i in possiblemoves:
        duplicateGrid = listCopy(grid)
        duplicateGrid[i] = computer
        if checkWin(duplicateGrid, computer) == True:
            move = i
            possibleToWin = True
            break
    if possibleToWin == False:
        #Stopping the user to win on the next move
        favourableMoves = listCopy(possiblemoves)
        k=0
        while k<len(favourableMoves):
            tempMove = favourableMoves[k]
            duplicateGrid = listCopy(grid)
            duplicateGrid[tempMove] = computer
            duplicatepossiblemoves = possibleMoves(duplicateGrid)
            userwinning = False
            for j in duplicatepossiblemoves:
                anotherduplicateGrid = listCopy(duplicateGrid)
                anotherduplicateGrid[j] = user
                if checkWin(anotherduplicateGrid, user) == True:
                    favourableMoves.pop(favourableMoves.index(tempMove))
                    userwinning = True
                    break
            if userwinning == False:
                k=k+1
        try:
            move = favourableMoves[random.randint(0,len(favourableMoves)-1)]
        except:
            move = random.choice(possibleMoves(grid))
    grid[move] = computer
    drawGrid(grid)
    a = checkWin(grid, computer)
    if a == True:
        print('Computer wins:(\tGame Over')
    return a


while True:
    print('Welcome to Tic-Tac-Toe!!!!')

    # Printing the positions in the grid
    print('Note down the positions in the grid as follows:')
    drawGrid(list(map(str, range(9))))

    # Naming the user and the computer
    a = input('What do you want to be? X or O ? (It\'s Oh not zero!)')
    while (a != 'X' and a != 'O'):
        print('Oh! That was an invalid entry:(')
        a = input('Try again:')
    user = a
    if user == 'X':
        computer = 'O'
    else:
        computer = 'X'

    # Initializing grid
    grid = []
    for i in range(9):
        grid.append(' ')

    # Deciding who plays first
    a = random.randint(0, 1)
    if a == 0:
        firstPlayer = computer
        secondPlayer = user
        print('Computer plays first!')
    else:
        firstPlayer = user
        secondPlayer = computer
        print('You play first!')

    count = 0
    if firstPlayer == computer:
        a = False
        while a != True:
            a = computersTurn(grid, computer)
            count = count + 1
            if count == 9 and a != True:
                break
            if a != True:
                a = usersTurn(grid, user)
                count = count + 1
    else:
        a = False
        while a != True:
            a = usersTurn(grid, user)
            count = count + 1
            if count == 9 and a != True:
                break
            if a != True:
                a = computersTurn(grid, computer)
                count = count + 1

    if count == 9:
        print('It\'s a draw -_-')

    choice = input('Wanna play again?(y/n)')
    while choice not in ['y','n']:
        print('Invalid entry')
        choice = input('Try again:')

    if choice == 'n':
        break











