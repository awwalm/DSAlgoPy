from Goodrich.Chapter7.positional_list import PositionalList
from Goodrich.Chapter9.heap_priority_queue import HeapPriorityQueue
from Goodrich.Chapter9.unsorted_priority_queue import UnsortedPriorityQueue
from Goodrich.Chapter9.sorted_priority_queue import SortedPriorityQueue


class PriorityQueue(HeapPriorityQueue, UnsortedPriorityQueue, SortedPriorityQueue):
    """Disposable/compact hybrid Priority Queue class."""
    ...

# Code Fragment 9.7: An implementation of the pq sort function, assuming an appropriate
# implementation of a PriorityQueue class. Note that each element of the input list C
# serves as its own key in the priority queue P.
def pq_sort(C: PositionalList):
    """Sort a collection of elements sorted in a positional list.\n
    * When P is sorted, pq_sort is akin to insertion sort, and runs at O(n^2).
    * When P is unsorted, pq_sort is akin to selection sort, and runs at O(n^2).
    * When P is heap-based, pq_sort is akin to heapsort, and runs at O(n log n).
    """
    n = len(C)
    P = PriorityQueue()
    for j in range(n):
        element = C.delete(C.first())
        P.add(element, element)             # Use element as key and value
    for j in range(n):
        k,v = P.remove_min()
        C.add_last(v)                       # Store smallest remaining element in C
