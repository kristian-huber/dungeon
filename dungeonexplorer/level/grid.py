from level.tile import TileDoorway, TileFloor, TileWall

class Grid:

    def __init__(self, size):
        self._grid = [[None for x in range(size)] for y in range(size)]
        self._room_tiles = dict()

    def set_tile_at(self, x, y, tile):
        self._grid[y][x] = tile

    def get_tile_at(self, x, y):
        return self._grid[y][x]

    def place_room(self, room):
        for j in range(room.y, room.y + room.height):
            for i in range(room.x, room.x + room.width):
                
                tile = room.get_tile_at(i - room.x, j - room.y)
                
                self._grid[j][i] = tile

                if tile.get_type() == 2:
                    coord = (i, j)
                    self._room_tiles[coord] = room

    def place_hallway(self, hallway):
        for j in range(hallway.y, hallway.y + hallway.height):
            for i in range(hallway.x, hallway.x + hallway.width):

                tile = hallway.get_tile_at(i - hallway.x, j - hallway.y)

                if tile is not None:
                    self._grid[j][i] = tile