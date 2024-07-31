"""Dijkstra's Single Source Shortest Path Algorithm."""

import math
import time
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

    unvisited: MinHeap[Int, Vertex] = MinHeap()
    """Priority Queue for ranking the distance of a vertex (key) and said vertex (value)."""

    # Declare distance records for other nodes
    for vert in G.vertices():
        distance[vert] = DistanceEntry(math.inf, None, False)

    # Insert starting vertex in unvisited heap and declare distance properties
    unvisited.insert(k=0, v=s)
    distance[s] = DistanceEntry(cost=0, predecessor=None, visited=False)

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
                if not distance[neighbor].visited:              # If neighbor has not been visited...
                    unvisited.insert(                           # Insert into univisted heap
                        k=distance[neighbor].cost, v=neighbor)
        distance[cur_vert].visited = True                       # Mark as visited
        cur_vert = unvisited.remove_min()[1]                    # Choose next minimum-edge vertex

    # Marks last-reachable vertex as visited when it has no outgoing edges (see init_directed_graph2())
    if len(unvisited) == 0 and not distance[cur_vert].visited:
        distance[cur_vert].visited = True

    return distance



if __name__ == "__main__":
    t1 = time.perf_counter()
    path1 = dijkstra(*init_undirected_graph2())
    t2 = f"{abs(t1 - time.perf_counter()):.3e}"
    t3 = time.perf_counter()
    path2 = dijkstra(*init_directed_graph2())
    t4 = f"{abs(t3 - time.perf_counter()):.3e}"
    print(f"Time taken\nUG2: {t2}\nDG2: {t4}")
    path3 = dijkstra(*init_undirected_graph3())
    path4 = dijkstra(*init_directed_graph3()[:2])

    for paths in path1, path2, path3, path4:
        print("\nNode | Dist | Pred  | Visited\t|")
        for k in paths:
            path = paths[k]
            print(f"{k.element()}\t|\t"
                  f"{path.cost}\t|\t"
                  f"{path.predecessor.element() if path.predecessor else '$'}\t|\t"
                  f"{path.visited}\t|\t")
