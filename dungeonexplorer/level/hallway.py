from level.tile import TileFloor, TileDoorway, TileWall

class Hallway:

    def __init__(self, room_a, room_b):
        self._populate_grid(room_a, room_b)

    def _populate_grid(self, room_a, room_b):
        direction, coord, src, dest = self._is_overlap(room_a, room_b)

        if direction == 'x':
            #Go from Y to Y
            if src.centerY > dest.centerY:
                for i in range(dest.y + dest.height - 1, src.y + 1):
                    self._place_horizontal_wall_segment(i, coord)
            else:
                for i in range(src.y + src.height - 1, dest.y + 1):
                    self._place_horizontal_wall_segment(i, coord)
        elif direction == 'y':
            #Go from X to X
            if src.centerX > dest.centerX:
                for i in range(dest.x + dest.width - 1, src.x + 1):
                    self._place_vertical_wall_segment(coord, i)
            else:
                for i in range(src.x + src.width - 1, dest.x+ 1):
                    self._place_vertical_wall_segment(coord, i)
        else:
            if src.centerX > dest.centerX and src.centerY > dest.centerY:
                # draw a line from the left of src to the center of dest
                for i in range(dest.centerX, src.x + 1):
                    self._place_vertical_wall_segment(src.centerY, i)
                # draw a line from that point down to dest
                for i in range(dest.y + dest.height - 1, src.centerY):
                    self._place_horizontal_wall_segment(i, dest.centerX)

                self._fix_corner(src.centerY, dest.centerX)

            if src.centerX < dest.centerX and src.centerY < dest.centerY:
                # draw a line right from src to center of dest
                for i in range(src.x + src.width - 1, dest.centerX):
                    self._place_vertical_wall_segment(src.centerY, i)

                # draw a line from that point up to the bottom of the dest room
                for i in range(src.centerY, dest.y + 1):
                    self._place_horizontal_wall_segment(i, dest.centerX)

                self._fix_corner(src.centerY, dest.centerX)
            
            if src.centerX > dest.centerX and src.centerY < dest.centerY:
                # draw a line up from src to the mid of dest
                for i in range(src.y + src.height - 1, dest.centerY):
                    self._place_horizontal_wall_segment(i, src.centerX)

                # draw a line from that point to the left of dest
                for i in range(dest.x + dest.width - 1, src.centerX):
                    self._place_vertical_wall_segment(dest.centerY, i)

                self._fix_corner(dest.centerY, src.centerX)

            if src.centerX < dest.centerX and src.centerY > dest.centerY:
                # draw a line from the right
                for i in range(src.x + src.width - 1, dest.centerX):
                    self._place_vertical_wall_segment(src.centerY, i)

                # draw a line down
                for i in range(dest.y + dest.height - 1, src.centerY):
                    self._place_horizontal_wall_segment(i, dest.centerX)

                self._fix_corner(src.centerY, dest.centerX)

    def _place_vertical_wall_segment(self, y, x):
        if self._grid[y - 1][x] is None:
            self._grid[y - 1][x] = TileWall()
        
        self._grid[y][x] = TileFloor()

        if self._grid[y + 1][x] is None:
            self._grid[y + 1][x] = TileWall()

    def _place_horizontal_wall_segment(self, y, x):
        if self._grid[y][x - 1] is None:
            self._grid[y][x - 1] = TileWall()

        self._grid[y][x] = TileFloor()

        if self._grid[y][x + 1] is None:
            self._grid[y][x + 1] = TileWall()

    def _fix_corner(self, y, x):
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if i == x and j == y:
                    self._grid[j][i] = TileFloor()
                elif self._grid[j][i] == None or self._grid[j][i].get_type() == 0:
                    self._grid[j][i] = TileWall()

    def _is_overlap(self, room_a, room_b):
    
        src, dest = room_a, room_b

        # Y overlap
        start_a, end_a = room_a.y + 1, room_a.y + room_a.height - 2
        start_b, end_b = room_b.y + 1, room_b.y + room_b.height - 2
        
        if start_a <= end_b and end_a >= start_b:
            if room_a.centerY < room_b.centerY:
                src, dest = room_a, room_b
            else:
                src, dest = room_b, room_a

            midpoint = self._clamp(
                src.centerY + (dest.centerY - src.centerY) // 2,
                src.y + 1,
                dest.y + dest.height - 2
            )
            return ('y', midpoint, src, dest)

        # X overlap
        start_a, end_a = room_a.x + 1, room_a.x + room_a.width - 2
        start_b, end_b = room_b.x + 1, room_b.x + room_b.width - 2

        if start_a <= end_b and end_a >= start_b:
            if room_a.centerX < room_b.centerX:
                src, dest = room_a, room_b
            else:
                src, dest = room_b, room_a

            midpoint = self._clamp(
                src.centerX + (dest.centerX - src.centerX) // 2,
                src.x + 1,
                dest.x + dest.width - 2
            )
            return ('x', midpoint, src, dest)

        return ('no overlap', -1, src, dest)

    def _clamp(self, val, min, max):
        if val < min:
            return min
        elif val > max:
            return max
        return val

    def get_tile_at(self, x, y):
        return self._grid[y][x]