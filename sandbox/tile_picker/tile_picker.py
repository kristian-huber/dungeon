from sandbox.tile_picker.window import set_sprite_lookup_table, add_tiles, start
from dungeonexplorer.gfx.sprite_lookup_table import SpriteLookupTable

custom = SpriteLookupTable("assets/textures/cave.png", 20, 16)
set_sprite_lookup_table(custom)

add_tiles(20, 16)

start()