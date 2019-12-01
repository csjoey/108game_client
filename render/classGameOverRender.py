import arcade

class GameOverRender:

    def __init__(self):
        self.score = None
        self.texture_wall = None

    def setup(self,score):
        self.score = score
        self.texture_wall = arcade.load_texture("res/images/wall_mid.png", width=45, height=45)

    def draw(self):
        self.draw_bg()

    def draw_bg(self):
        for row in range(16):
            for col in range(16):
                arcade.draw_texture_rectangle(
                    row * 45 + 22.5,
                    col * 45 + 22.5,
                    45,
                    45,
                    self.texture_wall
                )

    def draw_fg(self):
        pass