from RDNecaise.Chapter13.arrayheap import MaxHeap

#@TODO: This algorithm by the book author does NOT work. I hvae written mine from scratch in heapsort.py
def simpleHeapSort(theSeq):
    """A simple implementation of the heapsort algorithm."""
    n = len(theSeq)
    heap = MaxHeap(n)                   # Create an array-based max-heap.
    for item in theSeq:                 # Build a max-heap from the list of values.
        heap.add(item)
    for i in range(n-1, -1, -1):         # Extract each value from the heap and store them back into the list.
        theSeq[i] = heap.extract()

# Short test
A = [10,51,2,18,4,31,13,5,23,64,29]
B = [4,8,15,16,23,42]
C = [23,34,78,-1,6,90,343,5]
for s in A,B,C :
    print("Original sequence:\t", *s)        # 10 51 2 18 4 31 13 5 23 64 29
    simpleHeapSort(s)
    print("Sorted sequence:\t", *s, "\n")    # Expected (but doesn't work): 2 4 5 10 13 18 23 29 31 51 64
