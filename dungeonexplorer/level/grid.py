from level.tile import TileDoorway, TileFloor, TileWall

class Grid:

    def __init__(self, size):
        self._grid = [[None for x in range(size)] for y in range(size)]
        self._room_tiles = dict()

    def get_tile_at(self, x, y):
        return self._grid[y][x]

    def place_room(self, room):
        for j in range(room.y, room.y + room.height):
            for i in range(room.x, room.x + room.width):
                
                tile = room.get_tile_at(i - room.x, j - room.y)
                
                self._grid[j][i] = tile

                if tile.get_type() == 2:
                    coord = (i, j)
                    self._room_tiles[coord] = room

    def place_hallway(self, edge):
        direction, coord = self._is_overlap(edge.src, edge.dest)

        if direction == 'x':
            #Go from Y to Y
            if edge.src.centerY > edge.dest.centerY:
                for i in range(edge.dest.y + edge.dest.height - 1, edge.src.y + 1):
                    self._place_horizontal_wall_segment(i, coord)
            else:
                for i in range(edge.src.y + edge.src.height - 1, edge.dest.y + 1):
                    self._place_horizontal_wall_segment(i, coord)
        elif direction == 'y':
            #Go from X to X
            if edge.src.centerX > edge.dest.centerX:
                for i in range(edge.dest.x + edge.dest.width - 1, edge.src.x + 1):
                    self._place_vertical_wall_segment(coord, i)
            else:
                for i in range(edge.src.x + edge.src.width - 1, edge.dest.x+ 1):
                    self._place_vertical_wall_segment(coord, i)
        else:
            if edge.src.centerX > edge.dest.centerX and edge.src.centerY > edge.dest.centerY:
                # draw a line from the left of src to the center of dest
                for i in range(edge.dest.centerX, edge.src.x + 1):
                    self._place_vertical_wall_segment(edge.src.centerY, i)
                # draw a line from that point down to dest
                for i in range(edge.dest.y + edge.dest.height - 1, edge.src.centerY):
                    self._place_horizontal_wall_segment(i, edge.dest.centerX)

                self._fix_corner(edge.src.centerY, edge.dest.centerX)

            if edge.src.centerX < edge.dest.centerX and edge.src.centerY < edge.dest.centerY:
                # draw a line right from src to center of dest
                for i in range(edge.src.x + edge.src.width - 1, edge.dest.centerX):
                    self._place_vertical_wall_segment(edge.src.centerY, i)

                # draw a line from that point up to the bottom of the dest room
                for i in range(edge.src.centerY, edge.dest.y + 1):
                    self._place_horizontal_wall_segment(i, edge.dest.centerX)

                self._fix_corner(edge.dest.centerY, edge.src.centerX)
            
            if edge.src.centerX > edge.dest.centerX and edge.src.centerY < edge.dest.centerY:
                # draw a line up from src to the mid of dest
                for i in range(edge.src.y + edge.src.height - 1, edge.dest.centerY):
                    self._place_horizontal_wall_segment(i, edge.src.centerX)

                # draw a line from that point to the left of dest
                for i in range(edge.dest.x + edge.dest.width - 1, edge.src.centerX):
                    self._place_vertical_wall_segment(edge.dest.centerY, i)

                self._fix_corner(edge.dest.centerY, edge.src.centerX)

            if edge.src.centerX < edge.dest.centerX and edge.src.centerY > edge.dest.centerY:
                # draw a line from the right
                for i in range(edge.src.x + edge.src.width - 1, edge.dest.centerX):
                    self._place_vertical_wall_segment(edge.src.centerY, i)

                # draw a line down
                for i in range(edge.dest.y + edge.dest.height - 1, edge.src.centerY):
                    self._place_horizontal_wall_segment(i, edge.dest.centerX)

                self._fix_corner(edge.src.centerY, edge.dest.centerX)

    def _place_vertical_wall_segment(self, y, x):
        if self._grid[y - 1][x] is None:
            self._grid[y - 1][x] = TileWall()
        
        if self._is_room_tile(y, x):
            self._grid[y][x] = TileDoorway()
            coord = (x, y)
            room = self._room_tiles[coord]
            room.set_entry_point(x - room.x, y - room.y)
        else:
            self._grid[y][x] = TileFloor()

        if self._grid[y + 1][x] is None:
            self._grid[y + 1][x] = TileWall()

    def _place_horizontal_wall_segment(self, y, x):
        if self._grid[y][x - 1] is None:
            self._grid[y][x - 1] = TileWall()
        
        if self._is_room_tile(y, x):
            self._grid[y][x] = TileDoorway()
            coord = (x, y)
            room = self._room_tiles[coord]
            room.set_entry_point(x - room.x, y - room.y)
        else:
            self._grid[y][x] = TileFloor()

        if self._grid[y][x + 1] is None:
            self._grid[y][x + 1] = TileWall()

    def _fix_corner(self, y, x):
        pass

    def _is_room_tile(self, y, x):
        coord = (x, y)
        return self._room_tiles.__contains__(coord)

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