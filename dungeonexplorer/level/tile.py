from gfx.sprite_lookup_table import TEXTURE_FLOOR, TEXTURE_STAIRS, TEXTURE_WALL

class Tile:
    def __init__(self):
        pass

    def get_type(self):
        raise NotImplementedError("Please implement this method")

    def get_texture(self):
        raise NotImplementedError("Please implement this method")

class TileFloor(Tile):
    def get_type(self):
        return 1

    def get_texture(self):
        return TEXTURE_FLOOR

class TileWall(Tile):
    def get_type(self):
        return 2

    def get_texture(self):
        return TEXTURE_WALL

class TileStair(Tile):
    def get_type(self):
        return 3

    def get_texture(self):
        return TEXTURE_STAIRS