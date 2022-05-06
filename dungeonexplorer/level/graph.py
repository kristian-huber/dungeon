import bisect

class Vertex:
    def __init__(self, val):
        self.val = val

class Edge:
    def __init__(self, src, dest, weight):
        self.src = src
        self.dest = dest
        self.weight = weight

    def __eq__(self, other):
        if other is None:
            return False
        return self.src == other.src and self.dest == other.dest and self.weight == other.weight

    def __lt__(self, other):
        return self.weight < other.weight

    def __le__(self, other):
        return self.weight <= other.weight

    def __gt__(self, other):
        return self.weight > other.weight

    def __ge__(self, other):
        return self.weight >= other.weight

class Graph:

    def __init__(self):
        self._adjacency_list = dict()
        self._edges = list()
        self._vertices = 0

    def add_vertex(self, vertex):
        self._adjacency_list[vertex] = list()
        self._vertices = self._vertices + 1

    def add_edge(self, edge):
        self._adjacency_list[edge.src].append(edge)
        self._insert_edge(edge)

        edge2 = Edge(edge.dest, edge.src, edge.weight)
        self._adjacency_list[edge.dest].append(edge2)
        self._insert_edge(edge2)

    def remove_edge(self, edge):
        edge2 = Edge(edge.dest, edge.src, edge.weight)

        self._edges.remove(edge)
        self._adjacency_list[edge.src].remove(edge)

        self._edges.remove(edge2)
        self._adjacency_list[edge.dest].remove(edge2)

    def complete_graph(self):

        vertices = list()
        
        for key in self._adjacency_list.keys():
            vertices.append(key)

        for i in range(0, len(vertices) - 1):
            src = vertices[i]

            for j in range(1, len(vertices)):
                dest = vertices[j]

                weight = abs(src.centerX - dest.centerX) + abs(src.centerY - dest.centerY)
                
                self.add_edge(Edge(src, dest, weight))

    def create_min_spanning_tree(self):

        graph = Graph()

        # Add all of the vertices to it
        for vertex in self._adjacency_list.keys():
            graph.add_vertex(vertex)

        # Sort the list of _edges (already in sorted order)

        # Repeat until all of the vertices are in the tree
        count = 0
        edgeCount = 0

        while edgeCount < self._vertices - 1:

            # Remove the smallest one that doesn't make a cycle
            currentEdge = self._edges[count]
            graph.add_edge(currentEdge)

            hasCycle = graph._is_cyclic(graph)

            if hasCycle:
                graph.remove_edge(currentEdge)
            else:
                edgeCount = edgeCount + 1

            count = count + 1

        return graph

    def _insert_edge(self, edge):
        bisect.insort(self._edges, edge)

    def _is_cyclic(self, graph):

        visited = dict()
        for vertex in graph._adjacency_list.keys():
            visited[vertex] = False

        for vertex in graph._adjacency_list.keys():
            if visited[vertex] == False and self._is_cyclic_helper(graph, vertex, visited, None):
                return True

        return False

    def _is_cyclic_helper(self, graph, vertex, visited, parent):
        if visited[vertex]:
            return True

        visited[vertex] = True

        for edge in graph._adjacency_list[vertex]:
            if(visited[edge.dest] == True and edge.dest is not parent):
                return True

            if(edge.dest is not parent and self._is_cyclic_helper(graph, edge.dest, visited, vertex)):
                return True

        return False