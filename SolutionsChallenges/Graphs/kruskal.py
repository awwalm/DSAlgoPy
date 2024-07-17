"""Kruskal's Minimum Spanning Tree Algorithm."""
import time
from typing import Set, List
from Goodrich.Chapter13.GreedyTextCompression.min_heap import MinHeap
from Goodrich.Chapter14.Tests.init_graph import *
from Goodrich.Chapter14.graph import Graph

# @FIXME: Incorrect spannig logic; does not connect all vertices.
def kruskal(G: Graph):
    """Return the minimum spanning tree of
    a connected undirected graph G.
    """
    visited_vertices: Set[Graph.Vertex] = set()
    edge_heap: MinHeap[int, Graph.Edge] = MinHeap()
    MST: List[Graph.Edge] = list()

    for e in G.edges():
        edge_heap.insert(e.element(), e)

    while len(visited_vertices) < len(G.vertices()) and len(edge_heap) > 0:
        weight, min_edge = edge_heap.remove_min()
        u, v = min_edge.endpoints()

        if u not in visited_vertices and v in visited_vertices:
            visited_vertices.add(u)
            MST.append(min_edge)
        elif u in visited_vertices and v not in visited_vertices:
            visited_vertices.add(v)
            MST.append(min_edge)
        elif u not in visited_vertices and v not in visited_vertices:
            visited_vertices.add(u)
            visited_vertices.add(v)
            MST.append(min_edge)

        elif u in visited_vertices and v in visited_vertices:   # Both u and v have been visited
            print(u.element(), v.element(), weight)
            # continue

    return MST



if __name__ == "__main__":
    UG4 = init_undirected_graph4()
    t1 = time.perf_counter()
    # mst = prim(*UG4)          # Fixed starting point
    mst = kruskal(UG4[0])   # Randomnized starting point
    t2 = abs(t1 - time.perf_counter())
    for tree_edge in mst:
        endpoints = tree_edge.endpoints()
        print(f"{endpoints[0].element(), endpoints[1].element(), tree_edge.element()}")
    print(f"\nTime taken: {t2:.3e}")    # Faster than Goodrich textbook implementation
