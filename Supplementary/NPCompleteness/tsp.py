"""
Traveling Salesman solution (with visualization) using Nearest Neighbor Heuristic.
Credits: https://www.youtube.com/watch?v=r9lzHs2rZDc
"""

import random
from typing import List

import matplotlib.pyplot as plt
from networkx.algorithms.approximation import traveling_salesman_problem
import networkx as nx
Graph = nx.classes.graph.Graph
EdgeView = nx.classes.graph.EdgeView
NodeView = nx.classes.graph.NodeView
from Goodrich.Chapter14.Tests.init_graph import init_complete_graph

def plot_graph_step(G: Graph, tour: List[EdgeView], current_node: List[NodeView], pos):
    plt.clf()
    nx.draw(G, pos, with_labels=True, node_color="lightblue", node_size=500)
    path_edges = list(zip(tour, tour[1:]))
    nx.draw_networkx_edges(G, pos, edgelist=path_edges, edge_color="red", width=2)
    nx.draw_networkx_nodes(G, pos, nodelist=[current_node], node_color="green", node_size=500)

    edge_labels = nx.get_edge_attributes(G, "weight")
    nx.draw_networkx_edge_labels(G, pos, edge_labels=edge_labels)

    plt.pause(0.5)
    

def calculate_tour_cost(G: Graph, tour: List[EdgeView]):
    return sum(G[tour[i]][tour[i+1]]["weight"] for i in range(len(tour) - 1))


def nn_tsp(G: Graph, start_node=None):
    if not start_node:
        start_node = random.choice(list(G.nodes()))

    pos = nx.spring_layout(G)
    plt.ion()
    plt.show()

    unvisited = set(G.nodes())
    unvisited.remove(start_node)
    tour = [start_node]
    current_node = start_node
    plot_graph_step(G, tour, current_node, pos)

    while unvisited:
        next_node = min(unvisited, key=lambda node: G[current_node][node]["weight"])
        unvisited.remove(next_node)
        tour.append(next_node)
        current_node = next_node
        plot_graph_step(G, tour, current_node, pos)

    tour.append(start_node)
    plot_graph_step(G, tour, current_node, pos)

    print(tour)
    tour_cost = calculate_tour_cost(G, tour)
    print(f"Construction Heuristic Tour Cost: {tour_cost}")

    plt.ioff()
    plt.show()



if __name__ == "__main__":
    cg = init_complete_graph(n=10)

    approx_tour = traveling_salesman_problem(cg, cycle=True)
    approx_cost = calculate_tour_cost(cg, approx_tour)
    print(approx_tour)
    print(f"Approximation cost: {approx_cost}")

    print(cg.edges())
    nn_tsp(cg, 0)
