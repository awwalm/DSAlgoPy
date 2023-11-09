from Goodrich.Chapter7.positional_list import PositionalList
from Goodrich.Chapter9.priority_queue_base import PriorityQueueBase


class Empty(Exception):
    ...

class UnsortedPriorityQueue(PriorityQueueBase):     # Base class defines _Item
    """A min-oriented priority queue implemented with an unsorted list."""

    def _find_min(self):                            # is_empty inherited from base class
        """Return Position of item with minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty")
        small = self._data.first()
        walk = self._data.after(small)
        while walk is not None:
            if walk.element() < small.element():
                small = walk
            walk = self._data.after(walk)
        return small

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        self._data.add_last(self._Item(key, value))

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        p = self._find_min()
        item: UnsortedPriorityQueue._Item = p.element()
        return item.key, item.value

    def remove_min(self):
        """Remove and return (k,v) tuple with minimum key."""
        p = self._find_min()
        item: UnsortedPriorityQueue._Item = self._data.delete(p)
        return item.key, item.value
