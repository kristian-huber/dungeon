import pyglet
from pyglet import shapes
from pyglet.window import key

#Pyglet variables
window = pyglet.window.Window(384, 480)
batch = pyglet.graphics.Batch()

# Level Variables
_sprite_lookup_table = None
_tiles = list()
_display_multiplier = 24

def start():
    pyglet.app.run()

@window.event
def on_draw():
    window.clear()
    batch.draw()

@window.event
def on_mouse_press(x, y, button, modifiers):
    print("id=", ((y // 24) * 16 + (x // 24)))

def set_sprite_lookup_table(table):
    global _sprite_lookup_table
    _sprite_lookup_table = table

def add_tiles(h, w):
    global _tiles

    _tiles = list()

    for j in range(h):
        for i in range(w):

            tile_id = (w * j) + i

            rect = pyglet.sprite.Sprite(img=_sprite_lookup_table._sprite_images[tile_id], batch=batch)
            rect.x = i * _display_multiplier
            rect.y = j * _display_multiplier
            rect.scale = 1.5

            _tiles.append(rect)
