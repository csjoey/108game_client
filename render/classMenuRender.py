import arcade
from engine import classPlayerData
from render import classGameRender
class MenuRender:

    def __init__(self):
        self.next_stage = None

        self.texture_sword = None
        self.texture_wall = None

        self.selected = None
        self.selected_functions = None

        self.player_data = None

    def setup(self):
        # Player Data
        self.player_data = classPlayerData.PlayerData()
        self.player_data.load_local_save()

        # Textures
        self.texture_sword = arcade.load_texture("res/images/weapon_regular_sword.png",width=10,height=21)
        self.texture_wall = arcade.load_texture("res/images/wall_mid.png", width=45, height=45)
        self.selected_functions = [self.new_game, self.continue_game]

        # Env Vars
        self.selected = 0

    def update(self):
        pass

    def keypress(self, key):
        self.selected += (1 - self.selected) if key == arcade.key.S else 0
        self.selected -= (1 * self.selected) if key == arcade.key.W else 0

        if key == arcade.key.ENTER:
            func = self.selected_functions[self.selected]
            func()

    def new_game(self):
        self.player_data.blank_save()
        self.player_data.save_local_save()
        self.next_stage = classGameRender.GameRender

    def continue_game(self):
        self.next_stage = classGameRender.GameRender

    def draw(self):
        self.draw_bg()
        self.draw_menu()
        if self.player_data.playtime:
            self.draw_saved_player()
        arcade.draw_text("DEBUG:MENU", 0, 0, arcade.color.WHITE)

    def draw_saved_player(self):
        # TODO Draw player item counts and upgrades on main menu
        pass

    def draw_menu(self):
        arcade.draw_text("New Game",
                         50,
                         600,
                         arcade.color.WHITE,
                         40,
                         bold=True)

        arcade.draw_text("Continue",
                         50,
                         500,
                         arcade.color.WHITE,
                         40,
                         bold=True)
        arcade.draw_texture_rectangle(
            22.5,
            610 - self.selected*100,
            20,
            42,
            self.texture_sword
        )

    def draw_bg(self):
        for row in range(16):
            for col in range(16):
                arcade.draw_texture_rectangle(
                    row*45+22.5,
                    col*45+22.5,
                    45,
                    45,
                    self.texture_wall
                )
