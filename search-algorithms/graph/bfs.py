from queue import Queue

from networkx import Graph

from utils.models import initialize_graph


def breadth_first_search(graph: Graph, root: int, target: int):
    queue = Queue()
    queue.put(root)

    while not queue.empty():
        vertex = queue.get()
        print(f"Now handling vertex number: {vertex}")
        graph.nodes[vertex]["visited"] = True

        if vertex == target:
            return vertex
        for neighbour in graph.neighbors(vertex):
            if not graph.nodes[neighbour]["visited"]:
                queue.put(neighbour)

    return None


if __name__ == "__main__":
    graph = initialize_graph()
    target_vertex = breadth_first_search(graph, root=1, target=12)
    if target_vertex:
        print(f"Found target vertex: {target_vertex}")
    else:
        print("Not found target vertex")
