"""Code Fragments 9.1, 9.2, 9.3."""
from __future__ import annotations
from Goodrich.Chapter7.positional_list import PositionalList


class Empty(Exception):
    ...

class PriorityQueueBase:
    """Abstract base class for a priority queue."""

    # Nested _Item class ------------------------------------------------------------------
    class _Item:
        """Lightweight composite to store prority queue items."""
        __slots__ = '_key', '_value'

        def __init__(self, k, v):
            self._key = k
            self._value = v

        def __lt__(self, other: PriorityQueueBase._Item):
            return self._key < other._key           # Compare items based on their keys

        @property
        def key(self):
            return self._key

        @property
        def value(self):
            return self._value

    # Concrete method(s) ------------------------------------------------------------------
    # noinspection PyTypeChecker
    def is_empty(self):                             # Concrete method assuming abstract len
        """Return True if the priority queue is empty."""
        return len(self) == 0


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


class SortedPriorityQueue(PriorityQueueBase):       # Base class defines _Item
    """A min-oriented priority queue implemented with a sorted list."""

    def __init__(self):
        """Create a new empty Priority Queue."""
        self._data = PositionalList()

    def __len__(self):
        """Return the number of items in the priority queue."""
        return len(self._data)

    def add(self, key, value):
        """Add a key-value pair."""
        newest = self._Item(key, value)             # Make a new item instance
        walk = self._data.last()                    # Walk backward looking for smaller key
        while walk is not None and newest < walk.element():
            walk = self._data.before(walk)
        if walk is None:
            self._data.add_first(newest)            # New key is smallest
        else:
            self._data.add_after(walk, newest)      # Newest goes after walk

    def min(self):
        """Return but do not remove (k,v) tuple with minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty")
        p = self._data.first()
        item = p.element()
        return item.key, item.value

    def remove_min(self):
        """Remove and return (k,v) tuple wtih minimum key."""
        if self.is_empty():
            raise Empty("Priority queue is empty")
        item = self._data.delete(self._data.first())
        return item.key, item.value
