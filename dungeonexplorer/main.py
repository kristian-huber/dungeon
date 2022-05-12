from gfx.graphics import set_level, start, set_sprite_lookup_table
from gfx.sprite_lookup_table import DungeonExplorerSprites
from level.level import Level

sprite_lookup_table = DungeonExplorerSprites()
set_sprite_lookup_table(sprite_lookup_table)

level = Level()
level.generate_level()
set_level(level)

start()