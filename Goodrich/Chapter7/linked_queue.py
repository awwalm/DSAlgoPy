"""Code Fragment 7.6: Implementation of a queue ADT using a singly linked list for storage."""
from typing import Union


class EmptyError(Exception):
    ...


class LinkedQueue:
    """FIFO queue implementation using a singly linked list for storage."""

    # Nested _Node class -----------------------------------------------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = "_element", "_next"                     # Streamline memory usage.

        # noinspection PyShadowsBuiltInName
        def __init__(self, element, next):                  # Initialize node's fields.
            self._element = element                         # Reference to user's element.
            self._next = next                               # Reference to next node.

        @property
        def element(self):
            return self._element

        @property
        def next(self):
            return self._next

    # Queue methods ----------------------------------------------------------------------
    def __init__(self):
        """Create an empty queue."""
        self._head: Union[None, LinkedQueue._Node] = None
        self._tail: Union[None, LinkedQueue._Node] = None
        self._size = 0  									# Number of queue elements.

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
        return self._head.element  						# Front aligned with head of list.

    def dequeue(self):
        """Remove and return the first element of the queue (i.e. FIFO).\n
        :raises EmptyError: if the queue is empty."""
        if self.is_empty():
            raise EmptyError("Queue is empty")
        answer = self._head.element
        self._head = self._head.next
        self._size -= 1
        if self.is_empty():                                 # Special case as queue is empty.
            self._tail = None                               # Removed head had been the tail.
        return answer

    def enqueue(self, e):
        """Add an element to the back of the queue."""
        newest = self._Node(e, None)                        # Node will be new tail.
        if self.is_empty():
            self._head = newest                             # Special case: previously empty.
        else:
            self._tail.next = newest
        self._tail = newest                                 # Update reference to tail node.
        self._size += 1
