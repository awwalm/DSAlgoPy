"""Prim-Jarnik Minimum Spanning Tree algorithm."""

import random
import time
from typing import Set, List

from Goodrich.Chapter14.Tests.init_graph import init_undirected_graph4
from Goodrich.Chapter14.graph import Graph
from Goodrich.Chapter13.GreedyTextCompression.min_heap import MinHeap


def prim(G: Graph, s: Graph.Vertex):
    """Starting from vertex s, return the minimum
    spanning tree of a CONNECTED undirected graph G.
    """
    visited_vertices: Set[Graph.Vertex] = set()
    inserted_edges: Set[Graph.Edge] = set()  # To test Heap membership in O(1) time
    edge_heap: MinHeap[int, Graph.Edge] = MinHeap()
    MST: List[Graph.Edge] = list()

    # Mark start vertex as visited and insert every edge into heap
    visited_vertices.add(s)
    for e in G.incident_edges(s):
        edge_heap.insert(k=e.element(), v=e)
        inserted_edges.add(e)

    # Main loop: choose minimum-weight edge from heap, and add new vertices to MST
    while len(visited_vertices) < len(G.vertices()) and len(edge_heap) > 0:
        min_edge = edge_heap.remove_min()[1]
        u, v = min_edge.endpoints()

        # Determine the vertex not in the visited set
        if u in visited_vertices and v not in visited_vertices:
            new_vertex = v
        elif v in visited_vertices and u not in visited_vertices:
            new_vertex = u
        else:
            continue

        visited_vertices.add(new_vertex)
        MST.append(min_edge)

        # Add edges from the new vertex to the heap
        for e in G.incident_edges(new_vertex):
            if e not in inserted_edges:
                edge_heap.insert(k=e.element(), v=e)
                inserted_edges.add(e)

    return MST



if __name__ == "__main__":
    UG4 = init_undirected_graph4()
    start = random.choice(list(UG4[0].vertices()))
    t1 = time.perf_counter()
    # mst = prim(*UG4)          # Fixed starting point
    mst = prim(UG4[0], start)   # Randomnized starting point
    t2 = abs(t1 - time.perf_counter())
    for tree_edge in mst:
        endpoints = tree_edge.endpoints()
        print(f"{endpoints[0].element(), endpoints[1].element(), tree_edge.element()}")
    print(f"\nTime taken: {t2:.3e}")    # Faster than Goodrich textbook implementation
