from level.tiles.tile import Tile

class TileFloor(Tile):

    def get_type(self):
        return 1

    def get_color(self):
        return (155, 105, 25)