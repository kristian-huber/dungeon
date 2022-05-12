class Tile:

    def __init__(self):
        pass

    def get_type(self):
        raise NotImplementedError("Please implement this method")

    def get_image(self):
        raise NotImplementedError("Please implement this method")

class TileFloor(Tile):
    def get_type(self):
        return 1

    def get_image(self):
        return 160

class TileWall(Tile):
    def get_type(self):
        return 2

    def get_image(self):
        return 169

class TileStair(Tile):
    def get_type(self):
        return 3

    def get_image(self):
        return 194