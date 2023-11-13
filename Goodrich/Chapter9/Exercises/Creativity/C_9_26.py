"""C-9.26 Show how to implement the stack ADT using only a priority queue
 and one additional integer instance variable."""

from Goodrich.Chapter9.heap_priority_queue import HeapPriorityQueue


class PriorityStack(HeapPriorityQueue):
    def __init__(self):
        super().__init__(contents=())
        self._priority = -1

    @property
    def size(self):
        return len(self)

    def peek(self):
        if self.is_empty():
            return None     # raise Exception("Stack Empty")
        return self._data[len(self) - 1].value

    def push(self, value):
        self._priority += 1
        self._data.append(self._Item(self._priority, value))
        # self._upheap(len(self._data) - 1)  # Upheap not required, newly addded priority is always higher

    def pop(self):
        if self.is_empty():
            raise IndexError("Stack Empty")
        item = self._data.pop()
        self._priority -= 1
        return item.value
