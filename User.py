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
