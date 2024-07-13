import time

from Goodrich.Chapter14.Tests.init_graph import *
from Goodrich.Chapter14.graph import Graph
from Goodrich.Chapter9.ahpq import AdaptableHeapPriorityQueue


# Code Fragment 14.13: Python implementation of Dijkstra’s algorithm
# for computing the shortest-path distances from a single source.
# We assume that e.element() for edge e represents the weight of that edge.
def shortest_path_length(g: Graph, src: Graph.Vertex):
    """Compute shortest-path distances from src to reachable vertices of g.

    Graph g can be undirected or directed, but must be weighted such that
    e.element() returns a numeric weight for each edge e.
    """
    d = {}                                  # d[v] is upper bound from s to v
    cloud = {}                              # Map reachable v to its d[v] value
    pq = AdaptableHeapPriorityQueue()       # Vertex v will have key d[v]
    pqlocator = {}                          # Map from vertex to its pq locator

    # For each vertex v of the graph, add an entry to the priority queue,
    # with the source having distance 0 and all others having infinite distance
    for v in g.vertices():
        if v is src:
            d[v] = 0
        else:
            d[v] = float('inf')             # Syntax for positive infinity
        pqlocator[v] = pq.add(d[v], v)      # Save locator for future updates

    while not pq.is_empty():
        key, u = pq.remove_min()
        cloud[u] = key                      # Its correct d[u] value
        del pqlocator[u]                    # u is no longer in pq
        for e in g.incident_edges(u):       # Outgoing enges (u,v)
            v = e.opposite(u)
            if v not in cloud:              # Perform relaxation step on edge (u,v)
                wgt = e.element()
                if d[u] + wgt < d[v]:       # Better path to v?
                    d[v] = d[u] + wgt       # Update the distance
                    pq.update(              # Update the pq entry
                        pqlocator[v], d[v], v)

    return cloud                            # Only includes reachable vertices


# Code Fragment 14.14: Python function that reconstructs the shortest paths,
# based on knowledge of the single-source distances.
def shortest_path_tree(g: Graph, s: Graph.Vertex, d: dict[Graph.Vertex, int]):
    """Reconstruct shortest-path tree rooted at vertex s, given distance map d.

    Return tree as a map from each readable vertex v (other than s) to the
    edge e=(u,v) that is used to reach v from its parent u in the tree.
    """
    tree = {}
    for v in d:
        if v is not s:
            for e in g.incident_edges(v, False):  # consider INCOMING edges
                u = e.opposite(v)
                wgt = e.element()
                if d[v] == d[u] + wgt:                    # Edge e is used to reach v
                    tree[v] = e
    return tree


if __name__ == "__main__":
    UG1, s1 = init_undirected_graph2()
    UG2, s2 = init_directed_graph2()

    t1 = time.perf_counter()
    paths1: dict[Graph.Vertex, int] = shortest_path_length(UG1, s1)
    dtree1 = shortest_path_tree(UG1, s1, paths1)
    t2 = f"{abs(t1-time.perf_counter()):.3e}"
    t3 = time.perf_counter()
    paths2: dict[Graph.Vertex, int] = shortest_path_length(UG2, s2)
    dtree2 = shortest_path_tree(UG2, s2, paths2)
    t4 = f"{abs(t3-time.perf_counter()):.3e}"
    print(f"Time taken\nUG2: {t2}\nDG2: {t4}")

    for paths in paths1, paths2:
        print()
        for k in paths:
            print(f"{k.element()}\t|\t{paths[k]}")
