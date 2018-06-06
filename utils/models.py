from networkx import Graph


def initialize_graph():
    graph = Graph()
    graph.add_edges_from([(1, 2), (1, 3),
                          (2, 4), (2, 6), (4, 5),
                          (5, 11), (5, 12),
                          (3, 7), (3, 8),
                          (7, 9), (7, 10)])
    return graph
