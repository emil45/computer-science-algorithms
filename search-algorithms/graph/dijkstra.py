from networkx import Graph

from utils.models import initialize_weighted_graph
from utils.models import get_node_with_minimal_distance


def dijkstra(graph: Graph, source: int, target: int):
    graph.nodes[source]["distance"] = 0

    while graph.nodes:
        shortest_path_node = get_node_with_minimal_distance(graph)

        if target == shortest_path_node:
            return graph.nodes[target]["distance"]

        for neighbour in graph.neighbors(shortest_path_node):
            alt = graph.nodes[shortest_path_node]["distance"] + \
                  graph.get_edge_data(shortest_path_node, neighbour)["weight"]
            if alt < graph.nodes[neighbour]["distance"]:
                graph.nodes[neighbour]["distance"] = alt

        graph.remove_node(shortest_path_node)

    return graph


if __name__ == "__main__":
    weighted_graph = initialize_weighted_graph()
    shortest_distance = dijkstra(weighted_graph, 2, 6)
    print(f"Shortest distance from source to target is: {shortest_distance}")
