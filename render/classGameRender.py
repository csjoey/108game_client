import arcade
from engine import classEngine

class GameRender:

    def __init__(self):
        # Map sprite list
        self.map_sprites = None
        # Player Enemy and Upgrade sprite list
        self.ent_sprites = None

        # Map textures
        self.texture_wall = None
        self.texture_floor1 = None
        self.texture_floor2 = None

        # Ent sprites
        self.sprite_player = None


    def setup(self):
        self.ent_sprites = arcade.SpriteList()

        self.texture_wall = arcade.load_texture("res/images/wall_mid.png")





    def draw(self):
        arcade.draw_text("DEBUG:GAME",0,0,arcade.color.WHITE)
        self.draw_bg()


    def update(self):
        pass

    def draw_bg(self):
        for x in range(16):
            for y in range(16):
                arcade.draw_texture_rectangle(45*x+22.5,45*y+22.5,45,45,self.texture_wall)

