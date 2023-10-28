"""Tests for the LinkedBinaryTree class from Code Fragment 8.8-8.11."""
from pprint import pprint
from Goodrich.Chapter8.linked_binary_tree import LinkedBinaryTree
import inspect

lbt = LinkedBinaryTree()
# pprint(inspect.getmembers(lbt))
pprint(vars())
lbt._add_root(1)
node = lbt.root()
for i in range(2,11):
    node = lbt._add_left(node, i)
    