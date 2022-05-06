from gfx.graphics import *
from level.level import Level

level = Level()
level.generate_level()

set_level(level)
start()