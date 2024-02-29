"""Code Fragment 12.3: An implementation of merge-sort using a basic queue."""
from Goodrich.Chapter7.linked_queue import LinkedQueue


def merge(S1: LinkedQueue, S2: LinkedQueue, S: LinkedQueue):
    """Merge two sorted queue instances S1 and S2 into empty queue S."""
    while not S1.is_empty() and not S2.is_empty():
        if S1.first() < S2.first():
            S.enqueue(S1.dequeue())
        else:
            S.enqueue(S2.dequeue())
    while not S1.is_empty():                            # Move remaining elements of S1 to S
        S.enqueue(S1.dequeue())
    while not S2.is_empty():                            # Move remaining elements of S2 to S
        S.enqueue(S2.dequeue())

def merge_sort(S: LinkedQueue):
    """Sort the elements of queue S using the merge-sort algorithm."""
    n = len(S)
    if n < 2:
        return                                          # List is already sorted

    # DIVIDE
    S1 = LinkedQueue()                                  # Or any other queue implementation
    S2 = LinkedQueue()
    while len(S1) < n//2:                               # Move the first n//2 elements to S1
        S1.enqueue(S.dequeue())
    while not S.is_empty():                             # Move the rest to S2
        S2.enqueue(S.dequeue())

    # CONQUER (with recursion)
    merge_sort(S1)                                      # Sort first half
    merge_sort(S2)                                      # Sort second half
    merge(S1, S2, S)                                    # Merge sorted halves back into S
