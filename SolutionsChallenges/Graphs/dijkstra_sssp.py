"""Dijkstra's Single Source Shortest Path Algorithm."""

import math
from typing import Dict, List
from Goodrich.Chapter13.GreedyTextCompression.min_heap import MinHeap
from Goodrich.Chapter14.Tests.init_graph import *
from Goodrich.Chapter14.graph import Graph
Vertex = Graph.Vertex
Edge = Graph.Edge
Int = int
Bool = bool


def dijkstra(G: Graph, s: Vertex):
    """Return the record of shortest paths from s to all other vertices in G."""

    distance: Dict[Vertex, List[Int and (Vertex|None) and Bool]]  = dict()
    """Tri-column distance record: Distance, Predecessor, Visted?"""

    unvisited = MinHeap()
    """Priority Queue for ranking the distance of a vertex (key) and vertex itself (value)."""

    # Insert starting vertex in unvisited heap and declare distance properties
    unvisited.insert(k=0, v=s)
    distance[s] = [0, None, False]

    # Declare distance records for other nodes
    for vert in G.vertices():
        if vert is not s:
            distance[vert] = [math.inf, None, False]

    # Begin iterative relaxation and distance updating process
    cur_vert = s
    while len(unvisited) > 0:
        if not distance[cur_vert][2]:                   # If node is yet to be visited...
            for edge in G.incident_edges(cur_vert):     # For each adjacent neighbor...
                weight = edge.element()
                neighbor = edge.opposite(cur_vert)
                if distance[cur_vert][0] + weight < distance[neighbor][0]:
                    distance[neighbor][0] = \
                        distance[cur_vert][0] + weight  # Relax/update distance
                    distance[neighbor][1] = cur_vert    # Update predecessor
                if not distance[neighbor][2]:           # If vertex has not been visited...
                    unvisited.insert(                   # Insert into univisted heap
                        k=distance[neighbor][0], v=neighbor)
        distance[cur_vert][2] = True                    # Mark as visited
        cur_vert = unvisited.remove_min()[1]            # Choose next minimum

    return distance


if __name__ == "__main__":
    path1 = dijkstra(*init_undirected_graph2())
    path2 = dijkstra(*init_undirected_graph3())
    path3 = dijkstra(*init_directed_graph2())
    for paths in path1, path2, path3:
        print("\nNode | Dist | Pred | Visited")
        for k in paths:
            path = paths[k]
            print(f"{k.element()}\t|\t"
                  f"{path[0]}\t|\t"
                  f"{path[1].element() if path[1] else '$'}\t|\t"
                  f"{path[2]}\t|\t")
