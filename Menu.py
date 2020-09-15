
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
        from User import User
        from ComputerPlayer import ComputerPlayer

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

