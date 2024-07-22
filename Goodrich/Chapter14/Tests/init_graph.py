"""Canned examples of directed and undirected Adjacency Map graph instance generators."""
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

