from RDNecaise.Chapter13.arrayheap import MaxHeap


def siftUp(elements, ndx):
    """Sift the value at the ndx element up the elements array."""
    if ndx > 0:
        parent = ndx // 2
        if elements[ndx] > elements[parent]:  # Swap elements
            tmp = elements[ndx]
            elements[ndx] = elements[parent]
            elements[parent] = tmp
            siftUp(elements, parent)


def siftDown(elements, ndx):
    """Sift the value at the ndx element down the tree."""
    left = 2 * ndx + 1
    right = 2 * ndx + 2
    largest = ndx                   # Determine which node contains the larger value.
    count = len(elements)
    if left < count and elements[left] >= elements[largest]:
        largest = left
    elif right < count and elements[right] >= elements[largest]:
        largest = right
    if largest != ndx:
        # swap(self._elements[ndx], self._elements[largest])
        temp = elements[ndx]
        elements[ndx] = elements[largest]
        elements[largest] = temp
        siftDown(elements, largest)

def simpleHeapSort(theSeq):
    """A simple implementation of the heapsort algorithm."""
    n = len(theSeq)
    heap = MaxHeap(n)               # Create an array-based max-heap.
    for item in theSeq:             # Build a max-heap from the list of values.
        heap.add(item)
    for i in range(n, 0, -1):       # Extract each value from the heap and store them back into the list.
        theSeq[i] = heap.extract()


def heapSort(theSeq):
    """Improved implementation of the heapsort algorithm.\n
    Sorts a sequence in ascending order using the heapsort.
    """
    n = len(theSeq)
    for i in range(n):
        siftUp(theSeq, i)           # Build a max-heap within the same array.
    print(*theSeq)
    for j in range(n-1, 0, -1):
        tmp = theSeq[j]
        theSeq[j] = theSeq[0]
        theSeq[0] = tmp
        siftDown(theSeq, j-1)
    print(*theSeq)
    return theSeq

print(*[55,38,7,15,56,1,9])
heapSort([55,38,7,15,56,1,9])
