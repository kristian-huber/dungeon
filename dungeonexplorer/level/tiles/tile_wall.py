from level.tiles.tile import Tile

class TileWall(Tile):

    def get_type(self):
        return 2

    def get_color(self):
        return (25, 155, 25)