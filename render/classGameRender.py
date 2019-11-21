import arcade
from engine import classEngine

class GameRender:

    def __init__(self):
        # Engine
        self.engine = None

        # Map sprite list
        self.map_sprites = None
        # Player Enemy and Upgrade sprite list
        self.ent_sprites = None

        # Map textures
        self.texture_wall = None
        self.texture_floor1 = None
        self.texture_floor2 = None
        self.texture_spike = None
        self.texture_hole = None

        # Ent textures
        self.texture_player = None
        self.texture_coin = None
        self.texture_upgrade_speed = None
        self.texture_upgrade_maxhealth = None
        self.texture_healthpack = None
        self.texture_enemy = None

        # Texture Dicts
        self.bg_textures = None
        self.fg_textures = None


    def setup(self):
        self.engine = classEngine.Engine()
        self.engine.setup()
        self.engine.tile_data.print_grid(self.engine.tile_data.surface_grid)

        self.texture_player = arcade.load_texture("res/images/knight_f_idle_anim_f1.png")
        self.texture_coin = arcade.load_texture("res/images/coin_anim_f0.png")
        self.texture_upgrade_speed = arcade.load_texture("res/images/flask_big_blue.png")
        self.texture_upgrade_maxhealth = arcade.load_texture("res/images/flask_big_red.png")
        self.texture_healthpack = arcade.load_texture("res/images/ui_heart_full.png")
        self.texture_enemy = arcade.load_texture("res/images/imp_idle_anim_f1.png")

        self.texture_hole = arcade.load_texture("res/images/hole.png")
        self.texture_spike = arcade.load_texture("res/images/floor_spikes_anim_f3.png")
        self.texture_wall = arcade.load_texture("res/images/wall_mid.png")
        self.texture_floor1 = arcade.load_texture("res/images/floor_1.png")
        self.texture_floor2 = arcade.load_texture("res/images/floor_2.png")

        self.bg_textures = [
            self.texture_wall,
            self.texture_floor1,
            self.texture_floor2,
            self.texture_hole,
            self.texture_spike
        ]

        self.fg_textures = [
            None,
            self.texture_coin,
            self.texture_healthpack,
            self.texture_upgrade_maxhealth,
            self.texture_upgrade_speed,
            None
        ]

    def draw(self):
        self.draw_bg()
        self.draw_fg()
        arcade.draw_text("DEBUG:GAME", 0, 0, arcade.color.WHITE)


    def update(self):
        pass

    def draw_bg(self):
        for row in range(16):
            for col in range(16):
                arcade.draw_texture_rectangle(
                    (15-col)*45+22.5,
                    (15-row)*45+22.5,
                    45,
                    45,
                    self.bg_textures[self.engine.tile_data.floor_grid[row][col]]
                )

    def draw_fg(self):
        for row in range(16):
            for col in range(16):
                if self.engine.tile_data.surface_grid[row][col] not in [0,5]:
                    arcade.draw_texture_rectangle(
                        (15-col)*45+22.5,
                        (15-row)*45+22.5,
                        30,
                        30,
                        self.fg_textures[self.engine.tile_data.surface_grid[row][col]]
                    )