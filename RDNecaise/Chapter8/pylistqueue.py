"""Implementation of the ``Queue`` ADT using a Python list."""


class Queue:
    """Creates an empty queue."""
    def __init__(self):
        self._qlist = list()

    def __len__(self):
        return len(self._qlist)

    def isEmpty(self):
        """Returns ``True`` if the queue is empty."""
        return len(self) == 0

    def enqueue(self, item):
        """Adds the given item to the queue."""
        self._qlist.append(item)

    def dequeue(self):
        """Removes and returns the first item in the queue."""
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        return self._qlist.pop(0)
