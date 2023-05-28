"""A complete ``ArrayDeque`` implementation of the double-ended queue ADT as sketched in Section 6.3.2."""


class EmptyError(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class ArrayDeque:
    """Double-ended queue ADT using a Python list as underlying storage."""
    DEFAULT_CAPACITY = 10       # Moderate capacity for all new queues.

    def __init__(self):
        """Create an empty dequeue."""
        self._data = [None] * ArrayDeque.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0
        self._back = 0

    def __str__(self):
        """Return stringified representation of deque."""
        return f"{[i for i in self._data if i is not None]}"

    def __len__(self):
        """Return the number of elements in the deque."""
        return self._size

    def is_empty(self):
        """Return ``True`` if the deque is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.\n
        :raises EmptyError: if the deque is empty.
        """
        if self.is_empty():
            raise EmptyError("Deque is empty")
        return self._data[self._front]

    def last(self):
        """Return (but do not remove) the last element of deque.\n
        :raises EmptyError: if the deque is empty."""
        if self.is_empty():
            raise EmptyError("Deque is empty")
        self._back = (self._front + self._size - 1) % len(self._data)
        return self._data[self._back]

    def _resize(self, cap):                                     # We assume cap >= len(self).
        """Resize to a new list of capacity >= ``len(self)``."""
        old = self._data                                        # Keep track of existing list.
        self._data = [None] * cap                               # Allocate list with new capacity.
        walk = self._front
        for k in range(self._size):                             # Only consider existing elements.
            self._data[k] = old[walk]                           # Intentionally shift indices.
            walk = (1 + walk) % len(old)                        # Use old size as modulus.
        self._front = 0

    def add_last(self, e):                                      # Worst case: O(2n); Armotized: O(1)
        """Add an element to the back of deque."""
        if self._size == len(self._data):                       # If deque is in full capacity, resize.
            self._resize(2 * len(self._data))                   # Double the array size.
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1

    def add_first(self, e):                                     # Worst case: O(n-front)
        """Add an element to the front of deque."""
        if self._size == len(self._data):                       # If deque is in full capacity, resize.
            self._resize(2 * len(self._data))
        for i in range(self._size, self._front-1, -1):          # Identify index range from front to end.
            self._data[i] = self._data[i-1]                     # Shift elements from front rightwards.
        self._data[self._front] = e                             # Add desired element as new front.
        self._size += 1

    # noinspection PyNoneFunctionAssignment
    def delete_first(self):
        """Remove and return the first element from deque.\n
        :raises EmptyError: if the deque is empty."""
        if self.is_empty():
            raise EmptyError("Deque is empty")
        deleted = self.first()
        self._data[self._front] = None
        self._front = (self._front + 1) % len(self._data)
        self._size -= 1
        return deleted

    # noinspection PyNoneFunctionAssignment
    def delete_last(self):
        """Remove and return the last element from deque.\n
        :raises EmptyError: if the deque is empty."""
        if self.is_empty():
            raise EmptyError("Deque is empty")
        deleted = self.last()
        self._data[self._back] = None
        self._back = (self._front + self._size - 1) % len(self._data)
        self._size -= 1
        return deleted
