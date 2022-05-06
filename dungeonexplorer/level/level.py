from level.grid import Grid
from level.room import Room

class Level:

    def __init__(self):
        self._min_room_size = 5
        self._max_room_size = 11
        self._grid_size = 99
        self._room_attempts = 33

        self._grid = Grid(self._grid_size)
        self._rooms = list()

    def generate_level(self):
        self._generate_rooms()

    def _generate_rooms(self):
        for i in range(self._room_attempts):
            room = Room(
                randomize=True, 
                min_room_size=self._min_room_size, 
                max_room_size=self._max_room_size, 
                map_max = self._grid_size
            )
            
            intersects = False
            for room2 in self._rooms:
                if(room.intersects(room2)):
                    intersects = True
                    break

            if not intersects:
                self._rooms.append(room)
                self._grid.place_room(room)

    def get_grid(self):
        return self._grid

    def get_grid_size(self):
        return self._grid_size