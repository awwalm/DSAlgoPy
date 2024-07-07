"""Dijkstra's Single Source Shortest Path Algorithm."""

import math
from dataclasses import dataclass
from typing import Dict
from Goodrich.Chapter13.GreedyTextCompression.min_heap import MinHeap
from Goodrich.Chapter14.Tests.init_graph import *
from Goodrich.Chapter14.graph import Graph
Vertex = Graph.Vertex
Edge = Graph.Edge
Int = int
Float = float
Bool = bool


def dijkstra(G: Graph, s: Vertex):
    """Return the record of shortest paths from s to all other vertices in G."""

    @dataclass
    class DistanceEntry: cost: Int|Float; predecessor: Vertex|None; visited: Bool
    distance: Dict[Vertex, DistanceEntry] = dict()
    """Maps each vertex in G to distance properties (cost, predecessor, visited)."""

    unvisited = MinHeap()
    """Priority Queue for ranking the distance of a vertex (key) and said vertex (value)."""

    # Insert starting vertex in unvisited heap and declare distance properties
    unvisited.insert(k=0, v=s)
    distance[s] = DistanceEntry(cost=0, predecessor=None, visited=False)

    # Declare distance records for other nodes
    for vert in G.vertices():
        if vert is not s:
            distance[vert] = DistanceEntry(math.inf, None, False)

    # Begin iterative relaxation and distance updating process
    cur_vert = s
    while len(unvisited) > 0:
        if not distance[cur_vert].visited:                      # If node is yet to be visited...
            for edge in G.incident_edges(cur_vert):             # For each adjacent neighbor...
                weight = edge.element()
                neighbor = edge.opposite(cur_vert)
                if distance[cur_vert].cost + weight < distance[neighbor].cost:
                    distance[neighbor].cost = (                 # Relax/update distance
                            distance[cur_vert].cost + weight)
                    distance[neighbor].predecessor = cur_vert   # Update predecessor
                if not distance[neighbor].visited:              # If vertex has not been visited...
                    unvisited.insert(                           # Insert into univisted heap
                        k=distance[neighbor].cost, v=neighbor)
        distance[cur_vert].visited = True                       # Mark as visited
        cur_vert = unvisited.remove_min()[1]                    # Choose next minimum

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
                  f"{path.cost}\t|\t"
                  f"{path.predecessor.element() if path.predecessor else '$'}\t|\t"
                  f"{path.visited}\t|\t")
