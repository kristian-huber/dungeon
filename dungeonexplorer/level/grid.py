import re
from level.tile import TileFloor, TileWall

class Grid:

    def __init__(self, size, grid=list()):

        if(len(grid) == 0):
            self._grid = [[None for x in range(size)] for y in range(size)]
        else:
            self._grid = grid

    def get_tile_at(self, x, y):
        return self._grid[y][x]

    def place_room(self, room):
        for j in range(room.y, room.y + room.height):
            for i in range(room.x, room.x + room.width):
                self._grid[j][i] = room.get_tile_at(i - room.x, j - room.y)

    def place_hallway(self, edge):
        direction, coord = self._is_overlap(edge.src, edge.dest)

        if direction == 'x':
            #Go from Y to Y
            if edge.src.centerY > edge.dest.centerY:
                for i in range(edge.dest.y + edge.dest.height - 1, edge.src.y + 1):
                    self._grid[i][coord - 1] = TileWall()
                    self._grid[i][coord] = TileFloor()
                    self._grid[i][coord + 1] = TileWall()
            else:
                for i in range(edge.src.y + edge.src.height - 1, edge.dest.y + 1):
                    self._grid[i][coord - 1] = TileWall()
                    self._grid[i][coord] = TileFloor()
                    self._grid[i][coord + 1] = TileWall()
        elif direction == 'y':
            #Go from X to X
            if edge.src.centerX > edge.dest.centerX:
                for i in range(edge.dest.x + edge.dest.width - 1, edge.src.x + 1):
                    self._grid[coord - 1][i] = TileWall()
                    self._grid[coord][i] = TileFloor()
                    self._grid[coord + 1][i] = TileWall()
            else:
                for i in range(edge.src.x + edge.src.width - 1, edge.dest.x+ 1):
                    self._grid[coord - 1][i] = TileWall()
                    self._grid[coord][i] = TileFloor()
                    self._grid[coord + 1][i] = TileWall()
        else:
            pass

    def _is_overlap(self, src, dest):

        # X overlap
        startA = src.x + 1
        startB = dest.x + 1
        endA = src.x + src.width - 2
        endB = dest.x + dest.width - 2

        if startA <= endB and endA >= startB:
            midpoint = -1
            if(src.centerX > dest.centerX):
                midpoint = self._clamp(
                    dest.centerX + (src.centerX - dest.centerX) // 2,
                    src.x + 1,
                    dest.x + dest.width - 2
                )
            else:
                midpoint = self._clamp(
                    src.centerX + (dest.centerX - src.centerX) // 2,
                    dest.x + 1,
                    src.x + src.width - 2
                )
            return ('x', midpoint)

        # Y overlap
        startA = src.y + 1
        startB = dest.y + 1
        endA = src.y + src.height - 2
        endB = dest.y + dest.height - 2
        
        if startA <= endB and endA >= startB:
            midpoint = -1
            if(src.centerY > dest.centerY):
                midpoint = self._clamp(
                    dest.centerY + (src.centerY - dest.centerY) // 2,
                    src.y + 1,
                    dest.y + dest.height - 2
                )
            else:
                midpoint = self._clamp(
                    src.centerY + (dest.centerY - src.centerY) // 2,
                    dest.y + 1,
                    src.y + src.height - 2
                )
            return ('y', midpoint)

        return ('no overlap', -1)

    def _clamp(self, val, min, max):
        if val < min:
            return min
        elif val > max:
            return max
        return val