import json
class PlayerData:
    """
    Class for the storage and retrieval of player saves
    """
    def __init__(self):
        self.seed = None
        self.max_health_upgrades = None
        self.max_speed_upgrades = None
        self.coins = None
        self.score = None
        self.playtime = None

    def load_local_save(self):

        try:
            with open("savegame/data_file.json", "r") as read_file:
                data = json.load(read_file)
                self.seed = data['save_game']['seed']
                self.max_health_upgrades = data['save_game']["max_health_upgrades"]
                self.max_speed_upgrades = data['save_game']["max_speed_upgrades"]
                self.coins = data['save_game']["coins"]
                self.score = data['save_game']['score']
                self.playtime = data['save_game']["playtime"]
        except:
            self.blank_save()
            self.save_local_save()
            self.load_local_save()

    def save_local_save(self):
        data = {
            "save_game": {
                "seed": self.seed,
                "max_health_upgrades": self.max_health_upgrades,
                "max_speed_upgrades": self.max_speed_upgrades,
                "coins": self.coins,
                "score": self.score,
                "playtime": self.playtime
            }
        }
        with open("savegame/data_file.json", "w") as write_file:
            json.dump(data, write_file)

    def blank_save(self):
        self.seed = input("Input Seed for New Game:")
        self.max_health_upgrades = 0
        self.max_speed_upgrades = 0
        self.coins = 0
        self.score = 0
        self.playtime = 0