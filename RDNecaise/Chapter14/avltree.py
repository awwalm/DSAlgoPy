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
        __slots__ = "_key", "_value", "_parent", "_left", "_right", "_height"

        def __init__(self, key, value, parent, left=None, right=None, height=0):
            self._key = key
            self._value = value
            self._parent: Union[AVLTree._AVLNode, None] = parent
            self._left: Union[AVLTree._AVLNode, None] = left
            self._right: Union[AVLTree._AVLNode, None] = right
            self._height: int = height

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

    # AVL search tree utilities -----------------------------------------------------------------
    def __init__(self):
        self._root: Union[AVLTree._AVLNode, None] = None
        self._stop_node = None   # Height tracker (see insert(), _rebalance(), and _decrement_height()).
        self._size = 0

    def __len__(self):
        return self._size

    def __contains__(self, k):
        return True if self.search(k, self._root)[1] else False

    def root(self):
        return self._root

    def is_empty(self):
        return self._size == 0

    def search(self, key, subtree: _AVLNode):
        if key == subtree.key:
            return subtree, True                                # Successful search
        elif key < subtree.key:
            if subtree.left is not None:
                return self.search(key, subtree.left)
        else:
            if subtree.right is not None:
                return self.search(key, subtree.right)
        return subtree, False                                   # Unsuccessful search

    def insert(self, key, value):
        if self.is_empty():
            self._root = self._AVLNode(key, value, None)
            self._size += 1
            return self._root
        else:
            node, found = self.search(key, self._root)
            if found:
                node.value = value
            else:
                if key < node.key:
                    node.left = self._AVLNode(key, value, node)
                    if node.right is None:                      # If only node at the level
                        self._increment_height(node.left)       # Then increment branch height
                        self._rebalance(node, Path.L, None)      # Consider a rebalance
                else:
                    node.right = self._AVLNode(key, value, node)
                    if node.left is None:
                        self._increment_height(node.right)
                        self._rebalance(node, Path.R, None)
                self._size += 1

    def _increment_height(self, subtree: _AVLNode):
        """Recursively increment each parental node's height until root, or not required."""
        if subtree.parent is not None:
            if subtree.parent.height - subtree.height >= 1:     # A different branch is higher or height is ok
                self._stop_node = subtree.parent                # Assign to self._stop_node
            else:
                subtree.parent.height += 1
                self._increment_height(subtree.parent)

    # noinspection PyMethodMayBeStatic
    def _recompute_height(self, subtree: _AVLNode):
        """Recompute the height of a given node that was recently restructured."""
        if (subtree.left is None) and (subtree.right is None):
            return 0
        elif (subtree.left is None) and (subtree.right is not None):
            return 1 + subtree.right.height
        elif (subtree.left is not None) and (subtree.right is None):
            return 1 + subtree.left.height
        else:
            return 1 + max(subtree.left.height, subtree.right.height)

    def _decrement_height(self, subtree: _AVLNode):
        """Recursively decrement parental node heights until a stop node or root is reached."""
        if (subtree.parent != self._stop_node) and (subtree.parent is not None):                   # Do not process stop node
            if subtree.parent.height - subtree.height == 2:
                subtree.parent.height -= 1
                if subtree != self._root:
                    self._decrement_height(subtree.parent)
        else:
            self._stop_node = None                              # Reset to default

    def _rebalance(self, subtree: _AVLNode, patha: Path, pathb: Union[Path, None]):
        """Perform trinode restructure if required. Any three adjacent nodes
        must maintain the following property in top to bottom order:
         P-->[path a]-->C-->[path b]-->G.
        """
        if subtree == self._root : return                        # Wait for other nodes to be imbalanced
        LH = 0 if subtree.left is None else 1 + subtree.left.height
        RH = 0 if subtree.right is None else 1 + subtree.right.height
        subtree_root = subtree.parent
        child_path = Path.L
        if subtree_root is not None:
            child_path = child_path if subtree is subtree_root.left else Path.R

        if (LH - RH) > 1:                                       # Left imbalance from Path A
            if pathb == Path.R:                                 # LR imbalance
                p, c, g = subtree, subtree.left, subtree.left.right
                t2, t3 = subtree.left.right.left, subtree.left.right.right
                g.left = c                                      # G becomes new subtree root
                g.right = p
                c.right = t2
                p.left = t3
                if t2 is not None: t2.parent = c
                if t3 is not None: t3.parent = p
                p.parent = g
                g.parent = subtree_root                         # Register the parent of new subtree root
                if subtree_root is None:
                    self._root = g
                elif child_path == Path.L:
                    subtree_root.left = g
                else: subtree_root.right = g
                p.height = self._recompute_height(p)            # Recompute STRICTLY in this order: p > c > g
                c.height = self._recompute_height(c)
                g.height = self._recompute_height(g)
                self._decrement_height(g)                       # Adjust the height upwards

            elif pathb == Path.L:                               # LL imbalance
                p, c, g = subtree, subtree.left, subtree.left.left
                t3 = c.right
                c.right = p
                p.left = t3
                if t3 is not None: t3.parent = p
                p.parent = c
                c.parent = subtree_root
                if subtree_root is None:
                    self._root = c
                elif child_path == Path.L:
                    subtree_root.left = c
                else: subtree_root.right = c
                g.height = self._recompute_height(g)
                p.height = self._recompute_height(p)
                c.height = self._recompute_height(c)
                self._decrement_height(c)

        elif (LH - RH) < -1:                                    # Right imbalance from Path A
            if pathb == Path.R:                                 # RR imbalance
                p, c, g = subtree, subtree.right, subtree.right.right
                t2 = c.left
                c.left = p
                p.right = t2
                if t2 is not None: t2.parent = p
                p.parent = c
                c.parent = subtree_root
                if subtree_root is None:
                    self._root = c
                elif child_path == Path.L:
                    subtree_root.left = c
                else: subtree_root.right = c
                p.height = self._recompute_height(p)
                g.height = self._recompute_height(g)
                c.height = self._recompute_height(c)
                self._decrement_height(c)

            elif pathb == Path.L:                               # RL imbalance
                p, c, g = subtree, subtree.right, subtree.right.left
                t2, t3 = subtree.right.left.left, subtree.right.left.right
                g.left = p
                g.right = c
                p.right = t2
                c.left = t3
                if t2 is not None: t2.parent = p
                if t3 is not None: t3.parent = c
                g.parent = subtree_root
                if subtree_root is None:
                    self._root = g
                elif child_path == Path.L:
                    subtree_root.left = g
                else: subtree_root.right = g
                p.height = self._recompute_height(p)
                c.height = self._recompute_height(c)
                g.height = self._recompute_height(g)
                self._decrement_height(g)

        else:                                                   # No imbalance detected, walk upwards
            if subtree is subtree.parent.left:
                self._rebalance(subtree.parent, Path.L, patha)
            else:
                self._rebalance(subtree.parent, Path.R, patha)

