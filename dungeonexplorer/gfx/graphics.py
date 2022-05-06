import pyglet
from pyglet import shapes
from pyglet.window import key

#Pyglet variables
window = pyglet.window.Window(495, 495)
batch = pyglet.graphics.Batch()

# Level Variables
_level = None
_display_multiplier = 5
_tiles = list()

def start():
    pyglet.app.run()

@window.event
def on_draw():
    window.clear()
    batch.draw()

def set_display_multiplier(multiplier):
    global _display_multiplier
    _display_multiplier = multiplier

def set_level(level):
    global _level
    global _display_multiplier
    global _tiles

    _level = level
    _tiles = list()

    for j in range(level.get_grid_size()):
        for i in range(level.get_grid_size()):

            tile = shapes.Rectangle(
                i * _display_multiplier, j * _display_multiplier,
                _display_multiplier, _display_multiplier,
                _level.get_grid().get_tile_at(i,j).get_color(),
                batch=batch
            )
            _tiles.append(tile)
