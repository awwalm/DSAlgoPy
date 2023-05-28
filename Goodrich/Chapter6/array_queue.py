"""Code Fragment 6.6: Array-based implementation of a queue (continued in Code Fragment 6.7).
The ``@property`` decorator for wrapping a pseudo-constant in a getter method is no longer neccessary.
But the syntax for future reference is as follows:

.. highlight:: python
.. code-block:: python

    @property
    def DEFAULT_CAPACITY(self):
        # Wraps a constant value of 10 within a class, identified by the specified method name.
        return 10
"""


class EmptyError(Exception):
    """Error attempting to access an element from an empty container."""
    pass


class ArrayQueue:
    """FIFO queue implementation using a Python list as underlying storage."""

    DEFAULT_CAPACITY = 10       # Moderate capacity for all new queues.

    def __init__(self):
        """Create an empty queue."""
        self._data = [None] * ArrayQueue.DEFAULT_CAPACITY
        self._size = 0
        self._front = 0

    def __str__(self):
        """Return a string representation of queue."""
        return f"{[i for i in self._data if i is not None]}"

    def __len__(self):
        """Return the number of elements in the queue."""
        return self._size

    def is_empty(self):
        """Return ``True`` if the queue is empty."""
        return self._size == 0

    def first(self):
        """Return (but do not remove) the element at the front of the queue.\n
        :raises EmptyError: if the queue is empty.
        """
        if self.is_empty():
            raise EmptyError("Queue is empty")
        return self._data[self._front]

    def dequeue(self):
        """Remove and return the first element of the queue (i.e. FIFO).\n
        :raises EmptyError: if the queue is empty.
        """
        if self.is_empty():
            raise EmptyError("Queue is empty")
        answer = self._data[self._front]
        self._data[self._front] = None                          # Help garbage collection.
        self._front = (self._front + 1) % len(self._data)       # Circular index calculation.
        self._size -= 1
        return answer

    def _resize(self, cap):                                     # We assume cap >= len(self).
        """Resize to a new list of capacity >= ``len(self)``."""
        old = self._data                                        # Keep track of existing list.
        self._data = [None] * cap                               # Allocate list with new capacity.
        walk = self._front
        for k in range(self._size):                             # Only consider existing elements.
            self._data[k] = old[walk]                           # Intentionally shift indices.
            walk = (1 + walk) % len(old)                        # Use old size as modulus.
        self._front = 0                                         # Front has been realigned.

    def enqueue(self, e):
        """Add an element to the back of queue."""
        if self._size == len(self._data):
            self._resize(2 * len(self._data))                   # Double the array size.
        avail = (self._front + self._size) % len(self._data)
        self._data[avail] = e
        self._size += 1
