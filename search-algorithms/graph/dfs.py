from networkx import Graph

from utils.models import initialize_graph


def depth_first_search_recursive(graph: Graph, root: int, target: int):
    if root == target:
        return root

    print(f"Now handling vertex number: {root}")
    graph.nodes[root]["visited"] = True

    for neighbour in graph.neighbors(root):
        if not graph.nodes[neighbour]["visited"]:
            vertex = depth_first_search_recursive(graph, neighbour, target)
            if vertex:
                return vertex


def depth_first_search(graph: Graph, root: int, target: int):
    stack = [root]

    while stack:
        vertex = stack.pop()
        print(f"Now handling vertex number: {vertex}")
        graph.nodes[vertex]["visited"] = True

        if vertex == target:
            return vertex

        for neighbour in graph.neighbors(vertex):
            if not graph.nodes[neighbour]["visited"]:
                stack.append(neighbour)

    return None


if __name__ == "__main__":
    graph = initialize_graph()
    target_vertex = depth_first_search_recursive(graph, root=1, target=9)
    if target_vertex:
        print(f"Found target vertex: {target_vertex}")
    else:
        print("Not found target vertex")
