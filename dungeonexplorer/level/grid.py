from level.tile import TileFloor, TileWall

class Grid:

    def __init__(self, size):
        self._grid = [[None for x in range(size)] for y in range(size)]

    def get_tile_at(self, x, y):
        return self._grid[y][x]

    def set_tile_at(self, x, y, tile):
        self._grid[y][x] = tile

    def place_room(self, room):
        for j in range(room.y, room.y + room.height):
            for i in range(room.x, room.x + room.width):
                self._grid[j][i] = room.get_tile_at(i - room.x, j - room.y)

    def place_hallway(self, hallway):
        for j in range(hallway.y, hallway.y + hallway.height):
            for i in range(hallway.x, hallway.x + hallway.width):

                tile = hallway.get_tile_at(i - hallway.x, j - hallway.y)

                # Don't bother placing anything if it's None
                if tile is not None:
                     # Doesn't matter if we overwrite a None tile
                    if self._grid[j][i] == None:
                        self._grid[j][i] = tile

                    # Prioritize floors over walls. Handles hallway collisions
                    elif self._grid[j][i].get_type() == 2 and tile.get_type() == 1:
                        self._grid[j][i] = tile