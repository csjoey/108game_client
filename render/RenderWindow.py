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
        self.last_key = None



    def setup(self):
        """
        Sets up views and data

        """
        self.display_stage = classMenuRender.MenuRender()
        self.display_stage.setup()

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
        if self.display_stage.next_stage:
            self.display_stage = self.display_stage.next_stage()
            self.display_stage.setup()
        else:
            self.display_stage.update()

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

def main():
    """ Main method """
    game = Display(SCREEN_WIDTH, SCREEN_HEIGHT, SCREEN_TITLE)
    game.setup()
    arcade.run()