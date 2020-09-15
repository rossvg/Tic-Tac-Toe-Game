class GameBoard:
    '''
    Capabilities:
    Set up a blank board upon instantiation
    Print the current gameboard
    Update the gameboard given coordinates
    Transform user coordinates to program coordinates - NOTE: This has been moves to user.py!
    Determine and return active state of gameboard
    '''

    def __init__(self):
        self.board = self.setup_board()
        # setup the blank matrix

    def setup_board(self):
        #  Sets up a blank board full of '_' char
        masterMat = []
        user = '_________'
        masterMat.append(list(user[0:3]))
        masterMat.append(list(user[3:6]))
        masterMat.append(list(user[6:9]))
        return masterMat

    def update_board(self, sym, args):
        #  Update the board with the correct symbol at the correct location. Handles conflicts!
        x = args[0]
        y = args[1]
        if self.board[x][y] != '_':
            print("This cell is occupied! Choose another one!")
            return -1

        else:
            self.board[x][y] = sym
            return 1



    def get_xo(self):  # Note: May be deprecated
    # Determines amount of x and o chars and returns appropriate starting character

        x, o = 0, 0
        for i in self.board:
            for j in i:
                if j == 'X':
                    x = x + 1
                elif j == 'O':
                    o = o + 1
        if x == o:
            return 'X'
        elif x>o:
            return 'O'

    def print_board(self):
    # Prints the current tic-tac-toe matrix

        print('---------')
        print(f'| {self.board[0][0]} {self.board[0][1]} {self.board[0][2]} |')
        print(f'| {self.board[1][0]} {self.board[1][1]} {self.board[1][2]} |')
        print(f'| {self.board[2][0]} {self.board[2][1]} {self.board[2][2]} |')
        print('---------')

    def state(self):
        #  Determines and acts upon the state of the game.

        # do rows
        for row in self.board:
            if len(set(row)) == 1 and '_' not in row:
                return f'{row[0]} wins'

        # do cols
        transposeMat = [list(x) for x in zip(*self.board)]
        for row in transposeMat:
            if len(set(row)) == 1 and '_' not in row:
                return f'{row[0]} wins'

        # Computes diagonal win condition with hard-coded values. Outputs middle character as win character.
        if self.board[0][0] == self.board[1][1] and self.board[1][1] == self.board[2][2] and '_' not in self.board[1][1]:
            return f'{self.board[0][0]} wins'
        elif self.board[0][2] == self.board[1][1] and self.board[1][1] == self.board[2][0] and '_' not in self.board[1][1]:
            return f'{self.board[0][2]} wins'

        # Draw and game not finished
        if any(j for row in self.board for j in row if j == '_'):  # If any '_' is found and the above conditions are not met, the game is not finished
            #print('Game not finished')
            return 'Game not finished'
        else:  # If no '_' characters are found and no other win condition is met, it must be a draw.
            return 'Draw'
