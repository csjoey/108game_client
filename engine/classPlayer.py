class Player():
    def __init__(self,max_health_upgrades, speed_upgrades, start_row=1, start_col=1):
        self.row = start_row
        self.col = start_col
        self.health = 3 + max_health_upgrades
        self.max_health = 3 + max_health_upgrades
        self.move_delay = 60 - speed_upgrades*5
        self.dead = 0
        self.coins = 0
        self.face_right = True
        self.draw_sword = False
        self.tick = None

    # Note origin is bottom left
    def move(self, new_row, new_col):
        self.row = new_row
        self.col = new_col

    def sword_ticker(self):
        if self.draw_sword:
            self.tick -= 1
        else:
            self.tick = 10
        if self.tick == 0:
            self.draw_sword = False

    def lose_health(self):
        if self.health > 0:
            self.health -= 1
        if self.health == 0:
            self.dead = 1

    def max_health_up(self):
        if self.max_health <= 10:
            self.max_health += 1

    def speed_up(self):
        if self.move_delay > 5:
            self.move_delay -= 5

    def gain_health(self):
        if self.health < self.max_health:
            self.health += 1
