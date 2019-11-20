import arcade
class GameRender:

    def __init__(self):
        # Map sprite list
        self.map_sprites = None
        # Player Enemy and Upgrade sprite list
        self.ent_sprites = None

        # Map sprites
        sprite_wall = None
        sprite_floor1 = None
        sprite_floor2 = None

        # Ent sprites
        sprite_player = None

    def setup(self):
        self.map_sprites = arcade.SpriteList()
        self.ent_sprites = arcade.SpriteList()

    def draw(self):
        arcade.draw_text("DEBUG:GAME",0,0,arcade.color.WHITE)

    def update(self):
        pass
