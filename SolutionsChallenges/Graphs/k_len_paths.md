A _backtracking_<sup>*</sup> version of the DFS traversal used by [Goodrich, Tamassia & Goldwasser (2013)](https://www.amazon.com/dp/1118290275) in **Section 14.3.1 - 14.3.2**, can be modified and adapted to solve this problem. 

We also want to keep track of visited vertices and corresponding **_tree edges_** (or discovery edges) by the use of an ordered Hash Table (which implies your vertex must be hashable), which therein prevents cyclic traversal (by using an **Adjacency Map** to represent the Graph, we can query traversed vertices in _O_(1) time and omit *back edges*).

This will ultimately produce **the (implied) [strongly connected components](https://en.wikipedia.org/wiki/Strongly_connected_component) (or [connected components](https://en.wikipedia.org/wiki/Component_(graph_theory)) in the case of an undirected graph) reachable by traversing at most _k_-1 edges** in the graph, by invoking DFS on a starting vertex _s_, and then recursively calling DFS on all incidental discovery edge vertices at the specified _k_-range.

<sub>* We populate a concurrent path accumulator for every valid recursive DFS call (when _traversed edges_ < _k_) , and then backtrack and pop the corresponding retraction edges (triggered when _traversed edges_ >= _k_, until a new edge is traversed and accumulated again) as the recursion unwinds.</sub>

<hr>

The following solution uses an Adjacency Map representation of a Graph as presented by Goodrich et al. (pp. 635-637). For brevity, the Graph implementation which is 100% compatible with this algorithm with zero dependencies can be found here: [`graph.py`](https://github.com/awwalm/DSAlgoPy/blob/master/Goodrich/Chapter14/graph.py).

Methods `Graph.insert_vertex()`, `Graph.insert_edge()`, `Edge.opposite()`, `Edge.endpoints()` all run in _O_(1) time, except `Graph.incident_edges(v)` which takes _O_(_outgoing-degree_(_v_)) time.

Initially, `klen_dfs()` ought to take _O_(n) time at the worst case (when finding a vertex reachable in _k_ edges requires traversing the whole graph). However, saving each unique path (`path_array.append(p[:])`) incites some necessary recomputation amassing to a total of approximately _summation_(_k_) operations. Overall, `klen_dfs()` takes _O_(_k_<sup>2</sup> + n) time in worst case.

```python
from collections import OrderedDict
from typing import List
# noinspection PyUnresolvedReferences
from graph import Graph


def init_graph():
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


def klen_dfs(G: Graph, s: Graph.Vertex, k: int):
    """Report all paths (edge lists) less than length k.
    G - Adjacency Map Graph ADT
    s - Starting vertex
    k - Path length limit (actual limit = k-1)
    """
    discovery_edges: OrderedDict[Graph.Vertex, Graph.Edge] = OrderedDict()
    path_accummulator: List[Graph.Edge] = []
    path_array: List[List[Graph.Edge]] = []

    def dfs(g: Graph, u: Graph.Vertex, discovered, klen, p):
        """Traditional DFS with addtional params.
        u - A vertex in G
        p - Concurrent path array of less than k edges
        """
        if klen < k:
            for e in g.incident_edges(u, outgoing=True):
                v = e.opposite(u)
                if not discovered.get(v):  # Cyclic traversal prevention
                    discovered[v] = e
                    p.append(e)
                    path_array.append(p[:])
                    dfs(g, v, discovered, klen + 1, p)
                    p.pop()
                    discovered.pop(v)

    dfs(G, s, discovery_edges, 1, path_accummulator)
    return path_array


if __name__ == "__main__":
    # For graph produced by init_graph(), all k >= 3 has same results
    for K in range(1, 4):
        digraph, start = init_graph()
        paths = klen_dfs(digraph, start, K)
        formatted_paths = []
        for path in paths:
            formatted_path = []
            for edge in path:
                endpoints = edge.endpoints()
                formatted_path.append((
                    endpoints[0].element(), endpoints[1].element()))
            formatted_paths.append(formatted_path)
        print(f"ALL paths when k = {K} (i.e of length {K - 1} < k length)")
        print(*formatted_paths, sep="\n")
        print()
```

**Output:**

```
ALL paths when k = 1 (i.e of length 0 < k length)

ALL paths when k = 2 (i.e of length 1 < k length)
[(1, 2)]
[(1, 3)]

ALL paths when k = 3 (i.e of length 2 < k length)
[(1, 2)]
[(1, 3)]
[(1, 3), (3, 2)]
[(1, 3), (3, 4)]
```

**Visualization of _simple_ valid paths less than length _k_=3 when _s_=1**

[![Valid Edges][1]][1]


  [1]: https://i.sstatic.net/JpAuPCi2.png