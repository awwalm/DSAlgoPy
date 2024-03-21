"""
Given the set of keys {6, 7, 1, 4, 2}, how many unique binary search trees of height 2
are possible? Draw the trees. Assume that the height of the root-node is zero.

From Quora: https://qr.ae/psrOXE
"""
import itertools
from typing import Union, List
from RDNecaise.Chapter14.Utilities.utils import print_pretty_tree


class BST:

    # Composition Pattern: Nested private Node instance cannot exist independent of BST object
    class _Node:
        __slots__ = "_key", "_value", "_parent", "_left", "_right", "_height"
        def __init__(self, key, value, parent):
            self._key = key
            self._value = value
            self._parent = parent
            self._left = None
            self._right = None
            self._height = 0
        @property
        def key(self):
            return self._key
        @property
        def value(self):
            return self._value
        @property
        def right(self):
            return self._right
        @property
        def left(self):
            return self._left
        @property
        def height(self):
            return self._height
        @property
        def parent(self):
            return self._parent


    # BST methods and properties (deletion not implemented)
    def __init__(self):
        self._root: Union[BST._Node, None] = None
        self._size = 0

    @property
    def root(self):
        return self._root

    @property
    def size(self):
        return self._size

    def empty(self):
        return self._size == 0

    # noinspection PyMethodMayBeStatic
    def _update_height(self, subtree: _Node):   # Required by tree-printing heuristic
        if (not subtree.left) and (not subtree.right):
            subtree._height = 0
        elif subtree.left and not subtree.right:
            subtree._height = 1 + subtree.left.height
        elif subtree.right and not subtree.left:
            subtree._height = 1 + subtree.right.height
        else:                                   # Both subtrees are present
            subtree._height = 1 + max(subtree.left.height, subtree.right.height)

    def insert(self, key, value):
        max_height = 0
        if self.empty():
            self._root = self._Node(key, value, None)
            self._size = 1
        else:
            subtree, max_height = self.search(self._root, key, value, 0)
            if subtree.key == key:
                subtree._value = value          # Key already present in tree, update only value
                return max_height
            elif key < subtree.key:
                subtree._left = self._Node(key, value, subtree)
            else:                               # key > subtree.key
                subtree._right = self._Node(key, value, subtree)
            self._size += 1
            while subtree:
                self._update_height(subtree)
                subtree = subtree.parent
        return max_height

    def search(self, subtree: _Node, key, value, max_height: int):
        if subtree.key == key and subtree.value == value:
            return subtree, max_height          # Successful search
        elif key < subtree.key:
            if subtree.left:
                return self.search(subtree.left, key, value, max_height+1)
        elif key > subtree.key:
            if subtree.right:
                return self.search(subtree.right, key, value, max_height+1)
        return subtree, max_height              # Unsuccessful search

    def _bfs(self, level: List[_Node], traversed: List[List[_Node]]):
        if len(level) > 0:
            next_level, this_level = [], []
            for node in level:
                if node: this_level.append(node.value)
                if node.left: next_level.append(node.left)
                if node.right: next_level.append(node.right)
            traversed.append(this_level)
            del level                           # Free memory
            self._bfs(next_level, traversed)

    def traverse(self):
        values = []
        self._bfs([self._root], values)
        return values


def get_unique_bsts(keys: set, max_height: int):
    permutations = itertools.permutations(keys) # All possible permutations of keys
    unique_bsts = set()                         # Unique BSTs of height max_height based on given keys
    bfs_values = list()                         # BFS sequence of keys to verify structural uniqueness
    non_unique_bsts = set()                     # [Optional] All BSTs of height max_height

    for keys in permutations:
        bst = BST()
        height = 0
        for k in keys:
            height = bst.insert(k, k)
            if height > max_height-1:           # Max height exceeded; halt BST construction
                break
        if height == max_height-1:
            non_unique_bsts.add(bst)
            bfs_val = bst.traverse()
            print(bfs_val)                      # BFS sequence for all BSTs having a height of max_height
            if bfs_val not in bfs_values:
                unique_bsts.add(bst)            # BSTs filtered for uniqueness
                bfs_values.append(bfs_val)

    print(f"All BSTs of height {max_height} = {len(non_unique_bsts)}")

    for tree in unique_bsts: print(print_pretty_tree(tree.root))

    return len(unique_bsts)


if __name__ == '__main__':
    print(
        f"Number of unique BSTs of height 2 from set of keys <6, 7, 1, 4, 2> = "
        f"{get_unique_bsts(keys={6, 7, 1, 4, 2}, max_height=2)}"
    )
