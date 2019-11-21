from engine import classEnemy
from engine import classTileData
from engine import classPlayerData
from engine import classPlayer

class Engine:

    def __init__(self):
        self.tile_data = None
        self.player_data = None

        self.enemy_list = None

        self.player = None

    def setup(self):

        self.tile_data = classTileData.TileData()
        self.tile_data.seed_gen()

        self.player_data = classPlayerData.PlayerData()
        self.player = classPlayer.Player()

        self.enemy_list = []


