"""A simple implementation of the heapsort algorithm."""
from RDNecaise.Chapter13.arrayheap import MaxHeap


def simpleHeapSort(theSeq):
    n = len(theSeq)
    heap = MaxHeap(n)               # Create an array-based max-heap.
    for item in theSeq:             # Build a max-heap from the list of values.
        heap.add(item)
    for i in range(n, 0, -1):       # Extract each value from the heap and store them back into the list.
        theSeq[i] = heap.extract()
