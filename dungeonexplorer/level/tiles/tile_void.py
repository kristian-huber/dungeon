from level.tiles.tile import Tile

class TileVoid(Tile):
    
    def get_type(self):
        return 0

    def get_color(self):
        return (25,25,105)