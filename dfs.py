class Vertex:
    def __init__(self, vertex_id: int, goal: bool = False, neighbours: list = None):
        self.id = vertex_id
        self.visited = False
        self.goal = goal
        self.color = "white"

        if neighbours is None:
            neighbours = []

        self.neighbours = neighbours

    def __repr__(self):
        return f"Vertex({self.id}, {self.color})"


def initialize_graph():
    """Goal is set at initialization"""
    return [
        Vertex(1, neighbours=[
            Vertex(2, neighbours=[
                Vertex(4, neighbours=[
                    Vertex(5, neighbours=[
                        Vertex(11),
                        Vertex(12)])
                ]),
                Vertex(6)]),
            Vertex(3, neighbours=[
                Vertex(7, neighbours=[
                    Vertex(9),
                    Vertex(10, goal=True)]),
                Vertex(8)])
        ])]


def depth_first_search(start: Vertex):
    stack = [start]
    while stack:
        vertex = stack.pop()
        print(f"Now handling this vertex: {vertex}")
        vertex.color = "grey"
        if vertex.goal:
            return vertex
        for neighbour in vertex.neighbours:  # type: Vertex
            neighbour.visited = True
            if neighbour.color == "white":
                stack.append(neighbour)
        vertex.color = "black"


if __name__ == "__main__":
    graph = initialize_graph()
    goal_vertex = depth_first_search(start=graph[0])
    print(goal_vertex)
