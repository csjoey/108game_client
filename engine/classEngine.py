from engine import classEnemy
from engine import classTileData
from engine import classPlayerData
from engine import classPlayer
import hashlib

class Engine:

    def __init__(self):
        self.seed = None
        self.tile_data = None

        self.enemy_list = None
        self.player = None
        self.player_data = None

    def setup(self):
        self.seed = hash_string(input("Seed through console for now:"))

        self.tile_data = classTileData.TileData()
        self.tile_data.seed_gen(self.seed)

        self.player_data = classPlayerData.PlayerData()
        self.player = classPlayer.Player()

        self.enemy_list = []

    def next_map(self):
        self.seed = hash_string(self.seed)
        self.tile_data.seed_gen(self.seed)

# Locally global functions
def hash_string(str_obj):
    return hashlib.sha256(str_obj.encode()).hexdigest()

