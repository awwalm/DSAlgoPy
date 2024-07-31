"""
Uniform Cost Search (UCS), also known as 'Uninformed A* (A-star) Search'.
Based on Prof. John Levine: https://www.youtube.com/watch?v=dRMvK76xQJI
"""
import math
import time
from dataclasses import dataclass
from collections import OrderedDict
from typing import Set

from Goodrich.Chapter13.GreedyTextCompression.min_heap import MinHeap
from Goodrich.Chapter14.Tests.init_graph import init_directed_graph3
from Goodrich.Chapter14.graph import Graph


@dataclass
class CostRecord:
    cost: int | float
    predecessor: Graph.Vertex | None
    visited: bool


def ucs(G: Graph, start: Graph.Vertex, goals: Set[Graph.Vertex]):
    cost_heap = MinHeap[int, Graph.Vertex]()
    cost_table: OrderedDict[Graph.Vertex, CostRecord] = OrderedDict()
    scored: Set[Graph.Vertex] = set()

    for v in G.vertices():
        cost_table[v] = CostRecord(cost=math.inf, predecessor=None, visited=False)

    cost_table[start].cost = 0
    cost_heap.insert(k=0, v=start)

    while len(cost_heap) > 0 :
        current_cost, current_vertex = cost_heap.remove_min()

        if cost_table[current_vertex].visited:
            continue

        cost_table[current_vertex].visited = True

        if current_vertex in goals:
            scored.add(current_vertex)
            if len(scored) == len(goals):
                break   # All goal states reached, terminate
            continue    # Found a goal state, don't expand this node

        for edge in G.incident_edges(current_vertex):
            neighbor = edge.opposite(current_vertex)
            new_cost = current_cost + edge.element()

            if not cost_table[neighbor].visited and new_cost < cost_table[neighbor].cost:
                cost_table[neighbor].cost = new_cost
                cost_table[neighbor].predecessor = current_vertex
                cost_heap.insert(k=new_cost, v=neighbor)

    return cost_table



if __name__ == "__main__":
    t1 = time.perf_counter()
    ucs_table = ucs(*init_directed_graph3())
    t2 = f"{abs(t1 - time.perf_counter()):.3e}"
    print(f"Time taken: {t2}\n")

    print("\nNode | Dist | Pred  | Visited\t|")
    for u in ucs_table:
        path = ucs_table[u]
        print(f"  {u.element()}  |\t"
              f"{path.cost}\t|\t"
              f"{path.predecessor.element() if path.predecessor else '$'}\t|\t"
              f"{path.visited}\t|\t")
