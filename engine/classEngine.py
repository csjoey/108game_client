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
        self.enemy_locations = None
        self.player = None
        self.player_data = None

        self.max_health_upgrades = None
        self.speed_upgrades = None
        self.tick = None
        self.room_coins = None
        self.total_coins = None
        self.from_direction = None

        self.switch = {
            1: self.coin_pickup,
            2: self.heart_pickup,
            3: self.max_health_pickup,
            4: self.speed_pickup,
            5: self.enemy_spawn
        }

        self.sound_theme = None
        self.sound_all_coins = None
        self.sound_coin = None
        self.sound_attack = None
        self.sound_hurt = None
        self.sound_upgrade = None

        self.next_stage = None
        self.tick = None
        self.exit_list = [0,7,8,15]
        self.game_timer = None
        self.game_tick = None

    def setup(self):
        self.from_direction = 0
        self.tile_data = classTileData.TileData()
        # self.seed = input("Seed through console for now:")

        self.player_data = classPlayerData.PlayerData()
        self.player_data.load_local_save()

        self.seed = self.player_data.seed
        self.next_map()

        self.max_health_upgrades = self.player_data.max_health_upgrades
        self.speed_upgrades = self.player_data.max_speed_upgrades
        self.total_coins = self.tile_data.return_coins()

        self.player = classPlayer.Player(self.max_health_upgrades, self.speed_upgrades)

        self.enemy_list = []

        self.sound_theme = arcade.load_sound("res/sounds/game_music.wav")
        self.sound_all_coins = arcade.sound.load_sound("res/sounds/nextstage.wav")
        self.sound_coin = arcade.sound.load_sound("res/sounds/coin.wav")
        self.sound_attack = arcade.sound.load_sound("res/sounds/hit.wav")
        self.sound_hurt = arcade.sound.load_sound("res/sounds/hurt.wav")
        self.sound_upgrade = arcade.sound.load_sound("res/sounds/upgrade.wav")
        arcade.play_sound(self.sound_theme)

        self.game_tick = 30
        self.game_timer = 10

    def update(self):
        self.check_player_location()
        if len(self.enemy_list):
            if self.tick < 1:
                self.enemy_movement()
                self.tick = 30
            else:
                self.tick -= 1
        self.player.sword_ticker()
        if self.player.draw_sword:
            self.sword_collide()
        if self.game_tick > 0:
            self.game_tick -= 1
        if self.game_tick == 0:
            self.game_tick = 30
            self.game_timer -= 1

    def keypress(self,key):
        self.player.draw_sword = False
        if key == arcade.key.SPACE:
            self.next_map()

        if key == arcade.key.W:
            self.player_move(0, 1)

        if key == arcade.key.A:
            self.player_move(-1, 0)
            self.player.face_right = 0

        if key == arcade.key.S:
            self.player_move(0, -1)

        if key == arcade.key.D:
            self.player_move(1, 0)
            self.player.face_right = 1

        if key == arcade.key.ENTER:
            self.attack()

    def next_map(self):
        self.seed = hash_string(self.seed)
        self.tile_data.seed_gen(self.seed, self.from_direction)
        self.enemy_list = self.tile_data.enemy_list
        self.enemy_locations = []
        for enemy in self.enemy_list:
            self.enemy_locations.append(enemy.get_pos())
        self.room_coins = 0
        self.total_coins = self.tile_data.return_coins()

    def player_move(self, x_offset=0, y_offset=0):
        if self.tile_data.floor_grid[self.player.row + x_offset][self.player.col] > 0:
            if not ((self.player.row + x_offset, self.player.col) in self.enemy_locations):
                self.player.move(self.player.row + x_offset, self.player.col)

        if self.tile_data.floor_grid[self.player.row][self.player.col + y_offset] > 0:
            if not ((self.player.row + x_offset, self.player.col) in self.enemy_locations):
                self.player.move(self.player.row, self.player.col + y_offset)

        if self.player.col == 15:
            self.from_direction = 3
            self.player.col = 1
            self.next_map()
            self.game_timer += 3

        if self.player.row == 15:
            self.from_direction = 4
            self.player.row = 1
            self.next_map()
            self.game_timer += 3

        if self.player.col == 0:
            self.from_direction = 1
            self.player.col = 14
            self.next_map()
            self.game_timer += 3

        if self.player.row == 0:
            self.from_direction = 2
            self.player.row = 14
            self.next_map()
            self.game_timer += 3

    def check_player_location(self):
        if self.tile_data.surface_grid[self.player.row][self.player.col]:
            func = self.switch.get(self.tile_data.surface_grid[self.player.row][self.player.col])
            self.tile_data.surface_grid[self.player.row][self.player.col] = 0
            func()

    def enemy_movement(self):
        self.enemy_locations = []

        for enemy in self.enemy_list:
            if not self.enemy_attack(enemy):
                enemy.move(self.tile_data.floor_grid)
            self.enemy_locations.append(enemy.get_pos())

    def enemy_attack(self, enemy):
        for row in enemy.moves:
            for col in enemy.moves:
                if (self.player.row == enemy.row + row) and (self.player.col == enemy.col + col):
                    self.player.lose_health()
                    if self.player.health < 1:
                        self.end_game()
                    arcade.sound.play_sound(self.sound_hurt)
                    return True

    def coin_pickup(self):
        arcade.sound.play_sound(self.sound_coin)
        self.player.coins += 1
        self.room_coins += 1
        if self.room_coins == self.total_coins:
            arcade.sound.play_sound(self.sound_all_coins)
            for row in self.exit_list:
                for col in self.exit_list:
                    if self.tile_data.floor_grid[row][col] == -1:
                        self.tile_data.floor_grid[row][col] = 1




    def heart_pickup(self):
        self.player.gain_health()
        arcade.sound.play_sound(self.sound_upgrade)

    def max_health_pickup(self):
        self.player.max_health_up()
        self.max_health_upgrades += 1
        arcade.sound.play_sound(self.sound_upgrade)

    def speed_pickup(self):
        self.player.speed_up()
        self.speed_upgrades += 1
        arcade.sound.play_sound(self.sound_upgrade)

    def enemy_spawn(self):
        pass

    def stage_done(self):
        pass

    def end_game(self):
        arcade.stop_sound(self.sound_theme)
        self.player_data.seed = self.seed
        self.player_data.max_speed_upgrades = self.speed_upgrades
        self.player_data.max_health_upgrades = self.max_health_upgrades
        self.player_data.coins += self.player.coins
        self.player_data.playtime = 1
        self.player_data.save_local_save()
        self.next_stage = True

    def attack(self):
        self.player.draw_sword = True

    def sword_collide(self):
        new_list = []
        self.enemy_locations = []
        for enemy in self.enemy_list:
            if enemy.row == (self.player.row - 1 + (2 * self.player.face_right)) and enemy.col == self.player.col:
                enemy.kill()
                self.enemy_locations.append(enemy.get_pos())
                arcade.sound.play_sound(self.sound_attack)
            if not enemy.dead:
                new_list.append(enemy)
        self.enemy_list = new_list


# Locally global functions
def hash_string(str_obj):
    return hashlib.sha256(str_obj.encode()).hexdigest()


