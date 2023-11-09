# In-place heapsort by building a heap on a sequence, and extracting the root recursively.

def build_heap(seq):                                    # Time: O(n * log n) worst case
    """Build a heap out of the given sequence."""
    count = len(seq)
    for c in range(count):
        child = c + 1
        parent = child // 2
        verify_heap(seq, child, parent, c, count - 1)
    return seq

def swap(seq, k, j):                                    # Constant time/space operation: O(1)
    """Swap the elements at indices k and j in a given sequence."""
    temp = seq[k]
    seq[k] = seq[j]
    seq[j] = temp

def verify_heap(seq, child, parent, cur_ndx, end):      # Time: O(log n) worst case
    """Recursively verify the heap property given a sequence."""
    if cur_ndx <= end:
        if seq[child - 1] > seq[parent - 1]:
            swap(seq, child - 1, parent - 1)
            if (parent - 1) > 0:
                verify_heap(seq, child=parent, parent=parent // 2, cur_ndx=cur_ndx, end=end)

def extract_root(heap_seq):                             # Time: O(n * log n)
    """Extract the root from the heap and recursively reorganize the sequence."""
    curlen = len(heap_seq) - 1
    swap(heap_seq, 0, curlen)
    while curlen > 0:
        for i in range(curlen):
            child = i + 1
            parent = child // 2
            verify_heap(heap_seq, child, parent, i, curlen - 1)
        curlen -= 1
        swap(heap_seq, 0, curlen)

def heap_sort(the_seq):                                 # Time: θ(2(n * log n)) ∴ O(n * log n)
    """Sorts a sequence in ascending order using the heapsort."""
    assert len(the_seq) > 0, "Cannot sort empty sequence"
    build_heap(the_seq)
    extract_root(the_seq)
    return the_seq


# Short test
if __name__ == "__main__":
    A = [10,51,2,18,4,31,13,5,23,64,29]
    B = [4,8,15,16,23,42]
    C = [23,34,78,-1,6,90,343,5]
    D = [1,5,18,5,6,1,20]
    for s in A,B,C,D :                                   # For sequence A, we get...
        print("Original sequence:\t", *s,                # 10 51 2 18 4 31 13 5 23 64 29
          "\nHeap sequence:\t", *build_heap(s),          # 64 51 31 18 29 2 13 5 10 4 23
          "\nSorted sequence:\t", *heap_sort(s), "\n")   # 2 4 5 10 13 18 23 29 31 51 64
