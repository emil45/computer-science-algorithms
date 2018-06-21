import math
from collections import namedtuple

import networkx

Job = namedtuple("Job", ["start_time", "finish_time"])


def get_node_with_minimal_distance(graph: networkx.Graph):
    nodes = networkx.get_node_attributes(graph, "distance")
    return min(nodes, key=nodes.get)


def initialize_graph():
    graph = networkx.Graph()
    graph.add_edge(1, 2)
    graph.add_edge(1, 3)
    graph.add_edge(2, 4)
    graph.add_edge(2, 6)
    graph.add_edge(3, 7)
    graph.add_edge(3, 8)
    graph.add_edge(4, 5)
    graph.add_edge(5, 11)
    graph.add_edge(5, 12)
    graph.add_edge(7, 9)
    graph.add_edge(7, 10)
    networkx.set_node_attributes(graph, False, "visited")
    return graph


def initialize_weighted_graph():
    graph = networkx.Graph()
    graph.add_edge(1, 2, weight=6)
    graph.add_edge(1, 3, weight=4)
    graph.add_edge(1, 4, weight=3)
    graph.add_edge(3, 4, weight=1)
    graph.add_edge(3, 5, weight=7)
    graph.add_edge(3, 6, weight=9)
    graph.add_edge(4, 5, weight=2)
    graph.add_edge(5, 6, weight=2)
    networkx.set_node_attributes(graph, math.inf, "distance")
    return graph


def initialize_jobs():
    return [Job(1, 5), Job(5, 9), Job(10, 11), Job(2, 6), Job(2, 7),
            Job(1, 2), Job(3, 4), Job(2, 3), Job(4, 6), Job(6, 10)]
