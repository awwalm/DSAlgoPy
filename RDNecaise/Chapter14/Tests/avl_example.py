import random
from RDNecaise.Chapter14.avltree import AVLTree
from RDNecaise.Chapter14.Utilities.utils import *


def inorder_traversal(node):
    if node.left:
        inorder_traversal(node.left)
    print(node.value)
    if node.right:
        inorder_traversal(node.right)

def bfs(level):
    if level.__len__() == 0:
        return
    next_level = []
    for node in level:
        if node:
            print(node.value)
            if node.left: next_level.append(node.left)
            if node.right: next_level.append(node.right)
    del level
    bfs(next_level)


def test():
    tree = AVLTree()
    lim = random.randrange(10, 30)
    vals = random.sample(range(1, lim+1), lim) #[3,8,10,4,1,2,9,6,5,7,17,12,15,21,18,19,13,3,8,10,4,1,2]

    for i in vals:
        print(f"\ncurrent key/value: {i}")
        tree.insert(i, i)
        # print_tree(tree.root())
        print(print_pretty_tree(tree.root()))

    print("Attempting to delete key 36")
    try: tree.delete(36)
    except KeyError as e: print(e)
    print(print_pretty_tree(tree.root()))
    # print_tree(tree.root())

    root_key = tree.root().key
    tree.delete(root_key)
    print(f"Attempting to delete root key/value: {root_key}\nNew root is: {tree.root().key}")
    print(print_pretty_tree(tree.root()))
    # print_tree(tree.root())

    print(f"5 in tree: {5 in tree}")
    print(f"25 in tree: {25 in tree}")
    print(print_pretty_tree(tree.root()))
    # print_tree(tree.root())

    print(f"Attempting to delete a leaf with key: {vals[-1]}")
    tree.delete(vals[-1])
    print(print_pretty_tree(tree.root()))
    # print_tree(tree.root())

    print(f"Attempting to delete internal node with two children: {tree.root().right.key}")
    tree.delete(tree.root().right.key)
    print(print_pretty_tree(tree.root()))
    # print_tree(tree.root())

    print("Inorder traversal:")
    inorder_traversal(tree.root())

    print("BFS (left to right) traversal:")
    bfs([tree.root()])

test()
