
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
