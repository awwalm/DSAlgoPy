"""Implementation of the unbounded Priority Queue ADT using a Python list with new items appnded to the end."""
from RDNecaise.Chapter2.array import Array
from RDNecaise.Chapter8.llistqueue import Queue


class BPriorityQueue:
    """Creates an empty bounded priority queue."""
    def __init__(self, numLevels):
        self._qSize = 0
        self._qLevels = Array(numLevels)
        for i in range(numLevels):
            self._qLevels[i] = Queue()

    def isEmpty(self):
        """Returns True if the queue is empty."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in the queue."""
        return self._qSize

    def enqueue(self, item, priority):
        """Adds the given item to the queue."""
        assert 0 <= priority < len(self._qLevels), "Invalid priority level"
        self._qLevels[priority].enqueue(item)

    def dequeue(self):
        """Removes and returns the next item in the queue."""
        assert not self.isEmpty(), "Cannot dequeue from an empty queue"
        i = 0
        p = len(self._qLevels)
        while i < p and not self._qLevels[i].isEmpty():  # Finds the highest priority level
            i += 1
        return self._qLevels[i].dequeue()


class PriorityQueue:
    """Create an empty unbounded priority queue."""
    def __init__(self):
        self._qlist = list()

    def isEmpty(self):
        """Returns ``True`` if the queue is empty."""
        return len(self) == 0

    def __len__(self):
        """Returns the number of items in the queue."""
        return len(self._qlist)

    def enqueue(self, item, priority):
        """Adds the given item to the queue."""
        entry = _PriorityQEntry(item, priority)         # Create new storage instance and append it to list.
        self._qlist.append(entry)

    def dequeue(self):
        """Removes and returns the first item in the queue."""
        assert not self.isEmpty(), "Cannot dequeue from an empty queue."
        highest = self._qlist[0].priority
        for i in range(len(self)):
            if self._qlist[i].priority < highest:
                highest = self._qlist[i].priority
        entry = self._qlist.pop(highest)
        return entry.item


class _PriorityQEntry(object):
    def __init__(self, item, priority):
        self.item = item
        self.priority = priority
