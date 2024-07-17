
import time
from typing import Dict, List, Callable

from Goodrich.Chapter14.Tests.init_graph import init_undirected_graph4
from Goodrich.Chapter14.graph import Graph
from Goodrich.Chapter14.partition import Partition
from Goodrich.Chapter9.ahpq import AdaptableHeapPriorityQueue
from Goodrich.Chapter9.heap_priority_queue import HeapPriorityQueue

Locator = AdaptableHeapPriorityQueue.Locator


# Code Fragment 14.16: Python implementation of the Prim-Jarnik algorithm
# for the minimum spanning tree problem.
def MST_Prim_Jarnik(g: Graph):
    """Compute a minimum spanning tree of weighted graph G.\n
    Return a list of edges that comprise the MST (in arbitrary order).
    """
    d: Dict[Graph.Vertex, int|float] = { }          # Bound on distance to tree
    tree: List[Graph.Edge] = [ ]                    # List of edges in spanning tree
    pq = AdaptableHeapPriorityQueue()               # Maps to value (v, e=(u,v))
    pqlocator: Dict[Graph.Vertex, Locator] = { }    # Map from vertex to its pq locator

    # For each vertex v of the graph, add an entry to the pq, with
    # the source having distance 0 and others having infinite distance
    for v in g.vertices():
        if len(d) == 0:                             # This is the first node
            d[v] = 0                                # Make it the root
        else:
            d[v] = float('inf')                     # Positive infinity
        pqlocator[v] = pq.add(d[v], (v,None))

    while not pq.is_empty():
        key, value = pq.remove_min()
        u, edge = value                             # Unpack tuple from pq
        del pqlocator[u]                            # u is no longer in pq
        if edge is not None:
            tree.append(edge)                       # Add edge to tree
        for link in g.incident_edges(u):
            v = link.opposite(u)
            if v in pqlocator:                      # Thus, v not yet in tree
                # See if edge(u,v) better connects v to the growing tree
                wgt = link.element()
                if wgt < d[v]:                      # Better edge to v?
                    d[v] = wgt                      # Update the distance
                    pq.update(pqlocator[v],         # Update the pq entry
                              d[v],
                              (v, link))

    return tree



# Code Fragment 14.18: Python implementation of Kruskal’s algorithm
# for the minimum spanning tree problem.
def MST_Kruskal(g: Graph):
    """Compute a minimum spanning tree of a graph using Kruskal's algorithm.

    Return a list of edges that comprise the MST.
    The elements of the graph's edges are assumed to be weights.
    """
    tree: List[Graph.Edge] = [ ]                    # List of edges in spanning tree
    pq = HeapPriorityQueue()                        # Entries are edges in G, with weihts as key
    forest = Partition()                            # Keeps track of forest clusters
    position: Dict[Graph.Vertex, Partition] = { }   # Map each node to its Partition entry

    for v in g.vertices():
        position[v] = forest.make_group(v)

    for e in g.edges():
        pq.add(e.element(), e)                      # Edge's element is assumed to be its weight

    size = g.vertex_count()
    while len(tree) != size - 1 and not pq.is_empty():
        # Tree not spanning and unprocessed edges remain
        weight, edge = pq.remove_min()
        u, v = edge.endpoints()
        a = forest.find(position[u])
        b = forest.find(position[v])
        if a != b:
            tree.append(edge)
            forest.union(a,b)

    return tree



if __name__ == "__main__":
    def test_mst(mst_func: Callable):
        UG4 = init_undirected_graph4()
        t1 = time.perf_counter()
        mst = mst_func(UG4[0])
        t2 = abs(t1 - time.perf_counter())
        for tree_edge in mst:
            endpoints = tree_edge.endpoints()
            print(f"{endpoints[0].element(), endpoints[1].element(), tree_edge.element()}")
        print(f"\nTime taken [{mst_func.__name__}]: {t2:.3e}\n")

    test_mst(MST_Kruskal)
    test_mst(MST_Prim_Jarnik)
