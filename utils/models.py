from typing import List


class Vertex:
    """Vertex model for DFS and BFS algorithms"""
    def __init__(self, vertex_id: int, neighbours: List['Vertex'] = None):
        self.id = vertex_id
        self.visited = False

        if neighbours is None:
            neighbours = []

        self.neighbours = neighbours

    def __repr__(self):
        return f"Vertex({self.id})"