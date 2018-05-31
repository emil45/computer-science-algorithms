from queue import Queue


class Vertex:
    def __init__(self, vertex_id: int, goal: bool = False, neighbours: list = None):
        self.id = vertex_id
        self.visited = False
        self.goal = goal

        if neighbours is None:
            neighbours = []

        self.neighbours = neighbours

    def __repr__(self):
        return f"Vertex({self.id})"


def breadth_first_search(start: Vertex):
    queue = Queue()
    queue.put(start)
    start.visited = True

    while not queue.empty():
        vertex = queue.get()
        print(f"Now handling this vertex: {vars(vertex)}")
        if vertex.goal:
            return vertex
        for neighbour in vertex.neighbours:
            if not neighbour.visited:
                neighbour.visited = True
                queue.put(neighbour)


def initialize_graph():
    """Goal is set at initialization"""
    return [
        Vertex(1, neighbours=[
            Vertex(2, neighbours=[
                Vertex(4, neighbours=[
                    Vertex(5, neighbours=[
                        Vertex(11),
                        Vertex(12, goal=True)])
                ]),
                Vertex(6)]),
            Vertex(3, neighbours=[
                Vertex(7, neighbours=[
                    Vertex(9),
                    Vertex(10)]),
                Vertex(8)])
        ])]


if __name__ == "__main__":
    graph = initialize_graph()
    goal_vertex = breadth_first_search(start=graph[0])
    print(vars(goal_vertex))
