import pyglet
from pyglet import shapes
from pyglet.window import key

#Pyglet variables
window = pyglet.window.Window(495, 495)
batch = pyglet.graphics.Batch()
keys = key.KeyStateHandler()
window.push_handlers(keys)

_sprite_sheet = pyglet.image.load('assets/textures/sewer.png')
_sprite_images = pyglet.image.ImageGrid(_sprite_sheet, 22, 16)

_scroll_x = 0
_scroll_y = 0

# Level Variables
_level = None
_display_multiplier = 16
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
    global _scroll_x
    global _scroll_y

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
    global _sprite_images

    _level = level
    _tiles = list()

    for j in range(level.get_grid_size()):
        for i in range(level.get_grid_size()):

            tile = _level.get_grid().get_tile_at(i,j)
            
            if tile is None:
                continue
            
            rect = pyglet.sprite.Sprite(img=_sprite_images[tile.get_image()], batch=batch)
            rect.x = i * _display_multiplier
            rect.y = j * _display_multiplier

            _tiles.append(rect)
