# https://stackoverflow.com/questions/78678231

from collections import OrderedDict
from typing import List
from Goodrich.Chapter14.graph import Graph


def init_graph():
    G = Graph(directed=True)

    v1 = G.insert_vertex(1)
    v2 = G.insert_vertex(2)
    v3 = G.insert_vertex(3)
    v4 = G.insert_vertex(4)

    G.insert_edge(v1, v2)
    G.insert_edge(v1, v3)
    G.insert_edge(v3, v2)
    G.insert_edge(v3, v4)
    G.insert_edge(v4, v3)

    return G, v1

def klen_dfs(G: Graph, s: Graph.Vertex, k: int):
    """Report all paths (edge lists) less than length k.
    G - Adjacency Map Graph ADT
    s - Starting vertex
    k - Path length limit (actual limit = k-1)
    """
    discovery_edges: OrderedDict[Graph.Vertex, Graph.Edge] = OrderedDict()
    path_accummulator: List[Graph.Edge] = [ ]
    path_array: List[List[Graph.Edge]] = [ ]

    def dfs(g: Graph, u: Graph.Vertex, discovered, klen, p):
        """Traditional DFS with additional params.
        u - A vertex in G
        p - Concurrent path array of less than k edges
        """
        if klen < k:
            for e in g.incident_edges(u, outgoing=True):
                v = e.opposite(u)
                if not discovered.get(v):   # Cyclic traversal prevention
                    discovered[v] = e
                    p.append(e)
                    if klen == k-1: path_array.append(p[:])
                    dfs(g, v, discovered, klen + 1, p)
                    p.pop()
                    discovered.pop(v)

    dfs(G, s, discovery_edges, 1, path_accummulator)
    return path_array


if __name__ == "__main__":
    # For graph produced by init_graph(), all k >= 3 has same results
    for K in range(1,5):
        digraph, start = init_graph()
        paths = klen_dfs(digraph, start, K)
        formatted_paths = []
        for path in paths:
            formatted_path = []
            for edge in path:
                endpoints = edge.endpoints()
                formatted_path.append((
                    endpoints[0].element(), endpoints[1].element()))
            formatted_paths.append(formatted_path)
        print(f"ALL paths when k = {K} (i.e of length {K-1} < k length)")
        print(*formatted_paths, sep="\n")
        print()
