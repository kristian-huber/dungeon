from gfx.sprite_lookup_table import DungeonExplorerSprites

"""
Base Class
"""
class Tile:
    def __init__(self):
        pass

    def get_type(self):
        raise NotImplementedError("Please implement this method")

    def get_texture(self):
        raise NotImplementedError("Please implement this method")

"""
Classes custom to dungeon explorer
"""

class TileFloor(Tile):
    def get_type(self):
        return 1

    def get_texture(self):
        return DungeonExplorerSprites.TEXTURE_FLOOR

class TileWall(Tile):
    def __init__(self, texture=DungeonExplorerSprites.TEXTURE_WALL_BACK):
        self._texture = texture

    def get_type(self):
        return 2

    def get_texture(self):
        return self._texture

class TileStair(Tile):
    def get_type(self):
        return 3

    def get_texture(self):
        return DungeonExplorerSprites.TEXTURE_STAIRS