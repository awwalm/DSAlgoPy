"""Code Fragment 8.8-8.11: The ``LinkedBinaryTree`` class."""

from __future__ import annotations
from binary_tree import BinaryTree


class LinkedBinaryTree(BinaryTree):
    """Linked representation of a binary tree structure."""

    # Private _Node class -----------------------------------------------------------------------
    class _Node:        # Lightweight, nonpublic class for storing a node
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
        if p.node.parent is p.node:             # Convention for deprecated nodes
            raise ValueError("p is no longer valid")
        return p.node

    def _make_position(self, node: _Node):
        """Return Position instance for given node (or None if no node)."""
        return self.Position(self, node) if node is not None else None

