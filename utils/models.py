from typing import List


class Vertex:
    def __init__(self, vertex_id: int, neighbours: List['Vertex'] = None):
        self.id = vertex_id
        self.visited = False

        if neighbours is None:
            neighbours = []

        self.neighbours = neighbours

    def __repr__(self):
        return f"Vertex({self.id})"


class Edge:
    def __init__(self, v1: Vertex, v2: Vertex, value: int = None):
        self.v1 = v1
        self.v2 = v2
        self.value = value

    def __repr__(self):
        return f"Edge({self.v1}, {self.v2})"


class Graph:
    def __init__(self, root: Vertex, vertices: List[Vertex]):
        self.root = root
        self.vertices = vertices
        self.edges = self.__calculate_edges(self.vertices)

    @property
    def root(self):
        return self.root()

    @root.setter
    def root(self, value):
        self.root = value

    def add_edge(self, vertex1: Vertex, vertex2: Vertex):
        pass

    def __calculate_edges(self, future):
        pass