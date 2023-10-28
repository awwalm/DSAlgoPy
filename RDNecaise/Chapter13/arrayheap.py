"""An array-based implementation of the max-heap."""

from RDNecaise.Chapter2.array import Array


class MaxHeap:
    """Create a max-heap with maximum capacity of maxSize."""
    def __init__(self, maxSize):
        self._elements = Array(maxSize)
        self._count = 0

    def __len__(self):
        """Return the number of items in the heap."""
        return self._count

    def add(self, value):
        """Add a new value to the heap."""
        assert self._count < self.capacity(), "Cannot add to a full heap."
        self._elements[self._count] = value     # Add the new value to the end of the list.
        self._count += 1
        self._siftUp(self._count - 1)           # Sift the new value up the tree.

    def extract(self):
        """Extract the maximum value from the heap."""
        assert self._count > 0, "Cannot extract from an empty heap."
        value = self._elements[0]               # Save the root value and copy the last heap value to root.
        self._count -= 1
        self._elements[0] = self._elements[self._count]
        self._siftDown(0)                       # Sift the root value down the tree.

    def _siftUp(self, ndx):
        """Sift the value at the ndx element up the tree."""
        if ndx > 0:
            parent = ndx // 2
            if self._elements[ndx] > self._elements[parent]:    # Swap elements
                tmp = self._elements[ndx]
                self._elements[ndx] = self._elements[parent]
                self._elements[parent] = tmp
                self._siftUp(parent)

    def _siftDown(self, ndx):
        """Sift the value at the ndx element down the tree."""
        left = 2 * ndx + 1
        right = 2 * ndx + 2
        largest = ndx                           # Determine which node contains the larger value.
        if left < self._count and self._elements[left] >= self._elements[largest]:
            largest = left
        elif right < self._count and self._elements[right] >= self._elements[largest]:
            largest = right
        if largest != ndx:
            swap(self._elements[ndx], self._elements[largest])
            self._siftDown(largest)
