"""Binary Tree Rendering using Matplotlib and NetworkX."""
from Goodrich.Chapter13.GreedyTextCompression.min_heap import MinHeap

import matplotlib.pyplot as plt
import networkx as nx
import math

class BinaryTree:
    def __init__(self, value):
        self.value = value
        self.left = None
        self.right = None

def build_tree():
    root = BinaryTree(1)
    root.left = BinaryTree(2)
    root.right = BinaryTree(3)
    root.left.left = BinaryTree(4)
    root.left.right = BinaryTree(5)
    root.right.left = BinaryTree(6)
    root.right.right = BinaryTree(7)
    return root

# noinspection PyTypeChecker
def plot_tree(tree, pos=None, parent=None, angle=0, depth=0, depth_step=math.pi/6, angle_step=math.pi/6, **kwargs):
    if pos is None:
        pos = {}
    if tree:
        if parent is None:
            pos[tree.value] = (0, 0)
        else:
            x_parent, y_parent = pos[parent.value]
            radius = 1.5 ** -depth  # Adjust the radius based on the depth
            x_offset = math.sin(angle) * radius
            y_offset = -math.cos(angle) * radius  # Flip the y-coordinate
            pos[tree.value] = (x_parent + x_offset, y_parent + y_offset)
        plot_tree(
            tree.left,
            pos,
            tree,
            angle - angle_step / (depth + 1),
            depth + 1,
            depth_step,
            angle_step, **kwargs
        )
        plot_tree(
            tree.right,
            pos,
            tree,
            angle + angle_step / (depth + 1),
            depth + 1,
            depth_step,
            angle_step, **kwargs
        )
    return pos

def draw_binary_tree(tree):
    pos = plot_tree(tree)
    plt.figure(figsize=(8, 6))
    G = nx.Graph()
    for node, position in pos.items():
        G.add_node(node, pos=position)
    for node, position in pos.items():
        if node != 1:  # Skip root node since it has no parent
            parent = get_parent(tree, node)
            # if parent: parent_position = pos[parent.value]
            if parent: G.add_edge(node, parent.value)
    pos = nx.get_node_attributes(G, 'pos')
    nx.draw(G, pos, labels={node: node for node in pos.keys()}, **{
        'node_size': 500, # 5000
        'node_color': 'lightblue',
        'node_shape': 'o',
        'font_size': 10,
        'with_labels': True
    })
    plt.title("Binary Tree")
    plt.show()

def get_parent(tree, value):
    if tree is None:
        return None
    if (tree.left is not None and tree.left.value == value) or (tree.right is not None and tree.right.value == value):
        return tree
    left_parent = get_parent(tree.left, value)
    if left_parent is not None:
        return left_parent
    return get_parent(tree.right, value)

# Example usage
tree1 = build_tree()
draw_binary_tree(tree1)


if __name__ == "__main__":
    A = [10, 51, 2, 18, 4, 31, 13, 5, 23, 64, 29]
    B = [4, 8, 15, 16, 23, 42]
    C = [23, 34, 78, -1, 6, 90, 343, 5]
    D = [1, 5, 18, 5, 6, 1, 20]
    for data in A, B, C, D:
        heap = MinHeap()
        for d in data: heap.insert(d, d)
        t = heap.get_tree()
        draw_binary_tree(t)
