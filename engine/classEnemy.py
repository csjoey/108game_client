class Enemy:

    def __init__(self):
        self.x = None
        self.y = None

    def setxy(self, x, y):
        self.x = x
        self.y = y

    def update(self, player):
        pass