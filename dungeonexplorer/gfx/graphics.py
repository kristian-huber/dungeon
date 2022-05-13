import pyglet
from pyglet import shapes
from pyglet.window import key

#Pyglet variables
window = pyglet.window.Window(495, 495)
batch = pyglet.graphics.Batch()
keys = key.KeyStateHandler()
window.push_handlers(keys)

# Level Variables
_sprite_lookup_table = None
_level = None
_display_multiplier = 24
_tiles = list()

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

def set_sprite_lookup_table(table):
    global _sprite_lookup_table
    _sprite_lookup_table = table

def set_level(level):
    global _level
    global _display_multiplier
    global _tiles
    global _sprite_lookup_table

    _level = level
    _tiles = list()

    for j in range(level.get_grid_size()):
        for i in range(level.get_grid_size()):

            tile = _level.get_grid().get_tile_at(i,j)
            
            if tile is None:
                continue
            
            rect = pyglet.sprite.Sprite(img=_sprite_lookup_table.get_texture(tile.get_texture()), batch=batch)
            rect.x = i * _display_multiplier
            rect.y = j * _display_multiplier
            rect.scale = 1.5

            _tiles.append(rect)
