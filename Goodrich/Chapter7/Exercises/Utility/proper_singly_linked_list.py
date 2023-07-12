"""A proper singly linked list with simple and obvious properties and methods.

* Abolishes the use of sentinnel nodes (header and trailer).
* Not a base class - can be directly instantiated.

@TODO: Consider implementing a __iter__ method (less boilerplate for traversing all nodes).
"""
from __future__ import annotations
from typing import Union


class EmptyError(Exception):
    ...


class SinglyLinkedList:
    """A class providing a singly linked list representation."""

    # Nested _Node class -----------------------------------------------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = "_element", "_next"                         # Streamline memory usage.

        # noinspection PyShadowsBuiltInName
        def __init__(self, element, next: Union[SinglyLinkedList._Node, None]):
            self._element = element                             # Reference to user's element.
            self._next = next                                   # Reference to next node.

        @property
        def element(self):
            return self._element

        @property
        def next(self):
            return self._next

        @element.setter
        def element(self, value):
            self._element = value

        @next.setter
        def next(self, value):
            self._next = value

    # SinglyLinkedList methods ------------------------------------------------------------
    def __init__(self, head_element):
        """Create an empty list."""
        self._header: SinglyLinkedList._Node = self._Node(head_element, None)
        self._size = 1                                          # Number of elements.

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    @property
    def head(self):
        """Returns a reference to the Linked List ``_header``."""
        return self._header

    def is_empty(self):
        """Return ``True`` if the list is empty."""
        return self._size == 0

    def insert_before(self, e, guide: _Node):
        """Insert element ``e`` before a ``guide`` node and return new node."""
        newest = self._Node(e, guide)                           # Pre-linked before guide node.
        cur = self._header
        inserted = False
        if self.is_empty():                                     # If Linked List is empty, raise an exception.
            raise EmptyError("Linked List is empty")
        elif self._size == 1 or guide == self._header:         # If Linked List has singleton node and guide is head...
            self._header = newest                               # Make new node the header, pointed next to old head.
            inserted = True
        else:                                                   # If more than one node detected...
            cur = cur.next
            while cur is not None:                              # While current node is valid...
                if cur.next == guide:                           # If node ahead of current node is guide...
                    cur.next = newest                           # Point the node before guide next to a new node.
                    inserted = True
                    break                                       # Insertion complete, terminate loop.
                cur = cur.next                                  # If not, keep iterating till tail.
        if not inserted:
            raise ValueError(f"Node {guide} not in {self}")     # In case node is not found, raise an exception.        self._size += 1
        return newest

    def insert_after(self, e, guide: _Node):
        """Insert element ``e`` after a ``guide`` node and return new node."""
        newest = self._Node(e, guide.next)                      # Pre-linked to next node after guide node.
        cur = self._header
        inserted = False
        if self.is_empty():                                     # If Linked List is empty, raise an exception.
            raise EmptyError("Linked List is empty")
        else:                                                   # If one or more nodes detected...
            while cur is not None:
                if cur == guide:                                # When guide node is found, mark insertion as done.
                    guide.next = newest                         # Point guide next to new node.
                    inserted = True
                    break
                cur = cur.next
        if not inserted:
            raise ValueError(f"Node {guide} not in {self}")     # In case node is not found, raise an exception.
        self._size += 1
        return newest

    def delete_node(self, node: _Node):
        """Delete node from the list and return its element."""
        cur = self._header                                      # Head node.
        element = node.element
        deleted = False
        if self.is_empty():                                     # If Linked List is empty, raise an exception.
            raise EmptyError("Linked List is empty")
        elif node == self._header:                              # If node to be deleted is head...
            self._header = node.next
            node.element = node.next = None                     # Deprecate node.
            deleted = True
        else:
            while cur is not None:
                if cur.next == node:
                    cur.next = node.next
                    node.element = node.next = None
                    deleted = True
                    break
                cur = cur.next
        if not deleted:
            raise ValueError(f"Node {node} not in {self}")      # In case node is not found, raise an exception.
        self._size -= 1
        return element
