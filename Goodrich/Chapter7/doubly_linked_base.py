"""Code Fragment 7.11/.12: A Python Node class for use in a doubly linked list."""
from __future__ import annotations
from typing import Union


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    # Nested _Node class -----------------------------------------------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = "_element", "_prev", "_next"                        # Streamline memory usage.

        # noinspection PyShadowsBuiltInName
        def __init__(self,                                              # Initialize node's fields.
                     element,
                     prev: Union[_DoublyLinkedBase._Node, None],        # Future recursive type-hinting.
                     next: Union[_DoublyLinkedBase._Node, None]):
            self._element = element                                     # Reference to user's element.
            self._prev = prev                                           # Reference to previous node.
            self._next = next                                           # Reference to next node.

        @property
        def element(self):
            return self._element

        @property
        def prev(self):
            return self._prev

        @property
        def next(self):
            return self._next

        @element.setter
        def element(self, value):
            self._element = value

        @prev.setter
        def prev(self, value):
            self._prev = value

        @next.setter
        def next(self, value):
            self._next = value

    # _DoublyLinkedBase methods ------------------------------------------------------------
    def __init__(self):
        """Create an empty list."""
        self._header: _DoublyLinkedBase._Node = self._Node(None, None, None)
        self._trailer: _DoublyLinkedBase._Node = self._Node(None, None, None)
        self._header.next = self._trailer                     # Trailer is after header.
        self._header.prev = self._header                      # Header is before trailer.
        self._size = 0                                        # Number of elements.

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return ``True`` if the list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor: _Node, successor: _Node):
        """Add element ``e`` between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)        # Linked to neighbors.
        predecessor.next = newest
        successor.prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node: _Node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node.prev
        successor = node.next
        predecessor.next = successor
        successor.prev = predecessor
        self._size -= 1
        element = node.element                                # Record deleted element.
        node.prev = node.next = node.element = None           # Deprecate node.
        return element

    # Exercise C-7.33
    def reverse(self):
        curnode, prevnode = self._header, None
        while curnode is not None:
            nextnode = curnode.next
            curnode.prev = nextnode
            curnode.next = prevnode
            prevnode = curnode
            curnode = nextnode
        oldheader = self._header
        oldtrailer = self._trailer
        self._header = oldtrailer
        self._trailer = oldheader
