from level.tile import TileFloor, TileWall

class Grid:

    def __init__(self, size, grid=list()):

        if(len(grid) == 0):
            self._grid = [[None for x in range(size)] for y in range(size)]
        else:
            self._grid = grid

    def get_tile_at(self, x, y):
        return self._grid[y][x]

    def place_room(self, room):
        for j in range(room.y, room.y + room.height):
            for i in range(room.x, room.x + room.width):
                if i == room.x or i == room.x + room.width - 1 or j == room.y or j == room.y + room.height - 1:
                    self._grid[j][i] = TileWall()
                else:
                    self._grid[j][i] = TileFloor()