"""Code Fragment 14.5: Recursive implementation of depth-first search on a graph, 
starting at a designated vertex u."""
from Goodrich.Chapter14.graph import Graph


def DFS(g: Graph, u: Graph.Vertex, discovered: dict[Graph.Vertex, Graph.Edge]):
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
