from gfx.graphics import set_level, start
from level.level import Level

level = Level()
level.generate_level()

set_level(level)
start()