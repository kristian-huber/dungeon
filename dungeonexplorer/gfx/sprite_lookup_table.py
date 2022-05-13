from pyglet.image import load, ImageGrid

"""
Base Class
"""
class SpriteLookupTable:
    def __init__(self, image_name, rows, cols):
        self._sprite_sheet = load(image_name)
        self._sprite_images = ImageGrid(self._sprite_sheet, rows, cols)
        self._lookup_table = dict()

    def add_entry(self, texture_name, texture_id):
        self._lookup_table[texture_name] = texture_id

    def get_texture(self, texture_name):
        return self._sprite_images[self._lookup_table[texture_name]]

"""
Specific to dungeon explorer
"""

class DungeonExplorerSprites(SpriteLookupTable):
    
    TEXTURE_FLOOR = "floor"
    TEXTURE_WALL_BACK = "wall_back"
    TEXTURE_WALL_LEFT = "wall_left"
    TEXTURE_WALL_RIGHT = "wall_right"
    TEXTURE_STAIRS = "stairs"

    def __init__(self):
        super().__init__("assets/textures/cave.png", 20, 16)

        self.add_entry(DungeonExplorerSprites.TEXTURE_FLOOR, 160)
        self.add_entry(DungeonExplorerSprites.TEXTURE_WALL_BACK, 206)
        self.add_entry(DungeonExplorerSprites.TEXTURE_WALL_LEFT, 317)
        self.add_entry(DungeonExplorerSprites.TEXTURE_WALL_RIGHT, 319)
        self.add_entry(DungeonExplorerSprites.TEXTURE_STAIRS, 194)