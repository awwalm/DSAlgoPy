"""Canned examples of directed and undirected graph instance generators."""
import random
import networkx as nx
NXGraph = nx.classes.graph.Graph

from Goodrich.Chapter14.graph import Graph
Vertex = Graph.Vertex
Edge = Graph.Edge

# https://upload.wikimedia.org/wikipedia/commons/2/23/Directed_graph_no_background.svg
def init_directed_graph1():
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


# https://www.youtube.com/watch?v=pSqmAO-m7Lk
def init_directed_graph2():
    G = Graph(directed=True)
    v0 = G.insert_vertex(0)
    v1 = G.insert_vertex(1)
    v2 = G.insert_vertex(2)
    v3 = G.insert_vertex(3)
    v4 = G.insert_vertex(4)
    G.insert_edge(v0, v1, 4)
    G.insert_edge(v0, v2, 1)
    G.insert_edge(v2, v1, 2)
    G.insert_edge(v2, v3, 5)
    G.insert_edge(v1, v3, 1)
    G.insert_edge(v3, v4, 3)
    return G, v0


# https://www.youtube.com/watch?v=dRMvK76xQJI
def init_directed_graph3():
    """For testing Uniform Cost Search."""
    G = Graph(directed=True)
    s = G.insert_vertex("S")
    a = G.insert_vertex("A")
    b = G.insert_vertex("B")
    c = G.insert_vertex("C")
    d = G.insert_vertex("D")
    e = G.insert_vertex("E")
    f = G.insert_vertex("F")
    g1 = G.insert_vertex("G1")
    g2 = G.insert_vertex("G2")
    g3 = G.insert_vertex("G3")
    G.insert_edge(s, a, 5)
    G.insert_edge(s, b, 9)
    G.insert_edge(s, d, 6)
    G.insert_edge(a, g1, 9)
    G.insert_edge(a, b, 3)
    G.insert_edge(b, a, 2)
    G.insert_edge(b, c, 1)
    G.insert_edge(c, s, 6)
    G.insert_edge(c, g2, 5)
    G.insert_edge(c, f, 7)
    G.insert_edge(d, s, 1)
    G.insert_edge(d, c, 2)
    G.insert_edge(d, e, 2)
    G.insert_edge(e, g3, 7)
    G.insert_edge(f, d, 2)
    G.insert_edge(f, g3, 8)
    return G, s, {g1, g2, g3}


# https://porkostomus.gitlab.io/img/tc.jpg
def init_undirected_graph1():
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
    return G, A


# https://www.youtube.com/watch?v=bZkzH5x0SKU
def init_undirected_graph2():
    G = Graph()
    a = G.insert_vertex("A")
    b = G.insert_vertex("B")
    c = G.insert_vertex("C")
    d = G.insert_vertex("D")
    e = G.insert_vertex("E")
    f = G.insert_vertex("F")
    G.insert_edge(a, b, 2)
    G.insert_edge(a, d, 8)
    G.insert_edge(b, e, 6)
    G.insert_edge(b, d, 5)
    G.insert_edge(d, e, 3)
    G.insert_edge(d, f, 2)
    G.insert_edge(f, e, 1)
    G.insert_edge(f, c, 3)
    G.insert_edge(e, c, 9)
    return G, a


# https://www.youtube.com/watch?v=NyrHRNiRpds
def init_undirected_graph3():
    G = Graph()
    a = G.insert_vertex("A")
    b = G.insert_vertex("B")
    c = G.insert_vertex("C")
    d = G.insert_vertex("D")
    e = G.insert_vertex("E")
    f = G.insert_vertex("F")
    G.insert_edge(c, a, 2)
    G.insert_edge(c, d, 5)
    G.insert_edge(c, b, 9)
    G.insert_edge(a, f, 4)
    G.insert_edge(a, b, 5)
    G.insert_edge(b, e, 3)
    G.insert_edge(b, d, 8)
    G.insert_edge(f, e, 6)
    return G, c


# https://www.freecodecamp.org/news/prims-algorithm-explained-with-pseudocode/
def init_undirected_graph4():
    G = Graph()
    a = G.insert_vertex("A")
    b = G.insert_vertex("B")
    c = G.insert_vertex("C")
    d = G.insert_vertex("D")
    e = G.insert_vertex("E")
    f = G.insert_vertex("F")
    g = G.insert_vertex("G")
    G.insert_edge(a, b, 2)
    G.insert_edge(a, c, 1)
    G.insert_edge(a, d, 4)
    G.insert_edge(b, c, 3)
    G.insert_edge(b, e, 7)
    G.insert_edge(c, e, 9)
    G.insert_edge(c, g, 4)
    G.insert_edge(d, c, 2)
    G.insert_edge(d, f, 6)
    G.insert_edge(e, g, 3)
    G.insert_edge(f, g, 1)
    G.insert_edge(f, c, 8)
    return G, d


# https://www.youtube.com/watch?v=r9lzHs2rZDc
def init_complete_graph(n=random.randint(4,10), weight_range=(1,100)):
    G: NXGraph = nx.complete_graph(n)
    for u,v in G.edges():
        G.edges[u,v]["weight"] = random.randint(*weight_range)
        # print(f"type(u) = {type(u)}")
        # print(f"type(G.edges[u,v]) = {type(G.edges[u,v])}")
        # print(f"type(G.edges[u,v][`weight`]) = {type(G.edges[u,v]['weight'])}\n")

    return G

# Create an undirected graph acyclic and connected (tree)
def init_bin_tree_graph():
    """For testing modified Uniform Cost Search on a tree."""
    G = Graph(directed=False)
    s = G.insert_vertex("S")
    a = G.insert_vertex("A")
    b = G.insert_vertex("B")
    c = G.insert_vertex("C")
    d = G.insert_vertex("D")
    e = G.insert_vertex("E")
    f = G.insert_vertex("F")
    g1 = G.insert_vertex("G1")
    g2 = G.insert_vertex("G2")
    g3 = G.insert_vertex("G3")

    # Forming a tree structure
    G.insert_edge(s, a)  # S - A
    G.insert_edge(s, b)  # S - B
    G.insert_edge(b, c)  # B - C
    G.insert_edge(c, g1)  # C - G1
    G.insert_edge(c, d)  # C - D
    G.insert_edge(d, e)  # D - E
    G.insert_edge(e, g2)  # E - G2
    G.insert_edge(e, f)  # E - F
    G.insert_edge(f, g3)  # F - G3

    # return G, s, {g1, g2, g3}
    return G


def init_tree_graph():
    """Create a non-binary tree structure for testing."""
    G = Graph(directed=False)

    # Insert vertices
    s = G.insert_vertex("S")
    a = G.insert_vertex("A")
    b = G.insert_vertex("B")
    c = G.insert_vertex("C")
    d = G.insert_vertex("D")
    e = G.insert_vertex("E")
    f = G.insert_vertex("F")
    g = G.insert_vertex("G")
    h = G.insert_vertex("H")
    i = G.insert_vertex("I")
    j = G.insert_vertex("J")
    k = G.insert_vertex("K")
    l = G.insert_vertex("L")
    m = G.insert_vertex("M")

    # Insert edges (tree structure)
    G.insert_edge(s, a)  # S - A
    G.insert_edge(s, b)  # S - B
    G.insert_edge(s, c)  # S - C
    G.insert_edge(a, d)  # A - D
    G.insert_edge(a, e)  # A - E
    G.insert_edge(e, i)  # E - I
    G.insert_edge(i, k)  # I - K
    G.insert_edge(i, l)  # I - L
    G.insert_edge(c, f)  # C - F
    G.insert_edge(c, g)  # C - G
    G.insert_edge(c, h)  # C - H
    G.insert_edge(h, j)  # H - J
    G.insert_edge(j, m)  # J - M

    # return G, s, {d, k, m}  # Mark some nodes as goals (you can change this)
    return G


