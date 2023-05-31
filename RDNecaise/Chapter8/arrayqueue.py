"""Implementation of the Queue ADT using a circular array."""
from RDNecaise.Chapter2.array import Array


class Queue:
	"""Create an empty queue."""
	def __init__(self, maxSize):
		self._count = 0
		self._front = 0
		self._back = maxSize - 1
		self._qArray = Array(maxSize)

	def isEmpty(self):
		"""Returns ``True`` if the queue is empty."""
		return self._count == 0

	def isFull(self):
		"""Returns ``True`` if the queue is full."""
		return self._count == len(self._qArray)

	def __len__(self):
		"""Returns the number of items in the queue."""
		return self._count

	def enqueue(self, item):
		"""Adds the given item to the queue."""
		assert not self.isFull(), "Cannot enqueue to a full queue"
		maxSize = len(self._qArray)
		self._back = len(self._back + 1) % maxSize
		self._qArray[self._back] = item
		self._count += 1

	def dequeue(self):
		"""Removes and returns the first item in the queue."""
		assert not self.isEmpty(), "Cannot dequeue from an empty queue"
		item = self._qArray[self._front]
		maxSize = len(self._qArray)
		self._front = (self._front + 1) % maxSize
		self._count -= 1
		return item
