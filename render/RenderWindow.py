import render
import engine
import arcade


SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
SCREEN_TITLE = "The Dungon" # Mispelled on purpose

class Display(arcade.Window):

    def __init__(self, width, height, title):
        """
        Setup Background variables
        """
        super().__init__(width, height, title)
        arcade.set_background_color(arcade.color.AMAZON)
        self.display_stage = None
        self.game_seed = None
        self.game_render = None
        self.menu_render = None
        self.login_menu = None

    def setup(self):
        """
        Sets view to menu or login or game once implemented
        """
        self.display_stage = "Menu"
        self.game_render = render.classGameRender.GameRender()

    def on_draw(self):
        """
        Draws based on display stage
        """
        arcade.start_render()
        if self.display_stage == "Menu":
            arcade.finish_render()

    def on_update(self, delta_time):
        """
        All the logic to move, and the game logic goes here.
        Normally, you'll call update() on the sprite lists that
        need it.
        """
        pass

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


def main():
    """ Main method """
    game = Display(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()