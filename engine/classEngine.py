from engine import classEnemy
from engine import classTileData
from engine import classPlayerData
from engine import classPlayer
import hashlib
import arcade

class Engine:

    def __init__(self):
        self.seed = None
        self.tile_data = None

        self.enemy_list = None
        self.player = None
        self.player_data = None

    def setup(self):
        #self.seed = hash_string(input("Seed through console for now:"))
        self.seed = hash_string("J")
        self.tile_data = classTileData.TileData()
        self.tile_data.seed_gen(self.seed)

        self.player_data = classPlayerData.PlayerData()
        self.player = classPlayer.Player(0,0)

        self.enemy_list = []

    def update(self):
        pass

    def keypress(self,key):
        if key == arcade.key.SPACE:
            self.next_map()

        if key == arcade.key.W:
            self.player_move(0, 1)

        if key == arcade.key.A:
            self.player_move(-1, 0)

        if key == arcade.key.S:
            self.player_move(0, -1)

        if key == arcade.key.D:
            self.player_move(1, 0)

    def next_map(self):
        self.seed = hash_string(self.seed)
        self.tile_data.seed_gen(self.seed)

    def player_move(self, x_offset=0, y_offset=0):
        if self.tile_data.floor_grid[self.player.row + x_offset][self.player.col]:
            self.player.move(self.player.row + x_offset, self.player.col)

        if self.tile_data.floor_grid[self.player.row][self.player.col + y_offset]:
            self.player.move(self.player.row, self.player.col + y_offset)


# Locally global functions
def hash_string(str_obj):
    return hashlib.sha256(str_obj.encode()).hexdigest()

