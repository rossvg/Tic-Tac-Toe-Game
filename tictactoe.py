'''
Tic-Tac-Toe                                         September 10, 2020
Ross Vrana-Godwin

Tic-Tac-Toe based of a project from jetbrains academy.

The board displayed to the user looks like this:
(1, 3) (2, 3) (3, 3)
(1, 2) (2, 2) (3, 2)     USER
(1, 1) (2, 1) (3, 1)

The board the program uses looks like this:

[0,0] [0,1] [0,2]
[1,0] [1,1] [1,2]		PROGRAM
[2,0] [2,1] [2,2]

the transform(x, y) function maps between user input and the program.


'''

import random

masterMat = [] #  Keeps track of matrix at all times

def main():

    get_first_move() #  Displays an empty board.

    while True:

        get_coord() #  Get coordinates from user.

        winCondition = eval_game() # Get status of game
        if winCondition == 'Game not finished':
            print(winCondition)
        else:
            print(winCondition)
            print_matrix()
            break

        Easy_Com_Move() # 'Computer' makes a random move


        winCondition = eval_game() # Get status of game
        if winCondition == 'Game not finished':
            print(winCondition)
        else:
            print(winCondition)
            print_matrix()
            break

def get_first_move():
    # Sets up the board with initial 9 cells

    valid = ('X', 'O', '_') #  Valid characters the user can enter

    while True: #  This for loop runs until a valid input is entered
        #user = input('Enter Cells: > ')
        user = '_________'

        if len(user) != 9:
            print('must enter 9 characters')


        elif any(i for i in user if i not in valid) == True: #  checks if any user entered chars are not in the valid set
                print('not valid characters enter again')
        else:
            break  # User input is good, break the loop and print output

    # Create the board as a 3x3 matrix
    masterMat.append(list(user[0:3]))
    masterMat.append(list(user[3:6]))
    masterMat.append(list(user[6:9]))

    print_matrix()  # Display the board on the command line

def get_coord():
    # Get user coordinates

    valid = ['1', '2', '3']  # List of valid characters that can be entered

    while True:  # Ensures user input is valid
        user = input('Enter the coordinates: > ')
        user = user.strip() # Strip of any whitespace
        user = user.split(' ')

        if len(user) != 2:
            print('You should enter numbers!')
            continue

        elif any(i for i in user if i not in valid) == True:
            print('Coordinates should be from 1 to 3!')
            print('You should enter numbers!')
            continue

        x, y = transform(int(user[0]), int(user[1]))  # Input passed first two checks. Transform input to program coordinates

        if masterMat[x][y] != '_':
            print("This cell is occupied! Choose another one!")
            continue

        else:
            masterMat[x][y] = get_xo()
            print_matrix()
            break




def eval_game():

    copy = masterMat

    # do rows
    for row in masterMat:
        if len(set(row)) == 1 and '_' not in row:
            return f'{row[0]} wins'

    # do cols
    transposeMat = [list(x) for x in zip(*copy)]
    for row in transposeMat:
        if len(set(row)) == 1 and '_' not in row:
            return f'{row[0]} wins'
    # Do Diagonal
    if copy[0][0] == copy[1][1] and copy[1][1] == copy[2][2] and '_' not in copy[1][1]:
        return f'{copy[0][0]} wins'
    elif copy[0][2] == copy[1][1] and copy[1][1] == copy[2][0] and '_' not in copy[1][1]:
        return f'{copy[0][2]} wins'

    # Draw
    if any(j for row in copy for j in row if j == '_'):
        return 'Game not finished'
    else:
        return 'Draw'

def Easy_Com_Move():
    print('Making move level \"easy\"')
    while True:
        moveX = random.randint(0,2)
        moveY = random.randint(0,2)
        if masterMat[moveX][moveY] != '_': #  choice is a cell already occupied. Repeat loop unti lempty cell is chose
            continue
        else:
            masterMat[moveX][moveY] = 'O'
            print_matrix()
            break







def print_matrix():
    # Prints the current tic-tac-toe matrix

    print('---------')
    print(f'| {masterMat[0][0]} {masterMat[0][1]} {masterMat[0][2]} |')
    print(f'| {masterMat[1][0]} {masterMat[1][1]} {masterMat[1][2]} |')
    print(f'| {masterMat[2][0]} {masterMat[2][1]} {masterMat[2][2]} |')
    print('---------')


def get_xo():
    # Determines amount of x and o chars and returns appropriate starting character
        x, o = 0, 0
        for i in masterMat:
            for j in i:
                if j == 'X':
                    x = x + 1
                elif j == 'O':
                    o = o + 1
        if x == o:
            return 'X'
        elif x>o:
            return 'O'



def transform(x,y):
    # Transforms the function from the user input

    # There must be an easier way to do this
    # Col 1
    if x == 1:
        if y == 3:
            x, y = 0, 0
            return x, y
        elif y == 2:
            x, y = 1, 0
            return x, y
        elif y == 1:
            x, y = 2, 0
            return x, y

    # Col 2
    elif x == 2:
        if y == 3:
            x, y = 0, 1
            return x, y
        elif y == 2:
            x, y = 1, 1
            return x, y
        elif y == 1:
            x, y = 2,1
            return x, y

    # Col 3
    elif x == 3:
        if y == 3:
            x, y = 0,2
            return x, y
        elif y == 2:
            x, y = 1, 2
            return x, y
        elif y == 1:
            x, y = 2, 2
            return x, y





if __name__ == '__main__':
    main()



