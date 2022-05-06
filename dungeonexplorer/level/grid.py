from level.tiles.tile_void import TileVoid

class Grid:

    def __init__(self, size, grid=list()):

        if(len(grid) == 0):
            self._grid = [[TileVoid() for x in range(size)] for y in range(size)]
        else:
            self._grid = grid

    def get_tile_at(self, x, y):
        return self._grid[y][x]
