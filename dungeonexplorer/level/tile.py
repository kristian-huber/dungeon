class Tile:

    def __init__(self):
        pass

    def get_type(self):
        raise NotImplementedError("Please implement this method")

    def get_color(self):
        raise NotImplementedError("Please implement this method")

class TileFloor(Tile):
    def get_type(self):
        return 1

    def get_color(self):
        return (55, 55, 55)

class TileWall(Tile):
    def get_type(self):
        return 2

    def get_color(self):
        return (105, 105, 105)

class TileDoorway(Tile):
    def get_type(self):
        return 3

    def get_color(self):
        return (105, 105, 255)