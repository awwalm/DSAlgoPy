"""Code Fragment 8.8-8.11: The ``LinkedBinaryTree`` class."""

from __future__ import annotations
from binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    # Private _Node class -----------------------------------------------------------------------
    class _Node:                                # Lightweight, nonpublic class for storing a node
        __slots__ = '_element', '_parent', '_left', '_right'
        def __init__(self, element, parent=None, left=None, right=None):
            self._element = element
            self._parent = parent
            self._left = left
            self._right = right

        @property
        def element(self):
            return self._element

        @property
        def parent(self):
            return self._parent

        @property
        def left(self):
            return self._left

        @property
        def right(self):
            return self._right

        @left.setter
        def left(self, value):
            self._left = value

        @right.setter
        def right(self, value):
            self._right = value

        @element.setter
        def element(self, value):
            self._element = value

        @parent.setter
        def parent(self, value):
            self._parent = value

    # Nested Position class ---------------------------------------------------------------------
    class Position(BinaryTree.Position):
        """An abstraction representing the location of a single element."""

        def __init__(self, contianer: LinkedBinaryTree, node: LinkedBinaryTree._Node):
            """Constructor should not be invoked by user."""
            self._container = contianer
            self._node = node

        def element(self):
            """Return the element stored at this ``Position``."""
            return self._node.element

        def __eq__(self, other: LinkedBinaryTree.Position):
            """Return ``True`` if other is a ``Position`` representing the same location."""
            return type(other) is type(self) and other._node is self._node

        @property
        def container(self):
            return self._container

        @property
        def node(self):
            return self._node

    # Concrete LinkedBinaryTree methods ---------------------------------------------------------
    def _validate(self, p: Position):
        """Return associated node, if position is valid."""
        if not isinstance(p, self.Position):
            raise TypeError("p must be proper Position type")
        if p.container is not self:
            raise ValueError("p does not belong to this container")
        if p.node.parent is p.node:                     # Convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p.node

    def _make_position(self, node: _Node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

    # Binary Tree constructors -----------------------------------------------------------------
    def __init__(self):
        """Create an initially empty binary tree."""
        self._root: LinkedBinaryTree._Node | None = None
        self._size = 0

    # Public accessors -------------------------------------------------------------------------
    def __len__(self):
        """Return the total number of elements in the tree."""
        return self._size

    def root(self):
        """Return the root Position of the tree (or None if tree is empty)."""
        return self._make_position(self._root)

    def parent(self, p: Position):
        """Return the Position of p's parent (or None if p is root)."""
        node = self._validate(p)
        return self._make_position(node.parent)

    def left(self, p: Position):
        """Return the Position of p's left child (or None if no left child)."""
        node = self._validate(p)
        return self._make_position(node.left)

    def right(self, p: Position):
        """Return the Position of p's right child (or None if no right child)."""
        node = self._validate(p)
        return self._make_position(node.right)

    def num_children(self, p: Position):
        """Return the number of children of Position p."""
        node = self._validate(p)
        count = 0
        if node.left is not None:                       # Left child exists
            count += 1
        if node.right is not None:                      # Rigt child exists
            count += 1
        return count

    def _add_root(self, e):
        """Place element e at the root of an empty tree and return new Position.\n
        :raises ValueError: if tree nonempty.
        """
        if self._root is not None: raise ValueError("Root exists")
        self._size = 1
        self._root = self._Node(e)
        return self._make_position(self._root)

    def _add_left(self, p: Position, e):
        """Create a new left child for Position p, storing element e.\n
        :returns: The position of new node.
        :raises ValueError: if Position p is invalid or p already has a left child.
        """
        node = self._validate(p)
        if node.left is not None: raise ValueError("Left child exists")
        self._size += 1
        node.left = self._Node(e, node)                 # Node is its parent
        return self._make_position(node.left)

    def _add_right(self, p: Position, e):
        """Create a new right child for Position p, storing element e.\n
        :returns: The Position of a new node.
        :raises ValueError: if Position p is invalid or p already has a right child.
        """
        node = self._validate(p)
        if node.right is not None: raise ValueError("Right child exists")
        self._size += 1
        node.right = self._Node(e, node)                # Node is its parent
        return self._make_position(node.right)

    def _replace(self, p: Position, e):
        """Replace the element at Position p with e, and return old element."""
        node = self._validate(p)
        old = node.element
        node.element = e
        return old

    def _delete(self, p: Position):
        """Delete the node at Position p, and replace it with its child, if any.\n
        :returns: The element that had been stored at Position p.
        :raises ValueError: if Position p is invalid or p has two children.
        """
        node = self._validate(p)
        if self.num_children(p) == 2: raise ValueError("p has two children")
        child: LinkedBinaryTree._Node = node.left if node.left else node.right
        if child is not None:                           # Might be None (see previous line)
            child.parent = node.parent                  # Child's grandparent becomes parent
        if node is self._root:
            self._root = child                          # Child becomes root
        else:
            parent = node.parent
            if node is parent.left:
                parent.left = child
            else:
                parent.right = child
        self._size -= 1
        node.parent = node                              # Convention for deprecated node
        return node.element

    def _attach(self, p: Position, t1: LinkedBinaryTree, t2: LinkedBinaryTree):
        """Attach trees t1 and t2 as left and right subtrees of external p."""
        node = self._validate(p)
        if not self.is_leaf(p): raise ValueError("position must be leaf")
        if not type(self) is type(t1) is type(t2):      # All 3 trees must be same type
            raise TypeError("Tree types must match")
        self._size += len(t1) + len(t2)
        if not t1.is_empty():                           # Attached t1 as left subtree of node
            t1._root.parent = node
            node.left = t1._root
            t1._root = None                             # Set t1 instance to empty
            t1._size = 0
        if not t2.is_empty():                           # Attached t2 as right subtree of node
            t2._root.parent = node
            node.right = t2._root
            t2._root = None                             # Set t2 instance to empty
            t2._size = 0

