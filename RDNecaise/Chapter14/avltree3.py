"""A proper implementation of an AVL Tree with proper coding standards too.
The implementation from the book contains cryptic/indecipherable bugs."""

from enum import Enum, unique, auto
from typing import Union

@unique
class Path(Enum):
    L = auto()
    R = auto()

class AVLTree:
    """An AVL Tree."""

    # Nonpublic node class -----------------------------------------------------------------
    class _AVLNode:
        __slots__ = "_key", "_value", "_parent", "_left", "_right", "_height", "_node_size"

        def __init__(self, key, value, parent, left=None, right=None, height=0):
            self._key = key
            self._value = value
            self._parent: Union[AVLTree._AVLNode, None] = parent
            self._left: Union[AVLTree._AVLNode, None] = left
            self._right: Union[AVLTree._AVLNode, None] = right
            self._height: int = height
            self._node_size = 1     # Total number of nodes rooted in the subtree including itself

        @property
        def key(self):
            return self._key

        @property
        def value(self):
            return self._value

        @property
        def left(self):
            return self._left

        @property
        def right(self):
            return self._right

        @property
        def parent(self):
            return self._parent

        @property
        def height(self):
            return self._height

        @property
        def node_size(self):
            return self._node_size

        @key.setter
        def key(self, k):
            self._key = k

        @value.setter
        def value(self, v):
            self._value = v

        @left.setter
        def left(self, l):
            self._left = l

        @right.setter
        def right(self, r):
            self._right = r

        @parent.setter
        def parent(self, p):
            self._parent = p

        @height.setter
        def height(self, h):
            self._height = h

        @node_size.setter
        def node_size(self, ns):
            self._node_size = ns

    # AVL search tree utilities -----------------------------------------------------------------
    def __init__(self):
        self._root: Union[AVLTree._AVLNode, None] = None
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, k):
        return True if k == self.search(k, self._root).key else False

    def root(self):
        return self._root

    def is_empty(self):
        return self._size == 0

    def search(self, key, subtree: _AVLNode):
        if key == subtree.key:
            return subtree                                  # Successful search
        elif key < subtree.key:
            if subtree.left is not None:
                return self.search(key, subtree.left)
        else:
            if subtree.right is not None:
                return self.search(key, subtree.right)
        return subtree                                      # Unsuccessful search

    # noinspection PyMethodMayBeStatic
    def predecessor(self, subtree: _AVLNode):
        if subtree and subtree.left: subtree = subtree.left
        while subtree is not None:
            if subtree.right:
                subtree = subtree.right
            else:
                break
        return subtree

    def insert(self, key, value):
        if self.is_empty():
            self._root = self._AVLNode(key, value, None)
            self._size += 1
        else:
            node = self.search(key, self._root)
            if key == node.key:
                node.value = value
            else:
                if key < node.key:
                    node.left = self._AVLNode(key, value, node)
                    if node.right is None:                  # If only node at the level, increment height ↙
                        self._update_height(node)           # ↘ upwards until inbalanced node
                else:
                    node.right = self._AVLNode(key, value, node)
                    if node.left is None:
                        self._update_height(node)
                self._size += 1

    def delete(self, key):
        node = self.search(key, self._root)
        if key != node.key:
            raise KeyError(f"Key `{key}` not in AVLTree instance {self}")
        else:
            if node.left and node.right:
                ...
            elif node.right or node.left:
                self._remove_
            else:   # Leaf node
                self._remove_leaf(node)
            self._size -= 1



    # noinspection PyMethodMayBeStatic
    def _get_balance(self, subtree: _AVLNode):
        """Return the balance factor of a subtree."""
        left_height = 0 if subtree.left is None else 1 + subtree.left.height
        right_height = 0 if subtree.right is None else 1 + subtree.right.height
        return left_height - right_height

    # noinspection PyMethodMayBeStatic
    def _get_max_height(self, subtree: _AVLNode):
        """Obtains the highest height between the children of a subtree."""
        if (subtree.left is None) and (subtree.right is None):
            return 0
        elif (subtree.left is None) and (subtree.right is not None):
            return subtree.right.height
        elif (subtree.left is not None) and (subtree.right is None):
            return subtree.left.height
        else:
            return max(subtree.left.height, subtree.right.height)

    # noinspection PyMethodMayBeStatic
    def _recompute_height(self, subtree: _AVLNode):
        """Recompute the height of a given node whose branch grew taller."""
        changed = True
        while changed and subtree is not None:
            old_height = subtree.height
            subtree.height = 1 + self._get_max_height(subtree) if (subtree.left or subtree.right) else 0
            changed = subtree.height != old_height
            subtree = subtree.parent

    def _update_height(self, subtree: _AVLNode):
        """Increment height upwards until an imbalanced node is reached, and subsequently balanced."""
        node = subtree
        node.node_size += 1                                 # Now contains extra child as invoked by insert()
        if node.height == 0:                                # Update required (this node has a child)
            while node is not None:
                node.height = self._get_max_height(node) + 1
                bfactor = self._get_balance(node)
                if bfactor < -1 or bfactor > 1:             # Imbalance detected, do trinode restructure
                    self._rebalance(node)
                    return
                node = node.parent                          # Keep crawling up

    def _rebalance(self, subtree: _AVLNode):
        """Perform trinode restructure (double rotation) if required.
        """
        A = subtree
        F = A.parent
        if self._get_balance(subtree) == -2:                # Right imbalance detected
            if self._get_balance(subtree.right) <= 0:       # RR imbalance
                B = A.right
                A.right = B.left
                if A.right:
                    A.right.parent = A
                B.left = A
                A.parent = B
                if F is None:
                    self._root = B
                    self._root.parent = None
                else:
                    if F.right == A:
                        F.right = B
                    else:
                        F.left = B
                    B.parent = F
                self._recompute_height(A)
            else:                                           # RL imbalance
                B = A.right
                C = B.left
                B.left = C.right
                if B.left:
                    B.left.parent = B
                A.right = C.left
                if A.right:
                    A.right.parent = A
                C.right = B
                B.parent = C
                C.left = A
                A.parent = C
                if F is None:
                    self._root = C
                    self._root.parent = None
                else:
                    if F.right == A:
                        F.right = C
                    else:
                        F.left = C
                    C.parent = F
                self._recompute_height(A)
                self._recompute_height(B)

        else:                                               # Left imbalance detected
            if self._get_balance(subtree.left) >= 0:        # LL imbalance
                B = A.left
                A.left = B.right
                if A.left:
                    A.left.parent = A
                B.right = A
                A.parent = B
                if F is None:
                    self._root = B
                    self._root.parent = None
                else:
                    if F.right == A:
                        F.right = B
                    else:
                        F.left = B
                    B.parent = F
                self._recompute_height(A)

            else:                                           # LR imbalance
                B = A.left
                C = B.right
                A.left = C.right
                if A.left:
                    A.left.parent = A
                B.right = C.left
                if B.right:
                    B.right.parent = B
                C.left = B
                B.parent = C
                C.right = A
                A.parent = C
                if F is None:
                    self._root = C
                    self._root.parent = None
                else:
                    if F.right == A:
                        F.right = C
                    else:
                        F.left = C
                    C.parent = F
                self._recompute_height(A)
                self._recompute_height(B)

