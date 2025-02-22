import random
from engine import classEnemy

class TileData:
    """
    Creates tiledata object, basically the grid/maps that define building tiles and surface items/enemies
    """

    def __init__(self):
        self.enemy_list = []
        self.floor_grid = []
        self.surface_grid = []
        self.tile_dict = {
            -1: "spikes",
            0: "wall",
            1: "floor1",
            2: "floor2",
            3: "hole",
            4: "spike"
        }
        self.obj_dict = {
            0: "nothing",
            1: "coin",
            2: "heart",
            3: "max health",
            4: "max speed",
            5: "enemy spawn"
        }


    def seed_gen(self, seed, from_direction = 3):
        """
        Uses seed to randomly generate floor grid and surface grid
        :return:
         none
        """
        self.floor_grid = []
        self.surface_grid = []
        for row in range(16):

            self.floor_grid.append([])
            self.surface_grid.append([])
            for col in range(16):

                self.surface_grid[row].append(0)
                if (row == 0 or row == 15) or (col == 0 or col == 15):
                    self.surface_grid[row].append(0)
                    if (row == 7 or row == 8) or (col == 7 or col == 8):
                        self.floor_grid[row].append(-1)
                    else:
                        self.floor_grid[row].append(0)
                else:
                    self.floor_grid[row].append(1)

        if from_direction == 1:
            self.floor_grid[7][15] = 0
            self.floor_grid[8][15] = 0

        if from_direction == 2:
            self.floor_grid[15][7] = 0
            self.floor_grid[15][8] = 0

        if from_direction == 3:
            self.floor_grid[7][0] = 0
            self.floor_grid[8][0] = 0

        if from_direction == 4:
            self.floor_grid[0][7] = 0
            self.floor_grid[0][8] = 0


        """
        Begin population of the surface map based on game seed
        No real rules, just psuedo-randomness to a max number of items based on hex->int
        """
        max_items = 9
        items = int(seed[0:4], 16) % max_items  # Get num of items to render based on sha
        self.enemy_list = []
        for str_pos in range(items + 1):
            # Get item positions and values based on sha string
            # Items include nothing and enemy spawns in addition to others
            row = (int(seed[str_pos*4:str_pos*4+5], 16) % 13) + 2
            col = (int(seed[str_pos*4+1:str_pos*4+6], 16) % 13) + 2
            item = int(seed[str_pos*4+2:str_pos*4+7], 16) % 6

            if item == 2 or item == 4:
                item = 5

            self.surface_grid[row][col] = item

            if item == 5:
                self.enemy_list.append(classEnemy.Enemy(row, col))

        g_row = (int(seed[str_pos*4:str_pos*4+5], 16) % 13) + 2
        g_col = (int(seed[str_pos*4:str_pos*4+3], 16) % 13) + 2
        self.surface_grid[g_row][g_col] = 1

    def if_collide(self, row, col):
        """
        checks if tile has collision
        :param
        collide_tiles: list of tiles with collision
        floor_grid: map of floor/wall tiles
        :return: bool
        """
        return not self.floor_grid[row][col]

    def print_grid(self, grid):
        """
        test function to print grids
        :param grid: 2d list of ints
        :return: none
        """

        for row in range(len(grid)):
            for col in range(len(grid)):
                print(grid[row][col], end=" ")
            print("")

    def return_coins(self):
        sum = 0
        for row in self.surface_grid:
            for i in row:
                if i == 1:
                    sum += 1
        return sum


'''
#Test
world = TileData()
world.seed_gen()
world.print_grid(world.floor_grid)
print("next")
world.print_grid(world.surface_grid)
'''