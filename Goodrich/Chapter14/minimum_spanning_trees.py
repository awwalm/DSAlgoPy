"""
Code Fragment 14.16: Python implementation of the Prim-Jarnik algorithm for the minimum spanning tree problem.
"""
import time
from typing import Dict, List

from Goodrich.Chapter14.Tests.init_graph import init_undirected_graph4
from Goodrich.Chapter14.graph import Graph
from Goodrich.Chapter9.ahpq import AdaptableHeapPriorityQueue
Locator = AdaptableHeapPriorityQueue.Locator


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



if __name__ == "__main__":
    UG4 = init_undirected_graph4()
    t1 = time.perf_counter()
    mst = MST_Prim_Jarnik(UG4[0])
    t2 = abs(t1 - time.perf_counter())
    for tree_edge in mst:
        endpoints = tree_edge.endpoints()
        print(f"{endpoints[0].element(), endpoints[1].element(), tree_edge.element()}")
    print(f"\nTime taken: {t2:.3e}")
