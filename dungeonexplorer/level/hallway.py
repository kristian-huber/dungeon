from level.tile import TileFloor, TileWall

class Hallway:

    def __init__(self, room_a, room_b):
        self._populate_grid(room_a, room_b)

    def _populate_grid(self, room_a, room_b):
        direction, midpoint, src, dest = self._is_overlap(room_a, room_b)

        if direction == 'x':
            # Organize src and dest by y
            if src.y > dest.y:
                src, dest = dest, src

            # Go from Y to Y
            grid_height = (dest.y + 1) - (src.y + src.height - 1)

            self.x = midpoint - 1
            self.y = src.y + src.height - 1
            self.width = 3
            self.height = grid_height
            self._grid = [[None for x in range(3)] for y in range(grid_height)]

            for i in range(grid_height):
                self._place_horizontal_wall_segment(i, 1)

        elif direction == 'y':
            # Organize src and dest by x
            if src.x > dest.x:
                src, dest = dest, src

            # Go from X to X
            grid_width = (dest.x + 1) - (src.x + src.width - 1)

            self.x = src.x + src.width - 1
            self.y = midpoint - 1
            self.width = grid_width
            self.height = 3
            self._grid = [[None for x in range(grid_width)] for y in range(3)]

            for i in range(grid_width):
                self._place_vertical_wall_segment(1, i)

        else:
            # Only two cases because src.y is smaller
            if src.centerX < dest.centerX:
                self.x = src.centerX - 1
                self.y = src.y + src.height - 1
                self.width = dest.x + 1 - self.x
                self.height = dest.centerY + 1 - self.y
                self._grid = [[None for x in range(self.width)] for y in range(self.height)]
                
                # Draw a line up
                for i in range(self.height - 1):
                    self._place_horizontal_wall_segment(i, 1) 

                 # Draw a line from there to the right
                for i in range(1, self.width):
                    self._place_vertical_wall_segment(self.height - 2, i)

                self._fix_corner(self.height - 2, 1)

            else:
                self.x = dest.x + dest.width - 1
                self.y = src.y + src.height - 1
                self.width = src.centerX + 1 - self.x
                self.height = dest.centerY + 1 - self.y
                self._grid = [[None for x in range(self.width)] for y in range(self.height)]

                # Draw a line up
                for i in range(self.height - 1):
                    self._place_horizontal_wall_segment(i, self.width - 2)

                # Draw a line from there to the left
                for i in range(0, self.width - 1):
                    self._place_vertical_wall_segment(self.height - 2, i)

                self._fix_corner(self.height - 2, self.width - 2)

    def _place_vertical_wall_segment(self, y, x):
        if(self._grid[y - 1][x] == None):
            self._grid[y - 1][x] = TileWall()

        self._grid[y][x] = TileFloor()

        if(self._grid[y + 1][x] == None):
            self._grid[y + 1][x] = TileWall()

    def _place_horizontal_wall_segment(self, y, x):
        if(self._grid[y][x - 1] == None):
            self._grid[y][x - 1] = TileWall()

        self._grid[y][x] = TileFloor()

        if(self._grid[y][x + 1] == None):
            self._grid[y][x + 1] = TileWall()

    def _fix_corner(self, y, x):
        for j in range(y - 1, y + 2):
            for i in range(x - 1, x + 2):
                if i == x and j == y:
                    self._grid[j][i] = TileFloor()
                elif self._grid[j][i] == None:
                    self._grid[j][i] = TileWall()

    def _is_overlap(self, room_a, room_b):
    
        src, dest = None, None

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
                dest.y + 1,
                src.y + src.height - 2
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
                dest.x + 1,
                src.x + src.width - 2
            )
            return ('x', midpoint, src, dest)

        # Guarantee that src centerY is less
        src = room_a if room_a.centerY < room_b.y else room_b
        dest = room_a if room_a.centerY > room_b.y else room_b

        return ('no overlap', -1, src, dest)

    def _clamp(self, val, min, max):
        if val < min:
            return min
        elif val > max:
            return max
        return val

    def get_tile_at(self, x, y):
        return self._grid[y][x]