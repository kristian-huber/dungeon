from level.grid import Grid
from level.room import Room
from level.graph import Graph

class Level:

    def __init__(self, min_room_size=7, max_room_size=13, grid_size=99, room_attempts=50):
        self._min_room_size = min_room_size
        self._max_room_size = max_room_size
        self._grid_size = grid_size
        self._room_attempts = room_attempts

    def generate_level(self):
        self._grid = Grid(self._grid_size)
        self._rooms = list()
        self._graph = Graph()

        self._generate_rooms()

        self._graph.complete_graph()
        self._graph = self._graph.create_min_spanning_tree()

        self._generate_hallways()

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
                self._graph.add_vertex(room)

    def _generate_hallways(self):

        in_graph = list()

        for edge in self._graph._edges:
            if((edge.dest, edge.src) not in in_graph):
                self._grid.place_hallway(edge)
                in_graph.append((edge.src, edge.dest))

    def get_grid(self):
        return self._grid

    def get_grid_size(self):
        return self._grid_size