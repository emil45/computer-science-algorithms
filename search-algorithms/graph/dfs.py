from utils.models import Vertex


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
        ])
    ]


def depth_first_search(start: Vertex, goal: int):
    stack = [start]

    while stack:
        vertex = stack.pop()
        print(f"Now handling: {vertex}")
        vertex.visited = True

        if vertex.id == goal:
            return vertex
        for neighbour in vertex.neighbours:
            if not neighbour.visited:
                stack.append(neighbour)

    return None


if __name__ == "__main__":
    graph = initialize_graph()
    goal_vertex = depth_first_search(start=graph[0], goal=10)
    if goal_vertex:
        print(f"Found goal vertex: {goal_vertex}")
    else:
        print("Not found goal vertex")
