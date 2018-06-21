from networkx import Graph

from utils.models import initialize_weighted_graph
from utils.disjoint_set import union
from utils.disjoint_set import make_set
from utils.disjoint_set import find_set


def kruskal(graph: Graph):
    """
    Kruskal's algorithm is a minimum-spanning-tree algorithm which finds an edge of the least possible weight that
    connects any two trees in the forest. It is a greedy algorithm in graph theory as it finds a minimum spanning
    tree for a connected weighted graph adding increasing cost arcs at each step. This means it finds a subset of
    the edges that forms a tree that includes every vertex, where the total weight of all the edges in the tree is
    minimized.

    :return: Minimum spanning tree of the given graph
    """
    sets = {make_set(node) for node in graph.nodes}
    minimum_spanning_tree = Graph()
    sorted_edges = sorted(graph.edges(data=True), key=lambda edge: edge[2]["weight"])

    for edge in sorted_edges:
        node1, node2, weight = edge
        if find_set(node1, sets) != find_set(node2, sets):
            union(find_set(node1, sets), find_set(node2, sets), sets)
            minimum_spanning_tree.add_edge(node1, node2, weight=weight["weight"])

    return minimum_spanning_tree


if __name__ == "__main__":
    weighted_graph = initialize_weighted_graph()
    minimum_spanning_tree = kruskal(weighted_graph)
    print(minimum_spanning_tree.adj)
