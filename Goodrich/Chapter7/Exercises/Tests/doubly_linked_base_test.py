"""Tests for the Doubly Linked Base class provided in the book."""
from Goodrich.Chapter7.doubly_linked_base import _DoublyLinkedBase
from Goodrich.Chapter7.Exercises.Utility.utils import *


class DoublyLinkedList(_DoublyLinkedBase):
    """Compact ``DoublyLinkedList`` subclass of the base provided in the book."""

    def __init__(self):
        super().__init__()

    @property
    def head(self):
        return self._header.next

    @property
    def tail(self):
        return self._trailer.prev

    def insert_between(self, e, predecessor, successor):
        super()._insert_between(e, predecessor, successor)


# Instantiate doubly linked list and populate incrementally from 1 to 10.
dbll = DoublyLinkedList()
# noinspection PyProtectedMember
cur = dbll._header
for i in range(1, 11):
    # noinspection PyProtectedMember
    dbll.insert_between(i, cur, dbll._trailer)
    cur = cur.next

print_nodes(dbll)
dbll.reverse()
print_nodes(dbll)
