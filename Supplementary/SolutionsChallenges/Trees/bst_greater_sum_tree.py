# https://stackoverflow.com/questions/66018493/
# https://leetcode.com/problems/binary-search-tree-to-greater-sum-tree/description/
from RDNecaise.Chapter14.Utilities.tree_printer import print_pretty_tree
from RDNecaise.Chapter14.avltree import AVLTree


class Solution:
    agsum = 0
    def reversed_inorder(self, node):
        if node:
            if node.right: self.reversed_inorder(node.right)
            node.value += self.agsum
            self.agsum = node.value
            if node.left: self.reversed_inorder(node.left)


    def inorder(self, node, output):
        if node:
            if node.left: self.inorder(node.left, output)
            output.append(node)
            if node.right: self.inorder(node.right, output)

    def bfs(self, level, output):
            if len(level) == 0: return output
            next_level = []
            for node in level:
                if node:
                    output.append(node)
                    if node.left: next_level.append(node.left)
                    if node.right: next_level.append(node.right)
                    self.bfs(next_level, output)

    def bstToGst(self, root):
        nodes = []
        self.inorder(root, nodes)
        n = len(nodes) - 2
        while n > -1:
            nodes[n].value += nodes[n + 1].value
            n -= 1
        return root


def test1():
    tree = AVLTree()
    for i in [4, 1, 6, 0, 2, 5, 7, 3, 8]: tree.insert(i, i)
    print(print_pretty_tree(tree.root()))
    Solution().bstToGst(tree.root())
    print(print_pretty_tree(tree.root()))

def test2():
    tree = AVLTree()
    for i in [4, 1, 6, 0, 2, 5, 7, 3, 8]: tree.insert(i, i)
    print(print_pretty_tree(tree.root()))
    Solution().reversed_inorder(tree.root())
    print(print_pretty_tree(tree.root()))

if __name__ == "__main__":
    test2()
