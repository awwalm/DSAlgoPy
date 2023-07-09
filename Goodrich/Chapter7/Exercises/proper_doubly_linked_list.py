"""A proper doubly linked list with simple and obvious properties and methods.

* Abolishes the use of sentinnel nodes (header and trailer).
* Not a base class - can be directly instantiated.
"""
from __future__ import annotations
from typing import Union
from overrides import override
from proper_singly_linked_list import SinglyLinkedList, EmptyError


class DoublyLinkedList(SinglyLinkedList):
    """A class providing a doubly linked list representation, by inheriting singly linked list."""

    # Nested _Node class -----------------------------------------------------------------
    class _Node(SinglyLinkedList._Node):
        """Lightweight, nonpublic class for storing a doubly linked node.\n
        - Inherits from the ``SinglyLinkedList``'s internal ``_Node`` class.
        - Extends the ``_Node`` class with a ``_prev`` reference.
        """
        __slots__ = "_prev"  # Streamline memory usage.

        # noinspection PyShadowsBuiltInName
        def __init__(self,
                     element,
                     next: Union[DoublyLinkedList._Node, None],
                     prev: Union[DoublyLinkedList._Node, None]):
            self._prev = prev
            super().__init__(element, next)

        @property
        def prev(self):
            return self._prev

        @prev.setter
        def prev(self, value):
            self._prev = value

    # DoublyLinkedList methods ------------------------------------------------------------
    def __init__(self, head_element):
        """Create a doubly linked list initialized with a head node and a valid element."""
        super(DoublyLinkedList, self).__init__(head_element)
        self._header: DoublyLinkedList._Node = self._Node(head_element, None, None)
        self._tail = self._header

    def tail(self):
        """Returns a reference to the linked list's ``_tail``."""
        return self._tail

    @override
    def head(self):
        """Returns a reference to the Linked List ``_header``."""
        return self._header

    @override
    def insert_before(self, e, guide: DoublyLinkedList._Node):
        """Insert element ``e`` before a ``guide`` node and return new node."""
        if self.is_empty():
            raise EmptyError("Linked List is empty")
        elif self._size == 1 and guide == self._header:
            newest = self._Node(e, self._header, None)
            self._header.prev = self._header = newest
        else:
            newest = self._Node(e, guide, guide.prev)
            guide.prev.next = guide.prev = newest
        self._size += 1
        return newest

    @override
    def insert_after(self, e, guide: DoublyLinkedList._Node):
        """Insert element ``e`` after a ``guide`` node and return new node."""
        if self.is_empty():
            raise EmptyError("Linked List is empty")
        elif guide == self._tail:
            newest = self._Node(e, self._tail.next, self._tail)
            self._tail.next = self._tail = newest
        else:
            newest = self._Node(e, guide.next, guide)
            guide.next = newest
        self._size += 1
        return newest

    @override
    def delete_node(self, node: DoublyLinkedList._Node):
        """Delete node from the list and return its element."""
        if self.is_empty():
            raise EmptyError("Linked List is empty")
        elif node == self._header:
            oldhead = self._header
            self._header.next.prev = self._header = None
            self._header = oldhead.next
        elif node == self._tail:
            oldtail = self._tail
            self._tail.prev.next = self._tail = None
            self._tail = oldtail.prev
        else:
            node.prev.next = node.next
            node.next.prev = node.prev
        self._size -= 1
        element = node.element
        node.prev = node.next = node.element = None
        return element
