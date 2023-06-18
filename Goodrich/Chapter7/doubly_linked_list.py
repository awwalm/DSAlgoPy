"""Code Fragment 7.11/.12: A Python Node class for use in a doubly linked list."""


class EmptyError(Exception):
    ...


class _DoublyLinkedBase:
    """A base class providing a doubly linked list representation."""

    # Nested _Node class -----------------------------------------------------------------
    class _Node:
        """Lightweight, nonpublic class for storing a doubly linked node."""
        __slots__ = "_element", "_prev", "_next"            # Streamline memory usage.

        # noinspection PyShadowsBuiltInName
        def __init__(self, element, prev, next):            # Initialize node's fields.
            self._element = element                         # Reference to user's element.
            self._prev = prev                               # Reference to previous node.
            self._next = next                               # Reference to next node.

        @property
        def __element(self):
            return self._element

        @property
        def __prev(self):
            return self._prev

        @property
        def __next(self):
            return self._next

        @__element.setter
        def __element(self, value):
            self._element = value

        @__prev.setter
        def __prev(self, value):
            self._prev = value

        @__next.setter
        def __next(self, value):
            self._next = value

    # Doubly Linked Base methods ----------------------------------------------------------
    def __init__(self):
        """Create an empty list."""
        self._header: _DoublyLinkedBase._Node = self._Node(None, None, None)
        self._trailer: _DoublyLinkedBase._Node = self._Node(None, None, None)
        self._header.__next = self._trailer                 # Trailer is after header.
        self._header.__prev = self._header                  # Header is before trailer.
        self._size = 0                                      # Number of elements.

    def __len__(self):
        """Return the number of elements in the list."""
        return self._size

    def is_empty(self):
        """Return ``True`` if the list is empty."""
        return self._size == 0

    def _insert_between(self, e, predecessor: _Node, successor: _Node):
        """Add element ``e`` between two existing nodes and return new node."""
        newest = self._Node(e, predecessor, successor)      # Linked to neighbors.
        predecessor.__next = newest
        successor.__prev = newest
        self._size += 1
        return newest

    def _delete_node(self, node: _Node):
        """Delete nonsentinel node from the list and return its element."""
        predecessor = node.__prev
        successor = node.__next
        predecessor.__next = successor
        successor.__prev = predecessor
        self._size -= 1
        element = node.__element                            # Record deleted element.
        node.__prev = node.__next = node.__element = None   # Deprecate node.
        return element
