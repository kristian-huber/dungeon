from pyglet.image import load, ImageGrid

class SpriteLookupTable:

    def __init__(self, image_name, rows, cols):
        self._sprite_sheet = load(image_name)
        self._sprite_images = ImageGrid(self._sprite_sheet, rows, cols)
        self._lookup_table = dict()

    def add_entry(self, texture_name, texture_id):
        self._lookup_table[texture_name] = texture_id

    def get_texture(self, texture_name):
        return self._sprite_images[self._lookup_table[texture_name]]

TEXTURE_FLOOR = "floor"
TEXTURE_WALL = "wall"
TEXTURE_STAIRS = "stairs"

class DungeonExplorerSprites(SpriteLookupTable):

    def __init__(self):
        super().__init__("assets/textures/cave.png", 20, 16)

        self.add_entry(TEXTURE_FLOOR, 160)
        self.add_entry(TEXTURE_WALL, 169)
        self.add_entry(TEXTURE_STAIRS, 194)