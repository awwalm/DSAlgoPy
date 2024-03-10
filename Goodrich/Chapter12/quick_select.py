"""Code Fragment 12.9: Randomized quick-select algorithm."""
import random
from typing import Sequence


def quick_select(S: Sequence, k):
    """Return the kth smallest element of the list S, for k from 1 to len(S)."""
    if len(S) == 1:
        return S[0]

    pivot = random.choice(S)                # Pick random pivot element from S

    L = [x for x in S if x < pivot]         # Elements less than pivot
    E = [x for x in S if x == pivot]        # Elements equal to pivot
    G = [x for x in S if pivot < x]         # Elements greater than pivot

    if k <= len(L):
        return quick_select(L, k)           # kth smallest lies in L
    elif k <= len(L) + len(E):
        return pivot                        # kth smallest equal to pivot
    else:
        j = k - len(L) - len(E)             # New selection parameter
        return quick_select(G, j)           # kth smallest is jth in G
