from array_queue import ArrayQueue

aq = ArrayQueue()
aq.enqueue(5)
aq.enqueue(3)
print(len(aq))
aq.dequeue()
print(aq)
