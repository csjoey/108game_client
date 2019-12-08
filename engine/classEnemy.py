import random


class Enemy:
    """
    creates enemy objects
    """

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.dead = 0
        self.open_moves = []
        self.moves = [-1,0,1]

    def set_pos(self, row, col):
        # sets position based on parameters
        self.row = row
        self.col = col

    def move(self, floor_grid):
        # Random movement
        moves = self.moves
        self.open_moves = []
        if self.row == 14:
            moves = [-1,0]
        if self.row == 1:
            moves = [0,1]
        if self.col == 14:
            moves = [-1,0]
        if self.col == 1:
            moves = [0,1]

        for row in moves:
            for col in moves:
                if floor_grid[self.row + row][self.col + col] > 0:
                    self.open_moves.append([self.row + row,self.col + col])
        next_move = self.open_moves[random.randint(0, len(self.open_moves) - 1)]
        self.set_pos(next_move[0], next_move[1])

    def kill(self):
        # sets status of enemy object to dead
        self.dead = 1

    def update(self, player):
        # Runs when engine is updated
        pass



