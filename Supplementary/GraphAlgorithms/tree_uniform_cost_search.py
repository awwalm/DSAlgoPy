"""
Modified Uniform Cost Search (UCS), also known as 'Uninformed A* (A-star) Search'.
Based on Prof. John Levine: https://www.youtube.com/watch?v=dRMvK76xQJI
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
    tree1 = init_tree_graph()
    tree2 = init_bin_tree_graph()

    for tree in tree1, tree2:
        t1 = time.perf_counter()
        ucs_table, ucs_path = find_path_in_tree(*tree)
        t2 = f"{abs(t1 - time.perf_counter()):.3e}"
        print(f"\nTime taken: {t2}")

        path_str = "START :: -> "
        for vert in ucs_path: path_str += vert.element() + " -> "
        print(path_str + "END")

        print("\nNode | Pred | Visited\t|")
        for u in ucs_table:
            path = ucs_table[u]
            print(f"{u.element()}\t | "
                  f"\t{path.predecessor.element() if path.predecessor else '$'}\t| "
                  f"\t{path.visited}\t|")
