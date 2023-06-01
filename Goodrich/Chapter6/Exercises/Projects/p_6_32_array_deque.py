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
        self._back = self._size - 1 if self._size > 0 else 0

    def __str__(self):
        """Return stringified representation of deque."""
        return f"{[i for i in self._data if i is not None]}"

    def __repr__(self):
        """Return unfiltered stringified representation of deque."""
        return f"{[i for i in self._data]}"

    def __len__(self):
        """Return the number of elements in the deque."""
        return self._size

    def _is_internal_full(self):
        """Return ``True`` if internal list structure needs resizing."""
        return not (None in self._data)

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

    def _resize(self, cap):                                             # We assume cap >= len(self).
        """Resize to a new list of capacity >= ``len(self)``."""
        old = self._data                                                # Keep track of existing list.
        self._data = [None] * cap                                       # Allocate list with new capacity.
        walk = self._front
        for k in range(self._size):                                     # Only consider existing elements.
            self._data[k] = old[walk]                                   # Intentionally shift indices.
            walk = (1 + walk) % len(old)                                # Use old size as modulus.
        self._front = 0
        self._back = self._size - 1

    def add_last(self, e):                                              # Worst case: O(2n); Armotized: O(1)
        """Add an element to the back of deque."""
        if self._size == len(self._data):                               # If deque is in full capacity, resize.
            self._resize(2 * len(self._data))                           # Double the array size.
        self._back = (self._front + self._size) % len(self._data)       # Update back index of deque.
        self._data[self._back] = e
        self._size += 1

    def add_first(self, e):                                             # Worst case: O(n); Avg: O(n-front); Best: O(1)
        """Add an element to the front of deque."""
        if (self._front >= 1) & (self._data[self._front-1] is None):    # If index before front is vacant...
            self._front -= 1                                            # Point front index to vacant position behind.
            self._data[self._front] = e                                 # Insert element immediately.
            self._size += 1                                             # Update size and exit.
            return
        endx = len(self._data) - 1 if self._size > 0 else 0             # Last index of INTERNAL list container.
        endi = self._data[endx]                                         # Last item of INTERNAL list container.
        if (endi is not None) | (self._size == len(self._data)):        # If last index is not vacant or deque is full...
            self._resize(2 * len(self._data))                           # resize and...
            endx = self._size                                           # update last index (incremented +1).
        for i in range(endx, self._front-1, -1):                        # Identify index range from front to end (+1).
            self._data[i] = self._data[i-1]                             # Shift elements from front rightwards.
        self._data[self._front] = e                                     # Add desired element as new front.
        self._back = (self._front + self._size - 1) % len(self._data)
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
