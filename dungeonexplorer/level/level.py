from re import S
from level.grid import Grid

class Level:

    def __init__(self):
        self._grid_size = 99
        self._grid = Grid(self._grid_size)

    def get_grid(self):
        return self._grid

    def get_grid_size(self):
        return self._grid_size