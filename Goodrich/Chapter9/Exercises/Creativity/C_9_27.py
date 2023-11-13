"""C-9.27 Show how to implement the FIFO queue ADT using only a priority queue
and one additional integer instance variable."""

from Goodrich.Chapter9.sorted_priority_queue import SortedPriorityQueue


class FifoPriorityQueue(SortedPriorityQueue):

    def __init__(self, item, priority=1):
        super().__init__()
        self._priority = priority
        self._data.add_first(self._Item(self._priority, item))
        self._size = 1

    def __len__(self):
        return self._size

    def enqueue(self, value):
        self.add(self._priority, value)
        self._priority += 1
        self._size += 1

    def dequeue(self):
        value = self.remove_min()
        self._priority -= 1
        self._size -= 1
        return value[1]
