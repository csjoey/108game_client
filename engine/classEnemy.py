import random


class Enemy:

    def __init__(self):
        self.row = None
        self.col = None
        self.open_moves = []

    def set_pos(self, row, col):
        self.row = row
        self.col = col

    def move(self,floor_grid):
        self.open_moves = []
        moves = [-1,1]
        for row in moves:
            for col in moves:
                if not floor_grid[self.row + row][self.col + col]:
                    self.open_moves.append([self.row + row,self.col +col])
        next_move = self.open_moves[random.randint(range(len(self.open_moves)))]
        self.set_pos(next_move[0], next_move[1])






    def update(self, player):
        pass



