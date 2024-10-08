"""
Uniform-Cost Search (UCS) adapted for tree-like graphs.
Based on UCS by Prof. John Levine: https://www.youtube.com/watch?v=dRMvK76xQJI
Full explanation: https://stackoverflow.com/a/78889797/13488161
"""

import time
from dataclasses import dataclass
from collections import deque, OrderedDict
from typing import List, Optional, Tuple

from Goodrich.Chapter14.Tests.init_graph import init_bin_tree_graph, init_tree_graph
from Goodrich.Chapter14.graph import Graph


@dataclass
class PathRecord:
    predecessor: Optional[Graph.Vertex]
    visited: bool

def find_path_in_tree(G: Graph, start: Graph.Vertex, goal: Graph.Vertex) -> Tuple[
    OrderedDict[Graph.Vertex, PathRecord], List[Graph.Vertex | None]]:
    queue = deque([start])
    path_table: OrderedDict[Graph.Vertex, PathRecord] = OrderedDict()

    for v in G.vertices():
        path_table[v] = PathRecord(predecessor=None, visited=False)

    path_table[start].visited = True

    while queue:
        current_node = queue.popleft()

        if current_node == goal:
            break  # Goal found, terminate search

        for edge in G.incident_edges(current_node):
            child = edge.opposite(current_node)

            if not path_table[child].visited:
                path_table[child].visited = True
                path_table[child].predecessor = current_node
                queue.append(child)

    # Reconstruct the path_list from goal to start
    path_list = []
    current_node = goal
    while current_node:
        path_list.append(current_node)
        current_node = path_table[current_node].predecessor

    return path_table, path_list[::-1]  # Return reversed path_list (from start to goal)



if __name__ == "__main__":
    p1, p2, p3 = None, None, None   # Start states
    q1, q2, q3 = None, None, None   # Goal states

    tree1 = init_bin_tree_graph()   # Example 1
    for vert in tree1.vertices():   # [S,A,B,C,D,E,F,G1,G2,G3]
        if vert.element() == "A": p1 = vert
        elif vert.element() == "E": q1 = vert
        elif vert.element() == "S": p2 = vert
        elif vert.element() == "G3": q2 = vert

    tree2 = init_tree_graph()       # Example 2
    for vert in tree2.vertices():   # [S,A,B,C,D,E,F,G,H,I,J,K,L,M]
        if vert.element() == "K": p3 = vert
        elif vert.element() == "F": q3 = vert

    for example in (tree1, p1, q1), (tree1, p2, q2), (tree2, p3, q3):
        t1 = time.perf_counter()
        ucs_table, ucs_path = find_path_in_tree(*example)
        t2 = f"{abs(t1 - time.perf_counter()):.3e}"
        print(f"\nTime taken: {t2}")

        path_str = "START :: -> "
        for vert in ucs_path: path_str += vert.element() + " -> "
        print(path_str + "END")

        print("\nNode | Pred | Visited\t|")
        for u in ucs_table:
            path = ucs_table[u]
            print(f" {u.element()}\t | "
                  f"\t{path.predecessor.element() if path.predecessor else '$'}\t| "
                  f"\t{path.visited}\t|")

        print("="*60)
