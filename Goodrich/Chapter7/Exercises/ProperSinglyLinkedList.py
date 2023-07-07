"""A proper singly linked list with simple and obvious properties and methods.

* Abolishes the use of sentinnel nodes (header and trailer).
* Not a base class - can be directly instantiated.
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
        def __element(self):
            return self._element

        @property
        def __next(self):
            return self._next

        @__element.setter
        def __element(self, value):
            self._element = value

        @__next.setter
        def __next(self, value):
            self._next = value

    # _DoublyLinkedBase methods ------------------------------------------------------------
    def __init__(self):
        """Create an empty list."""
        self._header: SinglyLinkedList._Node = self._Node(None, None)
        self._size = 0                                          # Number of elements.

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return ``True`` if the list is empty."""
        return self._size == 0

    def insert_before(self, e, guide: _Node):
        """Insert element ``e`` before a guide node and return new node."""
        newest = self._Node(e, guide)
        cur = self._header
        if self.is_empty():                                     # If Linked List is empty, crash the code.
            raise EmptyError("Linked List is empty")
        elif self._size == 1 and guide == self._header:         # If Linked List has singleton node and guide is head...
            self._header = newest                               # Make new node the header, pointed next to old head.
        else:                                                   # If more than one node detected...
            while cur.__next is not None:                       # While current node is not the tail...
                if cur.__next == guide:                         # If node ahead of current node is guide...
                    cur.__next = newest                         # The point the node before guide next to a new node.
                    break
                cur = cur.__next
        self._size += 1
        return newest

    def delete_node(self, node: _Node):
        """Delete nonsentinel node from the list and return its element."""
        cur = self._header                                      # Head node.
        while cur is not None:
            if cur.__next == node:
                cur.__next = node.__next
                break
            elif cur == node:

            else:
                cur = cur.__next
        self._size -= 1
        element = node.__element
        return element
