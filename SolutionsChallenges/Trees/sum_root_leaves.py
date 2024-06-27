# https://stackoverflow.com/questions/77870059/
# https://leetcode.com/problems/sum-of-root-to-leaf-binary-numbers/description/

import random
from unique_bst import BST
from RDNecaise.Chapter14.Utilities.tree_printer import *


class Solution:
    def sumRootToLeaf(self, root):
        res = []
        out = bin(0)
        self.inorder(root, out, res)
        return sum(int(i,2) for i in res)

    def inorder(self, node, cur_str, output):
        if node:
            cur_str += str(node.value)
            if (not node.right) and (not node.left):
                output.append(cur_str)
                cur_str.replace(cur_str[-1], "")
            self.inorder(node.left, cur_str, output)
            cur_str.replace(cur_str[-1], "")
            self.inorder(node.right, cur_str, output)


def make_binary_values(node):
    if node:
        make_binary_values(node.right)
        node._value = random.randint(0,1)
        node._key = node.value
        make_binary_values(node.left)

def test1():
    tree = BST()
    lim = random.randrange(10, 30)
    vals = random.sample(range(1, lim + 1), lim)
    for i in vals[:10]: tree.insert(i, i)
    make_binary_values(tree.root)
    print_tree(tree.root)
    # print(print_pretty_tree(tree.root))
    print(Solution().sumRootToLeaf(tree.root))


if __name__ == "__main__":
    test1()
    test1()
    test1()
