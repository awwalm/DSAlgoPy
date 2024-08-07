"""Chained BFS implementation of Floyd-Warshall transitive closure algorithm."""

import copy
from collections import OrderedDict
from Goodrich.Chapter14.Tests.init_graph import *
from Goodrich.Chapter14.graph import Graph
Vertex = Graph.Vertex
Edge = Graph.Edge


def transitive_bfs(
        G:          Graph,                      # Adjacency Map Graph ADT
        origin:     Vertex,                     # Original vertex to connect with target t
        start:      Vertex,                     # Starting vetex of graph G
        target:     Vertex,                     # Target vertex being searched for
        discovery:  OrderedDict[Vertex, Edge],  # Discovery records
        found:      bool):                      # Boolean that is true when t is found
    """BFS traversal that finds target from origin, then connects an edge from origin to target."""

    outgoing_edges = G.incident_edges(
        start, outgoing=True if G.is_directed() else False)
    outgoing_vertices = []
    for e in outgoing_edges:
        v = e.opposite(start)
        if not discovery.get(v):
            outgoing_vertices.append(v)
            discovery[v] = e
            if v == target:   # Target found!
                G.insert_edge(origin, target)
                found = True
                return found
    for vert in outgoing_vertices:
        transitive_bfs(G, origin, vert, target, discovery, found)


def floyd_warshall(G: Graph):
    """Returns the transitive closure, G_closure, of G."""
    G_closure = copy.deepcopy(G)
    vertices = list(G_closure.vertices())
    n = len(vertices)
    for i in range(n):
        for j in range(n):
            reachable = False
            v_i, v_j = vertices[i], vertices[j]
            if v_i != v_j and not(G_closure.get_edge(v_i, v_j)):
                transitive_bfs(G_closure, v_i, v_i, v_j, OrderedDict(), reachable)
    return G_closure


if __name__ == "__main__":
    g1 = init_directed_graph1()[0]
    g2 = init_undirected_graph1()[0]
    c1 = floyd_warshall(g1)
    c2 = floyd_warshall(g2)
    edges1 = c1.edges()
    edges2 = c2.edges()
    edges3 = g1.edges()
    edges4 = g2.edges()

    print("Original edges:\n")
    for edge_array in edges3, edges4:
        for edge in edge_array:
            endpoint = edge.endpoints()
            print((endpoint[0].element(), endpoint[1].element()))
        print()

    print("Closure edges:\n")
    for edge_array in edges1, edges2:
        for edge in edge_array:
            endpoint = edge.endpoints()
            print((endpoint[0].element(), endpoint[1].element()))
        print()

