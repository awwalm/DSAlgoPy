# Code Fragment 14.10: Python implementation of the Floyd-Warshall algorithm.
from copy import deepcopy
from Goodrich.Chapter14.graph import Graph


def floyd_warshall(g: Graph):
    """Return a new graph that is the transitive closure of g."""
    closure = deepcopy(g)
    verts = list(closure.vertices())
    n = len(verts)
    for k in range(n):
        for i in range(n):
            # Verify that edge (i,k) exists in the partial closure
            if i != k and closure.get_edge(verts[i], verts[k]) is not None:
                for j in range(n):
                    # Verify that edge (k,j) exists in the partial closure
                    if i != j != k and closure.get_edge(verts[k], verts[j]) is not None:
                        # if (i,j) not yet included, add it to closure
                        if closure.get_edge(verts[i], verts[j]) is None:
                            closure.insert_edge(verts[i], verts[j])
    return closure
