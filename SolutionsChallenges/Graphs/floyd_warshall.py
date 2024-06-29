import copy
from collections import OrderedDict
from Goodrich.Chapter14.graph import Graph
Vertex = Graph.Vertex
Edge = Graph.Edge

def init_directed_graph():
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
    return G


def init_undirected_graph():
    G = Graph()
    A = G.insert_vertex("A")
    B = G.insert_vertex("B")
    C = G.insert_vertex("C")
    D = G.insert_vertex("D")
    E = G.insert_vertex("E")
    G.insert_edge(A, C)
    G.insert_edge(B, C)
    G.insert_edge(B, D)
    G.insert_edge(C, D)
    G.insert_edge(D, E)
    return G


def transitive_bfs(
        G: Graph,                       # Adjacency Map Graph ADT
        origin: Vertex,                 # Original vertex to connect with target t
        s: Vertex,                      # Starting vetex of graph G
        t: Vertex,                      # Target vertex being searched for
        d: OrderedDict[Vertex, Edge],   # Discovery records
        f: bool):                       # Boolean that is true when t is found
    """BFS traversal that finds t from s=origin,
    then connects an edge from origin to t."""

    outgoing_edges = list(G.incident_edges(s, outgoing=True if G.is_directed() else False))
    outgoing_vertices = []
    for e in outgoing_edges:
        v = e.opposite(s)
        if not d.get(v):
            outgoing_vertices.append(v)
            d[v] = e
            if v == t:   # Target found!
                G.insert_edge(origin, t)
                f = True
                return f
    for vert in outgoing_vertices: transitive_bfs(G, origin, vert, t, d, f)


def floyd_warshall(G: Graph):
    """Returns the transitive closure, G*, of G."""
    G_closure = copy.deepcopy(G)
    vertices = list(G_closure.vertices())
    n = len(vertices)

    for i in range(n):
        for j in range(n):
            reachable = False
            v_i, v_j = vertices[i], vertices[j]
            if v_i != v_j and not(G_closure.get_edge(v_i, v_j)):
                # print(f"No edge check passed: {(v_i.element(), v_j.element())}")
                transitive_bfs(G_closure, v_i, v_i, v_j, OrderedDict(), reachable)
    print()
    return G_closure


if __name__ == "__main__":
    c1 = floyd_warshall(init_directed_graph())
    c2 = floyd_warshall(init_undirected_graph())

    edges1 = c1.edges()
    edges2 = c2.edges()

    for edge_array in edges1, edges2:
        for edge in edge_array:
            endpoint = edge.endpoints()
            print((endpoint[0].element(), endpoint[1].element()))
        print()

