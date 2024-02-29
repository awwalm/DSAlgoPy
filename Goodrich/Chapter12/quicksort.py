"""Code Fragment 12.5: Quick-sort for a sequence S implemented as a queue."""
from Goodrich.Chapter7.linked_queue import LinkedQueue


def quick_sort(S: LinkedQueue):
    """Sort the elements of queue S using the quick-sort algorithm."""
    # BASE CASE
    n = len(S)
    if n < 2:
        return                          # List is already sorted

    # DIVIDE
    p = S.first()                       # Using first as arbitrary pivot
    L = LinkedQueue()                   # Elements less than p
    E = LinkedQueue()                   # Elements equal to p
    G = LinkedQueue()                   # Elements greater than p
    while not S.is_empty():             # Divide S into L, E, and G
        if S.first() < p:
            L.enqueue(S.dequeue())
        elif p < S.first():
            G.enqueue(S.dequeue())
        else:                           # S.first() must equal pivot
            E.enqueue(S.dequeue())

    # CONQUER (with recursion)
    quick_sort(L)                       # Sort elements less than p
    quick_sort(G)                       # Sort elements greater than p
    while not L.is_empty():             # Concatenate results
        S.enqueue(L.dequeue())
    while not E.is_empty():
        S.enqueue(E.dequeue())
    while not G.is_empty():
        S.enqueue((G.dequeue()))
