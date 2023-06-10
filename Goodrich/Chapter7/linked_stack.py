"""Code Fragment 7.5: Implementation of a stack ADT using a singly linked list."""
from typing import Union


class EmptyError(Exception):
    ...


class LinkedStack:
    """LIFO ``Stack`` implementation using a singly linked list for storage."""

    # Nested _Node class -----------------------------------------------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a singly linked node."""
        __slots__ = "_element", "_next"                     # Streamline memory usage.

        # noinspection PyShadowsBuiltInName
        def __init__(self, element, next):                  # Initialize node's fields.
            self._element = element                         # Reference to user's element.
            self._next = next                               # Reference to next node.

        @property
        def __element(self):
            return self._element

        @property
        def __next(self):
            return self._next

    # Stack methods ----------------------------------------------------------------------
    def __init__(self):
        """Create an empty stack."""
        self._head: Union[LinkedStack._Node, None] = None   # Reference to the head node.
        self._size = 0                                      # Number of stack elements.

    def __len__(self):
        """Return the number of elements in the stack."""
        return self._size

    def is_empty(self):
        """Return ``True`` if the stack is empty."""
        return self._size == 0

    def push(self, e):
        """Add element ``e`` to the top of the stack."""
        self._head = self._Node(element=e, next=self._head)  # Create and link a new node.
        self._size += 1

    def top(self):
        """Return (but do not remove) the element at the top of the stack.\n
        :raises EmptyError: if the stack is empty."""
        if self.is_empty():
            raise EmptyError("Stack is empty")
        return self._head.__element                          # Top of stack is at head of list.

    def pop(self):
        """Remove and return the element from the top of the stack (i.e. LIFO)\n
        :raises EmptyError: if the stack is empty."""
        if self.is_empty():
            raise EmptyError("Stack is empty")
        answer = self._head.__element
        self._head = self._head.__next                      # Bypass the former top node.
        self._size -= 1
        return answer
