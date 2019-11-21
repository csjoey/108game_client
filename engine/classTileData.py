import random

class TileData():

    def __init__(self):
        self.floor_grid = []
        self.surface_grid = []
        self.tile_dict = {
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

    def seed_gen(self):
        """
        Uses seed to randomly generate floor grid and surface grid
        :return: none
        """
        for row in range(16):
            self.floor_grid.append([])
            self.surface_grid.append([])
            for col in range(16):
                if (row == 0 or row == 15) or (col == 0 or col == 15):
                    self.surface_grid[row].append(0)
                    if (row == 7 or row == 8) or (col == 7 or col == 8):
                        self.floor_grid[row].append(1)
                    else:
                        self.floor_grid[row].append(0)
                else:
                    self.floor_grid[row].append(1)
                    if random.randint(0,10) == 7:
                        self.surface_grid[row].append(random.randint(1,4))
                    else:
                        self.surface_grid[row].append(0)
#                floor_grid[row].append(get_ftile())
#                surface_grid[row].append(get_stile())

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
        return None


#Test
world = TileData()
world.seed_gen()
world.print_grid(world.floor_grid)
print("next")
world.print_grid(world.surface_grid)