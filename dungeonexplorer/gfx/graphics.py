import pyglet
from pyglet import shapes
from pyglet.window import key

#Pyglet variables
window = pyglet.window.Window(495, 495)
batch = pyglet.graphics.Batch()
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Level Variables
_level = None
_display_multiplier = 5
_tiles = list()
_lines = list()

def start():
    pyglet.app.run()

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_key_release(symbol, modifiers):
    global _level

    if keys[key.SPACE]:
        print('Regenerating Level')
        _level.generate_level()
        set_level(_level)

def set_display_multiplier(multiplier):
    global _display_multiplier
    _display_multiplier = multiplier

def set_level(level):
    global _level
    global _display_multiplier
    global _tiles
    global _lines

    _level = level
    _tiles = list()
    _lines = list()

    for j in range(level.get_grid_size()):
        for i in range(level.get_grid_size()):

            tile = _level.get_grid().get_tile_at(i,j)
            
            if tile is None:
                continue

            rect = shapes.Rectangle(
                i * _display_multiplier, j * _display_multiplier,
                _display_multiplier, _display_multiplier,
                tile.get_color(),
                batch=batch
            )
            _tiles.append(rect)

    for edge in level._graph._edges:
        line = shapes.Line(
                edge.src.centerX * _display_multiplier, edge.src.centerY * _display_multiplier,
                edge.dest.centerX * _display_multiplier, edge.dest.centerY * _display_multiplier,
                1,
                color=(255, 0, 0),
                batch=batch
        )
        _lines.append(line)
