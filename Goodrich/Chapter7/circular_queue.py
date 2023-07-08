"""Code Fragment 7.9: Implementation of a CircularQueue class, using a circularly linked list as storage."""
from typing import Union


class EmptyError(Exception):
    ...


class CircularQueue:
    """Queue implementation using circularly linked list for storage."""

    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = "_element", "_next"                      # Streamline memory usage.

        # noinspection PyShadowsBuiltInName
        def __init__(self, _element, _next):                 # Initialize node's fields.
            self._element = _element                         # Reference to user's element.
            self._next: CircularQueue._Node = _next          # Reference to next node.

        @property
        def element(self):
            return self._element

        @property
        def next(self):
            return self._next

        @next.setter
        def next(self, value):
            self._next = value

    # Queue methods ----------------------------------------------------------------------
    def __init__(self):
        """Create an empty queue."""
        self._tail: Union[CircularQueue._Node, None] = None  # Represents tail of queue.
        self._size = 0  									 # Number of queue elements.

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return ``True`` if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.\n
        :raises EmptyError: if the queue is empty."""
        if self.is_empty():
            raise EmptyError("Queue is empty")
        head: CircularQueue._Node = self._tail.next
        return head.element

    def dequeue(self):
        """Remove and return the first element of the queue (i.e. FIFO).\n
        :raises EmptyError: if the queue is empty."""
        if self.is_empty():
            raise EmptyError("Queue is empty")
        oldhead: CircularQueue._Node = self._tail.next
        if self._size == 1:                                 # Removing only element (singleton node).
            self._tail = None                               # Queue becomes empty.
        else:
            self._tail.next = oldhead.next                  # Point tail node to next node after oldhead.
        self._size -= 1
        return oldhead.element

    def enqueue(self, e):
        """Add an element to the back of queue."""
        newest = self._Node(e, None)                        # Node will be new tail node.
        if self.is_empty():
            newest.next = newest                            # Initialize circularly (point back to self).
        else:
            newest.next = self._tail.next                   # New node points to head.
            self._tail.next = newest                        # Old tail points to new node.
        self._tail = newest                                 # New node becomes the tail.
        self._size += 1

    def rotate(self):
        """Rotate front element to the back of the queue."""
        if self._size > 0:
            self._tail = self._tail.next                    # Old head becomes new tail.
