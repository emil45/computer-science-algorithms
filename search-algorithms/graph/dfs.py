from networkx import Graph

from utils.models import initialize_graph


def depth_first_search(graph: Graph, root: int, target: int):
    stack = [root]
    visited = set()

    while stack:
        vertex = stack.pop()
        print(f"Now handling vertex number: {vertex}")
        visited.add(vertex)

        if vertex == target:
            return vertex
        for neighbour in graph.adj[vertex]:
            if neighbour not in visited:
                stack.append(neighbour)

    return None


if __name__ == "__main__":
    graph = initialize_graph()
    target_vertex = depth_first_search(graph, root=1, target=12)
    if target_vertex:
        print(f"Found target vertex: {target_vertex}")
    else:
        print("Not found target vertex")
