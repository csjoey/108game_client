import arcade
from render import classMenuRender
from engine import classPlayerData


class GameOverRender:

    def __init__(self):
        self.score = None
        self.texture_wall = None
        self.next_stage = None
        self.player_data = None
        self.timer = None

    def setup(self):
        self.timer = 90

        self.player_data = classPlayerData.PlayerData()
        self.player_data.load_local_save()
        # self.player_data now contains all player savedata
        self.score = self.player_data.score
        self.texture_wall = arcade.load_texture("res/images/wall_mid.png", width=45, height=45)

    def update(self):
        self.timer -= 1
        if self.timer == 0:
            self.next_stage = classMenuRender.MenuRender

    def draw(self):
        self.draw_bg()
        arcade.draw_text("GAMEOVER", 210, 360, arcade.color.WHITE,font_size=50,align="center")

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