"""Code Fragment 5.10: Python code for performing insertion-sort on a list."""


def insertion_sort(A):
    """Sort list of comparable elements into nondecreasing order."""
    if len(A) > 1:
        for k in range(1, len(A)):          # From 1 to n-1.
            cur = A[k]                      # Current element to be inserted.
            j = k                           # Find correct index j for current.
            while j > 0 and A[j-1] > cur:   # If element before current is greater...
                A[j] = A[j-1]               # swap places.
                j -= 1
            A[j] = cur                      # Cur is now in the right place.
