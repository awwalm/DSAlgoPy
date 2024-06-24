from typing import Dict
from Goodrich.Chapter14.graph import Graph


# Code Fragment 14.5: Recursive implementation of depth-first search on a graph,
# starting at a designated vertex u.
def DFS(g: Graph, u: Graph.Vertex, discovered: Dict[Graph.Vertex, Graph.Edge|None]):
    """
    Perform DFS of the undiscovered portion of Graph g starting at Vertex U.

    :param g: A Graph object containing a set of vertices containing u.

    :param u: A Vertex object which is the starting point for the DFS traversal.

    :param discovered: A dictionary mapping each vertex to the edge that was
    used to discover it during DFS. (u should be "discovered" prior to the call).
    Newly discovered vertices will be added to the dictionary as a result.
    """
    for e in g.incident_edges(u):
        v = e.opposite(u)
        if v not in discovered:
            discovered[v] = e
            DFS(g, v, discovered)


# Code Fragment 14.6: Function to reconstruct a directed path from u to v,
# given the trace of discovery from a DFS started at u.
# The function returns an ordered list of vertices on the path.
def construct_path(v: Graph.Vertex, u: Graph.Vertex, discovered: Dict[Graph.Vertex, Graph.Edge]):
    path = []
    if v in discovered:                     # Empty path by default
        # We build list from v to u and then reverse it at the end
        path.append(v)
        walk = v
        while walk is not u:
            e = discovered[walk]            # Find edge leading to walk
            parent = e.opposite(walk)
            path.append(parent)
            walk = parent
        path.reverse()                      # Reorient path from u to v
    return path


# Code Fragment 14.7: Top-level function that returns a DFS forest for an entire graph.
def DFS_complete(g: Graph):
    """Perform DFS for entire graph and return forest as dictionary.

    Result maps each vertex v to the edge that was used to discover it.
    (Vertices that are roots of a DFS tree are mapped to None.)
    """
    forest: Dict[Graph.Vertex, Graph.Edge|None] = {}
    for u in g.vertices():
        if u not in forest:
            forest[u] = None                # u will be the root of a tree
            DFS(g, u, forest)
    return forest


# Code Fragment 14.8: Implementation of breadth-first search on a graph,
# starting at a designated vertex s.
def BFS(g: Graph, s: Graph.Vertex, discovered: Dict[Graph.Vertex, Graph.Edge|None]):
    """Perform BFS of the undiscovered portion of Graph g starting at Vertex s.

    discovered is a dictionary mapping each vertex to the edge that was used to
    discover it during the BFS (s should be mapped to None prior to the call).
    Newly discovered vertices will be added to the dictionary as a result.
    """
    level = [s]                             # First level includes only s
    while len(level) > 0:
        next_level = []                     # Prepare to gather newly found vertices
        for u in level:
            for e in g.incident_edges(u):   # For every outgoing edge from u
                v = e.opposite(u)
                if v not in discovered:     # v is an unvisited vertex
                    discovered[v] = e       # e is the tree edge that discovered v
                    next_level.append(v)    # v will be further considered in next pass
        level = next_level                  # relabel 'next' level to become current

