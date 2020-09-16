class MediumComputerPlayer:

    def __init__(self, sym):
        self.sym = sym
        self.oppSym = self.get_opp_sym()

    def get_move(self, currentBoard):
        print('Making move level \'medium\'')

        #check rows
        # do rows
        check1 = self.check_all(currentBoard, self.sym)  # Check to see if there are winning coordinates on the board
        print(f'check1: {check1}')
        check2 = self.check_all(currentBoard, self.oppSym)  # Check to see if a block is available
        print(f'check2: {check2}')


        if check1:  # if true, return the the winning coordinate values.
            print('returning check 1 successful')
            return check1
        elif check2:
            print('check 2 succesfule')
            return check2
        else:
            return self.get_random_move()

    def get_random_move(self):
        from random import randint as r

        print('making random move')
        moveX = r(0,2)
        moveY = r(0,2)
        args = moveX, moveY
        return args

    def get_opp_sym(self):  # Get the opposite symbol of the current class symbol
        if self.sym == 'X':
            return 'O'
        else:
            return 'X'

    def check_all(self, currentBoard, sym_to_check):

        sym = sym_to_check

        # Check for winning values in ROWS
        print('start row check')
        for x, row in enumerate(currentBoard):
            for y, col in enumerate(row):
                if col == '_': #  If there is an empty space in a row
                    row[y] = sym # Fill that space with a symbol
                    if len(set(row)) == 1: # if the set is 1 all the symbols are the same!
                        print('this is the return statement for row check')
                        return x,y  # Return the wiinning coordinates
                    else:  # the set is not one so must be different symbols
                        row[y] = '_' # return it back to blank character

        print('start col check')

        import copy
        # Check for winning values in COLS
        currentBoard_copy = copy.deepcopy(currentBoard)  # Create a copy of the current board to transpose
        transposeMat = [list(x) for x in zip(*currentBoard_copy)]  # Transpose the current board
        for x, row in enumerate(transposeMat):  # Loop through new board. Keep track of row number in x
            for y, col in enumerate(row):  # Loop through each row, value stored in col, index stored in y
                if col == '_':  # If there is a blank value in the row
                    row[y] = sym  # Replace the value with the current symbol
                    if len(set(row)) == 1: # if the set is 1 all the symbols are the same!
                        transposeMat[x][y] = '!'  # Mark this location in the board with a '!' using x and y as they were keeping track of the index
                        transposeMat2 = [list(x) for x in zip(*transposeMat)] # Transpose the matrix back to the original
                        for i, rows2 in enumerate(transposeMat2):  # Find where the '!' symbol is and return the coord
                            if '!' in rows2:
                                return i, rows2.index('!')  # Return winning coordinates holy eff this was convoluted
                    else:
                        row[y] = '_' # Make sure to change value back!

                # Else: if no if statements succeeded and no return statements, continue on

        # Check first diagonal for winning value
        diagonal1 = [currentBoard[0][0], currentBoard[1][1], currentBoard[2][2]]
        for x, y in enumerate(list(diagonal1)):  # go through the fist list. Keep track of index in 'x'
            if y == "_":  # If there is an empty spot
                diagonal1[x] = sym  # Fill it with the current symbol
                if len(set(diagonal1)) == 1:  # See if all symbols match
                    if x == 0:  # If the symbols match at the 0 position in diagonal, return those coordinates
                        return 0, 0
                    elif x == 1:
                        return 1, 1
                    elif x == 2:
                        return 2, 2
                else:  # Symbols don't match, restore the list
                    diagonal1[x] = '_'

        # Check second diagonal for winning value
        print('start diag check 2')
        diagonal2 = [currentBoard[0][2], currentBoard[1][1], currentBoard[2][0]]
        for x, y in enumerate(list(diagonal2)):  # go through the fist list. Keep track of index in 'x'
            if y == "_": # If there is an empty spot
                diagonal2[x] = sym  # Fill it with the current symbol
                if len(set(diagonal2)) == 1:  # See if all symbols match
                    if x == 0:  # If the symbols match at the 0 position in diagonal, return those coordinates
                        return 0, 2
                    elif x == 1:
                        return 1, 1
                    elif x == 2:
                        return 2, 0
                else:  # Symbols don't match, restore the list
                    diagonal2[x] = '_'

        return False  # No other return statement was met so return false
