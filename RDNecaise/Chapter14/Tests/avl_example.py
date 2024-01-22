import random
from RDNecaise.Chapter14.avltree import AVLTree

tree = AVLTree()
for i in random.sample(range(1,11), 10):
    print(f"current key/value: {i}")
    tree.insert(i, i)

print(f"5 in tree: {5 in tree}")
print(f"15 in tree: {15 in tree}")

def inorder_traversal(node):
    if node.left:
        inorder_traversal(node.left)
    print(node.value)
    if node.right:
        inorder_traversal(node.right)

inorder_traversal(tree.root())