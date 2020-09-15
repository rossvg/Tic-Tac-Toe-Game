'''
TIC-TAC-TOE                                 Ross Vrana-Godwin
Updated: Sept.15/20

oop version - to be updated


'''


def main():

    print('Main Menu')
    print('input \'help\' to see available commands')
    menu = Menu()
    # Main Menu Loop
    while True:
            x = menu.get_command() # Get a command from the user in the menu
            if x == -1:  # -1 indicates invalid command, repeat the loop and ask for command again.
                print('Bad parameters!')
                continue
            elif x == 1:  # Return of 1 denotes help menu.
                continue
            else:  # Parameters are good, create two players
                p1, p2 = menu.create_players(x)
                break


    board = GameBoard()  # Create new gameboard,
    board.print_board()

    # Main Game Loop
    while True:

        # player 1 move
        '''
        Explanation of 'move block statement:
        This if statement checks to see if the board can be updated without running into a conflict (conflict returns
        a -1) board.update_board is passed the user symbol, and the x,y coordinates. If a conflict is recieved, repeat
        the check asking for coordinates again. .get_move()handles the passing of valid coordiantes from a user end. If
        all is good, update_board updates automatically and then the else statement prints the new board and breaks the
        loop
        '''
        # Player1 move.
        while True:
            if board.update_board(p1.sym, p1.get_move()) == -1:
                continue  # Received error from board indicating the address is already full. Get new move.
            else:  # Board has updated and show it
                board.print_board()
                break

        # Check state.
        if board.state() != 'Game not finished':  # If does not equal, then the game is finished and end program
            print(board.state())
            main()
        else:  # Print the state
            print(board.state())

        #  player 2 move.
        while True:
            if board.update_board(p2.sym, p2.get_move()) == -1:
                continue  # Received error from board indicating the address is already full. Get new move.
            else:  # Board has updated and show it
                board.print_board()
                break

        # Check state.
        if board.state() == False:  # If false, the game is finished! End Program.
            break
        else:  # Print the state
            print(board.state())


def menu_loop(menu):
        while True:
            x = menu.get_command() # Get a command from the user in the menu
            if x == -1:  # -1 indicates invalid command, repeat the loop and ask for command again.
                print('Bad parameters!')
                continue
            else:  # Parameters are good
                p1, p2 = menu.create_players(x)
                break
        return



#-------------------------START Computer Player CLASS--------------------------------------------------------------------------------

class ComputerPlayer:

    from random import random

    def __init__(self, sym):
        self.sym = sym

    def get_move(self):

        from random import randint as r

        print('Making move level \"easy\"')
        moveX = r(0,2)
        moveY = r(0,2)
        args = moveX, moveY
        return args
#-------------------------END ComputerPlayer CLASS--------------------------------------------------------------------------------

#-------------------------START User CLASS--------------------------------------------------------------------------------
class User:
    '''
    Capabilities:
    Creates a user with there player symbol
    Gets a proper move from the user and transforms the coordinates to interact with GameBoard
    '''

    def __init__(self, sym):
        self.sym = sym  # Where sym denotes either X or O
        self.move = None  # Player move

    def get_move(self):
        # Get user coordinates and return GameBoard coordinates

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

            x, y = self.transform(int(user[0]), int(user[1]))  # Input passed first two checks. Transform input to program coordinates
            args = (x, y)
            return args

            # if masterMat[x][y] != '_':
            #     print("This cell is occupied! Choose another one!")
            #     continue
            #
            # else:
            #     masterMat[x][y] = get_xo()
            #     print_matrix()
            #     break

    def transform(self, x ,y):
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

#-------------------------END User CLASS--------------------------------------------------------------------------------

#-------------------------START GameBoard CLASS--------------------------------------------------------------------------------

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

#-------------------------END GameBoard CLASS--------------------------------------------------------------------------------

#-------------------------START Menu CLASS--------------------------------------------------------------------------------


class Menu:

# Note: These methods are quite messy and can be refactored - Sept.15/20

    def __init__(self):
        attr = None

    def get_command(self):

        valid_players = [ 'user', 'easy',]  # List of valid player commands

        cmd = input('Input Command: > ')
        if cmd == 'help':
            self.help_menu()
            return 1

        if cmd != 'exit':  # First check to see if user did not input exit command
            if cmd.startswith('start') == False:  # Second check to see if the string has proprt start
                return -1
            else:
                players = cmd.split(' ') #  Split the commands into a list
                players.pop(0)  # Remove the start command, leaving list with only two player specifications

                if len(players) != 2:
                    return -1
                else:
                        if players[0] not in valid_players or players[1] not in valid_players:  # Check to make sure players is valid
                            return -1
                        else:
                            return players  # IF statement passes, return the players list

        elif cmd == 'exit':
            import sys
            print('system.exit()')
            sys.exit()
        else:
            return -1

    def create_players(self, players):

        # Player 1 determination
        if players[0] == 'user':
            p1 = User('X')
        elif players[0] == 'easy':
            p1 = ComputerPlayer('X')

        # Player 2 determinatation
        if players[1] == 'user':
            p2 = User('O')
        elif players[1] == 'easy':
            p2 = ComputerPlayer('O')

        return p1, p2

    def help_menu(self):
            print('Welcome to help command. Please see below for a list of commands as well as an example')
            print('exit  --> This command exits the program')
            print('help  --> This command prints the help menu')
            print('start <player1> <player2>  --> This command starts the game with the specified players. ')
            print('Only two commands are accepted for player and they must be between the <> characters:')
            print('easy  --> sets a player to an easy level computer player')
            print('user  --> sets a player to a human user player')
            print('Example: > start user easy')
            print('This example starts the game with a human as player 1 and easy level computer as player 2')

#-------------------------END Menu CLASS--------------------------------------------------------------------------------


if __name__ == '__main__':
    main()
