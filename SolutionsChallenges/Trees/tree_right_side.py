# https://stackoverflow.com/questions/72918442
# https://leetcode.com/problems/binary-tree-right-side-view/description/

import random
from unique_bst import BST
from RDNecaise.Chapter14.Utilities.tree_printer import *
from RDNecaise.Chapter14.avltree import AVLTree


class Solution:
    def rightSideView(self, level, output):
        if len(level) == 0: return output
        output.append(level[len(level) - 1])
        next_level = []
        for node in level:
            if node:
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
        self.rightSideView(next_level, output)


def test1():
    tree = BST()
    lim = random.randrange(10, 30)
    vals = random.sample(range(1, lim + 1), lim)
    for i in vals[:10]: tree.insert(i, i)
    print_tree(tree.root)
    rsv = []
    Solution().rightSideView([tree.root], rsv)
    for node in rsv: print(node.value)

def test2():
    tree = AVLTree()
    for i in [4, 1, 6, 0, 2, 5, 7, 3, 8]: tree.insert(i, i)
    print(print_pretty_tree(tree.root()))
    rsv = []
    Solution().rightSideView([tree.root()], rsv)
    for node in rsv: print(node.value)

if __name__ == "__main__":
    test1()
    test1()
    test1()
    test2()
