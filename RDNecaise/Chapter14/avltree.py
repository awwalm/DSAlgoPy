"""A proper implementation of an AVL Tree with proper coding standards.
This version was adapted from https://github.com/zinchse/AVLTree.
The implementation from the book contains cryptic/indecipherable bugs,
hence, not recommended for usage.

Implemented public/classic methods:
+ insert(key, value)
+ delete(key)
+ search(key)
+ predecessor(key)

Tree properties:
+ root()
+ __len__()
+ __contains__()

Node/subtree properties:
+ key()
+ value()
+ height()
+ left()
+ right()
"""
import ast
import inspect
from typing import Union


class AVLTree:
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


    # AVL search tree utilities -----------------------------------------------------------------
    # noinspection PyUnresolvedReferences
    def __init__(self):
        self._root: Union[AVLTree._AVLNode, None] = None
        self._size = 0
        frame = inspect.stack()[1]
        st = ast.parse(frame.code_context[0].strip())
        stmt = st.body[0]
        assert(isinstance(stmt, ast.Assign))
        self.__IDENTIFIER = stmt.targets[0].id              # Instance variable/identifier name
        del frame, st, stmt

    def __len__(self):
        return self._size

    def __contains__(self, k):
        return True if k == self.search(k, self._root).key else False

    def root(self):
        return self._root

    def is_empty(self):
        return self._size == 0

    def search(self, key, subtree: _AVLNode):
        """Returns the subtree containing a given key, or nearest subtree if key not found."""
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
        """Returns the predecessor of a subtree, or same subtree if no predecessor."""
        if subtree and subtree.left:
            subtree = subtree.left
            while subtree is not None:
                if subtree.right:
                    subtree = subtree.right
                else:
                    break
        elif subtree and subtree.parent:
            while subtree:
                if subtree.parent and subtree.parent.key < subtree.key:
                    return subtree.parent
                subtree = subtree.parent
        return subtree

    def insert(self, key, value):
        """Insert a unique node containing key and value into the tree."""
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
                elif key > node.key:
                    node.right = self._AVLNode(key, value, node)
                    if node.left is None:
                        self._update_height(node)
                self._size += 1

    def _remove_full_node(self, subtree: _AVLNode):
        """Heuristic for deleting internal node with two children."""
        predecessor = self.predecessor(subtree)
        subtree.key, subtree.value = predecessor.key, predecessor.value
        if predecessor.height == 0:
            self._remove_leaf_node(predecessor)
        else:
            self._remove_half_node(predecessor)

    def _remove_half_node(self, subtree: _AVLNode):
        """Heuristic for deleting internal node with one child."""
        parent = subtree.parent
        if parent:
            if parent.left == subtree:
                parent.left = subtree.right or subtree.left
            else:
                parent.right = subtree.right or subtree.left
            if subtree.left:
                subtree.left.parent = parent
            else:
                subtree.right.parent = parent
            self._recompute_height(parent)
        # Consider a rebalance
        subtree = parent
        while subtree:
            if self._get_balance(subtree) < -1 or self._get_balance(subtree) > 1:
                self._rebalance(subtree)
            subtree = subtree.parent

    def _remove_leaf_node(self, subtree: _AVLNode):
        """Heuristic for deleting leaf node."""
        parent = subtree.parent
        if parent:
            if parent.left == subtree:
                parent.left = None
            else:
                parent.right = None
            self._recompute_height(parent)
        else:
            self._root = None                               # Singleton root node
        # Consider a rebalance
        subtree = parent
        while subtree:
            if self._get_balance(subtree) < -1 or self._get_balance(subtree) > 1:
                self._rebalance(subtree)
            subtree = subtree.parent

    def delete(self, key):
        """Remove subtree with the given key from the tree, or raise key error if not found."""
        node = self.search(key, self._root)
        if key != node.key:
            raise KeyError(f"No key `{key}` in {self} assigend to `{self.__IDENTIFIER}`")
        else:
            if node.left and node.right:                    # Subtree has two children
                self._remove_full_node(node)
            elif node.right or node.left:                   # Subtree has at least one child
                self._remove_half_node(node)
            else:                                           # Leaf node: subtree has no children
                self._remove_leaf_node(node)
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
        if node.height == 0:                                # Update required (this node has a child)
            while node is not None:
                node.height = self._get_max_height(node) + 1
                bfactor = self._get_balance(node)
                if bfactor < -1 or bfactor > 1:             # Imbalance detected, do trinode restructure
                    self._rebalance(node)
                    return
                node = node.parent                          # Keep crawling up

    def _rebalance(self, subtree: _AVLNode):
        """Perform trinode restructure (double rotation) if required."""
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
