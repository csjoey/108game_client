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

        self.max_health_upgrades = None
        self.speed_upgrades = None
        self.tick = None

        self.switch = {
            1: self.coin_pickup,
            2: self.heart_pickup,
            3: self.max_health_pickup,
            4: self.speed_pickup,
            5: self.enemy_spawn
        }

    def setup(self):
        self.tile_data = classTileData.TileData()
        #self.seed = input("Seed through console for now:")
        self.seed = "J"
        self.next_map()

        self.player_data = classPlayerData.PlayerData()
        self.player_data.load_local_save()

        self.max_health_upgrades = self.player_data.max_health_upgrades
        self.speed_upgrades = self.player_data.max_speed_upgrades


        self.player = classPlayer.Player(self.max_health_upgrades, self.speed_upgrades)

        self.enemy_list = []

    def update(self):
        self.check_player_location()
        self.player.sword_ticker()
        if self.player.draw_sword:
            self.sword_collide()

    def keypress(self,key):
        if key == arcade.key.SPACE:
            self.next_map()

        if key == arcade.key.W:
            self.player_move(0, 1)

        if key == arcade.key.A:
            self.player_move(-1, 0)
            self.player.face_right = False

        if key == arcade.key.S:
            self.player_move(0, -1)

        if key == arcade.key.D:
            self.player_move(1, 0)
            self.player.face_right = True

        if key == arcade.key.ENTER:
            self.attack()

    def next_map(self):
        self.seed = hash_string(self.seed)
        self.tile_data.seed_gen(self.seed)
        self.enemy_list = self.tile_data.enemy_list
        print(self.enemy_list)

    def player_move(self, x_offset=0, y_offset=0):
        if self.tile_data.floor_grid[self.player.row + x_offset][self.player.col]:
            self.player.move(self.player.row + x_offset, self.player.col)

        if self.tile_data.floor_grid[self.player.row][self.player.col + y_offset]:
            self.player.move(self.player.row, self.player.col + y_offset)

    def check_player_location(self):
        if self.tile_data.surface_grid[self.player.row][self.player.col]:
            func = self.switch.get(self.tile_data.surface_grid[self.player.row][self.player.col])
            self.tile_data.surface_grid[self.player.row][self.player.col] = 0
            func()

    def coin_pickup(self):
        self.player.coins += 1

    def heart_pickup(self):
        self.player.gain_health()

    def max_health_pickup(self):
        self.player.max_health_up()
        self.max_health_upgrades += 1

    def speed_pickup(self):
        self.player.speed_up()
        self.speed_upgrades += 1

    def enemy_spawn(self):
        return None

    def attack(self):
        self.player.draw_sword = True

    def sword_collide(self):
        for enemy in self.enemy_list:
            if enemy.row == (self.player.row - 1 + (2 * self.player.face_right)) and enemy.col == self.player.col:
                enemy.kill()

# Locally global functions
def hash_string(str_obj):
    return hashlib.sha256(str_obj.encode()).hexdigest()


