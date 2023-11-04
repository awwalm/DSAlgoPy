from RDNecaise.Chapter13.arrayheap import MaxHeap


def simpleHeapSort(theSeq):
    """A simple implementation of the heapsort algorithm."""
    n = len(theSeq)
    heap = MaxHeap(n)               # Create an array-based max-heap.
    for item in theSeq:             # Build a max-heap from the list of values.
        heap.add(item)
    for i in range(n, 0, -1):       # Extract each value from the heap and store them back into the list.
        theSeq[i] = heap.extract()


def buildHeap(theSeq):
    """Build a heap out of the given sequence."""
    count = len(theSeq)
    for i in range(count):
        child = i + 1
        parent = child // 2
        checkParent(theSeq, child, parent, i, count-1)
    return theSeq

def checkParent(theSeq, child, parent, curNdx, end):
    if curNdx <= end:
        if theSeq[child-1] > theSeq[parent-1]:
            temp = theSeq[child - 1]
            theSeq[child - 1] = theSeq[parent - 1]
            theSeq[parent - 1] = temp
            if (parent-1) > 0:
                checkParent(theSeq, child=parent, parent=parent//2, curNdx=curNdx, end=end)

def extractRoot(heapSeq):
    """Extract the root from the heap and reorganize the sequence."""
    curlen = len(heapSeq) - 1
    last = heapSeq[curlen]
    heapSeq[curlen] = heapSeq[0]
    heapSeq[0] = last
    while curlen > 0:
        for i in range(curlen):
            child = i + 1
            parent = child // 2
            checkParent(heapSeq, child, parent, i, curlen-1)
        curlen -= 1
        last = heapSeq[curlen]
        heapSeq[curlen] = heapSeq[0]
        heapSeq[0] = last
    return heapSeq


def heapSort(theSeq):
    """Improved implementation of the heapsort algorithm.\n
    Sorts a sequence in ascending order using the heapsort.
    """
    assert len(theSeq) >= 1, "Cannot sort empty sequence"
    heap = buildHeap(theSeq)
    sortedSeq = extractRoot(heap)
    return sortedSeq



# Short test
A = [10,51,2,18,4,31,13,5,23,64,29]
# A = [4,8,15,16,23,42]
print("Original sequence:\t", *A,
      "\nHeap sequence:\t", *buildHeap(A),
      "\nSorted sequence:\t", *heapSort(A))
