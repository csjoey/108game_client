from render import classGameRender
from render import classLoginRender
from render import classMenuRender
from render import classGameOverRender
import arcade




SCREEN_WIDTH = 720
SCREEN_HEIGHT = 720
SCREEN_TITLE = "The Dungon" # mispelled on purpose
GAME_SPEED = 1/30 #30 fps

class Display(arcade.Window):

    def __init__(self, width, height, title):
        """
        Initialize window and display variables
        """

        # Setup Window
        super().__init__(width, height, title, update_rate=GAME_SPEED)
        arcade.set_background_color(arcade.color.AMAZON)

        # Setup display stages
        self.display_stage = None
        self.game_over = None
        self.score = None

    def setup(self):
        """
        Sets up views and data

        """
        #self.display_stage = classGameRender.GameRender()
        self.display_stage = classMenuRender.MenuRender()
        self.display_stage.setup()
        self.game_over = False

    def on_draw(self):
        """
        Draws based on display stage
        """
        arcade.start_render()

        self.display_stage.draw()

        arcade.finish_render()

    def on_update(self, delta_time):
        """
       Game update logic
        """
        if self.display_stage.next_stage and not self.game_over:
            self.display_stage = self.display_stage.next_stage()
            self.display_stage.setup()
        else:
            self.display_stage.update()
        if self.game_over:
            self.score = self.display_stage.get_score()
            self.display_stage = classGameOverRender.GameOverRender()
            self.display_stage.setup(self.score)

    def on_key_press(self, key, key_modifiers):
        """
        Called whenever a key on the keyboard is pressed.

        For a full list of keys, see:
        http://arcade.academy/arcade.key.html
        """
        self.display_stage.keypress(key)

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