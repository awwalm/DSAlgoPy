"""Code Fragment 7.13: Implementation of a LinkedDeque class that inherits from the DoublyLinkedBase class."""
from doubly_linked_base import _DoublyLinkedBase


class EmptyError(Exception):
    ...


class LinkedDeque(_DoublyLinkedBase):                                # Note the use of inheritance.
    """Double-ended queue implementation based on a doubly linked list."""
    def first(self):
        """Return (but do not remove) the element at the front of the deque."""
        if self.is_empty():
            raise EmptyError("Deque is empty")
        return self._header.next.element                              # Real item just after header.

    def last(self):
        """Return (but do not remove) the element at the back of the deque."""
        if self.is_empty():
            raise EmptyError("Deque is empty")
        return self._trailer.prev.element                             # Real item just before trailer.

    def insert_first(self, e):
        """Add an element to the front of the deque."""
        self._insert_between(e, self._header, self._header.next)      # After header.

    def insert_last(self, e):
        """Add an element to the back of the deque."""
        self._insert_between(e, self._trailer.prev, self._trailer)    # Before trailer.

    def delete_first(self):
        """Remove and return the element from the front of the deque.\n
        :raise EmptyError: if the deque is empty."""
        if self.is_empty():
            raise EmptyError("Deqeue is empty")
        return self._delete_node(self._header.next)                   # Use inherited method.

    def delete_last(self):
        """Remove and return the element from the back of the deque.\n
        :raise EmptyError: if the deque is empty."""
        if self.is_empty():
            raise EmptyError("Deqeue is empty")
        return self._delete_node(self._trailer.prev)                  # Use inherited method.
