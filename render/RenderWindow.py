from render import classGameRender
from render import classLoginRender
from render import classMenuRender
import arcade




SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
SCREEN_TITLE = "The Dungon" # Mispelled on purpose
GAME_SPEED = 1/30

class Display(arcade.Window):

    def __init__(self, width, height, title):
        """
        Initialize window and display variables
        """

        # Setup Window
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)

        # Setup display stages
        self.display_stage = None
        self.game_render = None
        self.menu_render = None
        self.login_render = None

    def setup(self):
        """
        Sets up views and data

        """
        self.display_stage = "Game"

        self.login_render = classLoginRender.LoginRender()
        self.login_render.setup()

        self.menu_render = classMenuRender.MenuRender()
        self.menu_render.setup()

        self.game_render = classGameRender.GameRender()
        self.game_render.setup()

        # Scheduling
#        arcade.schedule(self.scheduled1, 1)


    def on_draw(self):
        """
        Draws based on display stage
        """
        arcade.start_render()

        if self.display_stage == "Login":
            self.login_render.draw()

        if self.display_stage == "Menu":
            self.menu_render.draw()

        if self.display_stage == "Game":
            self.game_render.draw()

        arcade.finish_render()

    def on_update(self, delta_time):
        """
       Game update logic
        """

        if self.display_stage == "Login":
            self.login_render.update()

        if self.display_stage == "Menu":
            self.menu_render.update()

        if self.display_stage == "Game":
            self.game_render.update()


    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        pass

    def on_key_release(self, key, key_modifiers):
        """
        Called whenever the user lets off a previously pressed key.
        """
        self.game_render.engine.next_map()
        pass

    def on_mouse_motion(self, x, y, delta_x, delta_y):
        """
        Called whenever the mouse moves.
        """
        pass

    def on_mouse_press(self, x, y, button, key_modifiers):
        """
        Called when the user presses a mouse button.
        """
        pass

    def on_mouse_release(self, x, y, button, key_modifiers):
        """
        Called when a user releases a mouse button.
        """
        pass

    def scheduled1(self,*args,**kwargs):
        print("1 Second")
#        self.game_render.engine.tile_data.seed_gen()


def main():
    """ Main method """
    game = Display(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()