import random


class Enemy:

    def __init__(self, row, col):
        self.row = row
        self.col = col
        self.dead = 0
        self.open_moves = []
        self.moves = [-1,1]

    def set_pos(self, row, col):
        self.row = row
        self.col = col

    def move(self, floor_grid):
        self.open_moves = []
        for row in self.moves:
            for col in self.moves:
                if floor_grid[self.row + row][self.col + col]:
                    self.open_moves.append([self.row + row,self.col + col])
        print("moves: ", self.open_moves)
        next_move = self.open_moves[random.randint(0,len(self.open_moves) - 1)]
        self.set_pos(next_move[0], next_move[1])

    def kill(self):
        self.dead = 1

    def update(self, player):
        pass



