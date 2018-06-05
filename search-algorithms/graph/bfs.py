from queue import Queue
from utils.models import Vertex


def breadth_first_search(start: Vertex, goal: int):
    queue = Queue()
    queue.put(start)

    while not queue.empty():
        vertex = queue.get()
        vertex.visited = True
        print(f"Now handling: {vertex}")

        if vertex.id == goal:
            return vertex
        for neighbour in vertex.neighbours:
            if not neighbour.visited:
                neighbour.visited = True
                queue.put(neighbour)

    return None


def initialize_graph():
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
                    Vertex(10)]),
                Vertex(8)])
        ])]


if __name__ == "__main__":
    graph = initialize_graph()
    goal_vertex = breadth_first_search(start=graph[0], goal=14)
    if goal_vertex:
        print(f"Found goal vertex: {goal_vertex}")
    else:
        print("Not found goal vertex")
