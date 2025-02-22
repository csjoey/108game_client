from engine import classEnemy
from engine import classTileData
from engine import classPlayerData
from engine import classPlayer
import hashlib
import arcade
import pyglet


class Engine:
    """
    Class to handle game engine things, workplace for tile, enemy, and player objects
    """

    def __init__(self):
        self.seed = None
        self.tile_data = None

        self.enemy_list = None
        self.enemy_locations = None
        self.player = None
        self.player_data = None
        self.clear = None

        self.max_health_upgrades = None
        self.speed_upgrades = None
        self.room_coins = None
        self.total_coins = None
        self.from_direction = None

        # This switch case handles the different items that appear on the surface grid
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
        self.exit_list = [0,7,8,15]
        self.game_timer = None
        self.game_tick = None
        self.score = None
        self.theme = None

        self.mplayer = None

    def setup(self):
        self.from_direction = 0
        self.tile_data = classTileData.TileData()

        self.enemy_list = []

        self.player_data = classPlayerData.PlayerData()
        self.player_data.load_local_save()

        self.seed = self.player_data.seed
        self.next_map()

        self.max_health_upgrades = self.player_data.max_health_upgrades
        self.speed_upgrades = self.player_data.max_speed_upgrades
        self.total_coins = self.tile_data.return_coins()

        self.player = classPlayer.Player(self.max_health_upgrades, self.speed_upgrades)

        self.sound_theme = pyglet.media.load("res/sounds/game_music.wav")
        self.sound_all_coins = arcade.sound.load_sound("res/sounds/nextstage.wav")
        self.sound_coin = arcade.sound.load_sound("res/sounds/coin.wav")
        self.sound_attack = arcade.sound.load_sound("res/sounds/hit.wav")
        self.sound_hurt = arcade.sound.load_sound("res/sounds/hurt.wav")
        self.sound_upgrade = arcade.sound.load_sound("res/sounds/upgrade.wav")
        self.mplayer = pyglet.media.Player()
        for x in range(10):
            self.mplayer.queue(self.sound_theme)
        self.mplayer.play()

        self.game_tick = 30
        self.game_timer = 30
        self.score = 0

    def update(self):
        # Runs each time the window is updated

        self.clear_exits()

        self.check_player_location()

        self.player.sword_ticker()

        if self.player.draw_sword:
            self.sword_collide()

        if self.game_tick == 0:
            if len(self.enemy_list):
                self.enemy_movement()
            self.game_tick = 30
            self.game_timer -= 1
            if self.game_timer <= 0:
                self.end_game()
        else:
            self.game_tick -= 1

    def keypress(self,key):
        # Handles keypresses
        self.player.draw_sword = False

        if key == arcade.key.E:
            print(self.enemy_locations)

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
        # Handles generation of next room
        self.clear = 0
        if self.enemy_locations != None:
            self.game_timer += 2
            self.score += 1
        self.seed = hash_string(self.seed)
        self.tile_data.seed_gen(self.seed, self.from_direction)
        self.enemy_list = self.tile_data.enemy_list
        self.enemy_locations = []
        for enemy in self.tile_data.enemy_list:
            self.enemy_locations.append([enemy.row,enemy.col])
        self.room_coins = 0
        self.total_coins = self.tile_data.return_coins()

    def player_move(self, x_offset=0, y_offset=0):
        # Checks if player movement is possible than moves player to tile or new room
        if self.tile_data.floor_grid[self.player.row + x_offset][self.player.col] > 0:
            if not ([self.player.row + x_offset, self.player.col] in self.enemy_locations):
                self.player.move(self.player.row + x_offset, self.player.col)

        if self.tile_data.floor_grid[self.player.row][self.player.col + y_offset] > 0:
            if not ([self.player.row, self.player.col + y_offset] in self.enemy_locations):
                self.player.move(self.player.row, self.player.col + y_offset)

        if self.player.col == 15:
            self.from_direction = 3
            self.player.col = 1
            self.next_map()

        if self.player.row == 15:
            self.from_direction = 4
            self.player.row = 1
            self.next_map()

        if self.player.col == 0:
            self.from_direction = 1
            self.player.col = 14
            self.next_map()

        if self.player.row == 0:
            self.from_direction = 2
            self.player.row = 14
            self.next_map()
            self.game_timer += 5

    def check_player_location(self):
        # Runs each update, checks players location on surface grid to pickup items
        if self.tile_data.surface_grid[self.player.row][self.player.col]:
            func = self.switch.get(self.tile_data.surface_grid[self.player.row][self.player.col])
            self.tile_data.surface_grid[self.player.row][self.player.col] = 0
            func()

    def enemy_movement(self):
        # Moves all enemies in enemy list, unless they can attack
        self.enemy_locations = []

        for enemy in self.enemy_list:
            if not self.enemy_attack(enemy):
                enemy.move(self.tile_data.floor_grid)
            self.enemy_locations.append([enemy.row,enemy.col])

    def enemy_attack(self, enemy):
        # Enemy deals damage to player each time this is run
        for row in enemy.moves:
            for col in enemy.moves:
                if (self.player.row == enemy.row + row) and (self.player.col == enemy.col + col):
                    self.player.lose_health()
                    if self.player.health < 1:
                        self.end_game()
                    arcade.sound.play_sound(self.sound_hurt)
                    return True

    def coin_pickup(self):
        # Runs upon coin pickup
        arcade.sound.play_sound(self.sound_coin)
        self.player.coins += 1
        self.room_coins += 1

    def clear_exits(self):
        # Allows movement to next room when objectives are complete
        if not self.clear:
            if self.room_coins == self.total_coins and not len(self.enemy_list):
                self.clear = 1
                arcade.sound.play_sound(self.sound_all_coins)
                for row in self.exit_list:
                    for col in self.exit_list:
                        if self.tile_data.floor_grid[row][col] == -1:
                            self.tile_data.floor_grid[row][col] = 1


    def get_score(self):
        # Returns score int
        return self.score

    def get_time(self):
        # Returns time int
        return self.game_timer

    def heart_pickup(self):
        # Handles heart pickup
        self.player.gain_health()
        arcade.sound.play_sound(self.sound_upgrade)

    def max_health_pickup(self):
        # Handles max health pickup, if player already at 10 max health, increases game timer
        if self.player.max_health == 10:
            self.game_timer += 2
        else:
            self.player.max_health_up()
            self.max_health_upgrades += 1
            arcade.sound.play_sound(self.sound_upgrade)

    def speed_pickup(self):
        # Handles speed pickup, allows player to spam keys faster
        # Maybe change to tick system, with keys held down?
        self.player.speed_up()
        self.speed_upgrades += 1
        arcade.sound.play_sound(self.sound_upgrade)

    def enemy_spawn(self):
        # Does nothing if player encounters enemy spawn point
        pass

    def stage_done(self):
        # No usage, maybe remove?
        pass

    def end_game(self):
        # Saves game upon end
        self.mplayer.pause()
        self.player_data.seed = self.seed
        self.player_data.max_speed_upgrades = self.speed_upgrades
        self.player_data.max_health_upgrades = self.max_health_upgrades
        self.player_data.coins += self.player.coins
        self.player_data.score += self.score
        self.player_data.playtime = 1
        self.player_data.save_local_save()
        self.next_stage = True

    def attack(self):
        # Player attack animation
        self.player.draw_sword = True

    def sword_collide(self):
        # Handles sword collision with enemies
        new_list = []
        self.enemy_locations = []
        for enemy in self.enemy_list:
            if enemy.row == (self.player.row - 1 + (2 * self.player.face_right)) and enemy.col == self.player.col:
                enemy.kill()
                arcade.sound.play_sound(self.sound_attack)
                self.game_timer += 2
                if not self.tile_data.surface_grid[enemy.row][enemy.col] == 1:
                    self.tile_data.surface_grid[enemy.row][enemy.col] = 2
            if not enemy.dead:
                self.enemy_locations.append([enemy.row,enemy.col])
                new_list.append(enemy)
        self.enemy_list = new_list


# Locally global functions
def hash_string(str_obj):
    # Generates hash based on seed
    return hashlib.sha256(str_obj.encode()).hexdigest()


