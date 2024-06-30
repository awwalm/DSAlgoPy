from collections import OrderedDict
from typing import List
from graph import Graph


# Code Fragment 14.11: Python implementation for the topological sorting algorithm.
def topological_sort(g: Graph):
    """Return a list of vertices of directed acyclic graph g in topological order.
    If a graph g has a cycle, the result will be incomplete.
    """
    topo: List[Graph.Vertex] = []       # A list of vertices placed in topological order
    ready: List[Graph.Vertex] = []      # List of vertices that have no remaining constraints
    incount = OrderedDict()             # Keep track of in-degree for each vertex

    # Phase 1: Find vertices without incoming edges
    for u in g.vertices():
        incount[u] = g.degree(
            u, False)           # Parameter requests incoming degree
        if incount[u] == 0:             # If u has no incoming edges
            ready.append(u)             # It is free of constraints

    # Phase 2: Continuously remove vertices with no incoming edges
    while len(ready) > 0:
        u = ready.pop()                 # u is free of constraints
        topo.append(u)                  # add u to the topological order
        for e in g.incident_edges(u):   # consider all outgoing neighbors of u
            v = e.opposite(u)
            incount[v] -= 1             # v has one less constraint without u
            if incount[v] == 0:
                ready.append(v)
