class Player():
    def __init__(self):
        self.row = None
        self.col = None
        self.health = None
        self.max_health = 3
        self.move_delay = 60
        self.dead = 0


    def move(self, new_row, new_col):
        self.row = new_row
        self.col = new_col

    def lose_health(self):
        if self.health > 0:
            self.health -= 1
        if self.health == 0:
            self.dead = 1

    def max_health_up(self):
        self.max_health += 1

    def speed_up(self):
        if self.move_delay > 5:
            self.move_delay -= 5

    def gain_health(self):
        if self.health < self.max_health:
            self.health += 1
