"""NON-MINIMUM Spanning Tree examples."""

from typing import Set, List

from Goodrich.Chapter14.Tests.init_graph import *
from Goodrich.Chapter14.graph import Graph
from Goodrich.Chapter13.GreedyTextCompression.min_heap import MinHeap

def span1(G: Graph, s: Graph.Vertex):
    """Return a Spanning Tree of graph G from vertex s."""
    unvisited_vertices: Set[Graph.Vertex] = set(G.vertices())
    uninserted_edges: Set[Graph.Edge] = set(G.edges())
    edge_heap: MinHeap = MinHeap()
    MST: List[Graph.Edge] = list()

    unvisited_vertices.remove(s)
    for e in G.incident_edges(s):
        edge_heap.insert(k=e.element(), v=e)
        uninserted_edges.remove(e)

    cur_vert = s
    while len(unvisited_vertices) > 0 and len(edge_heap) > 0:
        for edge in G.incident_edges(cur_vert):
            weight = edge.element()
            if edge in uninserted_edges:
                edge_heap.insert(weight, edge)
                uninserted_edges.remove(edge)
        min_edge: Graph.Edge = edge_heap.remove_min()[1]
        nearest_neighbor = min_edge.opposite(cur_vert)
        if (nearest_neighbor in unvisited_vertices and cur_vert not in unvisited_vertices) \
                or (nearest_neighbor not in unvisited_vertices and cur_vert in unvisited_vertices):
            MST.append(min_edge)
            unvisited_vertices.remove(nearest_neighbor)
            cur_vert = nearest_neighbor

    return MST


def span2(G: Graph, s: Graph.Vertex):
    visited_vertices: Set[Graph.Vertex] = set()
    inserted_edges: Set[Graph.Edge] = set()
    edge_heap = MinHeap()
    tree: List[Edge] = list()

    visited_vertices.add(s)
    for e in G.incident_edges(s):
        if e not in inserted_edges:
            inserted_edges.add(e)
            edge_heap.insert(k=e.element(), v=e)

    cur_vert = s
    while len(visited_vertices) < len(G.vertices()) and len(edge_heap) > 0:

        min_edge = edge_heap.remove_min()[1]
        nearest_neighbor = min_edge.opposite(cur_vert)

        if nearest_neighbor not in visited_vertices and cur_vert in visited_vertices:
            visited_vertices.add(nearest_neighbor)
            tree.append(min_edge)
            cur_vert = nearest_neighbor
        elif nearest_neighbor in visited_vertices and cur_vert not in visited_vertices:
            visited_vertices.add(cur_vert)
            tree.append(min_edge)
            cur_vert = nearest_neighbor
        else:
            continue

        for e in G.incident_edges(cur_vert):
            if e not in inserted_edges:
                inserted_edges.add(e)
                edge_heap.insert(k=e.element(), v=e)

    return tree



if __name__ == "__main__":
    UG4 = init_undirected_graph4()
    # mst = span2(*UG4)
    mst = span1(*UG4)
    for tree_edge in mst:
        endpoints = tree_edge.endpoints()
        print(f"{endpoints[0].element(), endpoints[1].element(), tree_edge.element()}")
