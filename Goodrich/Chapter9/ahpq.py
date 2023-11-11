"""Code Fragment 9.8/9.9/: An implementation of an adaptable priority queue.
This extends the HeapPriorityQueue class of Code Fragments 9.4 and 9.5
"""
from Goodrich.Chapter9.heap_priority_queue import HeapPriorityQueue


class AdaptableHeapPriorityQueue(HeapPriorityQueue):
    """A locator-based priority queue implemented with a binary heap."""

    # Nested Locator class -------------------------------------------------------------
    class Locator(HeapPriorityQueue._Item):
        """Token for locating an entry of the priority queue."""
        __slots__ = "_index"                            # Add index as additional field

        def __init__(self, k, v, j):
            super().__init__(k,v)
            self._index = j

        @property
        def index_(self):
            return self._index

        @property
        def key_(self):
            return self._key

        @property
        def value_(self):
            return self._value

    # Nonpublic behaviors --------------------------------------------------------------
    def _swap(self, i, j):
        """Override swap to record new indices."""
        super()._swap(i,j)                              # Perform the swap
        self._data[i].index_ = i                        # Reset locator index (post-swap)
        self._data[j].index_ = j                        # Reset locator index (post-swap)

    def _bubble(self, j):
        if j > 0 and self._data[j] < self._data[self._parent(j)]:
            self._upheap(j)
        else:
            self._downheap(j)

    def add(self, key, value):
        """Add a key-value pair."""
        token = self.Locator(                           # Initialize locator index
            key, value, len(self._data))
        self._data.append(token)
        self._upheap(len(self._data) - 1)
        return token

    def update(self, loc: Locator, newkey, newval):
        """Update the key and value for the entry identified by ``Locator`` loc."""
        j = loc.index_
        if not(0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")
        loc._key = newkey
        loc._value = newval
        self._bubble(j)

    def remove(self, loc: Locator):
        """Remove and return the (k,v) pair identified by ``Locator`` loc."""
        j = loc.index_
        if not (0 <= j < len(self) and self._data[j] is loc):
            raise ValueError("Invalid locator")
        if j == len(self) - 1:                          # Item at last position
            self._data.pop()                            # Just remove it
        else:
            self._swap(j, len(self)-1)                  # Swap item to the last position
            self._data.pop()                            # Remove it from the list
            self._bubble(j)                             # Fix item displaced by the swap
        return loc.key_, loc.value_
